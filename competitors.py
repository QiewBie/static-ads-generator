"""Competitor registry — one source of truth for rival intel + comparison-creative assets.

Two concerns, one schema:
  · RENDER fields (name, ref_key, ref_path, form_factor, contrast) — read by the engine
    (prompt_builder) to build a comparison ad. Present ONLY on brands we hold an asset for
    (a `ref_path`); those are the render-capable rivals a spec may name via `competitor:`.
  · INTEL fields (tier, positioning, ad_style, keywords, page_id, last_pulled, deep_dive) —
    the competitive landscape humans + the research skill read. Present on every brand.

CLAUDE.md and research point HERE instead of restating the tables (kills the drift surface).
Add a rival's pouch/logo to assets/competitors_assets/ + the render fields to make it
comparison-capable. `keywords` feed Scrape Creators; `last_pulled` flags stale intel.
"""

COMPETITORS = {
    # ── Render-capable (we hold a pouch asset) — the engine can build a comparison ──
    "ag1": {
        "name":        "AG1",
        "ref_key":     "comp_ag1",
        "ref_path":    "assets/competitors_assets/ag1_pouch.png",
        "form_factor": "tall white single-serve greens pouch",
        "contrast":    "cool clinical green-and-white",
        "tier":        "broader",
        "positioning": "Greens powder, daily foundation nutrition",
        "ad_style":    "Endorsement-heavy, authority play, high production",
        "keywords":    "AG1 Athletic Greens",
        "page_id":     None,        # Scrape Creators Meta Ad Library page_id (fill when pulled)
        "last_pulled": None,        # ISO date of the last live-ad pull
        "deep_dive":   "research/competitor-im8-ag1.md",
    },
    "im8": {
        "name":        "IM8",
        "ref_key":     "comp_im8",
        "ref_path":    "assets/competitors_assets/im8_pouch.png",
        "form_factor": "dark premium stick-pack pouch",
        "contrast":    "deep burgundy-crimson",
        "tier":        "broader",
        "positioning": "Premium daily nutrition, science-heavy",
        "ad_style":    "Structured badge+headline+checkrow layout, trust-forward",
        "keywords":    "IM8 daily nutrition",
        "page_id":     None,
        "last_pulled": None,
        "deep_dive":   "research/competitor-im8-ag1.md",
    },

    # ── Intel-only (no asset yet) — landscape reference; NOT render-capable ──
    "ryze": {
        "name": "RYZE", "tier": "direct",
        "positioning": "#1 mushroom coffee by volume, heavy social proof",
        "ad_style": "Pain-point headlines, before/after progression, deal blocks",
        "keywords": "RYZE Superfoods mushroom coffee", "page_id": None, "last_pulled": None, "deep_dive": None,
    },
    "mudwtr": {
        "name": "MUD\\WTR", "tier": "direct",
        "positioning": "Coffee alternative, rebellious/anti-coffee",
        "ad_style": "Confrontational headlines, fake editorial, caffeine comparison infographics",
        "keywords": "MUDWTR coffee alternative", "page_id": None, "last_pulled": None, "deep_dive": None,
    },
    "everyday_dose": {
        "name": "Everyday Dose", "tier": "direct",
        "positioning": "'Mushroom latte' branding, lifestyle-focused",
        "ad_style": "Instructional grid (step-by-step), vibrant color panels",
        "keywords": "Everyday Dose mushroom latte", "page_id": None, "last_pulled": None, "deep_dive": None,
    },
    "four_sigmatic": {
        "name": "Four Sigmatic", "tier": "direct",
        "positioning": "OG mushroom coffee brand, ingredient-forward",
        "ad_style": "Ingredient callouts, earth tones, functional copy",
        "keywords": "Four Sigmatic mushroom coffee", "page_id": None, "last_pulled": None, "deep_dive": None,
    },
    "cymbiotika": {
        "name": "Cymbiotika", "tier": "broader",
        "positioning": "Premium supplements, lifestyle-aspirational",
        "ad_style": "Zero text / pure lifestyle photography",
        "keywords": "Cymbiotika supplements", "page_id": None, "last_pulled": None, "deep_dive": None,
    },
    "bloom": {
        "name": "Bloom Nutrition", "tier": "broader",
        "positioning": "Women's wellness, greens/energy",
        "ad_style": "UGC-style, vibrant, community-driven",
        "keywords": "Bloom Nutrition", "page_id": None, "last_pulled": None, "deep_dive": None,
    },
    "onnit": {
        "name": "Onnit", "tier": "broader",
        "positioning": "Performance supplements (Alpha Brain)",
        "ad_style": "Bold identity-based, athlete endorsement",
        "keywords": "Onnit Alpha Brain", "page_id": None, "last_pulled": None, "deep_dive": None,
    },
    "thesis": {
        "name": "Thesis", "tier": "broader",
        "positioning": "Personalized nootropics",
        "ad_style": "Us-vs-them, clinical comparison, direct response",
        "keywords": "Thesis nootropics", "page_id": None, "last_pulled": None, "deep_dive": None,
    },
}
