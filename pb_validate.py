"""Spec validation for the Alcami ad pipeline.

Split out from prompt_builder so the engine (data + prompt assembly) and the
rule-enforcement layer are separate concerns. Warnings always print; errors block
real generation (not --dry-run). Imports one-directionally from the engine — no cycle.
"""

import os
import re

from prompt_builder import (
    VALID_FORMATS, COMPETITORS, TEA_SKUS, BLEND_SKUS,
    CTA_STYLES, BLOCK_STYLES, DESIGN_ARCHETYPES, AUDIENCE_POLICY,
    SOCIAL_PROOF_VISUALS, TYPE_PERSONALITIES, EMPHASIS_TREATMENTS, LEVERS,
    UGC_CAPTURE_MODES, ART_STYLES,
    _stopwords, _default_archetype, _competitor, _social_proof_on, _is_photographic,
    _PROJECT_ROOT, _STYLE_TO_ARCHETYPE,
    build_prompt, _NON_PHOTOGRAPHIC_ARCHETYPES,
)
from brand_facts import PRICES, BLEND_PRICE_TOKEN, TEA_PRICE_TOKEN, CUSTOMER_COUNT_NUM


# Rival BRANDS may be named in creative (people/celebrities never). When one appears
# in rendered text the validator reminds that comparative claims carry obligations:
# true, parallel, substantiated — and a rival's mark is shown by form factor + name,
# never a distorted logo. Distinctive names only, to avoid false positives on common words.
COMPETITOR_NAMES = (
    "ryze", "mudwtr", "mud\\wtr", "mud wtr", "everyday dose", "four sigmatic",
    "im8", "cymbiotika", "ag1", "athletic greens",
)

# Prescription drug brands NEVER appear in creative — the class term ("GLP-1") is the
# only sayable reference, and only as third-person product-fit positioning ("The GLP-1
# ritual"), never a second-person status assumption ("On GLP-1?"). Hard error on these.
DRUG_BRAND_NAMES = (
    "ozempic", "wegovy", "mounjaro", "zepbound", "rybelsus", "saxenda",
    "semaglutide", "tirzepatide", "liraglutide",
)

# Hook openers that waste the 1-2s cold read (CLAUDE.md hook rules). A scroller can't
# decode a jargon word or care about an ingredient name before the outcome — these may
# SUPPORT a hook but never OPEN it. Detected only at the hook's opening, not anywhere.
JARGON_OPENERS = (
    "adaptogenic", "adaptogen", "adaptogens", "circadian", "bioavailability",
    "bioavailable", "nootropic", "nootropics", "mitochondrial", "parasympathetic",
    "neuroplasticity", "cortisol",
)
INGREDIENT_OPENERS = (
    "lion's mane", "lions mane", "reishi", "cordyceps", "guayusa", "polygala",
    "astragalus", "he shou wu", "shilajit", "gynostemma", "mucuna", "chamomile",
    "lavender", "butterfly pea", "moringa", "lemon verbena",
)

# Problem/negative words. The gold focal anchor should carry the OUTCOME, not gild the
# villain — gold on "foggy"/"crash" misplaces the eye's anchor (a strike-through on the
# same word is fine — that's negating it). Checked only against `gold` emphasis.
VILLAIN_WORDS = {
    "foggy", "fog", "crazy", "jitters", "jittery", "crash", "crashing", "crashes",
    "anxious", "anxiety", "tired", "exhausted", "worse", "bad", "wired", "shaking",
    "shake", "stress", "stressed", "burnout", "groggy", "drained", "sluggish", "restless",
}

# Fields whose text is actually RENDERED in the creative (vs. art-direction notes
# like `scene`/`visual_action` that only guide the model and are never drawn).
def _rendered_texts(ad: dict) -> list:
    out = []
    if ad.get("hook"):           out.append(("hook", ad["hook"]))
    if ad.get("headline"):       out.append(("headline", ad["headline"]))
    if ad.get("subhead"):        out.append(("subhead", ad["subhead"]))
    if ad.get("text_in_image"):  out.append(("text_in_image", ad["text_in_image"]))
    if ad.get("corner_stamp"):   out.append(("corner_stamp", ad["corner_stamp"]))
    # `proof` and `stats` are rendering aliases (see _chips) — BOTH are rendered text,
    # so both pass through every claim guard.
    for fld in ("stats", "proof"):
        for i, st in enumerate(ad.get(fld) or []):
            out.append((f"{fld}[{i}]", str(st)))
    for side in ("left", "right"):
        sd = ad.get("sides", {}).get(side, {})
        if sd.get("label"):
            out.append((f"sides.{side}.label", sd["label"]))
        for p in sd.get("points", []):
            out.append((f"sides.{side}", p))
    for i, it in enumerate(ad.get("items", [])):
        if isinstance(it, dict):
            out.append((f"items[{i}]", f"{it.get('label','')} {it.get('note','')}"))
        else:
            out.append((f"items[{i}]", str(it)))
    for i, b in enumerate(ad.get("blocks", [])):
        out.append((f"blocks[{i}]", b.get("content", "")))
    for i, s in enumerate(ad.get("steps", [])):
        out.append((f"steps[{i}]", f"{s.get('label','')} {s.get('detail','')}"))
    return out



