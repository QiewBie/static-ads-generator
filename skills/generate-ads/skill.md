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

**Two authorities — don't restate their rules in specs or here:**
- `prompt_builder.py` — formats, design archetypes, audience policy, all hard rules. Live matrix: `python3 gen.py --policy`
- `CLAUDE.md` — brand, product facts, voice, ICP. (Tea deep-dive: `tea-product-brief.md`.)

## Workflow

1. **Research** (if needed) — pick the right tool (table below). Never WebFetch/WebSearch.
2. **Diverge** — before writing any spec, sketch 2–3 genuinely different concepts per ad slot and pick the strongest. Never commit the first safe idea. See "Concept divergence" below.
3. **Write specs** — each ad is one dict in a campaign. Start from `batches/_template.py`.
4. **Dry run** — `python3 gen.py batches/<file>.py --campaign <name> --dry-run`. The validator prints errors (block generation) and warnings (fix if real).
5. **Review** the assembled prompts.
6. **Generate** — drop `--dry-run` (`--force` overwrites; `--only NN` re-runs one ad). The default model is **flash** (draft tier, ≈3.5x cheaper all-in); regenerate client-picked winners at final quality with `--model pro`. `--batch` runs the job through the Batch API at 50% price (async, minutes-to-hours; `--batch-fetch` collects an interrupted job).
7. **Deliverables** — images land in `ad-workspace/[RUN_ID]/`.

## Research tooling — which tool for which task

Three APIs in `.env`. Match the task to the tool; never WebFetch/WebSearch. Scrape Creators is **metered (credits)** — spend it only on what *only it* can do (real artifacts), and let Tavily (cheap, synthesized) carry everything factual.

| Task | Tool | Why |
|---|---|---|
| What a rival is **actually running** — live ad copy, headlines, CTAs, offers, which faces, active-ad counts | **Scrape Creators** → `GET /v1/facebook/adLibrary/search/companies?query=` (get `page_id`) then `/v1/facebook/adLibrary/company/ads?pageId=&country=US&trim=true` | Pulls the real Meta Ad Library creative; nothing else can |
| Real creator / UGC reference — how people actually shoot & caption (for `ugc` cuts) | **Scrape Creators** (IG/TikTok/YouTube profiles, posts, transcripts, comments) | Real social artifacts, not descriptions |
| Pricing, certifications, ingredients, specs | **Tavily** | Verifiable facts, synthesized answer + sources |
| Audience pain points, sentiment, reviews, "is X taste/claim true" | **Tavily** | Web sentiment + fact-check, no credits burned |
| Category trends, positioning gaps, news | **Tavily** | Broad web with `include_answer` |
| "What can tool/brand X do" capability research | **Tavily** | Broad web synthesis |
| Generate the ad image | **Gemini** via `gen.py` | The render step |
| Spec → prompt assembly, claim guards, validation, divergence | **local pipeline** (`prompt_builder.py` / `gen.py --policy`) | No API needed — don't research what the engine already owns |

**Efficiency rule:** if Tavily can answer it (a price, a fact, a sentiment), use Tavily. Reserve Scrape Creators for the *actual creative/artifacts*. Read keys from `.env`; save competitor analyses to `research/`.

**Calling conventions:**
- **These APIs are called with `curl`, not Python `urllib`.** `curl` uses the system cert store; Python's `urllib` raises `CERTIFICATE_VERIFY_FAILED` here. Read keys from `.env`, then `curl -s -H "x-api-key: $KEY" …` (Scrape Creators) and `curl -s -X POST -d '{…}'` (Tavily).
- **Scrape Creators company search matches broadly** — `search/companies?query=AG1` also returns people/shows with "AG". Query the **full brand name** ("Athletic Greens", "IM8 Health") and pick by `category` + `likes` for the right `page_id`.
- **Ads come from `/company/ads`** (with `pageId`); `/adLibrary/ads` is not a valid path.
- **Credits are metered.** Each Scrape Creators response carries `credits_remaining`; an exhausted key returns HTTP 402. Top up the key in `.env` when that happens.
- **Tavily's synthesized `answer` is sometimes content-filtered/blank** — read the `results[]` array, don't depend on `answer`.

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
`audience` ("acquisition" default / "retarget") is set on the **campaign**; ads inherit it. Full field reference: `batches/_template.py`.

## The structured text layer (use this — it carries the MESSAGE, not just a mood)

