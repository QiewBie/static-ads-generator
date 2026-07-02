#!/usr/bin/env python3
"""Pipeline contract tests — run `python3 tests/test_pipeline.py` (or `make check`).

Three guards that turn the ad-hoc verification into an enforced contract:
  1. VALIDATION   — every campaign validates with ZERO errors (warnings are fine).
  2. GOLDEN       — assembled prompts match tests/golden_prompts.sha. After a *deliberate*
                    engine change, regenerate with `--update` (or `make update-golden`).
                    This catches accidental assembly drift no one meant to ship.
  3. FACTS        — CLAUDE.md <-> engine consistency: every literal the engine renders
                    (prices, the customer count, caffeine-free, competitor names) must also
                    be stated in CLAUDE.md, so the engine and CLAUDE.md can never silently drift.

Exit 0 = all pass; exit 1 = a failure (CI-friendly).
"""
import sys, os, hashlib, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import prompt_builder as pb
import pb_validate as pv

BATCH_FILES = ["batches/blend.py", "batches/tea.py"]
GOLDEN = os.path.join(ROOT, "tests", "golden_prompts.sha")


def _load_campaigns(path):
    spec = importlib.util.spec_from_file_location("b_" + path.replace("/", "_"), os.path.join(ROOT, path))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.CAMPAIGNS


def _all_ads():
    """Yield (batch_file, campaign, ad-with-audience-stamped) for every spec — exactly the
    audience-stamping gen.py applies, so the test sees what the real run sees."""
    for bf in BATCH_FILES:
        for cname, camp in _load_campaigns(bf).items():
            aud = camp.get("audience", "acquisition")
            for ad in camp.get("ads", []):
                a = dict(ad)
                a.setdefault("audience", aud)
                yield bf, cname, a


# ── 1. validation ───────────────────────────────────────────────────────────────
def check_validation():
    fails = []
    for bf in BATCH_FILES:
        for cname, camp in _load_campaigns(bf).items():
            ads = camp.get("ads", [])
            aud = camp.get("audience", "acquisition")
            for a in ads:
                a.setdefault("audience", aud)
            errors, _ = pv.validate_campaign(ads)
            fails += [f"{bf}::{cname}: {e}" for e in errors]
    return fails


# ── 2. golden prompts ───────────────────────────────────────────────────────────
def _prompt_hashes():
    out = {}
    for bf, cname, a in _all_ads():
        key = f"{bf}::{cname}::{a.get('file')}"
        try:
            p = pb.build_prompt(a)
        except Exception as e:
            p = f"<<ERR {type(e).__name__}: {e}>>"
        out[key] = hashlib.sha256(p.encode()).hexdigest()
    return out


def _read_golden():
    golden = {}
    if not os.path.exists(GOLDEN):
        return None
    for line in open(GOLDEN):
        line = line.rstrip("\n")
        if not line:
            continue
        h, k = line.split("  ", 1)
        golden[k] = h
    return golden


def check_golden(update=False):
    cur = _prompt_hashes()
    if update:
        with open(GOLDEN, "w") as f:
            for k in sorted(cur):
                f.write(f"{cur[k]}  {k}\n")
        print(f"  updated golden ({len(cur)} prompts)")
        return []
    golden = _read_golden()
    if golden is None:
        return ["no golden file — run: python3 tests/test_pipeline.py --update"]
    fails = []
    for k in sorted(set(cur) | set(golden)):
        if k not in golden:
            fails.append(f"NEW prompt not in golden: {k}")
        elif k not in cur:
            fails.append(f"prompt REMOVED vs golden: {k}")
        elif cur[k] != golden[k]:
            fails.append(f"prompt CHANGED vs golden: {k}  (intentional? `make update-golden`)")
    return fails


# ── 3. fact consistency (the drift detector) ──────────────────────────────────────
def check_facts():
    claude = open(os.path.join(ROOT, "CLAUDE.md")).read()
    low = claude.lower()
    fails = []
    for pt, anchor in pb.PRICES.items():
        num = anchor.replace("From ", "").split("/")[0]          # "$39" / "$37.40"
        if num not in claude:
            fails.append(f"engine PRICES['{pt}'] = '{anchor}' but '{num}' is absent from CLAUDE.md")
    if "200,000" not in claude:
        fails.append("engine renders the '200,000+' customer count, but it's absent from CLAUDE.md")
    if "caffeine-free" not in low and "caffeine free" not in low:
        fails.append("engine guards a caffeine-free claim, but CLAUDE.md never states it as fact")
    # Only render-capable rivals (those the engine can put in a comparison ad) must be named
    # in CLAUDE.md; intel-only brands live in competitors.py + research, not the always-loaded file.
    for cid, c in pb.COMPETITORS.items():
        if c.get("ref_path") and c["name"] not in claude:
            fails.append(f"engine COMPETITORS['{cid}'] = '{c['name']}' is render-capable but not named in CLAUDE.md")
    return fails


def main():
    if "--update" in sys.argv:
        check_golden(update=True)
        return 0
    # `--invariants`: only the checks that must ALWAYS hold (validation + facts) — used by
    # the enforcement hook. The golden check is omitted because it is intentionally volatile
    # during development (it fails on every deliberate prompt change until `make update-golden`).
    invariants_only = "--invariants" in sys.argv
    checks = [("validation — every campaign 0 errors", check_validation),
              ("facts — CLAUDE.md <-> engine consistent", check_facts)]
    if not invariants_only:
        checks.insert(1, ("golden — assembled prompts unchanged", check_golden))
    print("Pipeline " + ("invariants" if invariants_only else "contract tests") + "\n")
    all_fails = []
    for name, fn in checks:
        fails = fn()
        print(f"  {'✓' if not fails else '✗'} {name}" + (f"   [{len(fails)}]" if fails else ""))
        for f in fails[:25]:
            print(f"      · {f}")
        all_fails += fails
    print("\nPASS ✓" if not all_fails else f"\nFAIL ✗  ({len(all_fails)} issue(s))")
    return 0 if not all_fails else 1


if __name__ == "__main__":
    sys.exit(main())
