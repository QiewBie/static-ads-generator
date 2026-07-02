# ─────────────────────────────────────────────────────────────────────────────
# Alcami Blend — Campaign Config
#
# All blend (Creamy Mushroom Latte) campaigns live here as named sections.
# Four flavors: original / cacao / matcha / espresso
#
# Run: python3 gen.py batches/blend.py --campaign <name>
#
# Folder naming (run_id) — micro-pain system:
#   {product}_{theme}_{micropain}   e.g. blend_productivity_coffee-anxiety
# Each campaign is ONE micro-pain from research/painpoints-{theme}.md, so the
# output folder names the exact situation it targets (not an opaque batch number).
# theme matches the painpoints file; micropain is a short kebab slug of the pain.
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

    # ── productivity_coffee_anxiety — micro-pain #1 (research/painpoints-productivity.md) ──
    # ONE micro-pain, SEVEN DISTINCT situations inside it — not one idea in seven fonts.
    # The pain: a caffeine-sensitive knowledge worker needs to focus, but coffee betrays
    # them. The situations: 01 escalation (the 4th coffee that still didn't land) ·
    # 02 the bind (need focus, hate jitters) · 03 the crash (sharp then foggy, an energy
    # curve) · 04 the reframe (blamed anxiety, it was coffee) · 05 the body symptom (racing
    # heart, sitting still) · 06 the quit story (switched off coffee, the shaking stopped) ·
    # 07 the ingredient concept (nine adaptogens, one scoop). COFFEE IS THE VILLAIN
    # throughout (frames the problem, never the product noun).
    #
    # Layout follows research/ad-design-principles.md: headline → pouch → social proof →
    # CTA across three dominance levels; social proof on every ad (varied treatment); the
    # CTA isolated from the proof chips; type personality chosen per register, never a
    # generic default sans.
    #
    # HOOK DISCIPLINE (the gate): every hook is ONE beat, problem-first, short, lifted from
    # real voice — never setup→conclusion→solution. The hook carries the PROBLEM; the
    # visual + body copy carry the solution (never crammed into the line). Cut decoration-
    # specificity (no "by 10am" filler). Default device: a direct problem question.
    #
    # Claims surgically true: no-jitter / no-spike / no-crash / calm steady focus — this focus
    # angle leads on the no-crash payoff, not the caffeine-free fact (true for Original, but
    # that's the sleep angle's lever); no medical/anxiety-cure language (anxiety lives only in
    # first-person VOICE describing the coffee problem). CTA varied across the batch. ORIGINAL pouch only.
    "productivity_coffee_anxiety": {
        "run_id": "blend_productivity_coffee-anxiety",
        "audience": "acquisition",
        "ads": [

            # 01 — scene / editorial · escalation — the fourth coffee that still didn't land
            {
                "file": "01_fourth_coffee.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "Fourth coffee and still can't focus?",
                "headline": "Four coffees in and still foggy?",
                "subhead": "Calm, steady focus. No jitters, no crash.",
                "emphasis": {"foggy": "gold"},
                "proof": ["NSF Certified", "90-day guarantee"],
                "scene": "A bright home desk: three or four COLD, drained, used coffee cups pushed aside to the left — the abandoned past — while the person sits calm, done with coffee, holding a single warm CREAMY Alcami latte in a clean ceramic mug (clearly different from the disposable coffee cups, NOT another coffee). The opened Alcami Original pouch stands prominent in the LOWER-RIGHT of the frame, filling that space, gold foil catching bright daylight — the resolution she switched to.",
                "visual_action": "The cold abandoned coffee cups are the past she's done with; the warm creamy Alcami latte in her hand is the switch she already made; the pouch lower-right is what she changed to. She is NOT reaching for another coffee.",
                "color_world": "a bright morning desk lit by a soft cream-to-warm-peach SUNRISE GRADIENT (a real glow, not a flat wash); the drained coffee cups stay cool, grey and desaturated against it — the warm gradient reads as relief, the grey cups as the dead past; the Alcami latte and gold-foil pouch the warmest, brightest, glowing focal points",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "button", "type_personality": "editorial_serif", "price": False,
            },

            # 02 — comparison / color_block · the bind — need the focus, hate the jitters
            {
                "file": "02_focus_hate_jitters.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "color_block",
                "hook": "Need to focus, but hate coffee jitters?",
                "emphasis": {"focus": "gold"},
                "sides": {
                    "left":  {"label": "Coffee",  "points": ["Jittery, can't focus", "Anxious by the second cup", "Crashes mid-afternoon"]},
                    "right": {"label": "Alcami",  "points": ["78% report sharper focus", "89% feel calmer", "84% more steady energy"]},
                },
                "visual": "a clean, BALANCED two-column split (both halves equally weighted, intentionally designed): the LEFT a cool desaturated slate-blue GRADIENT — coffee's tense world — with a single jittery half-drunk black coffee; the RIGHT a warm amber-to-cream GRADIENT — calm — with the Alcami Original pouch standing solidly GROUNDED on a real surface (soft contact shadow, never floating) beside a calm creamy cup, pouch crisp and undistorted with every label detail accurate. The cool-blue-vs-warm-amber contrast IS the bind resolving; the warm right is clearly the answer.",
                "cta": "Shop Now", "cta_style": "button", "type_personality": "condensed_bold", "price": False,
            },

            # 03 — scene / poster · the crash — sharp then foggy, rendered as an energy curve
            #      The mechanism is ONE fast-recognizable graphic — two energy lines — taking second
            #      attention after the head, then the pouch, then CTA + proof. A numbered time-block
            #      timeline is wrong here: it reads as a pill-by-the-hour dosing schedule for an
            #      anti-pill brand (research/ad-design-principles.md).
            {
                "file": "03_sharp_then_foggy.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "hook": "Sharp at 9, but already foggy by 11?",
                "headline": "Sharp at 9, but already foggy by 11?",
                "emphasis": {"foggy": "gold"},
                "associative": True,
                "scene": "A clean graphic poster (NOT a photograph) with a STRICT SIZE HIERARCHY — never a wall of equal-size text. HERO (large): a simple two-line energy graph in the upper-middle — a jagged COOL-GREY 'Coffee' line that spikes hard then crashes to nothing, and a smooth WARM-GOLD 'Alcami' line that rises gently and holds steady; just the two line SHAPES, a tiny label on each. Directly beneath the graph, ONE small subordinate caption (much smaller than the headline) explains why: 'Steady adaptogen energy - no spike to crash from.' The Original pouch stands grounded at the lower right as the resolution. The three certifications sit together as ONE small, unified, low trust strip beside the CTA — tiny and grouped on a single line, NEVER three big separate blocks. Generous breathing room; every level a clearly different size.",
                "visual_action": "The crashing grey line is the problem; the steady gold line is the turn; the small why-caption makes it credible; a tiny grouped trust strip de-risks it; the pouch is the resolution. Strict hierarchy — graph and headline big, the why-line and certs clearly small.",
                "color_world": "a clean cream field with a soft warm-gold radial GLOW behind the pouch fading out to bright cream; the coffee line cool steel-grey, the Alcami line warm confident gold — color carries the spike-vs-steady story",
                "proof": ["NSF Certified", "Third-party tested", "90-day guarantee"],
                "cta": "Shop Now", "cta_style": "arrow_down", "type_personality": "condensed_bold", "price": False,
            },

            # 04 — ugc / ugc_minimal · the reframe — blamed anxiety, it was the coffee (real-case voice)
            {
                "file": "04_wasnt_anxiety.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "Turns out it wasn't anxiety. It was my coffee.",
                "person": "A Gen-Z woman, early-to-mid 20s — the trendy 'that girl' wellness-creator look (effortless, current, relatable, lightly styled), face visible and genuine.",
                "moment": "A true front-facing selfie held at arm's length — her own hand on the phone, arm extended toward the camera the way a real selfie looks (you feel the arm holding the camera, never a second phone shown in frame), caught candid and slightly off-angle mid-moment, NOT posed or composed. The opened Alcami Original pouch sits prominent in the foreground beside a creamy mug, label readable — no coffee in sight.",
                "environment": "A real lived-in Gen-Z home space with natural window light and a few real colorful touches (plants, warm wood, a personal pop of color) — looks discovered in a feed, shot on an iPhone, not a flat beige set.",
                "text_in_image": "turns out it wasn't anxiety. it was my coffee.",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

            # 05 — scene / poster · the body symptom — racing heart while sitting still
            {
                "file": "05_heart_racing.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "hook": "Just sitting, but heart is going crazy?",
                "headline": "Just sitting, but heart's going crazy?",
                "subhead": "Steady energy that won't spike on you.",
                "emphasis": {"crazy": "gold"},
                "scene": "A bold typographic poster on a warm amber field, in two CLEARLY SEPARATED bands: the headline fills the UPPER portion as large type ('crazy' the gold focal word), then a CLEAR EMPTY HORIZONTAL GAP before the product zone begins. In the LOWER third, on a real warm wood desk in soft light, a smartwatch shows a high heart-rate alert beside the Alcami Original pouch — the pouch sits LOW and crisp as the calm resolution, and NEVER overlaps, touches, or rises into the headline type above it.",
                "visual_action": "The racing-heart question dominates; the watch alert makes it literal; the pouch below is the calm answer.",
                "color_world": "a warm amber-to-honey GRADIENT field over a real wood desk, deepening toward the edges — richer and more dimensional than flat cream, soft morning light, warm not clinical; negative space for the type",
                "cta": "Shop Now", "cta_style": "arrow_down", "type_personality": "condensed_bold", "price": False,
            },

            # 06 — scene / editorial (phone-look WOT) · the swap story — swapped coffee FOR Alcami
            #      The account's top-performing pattern (stacked first-person lines over a warm
            #      lifestyle photo), but the product is the EXPLICIT answer: the latte is the thing
            #      she swapped her coffee for, the headline says the swap, and a CTA closes the loop
            #      (a quit story with no alternative + no action is a dead end). Coffee = the villain
            #      she left; Alcami = what she drinks now.
            {
                "file": "06_quit_coffee.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "I swapped my morning coffee for this. The shaking stopped.",
                "headline": "I swapped my coffee for this.",
                "subhead": "Adaptogenic mushrooms instead of the jitters.",
                "emphasis": {"swapped": "gold"},
                "stats": ["Calmer mornings", "Focus that lasts"],
                "associative": True,
                "social_proof": "star_row",
                "scene": "A warm, intimate first-person morning photo with ONE coherent stage: a single warm wood desk, soft warm lamp light from the left, the room easing gently to soft shadow behind (one consistent background, nothing floating). The opened Alcami Original pouch and a fresh CREAMY Alcami latte sit together on the wood as her NEW morning drink — the thing she swapped her coffee for, unmistakably the hero and the answer, NO coffee anywhere in frame. The two benefits read as two small clean designed elements (not a comma-jammed line, not bolted-on boxes). The pouch is clearly what 'this' in the headline points at.",
                "visual_action": "The creamy Alcami latte is the new morning ritual that replaced coffee; the pouch is what 'this' refers to; the two benefit elements and the star rating are small and designed-in; the CTA tells them what to do.",
                "color_world": "a warm, intimate lamp-lit morning in a deep amber-to-soft-cream GRADIENT — rich warm depth (honey, amber, soft shadow falling off behind), the creamy latte and gold-foil pouch the glowing focal points; the warmth reads as relief, never a flat dim wash",
                "camera": "shot on a phone, slightly off-angle, first-person",
                "lighting": "one soft warm lamp from the left, warm and inviting, the room easing to soft shadow — intimate real morning, not studio-lit",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "button", "type_personality": "light_serif_italic", "price": False,
            },

            # 07 — blocks / ingredient_breakdown · the ingredient concept — nine adaptogens, one scoop
            #      The batch's ingredient-led cut: the super-herbs ARE the visual, each named with its
            #      one job, thin call-out lines from the pouch. Outcome hook (relief from the shelf),
            #      not an ingredient-list dump. Four heroes shown; the headline carries the full nine.
            {
                "file": "07_nine_adaptogens.png",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "style": "ingredient_breakdown", "archetype": "annotated",
                "hook": "Nine adaptogens. One scoop. No more shelf.",
                "headline": "Nine adaptogens. One scoop.",
                "subhead": "The whole morning shelf, in one creamy cup.",
                "emphasis": {"scoop": "gold"},
                "associative": True,
                "items": [
                    {"label": "Lion's Mane", "note": "focus & clarity"},
                    {"label": "Cordyceps", "note": "clean, steady energy"},
                    {"label": "Reishi", "note": "calm, no jitters"},
                    {"label": "Shilajit", "note": "85+ trace minerals"},
                ],
                "color_world": "a premium apothecary field with a soft warm radial GLOW behind the pouch (deep sand deepening to cream at the edges), dimensional and rich — not a flat beige; EXACTLY four call-outs total, one per adaptogen (Lion's Mane, Cordyceps, Reishi, Shilajit), each name appearing ONCE and NEVER duplicated or repeated, with a thin gold call-out line and a small real botanical image beside each name; editorial and uncluttered, never a busy supplement-facts panel",
                "cta": "Shop Now", "cta_style": "button", "type_personality": "editorial_serif", "price": False,
            },

        ],
    },

    # ── productivity_3pm_crash — micro-pain #2 (research/painpoints-productivity.md) ──
    # ONE micro-pain, THREE DISTINCT situations inside it. The pain: an office/WFH
    # worker whose brain "stops braining" by 2-3pm — the fog rolls in, hours still on
    # the clock, and the reflexive fix is a third coffee that doesn't land. The
    # situations: 01 the recognition (the day's over at 3, but it's only 1) ·
    # 02 the third coffee that betrays again (coffee = villain, the afternoon cup that
    # doesn't fix it) · 03 the steady-afternoon mechanism (Lion's Mane clarity +
    # no-crash adaptogen energy that holds past 3). COFFEE IS THE VILLAIN throughout.
    #
    # Divergence: poster · color_block · spec_card — three registers, three CTAs
    # (arrow_down · button · ghost_right), three type personalities. No two ads wear
    # the same treatment.
    #
    # Claims surgically true: no-crash / steady-through-the-afternoon / Lion's Mane
    # focus — this afternoon-focus angle leads on no-crash, not the caffeine-free fact
    # (true for Original, but that's the sleep angle's lever); no medical/ADHD language
    # (the "dead zone" / "brain isn't braining" lives only in first-person VOICE
    # describing the problem). ORIGINAL pouch only.
    "productivity_3pm_crash": {
        "run_id": "blend_productivity_3pm-crash",
        "audience": "acquisition",
        "ads": [

            # 01 — scene / poster · the recognition — the day's effectively over by 3
            {
                "file": "01_day_over_at_three.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "hook": "Is your day over by 3, but it's only 1?",
                "headline": "Is your day over by 3?",
                "subhead": "Steady focus that holds through the afternoon. No crash.",
                "emphasis": {"3": "gold"},
                "associative": True,
                "scene": "A bold typographic poster (NOT a photograph) with a STRICT SIZE HIERARCHY. HERO (large): the headline question fills the upper portion, with an oversized gold '3' as the focal numeral — the hour the afternoon shutdown hits. Beneath it, ONE small subordinate caption (much smaller than the headline) carries the turn: 'Steady adaptogen energy that holds - no third-coffee crash.' The Original pouch stands grounded at the lower right as the resolution, gold foil crisp and undistorted. The three certifications sit together as ONE small, unified trust strip beside the CTA - tiny and grouped on a single line, NEVER three big separate blocks. Generous breathing room; every level a clearly different size.",
                "visual_action": "The giant '3' names the hour the day dies; the small why-caption makes the fix credible; a tiny grouped trust strip de-risks it; the pouch lower-right is the resolution. Strict hierarchy - headline and '3' big, the why-line and certs clearly small.",
                "color_world": "a clean cream field with a soft warm-gold radial GLOW behind the pouch fading out to bright cream; the oversized '3' in confident warm gold - the warmth reads as the steady afternoon, never a flat wash",
                "proof": ["NSF Certified", "Third-party tested", "90-day guarantee"],
                "cta": "Shop Now", "cta_style": "arrow_down", "type_personality": "condensed_bold", "price": False,
            },

            # 02 — comparison / color_block · the third coffee that betrays again
            {
                "file": "02_third_coffee_betrays.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "color_block",
                "hook": "Third coffee at 3, and still foggy?",
                "sides": {
                    "left":  {"label": "The third coffee", "points": ["Wired but still foggy", "A jolt, then a deeper dip", "The day's already gone"]},
                    "right": {"label": "Alcami",           "points": ["Lion's Mane clarity, no fog", "Steady energy, no crash", "Focus that holds past 3"]},
                },
                "visual": "a clean, BALANCED two-column split (both halves equally weighted, intentionally designed): the LEFT a cool desaturated slate-grey GRADIENT - the dead-zone afternoon - with a single half-drunk black coffee going cold; the RIGHT a warm amber-to-cream GRADIENT - steady - with the Alcami Original pouch standing solidly GROUNDED on a real surface (soft contact shadow, never floating) beside a calm creamy cup, pouch crisp and undistorted with every label detail accurate. The cool-grey-vs-warm-amber contrast IS the afternoon resolving; the warm right is clearly the answer.",
                "cta": "Shop Now", "cta_style": "button", "type_personality": "condensed_bold", "price": False,
            },

            # 03 — blocks / spec_card · the steady-afternoon mechanism — why it holds past 3
            #      The mechanism cut: Lion's Mane + no-crash adaptogen energy, shown as
            #      designed objects (never a bulleted list). Outcome-led, not an ingredient dump.
            {
                "file": "03_holds_past_three.png",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "archetype": "spec_card",
                "hook": "Why the focus holds when coffee quits on you.",
                "headline": "Steady past 3. No crash.",
                "subhead": "Lion's Mane clarity on calm adaptogen energy: no spike to fall from.",
                "emphasis": {"Steady past 3": "gold"},
                "items": [
                    {"label": "LION'S MANE", "note": "clear focus, not a jolt"},
                    {"label": "NO SPIKE", "note": "nothing to crash from at 3"},
                    {"label": "STEADY ENERGY", "note": "holds through the afternoon"},
                ],
                "proof": ["4.9★", "NSF Certified", "90-day guarantee"],
                "color_world": "a clean spec-card field - bright cream with a soft warm-gold radial glow behind the pouch; the three items read as confident designed objects on a calm grid, never a busy supplement-facts panel",
                "cta": "Shop Now", "cta_style": "pill", "type_personality": "editorial_serif", "price": False,
            },

        ],
    },

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
    # the 89% enhanced-calm proof), never a brand claim; the blend is anti-jitter and NOT a
    # sleep aid, and this parent-relief angle doesn't lean on the caffeine-free fact (true for
    # Original, but it's the sleep angle's lever); before/after shows emotional state, never
    # physique (Meta supplement policy). Delivery note: dad-targeted cuts (06) need dad-specific
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

    # ── sleep_wave1 — the blend's DAYTIME sleep story (research/painpoints-sleep-blend.md) ──
    # The blend is a DAYTIME energy / coffee-replacement, NOT an evening drink — so the
    # sleep angle lives in daylight: the morning AFTER a bad night, and the afternoon
    # coffee that steals the night. The evening-cup / wine-swap angle is dropped (it
    # miscasts the product as a nightcap). Two micro-pains:
    #   E morning-after recovery (steady energy on no sleep, without the jitter stack)
    #   A 3pm-coffee-steals-the-night (swap the afternoon cup to caffeine-free Alcami).
    # TWO formats, alive hooks pulled straight from the real voice — no before/after,
    # no two-column comparison (both kept reading as templated/cluttered):
    #   SCENE 01-03 (alive real moments) · UGC 04-06 (truly native — no proof badge,
    #   a real front-facing selfie, a typed caption).
    # NOT a sleep aid — every claim is ENERGY / caffeine-displacement, never "makes you
    # sleep", sedation, insomnia, or melatonin. Coffee is the villain; the warm creamy
    # Alcami cup is the answer. Original pouch only.
    "sleep_wave1": {
        "run_id": "blend_sleep_wave1",
        "audience": "acquisition",
        "ads": [

            # 01 — SCENE · A · the realization (the alive reframe — real voice: "my afternoon
            #      coffee was keeping me up at night!!"). The winning "turns out it was the
            #      coffee" pattern, applied to sleep.
            {
                "file": "01_turns_out_3pm_coffee.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "Turns out my 3pm coffee was why I was up at 1am.",
                "headline": "Turns out my 3pm coffee was why I was up at 1am.",
                "subhead": "Swapped it for caffeine-free Alcami. My nights came back.",
                "emphasis": {"3pm coffee": "gold"},
                "proof": ["NSF Certified", "90-day guarantee"],
                "scene": "A real desk in the late afternoon, daylight going golden: a person mid-realization, pushing a half-finished afternoon coffee aside and reaching instead for a warm CREAMY Alcami latte. The opened Alcami Original pouch stands grounded at the LOWER-RIGHT as the swap they just made. A clock visible in frame reads about 3pm. Calm, lived-in, real — not a styled set.",
                "visual_action": "The afternoon coffee is the culprit they just figured out; setting it aside for the Alcami latte is the switch; the pouch lower-right is what they changed to. The realization is the whole moment.",
                "color_world": "a real late-afternoon room where the cool, over-caffeinated edge of the day softens into warm golden 3pm daylight around the Alcami; the abandoned coffee stays cool and grey while the warm light gathers on the latte and gold-foil pouch — light and surfaces carry the warmth, the person stays naturally lit",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "button", "type_personality": "editorial_serif",
                "social_proof": "corner_cluster", "price": False,
            },

            # 02 — SCENE · E · morning-after relief, the surprise of steadiness (real voice:
            #      "vibrating / shaking" — the no-jitter payoff made literal in steady hands).
            {
                "file": "02_hands_not_shaking.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "Four hours of sleep and normally I'd be shaking from coffee by now.",
                "headline": "Four hours of sleep. Normally I'd be shaking from coffee.",
                "subhead": "Caffeine-free Alcami instead of a third coffee on an empty tank.",
                "emphasis": {"coffee": "gold"},
                "proof": ["NSF Certified", "90-day guarantee"],
                "scene": "A real morning at a kitchen counter: a visibly under-slept person looking calm and steady, holding a warm CREAMY Alcami latte in two steady hands — no tremor, no wired tension, just quiet steadiness despite the obvious tiredness. The opened Alcami Original pouch stands grounded at the LOWER-RIGHT. Honest, a little messy, real morning light.",
                "visual_action": "The steady hands around the calm latte ARE the proof of the hook — steady on no sleep, without a jittery coffee; the pouch is the reason.",
                "color_world": "a cool, grey, under-slept early morning warming to a steady amber where the latte and pouch sit; the warmth reads as calm energy, not a wired buzz — light and atmosphere carry the tone, the person stays naturally lit",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "button_right", "type_personality": "mixed_weights",
                "social_proof": "star_row", "price": False,
            },

            # 03 — SCENE · A · the betrayal, as a bold poster line (the through-line stated plainly)
            {
                "file": "03_saves_afternoon_steals_night.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "hook": "The coffee that saves your afternoon is stealing your night.",
                "headline": "The coffee that saves your afternoon is stealing your night.",
                "subhead": "Switch the 3pm cup to caffeine-free Alcami.",
                "emphasis": {"stealing your night": "gold"},
                "associative": True,
                "scene": "A bold typographic poster (NOT a photograph) with a STRICT SIZE HIERARCHY: the line fills the upper two-thirds as large type ('stealing your night' the gold focal phrase), then a CLEAR EMPTY HORIZONTAL GAP, then the Alcami Original pouch standing grounded and crisp in the lower third as the switch — low, never rising into the type. Generous breathing room; every level a clearly different size.",
                "visual_action": "The line names the betrayal; the pouch below is the swap that ends it. Type is the hero, the pouch the resolution.",
                "color_world": "a clean poster field shifting from a cool, wired blue-grey at the top (the stolen night) to a warm confident gold around the pouch (the afternoon fixed without caffeine) — the cool-to-warm gradient carries the turn",
                "cta": "Shop Now", "cta_style": "arrow_down", "type_personality": "condensed_bold",
                "social_proof": "stamp", "price": False,
            },

            # 04 — UGC · E · morning-after, woman (truly native: front-facing selfie, typed caption, no proof badge)
            {
                "file": "04_four_hours_no_coffee_ugc.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "Had four hours of sleep and honestly I'm doing fine without coffee this morning.",
                "person": "A woman late-20s to early-30s, light natural makeup, hair casually pulled back, a little tired-eyed but genuinely relaxed and smiling slightly — she looks fine, just a bit under-slept. A real person, not a polished creator.",
                "moment": "A selfie in her kitchen — phone held in one hand at arm's length, she's looking at the camera with a small genuine smile. A warm creamy Alcami latte on the counter beside her; the opened Alcami Original pouch just in frame, label readable. NO coffee anywhere.",
                "environment": "A real lived-in kitchen, natural early-morning window light, a little messy and unstyled — looks discovered in a feed, shot on her own phone.",
                "text_in_image": "had four hours of sleep and honestly I'm doing fine without coffee this morning",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

            # 05 — UGC · A · quit the 3pm coffee, man (truly native)
            {
                "file": "05_quit_3pm_coffee_ugc.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "I stopped my 3pm coffee a week ago and honestly I'm finally sleeping again.",
                "person": "A man late-20s to mid-30s, casual tee, a little stubble, relaxed and real — not a polished creator.",
                "moment": "A true front-facing selfie held at arm's length (his own hand on the phone) at his desk in the late afternoon — face toward the camera, slightly off-angle, a small smile. A warm creamy Alcami latte in his other hand; the opened Alcami Original pouch sits by his keyboard, label readable. NO coffee cup in frame.",
                "environment": "A real home office, mild clutter, natural side daylight — looks shot on his own phone, discovered in a feed.",
                "text_in_image": "stopped my 3pm coffee a week ago and honestly the nights are so much better",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

            # 06 — UGC · E · the surprise-clarity, different woman (truly native)
            {
                "file": "06_worst_sleep_clear_morning_ugc.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "hook": "It was the worst sleep of the year but somehow this is the clearest morning I've had in weeks.",
                "person": "A woman mid-30s to early-40s, makeup-free, a busy-professional-at-home vibe, tired-eyed but genuine — a real person, not a creator.",
                "moment": "A true front-facing selfie held at arm's length (her own hand on the phone) in her kitchen mid-morning — face toward the camera, slightly off-angle. A warm creamy Alcami latte in her other hand; the opened Alcami Original pouch just in frame on the counter, label readable. NO coffee in frame.",
                "environment": "A real lived-in kitchen, soft daylight, a little morning mess — shot on her own phone, looks like a real post.",
                "text_in_image": "worst sleep of the year but somehow this is the clearest morning I've had in weeks",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
            },

        ],
    },

    # ── core_portfolio_v1 — a lever-spread "portfolio" batch (Superscale-style) ──
    # Not one micro-pain — a COVERAGE MAP across buyer-psychology levers, each ad
    # tagged with `lever` + a 3-part `rationale` (angle/format/design) that prints to
    # BRIEF.md. Demonstrates the strategic layer, the dark-premium register (01/02),
    # and the copy structures ("benefit without the villain", "N reasons"). Our rigor
    # vs the reference tool: REAL numbers (200,000+, nine adaptogens), enforced claims.
    "core_portfolio_v1": {
        "run_id": "blend_core_portfolio",
        "audience": "acquisition",
        "ads": [

            # 01 — BENEFIT · dark-premium poster · "benefit without the villain"
            {
                "file": "01_energy_focus_calm.png",
                "concept": "Energy / Focus / Calm",
                "lever": "benefit",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "hook": "Energy without the spike, focus without the fog, calm without the pills.",
                "headline": "Energy. Focus. Calm.",
                "subhead": "Without the spike. Without the fog. Without the pills.",
                "emphasis": {"Calm": "gold"},
                "type_personality": "editorial_serif",
                "scene": "A premium typographic poster on a deep near-black ground: ENERGY / FOCUS / CALM stacked huge in a high-contrast editorial serif, each paired to the right with a thin divider rule and a small qualifier — 'without the spike' / 'without the fog' / 'without the pills'. A thin gold rule, then the Alcami Original pouch lower-right as the ONE warm, lit object glowing against the dark. Generous negative space, strict size hierarchy.",
                "visual_action": "Each stacked benefit disarms a villain (spike/fog/pills); the pouch is the single warm resolution glowing out of the dark.",
                "color_world": "a deep near-black premium ground (the brand's dark #282111 world), cream type, one warm gold rule, the pouch the only lit warm object — dark, editorial, thumb-stopping; the opposite of a bright cream flat-lay",
                "proof": ["10:1 Full Spectrum", "Non-GMO", "Lab Tested"],
                "social_proof": False,
                "cta": "Shop Now", "cta_style": "integrated", "price": False,
                "rationale": {
                    "angle": "States all three core outcomes at once and pairs each with the villain it removes — 'without the pills' is the anti-stack DNA that separates us from a supplement routine.",
                    "format": "A type-dominant poster lets the three benefits own the frame; the parallel 'without the X' rhythm is built for big stacked type.",
                    "design": "A near-black ground is thumb-stopping in a bright wellness feed and reads premium; the pouch as the one warm object is unmistakably the resolution.",
                },
            },

            # 02 — INGREDIENT-PROOF · dark forest-green grid · transparency
            {
                "file": "02_nine_adaptogens_grid.png",
                "concept": "Nine Adaptogens, One Scoop",
                "lever": "ingredient-proof",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "style": "ingredient_breakdown", "archetype": "annotated",
                "hook": "Nine adaptogens, one scoop, no shelf to keep straight.",
                "headline": "Nine adaptogens. One scoop.",
                "subhead": "10:1 full-spectrum extracts. No sugar, no crash.",
                "emphasis": {"Nine": "gold"},
                "type_personality": "editorial_serif",
                "items": [
                    {"label": "Lion's Mane", "note": "clarity & focus"},
                    {"label": "Cordyceps", "note": "natural energy"},
                    {"label": "Reishi", "note": "calm & balance"},
                    {"label": "Shilajit", "note": "vitality & minerals"},
                ],
                "color_world": "a deep forest-green premium ground; the heading a high-contrast cream editorial serif; the adaptogens as clean dark cards in a tidy grid (each name in gold, its one job in cream beneath) — EXACTLY the four shown (Lion's Mane, Cordyceps, Reishi, Shilajit), each named once and NEVER duplicated; the Original pouch lower-center, warm and lit against the green. NO bullet dots — designed cards only.",
                "social_proof": False,
                "cta": "Make the Switch", "cta_style": "button", "price": False,
                "rationale": {
                    "angle": "Ingredient transparency is a top trust factor for first-time supplement buyers — naming the adaptogens and their jobs answers 'what's actually in this'.",
                    "format": "A grid of designed cards carries high proof density without a wall of text; the headline carries the full nine, the cards show the heroes.",
                    "design": "Deep forest-green is thumb-stopping and nature-aligned for a mushroom brand; cards organize the proof so it reads premium, not busy.",
                },
            },

            # 03 — COMPARISON · coffee vs Alcami · objection handling
            {
                "file": "03_coffee_vs_alcami.png",
                "concept": "Coffee vs Alcami",
                "lever": "comparison",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "color_block",
                "hook": "Same warm morning cup. None of the jitters.",
                "emphasis": {"jitters": "gold"},
                "sides": {
                    "left":  {"label": "Coffee", "points": ["Jitters by the second cup", "Anxious, wired focus", "The 11am crash"]},
                    "right": {"label": "Alcami", "points": ["Calm, steady focus", "Nine adaptogens, no spike", "Holds all morning, no crash"]},
                },
                "visual": "a balanced two-column split: LEFT a cool desaturated slate world with a jittery black coffee; RIGHT a warm amber world with the Alcami Original pouch grounded (soft contact shadow, never floating) beside a creamy cup, crisp and undistorted. The cool-vs-warm contrast IS the switch.",
                "cta": "Make the Switch", "cta_style": "button_right", "type_personality": "condensed_bold", "price": False,
                "rationale": {
                    "angle": "Handles the #1 objection to quitting coffee — losing the focus — by showing the same outcome without the jitters and the crash.",
                    "format": "A two-column comparison lets the contrast persuade; parallel rows keep it factual, not preachy.",
                    "design": "Cool-desaturated-left vs warm-amber-right makes the switch legible at a glance; Alcami is the full-contrast resolution.",
                },
            },

            # 04 — SOCIAL-PROOF · the real number (our rigor: 200,000+, not an invented count)
            {
                "file": "04_200k_social_proof.png",
                "concept": "200,000 Strong",
                "lever": "social-proof",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "archetype": "social_proof",
                "hook": "200,000 people switched and stayed.",
                "headline": "200,000+ customers. Zero celebrity endorsements.",
                "subhead": "They found it, tried it, and came back.",
                "emphasis": {"200,000+": "gold"},
                "type_personality": "mixed_weights",
                "items": [
                    {"label": "84% more energy", "note": "customer-reported"},
                    {"label": "78% sharper focus", "note": "customer-reported"},
                ],
                "proof": ["200,000+ customers", "NSF Certified", "90-day guarantee"],
                "social_proof": False,
                "cta": "Shop Now", "cta_style": "button", "price": False,
                "rationale": {
                    "angle": "Social proof is the highest-converting element for supplements; the real 200,000+ figure plus 'zero celebrity endorsements' is earned trust a rival can't manufacture.",
                    "format": "A proof-as-hero layout makes the number the composition; customer-reported outcomes back it without overclaiming.",
                    "design": "The oversized count anchors the eye first; everything else stays sub-dominant so the proof reads as the headline.",
                },
            },

            # 05 — BRAND · premium aspirational hero
            {
                "file": "05_morning_reimagined_hero.png",
                "concept": "Your Morning, Reimagined",
                "lever": "brand",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "The whole morning shelf, reimagined as one warm cup.",
                "headline": "Your morning, reimagined.",
                "subhead": "Nine adaptogens. One creamy ritual. No crash.",
                "emphasis": {"reimagined": "gold"},
                "type_personality": "editorial_serif",
                "scene": "A premium hero: the Alcami Original pouch and a fresh creamy latte on a clean, warm-lit neutral surface, soft morning light, generous negative space — aspirational and calm, the product the quiet center.",
                "visual_action": "The pouch and creamy latte are the reimagined morning ritual — premium, simple, the resolution to the cluttered shelf.",
                "color_world": "a warm premium morning light on a clean neutral surface, soft cream-to-sand gradient, the pouch and latte the warm focal points — aspirational, editorial, uncluttered",
                "social_proof": False,
                "cta": "Start the Ritual", "cta_style": "ghost_right", "price": False,
                "rationale": {
                    "angle": "The brand/aspiration play — frames Alcami as the elevated replacement for the whole morning routine, the identity the wellness buyer wants.",
                    "format": "A clean editorial hero lets the product and ritual breathe; minimal copy keeps it premium.",
                    "design": "Warm, bright, generous negative space reads aspirational and on-brand; the light makes the pouch the calm center.",
                },
            },

        ],
    },

    # ── sleep_wave2 — the bad-sleep CYCLE (research/painpoints-sleep-blend.md) ──────
    # ONE unified narrative: bad sleep → more coffee to cope → caffeine wrecks next
    # night → repeat. Alcami breaks the loop: caffeine-free energy today, nothing
    # following you to bed tonight. Every claim is ENERGY / caffeine-displacement —
    # the viewer connects the dots to "better sleep" themselves, we never promise it.
    # NOT a sleep aid. Coffee is the villain; the blend is the caffeine-free swap.
    # Original pouch only. Compliance: never "fall asleep faster," "cures insomnia,"
    # "knocks you out," "sleep through the night," "replaces melatonin," no mg.
    #
    # Micro-pains consumed: A (afternoon coffee steals the night) · E (morning-after
    # recovery) · C (evening drink void — wine swap only, not chamomile/sleep-tea)
    # · the full cycle named plainly.
    #
    # Format spread: poster-scene · editorial-scene ×2 · annotated-blocks ·
    # comparison · ugc · color_block-blocks — 5 formats, 6 distinct archetypes.
    "sleep_wave2": {
        "run_id": "blend_sleep_wave2",
        "audience": "acquisition",
        "ads": [

            # 01 — POSTER · the cycle named plainly — bold typographic declaration
            #      "Bad sleep. More coffee. Worse sleep." The three-beat cycle IS the
            #      composition; the pouch at the bottom is the break in the loop.
            {
                "file": "01_the_cycle.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "concept": "The Bad-Sleep Cycle",
                "lever": "problem-aware",
                "hook": "Bad sleep. More coffee. Worse sleep. You see the pattern.",
                "headline": "Bad sleep. More coffee. Worse sleep.",
                "subhead": "Alcami breaks the loop. Caffeine-free energy that doesn't follow you to bed.",
                "emphasis": {"Worse sleep": "gold"},
                "associative": True,
                "scene": "A bold typographic poster (NOT a photograph) with a STRICT SIZE HIERARCHY: the three-beat cycle 'Bad sleep. More coffee. Worse sleep.' fills the upper two-thirds as large stacked type ('Worse sleep' the gold focal phrase), then a CLEAR EMPTY HORIZONTAL GAP, then the Alcami Original pouch standing grounded and crisp in the lower third as the answer — the break in the loop. Generous breathing room; every level a clearly different size.",
                "visual_action": "The three-beat cycle names the pattern; the pouch below is the swap that ends it. Type is the hero, the pouch the resolution.",
                "color_world": "deep charcoal at the top (the trapped cycle) shifting to warm confident gold around the pouch at the bottom (the break) — the dark-to-warm gradient carries the turn from problem to answer",
                "cta": "Shop Now", "cta_style": "arrow_down", "type_personality": "condensed_bold",
                "social_proof": "stamp", "price": False,
                "rationale": {
                    "angle": "Names the vicious cycle every coffee drinker recognizes — the three-beat rhythm triggers instant recognition and the pouch is the resolution.",
                    "format": "A poster lets the cycle statement dominate — type IS the composition, nothing competes.",
                    "design": "Dark-to-gold gradient physically moves the eye from problem (dark) to answer (warm gold pouch) — the scroll-stop is the contrast in a bright feed.",
                },
            },

            # 02 — EDITORIAL SCENE · E · morning-after recovery — worst night, no coffee
            #      needed. Energy claim: steady, caffeine-free, no jitters on no sleep.
            {
                "file": "02_worst_night_no_coffee.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "concept": "Worst Night, No Coffee",
                "lever": "benefit",
                "hook": "Slept terribly last night. Still didn't need coffee to function.",
                "headline": "Slept terribly. Still didn't need coffee.",
                "subhead": "Steady, caffeine-free energy - no jitters on an empty tank.",
                "emphasis": {"coffee": "gold"},
                "proof": ["NSF Certified", "90-day guarantee"],
                "scene": "A real kitchen, early morning, honest daylight through a window. A visibly tired person — under-slept but calm and steady — holding a warm CREAMY Alcami latte. No coffee maker in sight, no coffee cup in frame. The opened Alcami Original pouch sits on the counter, label readable. Lived-in, real, not styled.",
                "visual_action": "The calm steadiness despite obvious tiredness IS the proof — steady on no sleep, without coffee. The pouch is the reason.",
                "color_world": "a cool grey early-morning light warming to steady amber where the latte and pouch sit — the warmth reads as calm energy on a rough day, not a wired buzz",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "pill", "type_personality": "editorial_serif",
                "social_proof": "corner_cluster", "price": False,
                "rationale": {
                    "angle": "The surprise of functioning after a terrible night without reaching for coffee — a personal, felt energy claim.",
                    "format": "An editorial scene lets the moment breathe — the tiredness and the calm coexist in one honest frame.",
                    "design": "Cool-to-warm gradient mirrors the feeling: a grey, rough start warming to steady amber around the product.",
                },
            },

            # 03 — ANNOTATED BLOCKS · what coffee breaks, Alcami's super-herbs fix.
            #      Nine functional ingredients that deliver where coffee fails.
            {
                "file": "03_what_coffee_cant_give.png",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "archetype": "annotated",
                "concept": "What Coffee Can't Give You",
                "lever": "ingredient-proof",
                "hook": "Everything coffee promises but never delivers. Nine super-herbs and mushrooms that actually do.",
                "headline": "What coffee breaks, Alcami fixes.",
                "items": [
                    {"label": "LION'S MANE", "note": "Focus that stays steady - no 3pm fog"},
                    {"label": "CORDYCEPS", "note": "Clean energy without the caffeine spike"},
                    {"label": "REISHI", "note": "Calm your coffee never gave you"},
                ],
                "proof": ["NSF Certified", "200,000+ customers", "Caffeine-free"],
                "emphasis": {"Alcami": "gold"},
                "color_world": "warm cream-to-gold gradient, premium and clean - the pouch is the warm focal point, each ingredient block feels like a designed card on a lightly tinted ground",
                "cta": "Shop Now", "cta_style": "pill", "type_personality": "mixed_weights",
                "social_proof": "badge_lockup", "price": False,
                "rationale": {
                    "angle": "Flips the script: instead of attacking coffee, shows what Alcami's super-herbs deliver that coffee can't - steady focus, clean energy, actual calm.",
                    "format": "Annotated blocks let each ingredient stand as its own proof point, designed as cards not bullets.",
                    "design": "Warm cream-to-gold keeps the premium feel; each ingredient block is a distinct designed object.",
                },
            },

            # 04 — EDITORIAL SCENE · the cycle confession — personal realization voice.
            #      "I was drinking coffee to fix the tiredness that coffee was causing."
            {
                "file": "04_cycle_confession.png",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "concept": "The Cycle Confession",
                "lever": "lifestyle",
                "hook": "I was fixing my tiredness with the exact thing causing it.",
                "headline": "I was fixing my tiredness with the exact thing causing it.",
                "subhead": "Switched to caffeine-free Alcami. The cycle broke itself.",
                "emphasis": {"causing it": "gold"},
                "proof": ["NSF Certified", "90-day guarantee"],
                "scene": "A real home desk, late afternoon golden light. A person mid-realization, pushing a half-finished coffee cup aside with one hand, holding a warm CREAMY Alcami latte in the other. The opened Alcami Original pouch sits on the desk, label readable. A small moment of clarity — they just figured it out. Lived-in, real, not a styled set.",
                "visual_action": "The coffee being pushed aside IS the realization — the person just connected the dots; the Alcami latte in their other hand is the answer they already switched to. The pouch grounds the frame.",
                "color_world": "warm late-afternoon golden light, the abandoned coffee stays cool and grey while the warm glow gathers on the Alcami latte and gold-foil pouch — light carries the turn from problem to resolution",
                "has_cup": True,
                "cta": "Shop Now", "cta_style": "pill_right", "type_personality": "light_serif_italic",
                "social_proof": "star_row", "price": False,
                "rationale": {
                    "angle": "The recursive irony — coffee fixing coffee's own damage — is immediately recognizable to every afternoon-coffee drinker. The personal voice makes it feel discovered, not sold.",
                    "format": "An editorial scene captures the mid-realization moment; the personal italic type matches the confessional register.",
                    "design": "Golden afternoon light naturally warms the Alcami side while the coffee stays cool/grey — the frame tells the story before the words do.",
                },
            },

            # 05 — COMPARISON · A · third coffee vs. Alcami — parallel energy products,
            #      caffeine-absence as fact (not sleep promise). Price earned in comparison.
            {
                "file": "05_third_coffee_vs_alcami.png",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "spec_card",
                "concept": "Third Coffee vs. Alcami",
                "lever": "comparison",
                "hook": "Your third coffee costs you more than $5. It costs you tonight's sleep.",
                "sides": {
                    "left": {
                        "label": "Your 3rd coffee",
                        "points": ["300mg+ caffeine by 3pm", "Jitters, anxiety, 11am crash", "Still in your system at midnight"],
                    },
                    "right": {
                        "label": "Alcami Blend",
                        "points": ["Zero caffeine, 9 super-herbs", "Steady energy, no crash", "Nothing in your system by bedtime"],
                    },
                },
                "visual": "split world — harsh cool grey left (the jittery coffee world) vs. warm cream-to-gold right (the calm Alcami side); the Alcami Original pouch stands full-contrast on the right.",
                "emphasis": {"tonight's sleep": "gold"},
                "color_world": "a strict split — cool, harsh, desaturated grey on the coffee side vs. warm cream-to-gold on the Alcami side; the temperature difference IS the argument",
                "cta": "Shop Now", "cta_style": "button", "type_personality": "mixed_weights",
                "social_proof": "corner_cluster", "price": False,
                "rationale": {
                    "angle": "Reframes the 'cost' of a third coffee beyond dollars — the caffeine still in your system at midnight is the real price. Both sides are energy products, so the comparison is parallel and fair.",
                    "format": "A two-column comparison lets the viewer run the math themselves — each row is apples-to-apples.",
                    "design": "The cool/warm split makes the argument visual before the text loads — grey jitters vs. golden calm.",
                },
            },

            # 06 — UGC · E + A · the swap story — personal, native, energy outcome.
            #      "Replaced my afternoon coffee with Alcami three weeks ago."
            {
                "file": "06_replaced_afternoon_coffee_ugc.png",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal",
                "concept": "The Afternoon Coffee Swap",
                "lever": "social-proof",
                "hook": "Replaced my afternoon coffee with Alcami three weeks ago. Mornings aren't a war anymore.",
                "person": "A man early-30s, casual tee, relaxed and genuinely happy with a small confident smile — he looks good, at ease, content. A real person, not a polished creator.",
                "moment": "A true front-facing selfie held at arm's length at his kitchen counter, morning — face toward the camera, slightly off-angle. A warm creamy Alcami latte in his other hand; the opened Alcami Original pouch sits on the counter just in frame, label readable. NO coffee anywhere in the frame.",
                "environment": "A real apartment kitchen, natural morning window light, a little messy and unstyled — looks discovered in a feed, shot on his own phone.",
                "text_in_image": "replaced my afternoon coffee with this three weeks ago and honestly mornings aren't a war anymore",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
                "rationale": {
                    "angle": "A personal swap story — names what he replaced (afternoon coffee), names the product (Alcami), and states a morning energy outcome. The sleep improvement is implied, never stated.",
                    "format": "UGC authenticity — a real person's phone post is the most relatable device for cold traffic.",
                    "design": "Deliberately unpolished: natural light, real kitchen, no staging. The pouch label is the only brand signal.",
                },
            },

            # 07 — COLOR_BLOCK BLOCKS · dark-premium · ingredient proof — 9 super-herbs
            #      and mushrooms, zero caffeine, energy benefits. The subhead names Alcami.
            {
                "file": "07_nine_adaptogens_zero_caffeine.png",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "archetype": "color_block",
                "concept": "Nine Super-Herbs, Zero Caffeine",
                "lever": "credibility",
                "hook": "Nine super-herbs and mushrooms in one scoop. Zero caffeine in your system by tonight.",
                "headline": "9 super-herbs and mushrooms. Zero caffeine.",
                "subhead": "Alcami: the energy that doesn't cost you your night.",
                "items": [
                    {"label": "LION'S MANE", "note": "Cognitive clarity, focus without fog"},
                    {"label": "CORDYCEPS", "note": "Natural energy, no caffeine spike"},
                    {"label": "REISHI", "note": "Calm, steady - no crash at 3pm"},
                ],
                "proof": ["NSF Certified", "90-day guarantee", "200,000+ customers"],
                "emphasis": {"Zero caffeine": "gold"},
                "color_world": "deep near-black to warm gold — the Alcami Original pouch is the one warm, lit object on a dark ground, the gold-foil typography glowing; the dark register stops the scroll in a bright feed",
                "cta": "Shop Now", "cta_style": "button_right", "type_personality": "condensed_bold",
                "social_proof": "stamp", "price": False,
                "rationale": {
                    "angle": "Leads with what the product IS (nine super-herbs and mushrooms) and what it ISN'T (caffeine). A cold viewer immediately knows: energy product, real ingredients, caffeine-free.",
                    "format": "Color-block zones give each ingredient its own space — designed objects, not a list.",
                    "design": "Dark-premium register breaks the warm/light monotony; the pouch as the one warm object on near-black is a proven scroll-stopper.",
                },
            },

        ],
    },

    # ── gut_relief_v1 — the gut / low-acid story, 5 divergent creative cuts ─────────
    # The gut wedge, claim-SAFE: coffee's acidity (and raw-greens grit) is the VILLAIN;
    # Alcami is the creamy, LOW-ACID, dairy-free morning cup carrying the real "GUT BALANCE
    # + IMMUNITY" badge on the pouch. The discomfort lives only in first-person VOICE or in
    # the coffee/greens contrast — NEVER a brand claim that Alcami treats a condition (no
    # "soothes / heals / cures", no gastritis / distension / inflammation language; that's
    # the off-brand medical trap blend_gut_v1 fell into). Emotion = relief/comfort.
    # ORIGINAL pouch only. Five frames · five devices · five emotions (no two share the
    # frame+device+emotion triple): 01 coffee-wreck reframe (scene/editorial, realization)
    # · 02 low-acid sensory (dark-premium poster, confidence) · 03 gut-balance-on-the-label
    # (annotated, trust) · 04 the swap (ugc, relief) · 05 greens paradox (comparison vs AG1,
    # vindication). CTAs + type personalities + color worlds all vary across the set.
    "gut_relief_v1": {
        "run_id": "blend_gut_relief",
        "audience": "acquisition",
        "ads": [

            # 01 — scene / editorial · the reframe — it wasn't the stomach, it was the coffee
            {
                "file": "01_wasnt_my_stomach.png",
                "concept": "It Wasn't My Stomach",
                "lever": "problem-aware",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "editorial",
                "hook": "Turns out my stomach wasn't the problem. My morning coffee was.",
                "headline": "It wasn't my stomach. It was the coffee.",
                "subhead": "Swapped it for a creamy, low-acid cup. Mornings sit easy again.",
                "emphasis": {"the coffee": "gold"},
                "scene": "A real morning kitchen counter in warm daylight. A person mid-realization sets a harsh, cold black coffee aside with one hand and lifts a warm CREAMY Alcami latte with the other; the opened Alcami Original pouch stands grounded at the LOWER-RIGHT, gold foil catching the light. The cold coffee reads grey and harsh; the creamy cup reads warm and gentle.",
                "visual_action": "The cold coffee being set aside is the culprit they just named; the creamy Alcami latte they lift instead is the gentle swap; the pouch lower-right is what they changed to.",
                "color_world": "a real morning warming from a cool, harsh grey around the abandoned coffee to soft cream-and-amber daylight around the Alcami latte and gold-foil pouch — light carries the turn from harsh to gentle, the person naturally lit",
                "has_cup": True,
                "cta": "Make the swap", "cta_style": "text_link", "type_personality": "light_serif_italic",
                "social_proof": "star_row", "price": False,
                "rationale": {
                    "angle": "The strongest gut micro-pain is coffee wrecking the stomach; the reframe ('it wasn't my stomach') lifts the blame off the body onto the coffee — which is exactly the swap Alcami is.",
                    "format": "An editorial scene of the mid-swap moment lets a stranger read the whole story — harsh coffee set down, creamy cup picked up — at a glance.",
                    "design": "A cool-harsh-grey to warm-cream gradient makes 'harsh vs gentle' legible before the words load; the creamy cup is the visible proof it goes down easy.",
                },
            },

            # 02 — scene / poster · dark-premium · the low-acid sensory contrast
            {
                "file": "02_like_cream_not_acid.png",
                "concept": "Like Cream, Not Acid",
                "lever": "benefit",
                "product_type": "blend", "sku": "original",
                "format": "scene", "archetype": "poster",
                "hook": "Coffee meets an empty stomach like acid. This meets it like cream.",
                "headline": "Goes down like cream. Not acid.",
                "subhead": "Low-acid, dairy-free, gentle on an empty stomach.",
                "emphasis": {"cream": "gold"},
                "scene": "A bold typographic poster (NOT a photograph) with a STRICT SIZE HIERARCHY on a deep near-black ground: the line 'Goes down like cream. Not acid.' fills the upper portion as large premium type ('cream' the gold focal word), a thin gold rule beneath it, then the Alcami Original pouch beside a single warm CREAMY latte in the lower third — the ONE warm, lit, creamy object glowing out of the dark. Generous negative space; every level a clearly different size.",
                "visual_action": "The sensory line is the hero; the creamy cup glowing warm against the near-black is the literal payoff of 'like cream', the pouch the resolution.",
                "color_world": "a deep near-black premium ground (the brand's dark #282111 world), cream type, one warm gold rule, the pouch and creamy latte the only warm lit objects — dark, editorial, thumb-stopping in a bright wellness feed",
                "has_cup": True,
                "cta": "Switch your cup", "cta_style": "integrated", "type_personality": "editorial_serif",
                "social_proof": False, "price": False,
                "rationale": {
                    "angle": "Translates 'low-acid' from a spec into a felt sensory contrast — coffee like acid, Alcami like cream — the exact difference a sensitive stomach wants.",
                    "format": "A type-led poster lets the one sensory line own the frame; minimal everything else keeps it premium.",
                    "design": "The dark-premium register (the gap in our warm/light range) stops the scroll; the creamy cup as the one warm object IS the 'like cream' proof.",
                },
            },

            # 03 — blocks / annotated · the gut-balance badge, read off the real pouch
            {
                "file": "03_gut_balance_on_the_label.png",
                "concept": "Gut Balance, On The Label",
                "lever": "ingredient-proof",
                "product_type": "blend", "sku": "original",
                "format": "blocks", "archetype": "annotated",
                "hook": "The gut-balance line is printed right on the pouch.",
                "headline": "Gut balance, built into the label.",
                "subhead": "Not a promise in an ad. A line on the pouch.",
                "emphasis": {"the label": "gold"},
                "items": [
                    {"label": "GUT BALANCE + IMMUNITY", "note": "the badge on every pouch"},
                    {"label": "LOW-ACID, COCONUT BASE", "note": "gentle where coffee is harsh"},
                    {"label": "NO DAIRY, NO SUGAR", "note": "nothing that sits heavy"},
                    {"label": "REISHI + LION'S MANE", "note": "calm, clear energy"},
                ],
                "proof": ["NSF Certified", "Dairy-free"],
                "color_world": "a warm apothecary field — deep sand deepening to cream at the edges with a soft glow behind the pouch — premium and uncluttered; each call-out a small designed label on a thin gold connector line to the exact spot on the pouch it names, never a bulleted list",
                "cta": "See what's inside", "cta_style": "pill", "type_personality": "mixed_weights",
                "social_proof": "badge_lockup", "price": False,
                "rationale": {
                    "angle": "Most gut ads make a vague promise; this points at the literal 'GUT BALANCE + IMMUNITY' badge on the real pouch — a claim the customer can verify on the product itself.",
                    "format": "Annotated connector lines tie each benefit to the exact spot on the pouch, so 'what's inside' reads as a designed diagram, not a list.",
                    "design": "Warm apothecary tones read premium and credible; thin gold connectors make the pouch the proof, not decoration.",
                },
            },

            # 04 — ugc / ugc_minimal · the swap, native and relieved
            {
                "file": "04_stomach_stopped_hating_mornings.png",
                "concept": "Stomach Stopped Hating Mornings",
                "lever": "social-proof",
                "product_type": "blend", "sku": "original",
                "format": "ugc", "archetype": "ugc_minimal", "capture_mode": "propped_phone",
                "hook": "I swapped my morning coffee for this and my stomach finally stopped hating mornings.",
                "person": "A real person early-to-mid 30s, unstyled, relaxed and genuinely relieved, holding a warm creamy mug — natural body language, face visible.",
                "moment": "Morning in her kitchen, a small content smile — relieved and easy; the opened Alcami Original pouch in use on the counter beside the creamy cup she just made, label readable. NO coffee anywhere in frame.",
                "environment": "A real lived-in kitchen, soft morning window light, a little unstyled — looks discovered in a feed, shot on her own phone.",
                "text_in_image": "swapped my morning coffee for this and my stomach stopped hating mornings",
                "creator_tag": "@alcamielements",
                "cta": "Shop Now", "cta_style": "none", "price": False,
                "rationale": {
                    "angle": "A first-person swap story — names what she replaced (morning coffee) and the felt relief (stomach stopped hating mornings) without a single medical word.",
                    "format": "UGC is the most relatable cold-traffic device; a propped-phone kitchen grab reads as a discovery, not an arm's-length ad-selfie.",
                    "design": "Deliberately unpolished — natural light, real kitchen, the pouch label the only brand signal; the creamy cup shows the gentle swap in use.",
                },
            },

            # 05 — comparison / color_block · the greens paradox (AG1 as the muted contrast)
            {
                "file": "05_greens_or_a_cup_you_crave.png",
                "concept": "Greens, Or A Cup You Crave",
                "lever": "comparison",
                "product_type": "blend", "sku": "original",
                "format": "comparison", "archetype": "color_block", "competitor": "ag1",
                "hook": "A scoop of raw grassy greens, or a creamy cup you actually crave?",
                "headline": "Choke down greens, or crave your cup?",
                "emphasis": {"crave": "gold"},
                "sides": {
                    "left":  {"label": "Greens powders", "points": ["A scoop of raw grassy fiber", "Gritty, grassy, sits heavy", "Choked down, never craved"]},
                    "right": {"label": "Alcami",         "points": ["A creamy 10:1 concentrate", "Smooth, low-acid, easy", "A cup you actually crave"]},
                },
                "proof": ["Gut balance + immunity", "NSF Certified"],
                "visual": "a balanced two-column split: LEFT a cool desaturated green world with the AG1 greens pouch and a gritty green shake going flat; RIGHT a warm cream-gold world with the Alcami Original pouch grounded (soft contact shadow, never floating) beside a creamy latte, crisp and undistorted. The grassy-green-vs-creamy-gold contrast IS the choice.",
                "cta": "See the difference", "cta_style": "button", "type_personality": "condensed_bold",
                "social_proof": "corner_cluster", "price": False,
                "rationale": {
                    "angle": "The greens-powder paradox is a direct competitor wedge — a bucket of raw fermentable grass vs a creamy concentrate with gut balance built in; the contrast is texture and form, never a medical claim about the rival.",
                    "format": "A parallel two-column comparison lets the texture contrast (gritty grass vs creamy) carry the argument, apples-to-apples per row.",
                    "design": "Cool grassy-green left vs warm creamy-gold right makes the choice legible at a glance; Alcami is the full-contrast craveable answer.",
                },
            },

        ],
    },

}
