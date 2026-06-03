# ─────────────────────────────────────────────────────────────────────────────
# Alcami Blend — Campaign Config
#
# All blend (Creamy Mushroom Latte) campaigns live here as named sections.
# Four flavors: original / cacao / matcha / espresso
#
# Run: python3 gen.py batches/blend.py --campaign <name>
#
# Price anchor for all blend ads: "From $39/month"
# Social proof: 200,000+ customers · 200,000+ five-star reviews
# Certifications: NSF Certified · GMP · Third-party lab tested
# Guarantee: 90 days
#
# Blend creative register vs. tea:
#   Blend declares — loud, confrontational, relief-driven
#   Tea observes — quiet, precise, recognition-driven
#   Blend ads can be bold and direct where tea ads are atmospheric and earned
#
# Core blend angles (all still valid — don't repeat currently running hooks):
#   · Coffee replacement (no jitter, no crash, still sharp)
#   · Supplement stack elimination (9 things, one ritual)
#   · Earned trust vs. celebrity credibility (200K real customers, no podcast deals)
#   · Taste as compliance (you actually look forward to this one)
#   · Transparency vs. proprietary blends (10:1 extract, every dose disclosed)
#
# Currently running (avoid repeating):
#   "Tired of running on empty?" / "Anti-Lazy Formula" / "9 super-herbs & mushrooms"
# ─────────────────────────────────────────────────────────────────────────────

