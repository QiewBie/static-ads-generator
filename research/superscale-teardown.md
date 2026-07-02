# Superscale AI — pipeline teardown (reference)

Reverse-engineered from generated Alcami creatives + the product UI (`research/superscale-examples/`). The point: understand their **strategic packaging**, which is their real edge — not their image fidelity (that has the same flash-gen limits we do).

## What Superscale outputs

From ONE product input it produces a **structured portfolio of N named creative concepts** (7 for Alcami), presented as:
- a **table** — `# · Creative Name · Format/Angle` (the concept menu), and
- per-creative **cards**, each with an expandable **Creative Rationale**.

It is not "make 7 variations." It's a deliberate spread across **buyer-psychology levers**, each concept a different lever.

## The 7-concept portfolio (the coverage matrix)

| # | Creative | Format / Angle | Buyer-psych lever it pulls |
|---|---|---|---|
| 1 | Hero Ritual Clean | Premium hero, "Your Morning. Reimagined." | brand / aspiration |
| 2 | 8 Mushrooms Grid | Ingredient call-out grid, deep green, "8 Reasons to Switch" | transparency / education / proof density |
| 3 | Coffee vs Alcami Split | Side-by-side comparison, coffee problems vs benefits | objection handling (cortisol/crash) |
| 4 | 4.9 Stars Social Proof | Star rating + testimonial card + 90-day CTA | risk aversion / first-time-buyer trust |
| 5 | Morning Ritual Lifestyle | Golden-hour flat-lay | identity / aspiration |
| 6 | Bold Benefit Statement | Oversized dark type — Energy / Focus / Calm | benefit clarity |
| 7 | Trust Badges Credibility | Clean white, Non-GMO / Lab Tested / 90-day badges | credibility |

The lesson: variety is organized by **what objection/desire each ad answers**, not by format for its own sake. A batch is a *coverage map* of the buyer's reasons to buy and reasons to hesitate.

## The 3-part Creative Rationale (their core mechanic)

Every creative carries ~3 rationale bullets, each a **different strategic lens**, all grounded in category (supplement) conversion principles:

1. **Angle / buyer-psychology** — *why this message converts.* e.g. "Social proof is #1 converting element for supplements"; "Cortisol spike objection"; "Ingredient transparency = top trust factor for purchase."
2. **Format / layout logic** — *why this layout serves the angle.* e.g. "Grid format = high proof density"; "Split format maximizes the comparison"; "Listing all 8 mushrooms with specific benefits directly addresses 'what's actually in this'."
3. **Design / feed-standout logic** — *why this look wins in-feed.* e.g. "Deep green/dark earthy backgrounds create strong thumb-stopping contrast in the typical Meta feed while staying on-brand"; "Cream/editorial aesthetic"; "Dark contrast stands out."

