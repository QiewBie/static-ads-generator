"""
Alcami Prompt Builder — universal assembly engine for ad generation.

Converts slim ad specs into full Gemini prompts. Keeps all SKU constants,
hard rules, and format logic in one place so they never drift across batch files.

Usage from a campaign config:
    from prompt_builder import build_prompt, get_refs_for_campaign, get_ad_refs

Format types:
    "scene"        — atmospheric/photography-based. Most ads. Hook + real-world scene.
    "comparison"   — side-by-side or before/after. Us vs. them, old way vs. new.
    "blocks"       — multi-section structured layout. Proof-heavy, system-level ads.
                     Sub-style via `style` field (ingredient_breakdown / benefit_highlights /
                     social_proof / testimonial_text) — actively shifts the prompt emphasis.
    "ugc"          — phone-shot, person-centric, deliberately imperfect. Strong for cold traffic.
    "how_it_works" — infographic mechanism flow. Numbered steps. Converts skeptics.

Authoring note: write the hook ONCE in the `hook` field. Inside blocks/steps/points,
reference it with the token {hook} — the builder substitutes it. Never restate the hook
text literally in content (that creates two sources of truth that drift apart).
"""

import hashlib
import os

# Repo root — so extra_ref path checks work regardless of caller's cwd.
_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# ── Photographic variety (the FROZEN-look fix) ──────────────────────────────────
# Each SKU carries a `mood` tag, not a single hardcoded camera/light. The scene
# builder picks one camera + one lighting from the mood's pool, chosen
# deterministically by the ad's filename — so a re-run is stable, but two
# different Night ads get genuinely different photography. A spec may override
# with its own "camera" / "lighting" keys.

MOOD_LOOKS = {
    "bright_warm": {
        "cameras": [
            "Hasselblad medium format, 80mm f/2 — shallow, premium product feel",
            "35mm reportage, candid and natural, slight handheld imperfection",
            "overhead flat-lay, 50mm, clean and graphic",
        ],
        "lightings": [
            "warm low-angle morning light from the left, golden-hour, directional",
            "bright soft window light, airy and clean, gentle shadows",
            "dappled sunlight through a window, warm pools of light",
        ],
    },
    "focused_clean": {
        "cameras": [
            "Hasselblad medium format, 80mm f/2.8 — crisp and considered",
            "35mm desk-level documentary, real workspace depth",
            "slight high-angle, 50mm, looking down on a work surface",
        ],
        "lightings": [
            "soft diffused daylight, clean and even",
            "crisp directional afternoon light with clearly defined shadows",
            "bright overcast quality — near-shadowless, focused",
        ],
    },
    "dark_moody": {
        "cameras": [
            "Canon EOS R5, 100mm macro f/2.8 — intimate detail",
            "50mm low-light, shallow depth, close and personal",
            "35mm dim interior, environmental, a real room around the product",
        ],
        "lightings": [
            "single soft spotlight from above, deep surrounding shadow",
            "warm bedside-lamp glow, low and pooled, the rest of the room dim",
            "blue-hour ambient with one warm accent light breaking the dark",
        ],
    },
    "editorial_even": {
        "cameras": [
            "Hasselblad medium format, 80mm — even, editorial product lighting",
            "overhead flat-lay, 50mm, symmetrical and considered",
            "three-quarter product angle, 90mm, gentle compression",
        ],
        "lightings": [
            "soft even studio lighting, full detail visible",
            "bright daylight with soft gradient-preserving shadows",
            "soft top light with subtle fill, premium catalogue feel",
        ],
    },
}

# ── Price anchors ─────────────────────────────────────────────────────────────

PRICES = {
    "tea":   "From $37.40/month",
    "blend": "From $39/month",
}

# ── Product category cue ────────────────────────────────────────────────────────
# What the product IS, in plain words. Must be legible in every creative unless
# the spec opts into `associative: True`. Stops "is this even tea?" ambiguity.

CATEGORY = {
    "tea":   "Adaptogenic Mushroom Tea",
    "blend": "Superfood Mushroom Latte",
}

# ── Tea SKU definitions ───────────────────────────────────────────────────────

TEA_SKUS = {
    "morning": {
        "name":          "Morning Ritual",
        "ref_key":       "tea_morn",
        "ref_path":      "assets/brand/product_images_tea/MorningTeasquare.png",
        "color_hex":     "#E8B840",
        "color_name":    "warm amber-gold",
        "canister_desc": "warm amber-gold #E8B840 ground color and near-black label text",
        "gradient_note": None,
        "opening_tone":  "warm, grounded, quietly energizing",
        "mood":          "bright_warm",
        "color_scene":   "anchored in warm amber-gold #E8B840 — the dominant tone of the light and key surfaces, while natural materials (wood, ceramic, linen) keep their real colors so it reads as a real room, not a single-hue wash",
        "night_cup":     False,
        "caffeine_note": "Morning is CAFFEINE-FREE. The lift is Cordyceps-driven cellular energy, NOT stimulant. Never imply caffeinated.",
        "closing":       "feel like a brand that understands what a morning that actually holds looks like — and captured it without explaining it",
    },
    "afternoon": {
        "name":          "Afternoon Ritual",
        "ref_key":       "tea_aft",
        "ref_path":      "assets/brand/product_images_tea/AfternoonTeasquare.png",
        "color_hex":     "#9CB87A",
        "color_name":    "muted sage-olive green",
        "canister_desc": "muted sage-olive green #9CB87A ground color and near-black/dark forest label text",
        "gradient_note": None,
        "opening_tone":  "focused, clean, productive — no drama",
        "mood":          "focused_clean",
        "color_scene":   "anchored in muted sage-olive green #9CB87A — the dominant tone of light and key surfaces, while natural materials keep their real colors so it reads as a real workspace, not a single-hue wash",
        "night_cup":     False,
        "caffeine_note": "Afternoon is the only lightly caffeinated SKU (Guayusa) — can be named but do not lead with it. Do not cite a specific mg figure.",
        "closing":       "feel like a brand that knows exactly what 3pm feels like — and named it without drama",
    },
    "night": {
        "name":          "Nighttime Ritual",
        "ref_key":       "tea_night",
        "ref_path":      "assets/brand/product_images_tea/NightTeasquare.png",
        "color_hex":     "#1C2456",
        "color_name":    "deep midnight navy",
        "canister_desc": "deep midnight navy #1C2456 ground color and gold/cream label text",
        "gradient_note": None,
        "opening_tone":  "quiet, precise, unhurried",
        "mood":          "dark_moody",
        "color_scene":   "anchored in deep midnight navy #1C2456 — the dominant tone, with warm lamp accents and natural materials breaking the dark so it reads as a real dim room, NOT a flat navy wash",
        "night_cup":     True,
        "caffeine_note": "Night is FULLY CAFFEINE-FREE. Reishi is parasympathetic permission — NOT sedation. Never say 'fall asleep faster.' Say: HRV, fewer 2am wake-ups, deep sleep architecture.",
        "closing":       "feel like a brand that knows exactly what happens at 9pm — and named it without needing to explain anything",
    },
    "trifecta": {
        "name":          "Trifecta",
        "ref_key":       "tea_tri",
        "ref_path":      "assets/brand/product_images_tea/trifecta-tea-no-bg.png",
        "color_hex":     "#FFFDF5",
        "color_name":    "warm cream",
        "canister_desc": "gradient canister: gold crown → sage mid-section → lavender base",
        "gradient_note": "CRITICAL GRADIENT: The canister runs from warm gold at the crown to sage green at the mid-section to soft lavender at the base. Preserve every zone exactly — do not flatten, simplify, or merge these zones.",
        "opening_tone":  "editorial, complete, considered",
        "mood":          "editorial_even",
        "color_scene":   "neutral warm cream #FFFDF5 ground that lets all three gradient zones of the canister read clearly, with natural materials adding tonal range",
        "night_cup":     False,
        "caffeine_note": "Trifecta contains mixed caffeine: Morning caffeine-free, Afternoon lightly caffeinated (Guayusa), Night caffeine-free.",
        "closing":       "feel like a brand that thought carefully about morning, afternoon, and night — and built a separate answer for each",
    },
}

