# ─────────────────────────────────────────────────────────────────────────────
# Alcami Tea — Campaign Config (acquisition + retarget)
#
# All tea campaigns live here. Audience is a FIELD, not a separate file:
#   acquisition = default · retarget = set "audience": "retarget" on the campaign
#
# Run: python3 gen.py batches/tea.py --campaign <name>
#
# Four SKUs: morning / afternoon / night / trifecta
# Price anchor for all tea ads: "From $37.40/month"
# Status, claims, social proof, kit: CLAUDE.md → Ritual Tea Line
# Deep creative strategy: tea-product-brief.md
# Spec fields + examples: batches/_template.py · Formats/archetypes: python3 gen.py --policy
#
# Retarget = LAUNCH to existing blend customers: "we made tea now" · "loved the
#   blend? try this" · two-product display · insider access · "one of the first".
#   Scene-led. Never comparison / ugc / testimonial / social_proof (validator warns).
# ─────────────────────────────────────────────────────────────────────────────

CAMPAIGNS = {

    # ── launch_v1 — tea launch to existing blend customers ────────────────────
    # LAUNCH register: share the news, extend the relationship. Lead with "we made
    # tea", "loved the blend? try this", a two-product display, insider access, and
    # the pioneer claim. Scene-led only (comparison is off-strategy for retarget).
    # SKU mix skews Trifecta + Night; all four SKUs appear for launch range.
    "launch_v1": {
        "run_id": "tea_retarget_batch1",
        "audience": "retarget",
        "ads": [

            # 01 — "We made tea" announcement · Trifecta
            {
                "file": "01_we_made_tea_trifecta.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "editorial",
                "hook": "You know Alcami. Now we made tea.",
                "headline": "We made tea.",
                "subhead": "From the creators of your daily blend.",
                "emphasis": {"tea": "gold"},
                "scene": "A calm kitchen counter in soft morning light. The gradient Trifecta tube stands alone on pale wood, a single ceramic cup beside it. Quiet, premium, the moment a new thing arrives.",
                "visual_action": "The new tube gets the spotlight, an announcement, unhurried and confident.",
                "cta": "Try the Tea",
                "cta_style": "button",
                "price": False,
            },

            # 02 — "We made tea" announcement · Night
            {
                "file": "02_we_made_tea_night.png",
                "product_type": "tea",
                "sku": "night",
                "format": "scene",
                "archetype": "editorial",
                "hook": "Alcami makes tea now. Start with the night one.",
                "headline": "We made a tea for your evenings.",
                "subhead": "Reishi, chamomile, lavender. Caffeine-free.",
                "emphasis": {"evenings": "gold"},
                "scene": "A dim bedside table at 9pm. The navy Night tube beside a small warm lamp, a calm cup of herbal tea catching the light. The rest of the room falls into shadow.",
                "visual_action": "The new night tube introduced into a real wind-down moment, lamp glow and calm.",
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 03 — Two-product display · Trifecta + Original blend
            {
                "file": "03_two_product_trifecta.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "editorial",
                "hook": "The blend you love, now joined by the tea.",
                "headline": "Your blend has company.",
                "subhead": "The ritual you know, extended across the whole day.",
                "scene": "A warm shelf in soft morning light, surface of darker walnut wood so the cream Original pouch separates clearly from the background. The Original blend pouch and the gradient Trifecta tea tube stand side by side, both large and prominent, with clear space between them.",
                "visual_action": "Two products, one family, both equally prominent. The blend they already own beside the tea that just arrived, recognition not a pitch.",
                "has_cup": False,
                "cta": "Get the Trifecta",
                "cta_style": "button_right",
                "price": False,
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # 04 — "Loved the blend? Try this" · Morning
            {
                "file": "04_loved_blend_morning.png",
                "product_type": "tea",
                "sku": "morning",
                "format": "scene",
                "archetype": "editorial",
                "hook": "Loved your morning blend? There's now a tea for it too.",
                "headline": "Loved the blend? Try the tea.",
                "subhead": "Morning Ritual. A cordyceps lift, caffeine-free.",
                "emphasis": {"tea": "gold"},
                "scene": "A bright breakfast counter in warm morning light. The amber-gold Morning tube beside a steaming ceramic cup and a small spoon on the wood.",
                "visual_action": "The morning tea presented as the natural next step for someone who already starts the day with Alcami.",
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 05 — "Loved the blend? Try this" · Trifecta
            {
                "file": "05_loved_blend_trifecta.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "editorial",
                "hook": "Loved the blend? Meet the whole tea range.",
                "headline": "Loved the blend? Meet the tea.",
                "subhead": "Three rituals for morning, afternoon, and night.",
                "emphasis": {"tea": "gold"},
                "scene": "A warm flat-lay on linen. The gradient Trifecta tube centered and large, its gold-to-sage-to-lavender gradient catching even light, generous clean space around it for the text.",
                "visual_action": "The full range offered to a customer who already trusts the brand, an invitation not an argument.",
                "cta": "Get the Trifecta",
                "cta_style": "button",
                "price": False,
            },

            # 06 — News / cross-sell · Afternoon (brings the 3pm SKU into the launch)
            {
                "file": "06_afternoon_3pm.png",
                "product_type": "tea",
                "sku": "afternoon",
                "format": "scene",
                "archetype": "editorial",
                "hook": "The blend gets your mornings. Now there's a tea for your 3pm.",
                "headline": "Now there's one for 3pm.",
                "subhead": "Afternoon Ritual. Clean, steady focus.",
                "emphasis": {"3pm": "gold"},
                "scene": "A bright, tidy desk mid-afternoon. The sage-green Afternoon tube beside a cup on a clean wooden surface, a notebook just in frame, daylight from the side.",
                "visual_action": "The afternoon tea placed in the 3pm moment it was built for, calm and focused, not frantic.",
                "has_cup": False,
                "cta": "Shop the Afternoon",
                "cta_style": "button_right",
                "price": False,
            },

            # 07 — Insider / early access · Trifecta
            {
                "file": "07_insider_trifecta.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "editorial",
                "hook": "Our customers get the tea first.",
                "headline": "You get it first.",
                "subhead": "The new Alcami tea, for the people who started it all.",
                "emphasis": {"first": "underline"},
                "scene": "A quiet, premium tabletop. The gradient Trifecta tube under a single clean key light, generous negative space around it.",
                "visual_action": "An exclusive, you're-on-the-list feeling, restrained and flattering, no urgency banners.",
                "cta": "Be the First",
                "cta_style": "button",
                "price": False,
            },

            # 08 — Pioneer claim · Night
            {
                "file": "08_pioneer_night.png",
                "product_type": "tea",
                "sku": "night",
                "format": "scene",
                "archetype": "editorial",
                "hook": "We made one of the first mushroom teas.",
                "headline": "One of the first of its kind.",
                "subhead": "A mushroom tea from the creators of your daily blend.",
                "emphasis": {"first": "gold"},
                "scene": "A premium, editorial reveal. The navy Night tube under a single soft key light against a deep, calm background, generous negative space, a sense of something genuinely new being shown.",
                "visual_action": "A proud, understated reveal, the product presented as a first of its kind without shouting.",
                "has_cup": False,
                "cta": "Shop the Tea",
                "cta_style": "button",
                "price": False,
            },

            # 09 — System · Trifecta · "a tea for every part of your day"
            {
                "file": "09_every_part_of_day.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "color_block",
                "hook": "Alcami made a tea for every part of your day.",
                "headline": "Morning. Afternoon. Night.",
                "subhead": "The new Alcami tea, built for the whole day.",
                "emphasis": {"Alcami": "gold"},
                "scene": "A clean three-zone surface washed gold, sage, then navy from left to right. The gradient Trifecta tube centered where the colors meet, its gradient echoing the scene.",
                "visual_action": "The day's arc made literal, the tube's gradient mirrored by the light across the surface.",
                "cta": "Get the Trifecta",
                "cta_style": "button",
                "price": False,
            },

            # 10 — Big launch hero · Trifecta (maximum new-product energy)
            {
                "file": "10_launch_hero_trifecta.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "color_block",
                "hook": "The new Alcami tea is here.",
                "headline": "It's here.",
                "subhead": "The new Alcami Ritual Tea has landed.",
                "emphasis": {"here": "gold"},
                "scene": "A bold hero shot. The full gradient Trifecta tube, large and entirely in frame (never cropped), against a rich color-blocked background echoing its gold-sage-lavender gradient, strong directional light, a sense of arrival and occasion.",
                "visual_action": "Full launch energy, the product as the event. Big, confident, the whole canister visible, unmistakably a new drop from a brand you already follow.",
                "cta": "Shop the Tea",
                "cta_style": "button",
                "price": False,
            },

        ],
    },

    # ── acquisition_v1 — cold audience, all five formats ──────────────────────
    # Cold traffic: each hook reads in under 2s with no prior brand knowledge, and the
    # scene/visual makes the claim. All five formats represented; price only on the
    # structured comparison + how-it-works ads. Claim guards: morning caffeine-free
    # (cordyceps), night = parasympathetic not sedation, no mg, Trifecta = one tube.
    "acquisition_v1": {
        "run_id": "tea_acquisition_batch2",
        "audience": "acquisition",
        "ads": [

            # 01 — comparison / spec_card · Afternoon — fruit-body vs mycelium-on-grain
            {
                "file": "01_fruit_body_vs_grain.png",
                "product_type": "tea",
                "sku": "afternoon",
                "format": "comparison",
                "archetype": "spec_card",
                "hook": "Most mushroom drinks are mostly grain. This is all mushroom.",
                "sides": {
                    "left": {
                        "label": "Most mushroom drinks",
                        "points": ["Mycelium grown on grain", "Starch fillers, few actives", "Flat, dusty tea bag"],
                    },
                    "right": {
                        "label": "Alcami tea",
                        "points": ["100% mushroom fruit-body", "Real Lion's Mane, full actives", "Whole-leaf pyramid sachet"],
                    },
                },
                "visual": "sage-green world; our plump whole-leaf pyramid sachet beside a thin flat bag of dull grain powder, same form factor, very different fill.",
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 02 — ugc / ugc_minimal · Morning — the coffee feeling, minus the crash
            {
                "file": "02_morning_coffee_feeling_ugc.png",
                "product_type": "tea",
                "sku": "morning",
                "format": "ugc",
                "archetype": "ugc_minimal",
                "hook": "I get the coffee feeling without the coffee crash.",
                "person": "A woman early-30s, no makeup, relaxed, in a worn sweatshirt",
                "moment": "standing at the kitchen counter just after waking, both hands around a warm cup, the amber-gold Morning tube on the counter beside her",
                "environment": "a real apartment kitchen, soft early daylight through the window, slightly messy and lived-in",
                "text_in_image": "No jitters. Just awake.",
                "text_treatment": "plain phone-caption text, lower third",
                "cta": "Shop Now",
                "cta_style": "none",
                "price": False,
            },

            # 03 — comparison / spec_card · Night — your nightcap vs your morning (price earned)
            {
                "file": "03_night_vs_nightcap.png",
                "product_type": "tea",
                "sku": "night",
                "format": "comparison",
                "archetype": "spec_card",
                "hook": "Your nightcap is working against your morning.",
                "sides": {
                    "left": {
                        "label": "Your usual nightcap",
                        "points": ["Wine or a pill to wind down", "Groggy, foggy next morning", "Still up at 2am"],
                    },
                    "right": {
                        "label": "Alcami Night",
                        "points": ["Reishi for parasympathetic calm", "Wake clear, not groggy", "Deeper sleep, fewer 2am wake-ups"],
                    },
                },
                "visual": "deep-navy calm world; a warm Night cup and our pyramid sachet beside a wine glass and a pill bottle pushed aside.",
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 04 — how_it_works / color_block · Trifecta — the day's arc (price earned)
            {
                "file": "04_trifecta_day_arc.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "how_it_works",
                "archetype": "color_block",
                "hook": "The right cup for morning, afternoon, and night.",
                "headline": "One tea for each part of your day.",
                "subhead": "The right herb at the right hour.",
                "steps": [
                    {"label": "7 AM Morning",    "detail": "Cordyceps for a caffeine-free lift"},
                    {"label": "12 PM Afternoon", "detail": "Lion's Mane for steady, calm focus"},
                    {"label": "9 PM Night",      "detail": "Reishi as the day winds down"},
                ],
                "color_world": "three solid zones flowing left to right: amber-gold, sage-green, deep navy. The gradient Trifecta tube centered where they meet.",
                "cta": "Get the Trifecta",
                "cta_style": "button",
                "price": False,
            },

            # 05 — blocks / annotated · Night — what's inside, no bulleted list
            {
                "file": "05_night_whats_inside.png",
                "product_type": "tea",
                "sku": "night",
                "format": "blocks",
                "archetype": "annotated",
                "hook": "Fewer 2am wake-ups, and you wake up clear.",
                "headline": "Fewer 2am wake-ups.",
                "subhead": "Calm and clear. Caffeine-free.",
                "items": [
                    {"label": "REISHI", "note": "the racing mind finally goes quiet"},
                    {"label": "CHAMOMILE + LAVENDER", "note": "shoulders drop before you reach the pillow"},
                    {"label": "BUTTERFLY PEA FLOWER", "note": "a warm, rich herbal cup"},
                ],
                "proof": ["4.9 stars", "100% fruit-body", "Caffeine-free"],
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 06 — scene / editorial · Night — the evening swap
            {
                "file": "06_night_traded_wine.png",
                "product_type": "tea",
                "sku": "night",
                "format": "scene",
                "archetype": "editorial",
                "hook": "I traded my evening glass of wine for this.",
                "headline": "I traded the wine for this.",
                "subhead": "Night Ritual. Caffeine-free, Reishi calm.",
                "emphasis": {"wine": "gold"},
                "scene": "A quiet, dim living room at night with one warm lamp. The navy Night tube and a calm cup of warm herbal tea on a side table; a wine glass sits empty and set aside, slightly out of focus.",
                "visual_action": "The swap made literal: the wine put down, the warm cup picked up, the room calm and premium.",
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

            # 07 — blocks / social_proof · Trifecta — the proof is the hero
            {
                "file": "07_trifecta_social_proof.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "blocks",
                "archetype": "social_proof",
                "hook": "Thousands rebuilt their whole day around three cups.",
                "headline": "4.9 stars.",
                "subhead": "Thousands switched their whole day to Alcami tea.",
                "emphasis": {"4.9 stars": "gold"},
                "items": [
                    {"label": "MORNING", "note": "the lift that doesn't spike"},
                    {"label": "AFTERNOON", "note": "focus that holds past 3pm"},
                    {"label": "NIGHT", "note": "the evening winds down"},
                ],
                "cta": "Get the Trifecta",
                "cta_style": "button",
                "price": False,
            },

            # 08 — scene / color_block · Morning — clear, not wired
            {
                "file": "08_morning_clear_not_wired.png",
                "product_type": "tea",
                "sku": "morning",
                "format": "scene",
                "archetype": "color_block",
                "hook": "I'm awake by 7 without caffeine and without the crash.",
                "headline": "Clear. Not wired.",
                "subhead": "Morning Ritual. A cordyceps lift, caffeine-free.",
                "emphasis": {"Clear": "gold"},
                "scene": "A bright morning kitchen washed in warm amber-gold light. The amber-gold Morning tube on a clean wooden counter beside a steaming cup, a window of soft daylight behind.",
                "visual_action": "The calm, awake feeling of a morning that didn't need caffeine — light and clean, the tube as its source.",
                "has_cup": True,
                "cta": "Shop Now",
                "cta_style": "button_right",
                "price": False,
            },

            # 09 — ugc / ugc_minimal · Afternoon — cancelled the afternoon coffee
            {
                "file": "09_afternoon_no_crash_ugc.png",
                "product_type": "tea",
                "sku": "afternoon",
                "format": "ugc",
                "archetype": "ugc_minimal",
                "hook": "I cancelled my afternoon coffee and nothing crashed.",
                "person": "A man late-20s in a casual tee at a home desk, unstyled, relaxed",
                "moment": "leaning back at his desk mid-afternoon holding a warm cup, the sage-green Afternoon tube next to his keyboard",
                "environment": "a real home office, slightly cluttered, natural daylight from one side",
                "text_in_image": "No 3pm crash. Day 12.",
                "text_treatment": "plain phone-caption text, lower third",
                "cta": "Shop Now",
                "cta_style": "none",
                "price": False,
            },

            # 10 — blocks / testimonial · Morning — customer voice is the hero
            {
                "file": "10_morning_testimonial.png",
                "product_type": "tea",
                "sku": "morning",
                "format": "blocks",
                "archetype": "testimonial",
                "hook": "My husband hasn't touched coffee in a month.",
                "headline": "My husband hasn't touched coffee in a month.",
                "items": [{"label": "Verified customer", "note": "Morning Ritual"}],
                "proof": ["4.9 stars"],
                "has_cup": False,
                "cta": "Shop Now",
                "cta_style": "button",
                "price": False,
            },

        ],
    },

    # ── pioneer_v1 — category-creator launch, every ad a distinct visual system ─
    # Retarget launch turned UP on the PIONEER claim, engineered so no two ads share
    # a frame, palette, product treatment, OR a line of copy. Each scene overrides
    # color_world + camera to break the per-SKU look; SKUs spread 4/2/2/2. Treatments:
    # poster type, a dark cinematic cup, overhead spilled sachets, a sachet steeping
    # in glass, a 3-zone graphic, hands-and-cup at a window, a macro engraving, a dark
    # two-product shelf, a candid cafe, and a saturated jewel hero. CTAs vary across
    # the full set. Copy is fresh — no line reused from launch_v1. Claims stay
    # defensible ("we started this" / "one of the first" / "first built for X") —
    # never "the only" or "world's first".
    "pioneer_v1": {
        "run_id": "tea_retarget_batch3",
        "audience": "retarget",
        "ads": [

            # 01 — Poster · Trifecta · bright graphic, type-dominant
            {
                "file": "01_started_the_category.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "poster",
                "hook": "We discovered something, then we made the first mushroom tea.",
                "headline": "We discovered something.",
                "subhead": "So we made one of the first mushroom teas.",
                "emphasis": {"discovered": "gold"},
                "color_world": "a clean, bright off-white gallery field with one bold band of saturated brand gold #867353 — graphic and confident, almost a printed poster, not a soft flat-lay",
                "camera": "flat, head-on graphic-poster framing, no perspective distortion",
                "scene": "A typographic poster: the statement set huge across the top two-thirds; the gradient Trifecta tube standing small and crisp on a narrow plinth at lower-center, like a museum label beneath a headline.",
                "visual_action": "Type is the hero and the tube is the receipt — the proof the claim is real.",
                "cta": "Try the Tea",
                "cta_style": "integrated",
                "price": False,
            },

            # 02 — Night · dark cinematic, brewed cup is hero, low angle
            {
                "file": "02_made_for_10pm.png",
                "product_type": "tea",
                "sku": "night",
                "format": "scene",
                "archetype": "editorial",
                "hook": "We made a mushroom tea for 10pm.",
                "headline": "We made a tea for 10pm.",
                "subhead": "Reishi, zero caffeine. A calm wind-down.",
                "emphasis": {"tea": "gold"},
                "color_world": "near-black cinematic darkness broken only by a low warm pool of lamplight on the cup and tube — deep shadow, moody, editorial, the navy canister almost dissolving into the dark",
                "camera": "low three-quarter angle, shallow depth of field, the steaming cup closest to camera",
                "scene": "Late night. A low warm lamp throws a single pool of light over a steaming cup of warm herbal tea in the foreground, the navy Night tube just behind it, everything else swallowed by darkness.",
                "visual_action": "The brewed cup is the hero, not the canister — the felt 10pm moment, the tube as quiet proof behind it.",
                "has_cup": True,
                "cta": "Shop the Night",
                "cta_style": "text_link",
                "price": False,
            },

            # 03 — Morning · overhead flat-lay, sachets spilled out
            {
                "file": "03_lift_without_caffeine.png",
                "product_type": "tea",
                "sku": "morning",
                "format": "scene",
                "archetype": "editorial",
                "hook": "A better morning that doesn't run on caffeine.",
                "headline": "Better mornings, no caffeine.",
                "subhead": "Cordyceps, not coffee. Our new morning tea.",
                "emphasis": {"Better mornings": "gold"},
                "color_world": "warm golden 7am daylight raking across a pale surface from a low side angle, honey-toned and airy, long soft morning shadows",
                "camera": "directly overhead flat-lay, everything arranged on the surface below",
                "scene": "An overhead flat-lay on a sunlit pale-wood counter: the amber-gold Morning tube open, three pyramid sachets spilled out beside it in a loose fan, a spoon and an empty cup, raking golden light.",
                "visual_action": "The product opened up and laid out from above — the sachets, the lift, the morning — not a tube standing on a table.",
                "has_cup": False,
                "cta": "Explore Mornings",
                "cta_style": "button_right",
                "price": False,
            },

            # 04 — Afternoon · sachet steeping in a clear glass, sunlit desk
            {
                "file": "04_steep_your_3pm.png",
                "product_type": "tea",
                "sku": "afternoon",
                "format": "scene",
                "archetype": "editorial",
                "hook": "We made a fix for the 3pm slump.",
                "headline": "A tea to fix your 3pm.",
                "subhead": "Lion's Mane clarity, fresh in your glass. New.",
                "emphasis": {"3pm": "gold"},
                "color_world": "bright clean midday daylight, fresh sage-and-glass tones, crisp cool shadows on a sunlit desk",
                "camera": "eye-level macro on a clear glass cup, the sachet steeping mid-frame, ultra-shallow focus",
                "scene": "A bright sunlit desk at 3pm. A pyramid sachet steeping in a clear glass cup, soft tendrils of herbal color releasing into the hot water, the sage-green Afternoon tube softly out of focus behind it.",
                "visual_action": "The brew itself is the hero — the sachet blooming in clear glass — proof of real fruiting-body inside, not a tube on a table.",
                "has_cup": True,
                "cta": "Steep One",
                "cta_style": "pill_right",
                "price": False,
            },

            # 05 — Blocks · Trifecta · 3-zone graphic, the timed system
            {
                "file": "05_three_firsts.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "blocks",
                "archetype": "color_block",
                "style": "benefit_highlights",
                "hook": "One tea timed to your whole day.",
                "headline": "One tea. All day.",
                "subhead": "Three mushrooms, timed to your day. New from Alcami.",
                "emphasis": {"All day": "gold"},
                "items": [
                    {"label": "7 AM", "note": "Cordyceps, for the climb"},
                    {"label": "1 PM", "note": "Lion's Mane, for the focus"},
                    {"label": "9 PM", "note": "Reishi, for the landing"},
                ],
                "color_world": "three bold vertical color zones — warm gold, sage green, deep navy, left to right — clean graphic blocks, high contrast, confident, not a photo",
                "cta": "Get the Trifecta",
                "cta_style": "button",
                "price": False,
            },

            # 06 — Morning · hands and cup at a bright window (human, full context)
            {
                "file": "06_morning_feels_yours.png",
                "product_type": "tea",
                "sku": "morning",
                "format": "scene",
                "archetype": "editorial",
                "hook": "We worked hard to get this morning tea right.",
                "headline": "We worked hard on this one.",
                "subhead": "Your new morning tea. Caffeine-free.",
                "emphasis": {"worked hard": "gold"},
                "color_world": "bright airy window light, soft and slightly overexposed at the edges, pale linen and warm natural skin tones, a calm sunlit kitchen",
                "camera": "natural medium shot, both hands and the cup in focus, the person softly present in frame",
                "scene": "A person in a sunlit kitchen by a bright window, both hands wrapped around a warm cup, the amber-gold Morning tube on the sill beside them. Relaxed and unhurried, the person clearly present in full — never a floating hand.",
                "visual_action": "A human morning moment, not a product shot — the cup held, the light, the calm; the tube simply belongs on the sill.",
                "has_cup": True,
                "cta": "Shop Mornings",
                "cta_style": "none",
                "price": False,
            },

            # 07 — Night · extreme macro of the engraving, moody craft
            {
                "file": "07_macro_night_craft.png",
                "product_type": "tea",
                "sku": "night",
                "format": "scene",
                "archetype": "editorial",
                "hook": "We obsessed over every detail of the night tea.",
                "headline": "We obsessed over this one.",
                "subhead": "Our new night tea. Reishi for 9pm.",
                "emphasis": {"obsessed": "gold"},
                "color_world": "deep navy-and-gold near-darkness, a thin dramatic raking light catching fine embossed detail, jewel-like, almost black",
                "camera": "extreme macro, raking light across the embossed mushroom engraving, ultra-shallow focus",
                "scene": "An extreme macro of the navy Night tube's surface: the gold mushroom engraving and ALCAMI wordmark catching a thin raking light, fine texture, the rest falling into deep shadow. Not the full canister, just the crafted detail.",
                "visual_action": "Pure craft and detail — the engraving filling the frame — a completely different way to show the product.",
                "has_cup": False,
                "cta": "Meet the Night",
                "cta_style": "text_link",
                "price": False,
            },

            # 08 — Two-product · blend + Trifecta · DARK dramatic shelf (color_world breaks the cream look)
            {
                "file": "08_first_blend_then_tea.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "editorial",
                "hook": "It's the Alcami you trust, now as a tea.",
                "headline": "It's Alcami. Now in tea.",
                "subhead": "The blend you love, plus something new.",
                "emphasis": {"Now in tea": "gold"},
                "color_world": "a dark dramatic shelf — deep charcoal and shadow with one warm side light grazing both products, rich and premium, deliberately NOT a bright cream flat-lay",
                "camera": "low side-lit product shot, dramatic chiaroscuro, both products lit from one side out of the dark",
                "scene": "A dark walnut shelf in near-shadow. The cream Original blend pouch and the gradient Trifecta tea tube stand side by side, both catching a single warm side light against deep darkness, clear space between them.",
                "visual_action": "Two products from one family lit dramatically out of the dark — recognition with weight, not a bright catalog shot.",
                "has_cup": False,
                "cta": "Meet the Tea",
                "cta_style": "integrated",
                "price": False,
                "extra_refs": [{"orig": "assets/brand/product_images_blend/original frontBIL2 .png"}],
            },

            # 09 — Afternoon · candid cafe, off-center, real-life
            {
                "file": "09_coffee_break_reinvented.png",
                "product_type": "tea",
                "sku": "afternoon",
                "format": "scene",
                "archetype": "editorial",
                "hook": "Try the new afternoon tea at 3pm.",
                "headline": "Try it at 3pm.",
                "subhead": "Our new afternoon tea. Clean focus, no crash.",
                "emphasis": {"Try it": "gold"},
                "color_world": "warm candid cafe daylight, soft bokeh background, lived-in and real, afternoon sun through a window",
                "camera": "candid off-center medium shot, product to one side, shallow cafe bokeh behind",
                "scene": "A candid cafe tabletop in afternoon light: the sage-green Afternoon tube and a cup set off to one side of the frame, a blurred cafe interior behind, a notebook and phone just in view — a real break, not a styled set.",
                "visual_action": "An off-center, candid, real-life cafe moment — the tea as the coffee-break replacement, not a centered hero.",
                "has_cup": True,
                "cta": "Try the Afternoon",
                "cta_style": "pill",
                "price": False,
            },

            # 10 — Trifecta · saturated jewel-toned hero (color_world breaks the cream look)
            {
                "file": "10_whole_day_in_one_tube.png",
                "product_type": "tea",
                "sku": "trifecta",
                "format": "scene",
                "archetype": "color_block",
                "hook": "We made this tea for you.",
                "headline": "We made this for you.",
                "subhead": "The new Alcami tea. Just try it.",
                "emphasis": {"for you": "gold"},
                "color_world": "a deep saturated jewel-toned backdrop — rich plum and emerald with a gold rim light, dramatic, high-gloss and editorial, deliberately NOT cream",
                "camera": "bold straight-on hero, dramatic gold rim lighting, product large and centered",
                "scene": "A dramatic hero against a saturated jewel-toned backdrop: the full gradient Trifecta tube, entirely in frame and never cropped, lit with a gold rim light, glossy and bold, an occasion.",
                "visual_action": "Maximum drama on a rich saturated ground — the opposite of a soft cream flat-lay — the tube as a jewel.",
                "has_cup": False,
                "cta": "Shop the Tea",
                "cta_style": "button",
                "price": False,
            },

        ],
    },

}
