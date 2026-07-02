---
name: generate-ads
description: Generate Alcami ad creatives (blend or tea, acquisition or retarget) from slim specs via the prompt_builder + gen.py pipeline. Use when the user wants to create, design, or produce static ad images for Facebook/Instagram.
---

# Generate Ads — Alcami Elements (blend + tea)

You write **slim specs**; `prompt_builder.py` assembles the full Gemini prompt; `gen.py` calls the API and writes images. One skill covers both product lines and both audiences — `product_type` and `audience` switch the behavior.

## The Pipeline

```
batches/blend.py · batches/tea.py   ← you write specs here (campaigns)
prompt_builder.py                   ← THE ENGINE: prompts, SKU constants, archetypes,
                                       audience policy, price anchors, claim guards, validator
gen.py                              ← calls Gemini → ad-workspace/[RUN_ID]/
```

**Never write raw Gemini prompts.** Write specs. The builder owns prompt craft.

**Authorities — write within them, never restate their rules in specs or here. Each fact has ONE home; copying it into a spec is how drift starts:**
- **The engine** — `prompt_builder.py` (formats, archetypes, audience policy, SKU color worlds, hard rules) + `brand_facts.py` (price anchors, the customer count) + `pb_validate.py` (the claim guards). Live matrix: `python3 gen.py --policy`.
- **`CLAUDE.md`** — brand identity, voice, ICP, the always-true claim/creative rules.
- **`tea-product-brief.md`** — tea creative strategy (the tea deep-dive).
- **`competitors.py`** — the rival registry (positioning, ad-style, comparison assets) for competitor ads.

**Reference detail (load only when you need it — keeps this skill lean):**
- [reference/brand-visual.md](reference/brand-visual.md) — color palette, per-flavor creative palettes, typography personalities, logo.
- [reference/ingredients.md](reference/ingredients.md) — the nine ingredients + what each does (ingredient-led ads).
- [reference/assets.md](reference/assets.md) — where the source pouch/canister/ingredient/kit images live (picking refs).

## Workflow

1. **Research** (if needed) — use the **research** skill (audience micro-pains, competitor ads, product facts). Never WebFetch/WebSearch.
2. **Diverge** — before writing any spec, sketch 2–3 genuinely different concepts per ad slot and pick the strongest. Never commit the first safe idea. See "Concept divergence" below.
3. **Write specs** — each ad is one dict in a campaign. Start from `batches/_template.py`.
4. **Dry run** — `python3 gen.py batches/<file>.py --campaign <name> --dry-run`. The validator prints errors (block generation) and warnings (fix if real).
5. **Pre-flight** — review the assembled prompts AND run the outside-in read (see "Pre-flight" below) before spending any generation budget. This is the judgment gate the validator can't be.
6. **Generate** — drop `--dry-run` (`--force` overwrites; `--only NN` re-runs one ad). The default model is **flash** (draft tier, ≈3.5x cheaper all-in); regenerate client-picked winners at final quality with `--model pro`. **Convention: any run of more than ONE image goes through `--batch`** (the Batch API, 50% price, async — submit it, then `--batch-fetch` collects when it finishes; minutes-to-hours). Interactive (non-batch) generation is reserved for a single-image reroll (`--only NN`).
7. **Deliverables** — images land in `ad-workspace/[RUN_ID]/`.

## Research

Audience micro-pains, competitor ads, and product/category facts are the **research** skill's job — run it first when a batch needs fresh insight. Findings land in `research/` (e.g. `research/painpoints-{theme}.md`, which becomes the brief you write specs from). The pivot the data forces: mine **specific, frequent** micro-pains, not broad themes — one micro-pain ≈ one tight campaign. Never WebFetch/WebSearch.

## From a micro-pain to a campaign (consuming research)