# ── Blend SKU definitions ─────────────────────────────────────────────────────

BLEND_SKUS = {
    "original": {
        "name":          "Original",
        "ref_key":       "orig",
        "ref_path":      "assets/brand/product_images_blend/original frontBIL2 .png",
        "color_hex":     "#FFFDF5",
        "color_name":    "warm cream to sand",
        "canister_desc": "warm cream to sand #D2C299 gradient on the label",
        "gradient_note": None,
        "opening_tone":  "bold, premium, direct",
        "mood":          "bright_warm",
        "color_scene":   "anchored in warm cream-to-sand #D2C299 — the dominant tone of light and key surfaces, while natural materials keep their real colors",
        "night_cup":     False,
        "closing":       "feel like a brand that earned 200,000 customers without a single celebrity endorsement",
    },
    "cacao": {
        "name":          "Cacao",
        "ref_key":       "cacao",
        "ref_path":      "assets/brand/product_images_blend/cacao front BILL 2.png",
        "color_hex":     "#282111",
        "color_name":    "near-black to deep bronze",
        "canister_desc": "near-black to bronze #867353 gradient on the label",
        "gradient_note": None,
        "opening_tone":  "rich, warm, indulgent — the ritual you look forward to",
        "mood":          "dark_moody",
        "color_scene":   "anchored in near-black #282111 to deep bronze #867353 — rich and dark, with warm highlights and natural materials breaking the dark",
        "night_cup":     False,
        "closing":       "feel like a brand that understood that a wellness ritual should be something you actually look forward to",
    },
    "matcha": {
        "name":          "Matcha",
        "ref_key":       "matcha",
        "ref_path":      "assets/brand/product_images_blend/matcha front BIL 2.png",
        "color_hex":     "#9CB87A",
        "color_name":    "earthy sage green to cream",
        "canister_desc": "sage green to cream gradient on the label",
        "gradient_note": None,
        "opening_tone":  "clean, focused, considered — premium without pretense",
        "mood":          "focused_clean",
        "color_scene":   "anchored in earthy sage-green to cream — the dominant tone of light and key surfaces, while natural materials keep their real colors",
        "night_cup":     False,
        "closing":       "feel like a brand that knows what clean energy actually looks like",
    },
    "espresso": {
        "name":          "Espresso",
        "ref_key":       "espresso",
        "ref_path":      "assets/brand/product_images_blend/espresso front BIL2.png",
        "color_hex":     "#1A1008",
        "color_name":    "near-black to dark espresso brown",
        "canister_desc": "near-black to dark espresso brown gradient on the label",
        "gradient_note": None,
        "opening_tone":  "bold, unapologetic, direct — the coffee replacement that doesn't apologize",
        "mood":          "dark_moody",
        "color_scene":   "anchored in near-black to dark espresso brown — the dominant tone, with strong highlights and natural materials breaking the dark",
        "night_cup":     False,
        "closing":       "feel like a brand that replaced coffee without apologizing for it",
    },
}

# ── Hard rules — appended to every prompt ────────────────────────────────────
# The PRODUCT clause is archetype-aware: for idea-led archetypes (poster, screenshot,
# ugc) the type/number/moment is the hero and the product need not dominate. Everything
# else (legibility, full-bleed, no garbled text) is a true non-negotiable on every ad.

_HARD_RULES_TMPL = """
HARD RULES — apply without exception:
· DESIGN, don't transcribe: render ONLY the words in the explicit text/copy fields. Never draw field labels, quote marks, art-direction notes, bullet/leading marks (· • - *), or this brief's line breaks. Grouping, line breaks, alignment and spacing are YOUR design decisions; items are visual objects (chips, cards, columns), never a document list.
· NO forbidden text: no dates, ship dates, deadlines, URLs, domain names, or review-count numbers (star rating like 4.9★ is fine).
· PUNCTUATION: plain hyphens (-) only, never en/em dashes (– —); no decorative bullet marks in any rendered text.
· FULL BLEED: fill the entire 1:1 square to all four edges — sharp square corners, NO rounded corners, NO border, frame, matte, or device/phone mockup around the image.
· {product_rule}
· TEXT LEGIBILITY: place text in the clean, uncluttered negative space of the frame first. Only when contrast is genuinely insufficient, add a SOFT gradient scrim that fades to transparent, sized just to the text — never a hard-edged opaque rectangle, never a full-width band, never over the product.
· CTA: a self-contained tappable button (sized to its text, margin from the edges), the single highest-contrast element on the canvas — never a full-width footer stripe.
· NO floating body parts: any human element is visibly attached to a person in full context."""

_PRODUCT_RULE_HERO = ("PRODUCT: the canister/pouch is ≥35% of image height, the resolution of the "
    "concept (not decoration), with a soft diffused shadow beneath it — never a flat cutout. Text "
    "never overlaps, covers, or crops the product — they occupy separate zones.")

_PRODUCT_RULE_SUPPORT = ("PRODUCT: the canister/pouch is reproduced ACCURATELY and is clearly present, "
    "but it need NOT dominate — the oversized type/number, the screenshot, or the person's moment is "
    "the hero. Keep the label truthful and legible (a soft shadow if it rests on a surface); never a "
    "garbled or invented label. Text never crops or covers the product.")

# Archetypes where the IDEA, not the product's size, is the hero.
_PRODUCT_SUPPORT_ARCHETYPES = {"poster", "screenshot", "ugc_minimal"}


def _hard_rules(ad: dict) -> str:
    """HARD_RULES with an archetype-appropriate product clause."""
    rule = (_PRODUCT_RULE_SUPPORT if ad.get("archetype") in _PRODUCT_SUPPORT_ARCHETYPES
            else _PRODUCT_RULE_HERO)
    return _HARD_RULES_TMPL.format(product_rule=rule)


# Back-compat: the hero variant as a plain constant for any external reference.
HARD_RULES = _HARD_RULES_TMPL.format(product_rule=_PRODUCT_RULE_HERO)

# ── CTA style guide ───────────────────────────────────────────────────────────
# The cta_style field in the spec. Builder maps these to prompt instructions.
# EVERY style is a self-contained, tappable BUTTON — sized to its text, with clear
# margin from all edges. NEVER a full-width edge-to-edge band/stripe (that cuts the
# composition and reads as a flat footer, not an action).

CTA_STYLES = {
    "button":       "a prominent self-contained rounded-rectangle button, centered low in the frame with clear margin from every edge, sized to its text (NOT full-width), bold text and a soft drop shadow giving it lift — the obvious tap target",
    "button_right": "a self-contained rounded-rectangle button anchored bottom-right with clear margin from the edges, sized to its text, bold text and a soft drop shadow — quiet, off-center, still unmistakably tappable",
    "pill":         "a compact rounded pill button, centered low with margin from the bottom edge, bold text and a soft shadow giving it lift — restrained but clearly a button",
    "pill_right":   "a compact rounded pill button, bottom-right with margin from the edges, bold text and a soft shadow — quiet, off-center, clearly tappable",
    "text_link":    "an underlined text link with a small trailing arrow, bottom-left, no box — minimal and editorial, but still clearly the action, not a passive caption",
    "integrated":   "woven into the headline lockup as its closing line, same type family but visibly the action (a color or weight shift sets it apart) — no separate box",
    "none":         "no visible CTA in the image — the CTA lives in the ad copy text field only",
}
# Back-compat aliases for older specs. The full-width 'band' is RETIRED — it cut
# the composition; it now resolves to a contained button.
CTA_STYLES.update({
    "band_bottom":       CTA_STYLES["button"],
    "pill_bottom":       CTA_STYLES["pill"],
    "pill_bottom_right": CTA_STYLES["pill_right"],
    "text_line":         CTA_STYLES["text_link"],
})

# ── Price style guide ─────────────────────────────────────────────────────────

PRICE_STYLES = {
    "pill":     "a slim horizontal pill, gold #867353 fill, near-black bold text — designed, not bolted on",
    "footnote": "small spaced text, below the main copy, minimal — a supporting detail",
    "band":     "a slim contained gold #867353 pill, near-black bold text — full-width price bands are retired; render it contained, never edge-to-edge",
    "none":     None,
}

