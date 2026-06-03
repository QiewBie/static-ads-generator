#!/usr/bin/env python3
"""
Alcami Ad Generator — universal engine.

Every batch file defines a CAMPAIGNS dict; pick one with --campaign.

Usage:
  python3 gen.py --policy                              print format/archetype/audience matrix
  python3 gen.py <batch.py>                            list campaigns in the batch
  python3 gen.py <batch.py> --campaign <name>          run a campaign (skips existing outputs)
  python3 gen.py <batch.py> --campaign <name> --force  re-run everything, overwrite existing
  python3 gen.py <batch.py> --campaign <name> --only 01 03   run only ads with these filename prefixes
  python3 gen.py <batch.py> --campaign <name> --dry-run      preview prompts, no API calls

Examples:
  python3 gen.py batches/tea.py --campaign retarget_v6 --dry-run
  python3 gen.py batches/blend.py --campaign main_v2
"""

import sys, json, os, time, base64, ssl, shutil, subprocess, importlib.util, urllib.request
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

# Stream output live even when piped/redirected, so progress and errors are visible
# instead of block-buffered until the process exits.
try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

# Image model + automatic fallback. The pro tier has the best text fidelity; when it is
# rate-limited (429 / quota), the run falls back to flash automatically so a single
# exhausted quota doesn't wall the whole batch.
PRIMARY_MODEL  = "gemini-3-pro-image"
FALLBACK_MODEL = "gemini-3.1-flash-image-preview"
MODELS = [PRIMARY_MODEL, FALLBACK_MODEL]


def load_env(path=".env") -> dict:
    """Parse .env into a dict — tolerant of ordering, comments, quotes, blank lines."""
    env = {}
    p = PROJECT_ROOT / path
    if not p.exists():
        return env
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


# ── Policy command — print the single source of truth and exit ─────────────────

if "--policy" in sys.argv:
    sys.path.insert(0, str(PROJECT_ROOT))
    from prompt_builder import print_policy
    print_policy()
    sys.exit(0)

# ── Load batch config ─────────────────────────────────────────────────────────

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

batch_path = Path(sys.argv[1]).resolve()
if not batch_path.exists():
    print(f"Error: batch file not found: {batch_path}")
    sys.exit(1)

spec  = importlib.util.spec_from_file_location("batch", batch_path)
batch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch)

# ── Parse CLI flags ───────────────────────────────────────────────────────────

flags   = sys.argv[2:]
force   = "--force" in flags
dry_run = "--dry-run" in flags
only: list = []
if "--only" in flags:
    idx  = flags.index("--only")
    only = [f for f in flags[idx + 1:] if not f.startswith("--")]

# ── Load the campaign ──────────────────────────────────────────────────────────
# Every batch file defines a CAMPAIGNS dict; pick one with --campaign <name>.

CAMPAIGNS = getattr(batch, "CAMPAIGNS", None)
if CAMPAIGNS is None:
    print(f"Error: {sys.argv[1]} has no CAMPAIGNS dict.")
    sys.exit(1)

campaign_name = None
if "--campaign" in flags:
    idx = flags.index("--campaign")
    remaining = [f for f in flags[idx + 1:] if not f.startswith("--")]
    if remaining:
        campaign_name = remaining[0]

if not campaign_name:
    print("Available campaigns:")
    for name in CAMPAIGNS:
        print(f"  {name}")
    print(f"\nRun: python3 gen.py {sys.argv[1]} --campaign <name>")
    sys.exit(0)

if campaign_name not in CAMPAIGNS:
    print(f"Error: campaign '{campaign_name}' not found.")
    print(f"Available: {', '.join(CAMPAIGNS.keys())}")
    sys.exit(1)

campaign = CAMPAIGNS[campaign_name]
raw_ads = campaign.get("ads", [])

# Stamp the campaign's audience onto each ad (ads may override). Audience is a
# field read by the validator — not a separate file.
camp_audience = campaign.get("audience", "acquisition")
for a in raw_ads:
    a.setdefault("audience", camp_audience)

# ── Output folder name: {product}_{audience}_batch{N} ──────────────────────────
# DETERMINISTIC — the same campaign always maps to the same folder, so a retry
# reuses it instead of spawning a new timestamped husk each time.
#   product  ← batch filename (blend.py → "blend", tea.py → "tea")
#   audience ← the campaign's audience
#   N        ← the campaign's 1-based position in this file's CAMPAIGNS
if campaign.get("run_id"):
    RUN_ID = campaign["run_id"]                     # explicit override still honored
