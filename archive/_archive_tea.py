# ─────────────────────────────────────────────────────────────────────────────
# Alcami Tea — ARCHIVED campaigns (v4, retarget_v4/v5/v6)
#
# Pre-launch-strategy tea campaigns, kept for reference only. Several specs use
# mg doses the validator now blocks, so these will not regenerate as-is. Their
# generated images live in ad-workspace/. Not part of active rotation.
# To revive one: copy it into batches/tea.py and strip any "<n>mg" from rendered text.
# ─────────────────────────────────────────────────────────────────────────────

CAMPAIGNS = {

    # ── v4 — first campaign using the new spec system ─────────────────────────
    # 10 ads. Mix of SKUs and formats. Each starts from a real human outcome.
    # Run: python3 gen.py batches/tea.py --campaign v4
    "v4": {
        "run_id": None,
        "ads": [

            # Night — bedside scene, quiet domestic, no text competing
            {
                "file": "01_night_bedside.png",
                "sku": "night",
                "product_type": "tea",
                "format": "scene",
                "hook": "I stopped waking up at 2am. Week two on this, it stopped.",
                "scene": "A wooden bedside table at 9pm. The navy canister sits in a small pool of lamplight. A closed book beside it. The room is dark beyond the lamp.",
                "visual_action": "The lamp illuminates only the canister and the book — everything else falls into deep navy shadow. The canister is the last decision of the day.",
                "text_in_image": "The 2am wake-ups stopped.",
                "text_treatment": "small cream italic, bottom-left, near-invisible — confirms the image",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "text_line",
                "price": False,
            },

            # Morning — kitchen moment, coffee comparison, real behavior
            {
                "file": "02_morning_no_coffee.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "scene",
                "hook": "My coffee maker has been unplugged for three weeks.",
                "scene": "A kitchen counter at 7am. The amber-gold canister stands where a coffee maker used to be. Morning window light cuts across the surface.",
                "visual_action": "The canister occupies the space a coffee maker would. The absence of the coffee maker is part of the image — a clean counter, one object, a choice made.",
                "text_in_image": "Three weeks. No coffee.",
                "text_treatment": "clean sans-serif, top-left, cream on warm gold — short, factual",
                "has_cup": False,
                "cta": "Try it",
                "cta_style": "pill_bottom_right",
                "price": False,
            },

            # Afternoon — desk scene, 3pm outcome, person present
            {
                "file": "03_afternoon_desk.png",
                "sku": "afternoon",
                "product_type": "tea",
                "format": "scene",
                "hook": "My 3pm used to mean a third coffee. Now it doesn't.",
                "scene": "A clean desk at 3pm. The sage-green canister, a brewed cup of tea, an open laptop. A woman's hands are on the keyboard — she is mid-thought, not mid-slump.",
                "visual_action": "She is at 3pm and still in it. Not surviving the afternoon — working in it. The canister explains why.",
                "text_in_image": "3pm. Still in it.",
                "text_treatment": "editorial italic serif, top-right, near-black on sage — quiet and specific",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "pill_bottom",
                "price": False,
            },

            # Night — chemistry moment, indigo cup, no person needed
            {
                "file": "04_night_indigo_pour.png",
                "sku": "night",
                "product_type": "tea",
                "format": "scene",
                "hook": "The cup turns indigo. That's butterfly pea flower — and it's the least interesting thing this tea does.",
                "scene": "Overhead macro: hot water pouring into a white ceramic cup. The liquid turns from clear to deep indigo blue as it contacts the sachet. Navy surface beneath, steam rising.",
                "visual_action": "The color transformation happening in real time — clear water becoming indigo. The sachet string draped over the rim. No canister needed — the product is demonstrating itself.",
                "text_in_image": "",
                "has_cup": True,
                "cta": "See what it does",
                "cta_style": "text_line",
                "price": False,
            },

            # Trifecta — comparison format, one herb vs three windows
            {
                "file": "05_trifecta_comparison.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "comparison",
                "hook": "Your morning tea and your night tea shouldn't be the same tea.",
                "sides": {
                    "left": {
                        "label": "Regular tea",
                        "points": [
                            "One blend. Any time.",
                            "No functional dose",
                            "Your 7am and 9pm treated the same",
                            "Mostly flavored water",
                        ],
                    },
                    "right": {
                        "label": "Alcami Ritual",
                        "points": [
                            "Morning: Cordyceps — cellular lift",
                            "Afternoon: Lion's Mane — focus that holds",
                            "Night: Reishi — the day closes properly",
                            "200–250mg per sachet. Fruit-body extract.",
                        ],
                    },
                },
                "visual": "clean cream #FFFDF5 background. Trifecta canister on the right, large. Left column in near-black type, right column in near-black with gold accents.",
                "cta": "Get the Trifecta",
                "cta_style": "band_bottom",
                "price": True,
                "price_style": "pill",
            },

            # Morning — proof blocks format, social proof focused
            {
                "file": "06_morning_blocks.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "blocks",
                "hook": "The 11am crash stopped. I changed one thing.",
                "blocks": [
                    {"size": "large", "content": "The amber-gold canister centered on a warm stone surface, morning light from the left, full photographic presence"},
                    {"size": "medium", "content": "Hook text in high-contrast editorial serif: 'The 11am crash stopped. I changed one thing.'"},
                    {"size": "small", "content": "Three proof points in small clean type: '4.9★ · Thousands of mornings · Caffeine-free lift'"},
                ],
                "color_world": "warm amber-gold #E8B840 — every surface and light source carries this warmth",
                "cta": "Shop Now",
                "cta_style": "pill_bottom",
                "price": True,
                "price_style": "footnote",
            },

            # Night — minimal scene, no text in image, visual carries everything
            {
                "file": "07_night_steam.png",
                "sku": "night",
                "product_type": "tea",
                "format": "scene",
                "hook": "9pm. The day is done. The tea knows.",
                "scene": "Extreme close-up: a navy ceramic mug on a dark wooden surface. Steam rising in a single curl. Deep navy world. The canister is partially visible at the left edge, out of focus.",
                "visual_action": "The steam is the subject — one slow exhale rising from the cup. Everything else is dark and still. The canister anchors the left edge without demanding attention.",
                "text_in_image": "9pm. The day is done.",
                "text_treatment": "light italic serif, centered upper third, cream — arrives like a thought, not a headline",
                "has_cup": True,
                "cta": "Start tonight",
                "cta_style": "text_line",
                "price": False,
            },

            # Afternoon — skeptic's reframe, functional vs. regular tea
            {
                "file": "08_afternoon_not_just_tea.png",
                "sku": "afternoon",
                "product_type": "tea",
                "format": "scene",
                "hook": "You've had tea before. It didn't do this.",
                "scene": "A clean wooden desk surface. The sage canister. A brewed cup of tea. A notebook with a page of clear handwriting — mid-thought, productive. Afternoon diffused green light.",
                "visual_action": "The scene is someone mid-afternoon and still productive — the tea and the notebook tell a quiet story. The handwriting implies the focus is real.",
                "text_in_image": "You've had tea before. It didn't do this.",
                "text_treatment": "condensed bold, two lines, left-aligned, near-black — direct, not pathos",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "pill_bottom",
                "price": False,
            },

            # Trifecta — lifestyle, gift angle, person present
            {
                "file": "09_trifecta_gift.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "scene",
                "hook": "I bought it as a gift. Then kept it for myself.",
                "scene": "A kitchen table. The Trifecta canister, unwrapped, the gradient label fully visible. A note beside it. Warm cream light. The sense of something just arrived and immediately wanted.",
                "visual_action": "The canister is the center of a quiet discovery — it arrived as a gift and became a daily ritual. The unwrapping energy is present without chaos.",
                "text_in_image": "I bought it as a gift. Kept it.",
                "text_treatment": "light italic serif, bottom-left, near-black — sounds like a real person wrote it",
                "has_cup": False,
                "cta": "Get the Trifecta",
                "cta_style": "pill_bottom_right",
                "price": True,
                "price_style": "pill",
            },

            # Night — HRV proof, structured blocks, most specific claim
            {
                "file": "10_night_hrv_blocks.png",
                "sku": "night",
                "product_type": "tea",
                "format": "blocks",
                "hook": "My sleep tracker noticed. I noticed. Week two.",
                "blocks": [
                    {"size": "large", "content": "Navy canister in a single soft spotlight on a dark surface — jewel-like, still"},
                    {"size": "medium", "content": "Hook text in editorial serif, cream on navy: 'My sleep tracker noticed. I noticed. Week two.'"},
                    {"size": "small", "content": "Proof strip: '4.9★ · 250mg Reishi · No melatonin · 90-day guarantee'"},
                ],
                "color_world": "deep midnight navy #1C2456 — full bleed, every surface in navy",
                "cta": "Start tonight",
                "cta_style": "pill_bottom",
                "price": True,
                "price_style": "pill",
            },

        ],
    },

    # ── v5 — next campaign placeholder ───────────────────────────────────────
    # Add new ads here when ready. Copy a spec block from v4, change the hook
    # and scene. The hook must be a different human outcome than any in v4.
    # "v5": {
    #     "run_id": None,
    #     "ads": [],
    # },


    # ══ RETARGET CAMPAIGNS (audience: retarget) — moved from former tea_retarget.py ══

    "retarget_v4": {
        "run_id": None,
        "audience": "retarget",
        "ads": [

            # Two products together — the natural next step framing
            {
                "file": "01_two_products_counter.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "scene",
                "hook": "You already start every morning with Alcami. Now there's a version for 3pm.",
                "scene": "A kitchen counter. The original blend pouch on the left, the afternoon sage canister on the right. Both in their natural places — not staged, lived-in.",
                "visual_action": "Two Alcami products coexist naturally on the same counter. The morning ritual already exists here. The afternoon option has just arrived beside it.",
                "text_in_image": "Your 3pm, now.",
                "text_treatment": "minimal italic, bottom-right, cream — a quiet addition, not an announcement",
                "has_cup": False,
                "cta": "Try the Afternoon",
                "cta_style": "pill_bottom_right",
                "price": False,
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # Macro indigo pour — pure chemistry, no copy needed
            {
                "file": "02_indigo_pour_macro.png",
                "sku": "night",
                "product_type": "tea",
                "format": "scene",
                "hook": "The color is real. So is everything else it does.",
                "scene": "Overhead extreme macro: water pouring into a clear glass. The liquid turns deep indigo-blue on contact with the Nighttime sachet. Navy surface. No canister in frame — the liquid IS the product.",
                "visual_action": "The transformation is happening mid-pour. The indigo blooms from the sachet upward. This is a product demonstrating itself without words.",
                "text_in_image": "Real. All of it.",
                "text_treatment": "tiny spaced caps, bottom edge, cream — an afterthought, not a headline",
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "text_line",
                "price": False,
            },

            # Domestic morning scene — person + both products
            {
                "file": "03_morning_person_kitchen.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "scene",
                "hook": "She made the switch. Then she made three more.",
                "scene": "A woman in a warm kitchen at 7am. She holds a mug. Behind her on the counter: the original blend pouch, the morning tea canister. Both visible, both hers. Morning window light.",
                "visual_action": "She is in the ritual — not performing it for camera. The two Alcami products behind her are part of the scene, not the subject. She is the subject.",
                "text_in_image": "",
                "has_cup": False,
                "cta": "Try the Morning Ritual",
                "cta_style": "pill_bottom",
                "price": False,
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # Welcome kit — preserved concept from retarget_03 ad 05 (rated "great")
            {
                "file": "04_welcome_kit_flatlay.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "scene",
                "hook": "The first order comes with a ceramic tumbler, a tote, and 5 travel sachets. Free.",
                "scene": "Flat-lay on a warm cream linen surface: the Trifecta canister, a ceramic tumbler, a canvas tote, 5 gold foil travel sachets, a small brass keychain. All Alcami. Soft overhead light, no shadows.",
                "visual_action": "Everything laid out as if just unboxed — the moment before the ritual begins. The Trifecta canister is the anchor, the accessories radiate from it.",
                "text_in_image": "Everything in the first box.",
                "text_treatment": "light serif italic, lower third, near-black — factual, warm",
                "has_cup": False,
                "cta": "Get the Trifecta",
                "cta_style": "pill_bottom",
                "price": True,
                "price_style": "pill",
            },

            # Night bedside — domestic retarget scene, intimate
            {
                "file": "05_night_bedside_person.png",
                "sku": "night",
                "product_type": "tea",
                "format": "scene",
                "hook": "You wind down every night. This is what it looks like when you do it properly.",
                "scene": "A woman sitting on the edge of her bed at 9pm. The navy canister on the nightstand beside a small lamp. She holds a cup. The room is dim. The lamp and the cup are the only warm things in frame.",
                "visual_action": "She is already in the wind-down. The tea is part of a ritual that exists, not one being sold. The canister on the nightstand is evidence, not product placement.",
                "text_in_image": "9pm. Done right.",
                "text_treatment": "small editorial serif, bottom-left, cream — quiet, inevitable",
                "has_cup": True,
                "cta": "Start tonight",
                "cta_style": "text_line",
                "price": False,
            },

            # Sachet backlit macro — texture and craft, no person
            {
                "file": "06_sachet_backlit.png",
                "sku": "afternoon",
                "product_type": "tea",
                "format": "scene",
                "hook": "Whole-leaf. Pyramid sachet. No plastic. It matters what's inside.",
                "scene": "A single Afternoon pyramid sachet held up against sage-green backlit light. The whole-leaf herbs visible through the translucent PLA material. Light diffuses through the sachet, illuminating the moringa and mint inside.",
                "visual_action": "The sachet is held at arm's length against the light — a quality reveal. What's inside is visible and beautiful. No canister needed — the sachet IS the argument.",
                "text_in_image": "Whole-leaf. No plastic.",
                "text_treatment": "condensed bold, top-left, near-black — direct, confident",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "pill_bottom_right",
                "price": False,
            },

            # Morning — extreme canister macro, botanical engraving detail
            {
                "file": "07_morning_canister_macro.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "scene",
                "hook": "The mushroom on the label is the same one doing the work inside.",
                "scene": "Extreme macro: the botanical engraving on the Morning canister fills the frame. The intricate mushroom cap illustration, the dual-hemisphere form, the luminous center oval catching warm amber light. The ALCAMI ELEMENTS wordmark readable at the top.",
                "visual_action": "The illustration itself is the subject — photographed as art, not packaging. The detail is the point. What you hold every morning is this considered.",
                "text_in_image": "",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "text_line",
                "price": False,
            },

            # Trifecta — all three canisters lineup, no person
            {
                "file": "08_trifecta_lineup.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "scene",
                "hook": "Three canisters. One for each part of the day you care about.",
                "scene": "Three canisters in a row on a cream stone surface: Morning amber-gold, Afternoon sage-green, Night deep navy. Left to right as the day moves. Soft directional studio light. Each canister fully visible with its botanical engraving glowing.",
                "visual_action": "The lineup is the argument. Three distinct colors, three distinct hours. The day has a shape — the canisters are its architecture.",
                "text_in_image": "Morning. Afternoon. Night.",
                "text_treatment": "spaced light caps, below the canisters, near-black — a label for what you're seeing, nothing more",
                "has_cup": False,
                "cta": "Get the Trifecta",
                "cta_style": "pill_bottom",
                "price": True,
                "price_style": "pill",
            },

            # Afternoon — color-drenched person in sage world
            {
                "file": "09_afternoon_sage_person.png",
                "sku": "afternoon",
                "product_type": "tea",
                "format": "scene",
                "hook": "This is what 3pm looks like when it actually works.",
                "scene": "A woman at a desk by a window, afternoon. Sage-olive light ambient. She wears sage-olive linen. The afternoon canister is on the desk beside her laptop. She is looking at the screen — not performing focus, just in it.",
                "visual_action": "The sage-green color world wraps the entire scene — her clothing, the light, the surface all carry the afternoon palette. The canister belongs because it was built for this exact world. She is the proof: 3pm, still productive.",
                "text_in_image": "3pm. Actually works.",
                "text_treatment": "two-line bold sans-serif, left-aligned, top-left corner, near-black — direct claim, no setup",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "pill_bottom_right",
                "price": False,
            },

            # Night — comparison blocks, melatonin replacement angle
            {
                "file": "10_night_melatonin_comparison.png",
                "sku": "night",
                "product_type": "tea",
                "format": "comparison",
                "hook": "I stopped buying melatonin. Here's what replaced it.",
                "sides": {
                    "left": {
                        "label": "Melatonin",
                        "points": [
                            "Works around your sleep system",
                            "Morning grogginess common",
                            "Dependency risk over time",
                            "Doesn't address why you wake at 2am",
                        ],
                    },
                    "right": {
                        "label": "Alcami Night Ritual",
                        "points": [
                            "250mg Reishi — parasympathetic support",
                            "Works with your nervous system",
                            "Chamomile + Lavender + Butterfly pea",
                            "HRV improvement. Fewer wake-ups.",
                        ],
                    },
                },
                "visual": "deep navy #1C2456 background. Night canister large on the right, illuminated. Left column in cream type. Right column in cream/gold type.",
                "cta": "Try it for 90 days",
                "cta_style": "band_bottom",
                "price": True,
                "price_style": "pill",
            },

        ],
    },

    # ── v5 — blend customer base → tea cross-sell ────────────────────────────
    # 10 ads. Warm audience — blend customers who haven't bought tea yet.
    # Hooks name the product directly. No brand intro needed.
    # Format mix: ugc (×3) · scene (×4) · comparison (×1) · blocks-testimonial (×1) · how_it_works (×1)
    # Run: python3 gen.py batches/tea.py --campaign retarget_v5
    "retarget_v5": {
        "run_id": None,
        "audience": "retarget",
        "ads": [

            # 01 — Trifecta · UGC · unboxing energy ───────────────────────────
            {
                "file": "01_trifecta_ugc_unbox.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "ugc",
                "hook": "The Alcami Tea set. All three blends. Start here.",
                "person": "A woman in her 30s, casual, no studio styling — Alcami blend pouch visible in the background, Trifecta canister just unboxed on the counter in front of her",
                "moment": "She's holding the Trifecta canister and reading the label — the blend is already part of her counter. The tea has just arrived.",
                "environment": "Real kitchen counter, natural light. Both Alcami products visible. Feels lived-in, not styled.",
                "text_in_image": "Already had the blend. Now this.",
                "text_treatment": "plain white text, bottom of frame — sounds like a caption, not an ad",
                "has_cup": False,
                "cta": "Get the Trifecta",
                "cta_style": "none",
                "price": True,
                "price_style": "footnote",
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # 02 — Night · Scene · two rituals on one bedside table ───────────
            {
                "file": "02_night_two_products.png",
                "sku": "night",
                "product_type": "tea",
                "format": "scene",
                "hook": "Alcami Night Tea. What happens after the morning ritual.",
                "scene": "A bedside table at 9pm. The Original blend pouch on one side, the Night tea canister on the other. A closed book. A single lamp. Both Alcami products living in the same space.",
                "visual_action": "Two rituals on the same table — one for morning, one for night. The lamp illuminates both equally. Neither competes.",
                "text_in_image": "7am is covered. Here's 9pm.",
                "text_treatment": "small light italic serif, bottom-left, cream — quiet, factual",
                "has_cup": False,
                "cta": "Try the Night",
                "cta_style": "text_line",
                "price": False,
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # 03 — Afternoon · Scene · the window the blend doesn't cover ─────
            {
                "file": "03_afternoon_3pm_desk.png",
                "sku": "afternoon",
                "product_type": "tea",
                "format": "scene",
                "hook": "Alcami Afternoon Tea. For the 3pm the blend doesn't reach.",
                "scene": "A clean desk at 3pm. The sage-green Afternoon canister front and center. The blend pouch partially visible at the far edge — already used this morning. A brewed cup beside the canister.",
                "visual_action": "The blend handled morning. The afternoon canister handles now. Two different tools, same quality. The desk shows both without one overshadowing the other.",
                "text_in_image": "The blend covered 7am. This covers 3pm.",
                "text_treatment": "clean bold sans-serif, top-left, near-black — direct, factual",
                "has_cup": False,
                "cta": "Try the Afternoon",
                "cta_style": "pill_bottom_right",
                "price": False,
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # 04 — Morning · Comparison · what they're doing vs. Alcami tea ───
            {
                "file": "04_morning_comparison.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "comparison",
                "hook": "Alcami Morning Tea. Cordyceps before your first coffee. Or instead of it.",
                "sides": {
                    "left": {
                        "label": "What most people drink first",
                        "points": [
                            "Generic herbal tea or warm water",
                            "No functional dose",
                            "Flavor only",
                            "Then still need coffee for the lift",
                        ],
                    },
                    "right": {
                        "label": "Alcami Morning Tea",
                        "points": [
                            "200mg Cordyceps — cellular lift",
                            "Ginger · Turmeric · Lemon peel",
                            "Caffeine-free — no cortisol spike",
                            "From the people who made the blend",
                        ],
                    },
                },
                "visual": "warm amber-gold #E8B840 background. Morning canister large on the right. Plain herbal tea bag on the left, smaller.",
                "cta": "Try the Morning",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 05 — Night · UGC · real evening, casual, no studio ──────────────
            {
                "file": "05_night_ugc_evening.png",
                "sku": "night",
                "product_type": "tea",
                "format": "ugc",
                "hook": "Alcami Night Tea. What happens after the morning ritual.",
                "person": "A woman in her 30s, soft robe, no makeup — real, not styled",
                "moment": "Sitting on the edge of her bed at 9pm. Holding a mug with deep indigo-blue tea. The navy Night canister on the nightstand. Phone face-down on the bed.",
                "environment": "Dim bedroom, lamp on, naturally quiet. The morning ritual already happened — this is what comes after.",
                "text_in_image": "After the blend. Before sleep.",
                "text_treatment": "plain white text, bottom-left — reads like a caption",
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "none",
                "price": False,
            },

            # 06 — Trifecta · Scene · the full Alcami range together ──────────
            {
                "file": "06_trifecta_full_range.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "scene",
                "hook": "You know the blend. You should try the tea.",
                "scene": "A kitchen counter in warm morning light. The Original blend pouch and all three tea canisters (Morning amber-gold, Afternoon sage, Night navy) arranged together — one family, different moments.",
                "visual_action": "The full Alcami range in one frame. The blend they already own is part of the composition — familiar and trusted. The three tea canisters are new additions to the same world.",
                "text_in_image": "You already have one. Here are the other three.",
                "text_treatment": "editorial italic serif, lower third, near-black — understated, warm",
                "has_cup": False,
                "cta": "Get the Trifecta",
                "cta_style": "pill_bottom",
                "price": True,
                "price_style": "pill",
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # 07 — Afternoon · Blocks / testimonial_text ──────────────────────
            {
                "file": "07_afternoon_testimonial.png",
                "sku": "afternoon",
                "product_type": "tea",
                "format": "blocks",
                "style": "testimonial_text",
                "hook": "I've used the blend for two years. Added the Afternoon Tea three months ago. The 3pm dip just stopped.",
                "blocks": [
                    {"size": "large",  "content": "Afternoon Ritual canister in a sage-green world, soft studio light — premium, still"},
                    {"size": "medium", "content": "Customer quote in light italic serif: 'I've used the blend for two years. Added the Afternoon Tea three months ago. The 3pm dip just stopped.' — attributed simply: 'Alcami customer'"},
                    {"size": "small",  "content": "4.9★ · Lion's Mane 200mg · USDA Organic"},
                ],
                "color_world": "muted sage-olive green #9CB87A — calm, productive, afternoon",
                "cta": "Shop Now",
                "cta_style": "pill_bottom",
                "price": False,
            },

            # 08 — Night · Scene · indigo pour macro ─────────────────────────
            {
                "file": "08_night_indigo_macro.png",
                "sku": "night",
                "product_type": "tea",
                "format": "scene",
                "hook": "Alcami Night Tea. The cup turns indigo. So does the evening.",
                "scene": "Overhead extreme macro: hot water pouring into a white ceramic cup. The liquid blooms from clear to deep indigo-blue as it contacts the Night sachet. Navy surface. Steam rising.",
                "visual_action": "The color transformation mid-pour — the most visually distinctive thing about this product, and owned by no other brand. The canister is partially in frame at the edge.",
                "text_in_image": "This is what 9pm looks like now.",
                "text_treatment": "small light italic, bottom-left, cream — barely there, confirms the image",
                "has_cup": True,
                "cta": "Try the Night",
                "cta_style": "text_line",
                "price": False,
            },

            # 09 — Morning · UGC · both products, same person ──────────────────
            {
                "file": "09_morning_ugc_both.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "ugc",
                "hook": "Alcami Morning Tea. Cordyceps before your first coffee. Or instead of it.",
                "person": "A person in their early 30s, casual morning clothes — a known Alcami blend customer in their natural habitat",
                "moment": "In the kitchen at 7am. The Morning tea canister is in their hand. The Original blend pouch is already on the counter behind them — both theirs.",
                "environment": "Real apartment kitchen, natural window light. Both Alcami products visible. The morning is already Alcami territory — the tea just joined it.",
                "text_in_image": "Alcami. Now in a teacup too.",
                "text_treatment": "plain white text, bottom of frame — casual, like a caption",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "none",
                "price": False,
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # 10 — Trifecta · How it works · full day arc ─────────────────────
            {
                "file": "10_trifecta_how_it_works.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "how_it_works",
                "hook": "We made tea. Three blends. Here's how your full day works now.",
                "steps": [
                    {"label": "7 AM — Morning Ritual",   "detail": "Cordyceps 200mg · Ginger · Turmeric · Caffeine-free lift"},
                    {"label": "12 PM — Afternoon Ritual","detail": "Lion's Mane 200mg · Guayusa · Focus that holds to 5pm"},
                    {"label": "9 PM — Night Ritual",     "detail": "Reishi 250mg · Chamomile · Lavender · The cup turns indigo"},
                ],
                "color_world": "warm cream #FFFDF5 — clean infographic ground. Trifecta canister anchors the right side, full gradient visible.",
                "cta": "Get the Trifecta",
                "cta_style": "band_bottom",
                "price": True,
                "price_style": "pill",
            },

        ],
    },

    # ── v6 — designed information ads, no UGC ────────────────────────────────
    # 10 ads. Warm audience — blend customers who haven't bought tea yet.
    # All structured/designed formats: comparison, blocks.
    # Comparisons only vs. generic tea (no competitor brand names).
    # Every ad: typographic hierarchy + product depth + text in containers + CTA contrast.
    # Run: python3 gen.py batches/tea.py --campaign retarget_v6
    "retarget_v6": {
        "run_id": None,
        "audience": "retarget",
        "ads": [

            # 01 — Night · comparison · vs. melatonin
            {
                "file": "01_night_vs_melatonin.png",
                "sku": "night",
                "product_type": "tea",
                "format": "comparison",
                "hook": "Alcami Night Tea. What melatonin can't do.",
                "sides": {
                    "left": {
                        "label": "Melatonin",
                        "points": [
                            "Synthetic hormone - works around your sleep system",
                            "Morning grogginess common",
                            "Dependency risk with daily use",
                            "Doesn't address why you wake at 2am",
                        ],
                    },
                    "right": {
                        "label": "Alcami Night Ritual",
                        "points": [
                            "250mg Reishi - works with your parasympathetic system",
                            "No grogginess - not a sedative",
                            "Non-habit-forming. Supports HRV.",
                            "Fewer 2am wake-ups. Better sleep architecture.",
                        ],
                    },
                },
                "visual": "deep midnight navy #1C2456 background. Night canister large on right with drop shadow. Left side: a white melatonin pill bottle, small and desaturated.",
                "cta": "Try it for 90 days",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 02 — Morning · comparison · vs. generic morning tea
            {
                "file": "02_morning_vs_basic_tea.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "comparison",
                "hook": "The Alcami you know. Now as morning tea.",
                "sides": {
                    "left": {
                        "label": "Regular morning tea",
                        "points": [
                            "Flat paper bag - often bleached, microplastic risk",
                            "Zero functional mushroom dose",
                            "Flavor only - you still need coffee after",
                            "No sourcing transparency",
                        ],
                    },
                    "right": {
                        "label": "Alcami Morning Ritual",
                        "points": [
                            "PLA pyramid sachet - whole-leaf, home-compostable",
                            "200mg Cordyceps - cellular lift, no cortisol spike",
                            "Caffeine-free - the lift is real, not stimulant",
                            "100% fruit-body extract, USDA Organic",
                        ],
                    },
                },
                "visual": "warm amber-gold #E8B840 background. Right side: Morning canister with drop shadow, large. Left side: a plain flat paper tea bag on a simple ceramic plate, small and desaturated.",
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 03 — Afternoon · comparison · vs. generic afternoon tea
            # Row 4 fixed: both sides on sourcing/quality dimension (parallel)
            {
                "file": "03_afternoon_vs_basic_tea.png",
                "sku": "afternoon",
                "product_type": "tea",
                "format": "comparison",
                "hook": "The blend is morning. Alcami tea is 3pm.",
                "sides": {
                    "left": {
                        "label": "Generic herbal tea",
                        "points": [
                            "No functional dose - just hot flavored water",
                            "Zero cognitive support",
                            "Caffeine: none or jitter from black tea",
                            "Unknown sourcing - commodity herbs",
                        ],
                    },
                    "right": {
                        "label": "Alcami Afternoon Ritual",
                        "points": [
                            "200mg Lion's Mane - cognitive clarity, NGF support",
                            "Focus that holds through to 5pm",
                            "Clean energy via Guayusa - no spike, no crash",
                            "USDA Organic - third-party tested, traceable",
                        ],
                    },
                },
                "visual": "muted sage-olive #9CB87A background. Afternoon canister large on right with drop shadow. Left: plain chamomile tea bag, small and desaturated. Two clear columns with strong vertical divider. Clean typographic hierarchy.",
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 04 — Night · blocks / ingredient_breakdown
            {
                "file": "04_night_ingredients.png",
                "sku": "night",
                "product_type": "tea",
                "format": "blocks",
                "style": "ingredient_breakdown",
                "hook": "What's actually in Alcami Night Tea.",
                "blocks": [
                    {"size": "large",  "content": "Night canister with drop shadow and subtle deep navy glow behind it - physically present, not floating. Dark textured surface."},
                    {"size": "medium", "content": "Hook: 'What's actually in Alcami Night Tea.' - bold editorial serif in cream, inside a near-black panel that spans the block width."},
                    {"size": "small",  "content": "Three frosted ingredient chips, each as a separate design object. Chip 1: 'REISHI 250mg - parasympathetic support, HRV, fewer 2am wake-ups'. Chip 2: 'CHAMOMILE + LAVENDER - the nervous system finally closes'. Chip 3: 'BUTTERFLY PEA FLOWER - the cup turns deep indigo'."},
                    {"size": "small",  "content": "Proof strip: CAFFEINE-FREE, USDA Organic, Third-party tested - small spaced caps inside a muted dark band."},
                    {"size": "small",  "content": "CTA band: full-width near-black band pinned to the very bottom of the canvas. 'Shop Now' in bold cream caps - tall band, noticeably larger text than anything else below the headline. The CTA is the most visually dominant element on the lower half of the canvas."},
                ],
                "color_world": "deep midnight navy #1C2456 - every surface and zone carries navy. Cream and gold are the only contrasting text colors.",
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 05 — Morning · blocks / ingredient_breakdown
            {
                "file": "05_morning_ingredients.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "blocks",
                "style": "ingredient_breakdown",
                "hook": "Alcami morning tea. Four ingredients. No caffeine.",
                "blocks": [
                    {"size": "large",  "content": "Morning canister with drop shadow and warm amber glow behind it on a textured warm stone surface."},
                    {"size": "medium", "content": "Hook: 'Alcami morning tea. Four ingredients. No caffeine.' - bold condensed sans-serif in near-black, inside a warm amber-gold #E8B840 band."},
                    {"size": "small",  "content": "Four frosted ingredient chips. Chip 1: 'CORDYCEPS 200mg - cellular oxygen uptake, slow-rising lift, no cortisol spike'. Chip 2: 'GINGER ROOT - warmth and circulation'. Chip 3: 'TURMERIC - anti-inflammatory grounding'. Chip 4: 'LEMON PEEL - the morning brightness that is not caffeine'."},
                    {"size": "small",  "content": "Proof: CAFFEINE-FREE, 100% Fruit-body extract, USDA Organic - spaced caps in a muted band."},
                ],
                "color_world": "warm amber-gold #E8B840 - every surface warm. Near-black text for maximum contrast on gold zones.",
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 06 — Afternoon · blocks / benefit_highlights
            {
                "file": "06_afternoon_benefits.png",
                "sku": "afternoon",
                "product_type": "tea",
                "format": "blocks",
                "style": "benefit_highlights",
                "hook": "Your afternoon is now Alcami territory.",
                "blocks": [
                    {"size": "large",  "content": "Afternoon canister on a sage-olive textured surface, soft directional light from the left, drop shadow beneath. Real environment depth - not flat."},
                    {"size": "medium", "content": "Hook in bold editorial serif, cream on near-black panel: 'Your afternoon is now Alcami territory.'"},
                    {"size": "small",  "content": "Three benefit chips in sage-toned frosted containers. Chip 1: 'Lion's Mane 200mg - cognitive clarity, NGF support'. Chip 2: 'Focus that holds to 5pm - not just through lunch'. Chip 3: 'Clean energy via Guayusa - no spike, no crash'."},
                    {"size": "small",  "content": "Proof: 4.9 stars, USDA Organic, Plastic-free pyramid sachet."},
                ],
                "color_world": "muted sage-olive #9CB87A - every surface and zone sage. Near-black and cream are the contrast colors.",
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 07 — Trifecta · blocks / benefit_highlights · sampler discovery angle
            # Changed from how_it_works — showing what's in the box, time-labeled chips.
            {
                "file": "07_trifecta_circadian.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "blocks",
                "style": "benefit_highlights",
                "hook": "We made Alcami teas for the whole day.",
                "blocks": [
                    {"size": "large",  "content": "Trifecta canister centered on a warm cream surface, drop shadow beneath, soft radial glow behind. Full gradient clearly visible: gold crown, sage mid, lavender base - every zone preserved."},
                    {"size": "medium", "content": "Hook in bold condensed serif, near-black on cream panel: 'We made Alcami teas for the whole day.'"},
                    {"size": "small",  "content": "Three time-labeled frosted chips, each in its SKU color. Amber chip: '7 AM - Morning. Cordyceps 200mg'. Sage chip: '12 PM - Afternoon. Lion's Mane 200mg'. Navy chip: '9 PM - Night. Reishi 250mg'."},
                    {"size": "small",  "content": "What's inside: 10 Morning sachets, 10 Afternoon sachets, 10 Night sachets. One tube. Text inside a muted warm-cream band."},
                ],
                "color_world": "warm cream #FFFDF5 - neutral canvas so all three SKU colors in the gradient and chips read clearly.",
                "cta": "Get the Trifecta",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 08 — Night · blocks / benefit_highlights · sleep quality angle
            {
                "file": "08_night_sleep_quality.png",
                "sku": "night",
                "product_type": "tea",
                "format": "blocks",
                "style": "benefit_highlights",
                "hook": "8 hours of sleep feels like 4? Here's the right tea for you.",
                "blocks": [
                    {"size": "large",  "content": "Night canister on a dark navy wood surface, single warm spotlight from above, deep shadow beneath. The canister and its label glow in the lamp - nothing else does."},
                    {"size": "medium", "content": "Hook in bold editorial serif, cream on near-black: '8 hours of sleep feels like 4? Here's the right tea for you.'"},
                    {"size": "small",  "content": "Three benefit chips in navy-frosted containers. Chip 1: 'Fewer 2am wake-ups - Reishi supports sleep architecture, not just onset'. Chip 2: 'Better HRV - parasympathetic calm, not forced sedation'. Chip 3: 'No morning grogginess - it doesn't override your system'."},
                    {"size": "small",  "content": "Proof: 4.9 stars, CAFFEINE-FREE, 90-day guarantee - spaced cream caps inside a muted dark band."},
                ],
                "color_world": "deep midnight navy #1C2456 - full bleed. Cream and gold for all text contrast.",
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 09 — Trifecta · blocks / benefit_highlights · all three teas
            {
                "file": "09_trifecta_system.png",
                "sku": "trifecta",
                "product_type": "tea",
                "format": "blocks",
                "style": "benefit_highlights",
                "hook": "All three Alcami teas. One box.",
                "blocks": [
                    {"size": "large",  "content": "Trifecta canister centered with drop shadow on a warm cream surface. Full gradient clearly visible: gold crown, sage mid, lavender base. Every zone of the gradient preserved."},
                    {"size": "medium", "content": "Hook in bold condensed serif, near-black on cream panel: 'All three Alcami teas. One box.'"},
                    {"size": "small",  "content": "Three time-labeled frosted chips, each in the matching SKU color. Amber chip: '7 AM - Cordyceps 200mg - Energy without the cortisol'. Sage chip: '12 PM - Lion's Mane 200mg - Focus to 5pm'. Navy chip: '9 PM - Reishi 250mg - Deep sleep architecture'."},
                    {"size": "small",  "content": "Proof: 4.9 stars, USDA Organic, Made in Canada, Third-party tested - spaced caps in a muted band."},
                ],
                "color_world": "warm cream #FFFDF5 - neutral so all three SKU colors in the chips and canister gradient read clearly without competition.",
                "cta": "Get the Trifecta",
                "cta_style": "band_bottom",
                "price": False,
            },

            # 10 — Morning · blocks / benefit_highlights · the Cordyceps lift
            {
                "file": "10_morning_cordyceps.png",
                "sku": "morning",
                "product_type": "tea",
                "format": "blocks",
                "style": "benefit_highlights",
                "hook": "Alcami morning. Now in a teacup.",
                "blocks": [
                    {"size": "large",  "content": "Morning canister on an amber-gold warm stone surface, drop shadow beneath, warm light from the left. A brewed cup of amber-gold tea beside it - same color world as the canister."},
                    {"size": "medium", "content": "Hook in bold editorial serif, near-black on warm gold band: 'Alcami morning. Now in a teacup.'"},
                    {"size": "small",  "content": "Three frosted chips in warm amber. Chip 1: 'Cellular oxygen uptake - not a stimulant rush'. Chip 2: 'Slow-rising energy - peaks at 90 min, holds for 4-5 hours'. Chip 3: 'No cortisol spike - no 11am crash'."},
                    {"size": "small",  "content": "Proof: CAFFEINE-FREE, 200mg Cordyceps per sachet, 4.9 stars - small spaced caps inside a warm amber muted band."},
                ],
                "color_world": "warm amber-gold #E8B840 - the entire canvas is warm amber. Near-black for high-contrast text.",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "band_bottom",
                "price": False,
            },

        ],
    },

}