# ── Block sub-style emphasis ────────────────────────────────────────────────────
# The blocks `style` field. Each shifts what the composition leads with. Injected
# into _build_blocks_prompt so the four sub-styles are genuinely different prompts.

BLOCK_STYLES = {
    "ingredient_breakdown":
        "STYLE — INGREDIENT BREAKDOWN: The composition leads with what is INSIDE the product "
        "and what each element does. Every ingredient is its own labeled chip paired with its "
        "function. The ingredient story is the hero; the hook frames it. Curious, educational register.",
    "benefit_highlights":
        "STYLE — BENEFIT HIGHLIGHTS: The composition leads with OUTCOMES, not ingredients. Each chip "
        "names a result the person actually feels. Benefit-first language. The hook states the promise; "
        "the chips prove it with specific, concrete outcomes. Punchy, declarative register.",
    "social_proof":
        "STYLE — SOCIAL PROOF: Trust elements dominate the supporting layer — star rating (4.9★), "
        "certification badges, and proof points are the largest elements after the product itself. "
        "Designed as a premium trust layout, never a cluttered proof wall. Confident, earned register.",
    "testimonial_text":
        "STYLE — TESTIMONIAL: A single customer quote is the dominant text element, set in editorial "
        "serif as if spoken aloud. Attribution is simple and small. The product supports the voice; "
        "the quote carries the ad. Warm, human, first-person register.",
}

# ── Design archetypes (the GRAPHIC layer) ──────────────────────────────────────
# Named, restrained design languages. The builder expands the chosen one so ads
# vary intentionally instead of getting the same maximalist chip-wall every time.
# "Professional but not overly so" = few elements, used with confidence.

DESIGN_ARCHETYPES = {
    "editorial":    "Editorial/magazine: one large refined headline, generous negative space, one short supporting line. No rules, borders, or divider lines. Almost no UI. Premium, considered, restrained.",
    "spec_card":    "Spec/data card: clean grid, small line-icons, numeric callouts (4.9 stars, ingredient counts — for tea, NO mg doses), confident grotesque type. Transparent, scientific, uncluttered.",
    "annotated":    "Annotated product: thin call-out lines from the product to 3-4 short labels, like a refined diagram. Carries 'what's inside' with NO bulleted list.",
    "color_block":  "Color-blocked: 2-3 solid color zones dividing the canvas; type lives inside each zone. Bold, modern, confident — never busy.",
    "badge":        "Badge/seal accents: circular seals (USDA, NSF, 90-day) used sparingly as trust marks, never a wall of logos.",
    "ugc_minimal":  "Near-zero design: phone-shot frame, optional plain caption. No panels, no chips, no art direction. Cold-traffic authenticity.",
    "testimonial":  "Customer voice is the hero — a real quote set large, simple attribution. The product supports the voice.",
    "social_proof": "Proof is the hero — rating, count, or outcome stat dominates as a designed element, not a cluttered wall.",
    "poster":       "Poster / typographic: a single oversized numeral, word, or short statement IS the composition, filling most of the frame. Maximum type, minimal everything else. Loud, declarative, impossible to scroll past. The product sits smaller but still present.",
    "screenshot":   "Native social proof: rendered to look like a real captured screenshot — an Instagram/Facebook comment thread, a review card with stars, or a text-message exchange. The words feel screenshotted, not designed. Cold-traffic authenticity, but legible and on-brand (no fake usernames of real people).",
    "before_after": "Before / after transformation: one subject in two honest states — the old way vs. the Alcami way, or day 1 vs. day 30. A clear divide or diptych; the change is the entire point. Never exaggerate the result.",
}

# Visual manifestations the model rotates across for the designed proof/idea archetypes.
TESTIMONIAL_TREATMENTS   = ["quote_card", "review_screenshot", "portrait_quote", "star_hero"]
SOCIAL_PROOF_TREATMENTS  = ["star_hero", "big_number", "stat_callouts", "review_wall", "badge_cluster"]
POSTER_TREATMENTS        = ["single_numeral", "single_word", "stacked_statement"]
SCREENSHOT_TREATMENTS    = ["ig_comment", "review_card", "text_message", "tweet"]
BEFORE_AFTER_TREATMENTS  = ["split_vertical", "diptych", "labeled_panels"]


# ── Audience policy (THE single source of truth) ────────────────────────────────
# Which formats/archetypes lead for each audience, and which are discouraged + WHY.
# The validator reads this. Docs/batch headers dereference it (gen.py --policy).
# Change audience strategy HERE and nowhere else.

AUDIENCE_POLICY = {
    "acquisition": {
        "lead_formats": ["ugc", "scene", "comparison", "blocks", "how_it_works"],
        "archetypes":   ["ugc_minimal", "editorial", "spec_card", "annotated",
                         "color_block", "badge", "testimonial", "social_proof",
                         "poster", "screenshot", "before_after"],
        "discouraged":  {},   # cold traffic can use anything
    },
    "retarget": {
        # LAUNCH / CROSS-SELL register: existing customers, brand-new product. The job is
        # to SHARE NEWS and extend a relationship, not to educate, prove, or argue.
        # Core angles: "we made tea now!" · "loved the blend? try this" · two-product display
        # · insider/early-access · "one of the first mushroom teas."
        "lead_formats": ["scene", "blocks", "how_it_works"],
        "archetypes":   ["editorial", "color_block", "spec_card", "annotated", "badge", "poster"],
        "discouraged": {
            "ugc":          "warm audience already trusts you — relatability proof is wasted",
            "comparison":   "launch register is news, not an argument — don't pit our brand-new product in a vs. layout for people who already buy from us",
            "testimonial":  "they don't need peer validation; share the news instead",
            "social_proof": "they're already sold on quality; lead with 'we made this — try it', not proof",
            "screenshot":   "native social-proof is for cold skeptics — warm buyers don't need authenticity signals",
            "before_after": "before/after is a proof/argument device — the launch register is news, not a case to argue",
        },
    },
}

# blocks `style` values map onto archetypes for policy checks
_STYLE_TO_ARCHETYPE = {"testimonial_text": "testimonial", "social_proof": "social_proof"}


def print_policy() -> None:
    """Print the authoritative format/archetype/audience matrix. `gen.py --policy`."""
    print("\nFORMATS:", ", ".join(sorted(VALID_FORMATS)))
    print("\nDESIGN ARCHETYPES:")
    for k, v in DESIGN_ARCHETYPES.items():
        print(f"  {k:13} {v}")
    print("\nAUDIENCE POLICY:")
    for aud, pol in AUDIENCE_POLICY.items():
        print(f"\n  [{aud}]")
        print(f"     lead formats: {', '.join(pol['lead_formats'])}")
        print(f"     archetypes:   {', '.join(pol['archetypes'])}")
        for k, why in pol["discouraged"].items():
            print(f"     discouraged: {k} — {why}")
    print()


# ── Ref helpers ───────────────────────────────────────────────────────────────

def get_refs_for_campaign(ads: list) -> dict:
    """Build the REFS dict from all ad specs in a campaign. Called by gen.py."""
    refs = {}
    for ad in ads:
        product_type = ad.get("product_type", "tea")
        sku_key = ad.get("sku", "")
        if product_type == "tea" and sku_key in TEA_SKUS:
            sku = TEA_SKUS[sku_key]
            refs[sku["ref_key"]] = sku["ref_path"]
        elif product_type == "blend" and sku_key in BLEND_SKUS:
            sku = BLEND_SKUS[sku_key]
            refs[sku["ref_key"]] = sku["ref_path"]
        for extra in ad.get("extra_refs", []):
            # extra_refs is a dict: {"key": "path"}
            refs.update(extra)
    return refs


