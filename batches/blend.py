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
# Core blend angles:
#   · Coffee replacement (no jitter, no crash, still sharp)
#   · Supplement stack elimination (9 things, one ritual)
#   · Earned trust vs. celebrity credibility (200K real customers, no podcast deals)
#   · Taste as compliance (you actually look forward to this one)
#   · Transparency vs. proprietary blends (10:1 extract, every dose disclosed)
#
# Hooks already live — use fresh angles, not these:
#   "Tired of running on empty?" / "Anti-Lazy Formula" / "9 super-herbs & mushrooms"
# ─────────────────────────────────────────────────────────────────────────────

CAMPAIGNS = {

    # ── energized_v1 — loud, colorful, high-energy cold acquisition ───────────
    # Blend "declare" register turned up: bold color-block zones, borrowed-frame
    # hooks, vivid benefits, stacked proof, product as the glowing resolution.
    # No UGC (its undesigned look fights the vibrant brief). Price off — none of
    # these are price concepts. Competitor brands may be named (people may not).
    "energized_v1": {
        "run_id": "blend_acquisition_batch2",
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

    # ── vs_ag1_v1 — Alcami blend vs AG1 (premium greens / daily foundational nutrition) ─
    # Cold acquisition. `competitor: "ag1"` brings AG1 in as the CONTRAST (greens-pouch form
    # + name in text, never a logo); Alcami is the resolution. People are never named — the
    # trust angle rides our own 200k. Fact-grounded (research/competitor-im8-ag1.md): AG1
    # $79/mo, 75 ingredients, proprietary blend, acquired/earthy greens taste, celebrity-led.
    # 6 angles: taste · transparency · dose-over-quantity · job-to-be-done · value · earned trust.
    "vs_ag1_v1": {
        "run_id": "blend_acquisition_batch3",
        "audience": "acquisition",
        "ads": [

            # 01 — comparison · taste -> daily compliance (lead)
            {
                "file": "01_latte_you_crave.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "color_block", "competitor": "ag1",
                "hook": "A greens shot, or a latte you crave?",
                "headline": "Greens you tolerate, or a latte you crave?",
                "emphasis": {"crave": "gold"},
                "sides": {
                    "left":  {"label": "AG1",    "points": ["An earthy greens taste", "A shot to get down", "Easy to skip"]},
                    "right": {"label": "Alcami", "points": ["Creamy cacao, matcha, espresso", "A ritual you look forward to", "Easy to keep daily"]},
                },
                "visual": "bold color-block split: the AG1 greens pouch muted on a cool green-white left, the Alcami Original pouch + a creamy latte glowing on a warm cream-gold right.",
                "cta": "Shop Now", "cta_style": "button", "price": False,
            },

            # 02 — scene · transparency (two products, Alcami hero)
            {
                "file": "02_every_dose_on_label.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial", "competitor": "ag1",
                "hook": "One hides the doses. One puts them on the label.",
                "headline": "Every dose on the label.",
                "subhead": "AG1 hides its doses in a proprietary blend. We disclose all 9, at 10:1.",
                "emphasis": {"Every dose": "gold"},
                "scene": "A clean, bright tabletop. The Alcami Original pouch front-and-center with its ingredient panel readable; the AG1 greens pouch smaller and muted to the side.",
                "visual_action": "Our label faces the camera, open and legible; theirs is turned and closed — transparency made literal.",
                "cta": "See the label", "cta_style": "text_link", "price": False,
            },

            # 03 — poster · dose over quantity
            {
                "file": "03_nine_at_ten_x.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster", "competitor": "ag1",
                "hook": "75 ingredients, or 9 at a dose you'll feel?",
                "headline": "9 ingredients. 10x the dose.",
                "subhead": "AG1 spreads thin across 75. We go deep on 9, at 10:1.",
                "emphasis": {"10x the dose": "gold"},
                "scene": "A bold typographic poster: a giant '9' and '10x' on a warm cream-gold field, the Alcami Original pouch crisp below; the AG1 greens pouch tiny and muted in a corner as the busy contrast.",
                "visual_action": "Two numbers carry the ad; quantity loses to dose.",
                "cta": "Shop Now", "cta_style": "integrated", "price": False,
            },

            # 04 — scene · different job (coffee, not a multivitamin)
            {
                "file": "04_not_a_multivitamin.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial", "competitor": "ag1",
                "hook": "It's not your multivitamin. It's your coffee.",
                "headline": "Not a multivitamin. Your coffee.",
                "subhead": "AG1 fills nutrient gaps. Alcami replaces the jitters and the 3pm crash.",
                "emphasis": {"Your coffee": "gold"},
                "scene": "A morning kitchen counter where the coffee used to be: a creamy Alcami latte in a warm ceramic mug and the Original pouch in warm light; the AG1 greens pouch off to one side as the other, separate category.",
                "visual_action": "Alcami takes the coffee's place — the mug and pouch together; the greens pouch is clearly a different job, set apart.",
                "has_cup": True,
                "cta": "Make the swap", "cta_style": "pill", "price": False,
            },

            # 05 — comparison · value (price lives in the comparison concept)
            {
                "file": "05_half_the_price.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "spec_card", "competitor": "ag1",
                "hook": "Same daily ritual. Less than half the price.",
                "headline": "Half the price. Nothing hidden.",
                "emphasis": {"Half the price": "gold"},
                "sides": {
                    "left":  {"label": "AG1",    "points": ["$79 a month", "Doses hidden in a blend", "NSF Certified"]},
                    "right": {"label": "Alcami", "points": ["From $39 a month", "Every dose disclosed", "NSF Certified"]},
                },
                "visual": "clean spec-card comparison: the Alcami Original pouch prominent on the right, the AG1 greens pouch muted on the left.",
                "cta": "Shop Now", "cta_style": "button_right", "price": False,
            },

            # 06 — poster · earned trust (names AG1 brand + our 200k; never a person)
            {
                "file": "06_earned_trust.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster", "competitor": "ag1",
                "hook": "AG1 buys the spotlight. We earned 200,000 customers.",
                "headline": "200,000 reasons to trust us.",
                "subhead": "AG1 buys the spotlight. We earned 200,000 customers, one morning at a time.",
                "emphasis": {"200,000 reasons": "gold"},
                "scene": "A bold typographic poster on a warm cream field: '200,000' enormous across the frame, the Alcami Original pouch crisp below; the AG1 greens pouch small and muted in a corner.",
                "visual_action": "The number is the whole ad; the pouch is the receipt.",
                "cta": "Shop Now", "cta_style": "integrated", "price": False,
            },

        ],
    },

    # ── vs_im8_v1 — Alcami blend vs IM8 (premium all-in-one "replaces 16 supplements") ─
    # Cold acquisition. `competitor: "im8"` brings IM8 in as the CONTRAST (dark stick-pack
    # form + name in text, never a logo); Alcami is the resolution. People are never named.
    # Fact-grounded: IM8 $79/mo, 90 ingredients, proprietary blend, a stir-in-water sachet
    # (fruity — so the wedge is RITUAL, not a taste-knock), celebrity/authority-led.
    # 6 angles: ritual · transparency · value · focus/coffee-replacement · dose-spread · earned trust.
    "vs_im8_v1": {
        "run_id": "blend_acquisition_batch4",
        "audience": "acquisition",
        "ads": [

            # 01 — scene · ritual / experience (IM8 is a fruity sachet — wedge is ritual, not taste)
            {
                "file": "01_a_ritual_not_a_routine.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial", "competitor": "im8",
                "hook": "A sachet stirred in water, or a ritual you look forward to?",
                "headline": "A ritual, not a routine.",
                "subhead": "IM8 is a sachet to stir and drink. Alcami is a creamy latte you actually look forward to.",
                "emphasis": {"ritual": "gold"},
                "scene": "A warm, inviting morning: a creamy Alcami latte mid-pour into a warm ceramic mug, the Original pouch on a wood counter; the IM8 stick-pack sits flat and muted to the side.",
                "visual_action": "Ours is a sensory moment — steam, cream, warmth, the mug being filled; theirs is a functional packet, set apart.",
                "has_cup": True,
                "cta": "Try Alcami", "cta_style": "pill_right", "price": False,
            },

            # 02 — comparison · transparency
            {
                "file": "02_doses_you_can_see.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "spec_card", "competitor": "im8",
                "hook": "90 ingredients you can't see, or 9 you can?",
                "headline": "Every dose on the label.",
                "emphasis": {"Every dose": "gold"},
                "sides": {
                    "left":  {"label": "IM8",    "points": ["90 ingredients in a blend", "Doses you can't see", "Proprietary formula"]},
                    "right": {"label": "Alcami", "points": ["9 adaptogens, named", "Every dose disclosed", "10:1 extracts, shown"]},
                },
                "visual": "clean spec-card comparison: the Alcami Original pouch prominent on the right, the IM8 stick-pack muted on the left.",
                "cta": "See the label", "cta_style": "button", "price": False,
            },

            # 03 — comparison · value (price lives in the comparison concept)
            {
                "file": "03_half_the_price.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "color_block", "competitor": "im8",
                "hook": "Same daily ritual. Less than half the price.",
                "headline": "Half the price. Nothing hidden.",
                "emphasis": {"Half the price": "gold"},
                "sides": {
                    "left":  {"label": "IM8",    "points": ["$79 a month", "Doses hidden in a blend", "NSF Certified"]},
                    "right": {"label": "Alcami", "points": ["From $39 a month", "Every dose disclosed", "NSF Certified"]},
                },
                "visual": "bold color-block comparison: the Alcami Original pouch full-contrast on a warm cream-gold right, the IM8 stick-pack muted on a cool burgundy left.",
                "cta": "Shop Now", "cta_style": "button_right", "price": False,
            },

            # 04 — scene · focus / coffee replacement (IM8 = replace everything)
            {
                "file": "04_we_do_mornings.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial", "competitor": "im8",
                "hook": "Replace 16 supplements, or just fix your mornings?",
                "headline": "We don't do everything. We do mornings.",
                "subhead": "IM8 replaces 16 supplements. Alcami replaces your coffee: calm, focused energy, no crash.",
                "emphasis": {"mornings": "gold"},
                "scene": "A focused morning counter: a single creamy Alcami latte in a warm ceramic mug and the Original pouch in warm light; the IM8 stick-pack sits among a muted scatter of other products, busy and secondary.",
                "visual_action": "One clear morning ritual in focus — the mug and pouch, clean and intentional; their do-everything pile fades back.",
                "has_cup": True,
                "cta": "Make the swap", "cta_style": "text_link", "price": False,
            },

            # 05 — poster · dose spread thin
            {
                "file": "05_spread_thin.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster", "competitor": "im8",
                "hook": "90 ingredients, spread thin. Or 9 at 10:1.",
                "headline": "90 ingredients, spread thin.",
                "subhead": "IM8 spreads across 90. Alcami goes deep on 9, at a dose you feel.",
                "emphasis": {"spread thin": "gold"},
                "scene": "A bold typographic poster: a fractured, thinly-scattered '90' on a cool burgundy field versus a solid, confident '9' with the Alcami Original pouch crisp below; the IM8 stick-pack small and muted.",
                "visual_action": "The fractured 90 versus the solid 9 — spread thin versus a dose you feel.",
                "cta": "Shop Now", "cta_style": "integrated", "price": False,
            },

            # 06 — poster · earned trust (names IM8 brand + our 200k; never a person)
            {
                "file": "06_earned_not_announced.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster", "competitor": "im8",
                "hook": "IM8 launched with headlines. We earned 200,000 customers.",
                "headline": "Earned, not announced.",
                "subhead": "IM8 launched with headlines. Alcami earned 200,000 customers, one morning at a time.",
                "emphasis": {"not announced": "gold"},
                "scene": "A bold typographic poster on a warm cream field: 'Earned, not announced.' large, the Alcami Original pouch crisp below; the IM8 stick-pack small and muted in a corner.",
                "visual_action": "Quiet confidence — the words and the pouch, no fanfare.",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

        ],
    },

    # ── tired_parents_v1 — depleted-parent cold acquisition, relief register ─────
    # Audience: exhausted parents running on broken sleep + too much coffee (wired AND
    # tired). The blend's wedge: anti-jitter calm energy + "one scoop IS the whole
    # routine" + the guilt-free minutes that are theirs. Register: honest, a little
    # selfish, funny — but the copy always NAMES THE STAKES (keeps me afloat, happy mom
    # again, surviving 5pm), never just a possessive joke or a native vibe.
    # Every ad carries the parent match IN the ad (kids in frame or parent copy) — the
    # landing page is generic. ORIGINAL pouch only (single-flavor site). Coffee is the
    # villain ("no third coffee"), never the product noun — no "latte" in rendered text.
    # The proven beat is ad 07: a parent-specific outcome in plain words + proof.
    # Claims stay surgically true: calm/"yelled less" only in first-person VOICE (rides
    # the 89% enhanced-calm proof), never a brand claim; the blend is anti-jitter, NOT a
    # sleep aid and NOT caffeine-free; before/after shows emotional state, never physique
    # (Meta supplement policy). Delivery note: dad-targeted cuts (06) need dad-specific
    # primary text at deliverables time, or the targeting is wasted.
    "tired_parents_v1": {
        "run_id": "blend_acquisition_batch5",
        "audience": "acquisition",
        "ads": [

            # 01 — scene / editorial · original — the hidden lifeline (visual proven; copy names the stakes)
            {
                "file": "01_hidden_behind_protein.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "The thing that keeps me afloat is hidden behind the kids' snacks.",
                "headline": "The thing that keeps me afloat.",
                "subhead": "Hidden behind the kids' snacks, where nobody ever looks.",
                "emphasis": {"keeps me afloat": "gold"},
                "scene": "A bright, real family kitchen cabinet shelf in pale wood and cream: the Alcami Original pouch pulled forward and fully visible, front label facing out and well-lit, while a kids' cereal box, snack pouches, and a small toy sit duller behind and beside it. Clean morning daylight.",
                "visual_action": "The Original pouch sits a step in front of the kids' stuff — lit, in focus, obviously the one thing that matters; the kids' clutter is the dull background it's been hidden among. The gold foil catches the light so the pouch reads premium against the shelf.",
                "color_world": "a bright, airy family kitchen — pale wood, cream, soft daylight; warm but light, NOT a dark pantry. The pouch's gold foil typography is the brightest accent on the shelf",
                "camera": "eye-level, the pouch clearly front-and-center, sharp and well-lit",
                "cta": "Claim yours", "cta_style": "text_link", "price": False,
            },

            # 02 — scene / before_after · original — the client-approved emotional split:
            #      same kids, same hour, a different mom. EMOTIONAL state only, never
            #      physique; both halves honest (overwhelmed ≠ horror, calm ≠ bliss).
            {
                "file": "02_same_kids_different_mom.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "before_after",
                "hook": "My kids didn't get calmer. I did.",
                "headline": "Same kids. Same 7am. Different mom.",
                "subhead": "One creamy scoop before they wake up.",
                "emphasis": {"Different mom": "gold"},
                "scene": "An honest split of the same family breakfast table at 7am. LEFT (before): cereal chaos mid-spill, a crying toddler reaching, the mom rubbing her forehead, frazzled but human - muted, cooler light. RIGHT (after): the same table, the mess settled, the mom relaxed and genuinely smiling as she reads a picture book to the same kids, the Alcami Original pouch and a warm creamy mug at her place - warm, bright light.",
                "visual_action": "The split makes one argument: nothing about the kids changed, the mom did. The pouch and mug sit only on the right side - the visible difference between the two halves.",
                "color_world": "left half muted and cool-toned; right half warm cream and gold daylight - the same room, two emotional temperatures",
                "cta": "Start your mornings", "cta_style": "pill", "price": False,
            },

            # 03 — scene / editorial · original — calm parent in the kids' chaos, WITH the
            #      product explained (the designed slot that says what this actually is)
            {
                "file": "03_outnumbered_still_calm.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "I'm outnumbered three to one, and I'm still the calm one.",
                "headline": "Outnumbered. Still calm.",
                "subhead": "Nine adaptogens in one creamy scoop. Steady energy, no jitters.",
                "emphasis": {"Still calm": "gold"},
                "proof": ["10:1 extracts", "4.9★"],
                "scene": "A real morning kitchen: a parent leans against the counter mid-sip, genuinely relaxed, while two kids blur past in playful chaos in the soft background - a toy mid-air, breakfast in progress. The Alcami Original pouch stands sharp and well-lit on the counter beside the parent's warm creamy mug.",
                "visual_action": "The chaos is soft and in motion; the parent and the pouch are still and in focus - the eye lands on the one calm point in the room, and the subhead explains why it exists.",
                "color_world": "a bright real family kitchen, warm cream and pale wood, morning daylight; the kids' motion blurred, the parent and product crisp",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "button_right", "price": False,
            },

            # 04 — ugc · original — relief, the selfish ten minutes (kids named in copy AND
            #      visible by their traces; the pouch unmistakably in use)
            {
                "file": "04_before_the_kids.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "I wake up before my kids now. Not for them. For me.",
                "person": "A real parent in their late 30s, tired but content, no makeup, worn t-shirt, holding a warm mug — natural body language, face visible.",
                "moment": "The quiet ten minutes before the house wakes — sitting at the kitchen table with a warm creamy drink, the opened Alcami Original pouch clearly in use beside the mug, label readable. A high chair and a small scatter of kids' toys sit soft in the background.",
                "environment": "A real lived-in family kitchen at early dawn, soft window light, cream tones — the kids' traces visible but quiet.",
                "text_in_image": "Not for my kids. For me.",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

            # 05 — ugc · original — calm, honest humor; copy lands the payoff (happy mom again)
            {
                "file": "05_nobody_yelled.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "One cup and nobody got yelled at before 8am. I'm a happy mom again.",
                "person": "A parent mid-morning with a genuine, relieved smile, holding a warm creamy mug — natural, unposed, face visible.",
                "moment": "A candid kitchen moment, the kids' breakfast aftermath soft in the background, the parent taking a calm sip — the opened Alcami Original pouch in use on the counter, label readable.",
                "environment": "A real family kitchen, morning, natural light, warm cream tones.",
                "text_in_image": "One cup. Happy mom again.",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

            # 06 — ugc · original — the calm dad, kids' chaos staged around him (the parent
            #      match lives in the frame; dad-specific primary text at delivery)
            {
                "file": "06_less_of_a_gremlin.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "My kids are louder than ever. I'm just less of a gremlin by 9am.",
                "person": "A bleary but genuinely smiling dad, half-awake and human, holding a warm creamy mug — leaning on the counter, face visible, visibly the calm point of the room.",
                "moment": "Mid-morning chaos around him: two kids tearing past in the soft background mid-game, breakfast debris on the table — while he stands still and content mid-sip, the opened Alcami Original pouch in use on the counter beside him.",
                "environment": "A real family kitchen, morning, natural light, warm neutral tones — the kids' motion soft, the dad and pouch clear.",
                "text_in_image": "Less of a gremlin by 9am.",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

            # 07 — scene / testimonial · original — blunt, the customer voice as hero
            {
                "file": "07_never_write_reviews.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "testimonial",
                "hook": "I never write reviews. This is the first in years.",
                "headline": "I never write reviews. I wrote this one.",
                "subhead": "First thing in two years that got me through 4pm with the kids. No third coffee. No crash.",
                "emphasis": {"wrote this one": "gold"},
                "proof": ["4.9★"],
                "scene": "A clean, designed review card on a warm cream surface: a large customer quote as the hero, a small 4.9-star row beneath it, and the Alcami Original pouch resting beside the card as quiet confirmation. Nothing else on the surface — no camera, no phone, no devices, no extra props.",
                "visual_action": "The quote leads; the outcome line below tells a stranger exactly what it did for a tired parent; the pouch confirms which product. Just the card and the pouch — no other objects in frame.",
                "cta": "Read the reviews", "cta_style": "ghost_right", "price": False,
            },

            # 08 — scene · original — skeptic flip that lands on a PARENT outcome
            {
                "file": "08_annoyingly_isnt.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "I wanted it to be another overpriced wellness thing. It got me through 5pm with the kids.",
                "headline": "I wanted it to be another overpriced wellness thing.",
                "subhead": "Annoyingly, it got me through 5pm with the kids.",
                "emphasis": {"got me through 5pm": "gold"},
                "scene": "A real kitchen counter shot like a quick phone photo: a just-made creamy drink beside the opened Alcami Original pouch, a kid's sippy cup and a crayon drawing taped to the fridge at the frame's edge, ordinary late-afternoon light, a little imperfect - not a studio product shot.",
                "visual_action": "The made drink and opened pouch sit casually, as if the skeptic just made the day's second cup; the kid traces at the edges quietly say who needed to get through 5pm. The accented line lands the flip.",
                "color_world": "a real ordinary family kitchen, warm cream tones, a slightly imperfect phone-photo look - not glossy or studio-lit",
                "camera": "shot on a phone, eye-level, natural and a little imperfect - not a polished studio shot",
                "lighting": "flat natural window light, no studio fill",
                "cta": "Shop Now", "cta_style": "text_link", "price": False,
            },

            # 09 — ugc · original — anti-perfect-routine, relief
            {
                "file": "09_ninety_seconds.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "No ice bath. No journaling. Ninety seconds and I'm a person again.",
                "person": "A parent in pajamas, unpretentious, mid-task making the latte — natural, face visible.",
                "moment": "Frothing and stirring the Original latte at the counter, casual and ordinary.",
                "environment": "A real ordinary kitchen, morning, cream tones, natural window light.",
                "text_in_image": "Ninety seconds. I'm a person again.",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

            # 10 — comparison / color_block · original — simplicity, one scoop IS the routine
            {
                "file": "10_twelve_steps_or_one.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "color_block",
                "hook": "One scoop replaced the whole morning shelf.",
                "headline": "One scoop replaced the whole shelf.",
                "emphasis": {"One scoop": "gold"},
                "sides": {
                    "left":  {"label": "A basic parent's morning",     "points": ["Five bottles, a checklist", "Twenty minutes you don't have", "Skipped by Tuesday"]},
                    "right": {"label": "An Alcami parent's morning",   "points": ["One scoop, ninety seconds", "Nine adaptogens in one", "Done before they're awake"]},
                },
                "visual": "bold color-block split: a cluttered, muted row of supplement bottles and a crumpled checklist on the left; the Alcami Original pouch glowing on a warm cream-gold right with a single calm latte mug beside it.",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "button", "price": False,
            },

        ],
    },

    # ── glp1_v1 — GLP-1 companion, cold acquisition (VISUAL-LED) ─────────────────
    # Audience: people on a GLP-1 routine whose appetite + energy have cratered —
    # coffee turns on their stomach, the body forgets to eat, food brings less joy,
    # the supplement stack grows. The blend's wedge: a warm, gentle, low-acid cup that
    # goes down easy — calm jitter-free energy + the canonical GUT BALANCE — a pleasant
    # ritual that fits the new life, never posing as protein / weight-loss / meal-replacement.
    #
    # FAST-RECOGNITION RULE (the job of every ad): a GLP-1 user scrolling must clock
    # "this is for me" in one second. Two requirements per ad, no exceptions:
    #   (1) "GLP-1" is NAMED in rendered text (headline, subhead, comparison label, or caption).
    #   (2) the FRAME carries a recognizable GLP-1 signal — the abandoned coffee, the
    #       "eat something" reminder, the morning supplement stack, the before/after
    #       morning — OR it is a clean type POSTER whose statement names the subject.
    # No atmospheric cup-in-nice-light ad that reads as generic wellness.
    #
    # ONE IDEA PER AD, NO TWINS: nine distinct looks for nine GLP-1 truths — never the
    # same frame+format twice, never a native label with no stake (every line names what
    # CHANGES, not just who it's for). Each ad earns its slot on a different truth:
    #   01 coffee aversion (comparison) · 02 energy on little food (first-person outcome
    #   + proof) · 03 food brings less joy (intimate scene) · 04 cravings quiet, energy
    #   gap (poster) · 05 the whole morning, before/after (emotional split) · 06 sensitive
    #   stomach (gut spec card) · 07 the body forgets to eat (desk + phone) · 08 the
    #   supplement stack (UGC) · 09 nine-in-one, fewer bottles (numeral poster).
    # CTA treatment varied across the batch (a 4th divergence axis).
    #
    # COMPLIANCE SPINE: "GLP-1" is third-person POSITIONING only ("Built for the GLP-1
    # stomach", "for GLP-1 days") — never a second-person status question ("are you on
    # GLP-1?"), never a drug brand, never a treatment/weight claim. Coffee is the villain
    # (an abandoned coffee is a fair contrast); the warm cup is always the resolution —
    # no unappetizing food, no plate, nobody who reads as ill (a "before" half is low-
    # energy/foggy, never sick, and the contrast is the MORNING/mood, never the body).
    "glp1_v1": {
        "run_id": "blend_acquisition_batch6",
        "audience": "acquisition",
        "ads": [

            # 01 — comparison / spec_card · original — coffee on a GLP-1 stomach vs. the gentle cup
            #      (THE most actionable GLP-1 truth: coffee becomes nauseating. Visual = cold
            #      abandoned coffee, muted left · warm Alcami cup + pouch, full-contrast right.)
            {
                "file": "01_coffee_vs_gentle.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "spec_card",
                "hook": "On a GLP-1 routine, coffee can turn on you. This doesn't.",
                "sides": {
                    "left": {
                        "label": "Coffee on a GLP-1 stomach",
                        "points": ["Acid on an empty stomach", "Queasy before noon", "A jittery, hollow lift"],
                    },
                    "right": {
                        "label": "Alcami in the morning",
                        "points": ["Creamy and low-acid", "Settles easy, no nausea", "Calm, steady energy"],
                    },
                },
                "visual": "a clean two-cup split: on the LEFT a cold, dull, abandoned mug of black coffee in muted grey light; on the RIGHT the Original pouch and a fresh creamy warm cup in bright full-contrast light. The warm cup clearly wins.",
                "cta": "Make the swap", "cta_style": "button", "price": False,
            },

            # 02 — blocks / testimonial · original — first-person lived outcome + proof
            #      (the register that WON the parents batch: a specific, true GLP-1 moment in
            #      plain words, a real customer voice, one star-rating proof. Energy on almost
            #      no food — the appetite-suppression core truth, not coffee, not 3pm.)
            {
                "file": "02_barely_eat.png",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "archetype": "testimonial",
                "hook": "Some mornings I barely eat. This keeps me steady anyway.",
                "headline": "Some mornings I barely eat. This keeps me steady anyway.",
                "subhead": "Calm, caffeine-free energy for GLP-1 days.",
                "emphasis": {"keeps me steady": "gold"},
                "items": [{"label": "Verified customer", "note": "GLP-1 morning routine"}],
                "proof": ["4.9★"],
                "cta": "Read the reviews", "cta_style": "ghost_right", "price": False,
            },

            # 03 — scene / editorial · original — food brings less joy, the cup is the pleasure
            #      (intimate WARM register — distinct from the bright desk/before-after scenes.
            #      Names a real GLP-1 truth: eating is complicated now; the warm cup stays simple.
            #      Never sad/restrictive — the cup is a genuine pleasure, not a consolation.)
            {
                "file": "03_eating_got_complicated.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "Eating got complicated. This stayed simple.",
                "headline": "Eating got complicated. This didn't.",
                "subhead": "The one easy pleasure in a GLP-1 morning.",
                "emphasis": {"This didn't": "gold"},
                "scene": "An intimate, close, warm moment: a creamy golden Original latte cradled in two hands in soft low light, the opened Alcami pouch just behind on a warm wood surface, its gold foil catching the light. Cozy, content, unhurried. No food, no plate — the warm cup is the pleasure.",
                "visual_action": "The cradled cup reads as the small daily pleasure that still works when eating brings less joy; the warm intimate light makes the cup the glowing center and the gold foil the accent.",
                "color_world": "warm cream and gold, soft low daylight, intimate and calm",
                "has_cup": True,
                "cta": "Make it yours", "cta_style": "text_link", "price": False,
            },

            # 04 — scene / poster · original — the problem/solution turn (cravings quiet, energy gap)
            {
                "file": "04_quieted_not_the_crash.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "hook": "GLP-1 quieted the cravings. The 3pm crash is on its own.",
                "headline": "GLP-1 quieted the cravings. Not the 3pm crash.",
                "subhead": "Clean afternoon energy, no caffeine.",
                "emphasis": {"Not the 3pm crash": "gold"},
                "scene": "The Original pouch on a clean warm-toned background with bold negative space for the statement type.",
                "visual_action": "The two-beat line dominates the frame; the pouch is the smaller resolving subject below it.",
                "color_world": "warm cream and gold, clean and graphic",
                "cta": "Fix the dip", "cta_style": "arrow_down", "price": False,
            },

            # 05 — scene / before_after · original — the whole morning, honest emotional split
            #      (the client-APPROVED parents register: same person, two morning states. The
            #      contrast is ENERGY/MOOD and the MORNING, never the body, never illness — the
            #      "before" is flat/foggy/drained-but-human, the "after" calm and present. Pouch
            #      + cup live only on the right: the visible difference between the halves.)
            {
                "file": "05_before_after_morning.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "before_after",
                "hook": "The GLP-1 mornings got easier when one thing changed.",
                "headline": "Same 7am. Same GLP-1. Different morning.",
                "subhead": "One warm cup before the day starts.",
                "emphasis": {"Different morning": "gold"},
                "scene": "An honest split of the same person at the same kitchen counter at 7am. LEFT (before): flat, foggy and low-energy, head propped on a hand, a cold pushed-aside mug, nothing appealing - muted, cooler light (drained but human, never sick). RIGHT (after): the same person upright, calm and genuinely present, both hands around a warm creamy Original latte with the opened pouch beside it - warm, bright light.",
                "visual_action": "The split makes one argument: nothing about the morning changed, the energy did. The pouch and warm cup sit only on the right - the visible difference between the two halves.",
                "color_world": "left half muted and cool-toned; right half warm cream and gold daylight - the same kitchen, two emotional temperatures",
                "cta": "Start your mornings", "cta_style": "pill", "price": False,
            },

            # 06 — blocks / annotated · original — built for the GLP-1 stomach (gut balance + low-acid)
            #      (the one designed-information ad: the "what's inside / why it's gentle" card for
            #      skeptics who want to understand the fit before buying.)
            {
                "file": "06_built_for_the_stomach.png",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "archetype": "annotated",
                "hook": "Gut balance and calm energy, gentle on a sensitive stomach.",
                "headline": "Built for the GLP-1 stomach.",
                "subhead": "Gut balance and calm energy, gentle by design.",
                "emphasis": {"GLP-1 stomach": "gold"},
                "items": [
                    {"label": "GUT BALANCE + IMMUNITY", "note": "the daily support, right on the pouch"},
                    {"label": "LOW-ACID, NO CAFFEINE", "note": "nothing that fights a tender stomach"},
                    {"label": "WARM + CREAMY", "note": "goes down easy when little else does"},
                ],
                "proof": ["NSF Certified", "Gut balance + immunity"],
                "has_cup": True,
                "cta": "See what's inside", "cta_style": "pill", "price": False,
            },

            # 07 — scene / editorial · original — "eat something" reminder + the easy answer (desk)
            #      (the phone reminder is the single most-recognized GLP-1 moment: the body forgets
            #      to eat. Diegetic prop; the warm cup is the answer — energy without a meal. The
            #      line names the reality in third person, never a flip wink.)
            {
                "file": "07_eat_something.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "Some days the body forgets to eat. The day doesn't stop.",
                "headline": "Some days the body forgets to eat.",
                "subhead": "Clean GLP-1 energy, no meal required.",
                "emphasis": {"forgets to eat": "gold"},
                "scene": "An afternoon desk: a phone face-up shows a gentle calendar reminder that reads 'Eat something'; beside it a warm creamy Original latte and the opened Alcami pouch, soft daylight. Calm, not clinical. No food in frame.",
                "visual_action": "The phone reminder names the GLP-1 reality — the body forgets to eat; the warm cup sits right beside it as the easy answer, energy without a meal.",
                "color_world": "a calm home workspace, warm neutral tones, soft afternoon daylight",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "text_link", "price": False,
            },

            # 08 — ugc / ugc_minimal · original — the GLP-1 morning stack, Alcami the part you feel
            #      (the supplement-stack spread is THE purchase-motivated GLP-1 visual — Alcami
            #      belongs in that frame. Other containers plain/unbranded; the pouch is the hero.
            #      The caption names a STAKE — the one they look forward to — not just "easiest".)
            {
                "file": "08_morning_stack.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "Most of my GLP-1 stack is a chore. This is the part I look forward to.",
                "person": "A real person in their 30s-40s at a kitchen counter, casual and content, unstyled, face visible.",
                "moment": "Reaching for a warm creamy Original latte among a small morning supplement lineup — a couple of plain, unbranded protein/vitamin containers nearby — with the opened Alcami pouch front and clearly readable; the made cup is the one they actually want.",
                "environment": "A real lived-in kitchen counter, morning light, cream tones.",
                "text_in_image": "the one I look forward to in my GLP-1 stack",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

            # 09 — scene / poster · original — nine adaptogens, one scoop (fewer bottles)
            {
                "file": "09_nine_simplified.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "hook": "Nine adaptogens in one scoop, instead of nine more bottles.",
                "headline": "9 adaptogens. One scoop.",
                "subhead": "The GLP-1 routine, simplified.",
                "emphasis": {"9": "gold"},
                "scene": "The Original pouch on a clean warm-toned background, with the numeral 9 as a massive graphic element dominating the composition.",
                "visual_action": "The oversized 9 is the hero; 'adaptogens, one scoop' resolves it; the pouch sits below, smaller but clearly present.",
                "color_world": "warm cream and gold, bold and graphic",
                "cta": "Simplify it", "cta_style": "text_link", "price": False,
            },

        ],
    },

}