Every format **except `ugc`** renders this structured text block (`ugc` stays deliberately undesigned — its only text is `hook` + an optional `text_in_image` caption; the validator warns if you set the fields below on a `ugc` ad). Default to giving an ad enough to be understood, not just felt:

**UGC still has to sell.** Super-native with nothing explained = weak: the caption carries an outcome (not just a vibe), the pouch is unmistakably in use with the label readable, and the primary text explains what the product is. When the explanation must live *in the image*, use a phone-look `scene` (editorial archetype, phone camera/lighting overrides) instead of `ugc` — it keeps the casual feel and can carry a designed line.

- `headline` — the message, rendered dominant (largest, reads first). Falls back to `hook` if omitted.
- `subhead` — the clarifier / category line / second idea (~55% of headline). Add when the viewer needs more than the headline.
- `stats` / `proof` — aliases for the same proof chips (either name works in any rendering format): up to 3, each its own chip. Keep them product-correct: blend → `["200,000+ customers", "NSF Certified", "90-day guarantee"]`; tea → `["4.9 stars", "USDA Organic", "100% fruit-body"]`. Never cross them — "200,000+" and NSF are blend-only (the validator hard-errors on "200,000+" in tea text).
- `emphasis` — per-word typography: a dict of `{"phrase": "treatment"}`. Treatments: `bold` · `italic` · `underline` · `strike` (negates — great for comparison "before" rows) · `gold` (brand accent) · `boxed` (own background chip).
  - The validator **enforces placement**: a phrase not in the headline/subhead is a hard **error**; a stopword ("the") or a phrase appearing twice is a **warning**. Emphasis always lands on a real, meaningful word.

**Register — pick one deliberately, don't default to safe.** Two legitimate modes:
- **Explanatory** (the default) — the product **category** ("Adaptogenic Mushroom Tea" / "Superfood Mushroom Latte") is forced legible so a stranger instantly knows what it is.
- **Associative / mood-led** — set `"associative": True` to suppress the forced category so the ad can lead with feeling and intrigue (the "From the forest" winner is this mode). This is a **first-class choice** for the right concept, not a fallback — reach for it when the image earns recognition rather than explanation. Override category wording with `category_cue`.

When the ad needs information (pain points, bullets, a testimonial), use the body fields for that format — `items` (blocks), `sides` (comparison), `steps` (how_it_works) — alongside headline/subhead. Match the amount of text to the format.

## Clean copy/layout path for blocks

`blocks` accepts two shapes through **one** builder. PREFERRED: `headline` + `items` ([{label,note}]) + `proof`. LEGACY: a `blocks` list of `{size,content}` (still works, the validator nudges you toward `items`). The engine designs items as objects, never a bulleted list. Reference the hook anywhere with the `{hook}` token.

## Formats & archetypes

Formats: `scene` · `comparison` · `blocks` · `ugc` · `how_it_works`.
Design archetypes (the graphic layer): `editorial` · `spec_card` · `annotated` · `color_block` · `badge` · `ugc_minimal` · `testimonial` · `social_proof` · `poster` · `screenshot` · `before_after`. If you omit `archetype`, the engine applies a sensible per-format default (the validator tells you which) — but set it explicitly for intended variety. Run `python3 gen.py --policy` for descriptions and audience fit.

**Bold/DR devices — use them; the brand's top performers are loud:**
- `poster` — an oversized number/word/statement IS the composition (200,000. / 10:1.).
- `screenshot` — a native IG/FB comment, review card, or text exchange; cold-traffic authenticity.
- `before_after` — two honest states; the change is the whole point.
- `stamp` (a field, not an archetype) — a bold corner stamp like `"RESTOCK"` / `"NEW"` / `"BESTSELLER"`. Opt-in, and use ONLY for a literally true state — never manufacture scarcity (the validator warns).

**Naming a rival in creative:** allowed for *brands* (never people). Show the competitor by pouch/form factor + brand name in text, never a distorted logo; keep every comparative claim true, parallel, and substantiated; and treat the rival as a creative *parameter* — it can anchor a `scene`, `poster`, or `before_after`, not just the two-column `comparison`. Full stance + the `assets/competitors_assets/` files (AG1, IM8): **CLAUDE.md → Competitors**. The validator warns whenever a rival is named.

## Photographic variety (you don't need to set this, but you can)