def get_ad_refs(ad: dict) -> list:
    """Return ordered list of ref keys for a single ad spec."""
    product_type = ad.get("product_type", "tea")
    sku_key = ad.get("sku", "")
    if product_type == "tea" and sku_key in TEA_SKUS:
        primary = TEA_SKUS[sku_key]["ref_key"]
    elif product_type == "blend" and sku_key in BLEND_SKUS:
        primary = BLEND_SKUS[sku_key]["ref_key"]
    else:
        primary = None
    refs = [primary] if primary else []
    for extra in ad.get("extra_refs", []):
        refs += list(extra.keys())
    return refs


# ── SKU lookup ────────────────────────────────────────────────────────────────

def _get_sku(ad: dict) -> dict:
    product_type = ad.get("product_type", "tea")
    sku_key = ad.get("sku", "")
    table = TEA_SKUS if product_type == "tea" else BLEND_SKUS
    if sku_key not in table:
        raise ValueError(
            f"{ad.get('file','<no file>')}: unknown sku '{sku_key}' for product_type "
            f"'{product_type}'. Valid: {sorted(table)}. (No silent fallback — fix the spec.)"
        )
    return table[sku_key]


def _get_price_line(ad: dict, sku: dict) -> str:
    if not ad.get("price"):
        return ""
    product_type = ad.get("product_type", "tea")
    price_str = PRICES[product_type]
    style_key = ad.get("price_style", "pill")
    style_desc = PRICE_STYLES.get(style_key, PRICE_STYLES["pill"])
    if not style_desc:
        return ""
    return f'\nPRICE: Show "{price_str}" as {style_desc}.'


def _get_cta_line(ad: dict) -> str:
    cta_text = ad.get("cta", "Shop Now")
    style_key = ad.get("cta_style", "button")
    style_desc = CTA_STYLES.get(style_key, CTA_STYLES["button"])
    if style_key == "none":
        return "\nNo visible CTA in the image."
    return (f'\nCALL TO ACTION — render the button text exactly "{cta_text}" '
            f'(those words only, never a "CTA" label): {style_desc}. '
            f'Fill it for MAXIMUM contrast against whatever sits directly behind it — a near-black '
            f'fill with cream text on light or warm backgrounds; a cream or brand-gold #867353 fill '
            f'with dark text on dark backgrounds. It must be the single highest-contrast, most '
            f'obviously tappable element on the canvas, and must never blend into the scene.')


def _stamp_line(ad: dict) -> str:
    """Optional bold overlay stamp (e.g. RESTOCK, NEW, BESTSELLER) — opt-in via the
    `stamp` field. Use ONLY for a literally true state; never manufacture scarcity.
    Rendered as a rotated rubber-stamp/sticker badge, never over product or headline."""
    stamp = ad.get("stamp")
    if not stamp:
        return ""
    return (f'\nSTAMP: render the word "{stamp}" as a bold, slightly rotated rubber-stamp or '
            f'sticker badge in a high-energy accent color, tucked in a corner so it never covers '
            f'the product or the headline — an attention spike, not clutter.')


def _pick(options: list, ad: dict, salt: str) -> str:
    """Deterministically pick one option, seeded by the ad filename + salt.
    Same file → same pick (stable re-runs); different files → different looks."""
    if not options:
        return ""
    key = (ad.get("file", "") + salt).encode()
    idx = int(hashlib.md5(key).hexdigest(), 16) % len(options)
    return options[idx]


def _pick_look(ad: dict, sku: dict) -> tuple:
    """Return (camera, lighting) for a scene. A spec may override either with its
    own 'camera'/'lighting' key; otherwise we sample the SKU mood's pool."""
    pool = MOOD_LOOKS.get(sku.get("mood", ""), {})
    camera   = ad.get("camera")   or _pick(pool.get("cameras", []),   ad, "cam") or "medium format, 80mm, premium product photography"
    lighting = ad.get("lighting") or _pick(pool.get("lightings", []), ad, "lit") or "soft directional natural light"
    return camera, lighting


def _get_night_cup_line(ad: dict, sku: dict) -> str:
    """Note for a brewed Night cup when one is present. Shared by ALL builders.
    The cup is just a calm, warm cup of herbal tea — we do NOT force an indigo
    color (no on-site basis, and it was never the point of the product)."""
    if sku.get("night_cup") and ad.get("has_cup", False):
        return (
            "\nNIGHT CUP: any brewed cup is a calm, inviting cup of herbal tea in a warm "
            "natural amber tone, gentle steam rising in the lamp light. Keep it natural and "
            "understated — not a bright or artificially colored liquid."
        )
    return ""


def _fill(text: str, ad: dict) -> str:
    """Substitute the {hook} token so the hook lives in exactly one place (the `hook` field).
    Authors write the visual treatment in block/step content and use {hook} for the words."""
    if not isinstance(text, str):
        return text
    return text.replace("{hook}", ad.get("hook", ""))


def _archetype_line(ad: dict) -> str:
    """Expand the chosen design archetype into specific design language."""
    arche = ad.get("archetype")
    desc = DESIGN_ARCHETYPES.get(arche) if arche else None
    if not desc:
        return ""
    treatments = {
        "testimonial":   TESTIMONIAL_TREATMENTS,
        "social_proof":  SOCIAL_PROOF_TREATMENTS,
        "poster":        POSTER_TREATMENTS,
        "screenshot":    SCREENSHOT_TREATMENTS,
        "before_after":  BEFORE_AFTER_TREATMENTS,
    }.get(arche)
    extra = f" Pick one treatment and commit to it: {', '.join(treatments)}." if treatments else ""
    return f"\nDESIGN ARCHETYPE — {arche}: {desc}{extra}\n"


# Sensible archetype when a spec omits one — keyed by (format, blocks-style).
# Retarget never gets testimonial/social_proof defaults (off-strategy).
def _default_archetype(fmt: str, style: str, audience: str) -> str:
    if fmt == "ugc":
        return "ugc_minimal"
    if fmt == "comparison":
        return "spec_card"
    if fmt == "how_it_works":
        return "color_block"
    if fmt == "scene":
        return "editorial"
    if fmt == "blocks":
        by_style = {
            "ingredient_breakdown": "annotated",
            "benefit_highlights":   "spec_card",
            "social_proof":         "social_proof",
            "testimonial_text":     "testimonial",
        }
        cand = by_style.get(style, "spec_card")
        # don't auto-apply an off-strategy archetype for retarget
        if audience == "retarget" and cand in ("testimonial", "social_proof"):
            return "spec_card"
        return cand
    return "editorial"


def _fmt_items(items: list) -> str:
    """Format copy items for the clean blocks path. Items are plain strings or
    {label, note} dicts. The ' | ' separates a bold name from its lighter note —
    the model is told never to render the bar itself."""
    out = []
    for it in items:
        if isinstance(it, dict):
            lab = it.get("label", "").strip()
            note = it.get("note", "").strip()
            out.append(f"     {lab} | {note}" if note else f"     {lab}")
        else:
            out.append(f"     {it}")
    return "\n".join(out)


# ── Typography: per-word emphasis vocabulary ────────────────────────────────────
# `emphasis` maps an exact phrase → a treatment. The builder turns it into plain
# typographic instructions; the validator (separately) checks each phrase actually
# occurs in the rendered text so emphasis always lands on a real, meaningful word.

EMPHASIS_TREATMENTS = {
    "bold":      "set in heavy bold weight",
    "italic":    "set in italic",
    "underline": "underlined with a clean rule",
    "strike":    "struck through (line through the word) — reads as negated/old",
    "gold":      "set in brand gold #867353 as a color accent",
    "boxed":     "enclosed in its own small high-contrast background chip",
}


def _emphasis_line(text: str, emphasis: dict) -> str:
    """Build a one-line typographic instruction for the emphasized words in `text`.
    Returns '' when there is nothing to emphasize."""
    if not emphasis:
        return ""
    parts = []
    for phrase, treat in emphasis.items():
        desc = EMPHASIS_TREATMENTS.get(treat, treat)
        parts.append(f'the word(s) "{phrase}" {desc}')
    return "  Within this line: " + "; ".join(parts) + "."


def _chips(ad: dict) -> list:
    """Proof/stat chips. `proof` and `stats` are ALIASES (proof wins if both set);
    capped at 3 — the layout asks for at most three."""
    chips = ad.get("proof") or ad.get("stats") or []
    return [str(c).strip() for c in chips if str(c).strip()][:3]