def validate_spec(ad: dict) -> tuple:
    """Return (errors, warnings) for one ad spec. Errors should block generation."""
    errors, warnings = [], []
    fid = ad.get("file", "<no file>")
    pt = ad.get("product_type", "tea")
    sku = ad.get("sku", "")
    fmt = ad.get("format", "scene")

    # ── Required core fields ──
    for field in ("file", "sku", "product_type", "format", "hook"):
        if not ad.get(field):
            errors.append(f"{fid}: missing required field '{field}'")

    if fmt not in VALID_FORMATS:
        errors.append(f"{fid}: unknown format '{fmt}' (use {sorted(VALID_FORMATS)})")

    valid_skus = TEA_SKUS if pt == "tea" else BLEND_SKUS
    if sku and sku not in valid_skus:
        errors.append(f"{fid}: sku '{sku}' invalid for product_type '{pt}'")

    # Blend creative ships with the ORIGINAL pouch only (the site consolidates to the
    # single Original flavor) — another pouch is a deliberate exception, never a default.
    if pt == "blend" and sku in ("matcha", "cacao", "espresso"):
        warnings.append(f"{fid}: blend ads use the ORIGINAL pouch only (single-flavor site); "
                        f"sku '{sku}' is off-catalog for creative — keep only if deliberately approved.")

    comp_key = ad.get("competitor")
    if comp_key:
        if comp_key not in COMPETITORS:
            errors.append(f"{fid}: competitor '{comp_key}' unknown (use {sorted(COMPETITORS)})")
        elif not COMPETITORS[comp_key].get("ref_path"):
            capable = sorted(k for k, v in COMPETITORS.items() if v.get("ref_path"))
            errors.append(f"{fid}: competitor '{comp_key}' is intel-only (no comparison asset) — only "
                          f"render-capable rivals {capable} can anchor a comparison ad.")

    # ── Format-specific required fields ──
    if fmt == "scene" and not (ad.get("scene") and ad.get("visual_action")):
        errors.append(f"{fid}: scene format needs both 'scene' and 'visual_action'")
    if fmt == "comparison":
        l = ad.get("sides", {}).get("left", {}).get("points", [])
        r = ad.get("sides", {}).get("right", {}).get("points", [])
        if not l or not r:
            errors.append(f"{fid}: comparison needs sides.left.points and sides.right.points")
        elif len(l) != len(r):
            errors.append(f"{fid}: comparison row counts differ (left {len(l)} vs right {len(r)}) — rows must be parallel")
    if fmt == "blocks" and not ad.get("blocks") and not ad.get("items"):
        errors.append(f"{fid}: blocks format needs an 'items' list (recommended) or a free-form 'blocks' list")
    if fmt == "blocks" and ad.get("blocks") and ad.get("items") is None:
        warnings.append(f"{fid}: uses the free-form 'blocks' list — prefer the 'items' copy/layout-split path (cleaner design, avoids document-look). Both render through one builder.")
    if fmt == "ugc" and not all(ad.get(k) for k in ("person", "moment", "environment")):
        errors.append(f"{fid}: ugc format needs 'person', 'moment', 'environment'")
    if fmt == "how_it_works":
        steps = ad.get("steps", [])
        if not steps:
            errors.append(f"{fid}: how_it_works needs a 'steps' list")
        elif len(steps) > 4:
            warnings.append(f"{fid}: {len(steps)} steps — keep how_it_works to 3-4 max")

    # ── ugc renders no designed text layer — warn on set-but-ignored structured fields ──
    if fmt == "ugc":
        for f in ("headline", "subhead", "stats", "proof", "emphasis"):
            if ad.get(f):
                warnings.append(f"{fid}: '{f}' is set but ugc renders no designed text — it will be ignored. Put copy in 'hook' / 'text_in_image'.")
        if ad.get("cta_style") not in (None, "none"):
            warnings.append(f"{fid}: ugc with a visible in-image CTA ('{ad.get('cta_style')}') — a designed "
                            f"button breaks the real-person's-post illusion. Keep the CTA in the ad copy; "
                            f"set cta_style 'none'.")
        cm = ad.get("capture_mode")
        if cm and cm not in UGC_CAPTURE_MODES:
            warnings.append(f"{fid}: unknown capture_mode '{cm}' (use {sorted(UGC_CAPTURE_MODES)}) — "
                            f"the builder will fall back to rotating one.")
        # Capture framing belongs to `capture_mode` (the engine rotates it). Framing baked
        # into person/moment/environment prose can contradict the rotated capture line.
        if not cm:
            free = " ".join(str(ad.get(k, "")) for k in ("person", "moment", "environment")).lower()
            if any(w in free for w in ("selfie", "arm's length", "arms length", "front-facing", "front facing")):
                warnings.append(f"{fid}: ugc prose dictates the camera framing (selfie / arm's length / "
                                f"front-facing) but no capture_mode is pinned — the engine rotates a capture "
                                f"mode that may contradict it. Move framing into capture_mode, or pin one.")

    # ── Portfolio lever + 3-part creative rationale (optional strategic layer) ──
    # Both are meta-fields — never injected into the image prompt, only read for the
    # batch BRIEF.md. Warn only when present-but-malformed; absence is fine.
    lever = ad.get("lever")
    if lever and lever not in LEVERS:
        warnings.append(f"{fid}: lever '{lever}' is not a known buyer-psych lever (use {sorted(LEVERS)}).")
    rat = ad.get("rationale")
    if rat is not None:
        if not isinstance(rat, dict):
            warnings.append(f"{fid}: 'rationale' should be a dict of 'angle' / 'format' / 'design' lines.")
        else:
            missing = [k for k in ("angle", "format", "design") if not rat.get(k)]
            if missing:
                warnings.append(f"{fid}: rationale missing {missing} — justify message (angle), structure (format), standout (design).")

    # ── Hook quality ──
    hook = (ad.get("hook") or "").strip()
    if hook:
        if len(hook.split()) < 3:
            warnings.append(f"{fid}: hook is very short — may be a fragment: '{hook}'")
        if hook[-1] not in ".?!":
            warnings.append(f"{fid}: hook doesn't end with . ? ! — may be a fragment: '{hook}'")
        # Opener checks: a jargon word or an ingredient name in the FIRST 1-3 words wastes
        # the cold read (CLAUDE.md: "No jargon as the hook" / ingredient names aren't hooks).
        tokens = [t for t in re.split(r"[^a-z']+", hook.lower()) if t]
        if tokens and tokens[0] in ("the", "a", "an"):
            tokens = tokens[1:]
        opener1 = tokens[0] if tokens else ""
        opener3 = " ".join(tokens[:3])
        if opener1 in JARGON_OPENERS:
            warnings.append(f"{fid}: hook OPENS with jargon ('{opener1}') — a cold scroller won't decode it "
                            f"in 1-2s. Lead with the outcome/feeling; let the term support the hook, never open it.")
        if any(opener3.startswith(ing) for ing in INGREDIENT_OPENERS):
            warnings.append(f"{fid}: hook OPENS with an ingredient name — nobody scrolling cares about the "
                            f"ingredient yet. Lead with what it DOES (the outcome or feeling), not what's in it.")
        # Constructed parallelism (≥3 short period-split fragments, no connector) reads as
        # copywriter rhythm, not lifted real voice (feedback-hook-craft). Nudge, never block.
        line = ad.get("headline") or hook
        frags = [f.strip() for f in re.split(r"[.!?]+", line) if f.strip()]
        if len(frags) >= 3 and all(len(f.split()) <= 3 for f in frags) \
           and not (set(line.lower().split()) & {"but", "and", "just", "already", "still", "so", "because", "yet"}):
            warnings.append(f"{fid}: '{line}' reads as constructed parallelism (3+ short fragments, no connector) "
                            f"— our rule prefers lifted real-voice (connectors that sound spoken) over copywriter "
                            f"rhythm. Confirm it sounds said, not written.")

    # ── Claimed-count vs shown: "nine super-herbs" headline but only M call-outs ──
    # The number-vs-shown mismatch (the pattern we flag in competitors). Warn, never block —
    # showing all N is often impractical; the warning forces a conscious design choice.
    _NUM = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
            "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}
    claim_text = ((ad.get("headline") or "") + " " + (ad.get("hook") or "")).lower()
    m = re.search(r"\b(\d+|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s+"
                  r"(adaptogens?|super-?herbs?|mushrooms?|herbs?|ingredients?|reasons?)\b", claim_text)
    shown = len([it for it in ad.get("items", []) if it])
    if m and shown:
        claimed = int(m.group(1)) if m.group(1).isdigit() else _NUM.get(m.group(1), 0)
        if claimed > shown:
            warnings.append(f"{fid}: claims '{m.group(0)}' but shows only {shown} call-out(s)/item(s) — the "
                            f"number-vs-shown mismatch. Confirm the design doesn't imply {shown} is the total.")
    if pt == "blend" and re.search(r"\b(\d+|nine)\s+adaptogens?\b", claim_text):
        warnings.append(f"{fid}: 'adaptogens' as the counted noun — not all nine blend ingredients are strictly "
                        f"adaptogens (Shilajit is a mineral resin). The brand-matching phrase is "
                        f"'super-herbs and mushrooms' (the live-ad wording).")

    # ── Orphan referent: in-image text that hinges on an unnamed "them/they/those" ──
    # A cold viewer reads the IN-IMAGE words in 1-2s; a bare pronoun ("Not for them.")
    # has no referent unless the frame or copy names who/what. Name it or show it.
    in_img = (ad.get("text_in_image") or ad.get("headline") or "").lower()
    if re.search(r"\b(them|they|those|theirs)\b", in_img):
        warnings.append(f"{fid}: in-image text leans on a pronoun ('them/they/those') with no named "
                        f"referent — a cold viewer may not know who it means. Name it (e.g. 'my kids') "
                        f"or make the referent visible in the frame.")

    # ── corner_stamp: opt-in urgency/news device — must reflect a TRUE state ──
    if ad.get("corner_stamp"):
        warnings.append(f"{fid}: corner_stamp '{ad['corner_stamp']}' — use only for a literally true state "
                        f"(real restock / new launch / bestseller); never manufacture scarcity.")

    # ── style field sanity ──
    style = ad.get("style")
    if style and fmt != "blocks":
        warnings.append(f"{fid}: 'style' set but format is '{fmt}' — style only affects blocks")
    if fmt == "blocks" and style and style not in BLOCK_STYLES:
        warnings.append(f"{fid}: unknown blocks style '{style}' (use {sorted(BLOCK_STYLES)})")

    # ── art_style (the artistic-medium axis) sanity ──
    ast = ad.get("art_style")
    if ast and ast not in ART_STYLES:
        warnings.append(f"{fid}: unknown art_style '{ast}' (use {sorted(ART_STYLES)})")
    if ast and ast != "photographic" and fmt == "ugc":
        warnings.append(f"{fid}: art_style '{ast}' set on a ugc ad — ugc is phone-photographic by "
                        f"nature, so art_style is ignored here. Use a non-ugc format for an art-led look.")

    # ── per-word emphasis placement (must land on a real, meaningful word) ──
    # Skipped for ugc, where emphasis never renders (warned above instead).
    emphasis = ad.get("emphasis", {})
    if emphasis and fmt != "ugc":
        target_text = ((ad.get("headline") or ad.get("hook", "")) + " " + ad.get("subhead", "")).lower()
        stops = _stopwords()
        for phrase, treat in emphasis.items():
            p = str(phrase).lower().strip()
            count = target_text.count(p)
            if treat not in EMPHASIS_TREATMENTS:
                warnings.append(f"{fid}: emphasis '{phrase}' uses unknown treatment '{treat}' (use {sorted(EMPHASIS_TREATMENTS)})")
            if count == 0:
                errors.append(f"{fid}: emphasis target '{phrase}' is NOT in the headline/subhead — it can't be placed. Fix the phrase.")
            elif count > 1:
                warnings.append(f"{fid}: emphasis target '{phrase}' appears {count}× — ambiguous which one gets emphasized.")
            if p in stops:
                warnings.append(f"{fid}: emphasis on stopword '{phrase}' — emphasis is wasted unless it carries meaning.")
            if treat == "gold" and (p in VILLAIN_WORDS or any(w in VILLAIN_WORDS for w in p.split())):
                warnings.append(f"{fid}: gold emphasis on '{phrase}' — that's a problem/negative word; the gold focal "
                                f"anchor usually carries the OUTCOME, not the villain. Move it to the benefit word "
                                f"(a strike-through on the villain is fine; gold isn't).")

    # ── cta_style sanity ──
    cta_style = ad.get("cta_style")
    if cta_style and cta_style not in CTA_STYLES:
        warnings.append(f"{fid}: unknown cta_style '{cta_style}' (use {sorted(k for k in CTA_STYLES)}) — falling back to 'button'")
    # CTA isolation: an outline/ghost CTA among outline proof chips reads as a third badge,
    # not an action (the click-killer the design research warns about) — force a distinct form.
    if cta_style in ("ghost", "ghost_right", "text_link") and (ad.get("proof") or ad.get("stats")):
        warnings.append(f"{fid}: outline/ghost CTA '{cta_style}' sits among proof chips — they collide "
                        f"(both read as outline pills). Use a solid/distinct CTA form (button, pill, arrow_down).")

    # ── type_personality / social_proof field sanity ──
    tp = ad.get("type_personality")
    if tp and tp not in TYPE_PERSONALITIES:
        warnings.append(f"{fid}: unknown type_personality '{tp}' (use {sorted(TYPE_PERSONALITIES)})")
    spf = ad.get("social_proof")
    if isinstance(spf, str) and spf not in SOCIAL_PROOF_VISUALS:
        warnings.append(f"{fid}: unknown social_proof '{spf}' (use {sorted(SOCIAL_PROOF_VISUALS)}, or True/False)")
    # Trust-mark duplication: when the social-proof lockup renders the count ("200,000+
    # customers" / "loved by thousands"), a proof chip repeating it is redundant. The engine
    # drops the chip to avoid a double-print; the spec is cleaner without it. Uses the engine's
    # own gate (imported) so this can't drift from what actually renders — e.g. the social_proof
    # archetype suppresses the lockup, so a count chip there is the intended hero, not a dup.
    if _social_proof_on(ad):
        for c in list(ad.get("proof") or []) + list(ad.get("stats") or []):
            cl = str(c).lower()
            if ("thousand" in cl) if pt == "tea" else (CUSTOMER_COUNT_NUM in cl or CUSTOMER_COUNT_NUM.replace(",", "") in cl):
                warnings.append(f"{fid}: proof chip '{c}' repeats the customer count the social-proof lockup already "
                                f"renders — the engine drops it to avoid a double-print. Remove it from the spec, "
                                f"or set social_proof=False.")

    # ── archetype sanity ──
    arche = ad.get("archetype")
    if arche and arche not in DESIGN_ARCHETYPES:
        warnings.append(f"{fid}: unknown archetype '{arche}' (use {sorted(DESIGN_ARCHETYPES)})")
    if not arche:
        suggested = _default_archetype(fmt, ad.get("style"), ad.get("audience", "acquisition"))
        warnings.append(f"{fid}: no archetype set — will default to '{suggested}'. Set one explicitly for intended design variety.")

    # ── audience fit (reads AUDIENCE_POLICY — the single source of truth) ──
    audience = ad.get("audience", "acquisition")
    pol = AUDIENCE_POLICY.get(audience)
    if pol:
        disc = pol["discouraged"]
        candidates = {fmt, arche, _STYLE_TO_ARCHETYPE.get(style, style)}
        for key in candidates:
            if key and key in disc:
                warnings.append(f"{fid}: '{key}' is off-strategy for {audience} — {disc[key]}")

    # ── retarget must carry a LAUNCH signal (it's a product launch, not a generic ad) ──
    if audience == "retarget":
        launch_text = " ".join(t for _, t in _rendered_texts(ad)).lower()
        signals = ("alcami", "blend", "new", "first", "now", "made", "introduc",
                   "meet", "here", "arrived", "landed", "try this", "loved")
        if launch_text and not any(s in launch_text for s in signals):
            warnings.append(
                f"{fid}: retarget ad has no launch signal in its rendered text (Alcami / blend / "
                f"new / first / now / we made / loved this) — it reads like a generic ad, not news "
                f"to a customer who already bought. Make it unmistakably a launch."
            )

    # ── Competitor mentions: naming a rival BRAND is allowed; the obligations are not ──
    # Comparative claims must be TRUE, parallel, and substantiated; a rival is shown by
    # form factor + named in text, never as a distorted logo; people are never named.
    # Fires on the `competitor` field OR a rival name in rendered text.
    comp = _competitor(ad)
    rendered_low = " ".join(t for _, t in _rendered_texts(ad)).lower()
    brand = comp.get("name") if comp else next((b for b in COMPETITOR_NAMES if b in rendered_low), None)
    if brand:
        warnings.append(
            f"{fid}: names competitor '{brand}' — every comparative claim must be TRUE, parallel, and "
            f"substantiated (same dimension per row). Show their product by form factor and name them in "
            f"text; never reproduce a competitor logo at distorting fidelity; never name people. Alcami stays the resolution."
        )

    # ── Brand-claim guards on RENDERED text ──
    for where, text in _rendered_texts(ad):
        low = text.lower()
        if pt == "tea":
            if CUSTOMER_COUNT_NUM in text or CUSTOMER_COUNT_NUM.replace(",", "") in text:
                errors.append(f"{fid} [{where}]: '{CUSTOMER_COUNT_NUM}+' is a BLEND claim — tea uses 'thousands' or 4.9★")
            if BLEND_PRICE_TOKEN in text:
                errors.append(f"{fid} [{where}]: '{BLEND_PRICE_TOKEN}' is the blend price — tea anchor is '{PRICES['tea']}'")
            if sku == "morning" and "caffeinated" in low:
                errors.append(f"{fid} [{where}]: Morning is caffeine-FREE — never 'caffeinated'")
            if sku == "night" and "fall asleep faster" in low:
                errors.append(f"{fid} [{where}]: Night = parasympathetic, not sedation — never 'fall asleep faster'")
            if sku == "trifecta" and "try all three" in low:
                errors.append(f"{fid} [{where}]: Trifecta is ONE product — never 'try all three' (use 'Get the Trifecta')")
            if re.search(r"\d+\s*mg", low):
                errors.append(f"{fid} [{where}]: specific mg dose on tea — the site publishes none. Use ingredient name/function, not '250mg'.")
        else:  # blend
            if TEA_PRICE_TOKEN in text or TEA_PRICE_TOKEN.lstrip("$") in text:
                errors.append(f"{fid} [{where}]: '{TEA_PRICE_TOKEN}' is the tea price — blend anchor is '{PRICES['blend']}'")
            # Original is brand-stated caffeine-free; Matcha = minimal caffeine, Cacao = trace
            # theobromine — so an absolute caffeine-free claim is Original-only (CLAUDE.md).
            if sku in ("matcha", "cacao") and re.search(r"(caffeine[- ]free|zero caffeine|no caffeine)", low):
                errors.append(f"{fid} [{where}]: '{sku}' is NOT caffeine-free (Matcha = minimal caffeine, "
                              f"Cacao = trace theobromine) — caffeine-free / zero-caffeine is an Original-only claim.")
            if "latte" in low:
                warnings.append(f"{fid} [{where}]: 'latte' in rendered text — coffee/latte is the reference "
                                f"experience, never what we sell (an adaptogenic superfood blend). Make sure "
                                f"the line can't read as a coffee brand.")
        # Universal rendered-text hygiene
        if "—" in text or "–" in text:
            warnings.append(f"{fid} [{where}]: contains en/em dash — house style is hyphen '-': '{text[:50]}…'")
        if " - " in text:
            warnings.append(f"{fid} [{where}]: ' - ' as a clause separator — the model renders it as an en-dash, "
                            f"and a 'word - clause' subhead is a banned construction. Use a period or colon: '{text[:50]}…'")
        if "·" in text:
            warnings.append(f"{fid} [{where}]: contains '·' bullet in rendered text — remove for clean copy: '{text[:50]}…'")
        if re.search(r"\d+\s*(reviews|ratings)", low):
            warnings.append(f"{fid} [{where}]: review COUNT in image text — use star rating only (4.9★)")
        for drug in DRUG_BRAND_NAMES:
            if drug in low:
                errors.append(f"{fid} [{where}]: names prescription drug '{drug}' — creative references "
                              f"the class ('GLP-1') only, never a drug brand (Meta prescription-drug "
                              f"rules + trademark exposure).")
        if re.search(r"\b(your|you'?re on|are you on)\s+(a\s+)?glp-?1", low):
            warnings.append(f"{fid} [{where}]: second-person GLP-1 phrasing ('your GLP-1' / 'are you on') "
                            f"asserts the viewer's medical status — a Meta Personal Attributes violation. "
                            f"Speak to the product's fit ('The GLP-1 ritual'), never the viewer's status.")

    # ── Trifecta gradient reminder (soft) ──
    if pt == "tea" and sku == "trifecta" and fmt in ("blocks", "scene", "how_it_works"):
        joined = (
            " ".join(t for _, t in _rendered_texts(ad))
            + " " + str(ad.get("color_world", ""))
            + " " + str(ad.get("visual", ""))
            + " " + " ".join(b.get("content", "") for b in ad.get("blocks", []))
        ).lower()
        if not any(k in joined for k in ("gradient", "lavender", "gold crown", "three zone", "gold to sage")):
            warnings.append(f"{fid}: Trifecta ad — confirm the gold/sage/lavender gradient is preserved in the visual")

    # ── extra_refs: catch missing reference files at validate time, not mid-run ──
    for extra in ad.get("extra_refs", []):
        for key, path in extra.items():
            if not os.path.exists(os.path.join(_PROJECT_ROOT, path)):
                errors.append(f"{fid}: extra_ref '{key}' path not found: {path}")

    # ── Register coherence: a loud, confrontational headline type ('condensed_bold')
    # wants a color world with real contrast or depth. Pairing it with a soft, pale, flat
    # world makes the ad shout in a whisper (the 3pm ad-01 failure). Heuristic → warning. ──
    tp = ad.get("type_personality", "")
    cw = (ad.get("color_world") or "").lower()
    if tp == "condensed_bold" and cw:
        soft = any(w in cw for w in ("soft", "pale", "gentle", "whisper", "faint", "airy",
                                     "delicate", "bright cream", "muted"))
        contrast = any(w in cw for w in ("dark", "near-black", "black", "deep", "saturated",
                                         "bold", "high-contrast", "high contrast", "split", " vs ",
                                         "charcoal", "espresso", "midnight", "forest", "electric",
                                         "vivid", "molten", "graphite"))
        if soft and not contrast:
            warnings.append(
                f"{fid}: type_personality 'condensed_bold' (loud/confrontational) sits in a soft, low-contrast "
                f"color_world — register mismatch (the headline shouts in a whisper-toned world). Pair loud type "
                f"with a higher-contrast or darker world, or pick a quieter type_personality.")

    return errors, warnings