else:
    product   = batch_path.stem.lstrip("_")         # "blend" / "tea" / "template"
    batch_num = list(CAMPAIGNS).index(campaign_name) + 1
    RUN_ID    = f"{product}_{camp_audience}_batch{batch_num}"

sys.path.insert(0, str(PROJECT_ROOT))
from prompt_builder import build_prompt, get_refs_for_campaign, get_ad_refs, validate_campaign

# ── Validate specs before doing anything else ──
val_errors, val_warnings = validate_campaign(raw_ads)
if val_warnings:
    print("\n  ⚠  WARNINGS:")
    for w in val_warnings:
        print(f"     · {w}")
if val_errors:
    print("\n  ✗  ERRORS:")
    for e in val_errors:
        print(f"     · {e}")
    if not dry_run:
        print("\n  Generation blocked — fix the errors above, or use --dry-run to preview anyway.\n")
        sys.exit(1)

REFS = get_refs_for_campaign(raw_ads)
ADS = [{
    "file":   ad_spec["file"],
    "refs":   get_ad_refs(ad_spec),
    "prompt": build_prompt(ad_spec),
} for ad_spec in raw_ads]

if only:
    ADS = [ad for ad in ADS if any(ad["file"].startswith(o) for o in only)]

if not ADS:
    print("No ads matched. Check your --only filter or ADS list.")
    sys.exit(0)

# ── Paths & API setup ─────────────────────────────────────────────────────────

os.chdir(PROJECT_ROOT)
ENV = load_env()
api_key = ENV.get("GEMINI_API_KEY")
if not api_key and not dry_run:
    print("Error: GEMINI_API_KEY not found in .env")
    sys.exit(1)
OUT      = PROJECT_ROOT / "ad-workspace" / RUN_ID
REFS_DIR = OUT / "references"
# Touch nothing on disk during a dry-run — only create the folder when generating.
if not dry_run:
    os.makedirs(REFS_DIR, exist_ok=True)

def _api_url(model: str) -> str:
    return ("https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent?key=" + (api_key or ""))

# TLS: this environment's Python lacks system CA certs, so verification is OFF by
# default (matches the working setup). Set GEMINI_VERIFY_SSL=1 to turn it on.
CTX = ssl.create_default_context()
if ENV.get("GEMINI_VERIFY_SSL") != "1":
    CTX.check_hostname = False
    CTX.verify_mode    = ssl.CERT_NONE

# ── Prepare reference images ──────────────────────────────────────────────────
# sips only runs if the cached resized version doesn't already exist.
# Skipped entirely in dry-run — a preview should write nothing to disk.

loaded: dict = {}
print()
for key, src in ({} if dry_run else REFS).items():
    dst = REFS_DIR / f"{key}.png"
    src_path = PROJECT_ROOT / src
    if not dst.exists():
        subprocess.run(
            ["sips", "-Z", "1024", str(src_path), "--out", str(dst)],
            capture_output=True
        )
        tag = "resized"
    else:
        tag = "cached"
    with open(dst, "rb") as f:
        loaded[key] = base64.b64encode(f.read()).decode()
    print(f"  ref [{tag}]: {key}")

# ── Generation function ───────────────────────────────────────────────────────

def gen(prompt: str, ref_keys: list, fname: str, delay: int = 15):
    """Generate one image. Tries the primary model, and on a 429/quota switches to the
    fallback model instead of burning the full backoff on an exhausted quota.
    Returns (ok, kb, model_used)."""
    parts = [{"text": prompt}]
    for key in ref_keys:
        if key not in loaded:
            print(f"      ✗ ref key '{key}' not found in REFS — check your batch file")
            return False, 0, None
        parts.append({"inlineData": {"mimeType": "image/png", "data": loaded[key]}})

    payload = json.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {"aspectRatio": "1:1"}
        }
    }).encode()

    for mi, model in enumerate(MODELS):
        is_last_model = mi == len(MODELS) - 1
        if mi > 0:
            print(f"      ↪ falling back to {model}")
        for attempt in range(1, 4):
            try:
                req  = urllib.request.Request(
                    _api_url(model), data=payload,
                    headers={"Content-Type": "application/json"}
                )
                resp = urllib.request.urlopen(req, timeout=180, context=CTX)
                body = json.loads(resp.read())
                for part in (body.get("candidates", [{}])[0]
                                 .get("content", {}).get("parts", [])):
                    if "inlineData" in part:
                        img = base64.b64decode(part["inlineData"]["data"])
                        with open(OUT / fname, "wb") as f:
                            f.write(img)
                        time.sleep(delay)
                        return True, len(img) // 1024, model
                    elif "text" in part:
                        print(f"      model: {part['text'][:80]}")
                print(f"      [{model}] attempt {attempt}: no image in response")
            except Exception as e:
                msg = str(e)
                print(f"      [{model}] attempt {attempt}: {msg[:80]}")
                if "429" in msg or "quota" in msg.lower():
                    # Rate-limited: jump to the next model rather than waiting out the
                    # full backoff on a quota that's likely exhausted. Only sleep if
                    # there's no fallback left to try.
                    if not is_last_model:
                        break
                    print("      rate limited — waiting 60s")
                    time.sleep(60)
                elif attempt < 3:
                    time.sleep(10)
    return False, 0, None

