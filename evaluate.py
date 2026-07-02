#!/usr/bin/env python3
"""Automated ad grader — the evaluator half of an evaluator-optimizer loop.

A fresh model looks at each GENERATED image (the artifact a stranger actually meets) and
scores it against a fixed rubric, so "is this ad any good" stops being a purely manual call.
gen.py invokes this automatically after a generation run; it also runs standalone:

    python3 evaluate.py batches/blend.py --campaign sleep_wave2        # grade what's on disk
    python3 evaluate.py batches/blend.py --campaign sleep_wave2 --dry-run   # show the rubric prompt

Output: GRADES.md in the run folder + a printed pass/fail summary; failures are the reroll list.
The rubric below is the durable asset; GRADER_MODEL is a swappable constant (any Gemini
vision+text model — NOT the image-generation model gen.py uses).
"""
import sys, os, json, base64, ssl, re, urllib.request

from prompt_builder import CATEGORY   # the per-product category cue the comprehension check names

GRADER_MODEL = "gemini-2.5-flash"   # vision+text understanding model; configurable

# The rubric — each criterion is a real failure mode we've actually shipped (see the batch
# critique). Two families: RENDER faults (garbled text, invented labels, faint CTA) and
# DESIGN faults (hierarchy, proof placement, comprehension, trust-mark grouping). The design
# ones are why a technically-clean ad can still be a bad ad — the grader must catch both.
# Every criterion is phrased as a CONCRETE, observable yes/no a vision model can actually
# answer, not an abstract "is the hierarchy good" (that's vibes, not reproducible).
RUBRIC = [
    # ── Render faults ────────────────────────────────────────────────────────
    ("legible",          "All DESIGNED ad text (headline, subhead, chips, captions, CTA) is crisp and correctly spelled — no garbled, warped, doubled, or nonsense words. The product label's own fine print is naturally small and is NOT a legibility failure by itself (garbled or invented label text still fails under no_invented_text)."),
    ("product_present",  "The Alcami pouch/canister is clearly present and recognizable. Hero formats (scene/comparison/blocks/how_it_works): it should occupy roughly a third of the image height or more. Poster/UGC: simply present and legible is enough."),
    ("no_invented_text", "No invented brand names, fake company/legal lines, taglines, or garbled sub-labels anywhere (e.g. a made-up 'ACME CORP APS' line near the product)."),
    ("no_duplicate_claim","No trust mark or claim printed twice — e.g. '200,000+ customers' must not appear in two separate places."),
    ("cta_clear",        "If a call-to-action button is shown, it is a solid, legible, high-contrast element — never a faint, washed-out, or barely-visible pale shape. (If the ad intentionally has no CTA, pass.)"),
    ("clean_composition","Fills the square to all four edges; no floating disembodied hands/arms; no heavy unnatural single-color cast washing over a person's skin."),
    # ── Design faults (the ones a presence-only grader misses) ───────────────
    ("hook_supported",   "The intended headline text is present and readable, and the image supports it rather than contradicting it (e.g. an anti-coffee line should not show what looks like a cup of coffee as the hero)."),
    ("headline_dominant","The headline is the single largest, highest-contrast text element and is unmistakably the FIRST thing the eye lands on. FAIL if a star rating, a '200,000+ customers' line, a badge, a price, or any secondary element competes with or out-ranks the headline for first attention — or if no single element clearly dominates."),
    ("proof_not_orphaned","Star ratings and social-proof lines ('200,000+ customers', '4.9 stars') are integrated into a deliberate block beside related content — NOT floating alone in a top corner, above or apart from the headline, where they steal the prime first-glance slot. FAIL if a small proof line sits isolated in a top corner occupying the primary optical position."),
    ("comprehension",    "A first-time viewer who has never heard of the brand can tell WHAT the product is — {category} — and roughly WHY it answers the headline, from a legible category cue, ingredient cue, or one-line mechanism. FAIL if the ad is only a headline + a product + a CTA with no 'what it is / why it works': a package and a feeling is not enough."),
    ("trust_marks_grouped","Certification / trust marks (NSF, Third-party tested, 90-day guarantee, etc.) read as ONE compact strip, clearly subordinate to the headline and product. FAIL if they render as several separate equal-weight blocks competing with the main content, or are wedged into dead space between two unrelated elements (e.g. floating in the gap between the subhead and the CTA)."),
]