A `research/painpoints-{theme}.md` entry maps 1:1 to a tight campaign — carry its parts into the specs, don't re-genericize them back into a broad theme:
- **the specific situation** → the `hook` and the `scene`/`visual` (the concrete recurring moment, shown or named — "re-reading the same email at 9am," not "be more productive").
- **the real-voice quotes** → the copy register and `headline`/`subhead` wording (use their words; the `ad-copy` skill turns them into primary text).
- **the persona** → visible in the frame or named in copy — the landing page is generic, so the ad alone carries the match.
- **the angle seed + Alcami-fit** → the claim, kept surgically true (the engine's guards hold it; never borrow a competitor's mg / discount / 10x magnitude).

One micro-pain → one campaign → 3–6 creatives that **diverge on frame/device/emotion** (see Concept divergence) while all landing the *same* specific situation. The failure the data punishes: a broad-persona batch where every ad states the theme generically.

## The Spec

```python
{
    "file": "01_night_inside.png",
    "product_type": "tea",          # "blend" or "tea" — drives price/SKUs/claim guards
    "sku": "night",                 # blend: original/cacao/matcha/espresso
                                    # tea:   morning/afternoon/night/trifecta
    "format": "blocks",             # scene/comparison/blocks/ugc/how_it_works
    "archetype": "annotated",       # optional, recommended — see `gen.py --policy`
    "hook": "What's actually in Alcami Night Tea.",
    # ... format-specific fields ...
}
```
`audience` ("acquisition" default / "retarget") is set on the **campaign**; ads inherit it. Core field reference: `batches/_template.py`; the craft fields (`emphasis` · `type_personality` · `social_proof` · `capture_mode` · `has_cup` · `look_seed` · `corner_stamp` · `concept`/`lever`/`rationale`) are documented in this skill's sections below.

## The structured text layer (use this — it carries the MESSAGE, not just a mood)

`scene` renders the full structured block below (headline/subhead/stats/emphasis). The other formats carry the same *ideas* through their own fields — `blocks` via `headline` + `items` + `proof`, `comparison` via the hook + `sides`, `how_it_works` via the hook + `steps` — so reach for those fields there, not `subhead`/`stats`. `ugc` stays deliberately undesigned (its only text is `hook` + an optional `text_in_image` caption; the validator warns if you set the designed fields on a `ugc` ad). Default to giving an ad enough to be understood, not just felt:

**UGC still has to sell.** Super-native with nothing explained = weak: the caption carries an outcome (not just a vibe), the pouch is unmistakably in use with the label readable, and the primary text explains what the product is. When the explanation must live *in the image*, use a phone-look `scene` (editorial archetype, phone camera/lighting overrides) instead of `ugc` — it keeps the casual feel and can carry a designed line.

**UGC capture is a rotated parameter (`capture_mode`).** The engine rotates HOW the phone shot was grabbed — `arms_length` (selfie) · `pov_handheld` (no face, own hand in frame) · `propped_phone` (static angle, hands free) · `friend_candid` (caught across the table) · `mirror` — seeded by filename, so a batch of "real posts" isn't five identical selfies. Pin one whenever the `person`/`moment` prose implies a framing (the validator warns when prose dictates a selfie but no mode is pinned); write the *moment*, not the camera, in the prose.