def _subhead_emphasis_chips(ad: dict, headline_text: str, *, with_chips: bool) -> str:
    """Shared secondary text layer for builders that render their OWN headline/hook:
    subhead + per-word emphasis (+ optional proof chips). Returns '' if nothing to add.
    Emphasis is matched against headline_text + subhead so it can land on either."""
    subhead = ad.get("subhead", "")
    emph = _emphasis_line((headline_text + " " + subhead), ad.get("emphasis", {}))
    chips = _chips(ad) if with_chips else []
    if chips and subhead:
        sub_low = subhead.lower()
        chips = [c for c in chips if c.lower() not in sub_low]
    lines = []
    if subhead:
        lines.append(f'  Subhead (supporting line, about half the headline size): "{subhead}"')
    if emph:
        lines.append(emph)
    if chips:
        cl = "; ".join(f'"{c}"' for c in chips)
        lines.append(f'  Proof chips: render EXACTLY {len(chips)} small chip(s), words only, '
                     f'no brackets/quotes/punctuation drawn, no invented chips: {cl}.')
    return ("\n" + "\n".join(lines)) if lines else ""


def _stopwords():
    return {"the","a","an","and","or","of","to","in","on","for","is","it","at","be",
            "this","that","your","you","with","my","i","no","not","but","so"}


def _category_line(ad: dict, sku: dict) -> str:
    """Make the product category legible for a STRANGER who needs it (cold traffic).
    Suppressed when: the ad opts into association; the audience already knows the
    brand (retarget); or the headline/subhead/hook already names the category. A spec
    forces it with `force_category=True`, or overrides the wording with `category_cue`."""
    if ad.get("associative"):
        return ""
    pt = ad.get("product_type", "tea")
    cue = ad.get("category_cue") or CATEGORY.get(pt, "")
    if not cue:
        return ""
    forced = bool(ad.get("force_category") or ad.get("category_cue"))
    # Warm/retarget buyers already know what we sell — don't clutter the launch.
    if ad.get("audience") == "retarget" and not forced:
        return ""
    # Redundant if the copy already names the category.
    word = "tea" if pt == "tea" else "latte"
    said = (str(ad.get("headline", "")) + " " + str(ad.get("subhead", "")) + " "
            + str(ad.get("hook", ""))).lower()
    if word in said and not forced:
        return ""
    return (f'\nCATEGORY CUE: the words "{cue}" appear EXACTLY ONCE, as a small caption '
            f'integrated into the product lockup (close to the canister, not floating in a '
            f'corner) so a stranger instantly knows this is {pt}. Secondary to the headline, '
            f'never duplicated, never a free-floating sticker.')


def _text_block(ad: dict, sku: dict) -> str:
    """Assemble the structured text layer shared by every format: headline (with
    optional per-word emphasis), optional subhead, optional stat chips. Body
    content (items/sides/steps) is handled per-format and is separate from this."""
    headline = ad.get("headline") or ad.get("hook", "")
    subhead  = ad.get("subhead", "")
    stats    = _chips(ad)
    emph     = _emphasis_line(headline + " " + subhead, ad.get("emphasis", {}))

    # Drop any stat already stated in the subhead — avoids duplicate chips.
    if stats and subhead:
        sub_low = subhead.lower()
        stats = [s for s in stats if str(s).lower().strip() not in sub_low]

    lines = [
        "TEXT TO RENDER — the ONLY words that appear in the image. Render each quoted string exactly; "
        "never draw these labels, the quote marks, the parentheses, or any size/percent note:"
    ]
    lines.append(f'  Headline: "{headline}"')
    if emph:
        lines.append(emph)
    if subhead:
        lines.append(f'  Subhead: "{subhead}"')
    if stats:
        chip_list = "; ".join(f'"{s}"' for s in stats)
        lines.append(
            f'  Proof chips: render EXACTLY {len(stats)} small chip(s) in one aligned row, each holding '
            f'ONLY the words quoted here, with no brackets/quotes/punctuation drawn and no invented chips: {chip_list}.'
        )
    # Size/role guidance kept SEPARATE from the quoted words so it can't be transcribed.
    lines.append(
        "  SIZE HIERARCHY (apply to the layout; do NOT render this note): the headline is the dominant, "
        "largest element and reads first; the subhead is about half its size and supports it; any chips are smallest."
    )
    return "\n".join(lines)


# ── Format builders ───────────────────────────────────────────────────────────

def _build_scene_prompt(ad: dict, sku: dict) -> str:
    product_type = ad.get("product_type", "tea")
    is_tea = product_type == "tea"

    # Canister/pouch reference instruction
    if is_tea:
        ref_line = (
            f"REFERENCE IMAGE 1: This is the ACTUAL Alcami Elements {sku['name']} canister. "
            f"Reproduce this exact cylindrical canister with photographic accuracy — "
            f"the ALCAMI ELEMENTS wordmark, the botanical mushroom engraving centered on the label, "
            f"the {sku['canister_desc']}, and all label text are essential. "
            f"The canister must be at least 35% of image height."
        )
        if sku.get("gradient_note"):
            ref_line += f"\n{sku['gradient_note']}"
    else:
        ref_line = (
            f"REFERENCE IMAGE 1: This is the ACTUAL Alcami Elements {sku['name']} pouch. "
            f"Reproduce this exact packaging with photographic accuracy — "
            f"every label detail, the gradient, and gold foil typography exactly as shown. "
            f"The pouch must be at least 35% of image height."
        )

    # Text layer: prefer the structured headline/subhead/stats model; fall back to
    # the legacy single text_in_image line for older atmospheric specs.
    if any(ad.get(k) for k in ("headline", "subhead", "stats", "proof", "emphasis")):
        text_line = "\n\n" + _text_block(ad, sku)
    else:
        text_in_image = ad.get("text_in_image", "")
        text_treatment = ad.get("text_treatment", "minimal, legible, not competing with the scene")
        text_line = f'\nTEXT IN IMAGE: "{text_in_image}" — {text_treatment}. High-contrast, fully legible.' if text_in_image else ""

    category_line = _category_line(ad, sku)

    # Night cup (shared helper — fires in every format, not just scene)
    night_cup_line = _get_night_cup_line(ad, sku)

    # Extra refs note
    extra_note = ""
    if ad.get("extra_refs"):
        extra_note = "\nREFERENCE IMAGE 2: Additional reference provided — use for context or product accuracy as described in the scene."

    price_line = _get_price_line(ad, sku)
    cta_line = _get_cta_line(ad)
    camera, lighting = _pick_look(ad, sku)

    prompt = f"""You are a world-class advertising photographer and art director creating a {sku['opening_tone']} advertisement for Alcami Elements {sku['name']}{" tea" if is_tea else ""}.

{ref_line}{extra_note}

HOOK (the one idea this ad is built from): {ad['hook']}

SCENE: {ad['scene']}

VISUAL ACTION: {ad['visual_action']}

COLOR WORLD: The entire scene is {sku['color_scene']}. The product belongs here because the world was built for it. NOTE: "color world" means the ambient light, surfaces, and atmosphere carry this tone — NOT the literal pigment of a person's skin or clothing. People stay naturally colored; the world around them carries the palette.

CAMERA: {camera}.

LIGHTING: {lighting}.

{_archetype_line(ad)}
DESIGN DEPTH:
· The product has a soft diffused shadow beneath it on its surface — physical weight, not a paste-in.
· Text and product occupy SEPARATE zones: the text lives in the clean negative space of the scene, never on top of or cropping the product. For legibility, prefer placing text where the background is already calm; if contrast is short, use a soft gradient scrim that fades to transparent, sized to the text only — never a hard opaque box, never a full-width band.
· Subtle vignette at canvas corners if the scene needs it — draws focus toward the product and text.{text_line}{category_line}{night_cup_line}{_stamp_line(ad)}{price_line}{cta_line}

{_hard_rules(ad)}

This should NOT look like a generic wellness ad. It should {sku['closing']}."""

    return prompt