Verbatim sample (the testimonial card's rationale tooltip): *"Star ratings + testimonials are the highest-converting ad elements for health supplements. The 4.9 star figure combined with a specific user story (coffee replacement narrative) directly addresses risk aversion in first-time buyers."*

So each creative is justified on three axes — **message, structure, and standout** — tied to a named buyer state.

## Design craft observed (the three finished pieces)

- **Two background registers, alternated for feed variety:** *dark/deep* (near-black; deep forest green) for thumb-stopping premium, and *light/cream* for clean trust. We skew almost entirely warm/cream/light — the dark register is a gap in our range.
- **Big high-contrast editorial serif** (Didot/Bodoni) as the dominant voice.
- **Mixed-weights** — a huge serif benefit word beside a small sans qualifier ("ENERGY | without the spike").
- **Parallel copy structures** that fit our DNA: "Energy / Focus / Calm — without the spike / fog / pills" (benefit-paired-with-villain), "8 Reasons to Switch."
- **Designed info blocks** — the ingredient grid is cards on a tinted ground, never a bullet list.
- **Testimonial card** with a concrete, specific story ("I used to need 3 coffees… I don't crash by 2pm").
- **Risk-reversal CTA** — "Try Risk-Free — 90-Day Guarantee."
- **Strict hierarchy + generous negative space** on every piece; the pouch is the one warm/lit object.

## Their weaknesses (honest — their image-gen is no better than ours)

- **Same fine-text garbling:** the ingredient grid misspells ingredients ("Astragalus"→"Astiniralus", "Dottry Resilience"). Identical to our flash pouch-label garble — proof it's a model limit, not a us-problem.
- **Loose claims:** "from 2,000+ verified customers" (Alcami's real figure is 200,000+); "8 Reasons to Switch" then shows 9 cards. Their pipeline doesn't enforce claim accuracy.
- **Generic grounding:** rationales lean on generic "supplement best-practice," not mined real-audience voice.
- **The ingredient grid isn't just garbled — it's factually wrong, and the error compounds from the
  concept name down.** Checked directly against our real roster (`ingredients.md`: 3 mushrooms —
  Lion's Mane, Cordyceps, Reishi — + 6 botanicals — Polygala, Astragalus, He Shou Wu, Shilajit,
  Gynostemma, Mucuna): the concept is named **"8 Mushrooms Grid"** in their own coverage table, but
  Alcami has 3 mushrooms, not 8, and most of "the nine" are botanicals, not mushrooms — the concept's
  *name* is wrong before a single card renders. The rendered grid then shows **"Chaga"** — a mushroom
  **not in Alcami's real formula at all** — while **He Shou Wu and Mucuna, which ARE real
  ingredients, never appear.** And one card ("Astinrralus — Dottry Resilience") is a garbled
  *duplicate* of the Astragalus card that appears two cells later ("Astragalus — Daily Resilience"),
  not a different ingredient. So the grid invents one ingredient, drops two real ones, and duplicates
  a third — a factual-accuracy failure, not a spelling one. **This is the gap our own validator
  exists to close** — `pb_validate.py` rejects invented ingredient text and enforces the real roster;
  Superscale's pipeline has no equivalent, because the LLM writing the grid content apparently isn't
  grounded against a validated ingredient list — it pattern-matched to "mushroom-coffee brand → big
  ingredient grid" rather than checking what's actually in the product. Worth knowing as a strength of
  our own foundation, not just a competitor critique.
- **The pouch hero render itself, by contrast, is faithful across all three example ads** — same
  exact tagline ("ACHIEVE YOUR HIGHEST SELF"), same exact product line ("CREAMY SUPERFOOD BLEND WITH
  ADAPTOGENIC MUSHROOMS"), same gold/cream identity, unchanged every time (verified by direct
  comparison against our real asset, `assets/brand/product_images_blend/original frontBIL2 .png`).
  **The error pattern is concentrated in the custom, novel graphic (the ingredient grid) — not in the
  reused product asset.** That's a meaningful, more precise read than "their image-gen is no better
  than ours": whatever keeps the product render consistent across creatives (a locked reference image,
  a fixed brand asset, or just a heavily-conditioned regeneration) is working; what's ungrounded is any
  *novel* text content an LLM has to generate fresh per ad, because nothing checks it against a real
  source of truth. That's exactly the lesson for our own compositing plan below: pasting a real pixel
  layer solves *rendering* fidelity, but the *content* of any generated/typeset text still needs to
  come from a validated list (ours already does, via the batch specs) — compositing alone wouldn't
  have caught Chaga; a validated ingredient source is what catches it.

## Us vs. them — where each wins

| Dimension | Superscale | Us |
|---|---|---|
| Concept packaging | **Named portfolio + 3-part rationale, client-facing** | internal `#` dev comments only |
| Background range | **dark + light, alternated** | warm/cream/light only (gap) |
| Copy structures | "benefit without villain", "N reasons" formalized | hooks, not formalized as structures |
| Claim accuracy | loose (invented numbers, count slip) | **validator enforces real numbers/claims** |
| Audience grounding | generic supplement principles | **real-voice mining (research skill)** |
| Image text fidelity | garbled (same as us) | garbled (same) — both flash-limited |

**Their edge is strategic packaging; ours is rigor (accurate claims + real-voice specificity).** The win is to bolt their packaging onto our foundation.

## Adoption candidates (proposals — not yet built)

1. **A per-creative `rationale` layer** — for each spec, capture the 3 lenses (angle / format / design), each one sentence. Forces every creative to justify itself on message+structure+standout (makes our "every element is a chosen parameter" rule explicit), and doubles as a **client-facing campaign brief** generated per batch.
2. **Portfolio-coverage framing** — when scoping a batch, spread deliberately across buyer-psych levers (brand · ingredient-proof · comparison/objection · social-proof · lifestyle · benefit · credibility), then pick the formats — a coverage check, not format-roulette.
3. **A dark-premium editorial register** — add a deep/dark `color_world` + the ENERGY/FOCUS/CALM template (dark ground, big serif, mixed-weights, "benefit without villain", pouch as the one warm object) to break our warm/light monotony.
4. **Reusable copy structures** — "benefit without the villain" and "N reasons to switch," both on-DNA (anti-stack, no-crash).
5. **Compositing real assets instead of generating everything as pixels** — see the architecture
   addendum below. The single highest-leverage idea found since the original teardown.

## Architecture deep-dive — critically filtered (external research, addendum)

A longer piece of external research reconstructed Superscale's likely internal architecture (brand-
context retrieval → an LLM "art director" pass that writes a structured creative spec → a hybrid
renderer → validators). It's honest about its own limits — it labels claims confirmed (stated by
Superscale or seen by an independent tester) vs. reconstructed (inferred from how the category
provably works) vs. unknown, and it does NOT claim to have Superscale's actual system prompt or
validator code. That honesty is correct to preserve: **the actionable value here isn't "Superscale's
exact prompt" (unknowable) — it's a few documented industry patterns worth checking against what we
already do.** Filtering signal vs. noise:

**Already true for us — not new, just independent confirmation:**
- Brand-context retrieval feeding every generation → that's CLAUDE.md + the skill's `reference/`
  files + `competitors.py`. We have this.
- A structured per-creative rationale → already adoption candidate #1 above, proposed before this
  text arrived.
- A pre-flight "AI-tells" checklist (misspelled brand name, garbled text, wrong SKU) → this is
  `evaluate.py`'s grader, already built and already stricter than what's described (ours now also
  catches hierarchy/proof-orphaning/comprehension, which the described checklist doesn't mention).

**Not applicable yet — correctly out of scope:**
- A performance-validator loop (winners feed the next brief, conditioned on real Meta spend data) —
  we have no live spend data to condition on. Worth designing for once real campaigns run, not now.
- The specific reconstructed system-prompt skeleton and "which foundation model is the art director"
  — speculative by the source's own admission; nothing to act on.

**Genuinely new and the one worth building — the compositing architecture:**
The category-wide best practice the piece describes: generate ONLY the forgiving, high-variance part
(the background/scene) with the image model; composite the brand-critical, error-prone parts — the
real logo, the real product photography, the headline text — as deterministic layers on top, typeset
or pasted, never re-generated as pixels. This is why a Superscale-class static doesn't garble a brand
name or distort a pouch label: that text was never asked of the image model in the first place.

**Why this is real for us, not aspirational:** confirmed by grepping our own code — `Image.open` in
`gen.py` is the ONLY Pillow operation in the entire pipeline (the PNG re-encode); there is zero
compositing today. Every pixel — background, pouch render, headline, trust badges — comes out of one
Gemini call. That's the direct cause of two recurring failure classes already on record: garbled
pouch fine-print (the `legible` grader failures, e.g. `02_third_coffee_betrays.png` in the 3pm-crash
batch) and invented/garbled label text (`pb_validate.py`'s `no_invented_text` guard exists *because*
the model invents text when asked to render it as pixels). We already have the raw materials a
compositing pipeline needs without any new references: real pouch cutout PNGs
(`assets/brand/product_images_blend/`), Pillow already imported, and `gen.py` already does
post-processing per generated file. The shift would be: Gemini generates the scene/background only;
Pillow pastes the real pouch PNG and typesets the real headline/proof text on top. This is a genuine
architecture change (more code, a font/typesetting decision, a new failure mode to test — text
overlay placement) — not a prompt tweak — so it deserves its own scoped pass, not a drive-by edit.

**Feasibility, checked directly rather than assumed:**
- `gen.py` already sends the real pouch PNG into the Gemini call as an `inlineData` image part
  alongside the text prompt — so today's pipeline is **reference-conditioned regeneration**, not
  zero asset-grounding. The model is asked to *repaint* the pouch using the real image as a guide,
  which is why our pouch likeness is usually decent but can still garble fine print (it's a repaint,
  not a copy). True compositing (`Pillow.paste`) would make that specific layer un-garblable, because
  a pasted pixel is never re-rendered.
- The real pouch asset (`original frontBIL2 .png`) is **RGBA, 3851×4814** — already has an alpha
  channel and is high-resolution, so it's paste-ready with no preprocessing.
- Every `TYPE_PERSONALITIES` entry already names a real typeface family in its description, and the
  literal files exist as **macOS system fonts already on this machine**: `condensed_bold` →
  `Impact.ttf` / `DIN Condensed Bold.ttf`; `editorial_serif` → `Didot.ttc` / `Bodoni 72.ttc`;
  `light_serif_italic` → `Georgia Italic.ttf` / `Times New Roman Italic.ttf`. No font sourcing or
  licensing work needed for a first prototype — the prose descriptions and the real fonts already
  match by name.