def _grade_prompt(ad: dict) -> str:
    fmt = ad.get("format", "scene")
    # UGC renders the native caption (text_in_image), NOT the hook — grade against what's
    # actually on the image, or a caption that trims the hook reads as a false "missing words" fault.
    if fmt == "ugc":
        hook = ad.get("text_in_image") or ad.get("hook", "")
    else:
        hook = ad.get("headline") or ad.get("hook", "")
    sub = ad.get("subhead", "")
    # The comprehension criterion names the product the ad actually sells — grading a tea ad
    # against "a latte" is the wrong answer, so the category comes from the ad's product_type.
    pt = ad.get("product_type", "tea")
    category = {"blend": f"a {CATEGORY['blend'].lower()} (a superfood coffee-alternative)",
                "tea":   f"an {CATEGORY['tea'].lower()} (a functional herbal tea)"}[pt if pt in ("blend", "tea") else "tea"]
    lines = [
        "You are a strict senior DTC art director reviewing ONE generated static ad (1:1) before it "
        "goes to a paying client. A junior laid out the elements; your job is to catch the design "
        "failures the client would reject — not just spelling and presence, but hierarchy, where the "
        "eye lands, whether a stranger understands the product, and whether trust marks are designed "
        "or just dumped in.",
        f"The ad's intended headline / hook is: \"{hook}\".",
    ]
    if sub:
        lines.append(f"The ad's intended subhead is: \"{sub}\".")
    lines += [
        f"The ad's format is: {fmt}.",
        "Judge ONLY what is visible in the image, as a first-time viewer who has never seen the brand. "
        "Picture it at thumbnail size in a fast-scrolling feed: for hierarchy, hook and comprehension, "
        "only what is readable at a 1.5-second glance counts — tiny print legible solely on close zoom "
        "(e.g. small text on the pouch) does NOT satisfy comprehension. "
        "Be strict — a genuine defect is a FAIL, not a pass. Do not give benefit of the doubt.",
        "Score each criterion pass/fail:",
    ]
    for key, desc in RUBRIC:
        lines.append(f"- {key}: {desc.format(category=category) if '{category}' in desc else desc}")
    lines.append(
        "overall_pass is FALSE if ANY criterion fails — there is no partial credit, a single real "
        "design or render defect fails the ad.\n"
        'Respond with ONLY a JSON object, no prose:\n'
        '{"criteria": {"<key>": {"pass": true|false, "reason": "<short>"}, ...}, '
        '"overall_pass": true|false, "worst_issue": "<the single most important problem, or none>"}'
    )
    return "\n".join(lines)


def _parse_verdict(text: str) -> dict:
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return {"overall_pass": None, "worst_issue": "no JSON in grader response", "criteria": {}}
    try:
        return json.loads(m.group(0))
    except Exception as e:
        return {"overall_pass": None, "worst_issue": f"unparseable grader JSON: {e}", "criteria": {}}


def grade_image(image_path: str, ad: dict, api_key: str, ctx) -> dict:
    """Grade one image. Returns the verdict dict (overall_pass may be None on a grader error
    — e.g. no API balance — so the caller degrades gracefully instead of crashing)."""
    try:
        img_b64 = base64.b64encode(open(image_path, "rb").read()).decode()
        payload = json.dumps({
            "contents": [{"parts": [
                {"text": _grade_prompt(ad)},
                {"inlineData": {"mimeType": "image/png", "data": img_b64}},
            ]}],
            "generationConfig": {"responseModalities": ["TEXT"], "temperature": 0.0},
        }).encode()
        url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
               f"{GRADER_MODEL}:generateContent?key={api_key}")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        resp = urllib.request.urlopen(req, timeout=120, context=ctx)
        body = json.loads(resp.read())
        text = "".join(p.get("text", "")
                       for p in body.get("candidates", [{}])[0].get("content", {}).get("parts", []))
        return _parse_verdict(text)
    except Exception as e:
        return {"overall_pass": None, "worst_issue": f"grader unavailable: {str(e)[:80]}", "criteria": {}}