def _build_comparison_prompt(ad: dict, sku: dict) -> str:
    product_type = ad.get("product_type", "tea")
    is_tea = product_type == "tea"

    sides = ad.get("sides", {})
    left = sides.get("left", {})
    right = sides.get("right", {})
    left_points = "\n".join(f"  {_fill(p, ad)}" for p in left.get("points", []))
    right_points = "\n".join(f"  {_fill(p, ad)}" for p in right.get("points", []))

    if is_tea:
        ref_line = (
            f"REFERENCE IMAGE 1: This is the ACTUAL Alcami Elements {sku['name']} canister. "
            f"Reproduce this exact cylindrical canister with photographic accuracy — "
            f"the ALCAMI ELEMENTS wordmark, the botanical mushroom engraving, "
            f"the {sku['canister_desc']}, and all label text. At least 35% of image height."
        )
        if sku.get("gradient_note"):
            ref_line += f"\n{sku['gradient_note']}"
    else:
        ref_line = (
            f"REFERENCE IMAGE 1: This is the ACTUAL Alcami Elements {sku['name']} pouch. "
            f"Reproduce with photographic accuracy. At least 35% of image height."
        )

    visual = ad.get("visual", "clean cream #FFFDF5 background, premium and minimal — the comparison does the work")
    price_line = _get_price_line(ad, sku)
    cta_line = _get_cta_line(ad)
    night_cup_line = _get_night_cup_line(ad, sku)
    category_line = _category_line(ad, sku)
    big = ad.get("headline") or ad["hook"]
    secondary = _subhead_emphasis_chips(ad, big, with_chips=True)

    prompt = f"""You are a world-class advertising art director creating a structured comparison advertisement for Alcami Elements {sku['name']}{" tea" if is_tea else ""}.

{ref_line}

The line "{big}" is the HEADLINE — render it as the largest text on the canvas, with no label or quote marks drawn.{secondary}

VISUAL DIRECTION (not text to render): {visual}
{_archetype_line(ad)}
COMPARISON LAYOUT — two clearly separated columns, structured and designed:

LEFT — "{left.get('label', 'Before')}":
{left_points}

RIGHT — "{right.get('label', 'Alcami')}":
{right_points}

The product ({sku['name']}) appears prominently on the RIGHT side — it is the answer, not decoration.

TYPOGRAPHY HIERARCHY (non-negotiable):
· Hook/headline above the comparison: LARGEST text on canvas. Dominant. Stops the scroll. Bold, condensed, high-contrast.
· Column headers ("{left.get('label', 'Before')}" / "{right.get('label', 'Alcami')}"): bold condensed — ~60% of headline size. Each in its own panel or clearly defined zone.
· Bullet text: clean regular weight — ~30% of headline size. Readable at mobile. Never the same visual weight as headers.
· Size ratios must be clearly visible: headline dominates → headers support → bullets are information.

ROW PARALLELISM — CRITICAL:
· Every left bullet and its corresponding right bullet address THE EXACT SAME dimension or variable (e.g., row 1 = both about dose, row 2 = both about caffeine, row 3 = both about format/packaging).
· Never mix dimension types within a row pair. The rows are a direct apples-to-apples comparison.
· Left and right bullets sit at the same vertical level — perfect horizontal alignment across both columns.
· Row count left = row count right, always.

DESIGN DEPTH:
· The Alcami canister on the right has a soft drop shadow beneath it — it has physical weight and presence.
· Right column: subtle SKU color ({sku['color_hex']} at 10-15% opacity behind bullet rows) — a visual bias toward our side. Not aggressive, just clearly the winner.
· Thin horizontal divider lines between row pairs — creates structure and readability.
· Left column text: muted, slightly desaturated — the lesser option, not attacked.
· Right column: full contrast, full color — this is the answer.
· Each column header sits inside its own defined panel or zone with a contrasting background.

TONE: Confident and factual. Not aggressive. The comparison speaks for itself.
{category_line}{night_cup_line}{_stamp_line(ad)}{price_line}{cta_line}

{_hard_rules(ad)}

This should NOT look like a generic wellness comparison. It should feel like a brand presenting facts — not selling."""

    return prompt


# Shared design scaffolding for ALL blocks ads — ONE source so the two input
# shapes (clean `items` / legacy `blocks`) can never drift apart.
_BLOCKS_DESIGN_TAIL = """LAYOUT — you are a designer, not a typewriter; interpret the copy into a deliberate composition:
· Each text group is its OWN visual object (chip, card, column, or panel) — NEVER a vertical bulleted list, NEVER leading dots/dashes.
· Hierarchy must be obvious: the headline dominates, supporting items step down, proof is smallest.

DESIGN DEPTH:
· The product sits in a REAL, dimensional context — a textured surface, a soft shadow beneath it, a subtle glow behind it. NEVER a flat cutout on a plain colored fill.
· Subtle vignette at the corners draws focus to the center.

TYPOGRAPHY HIERARCHY:
· Headline: dominant, the largest element on the canvas.
· Item names ~55-65%; notes and proof smallest (~25-30%). Every level visibly distinct.
· Editorial serif (Didot/Bodoni) for the headline; clean sans-serif for item/proof text."""


def _build_blocks_prompt(ad: dict, sku: dict) -> str:
    """The ONE blocks builder. Two input shapes flow through one set of design
    rules so they cannot drift:
      · PREFERRED — `items` ([{label,note}]) + `headline` + `proof`: copy/layout
        split, the clean anti-transcription path.
      · LEGACY    — `blocks` ([{size,content}]): older free-form specs, rendered
        through the SAME scaffolding. Prefer `items` for new work."""
    is_tea = ad.get("product_type", "tea") == "tea"
    kind = "canister" if is_tea else "pouch"
    ref_line = (
        f"REFERENCE IMAGE 1: the ACTUAL Alcami Elements {sku['name']} {kind} — reproduce it with "
        f"photographic accuracy ({sku['canister_desc']}, ALCAMI ELEMENTS wordmark"
        f"{', botanical engraving' if is_tea else ', gold foil typography'}). At least 35% of image height."
    )
    if is_tea and sku.get("gradient_note"):
        ref_line += f"\n{sku['gradient_note']}"

    color      = ad.get("color_world", f"palette anchored by {sku['color_name']} {sku['color_hex']} — dominant tone, natural materials keep real colors")
    arche_line = _archetype_line(ad)
    price_line = _get_price_line(ad, sku)
    cta_line   = _get_cta_line(ad)
    night_cup_line = _get_night_cup_line(ad, sku)
    category_line = _category_line(ad, sku)

    style_key  = ad.get("style")
    style_line = f"\n{BLOCK_STYLES[style_key]}\n" if style_key in BLOCK_STYLES else ""

    if ad.get("items") is not None:
        # ── PREFERRED: copy/layout split ──
        headline    = ad.get("headline") or ad.get("hook", "")
        items       = ad.get("items", [])
        proof       = _chips(ad)
        items_block = _fmt_items(items)
        sub_emph    = _subhead_emphasis_chips(ad, headline, with_chips=False)
        proof_line  = "      ".join(proof) if proof else ""
        proof_block = f"\n  Proof (small secondary trust row):\n     {proof_line}" if proof_line else ""
        content_section = f"""TEXT TO RENDER — render ONLY these words (plus the CTA below). Do NOT draw the labels, the quote marks, or the | separator:
  Headline (largest element on the canvas):
     {headline}{sub_emph}
  Items (each its OWN discrete visual object):
{items_block}{proof_block}

· Where an item contains ' | ', the text before it is a bold name and the text after is a lighter note beneath it. Never render the | character itself."""
    else:
        # ── LEGACY: free-form blocks, normalized through the same scaffolding ──
        blocks = ad.get("blocks", [])
        block_lines = "\n".join(
            f"  {b.get('size','medium')} block: {_fill(b.get('content',''), ad)}" for b in blocks
        )
        sub_emph = _subhead_emphasis_chips(ad, ad.get("headline") or ad["hook"], with_chips=False)
        content_section = f"""HOOK: {ad['hook']}{sub_emph}

CONTENT BLOCKS — {len(blocks)} blocks, largest dominates, smaller blocks support (interpret as a layout, not a transcript):
{block_lines}"""

    prompt = f"""You are an elite advertising art director designing a premium static ad for Alcami Elements {sku['name']}{" tea" if is_tea else ""}.

{ref_line}

COLOR WORLD: {color}. The palette lives in the light, surfaces and graphic zones — the product keeps its true colors; people (if any) keep natural skin and clothing.
{arche_line}{style_line}
{content_section}

{_BLOCKS_DESIGN_TAIL}{category_line}{night_cup_line}{_stamp_line(ad)}{price_line}{cta_line}

{_hard_rules(ad)}

The result must look designed by a person with taste — structured, legible, premium — and NOT like a text document with bullet points."""
    return prompt


