# ─────────────────────────────────────────────────────────────────────────────
# Alcami — Campaign Config TEMPLATE (blend + tea, acquisition + retarget)
#
# Copy a campaign section into batches/blend.py or batches/tea.py, rename it,
# write your specs. No new files per campaign — campaigns are keys in CAMPAIGNS.
#
# Run:
#   python3 gen.py batches/<file>.py                      ← list campaigns
#   python3 gen.py batches/<file>.py --campaign NAME --dry-run
#   python3 gen.py batches/<file>.py --campaign NAME --only 03 07
#   python3 gen.py batches/<file>.py --campaign NAME --force
#   python3 gen.py --policy                               ← formats/archetypes/audience
#
# THE TWO AUTHORITIES (don't restate their rules in specs):
#   prompt_builder.py  — formats, design archetypes, audience policy, price anchors,
#                        SKU color worlds, all hard rules, the validator.
#   CLAUDE.md          — brand, product facts, voice, ICP.
#
# KEY FIELDS
#   file          output filename (zero-padded prefix lets --only target it)
#   product_type  "blend" or "tea"   → drives price anchor, SKU set, claim guards
#   sku           blend: original/cacao/matcha/espresso · tea: morning/afternoon/night/trifecta
#   audience      set on the CAMPAIGN ("acquisition" default | "retarget"); ads inherit it
#   format        scene · comparison · blocks · ugc · how_it_works
#   archetype     (optional, recommended) editorial · spec_card · annotated · color_block ·
#                 badge · ugc_minimal · testimonial · social_proof   (see --policy)
#   hook          ONE complete sentence the ad is built from (outcome, not ingredient)
#
# COPY/LAYOUT-SPLIT (the clean path that stops "looks like a document"):
#   For blocks, prefer `headline` + `items` + `proof` over the legacy `blocks` list.
#   items: list of {"label": "...", "note": "..."} — the engine tells the model to
#   DESIGN them as objects, never as a bulleted list. Reference the hook with {hook}.
#
# PRICE IS THE EXCEPTION: default "price": False. Only True on structured/comparison
#   ads that earned trust first. Atmospheric/emotional scenes: always False.
# ─────────────────────────────────────────────────────────────────────────────

CAMPAIGNS = {

    # ══ ACQUISITION example campaign (cold audience) ═════════════════════════════
    "my_campaign": {
        "run_id": None,
        "audience": "acquisition",      # ads inherit this; the validator checks format fit
        "ads": [

            # ── scene (blend) — atmospheric, price OFF ────────────────────────
            {
                "file": "01_coffee_replacement.png",
                "product_type": "blend",
                "sku": "original",
                "format": "scene",
                "archetype": "editorial",
                "hook": "My coffee maker has been unplugged for two months.",
                "scene": "A kitchen counter where a coffee maker used to be. Morning light, one object, clean surface.",
                "visual_action": "The pouch occupies the coffee maker's old spot — the choice already made.",
                "text_in_image": "Two months. No coffee.",
                "text_treatment": "condensed bold, top-left, cream",
                "cta": "Shop Now",
                "cta_style": "pill",
                "price": False,
            },

            # ── blocks via CLEAN items path (tea) — annotated archetype ────────
            # The recommended way to do "what's inside" without a bulleted list.
            {
                "file": "02_night_inside.png",
                "product_type": "tea",
                "sku": "night",
                "format": "blocks",
                "archetype": "annotated",
                "hook": "What's actually in Alcami Night Tea.",
                "headline": "What's actually inside",
                "items": [
                    {"label": "REISHI", "note": "parasympathetic support, fewer 2am wake-ups"},
                    {"label": "CHAMOMILE + LAVENDER", "note": "the nervous system finally closes"},
                    {"label": "BUTTERFLY PEA FLOWER", "note": "a warm, naturally rich herbal steep"},
                ],
                "proof": ["4.9 stars", "USDA Organic", "Caffeine-free"],
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # ── comparison (tea) — parallel rows, price earned ────────────────
            {
                "file": "03_morning_vs_tea.png",
                "product_type": "tea",
                "sku": "morning",
                "format": "comparison",
                "archetype": "spec_card",
                "hook": "Your morning tea has no dose. This one does.",
                "sides": {
                    "left": {
                        "label": "Regular morning tea",
                        "points": ["Flavor only, no function", "No mushroom dose", "Still need coffee after"],
                    },
                    "right": {
                        "label": "Alcami Morning",
                        "points": ["Real Cordyceps lift", "Caffeine-free, no spike", "Whole-leaf pyramid sachet"],
                    },
                },
                "visual": "warm amber-gold world; pyramid sachet vs. a plain flat tea bag.",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": True,
                "price_style": "pill",
            },

            # ── ugc (blend) — cold-traffic relatability, no in-image CTA ───────
            {
                "file": "04_morning_ugc.png",
                "product_type": "blend",
                "sku": "original",
                "format": "ugc",
                "archetype": "ugc_minimal",
                "hook": "I swapped my third coffee for this and the jitters stopped.",
                "person": "A person early-30s, casual, no studio styling",
                "moment": "in the kitchen mid-morning, holding a latte mug, pouch on the counter",
                "environment": "real apartment kitchen, natural window light",
                "text_in_image": "No more 11am crash.",
                "text_treatment": "plain caption text, bottom",
                "cta": "Shop Now",
                "cta_style": "none",
                "price": False,
            },

            # ── testimonial (tea) — ACQUISITION ONLY (validator warns on retarget) ─
            {
                "file": "05_afternoon_testimonial.png",
                "product_type": "tea",
                "sku": "afternoon",
                "format": "blocks",
                "archetype": "testimonial",
                "hook": "The 3pm dip just stopped.",
                "headline": "The 3pm dip just stopped.",
                "items": [{"label": "Verified customer", "note": "Afternoon Ritual, 3 months in"}],
                "proof": ["4.9 stars", "Lion's Mane for focus"],
                "cta": "Shop Now",
                "cta_style": "pill",
                "price": False,
            },

        ],
    },

    # ══ RETARGET example campaign (warm — they already bought) ═══════════════════
    # Audience = field, not a file. Validator flags ugc/testimonial/social_proof here.
    "my_retarget_campaign": {
        "run_id": None,
        "audience": "retarget",
        "ads": [

            # how_it_works (tea) — the circadian argument for people who know the blend
            {
                "file": "01_trifecta_day.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "how_it_works",
                "archetype": "color_block",
                "hook": "We made Alcami teas for the whole day.",
                "steps": [
                    {"label": "7 AM Morning",    "detail": "Cordyceps, slow-rising lift"},
                    {"label": "12 PM Afternoon", "detail": "Lion's Mane, focus to 5pm"},
                    {"label": "9 PM Night",      "detail": "Reishi, the day closes"},
                ],
                "color_world": "three SKU colors flowing left to right: amber, sage, navy",
                "cta": "Get the Trifecta",
                "cta_style": "button",
                "price": False,
            },

        ],
    },

}