- `headline` — the message, rendered dominant (largest, reads first). Falls back to `hook` if omitted.
- `subhead` — the clarifier / category line / second idea (~55% of headline). Add when the viewer needs more than the headline.
- `stats` / `proof` — aliases for the same proof chips (either name works in any rendering format): up to 3, each its own chip. Keep them product-correct: blend → `["200,000+ customers", "NSF Certified", "90-day guarantee"]`; tea → `["4.9 stars", "USDA Organic", "100% fruit-body"]`. Never cross them — "200,000+" and NSF are blend-only (the validator hard-errors on "200,000+" in tea text).
- `social_proof` — a sub-dominant trust mark that rides on most acquisition ads, its treatment rotating per ad (seeded by filename) so a batch mixes proof looks instead of repeating one. Treatments: `star_row` · `corner_cluster` · `big_number` · `badge_lockup` · `stamp`. ON by default for acquisition; **OFF for `ugc`** (a ★-rating / customer-count lockup breaks the "real person's post" feel — UGC sells through relatability, not badges), OFF for retarget (launch register), and **OFF for the `social_proof` archetype** (proof is already the designed hero there, so a sub-dominant rider would duplicate the count and contradict the hierarchy). Set `social_proof: False` to opt any ad out, or name a treatment to force one. Wording is claim-locked by product: blend → five ★ + "200,000+ customers"; tea → 4.9★ + "loved by thousands" (never 200,000 / a count on tea). Distinct from the `proof`/`stats` chips (certs/outcomes) and from the `social_proof` *archetype* (proof as the whole hero) — a batch with no visible trust mark is the failure this prevents.
- `emphasis` — per-word typography: a dict of `{"phrase": "treatment"}`. Treatments: `bold` · `italic` · `underline` · `strike` (negates — great for comparison "before" rows) · `gold` (brand accent) · `boxed` (own background chip).
  - The validator **enforces placement**: a phrase not in the headline/subhead is a hard **error**; a stopword ("the") or a phrase appearing twice is a **warning**. Emphasis always lands on a real, meaningful word.
  - **One gold focal-anchor word per headline — non-negotiable.** Every headline carries exactly one emphasized (`gold`) word: the single mark the eye catches first, the front idea made visible. A headline with no anchor reads "too heavy, nothing to grab." Don't over-paint either — two or three gold words and the anchor dissolves.
  - **Anchor a word IN the headline, never the subhead's lead phrase.** Emphasizing the opening words of a `subhead` makes the model render a phantom duplicate gold sub-headline (a floating "Calm, steady focus" ghost). Keep the anchor on a headline word; if the subhead truly needs a highlight, pick a word mid-phrase, not its lead. And never *delete* emphasis to fix a problem — that just removes the anchor.
- `type_personality` — the headline's font voice, chosen to the register and never left to a generic sans. The catalog: `condensed_bold` (Bebas/Impact — confrontational, declarative) · `editorial_serif` (Didot/Bodoni — premium, considered) · `light_serif_italic` (a personal, spoken voice) · `mixed_weights` (a thin serif headline + small bold all-caps subtext — two contrasting ideas) · `oversized_numeral` (a massive numeral as the graphic hero). Set it on any ad where the type carries the mood; unset falls back to the archetype default, which on quiet archetypes is a plain sans. Pick the one that feels inevitable for the hook — don't auto-reach for `condensed_bold`, and a personal/voice hook in heavy condensed type is as wrong as a declaration in delicate italic.

**Register — pick one deliberately, don't default to safe.** Two legitimate modes:
- **Explanatory** (the default) — the product **category** ("Adaptogenic Mushroom Tea" / "Superfood Mushroom Latte") is forced legible so a stranger instantly knows what it is.
- **Associative / mood-led** — set `"associative": True` to suppress the forced category so the ad can lead with feeling and intrigue (the "From the forest" winner is this mode). This is a **first-class choice** for the right concept, not a fallback — reach for it when the image earns recognition rather than explanation. Override the cue's wording with `category_cue`; force the cue onto an ad the engine would skip it on (retarget, or copy that already says "latte"/"tea") with `force_category: True`.

When the ad needs information (pain points, bullets, a testimonial), use the body fields for that format — `items` (blocks), `sides` (comparison), `steps` (how_it_works) — alongside headline/subhead. Match the amount of text to the format.

## Clean copy/layout path for blocks

`blocks` accepts two shapes through **one** builder. RECOMMENDED: `headline` + `items` ([{label,note}]) + `proof`. Also accepted: a free-form `blocks` list of `{size,content}` (the validator nudges you toward `items`). The engine designs items as objects, never a bulleted list. Reference the hook anywhere with the `{hook}` token.

## Formats & archetypes

Formats: `scene` · `comparison` · `blocks` · `ugc` · `how_it_works`.
Design archetypes (the graphic layer): `editorial` · `spec_card` · `annotated` · `color_block` · `badge` · `ugc_minimal` · `testimonial` · `social_proof` · `poster` · `screenshot` · `before_after`. If you omit `archetype`, the engine applies a sensible per-format default (the validator tells you which) — but set it explicitly for intended variety. Run `python3 gen.py --policy` for descriptions and audience fit.