# ── UGC format builder ────────────────────────────────────────────────────────

def _build_ugc_prompt(ad: dict, sku: dict) -> str:
    """
    UGC-style: lower fidelity, person-centric, phone-shot feel.
    Deliberately imperfect. Feels discovered, not produced.
    Strong for cold traffic — outperforms polished photography on relatability.
    """
    product_type = ad.get("product_type", "tea")
    is_tea = product_type == "tea"

    if is_tea:
        ref_line = (
            f"REFERENCE IMAGE 1: This is the ACTUAL Alcami Elements {sku['name']} canister. "
            f"Reproduce this exact cylindrical canister accurately — "
            f"the {sku['canister_desc']}, ALCAMI ELEMENTS wordmark, and botanical engraving. "
            f"The canister must be clearly identifiable. At least 35% of image height."
        )
        if sku.get("gradient_note"):
            ref_line += f"\n{sku['gradient_note']}"
    else:
        ref_line = (
            f"REFERENCE IMAGE 1: This is the ACTUAL Alcami Elements {sku['name']} pouch. "
            f"Reproduce accurately — label, gradient, and gold foil typography. At least 35% of image height."
        )

    person = ad.get("person", "A real person — not a model, not a set")
    moment = ad.get("moment", "a natural everyday moment with the product present")
    environment = ad.get("environment", "a real home environment, natural light")

    text_in_image = ad.get("text_in_image", "")
    text_treatment = ad.get("text_treatment", "minimal, bottom of frame, plain text — no designer treatment")
    text_line = f'\nTEXT IN IMAGE: "{text_in_image}" — {text_treatment}.' if text_in_image else ""

    price_line = _get_price_line(ad, sku)
    cta_line = _get_cta_line(ad)
    night_cup_line = _get_night_cup_line(ad, sku)

    prompt = f"""You are creating a UGC-style social media advertisement for Alcami Elements {sku['name']}{" tea" if is_tea else ""}. This is NOT a polished studio ad — it should look and feel like organic content someone would discover in their feed.

{ref_line}

HOOK: {ad['hook']}

PERSON: {person}

MOMENT: {moment}

ENVIRONMENT: {environment}

AESTHETIC — critical parameters for UGC authenticity:
· Shot on a smartphone — NOT a DSLR or medium format. Slight lens distortion, natural compression.
· Imperfect framing — slightly off-center, not perfectly composed. Like a real person took it.
· Natural ambient light only — window light, room light, no studio lighting or fill cards. Ambient light temperature should carry the SKU's color tone ({sku['color_name']}).
· The product is present and clearly visible but is NOT the hero. The person and their moment are.
· Color correction: minimal. Natural skin tones, slightly warm or cool depending on the room.
· No graphic overlays, no designed text boxes, no production elements.

ENVIRONMENT RULES (non-negotiable):
· NO competing brand products visible anywhere in the frame — no food packaging (cereal boxes, condiment bottles, protein tubs), no other supplement brands, no coffee makers from competing brands, no spice racks.
· Maximum 2–3 objects on any visible surface. The Alcami product, the person, and one supporting element (a mug, a book) are the entire story.
· "Real" means authentic body language and natural light — NOT clutter. The environment feels like a real home that happens to be intentionally tidy.
· The person's face must be visible and in context — no backs to camera, no silhouettes that hide identity.
· Aspirational-real: the kind of apartment you'd want to live in, not a documentary of a messy one.{text_line}{night_cup_line}{_stamp_line(ad)}{price_line}{cta_line}

{_hard_rules(ad)}

This should look like it was filmed by a real customer — not a brand. If it looks like an ad, it has failed. If the background is cluttered with other brands' products, it has failed."""

    return prompt


# ── How It Works / Mechanism format builder ───────────────────────────────────

def _build_how_it_works_prompt(ad: dict, sku: dict) -> str:
    """
    Infographic explaining the mechanism: what the product does and how.
    Works well for skeptic-heavy audiences who need to understand before buying.
    Gemini can render this cleanly with specific, structured prompting.
    """
    product_type = ad.get("product_type", "tea")
    is_tea = product_type == "tea"

    if is_tea:
        ref_line = (
            f"REFERENCE IMAGE 1: This is the ACTUAL Alcami Elements {sku['name']} canister. "
            f"Include it prominently in the composition — the {sku['canister_desc']}, "
            f"ALCAMI ELEMENTS wordmark, botanical engraving. At least 35% of image height."
        )
        if sku.get("gradient_note"):
            ref_line += f"\n{sku['gradient_note']}"
    else:
        ref_line = (
            f"REFERENCE IMAGE 1: This is the ACTUAL Alcami Elements {sku['name']} pouch. "
            f"Include it prominently in the composition. At least 35% of image height."
        )

    steps = ad.get("steps", [])
    steps_desc = "\n".join(
        f"  Step {i+1}: {_fill(step['label'], ad)} — {_fill(step.get('detail', ''), ad)}"
        for i, step in enumerate(steps)
    )

    color = ad.get("color_world", f"{sku['color_name']} {sku['color_hex']} — clean and legible")
    price_line = _get_price_line(ad, sku)
    cta_line = _get_cta_line(ad)
    night_cup_line = _get_night_cup_line(ad, sku)
    category_line = _category_line(ad, sku)
    big = ad.get("headline") or ad["hook"]
    secondary = _subhead_emphasis_chips(ad, big, with_chips=True)

    prompt = f"""You are a world-class advertising art director creating an infographic-style mechanism advertisement for Alcami Elements {sku['name']}{" tea" if is_tea else ""}. This ad explains HOW the product works through a clean visual flow.

{ref_line}

HEADLINE (largest text on canvas, above the steps): {big}{secondary}

COLOR WORLD: {color}
{_archetype_line(ad)}
INFOGRAPHIC LAYOUT — {len(steps)} steps in a clear vertical or horizontal flow:
{steps_desc}

DESIGN DEPTH:
· The product canister/pouch at the conclusion of the flow has a soft drop shadow — it sits on the ground plane.
· Each step is inside a defined container: a rounded-rectangle card, a numbered circle + attached content panel, or a clearly bordered row. Steps are design objects, not floating text lines.
· Color zone separation: the step flow area has a slightly different background tone from the product area — creates visual separation between mechanism and answer.
· Subtle vignette at canvas corners — draws the eye to the central flow.

DESIGN DIRECTION — critical for legibility:
· The hook/headline above the steps: LARGEST text on canvas. Dominant. Stops the scroll.
· Each step has a large bold step number (①②③) as the visual anchor — the biggest element within each step card.
· Step labels: bold, large, high-contrast — readable at mobile size without zooming. ~60% of headline size.
· Between steps: a simple directional arrow or connecting line — no decorative complexity.
· Each step's detail text is smaller but fully legible — ~25% of headline size. Never same weight as labels.
· The product appears at the END of the flow as the answer — the physical conclusion of the steps.
· Background: clean, minimal — the infographic content is the visual. No competing imagery.
· ALL TEXT must be crisp, correctly spelled, perfectly aligned. If text is not legible, the ad fails.

TYPOGRAPHY HIERARCHY:
· Headline : step label : detail body = 5 : 2.5 : 1 (size ratio, clearly visible).
· Step numbers are bolder and larger than the step labels they precede.
· Clean bold sans-serif for step labels. Regular weight sans-serif for detail. High contrast throughout.
{category_line}{night_cup_line}{_stamp_line(ad)}{price_line}{cta_line}

{_hard_rules(ad)}

This should feel like a premium brand explaining something clearly — not a supplement warning label. Structure is the design."""

    return prompt