# ── Assembled-prompt linter ───────────────────────────────────────────────────
# validate_spec reads the SPEC; this reads the BUILT PROMPT. Self-contradictions only
# appear after fragments concatenate (author prose + rotated treatments + format defaults
# + hard rules), so they're invisible to spec validation. Each rule below is a real case
# found by reading an assembled prompt (the redesign roadmap records the failure classes:
# research/prompt-architecture-redesign.md).
_HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}\b")
# Ambient design-context lines may legitimately carry a hex; copy/action directives may NOT
# (the model can render a hex it's shown — a documented leak). Prefix-allowlist by line.
_HEX_CONTEXT_PREFIXES = ("COLOR WORLD", "CAMERA", "LIGHTING", "REFERENCE IMAGE")


def _effective_archetype(ad: dict) -> str:
    return ad.get("archetype") or _default_archetype(
        ad.get("format", "scene"), ad.get("style"), ad.get("audience", "acquisition"))


def lint_prompt(ad: dict, prompt: str) -> tuple:
    """Lint the ASSEMBLED prompt for self-contradictions. Returns (errors, warnings).
    Errors are cases a source fix has already eliminated globally (so they stay green and
    block regressions); warnings are detection-only patterns an author should resolve."""
    errors, warnings = [], []
    fid = ad.get("file", "?")
    lines = prompt.split("\n")

    # 1) hex code inside a copy/action directive — leak risk (use a color NAME there).
    for ln in lines:
        s = ln.strip()
        if _HEX_RE.search(s) and not s.startswith(_HEX_CONTEXT_PREFIXES):
            errors.append(f"{fid} [prompt]: hex code in a non-design line (leak risk — name the "
                          f"color in copy/CTA directives): \"{s[:70]}…\"")
            break

    # 2) camera / lighting direction on a non-photographic archetype OR art_style (a lens
    #    contradicts a typographic poster or an illustration / riso / graphic-design medium).
    arche = _effective_archetype(ad)
    non_photo = arche in _NON_PHOTOGRAPHIC_ARCHETYPES or not _is_photographic(ad)
    if non_photo and ("\nCAMERA:" in prompt or "\nLIGHTING:" in prompt):
        why = (f"archetype '{arche}'" if arche in _NON_PHOTOGRAPHIC_ARCHETYPES
               else f"art_style '{ad.get('art_style')}'")
        errors.append(f"{fid} [prompt]: {why} is non-photographic but the prompt carries CAMERA/LIGHTING "
                      f"direction — contradiction (no lens on a poster, illustration, or print).")

    # 3) social proof aimed at a TOP/UPPER corner — it steals the headline's first-read slot.
    for ln in lines:
        if ln.startswith("SOCIAL PROOF") and re.search(r"\b(upper|top)[- ]?(corner|left|right|edge)\b", ln, re.I):
            errors.append(f"{fid} [prompt]: social proof directed to a TOP/UPPER corner — it competes with "
                          f"the headline for first read (proof anchors near the product or below, never above).")
            break

    # 4) copy embedded in scene/visual_action prose — a second headline/subhead the model may
    #    double-render or contradict against the structured text block. Detection only.
    prose = " ".join(str(ad.get(k, "")) for k in ("scene", "visual_action"))
    embedded = re.findall(r"['\"]([^'\"]{12,}?)['\"]", prose)
    copy_like = [s for s in embedded if len(s.split()) >= 3]
    if copy_like:
        warnings.append(f"{fid} [prompt]: scene/visual_action prose embeds copy-like text "
                        f"(\"{copy_like[0][:48]}…\") — keep copy in the structured headline/subhead "
                        f"fields only; prose copy can double-render or contradict them.")

    # 5) defaulted lighting fighting the concept's time of day. Detection only.
    m = re.search(r"\nLIGHTING:[^\n]*", prompt)
    lit = (m.group(0) if m else "").lower()
    copy_txt = " ".join(str(ad.get(k, "")) for k in ("hook", "headline", "subhead")).lower()
    if "morning" in lit and re.search(r"\b(3\s?pm|3 ?p\.?m\.?|afternoon|night|evening|midnight|2am|3am)\b", copy_txt):
        warnings.append(f"{fid} [prompt]: LIGHTING reads 'morning' but the copy implies a different time of "
                        f"day — defaulted lighting (keyed to SKU mood) fighting the concept.")

    # 6) proof can't be the hero AND sub-dominant: the social_proof archetype ("Proof is the hero")
    #    must not co-occur with the sub-dominant proof lockup in the same prompt.
    if "Proof is the hero" in prompt and "SOCIAL PROOF (sub-dominant" in prompt:
        errors.append(f"{fid} [prompt]: the social_proof archetype ('Proof is the hero') and the sub-dominant "
                      f"proof lockup are both present — proof can't be hero and sub-dominant at once. The "
                      f"lockup is suppressed for this archetype; don't force it back on.")

    return errors, warnings