**Bold/DR devices — use them; the brand's top performers are loud:**
- `poster` — an oversized number/word/statement IS the composition (200,000. / 10:1.).
- `screenshot` — a native IG/FB comment, review card, or text exchange; cold-traffic authenticity.
- `before_after` — two honest states; the change is the whole point.
- **WOT (wall-of-text) — the account's top-performing pattern:** stacked bold claim lines + a highlighted hook ("Why I quit RYZE…") over a darkened lifestyle photo, native and first-person. Build it as a phone-look `scene` (editorial archetype + phone `camera`/`lighting`) carrying a multi-line `headline` + `stats`/`proof`, or as a `screenshot` cut. Keep claims surgically true — the proven version leaned on `1000mg / 85% off / 10x RYZE`, which our guards forbid; swap the magnitude for a specific, true outcome.
- `corner_stamp` (a field, not an archetype; distinct from the `stamp` social-proof treatment) — a bold corner stamp like `"RESTOCK"` / `"NEW"` / `"BESTSELLER"`. Opt-in, and use ONLY for a literally true state — never manufacture scarcity (the validator warns).

**Naming a rival in creative:** allowed for *brands* (never people). Show the competitor by pouch/form factor + brand name in text, never a distorted logo; keep every comparative claim true, parallel, and substantiated; and treat the rival as a creative *parameter* — it can anchor a `scene`, `poster`, or `before_after`, not just the two-column `comparison`. Full stance + the `assets/competitors_assets/` files (AG1, IM8): **CLAUDE.md → Competitors**. The validator warns whenever a rival is named.

## Photographic variety (you don't need to set this, but you can)

Each SKU has a `mood`; the engine rotates camera + lighting per ad (seeded by filename — stable re-runs, but different files look different). Override per spec with `camera` and/or `lighting` when a shot needs a specific look. To **re-roll the photography on the same file** without renaming it, bump `look_seed` (any string) — it reseeds every deterministic pick (camera, lighting, proof treatment). Color worlds are tonal anchors, not single-hue washes — real rooms, natural materials.

**Color is a chosen parameter, not a default — set `color_world` per ad to the emotion.** Left blank it falls back to the SKU tone, and a whole batch on that one tone reads monotonous. Give each ad real range — a gradient, a brightness or warm/cool shift matched to its feeling (cold desaturated grey = the problem / coffee; warm amber, sunrise glow, radial gold = the relief). The Original pouch stays cream/gold (brand rule) — the color lives in the **light, surface, and background gradient**, never repainted onto the pouch.

**A dark-premium register is first-class — use it to break the warm/light monotony and stop the scroll.** Most blend ads run cream/light; a deep near-black or deep-forest-green `color_world`, a big high-contrast editorial serif, and the pouch as the *one warm, lit object* is a strong thumb-stopping contrast in a bright feed (the "ENERGY / FOCUS / CALM — without the spike / fog / pills" look). Reach for it on `editorial`/`poster` benefit and ingredient-grid ads, and **alternate dark and light across a batch** so the set has range.