CAMPAIGNS = {

    # ── main_v2 — replaces batch_main_product.py with slim spec format ─────────
    # Run: python3 gen.py batches/blend.py --campaign main_v2
    "main_v2": {
        "run_id": None,
        "ads": [

            # Coffee replacement — direct, confrontational, acquisition
            {
                "file": "01_coffee_replacement.png",
                "sku": "original",
                "product_type": "blend",
                "format": "scene",
                "hook": "My coffee maker is unplugged. Has been for two months.",
                "scene": "A kitchen counter. The original blend pouch where a coffee maker used to be. Clean surface, one object, morning light. The absence of the coffee maker is part of the composition.",
                "visual_action": "The pouch occupies the counter space a coffee maker would. The choice already made.",
                "text_in_image": "Two months. No coffee.",
                "text_treatment": "condensed ultra-bold, top-left, cream — confrontational, direct",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "pill_bottom",
                "price": True,
                "price_style": "pill",
            },

            # Stack elimination — 9 adaptogens angle
            {
                "file": "02_nine_things.png",
                "sku": "original",
                "product_type": "blend",
                "format": "scene",
                "hook": "Nine adaptogens. One morning. No more shelf of supplements.",
                "scene": "A kitchen counter showing 9 separate supplement bottles arranged in a row — then the Alcami pouch alone at the end. The contrast is visual and immediate.",
                "visual_action": "The 9 bottles fill the left, the single pouch sits at the right. The visual math is obvious without labels.",
                "text_in_image": "All 9. One scoop.",
                "text_treatment": "bold sans-serif two lines, left-aligned, near-black",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": True,
                "price_style": "band",
            },

            # Earned trust — no celebrities, real customers
            {
                "file": "03_earned_trust.png",
                "sku": "original",
                "product_type": "blend",
                "format": "scene",
                "hook": "200,000 customers. Zero celebrity endorsements. Just results.",
                "scene": "The original pouch on a warm cream surface, soft studio light. Premium, clean, no props. The pouch is the proof.",
                "visual_action": "The pouch speaks without context. No lifestyle, no scene. The hook carries the argument.",
                "text_in_image": "200,000 mornings.\nZero celebrity deals.",
                "text_treatment": "editorial high-contrast serif, centered, near-black — confident, factual",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "pill_bottom",
                "price": True,
                "price_style": "pill",
            },

            # Taste — cacao flavor, ritual compliance angle
            {
                "file": "04_cacao_taste.png",
                "sku": "cacao",
                "product_type": "blend",
                "format": "scene",
                "hook": "The only supplement you'll actually look forward to.",
                "scene": "A ceramic mug of cacao latte blend on a dark wooden surface. Steam rising. The cacao pouch beside it. Near-black to bronze color world. Morning mood, intimate.",
                "visual_action": "The mug is the subject — the ritual moment. The pouch is the explanation. The steam is the product working.",
                "text_in_image": "You'll look forward to this one.",
                "text_treatment": "light italic serif, bottom-left, cream — sounds like a real recommendation",
                "has_cup": False,
                "cta": "Try it",
                "cta_style": "pill_bottom_right",
                "price": False,
            },

            # AG1 comparison — direct, without naming
            {
                "file": "05_ag1_comparison.png",
                "sku": "original",
                "product_type": "blend",
                "format": "comparison",
                "hook": "Their trial showed no benefit. Ours showed 84% reported more energy.",
                "sides": {
                    "left": {
                        "label": "The green powder you've heard of",
                        "points": [
                            "$2.63/day",
                            "Proprietary blend — doses undisclosed",
                            "1 flavor. Earthy. Polarizing.",
                            "Own trial: 'no clinical benefit' (2024)",
                            "Active class action over subscriptions",
                        ],
                    },
                    "right": {
                        "label": "Alcami Elements",
                        "points": [
                            "$1.30/day",
                            "10:1 extract — every dose disclosed",
                            "4 flavors. Actually tastes good.",
                            "84% more energy · 78% better focus",
                            "90-day guarantee. Cancel anytime.",
                        ],
                    },
                },
                "visual": "warm cream #FFFDF5 background. Original pouch large on right. Near-black type throughout.",
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": True,
                "price_style": "pill",
            },

            # Matcha flavor — clean, focused, identity
            {
                "file": "06_matcha_focused.png",
                "sku": "matcha",
                "product_type": "blend",
                "format": "scene",
                "hook": "Clean energy. No crash. Tastes like matcha, works like nothing matcha ever did.",
                "scene": "A matcha latte in a clean white ceramic cup on a light stone surface. The matcha pouch behind it. Sage-green ambient light. Minimal, considered.",
                "visual_action": "The drink looks like matcha — familiar, approachable. The pouch makes it clear it's more than matcha. The tension is the hook.",
                "text_in_image": "Matcha. But it actually does something.",
                "text_treatment": "clean bold sans-serif, top-right, near-black — direct, slightly skeptic-breaking",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "pill_bottom",
                "price": False,
            },

            # NSF / transparency — proof-focused, trust-building
            {
                "file": "07_nsf_proof.png",
                "sku": "original",
                "product_type": "blend",
                "format": "blocks",
                "hook": "We didn't skip the test. NSF Certified. Every batch, third-party.",
                "blocks": [
                    {"size": "large", "content": "Original pouch centered on cream surface, soft studio light — clean and premium"},
                    {"size": "medium", "content": "Hook text in editorial serif: 'We didn't skip the test.'"},
                    {"size": "small", "content": "Proof strip: 'NSF Certified · GMP Facility · Third-party lab tested · 90-day guarantee'"},
                ],
                "color_world": "warm cream #FFFDF5 — premium and clean",
                "cta": "Shop Now",
                "cta_style": "pill_bottom",
                "price": True,
                "price_style": "pill",
            },

            # 3pm crash — afternoon angle for the blend
            {
                "file": "08_3pm_crash.png",
                "sku": "original",
                "product_type": "blend",
                "format": "scene",
                "hook": "The 3pm crash is built into the morning choice. Change the morning.",
                "scene": "A person's hand reaching for a coffee cup at what should be 3pm — but stopping. The Alcami original pouch is on the desk beside it. The choice interrupted.",
                "visual_action": "The hand stops mid-reach. The Alcami pouch is the reason. The crash was prevented before the day started.",
                "text_in_image": "The crash starts at 7am.",
                "text_treatment": "bold condensed sans-serif, top-left, near-black — the reveal, the insight",
                "has_cup": False,
                "cta": "Change the morning",
                "cta_style": "integrated",
                "price": False,
            },

        ],
    },

    # ── energized_v1 — loud, colorful, high-energy cold acquisition ───────────
    # Blend "declare" register turned up: bold color-block zones, borrowed-frame
    # hooks, vivid benefits, stacked proof, product as the glowing resolution.
    # No UGC (its undesigned look fights the vibrant brief). Price off — none of
    # these are price concepts. Competitor brands may be named (people may not).
    "energized_v1": {
        "run_id": None,
        "audience": "acquisition",
        "ads": [

            # 01 — comparison / color_block · original — the supplement-shelf villain
            {
                "file": "01_shelf_vs_scoop.png",
                "sku": "original",
                "product_type": "blend",
                "format": "comparison",
                "archetype": "color_block",
                "hook": "Nine bottles every morning, or one scoop?",
                "emphasis": {"one scoop": "gold"},
                "sides": {
                    "left": {
                        "label": "Your supplement shelf",
                        "points": ["Nine bottles to keep straight", "A fistful of pills every morning", "Half of them quietly expire"],
                    },
                    "right": {
                        "label": "One scoop of Alcami",
                        "points": ["Nine adaptogens in one", "One drink you look forward to", "30 mornings a pouch"],
                    },
                },
                "visual": "high-energy color-block split: a chaotic pile of dull, muted pill bottles on the left, struck through; the Original pouch glowing on a bold, saturated warm-gold zone on the right.",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 02 — blocks / social_proof · original — the count as hero
            {
                "file": "02_200k_quit_shelf.png",
                "sku": "original",
                "product_type": "blend",
                "format": "blocks",
                "archetype": "social_proof",
                "hook": "200,000 people quit the supplement shelf.",
                "headline": "200,000 quit the shelf.",
                "subhead": "Nine adaptogens. One scoop. One ritual.",
                "emphasis": {"200,000": "gold"},
                "items": [
                    {"label": "ONE SCOOP", "note": "replaces the whole cabinet"},
                    {"label": "NO CELEBRITY", "note": "they found it and came back"},
                ],
                "proof": ["NSF Certified", "GMP Facility", "90-day guarantee"],
                "color_world": "bold, saturated warm cream-to-gold color-block zones, high energy, the number enormous",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 03 — how_it_works / color_block · espresso — the coffee curve, fixed
            {
                "file": "03_no_spike_no_crash.png",
                "sku": "espresso",
                "product_type": "blend",
                "format": "how_it_works",
                "archetype": "color_block",
                "hook": "Coffee spikes you at 8 and drops you at 11. This doesn't.",
                "headline": "All-day steady. No spike, no crash.",
                "subhead": "Bold as espresso, without the betrayal.",
                "emphasis": {"No spike, no crash": "gold"},
                "steps": [
                    {"label": "8 AM",  "detail": "A smooth lift, no caffeine spike"},
                    {"label": "11 AM", "detail": "Still steady, no crash"},
                    {"label": "3 PM",  "detail": "Focus holds, no third cup"},
                ],
                "color_world": "bold near-black espresso zones with an electric molten-gold accent flowing across, vibrant and confident",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 04 — comparison / spec_card · cacao — the 10:1 potency ladder (names rivals)
            {
                "file": "04_ratio_ladder.png",
                "sku": "cacao",
                "product_type": "blend",
                "format": "comparison",
                "archetype": "spec_card",
                "hook": "Most mushroom coffees are 1:1. Ours is 10:1.",
                "emphasis": {"10:1": "gold"},
                "sides": {
                    "left": {
                        "label": "Other mushroom coffees",
                        "points": ["RYZE, MUD\\WTR: 1:1 to 3:1", "Token, under-dosed extracts", "You barely feel it"],
                    },
                    "right": {
                        "label": "Alcami",
                        "points": ["10:1 concentrated extract", "Clinically meaningful dose", "Feel it in 20 minutes"],
                    },
                },
                "visual": "bold spec-card grid with a rising ratio ladder from 1:1 up to 10:1; the cacao pouch glowing at the top of the ladder on a rich, saturated chocolate-and-bronze zone.",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 05 — scene / color_block · cacao — taste-as-trojan-horse
            {
                "file": "05_dessert_multivitamin.png",
                "sku": "cacao",
                "product_type": "blend",
                "format": "scene",
                "archetype": "color_block",
                "hook": "It tastes like dessert and works like a multivitamin.",
                "headline": "Dessert that works like a multivitamin.",
                "subhead": "Nine adaptogens. Rich cacao. Zero sugar.",
                "emphasis": {"Dessert": "gold"},
                "scene": "A vibrant, high-energy kitchen moment: a rich cacao latte mid-pour with a glossy chocolate swirl, the cacao pouch beside it on a saturated chocolate-and-bronze color-blocked surface with a bold pop of warm gold light.",
                "visual_action": "The indulgent pour IS the hook — it looks like dessert; the pouch reveals it's actually doing the work of a shelf of supplements.",
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "button_right",
                "price": False,
            },

            # 06 — blocks / color_block · matcha — clean focus, no comedown
            {
                "file": "06_focus_no_comedown.png",
                "sku": "matcha",
                "product_type": "blend",
                "format": "blocks",
                "archetype": "color_block",
                "style": "benefit_highlights",
                "hook": "Clean focus, zero jitters, no 2pm comedown.",
                "headline": "Focus with no comedown.",
                "subhead": "Lion's Mane clarity, calm energy, no crash.",
                "emphasis": {"no comedown": "gold"},
                "items": [
                    {"label": "LION'S MANE", "note": "hours of clear focus"},
                    {"label": "NO JITTERS", "note": "calm, never wired"},
                    {"label": "NO 2PM CRASH", "note": "steady all afternoon"},
                ],
                "color_world": "vivid, saturated matcha-green color-block zones with bright cream, energetic and clean",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 07 — blocks / color_block · espresso — coffee energy, none of the chaos
            {
                "file": "07_coffee_no_chaos.png",
                "sku": "espresso",
                "product_type": "blend",
                "format": "blocks",
                "archetype": "color_block",
                "style": "benefit_highlights",
                "hook": "Coffee energy. Without the acid, the jitters, or the crash.",
                "headline": "Coffee energy. No coffee chaos.",
                "subhead": "Bold and espresso-dark, gentle on your gut.",
                "emphasis": {"No coffee chaos": "gold"},
                "items": [
                    {"label": "NO JITTERS", "note": "calm, focused energy"},
                    {"label": "NO ACID", "note": "easy on your stomach"},
                    {"label": "NO 3PM CRASH", "note": "steady till evening"},
                ],
                "color_world": "bold near-black espresso zones with an electric warm-amber accent, high contrast and high energy",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 08 — scene / badge · original — the quality flex
            {
                "file": "08_didnt_skip_the_test.png",
                "sku": "original",
                "product_type": "blend",
                "format": "scene",
                "archetype": "badge",
                "hook": "We didn't skip the test. Every batch, third-party.",
                "headline": "We didn't skip the test.",
                "subhead": "NSF Certified. Every single batch.",
                "emphasis": {"didn't skip": "gold"},
                "scene": "A bold, premium hero: the Original pouch glowing on a vibrant cream-and-gold color-blocked surface, crisp directional light, clean certification seals arranged around it.",
                "visual_action": "The pouch presented like a tested, certified product — confident and loud, the seals as the proof, nothing to hide.",
                "proof": ["NSF Certified", "GMP Facility", "Third-party tested"],
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 09 — blocks / social_proof · matcha — the outcome stat
            {
                "file": "09_84_percent_energy.png",
                "sku": "matcha",
                "product_type": "blend",
                "format": "blocks",
                "archetype": "social_proof",
                "hook": "84% reported more energy. Here's the number.",
                "headline": "84% felt more energy.",
                "subhead": "From 200,000+ real customers. No celebrity, no hype.",
                "emphasis": {"84%": "gold"},
                "items": [
                    {"label": "78%", "note": "sharper focus"},
                    {"label": "89%", "note": "calmer, less stress"},
                ],
                "proof": ["NSF Certified", "90-day guarantee"],
                "color_world": "bold, saturated matcha-green and cream color zones, energetic, the percentage enormous",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 10 — comparison / color_block · original — transparency vs proprietary
            {
                "file": "10_every_dose_disclosed.png",
                "sku": "original",
                "product_type": "blend",
                "format": "comparison",
                "archetype": "color_block",
                "hook": "Proprietary blend, or every dose on the label?",
                "emphasis": {"every dose": "gold"},
                "sides": {
                    "left": {
                        "label": "Greens powders and blends",
                        "points": ["Proprietary blend, hidden doses", "One earthy flavor", "Self-reported, not tested"],
                    },
                    "right": {
                        "label": "Alcami",
                        "points": ["Every dose disclosed, 10:1", "Four flavors you crave", "NSF, third-party tested"],
                    },
                },
                "visual": "bold color-block comparison: a blacked-out 'proprietary' label on the muted left, the Original pouch with a clear, readable ingredient panel glowing on a bright color zone right.",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

        ],
    },

    # ── giveaway_v4 — placeholder, replace batch_giveaway_v3 when needed ──────
    # "giveaway_v4": {
    #     "run_id": None,
    #     "ads": [],
    # },

}