# ── Run ───────────────────────────────────────────────────────────────────────

label = "  [DRY RUN]" if dry_run else ""
print(f"\n→ {OUT}  ({len(ADS)} ads){label}\n")

results = []
consec_fail = 0
for i, ad in enumerate(ADS, 1):
    fname    = ad["file"]
    out_path = OUT / fname
    prefix   = f"  [{i}/{len(ADS)}]"

    if not force and out_path.exists():
        kb = out_path.stat().st_size // 1024
        print(f"{prefix} {fname}  ↩ skipped ({kb}KB, use --force to overwrite)")
        results.append({"file": fname, "status": "skipped", "kb": kb})
        continue

    print(f"{prefix} {fname}")

    if dry_run:
        print(f"      refs: {ad['refs']}")
        prompt_preview = ad['prompt']
        # Show full assembled prompt in campaign mode so it can be reviewed before generation
        if CAMPAIGNS is not None:
            print(f"      --- ASSEMBLED PROMPT ---")
            for line in prompt_preview.strip().split("\n"):
                print(f"      {line}")
            print(f"      --- END PROMPT ---")
        else:
            print(f"      prompt: {prompt_preview[:120].strip()}...")
        results.append({"file": fname, "status": "dry-run"})
        continue

    ok, kb, model = gen(ad["prompt"], ad["refs"], fname)
    if ok:
        consec_fail = 0
        via = "" if model == PRIMARY_MODEL else f"  [via fallback: {model}]"
        print(f"      ✓ {kb}KB{via}")
        results.append({"file": fname, "status": "ok", "kb": kb, "model": model})
    else:
        consec_fail += 1
        print(f"      ✗ FAILED")
        results.append({"file": fname, "status": "failed", "kb": 0})
        if consec_fail >= 3:
            print("\n  ✗ Aborting after 3 consecutive failures (likely rate limit / exhausted "
                  "quota). Re-run later, or check your GEMINI_API_KEY quota.")
            break

# ── Summary ───────────────────────────────────────────────────────────────────

ok_list      = [r for r in results if r["status"] == "ok"]
failed_list  = [r for r in results if r["status"] == "failed"]
skipped_list = [r for r in results if r["status"] == "skipped"]

print(f"\n{'─' * 52}")
print(f"  ✓ {len(ok_list)} generated   ↩ {len(skipped_list)} skipped   ✗ {len(failed_list)} failed")
if failed_list:
    print(f"  Failed: {', '.join(r['file'] for r in failed_list)}")

# ── Clean up empty/orphan output ───────────────────────────────────────────────
# If this run produced no images and none already exist, the folder is a husk —
# remove it (incl. its references cache) so failed runs don't leave empty dirs.
existing_pngs = [p for p in OUT.glob("*.png")]
if not dry_run and not existing_pngs:
    shutil.rmtree(OUT, ignore_errors=True)
    print(f"  (removed empty folder — nothing generated)\n")
else:
    print(f"  → {OUT}/\n")

# ── Save run log ──────────────────────────────────────────────────────────────

if not dry_run and existing_pngs:
    log = {
        "run_id":     RUN_ID,
        "batch_file": str(batch_path),
        "timestamp":  datetime.now().isoformat(),
        "total":      len(results),
        "ok":         len(ok_list),
        "skipped":    len(skipped_list),
        "failed":     len(failed_list),
        "results":    results,
    }
    with open(OUT / "run_log.json", "w") as f:
        json.dump(log, f, indent=2)