**The artistic medium is a chosen parameter too (`art_style`) — the biggest scroll-stopping lever.** Every ad defaults to `photographic`; the category (and most of our own batches) is wall-to-wall wellness photography, so a non-photographic cut is the strongest way to stop the scroll. The curated palette: `editorial_graphic` (flat premium print — color fields, vector shapes, museum-poster restraint) · `illustrated` (crafted editorial / botanical illustration, echoing the pouch's own mushroom engraving — never cartoonish) · `risograph` (limited-palette screenprint grain). A non-photographic style swaps the persona (illustrator / designer, not photographer), drops camera/lighting, and lets the *concept* lead while the pouch stays recognizable. Pairs with any non-`ugc` format/archetype (`ugc` is phone-photographic — `art_style` is ignored there). Don't ship a whole batch photographic — the brief flags an all-photographic set. Keep it on-brand: premium and crafted, never woo-woo or childish. (Compositing the real pouch onto the rendered background makes these fully safe; until then the model renders the pouch in-style.)

**Craft devices the category's top spend proves (AG1 / IM8 / RYZE) — reach for these; they're already in the engine:**
- **Show the finished latte, not just the dry pouch** (`has_cup: True` on blend). RYZE shows the prepared drink in nearly every ad because the buyer's real question is "does this still work like coffee" — the creamy latte beside the pouch is the proof the ritual is real and enjoyable. Worth testing on most blend scenes.
- **Tether every floating callout to its object** (the `annotated` archetype) — a thin connector line/dot from a label to the exact product feature it names. A label adrift in the frame is the orphan failure (the same reason proof never floats in a top corner). When an ad points at "what's inside," reach for `annotated`.
- **Match the badge SHAPE to its job** — a starburst/circle reads urgency, a pill reads a verified claim, a speech-bubble reads an announcement, a `corner_stamp` reads a hand-placed mark. Don't render every badge as the same generic rounded chip; the shape should say what the badge is *for*.
- **Density is a register + funnel choice, not a default** — cold/offer-led ads can run dense (several claims, a price, badges); premium and retarget run sparse, and whitespace itself reads premium (IM8's sparsest ads read the most premium). Match the element count to the job.

## Audience fit (strategy here; the enforced format/archetype lists are `AUDIENCE_POLICY` → `gen.py --policy`)

- **Acquisition (cold):** any format/archetype — incl. `ugc`, `testimonial`, `social_proof`, and the bold devices (`poster`, `screenshot`, `before_after`, `comparison`, the `corner_stamp` field). Cold traffic rewards clarity and boldness; the brand's proven winners are loud. **Tea cold acquisition:** the quiet editorial register is the *default*, not a requirement — loud comparison/poster/bold-hook cuts are allowed and worth testing against the quiet one (don't lock cold tea into a whisper).
- **Retarget (warm — already bought):** this is a **product LAUNCH to existing customers**, not an education campaign. Lead with the *news*, not proof. Core angles: "we made tea now!" · "loved the blend? try this" · a **two-product display** (blend + tea in one frame) · insider/early-access · "one of the first mushroom teas." `blocks`/`how_it_works` are the FOLLOW-UP for people who want detail. The validator **warns** on `comparison` (launch register is news, not an argument), `ugc`, `testimonial`, `social_proof` — warm buyers don't need convincing. Every retarget ad must carry a launch signal (Alcami / blend / new / first / now — the validator warns if none is present). Extend the relationship, never gap-fill ("what your ritual is missing" implies the blend is incomplete — it isn't). Keep early-access date-free in the image (no "Pre-Order", no ship dates).

## Concept divergence (before specs)

For each ad slot, rough out **2–3 distinct concepts** before committing to a spec. A concept = a hook + the device that performs it. Force them apart on these axes so you're *choosing*, not settling:

- **Reference frame** — coffee · a nightcap / melatonin · a competitor · a number · provenance · a behavior. (Most cold hooks borrow one — vary which.)
- **Device / archetype** — `comparison` · `poster` · `scene` · `screenshot` · `before_after` · `how_it_works` · `ugc`. (Don't render every idea as the same scene.)
- **Medium (`art_style`)** — `photographic` · `editorial_graphic` · `illustrated` · `risograph`. The hardest axis to vary and the strongest scroll-stopper — don't leave a whole batch photographic.
- **Emotion** — relief · attunement · pride · curiosity · belonging · skeptic-flipped.

Then pick the concept whose hook→visual handoff is sharpest (see "How the hook and visual combine"). **Across a batch: no two ads may repeat the same frame + device + emotion triple** — if two land the same beat, cut one and diverge again. Gut check: if every concept you wrote is a quiet photographic scene, you stopped early — push at least one loud (`poster`/`comparison`/`corner_stamp`), one mood-led (`associative`), and one art-led (`illustrated`/`editorial_graphic`/`risograph`) into the mix before deciding.

## Strategic layer — concept · lever · rationale (the batch brief)

Three optional **meta-fields** turn a batch into a *portfolio* and produce a client-facing brief (`BRIEF.md`, written into the run folder; printed in `--dry-run`). They are never injected into the image prompt — they're the strategy around the creative.

- `concept` — a short name for the creative ("Third-Coffee Trap", "8 Reasons to Switch"). Defaults to the filename.
- `lever` — the ONE buyer-psychology lever this ad pulls: `problem-aware` · `benefit` · `comparison` · `social-proof` · `ingredient-proof` · `credibility` · `lifestyle` · `brand`. A batch is a **coverage map** of reasons-to-buy and reasons-to-hesitate — tag each ad, then read the spread in the brief (don't over-index one lever or leave an objection unanswered). The brief flags which levers aren't covered.
- `rationale` — a dict that justifies the creative on three lenses, one sentence each: `{"angle": why this message converts, "format": why this layout serves it, "design": why this look stops the scroll}`. This makes "every element is a chosen parameter" explicit, and is the strategic copy the client reads.

Absence is fine (the brief degrades to file + hook). Set them when you want the portfolio view and the deliverable — and treat the `lever` spread as a scoping check alongside Concept divergence.

## Hook rules — the craft

The non-negotiable rules — complete sentence · outcome not ingredient · no jargon · cold-audience-clear · name the referent and the stakes · one distinct outcome per batch · audience-locked ads carry their match · coffee is the villain, never the product noun — trace to **CLAUDE.md → The always-true rules** (the one-line guards); the full hook craft is right here in this skill. Apply them; don't restate them. What this skill adds is how the hook drives the *visual*:
- **Borrow a reference frame the stranger already owns** — pin the unknown product to a known thing (a daily habit, a familiar product, a number read instantly) so it lands in under 2s. Most acquisition hooks, not all — leave room for a pure outcome, a behavior, or provenance.
- **Pattern-interrupt / humor earns the read** — concede the unexpected thing first, then over-deliver.
- **Vivid, specific benefits** — a function translated into a felt, concrete moment, never a category word ("calmer even mid-argument," not "less stress"). This is exactly where the micro-pain's real-voice situation lands.

**Two reusable copy structures (both on-DNA, both proven in the category):**
- **Benefit without the villain** — pair each benefit with the thing it avoids: "Energy without the spike. Focus without the fog. Calm without the pills." The last line carries the anti-stack DNA; the parallel rhythm is built for a benefit `poster`/`editorial`, ideally in the dark register.
- **"N reasons to switch"** — a numbered ingredient/benefit grid ("8 Reasons to Switch") that carries proof density as **designed blocks** (cards on a tinted ground), never a bullet list. Pulls the `ingredient-proof` lever.

## How the hook and visual combine (the handoff)

The winners never say the same thing twice — the hook opens a thought and the visual *finishes* it. Learn the handoff, not the layout:
- **Visual as evidence** — the hook makes a claim; the visual proves it (an accusation hook paid off by a comparison that *shows* the gap).
- **Visual answers the objection the hook raises** — a provocative power claim met by a calm, unjittery scene; the image quietly resolves the "but won't it…?" the hook triggers.
- **Visual closes the hook's open loop** — a hook that concedes "…but" hands the punchline to the image, which delivers the payoff the words set up.
- **One register** — provocative hook ↔ bold, high-contrast layout; quiet provenance hook ↔ atmospheric scene. A mismatch (delicate hook, shouting layout) breaks the spell.

The test: if the hook and the visual are landing the *same* beat, one of them is wasted — make the visual carry what the hook implies but doesn't state.

## The visual must perform the claim — not decorate

The chosen `scene`/`visual_action` (or `visual`/`sides`) should *enact* the argument, product as its resolution — not merely contain it. The reasoning: a comparison *shows* dismissal and elevation; a benefit ad *radiates* outcomes from the product; a provenance ad *embeds* it in its origin. Ask "what is the image *doing* to prove the hook?" If the answer is "the product is in it," the spec isn't ready.

> **All of the above are ways of thinking, NOT a copy bank.** Write a fresh hook and a fresh visual for the batch in front of you. If a draft matches something you remember, that's the signal you stopped thinking — throw it out. Study the proven performers in `assets/brand/refs/` for *why* each works — which frame it borrowed, what its visual proved, how the two hand off — never to reuse a phrase or a layout. The reasoning transfers; the words and compositions don't. (The engine already enforces product-as-hero, proof chips, emphasis, and comparison parity — your job is the idea the hook and visual perform together.)

## Price & product

- Price is corroboration, not the hook — default `price: False`. Set `True` only when price is part of the ad's idea (a value/comparison concept); being structured or a comparison does NOT by itself earn it.
- Product is ≥35% of image height, always the resolution of the concept.

## CTA treatment (`cta_style`) — match the register, vary across a batch

The CTA is a **creative choice**, not a default pill on every ad. (The style names below are the engine's `CTA_STYLES` catalog — `gen.py --policy`; this section is how to *choose* among them.) A Meta square feed ad renders the creative intact, with the platform's own action button shown in the chrome directly *below* the image (the top/bottom UI-overlay only happens on vertical 9:16 Stories/Reels, which we don't run). So the in-image CTA *complements* the platform button below — it never redundantly clones it. Pick the treatment that matches the ad's register, and don't render every ad in a batch with the same one:

- **Loud / direct-response** (`color_block`, `comparison`, `social_proof`, `badge`): `button` / `button_right` (solid, highest-contrast) or `pill` / `pill_right` (brand-gold, restrained).
- **Editorial / atmospheric** (`editorial` scene, premium): `ghost` / `ghost_right` (hollow outline — A/B-tests neck-and-neck with solid, far more premium), `text_link` (underlined + arrow), or `integrated` (woven into the headline lockup).
- **Distinctive / native** when the concept earns it: `tab` (a bookmark anchored to an edge), `sticker` (rotated die-cut), `arrow_down` (the action word plus a bare downward chevron that points at the platform's real button — turns the in-image cue and Meta's button into one gesture).
- **`poster` / `screenshot` / `ugc`**: usually `none` or `integrated` — a floating button breaks a poster's composition and a screenshot's native feel; `ugc` keeps its CTA in the copy only.

The CTA always reads *after* the headline and subhead — never the loudest element — and is never a full-width band (that reads as a flat footer). Treat the CTA as a fourth divergence axis: if every ad in the batch wears the same button, push at least one to a quieter or more distinctive treatment.

## Tea creative claim-guards

Tea carries hard claim-guards: Morning caffeine-free (Cordyceps lift) · Night = parasympathetic, not sedation (never "fall asleep faster") · no mg doses · the Night cup is a natural warm tea, not indigo (`has_cup: True` only when a cup is genuinely in frame; never make cup color the hook) · no specific counts (4.9★ or "thousands") · tea price is $37.40, never $39 · Trifecta is ONE product ("Get the Trifecta", never "try all three"), preserve the gold→sage→lavender gradient.

These — and all product facts (prices, social proof, SKU tables, positioning) — are owned by **CLAUDE.md → Ritual Tea Line** + **tea-product-brief.md** and **enforced by the validator** (a dry-run blocks violations). Write within them; never restate facts in specs.

## Validator guarantees (errors block generation unless --dry-run)

- Unknown `sku` for the product type → hard error (no silent fallback to a wrong SKU).
- `extra_refs` paths that don't exist on disk → error at dry-run, not mid-generation.
- Tea/blend claim guards on rendered text (price anchor, social-proof number, caffeine, sedation, "try all three") — `proof` and `stats` chips included.
- Prescription-drug brand names anywhere in rendered text → hard error; the class term ("GLP-1") is the only sayable reference, as third-person product-fit positioning — second-person status phrasing ("your GLP-1", "are you on") draws a Personal-Attributes warning.
- Emphasis placement, comparison row parity, duplicate files/hooks, audience fit, ugc with a visible in-image CTA (warning), orphan "them/they/those" in in-image text (warning).
- Hook that OPENS with jargon ("adaptogenic", "circadian"…) or an ingredient name (warning) — the mechanical half of the hook gate; the semantic half is the pre-flight below.
- Anti-defaulting (warning): a `format`, `cta_style`, or `archetype` identical across the WHOLE batch reads as defaulted, not chosen — break at least one ad.

## Pre-flight — the outside-in read before you generate or present

The validator is the **mechanical** gate (claim-safe, well-formed). This is the **judgment** gate — run it on every batch after the dry-run, *before* you spend generation budget and *before* you show me anything. Read each creative the way a stranger meets it in the feed, never the way its author would defend it.

1. **Stranger comprehension — the 1-2s test.** Mentally cover everything except the words that render *in the image*. In one read, does a cold stranger know **what this is** and **why it matters to them**? If it only lands once you add the scene note, the rationale, or prior Alcami knowledge, the hook (or the category cue) is failing — not the viewer.
2. **Run each hook through the full 7-point gate (CLAUDE.md).** The validator catches four points mechanically (fragment · jargon/ingredient opener · orphan pronoun · duplicate). You judge the three it can't: **outcome, not an ingredient/claim** · **names the stakes, not just the joke** (what changes in their life, not a clever setup) · **an audience-locked ad carries its match** in the frame or the copy (the landing page is generic, so the ad alone makes the targeting land).
3. **Does the visual *perform* the claim?** "The product is in it" is a fail — the image must enact the argument and resolve on the product (≥35%, the answer). The hook and the visual must land *different* beats; if they say the same thing, one is wasted.
4. **Anti-defaulting — variety is first-class.** Across the batch, is each of format · CTA · archetype · register genuinely *chosen* and varied? The validator flags an element identical across the whole batch; you catch the near-uniform case (7 of 8 the same is still defaulting).
5. **Brief honesty — no hype.** Read `BRIEF.md` as the client will. Each creative must justify itself on all three lenses (angle / format / design) in plain, true sentences — not self-congratulation; and the `lever` spread must be a real coverage map (distinct reasons-to-buy and objections answered), not three ads pulling one lever. If a rationale can't be written honestly, the creative isn't ready.

Only after this read do you present — and when something is weak, say so plainly with the fix. Never sell a batch; the review is an asset, not a pitch.

**Recurring failure patterns — catch these specifically (all observed in shipped batches):**
- **Visual contradicts the copy.** An anti-coffee ad whose hero is a creamy mug indistinguishable from a café latte undercuts "didn't need coffee." If the product photographs *as the villain*, change the framing (show the pouch/ritual, not a coffee-look-alike cup).
- **Constructed parallelism loses to lifted voice.** "Bad sleep. More coffee. Worse sleep." is copywriter rhythm, not a line lifted from a real thread. The validator nudges 3-fragment parallelism; you judge the subtler cases. Keep the connector ("…but already foggy by 11?").
- **Ingredient / solution as the hook.** "Nine adaptogens. One scoop." leads with what's *in* it, not the *problem*. The validator flags ingredient openers; you catch claim-led hooks that skip the one-beat problem.
- **One insight in many fonts.** The campaign-level version of defaulting: 13 ads that all say "coffee sabotages you, Alcami is the caffeine-free swap" are one insight in many formats, not a portfolio. Each ad needs a distinct *situation/insight*, not just a distinct layout.
- **Scene & motif déjà vu.** "Person pushes a coffee cup aside" three times, or bodiless forearms reaching into frame on every scene, is repetition the `lever` spread won't catch. Vary the moment, not just the format.
- **Expression must match the caption.** A flat or faintly-annoyed face under a line about relief ("clearest morning") reads false. The UGC directive enforces it; verify the rendered face actually carries the emotion.
- **Number-vs-shown & gold-on-villain.** "Nine" claimed but four shown; the gold focal word landing on "foggy/crash" instead of the outcome. The validator nudges both — don't wave them off.

## After generation

Review each image against its hook — and against the same outside-in read above (a generated image is the asset the stranger actually meets). If it doesn't deliver, revise the **spec** (not a raw prompt) and regenerate with `--only NN`.