Each SKU has a `mood`; the engine rotates camera + lighting per ad (seeded by filename — stable re-runs, but different files look different). Override per spec with `camera` and/or `lighting` when a shot needs a specific look. Color worlds are tonal anchors, not single-hue washes — real rooms, natural materials.

## Audience fit (enforced by the validator)

- **Acquisition (cold):** any format/archetype — incl. `ugc`, `testimonial`, `social_proof`, and the bold devices (`poster`, `screenshot`, `before_after`, `comparison`, the `stamp` field). Cold traffic rewards clarity and boldness; the brand's proven winners are loud. **Tea cold acquisition:** the quiet editorial register is the *default*, not a requirement — loud comparison/poster/bold-hook cuts are allowed and worth testing against the quiet one (don't lock cold tea into a whisper).
- **Retarget (warm — already bought):** this is a **product LAUNCH to existing customers**, not an education campaign. Lead with the *news*, not proof. Core angles: "we made tea now!" · "loved the blend? try this" · a **two-product display** (blend + tea in one frame) · insider/early-access · "one of the first mushroom teas." `blocks`/`how_it_works` are the FOLLOW-UP for people who want detail. The validator **warns** on `comparison` (launch register is news, not an argument), `ugc`, `testimonial`, `social_proof` — warm buyers don't need convincing. Every retarget ad must carry a launch signal (Alcami / blend / new / first / now — the validator warns if none is present). Extend the relationship, never gap-fill ("what your ritual is missing" implies the blend is incomplete — it isn't). Keep early-access date-free in the image (no "Pre-Order", no ship dates).

## Concept divergence (before specs)

For each ad slot, rough out **2–3 distinct concepts** before committing to a spec. A concept = a hook + the device that performs it. Force them apart on three axes so you're *choosing*, not settling:

- **Reference frame** — coffee · a nightcap / melatonin · a competitor · a number · provenance · a behavior. (Most cold hooks borrow one — vary which.)
- **Device / archetype** — `comparison` · `poster` · `scene` · `screenshot` · `before_after` · `how_it_works` · `ugc`. (Don't render every idea as the same scene.)
- **Emotion** — relief · attunement · pride · curiosity · belonging · skeptic-flipped.

Then pick the concept whose hook→visual handoff is sharpest (see "How the hook and visual combine"). **Across a batch: no two ads may repeat the same frame + device + emotion triple** — if two land the same beat, cut one and diverge again. Gut check: if every concept you wrote is a quiet scene, you stopped early — push at least one loud (`poster`/`comparison`/`stamp`) and one mood-led (`associative`) into the mix before deciding.

## Hook rules (non-negotiable)

- One complete sentence a cold stranger understands. Outcome/feeling, not an ingredient.
- Short for minimal scenes; no jargon ("circadian", "adaptogenic") on the hook itself.
- One distinct human outcome per hook — no two ads in a batch repeat the same feeling.
- **Borrow a reference frame the stranger already owns** — the move is to pin the unknown product to a known thing (a daily habit, a familiar product, a number read instantly) so it lands in under 2s. Use on *most* acquisition hooks, not all — leave room for a pure outcome, a behavior, or provenance.
- **Pattern-interrupt / humor** earns the read: concede the unexpected thing first, then over-deliver.
- **Vivid, specific benefits** — a function translated into a felt, concrete moment, never a category word ("calmer even mid-argument," not "less stress").
- **Name the stakes, not just the joke** — a possessive line or a native vibe alone undersells; the in-image copy says what changes in their life ("keeps me afloat," "happy mom again," "got me through 5pm").
- **Audience-locked batches carry their match in the ad** — the target (parents, the GLP-1 routine) is visible in the frame or named in the copy; the landing page is generic, so the ad alone carries the match. Coffee is the villain, never the product noun (CLAUDE.md → "Coffee is the villain, never the product").

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

The CTA is a **creative choice**, not a default pill on every ad. A Meta square feed ad renders the creative intact, with the platform's own action button shown in the chrome directly *below* the image (the top/bottom UI-overlay only happens on vertical 9:16 Stories/Reels, which we don't run). So the in-image CTA *complements* the platform button below — it never redundantly clones it. Pick the treatment that matches the ad's register, and don't render every ad in a batch with the same one:

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

## After generation

Review each image against its hook. If it doesn't deliver, revise the **spec** (not a raw prompt) and regenerate with `--only NN`.