def grade_campaign(out_dir, ads_by_file: dict, files: list, api_key: str, ctx) -> dict:
    """Grade each generated file, write GRADES.md, return {file: verdict}. `ads_by_file`
    maps filename -> spec; `files` is the list to grade (typically this run's successes)."""
    verdicts = {}
    for fn in files:
        ad = ads_by_file.get(fn, {})
        path = os.path.join(str(out_dir), fn)
        if not os.path.exists(path):
            continue
        verdicts[fn] = grade_image(path, ad, api_key, ctx)
    _write_report(out_dir, ads_by_file, verdicts)
    return verdicts


def _write_report(out_dir, ads_by_file, verdicts):
    L = ["# Ad grades", "", f"_{GRADER_MODEL} · {len(verdicts)} graded_", ""]
    for fn, v in verdicts.items():
        op = v.get("overall_pass")
        mark = "✓ PASS" if op is True else ("✗ FAIL" if op is False else "… ungraded")
        L.append(f"## {mark} — {fn}")
        if v.get("worst_issue") and op is not True:
            L.append(f"- **worst issue:** {v['worst_issue']}")
        for key, c in (v.get("criteria") or {}).items():
            if isinstance(c, dict) and c.get("pass") is False:
                L.append(f"- ✗ {key}: {c.get('reason','')}")
        L.append("")
    with open(os.path.join(str(out_dir), "GRADES.md"), "w") as f:
        f.write("\n".join(L))


def summarize(verdicts: dict) -> tuple:
    """Return (passed, failed, ungraded) filename lists."""
    passed = [f for f, v in verdicts.items() if v.get("overall_pass") is True]
    failed = [f for f, v in verdicts.items() if v.get("overall_pass") is False]
    ungraded = [f for f, v in verdicts.items() if v.get("overall_pass") is None]
    return passed, failed, ungraded


# ── Standalone CLI ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import importlib.util
    ROOT = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) < 2 or "--campaign" not in sys.argv:
        print("usage: python3 evaluate.py <batch.py> --campaign <name> [--dry-run]")
        sys.exit(1)
    batch_path = sys.argv[1]
    campaign = sys.argv[sys.argv.index("--campaign") + 1]
    dry = "--dry-run" in sys.argv
    spec = importlib.util.spec_from_file_location("b", batch_path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    camp = m.CAMPAIGNS[campaign]
    aud = camp.get("audience", "acquisition")
    ads = camp.get("ads", [])
    for a in ads:
        a.setdefault("audience", aud)
    ads_by_file = {a["file"]: a for a in ads}
    # Folder resolution mirrors gen.py exactly: the pinned run_id, else the positional
    # fallback {product}_{audience}_batch{N} — so standalone grading finds the same folder.
    run_id = camp.get("run_id") or (
        f"{os.path.basename(batch_path).rsplit('.', 1)[0].lstrip('_')}_{aud}_batch"
        f"{list(m.CAMPAIGNS).index(campaign) + 1}")
    out_dir = os.path.join(ROOT, "ad-workspace", run_id)

    if dry:
        print("── grader prompt for the first ad (no API call) ──\n")
        print(_grade_prompt(ads[0]))
        sys.exit(0)

    # load API key the same way gen.py does
    env = {}
    envp = os.path.join(ROOT, ".env")
    if os.path.exists(envp):
        for line in open(envp):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    api_key = env.get("GEMINI_API_KEY", "")
    # TLS matches gen.py: verification off unless GEMINI_VERIFY_SSL=1 (this environment's
    # Python lacks system CA certs).
    ctx = ssl.create_default_context()
    if env.get("GEMINI_VERIFY_SSL") != "1":
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    files = sorted(f for f in os.listdir(out_dir) if f.endswith(".png")) if os.path.isdir(out_dir) else []
    verdicts = grade_campaign(out_dir, ads_by_file, files, api_key, ctx)
    p, f, u = summarize(verdicts)
    print(f"\n  graded {len(verdicts)}:  ✓ {len(p)} pass   ✗ {len(f)} fail   … {len(u)} ungraded")
    if f:
        print(f"  reroll: {', '.join(f)}")
    print(f"  → {out_dir}/GRADES.md")