def validate_campaign(ads: list) -> tuple:
    """Validate every ad + cross-ad checks (duplicate filenames, duplicate hooks)."""
    all_errors, all_warnings = [], []
    seen_files, seen_hooks = {}, {}
    for ad in ads:
        e, w = validate_spec(ad)
        all_errors += e
        all_warnings += w
        f = ad.get("file")
        if f in seen_files:
            all_errors.append(f"{f}: duplicate filename in campaign")
        seen_files[f] = True
        h = (ad.get("hook") or "").strip().lower()
        if h and h in seen_hooks:
            all_warnings.append(f"{f}: hook duplicates {seen_hooks[h]} — every hook should be a distinct angle")
        elif h:
            seen_hooks[h] = f

    # ── Anti-defaulting: a creative element identical across the WHOLE batch was
    # defaulted, not chosen (CLAUDE.md: variety across a batch is first-class). Effective
    # value = what actually renders (cta unset → 'button'; archetype unset → its default).
    if len(ads) >= 3:
        def _eff_cta(a):  return a.get("cta_style") or "button"
        def _eff_arch(a): return a.get("archetype") or _default_archetype(
            a.get("format", "scene"), a.get("style"), a.get("audience", "acquisition"))
        for label, fn in (("format", lambda a: a.get("format", "scene")),
                          ("CTA style", _eff_cta),
                          ("archetype", _eff_arch)):
            vals = {fn(a) for a in ads}
            if len(vals) == 1:
                all_warnings.append(
                    f"BATCH: every ad uses the same {label} ('{next(iter(vals))}') — a defaulted element, "
                    f"not a chosen one. CLAUDE.md: variety across a batch is first-class; break at least one "
                    f"ad to a different {label} (or confirm the uniformity is deliberate).")

    # ── CTA COPY defaulting (distinct from CTA *style*): "Shop Now" on every ad is defaulted
    # copy, even when the button shapes vary. The copy is free text — vary the verb to the angle. ──
    if len(ads) >= 3:
        ctas = [(a.get("cta") or "").strip() for a in ads]
        ctas = [c for c in ctas if c]
        if len(ctas) >= 3 and len({c.lower() for c in ctas}) == 1:
            all_warnings.append(
                f"BATCH: every ad's CTA reads the same copy ('{ctas[0]}') — defaulted, not chosen. The CTA "
                f"copy is free text; vary the verb to the angle ('Fix the dip', 'Make the swap', 'See the "
                f"label'), not just the button shape.")

    # ── Defaulted trust chrome: the same proof chip stamped across most of a batch is
    # defaulted, not designed (e.g. NSF on nearly every ad). Warn once, name the chip. ──
    if len(ads) >= 4:
        chip_on = {}            # chip -> how many ads carry it
        ads_with_proof = 0
        for a in ads:
            chips = {str(c).strip().lower() for c in (a.get("proof") or a.get("stats") or []) if str(c).strip()}
            if chips:
                ads_with_proof += 1
                for c in chips:
                    chip_on[c] = chip_on.get(c, 0) + 1
        if ads_with_proof >= 4 and chip_on:
            chip, n = max(chip_on.items(), key=lambda kv: kv[1])
            if n / ads_with_proof >= 0.6:
                all_warnings.append(
                    f"BATCH: proof chip '{chip}' appears on {n}/{ads_with_proof} ads with proof — recycled "
                    f"trust chrome reads as defaulted, not designed per ad. Vary the proof points, or design "
                    f"the trust block differently across the batch (the same NSF+guarantee pair on every ad).")

    # ── Hook-shape monotony: a batch where most hooks are questions is one shape over-indexed. ──
    if len(ads) >= 4:
        q = sum(1 for a in ads if (a.get("headline") or a.get("hook") or "").strip().endswith("?"))
        if q / len(ads) > 0.5:
            all_warnings.append(
                f"BATCH: {q}/{len(ads)} hooks are questions ('?') — one hook shape over-indexed. Vary the "
                f"shape (an outcome, a behavior, a comparison, a provenance line), not just the format.")

    # ── Assembled-prompt lint: build each prompt and scan the OUTPUT for self-contradictions
    # that spec validation can't see (they only appear after fragments concatenate). A build
    # failure here is not ours to report — gen.py's own build step surfaces it. ──
    for ad in ads:
        try:
            built = build_prompt(ad)
        except Exception:
            continue
        e, w = lint_prompt(ad, built)
        all_errors += e
        all_warnings += w

    return all_errors, all_warnings