# ── Spec validation ─────────────────────────────────────────────────────────
# Enforces the brand/format rules that previously lived only in prose. Called by
# gen.py: warnings always print; errors block real generation (not --dry-run).

VALID_FORMATS = {"scene", "comparison", "blocks", "ugc", "how_it_works"}

# Fields whose text is actually RENDERED in the creative (vs. art-direction notes
# like `scene`/`visual_action` that only guide the model and are never drawn).
def _rendered_texts(ad: dict) -> list:
    out = []
    if ad.get("hook"):           out.append(("hook", ad["hook"]))
    if ad.get("headline"):       out.append(("headline", ad["headline"]))
    if ad.get("subhead"):        out.append(("subhead", ad["subhead"]))
    if ad.get("text_in_image"):  out.append(("text_in_image", ad["text_in_image"]))
    if ad.get("stamp"):          out.append(("stamp", ad["stamp"]))
    for i, st in enumerate(ad.get("stats", [])):
        out.append((f"stats[{i}]", str(st)))
    for side in ("left", "right"):
        for p in ad.get("sides", {}).get(side, {}).get("points", []):
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
        errors.append(f"{fid}: blocks format needs a 'blocks' list (legacy) or an 'items' list (clean path)")
    if fmt == "blocks" and ad.get("blocks") and ad.get("items") is None:
        warnings.append(f"{fid}: uses legacy 'blocks' list — prefer the 'items' copy/layout-split path (cleaner design, avoids document-look). Both still render through one builder.")
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

    # ── Hook quality ──
    hook = (ad.get("hook") or "").strip()
    if hook:
        if len(hook.split()) < 3:
            warnings.append(f"{fid}: hook is very short — may be a fragment: '{hook}'")
        if hook[-1] not in ".?!":
            warnings.append(f"{fid}: hook doesn't end with . ? ! — may be a fragment: '{hook}'")

    # ── stamp: opt-in urgency/news device — must reflect a TRUE state ──
    if ad.get("stamp"):
        warnings.append(f"{fid}: stamp '{ad['stamp']}' — use only for a literally true state "
                        f"(real restock / new launch / bestseller); never manufacture scarcity.")

    # ── style field sanity ──
    style = ad.get("style")
    if style and fmt != "blocks":
        warnings.append(f"{fid}: 'style' set but format is '{fmt}' — style only affects blocks")
    if fmt == "blocks" and style and style not in BLOCK_STYLES:
        warnings.append(f"{fid}: unknown blocks style '{style}' (use {sorted(BLOCK_STYLES)})")

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

    # ── Brand-claim guards on RENDERED text ──
    for where, text in _rendered_texts(ad):
        low = text.lower()
        if pt == "tea":
            if "200,000" in text or "200000" in text:
                errors.append(f"{fid} [{where}]: '200,000+' is a BLEND claim — tea uses 'thousands' or 4.9★")
            if "$39" in text:
                errors.append(f"{fid} [{where}]: '$39' is the blend price — tea anchor is 'From $37.40/month'")
            if sku == "morning" and "caffeinated" in low:
                errors.append(f"{fid} [{where}]: Morning is caffeine-FREE — never 'caffeinated'")
            if sku == "night" and "fall asleep faster" in low:
                errors.append(f"{fid} [{where}]: Night = parasympathetic, not sedation — never 'fall asleep faster'")
            if sku == "trifecta" and "try all three" in low:
                errors.append(f"{fid} [{where}]: Trifecta is ONE product — never 'try all three' (use 'Get the Trifecta')")
            import re as _re_mg
            if _re_mg.search(r"\d+\s*mg", low):
                errors.append(f"{fid} [{where}]: specific mg dose on tea — the site publishes none. Use ingredient name/function, not '250mg'.")
        else:  # blend
            if "$37.40" in text or "37.40" in text:
                errors.append(f"{fid} [{where}]: '$37.40' is the tea price — blend anchor is 'From $39/month'")
        # Universal rendered-text hygiene
        if "—" in text or "–" in text:
            warnings.append(f"{fid} [{where}]: contains en/em dash — house style is hyphen '-': '{text[:50]}…'")
        if "·" in text:
            warnings.append(f"{fid} [{where}]: contains '·' bullet in rendered text — remove for clean copy: '{text[:50]}…'")
        import re as _re
        if _re.search(r"\d+\s*(reviews|ratings)", low):
            warnings.append(f"{fid} [{where}]: review COUNT in image text — use star rating only (4.9★)")

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
    return all_errors, all_warnings


# ── Main entry point ──────────────────────────────────────────────────────────

def build_prompt(ad: dict) -> str:
    """
    Build a full Gemini prompt from a slim ad spec.

    Required fields in ad spec:
        file         — output filename (e.g. "01_night_permission.png")
        sku          — tea: "morning"/"afternoon"/"night"/"trifecta"
                       blend: "original"/"cacao"/"matcha"/"espresso"
        product_type — "tea" (default) or "blend"
        format       — "scene" / "comparison" / "blocks" / "ugc" / "how_it_works"
        hook         — the one line the ad is built from. Outcome-focused, complete thought.

    Format-specific required fields:
        scene:         scene, visual_action
        comparison:    sides (dict with left/right labels + points lists)
        blocks:        blocks (list of {size, content} dicts)
        ugc:           person, moment, environment
        how_it_works:  steps (list of {label, detail} dicts)

    Optional fields (all formats):
        text_in_image   — text to show in the image creative
        text_treatment  — how that text appears ("minimal bottom-left" etc.)
        has_cup         — True if a brewed cup appears (triggers a natural warm-cup note for night — never indigo)
        price           — True/False
        price_style     — "pill" / "footnote" / "band" (default: "pill")
        cta             — CTA text (default: "Shop Now")
        cta_style       — "button" / "button_right" / "pill" / "pill_right" /
                          "text_link" / "integrated" / "none"  (all render as
                          self-contained buttons; the full-width band is retired)
        extra_refs      — list of {"key": "path"} dicts for additional reference images
        color_world     — override for blocks/how_it_works format color description
        visual          — override for comparison format visual description
        associative     — True suppresses the forced category cue (mood-led mode)
        stamp           — opt-in overlay stamp text ("RESTOCK"/"NEW"/"BESTSELLER");
                          use ONLY for a literally true state (validator warns)

    Design archetypes (see DESIGN_ARCHETYPES / `gen.py --policy`):
        editorial · spec_card · annotated · color_block · badge · ugc_minimal ·
        testimonial · social_proof · poster · screenshot · before_after

    blocks sub-styles (set via style field, affects opening framing):
        "ingredient_breakdown" — botanical visual + ingredient list with effects
        "benefit_highlights"   — outcome-led checklist or bullet list
        "social_proof"         — proof elements dominate (badges, ratings, stats)
        "testimonial_text"     — customer quote as the dominant element
    """
    sku = _get_sku(ad)
    fmt = ad.get("format", "scene")

    # Default an archetype when the spec omits one, so the graphic-variety system
    # is actually exercised instead of falling back to a generic look.
    if not ad.get("archetype"):
        ad = {**ad, "archetype": _default_archetype(fmt, ad.get("style"), ad.get("audience", "acquisition"))}

    if fmt == "scene":
        return _build_scene_prompt(ad, sku)
    elif fmt == "comparison":
        return _build_comparison_prompt(ad, sku)
    elif fmt == "blocks":
        return _build_blocks_prompt(ad, sku)   # one builder, both input shapes
    elif fmt == "ugc":
        return _build_ugc_prompt(ad, sku)
    elif fmt == "how_it_works":
        return _build_how_it_works_prompt(ad, sku)
    else:
        raise ValueError(f"Unknown format type: '{fmt}'. Use: 'scene', 'comparison', 'blocks', 'ugc', 'how_it_works'.")
