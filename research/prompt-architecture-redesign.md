# Prompt-architecture redesign — the plan

A phased plan to lift two ceilings in the ad engine: **creativity** (every ad looks like the
same wellness photo) and **reliability** (the model garbles labels and exact text). This file
is the canonical roadmap — goal, status, and remaining work for every phase. Status markers:
**DONE** (shipped, `make check` green) · **NEXT** (the next phase to build) · **LATER** (planned).

## Status at a glance

| Phase | What it does | Status |
|---|---|---|
| 0 — Prompt hardening | Fix the shipped defects the failed gut batch exposed | **DONE — validated** (rerolled 01/02 pass the grader; the double-print class is gone) |
| 1 — `art_style` axis | Add the artistic-medium axis (photo / illustrated / graphic / riso) | **DONE** (composited variant proven by the 03 graphic proto; direct-path demo batch still open) |
| 2 — Compositing | Paste the real pouch + typeset copy in code, generate background only | **PROTOTYPE DONE** (`composite.py`, 3/3 pass the grader) — main-path wiring is NEXT |
| 3 — Analytics loop | Feed live ad performance back into the next batch's brief | **LATER** |

## The diagnosis (why any of this)

The engine is a **"photograph-the-product + overlay-the-text" machine.** One architecture
produces two symptoms:

- **Creativity cap.** "Artistic style" was never a parameter — photography is welded into every
  builder's opening line and the CAMERA/LIGHTING blocks. Of the six artistic-style families a
  modern image model can render, the engine used exactly one. Result: hands, interiors, people —
  no range.
- **Reliability cap.** In the same architecture the model must render two deterministic things it
  is bad at — the exact pouch label and every exact word of copy. The `gut_relief_v1` batch failed
  all five ads on this class: duplicate category cue (01/02), ungrouped trust marks (03), dropped
  headline words + illegible fine print (04), duplicate comparison row + a co-equal competitor (05).

These are not two problems. They are one architecture seen twice. The cure is to **split the
deterministic layer (pouch + text) from the generative layer (background/scene)** — which is
Phase 2. Phases 0 and 1 harden and widen the generative path in the meantime; Phase 2 is the
keystone that makes creative range *safe* and kills the text/label defects outright.

## Research basis (compressed)

- **D-Libro (AI-image course)** — the structural keystone. Every image prompt is one of **4
  approaches** (subject / scene / **design** / **abstract**) built from **6 prompt elements**, one
  of which is **artistic style**, spanning **6 style families** (photography · traditional art ·
  digital/3D · graphic design · fine-art/experimental · cultural-historical). Two modes: descriptive
  (over-specify) vs inspirational (set a mood, let the model imagine). Also, independently: "plan on
  editing or replacing text manually afterward" → validates compositing.
- **AdensLab + Meta Andromeda** — the algorithm now matches creative-to-person, so **creative
  diversity is the performance lever**, not a vanity metric ("volume beats perfection").
- **Superscale** — AI is a **volume engine; the human supplies the concept/point-of-view.**
  Successful pipelines have four pillars: brand-voice card · per-brief falsifiable hypothesis ·
  promise-accuracy review · weekly analytics loop. We have three (CLAUDE.md · the lever taxonomy ·
  the validator); the analytics loop is Phase 3.

### Sources — where to read them

| Source | What it gave us | Read it |
|---|---|---|
| D-Libro — *Anatomy of AI Prompts* | the keystone: 4 approaches / 6 prompt elements / 6 style families | https://d-libro.com/topic/anatomy-of-ai-prompts/ |
| AdensLab — *Scroll-stopping static ads* | diversity-as-performance, the 3×3 method, Meta Andromeda | https://www.adenslab.com/blog/scroll-stopping-static-ads-copy-paste-prompts |
| Superscale — *Ad Creative Automation* | the volume-engine / human-concept thesis + the four pillars | https://superscale.ai/learn/ad-creative-automation/ |
| AI World Today — *Prompt Engineering for AI Artists* | supplementary prompt-anatomy cross-check | https://www.aiworldtoday.net/p/prompt-engineering-guide-ai-artists |

Local scraped copies are in `.firecrawl/` (`src-dlibro.md`, `src-adenslab.md`, `src-superscale.md`,
`src-aiworld.md`) — **gitignored scratch, so treat the URLs above as the durable pointer.** Pulled
via the firecrawl-search skill; search queries: `r1-prompt-structure` · `r2-creative-variety` ·
`r3-ai-ad-tools` (result sets in `.firecrawl/r1..r3-*.json`).

---

## Phase 0 — Prompt hardening — **DONE**

**Goal:** fix the concrete defects the `gut_relief_v1` batch exposed, cheaply, without an
architecture change — so the model-rendered path is as clean as it can be before compositing.

**What exists now (the six changes):**
1. **CUP line** ([`prompt_builder.py` `_night_cup_line`](../prompt_builder.py)) no longer contains
   the label-like phrase "creamy superfood latte" and explicitly forbids printing text near the cup.
   Fixes the 01/02 duplicate "Superfood Mushroom Latte" (a second source collided with the category
   cue) and removes a latent CLAUDE.md violation (latte as the product noun; it belongs only in the
   category cue).
2. **UGC `capture_mode`** — a rotated catalog (`arms_length` · `pov_handheld` · `propped_phone` ·
   `friend_candid` · `mirror`) replaces the hardcoded forced arm's-length selfie, which was the tell
   that manufactured the "fake UGC" look. A spec may pin one; otherwise it rotates by filename.
3. **UGC defaults `cta_style="none"`** — the UGC hard rules ban an in-image action button, but the
   engine used to inject one anyway (default `"button"`). Now the medium and the rule agree.
4. **Grader** ([`evaluate.py` `_grade_prompt`](../evaluate.py)) reads `text_in_image` for UGC, not
   `hook` — UGC renders the native caption, so grading against the longer hook produced false
   "missing words" faults (04).
5. **Validator** ([`pb_validate.py`](../pb_validate.py)) gained `capture_mode` sanity + a
   **framing-contradiction guard**: it flags a UGC spec whose `person`/`moment`/`environment` prose
   dictates the camera framing (selfie / arm's length / front-facing) while no `capture_mode` is
   pinned — because the rotation would then contradict the prose. (Surfaces 5 shipped UGC ads for
   cleanup when next touched, without changing them.)
6. **`gut_relief_v1` ad 04** ([`batches/blend.py`](../batches/blend.py)) pins
   `capture_mode="propped_phone"` and rewrites `moment` to describe the moment, not the capture —
   so the fix actually lands on the one UGC ad in that batch.

**What Phase 0 fixes:** 01/02 double-print, 04's capture/CTA/grader faults.
**What it deliberately does *not* fix:** 03 (ungrouped trust marks) and 05 (duplicate row, co-equal
competitor) — those are the deterministic-layout class that only **Phase 2 (compositing)** cures.

**Validated on a reroll** (`gut_relief_v1` 01/02/05, Batch API, flash): 01 and 02 pass the grader —
the duplicate category-descriptor print is gone. 05 fails exactly on the deterministic class (a
garbled rendered word "flated", a trust mark on the rival's column) — the residue Phase 2 removes.

**Remaining under Phase 0:** none. (The 5 flagged legacy UGC specs are optional cleanup, surfaced by
the validator; they are not blocking.)

---

## Phase 1 — The `art_style` axis — **DONE**

**Goal:** make artistic style a first-class parameter — the direct answer to "too narrow in
creativity." Add the missing prompt element and the missing style families, curated to stay on-brand.

**The field:** `art_style` (not `style` — that name is taken by the `blocks` sub-layout). Defaults
to `photographic`, so every existing ad is **byte-identical** and golden does not churn; only ads
that opt in diverge. The "4 approaches" are not a separate field: subject / scene / design are
already covered by `format` + `archetype`; the missing **abstract** approach is realized through a
style (`surreal_conceptual`, in the Bold tier — deferred).

**The curated palette (MODERATE tier, chosen):**
| art_style | Medium | Brand fit |
|---|---|---|
| `photographic` | real photography (default, unchanged) | the existing path |
| `editorial_graphic` | flat premium print — color fields, vector shapes, museum-poster restraint | "premium but accessible" |
| `illustrated` | crafted editorial / botanical illustration, never cartoonish | echoes the pouch's own botanical mushroom engraving; "ancient wisdom" |
| `risograph` | limited-palette screenprint grain | premium-indie, tactile |

**The mechanism** (all in [`prompt_builder.py`](../prompt_builder.py), `ART_STYLES` + the helpers
`_art_style` / `_is_photographic` / `_persona` / `_art_style_line`): a non-photographic style (1)
swaps the opening persona (illustrator / graphic designer / riso artist, not photographer), (2)
withholds CAMERA/LIGHTING (a lens contradicts an illustration — same mechanism posters use), (3)
injects an `ART STYLE —` directive block, and (4) routes the product through the **SUPPORT** rule so
the concept can breathe while the pouch stays recognizable. Applies to `scene` / `comparison` /
`blocks` / `how_it_works`; `ugc` is inherently phone-photographic and ignores it.

**Wiring (discoverability + guards):**
- [`pb_validate.py`](../pb_validate.py): `art_style` value sanity, a warning when set on `ugc`, and
  the assembled-prompt lint extended so a non-photographic art_style can never carry CAMERA/LIGHTING.
- [`gen.py --policy`](../gen.py): lists the art styles in the live matrix.
- [`gen.py` `build_brief`](../gen.py): the BRIEF reports **medium spread** — an all-photographic
  batch is flagged as the defaulting it is.
- [`batches/_template.py`](../batches/_template.py) + the [generate-ads skill](../skills/generate-ads/skill.md):
  `art_style` documented as a KEY FIELD and as a **fourth concept-divergence axis** (Medium).

**Remaining under Phase 1:**
- **No spec uses `art_style` yet.** The axis is built but unexercised — author an art-led gut batch
  (2–3 concepts as `illustrated` / `editorial_graphic` / `risograph`) and generate it to validate
  empirically.
- **Bold tier deferred:** `collage` and `surreal_conceptual` (the abstract/conceptual approach),
  plus inspirational-mode prompting (a spare metaphor instead of a pixel-spec) for those styles.
  Add when the Moderate tier is proven and, ideally, after compositing lands (they lean hardest on
  the guards).

---

## Phase 2 — Compositing — **PROTOTYPE DONE (the keystone); wiring NEXT**

**Goal:** stop asking the model to render the pouch label and the exact copy. Generate the
**background/scene only**; paste the real pouch PNG (RGBA 3851×4814) and typeset the copy in code.

**Why it is the keystone:**
- **Cures the reliability cap outright** — zero garbled labels, zero dropped words, perfect
  hierarchy, real fonts. Fixes exactly the 03/05-class defects Phase 0 could not.
- **Makes Phase 1 fully safe** — with the pouch and text owned by code, the generative layer can go
  fully illustrated / surreal / collage with no fidelity risk. Unlocks the Bold tier.
- **Unlocks expressive type** — the model can't reliably render expressive/experimental type; Pillow
  can (Impact/DIN Condensed, Didot/Bodoni, Georgia on macOS).

**The prototype ([`composite.py`](../composite.py), self-contained spike — graduates into the
engine as one deliberate step):**
- **Background-plate prompt mode** — the scene/color world plus reserved clean zones, with a hard
  "no product, no packaging, no text/letters/numbers" rule; flash renders the plate (drafts tier).
- **Layout presets** (`LAYOUTS`) — the small declarative spec: text zone + pouch anchor/height +
  CTA/proof/social slots (`pouch_right` · `poster_top` · `pouch_center`).
- **Type system** (`FONTS`) — `TYPE_PERSONALITIES` mapped to real macOS fonts (DIN Condensed Bold /
  Bodoni 72 / Georgia Italic / Didot / Impact; Helvetica for chips/CTA/captions).
- **Deterministic layer** — real pouch paste with a soft blurred-alpha drop shadow; headline with
  the per-word gold emphasis (NBSP-joined so the accent phrase never splits across a wrap); subhead;
  outlined proof chips; five drawn-polygon stars + the `brand_facts` trust line; category cue fused
  to the pouch lockup (relocates above the pouch when the CTA band would collide); solid/pill/text-link
  CTA with a drawn arrow. Colors are luminance-adaptive (cream-on-dark / dark-on-light; brand gold
  `#867353` on light, sand `#D2C299` on dark) with a soft scrim only when the text zone is mid-tone.
- **Grader calibration** — the `legible` criterion judges the DESIGNED text layer; a real label's
  fine print is not a defect (garbled/invented label text still fails `no_invented_text`).

**Proven on the 3 gut concepts** (photographic scene · dark poster · editorial-graphic medium):
3/3 pass the grader; the label is pixel-perfect by construction and every word is exactly the
spec's. The same run's direct-path reroll put the contrast on record — 05 rendered "flated".

**Remaining to wire into the main path:**
- A `render_mode: "composite"` spec field: `prompt_builder` emits the background-plate prompt;
  `gen.py` generates plates (incl. `--batch`), then composites — one pipeline, both paths.
- Treatment parity: the engine's full `CTA_STYLES` / `SOCIAL_PROOF_VISUALS` catalogs re-expressed as
  drawn treatments (the prototype implements button / pill / text_link and the star-row lockup).
- Tea canister support (per-SKU refs + the Trifecta gradient asset) — the prototype is blend-only.
- Validator rules for the layout spec + golden coverage once composite prompts join the contract.

---

## Phase 3 — Analytics feedback loop — **LATER**

**Goal:** close Superscale's missing fourth pillar — feed live ad performance back into the next
batch's brief, so a brief carries a falsifiable hypothesis and the next batch is shaped by what
actually won (not just internal judgement).

**Why later:** it requires real spend and live data. Until then there is nothing to feed back.

**Tasks (when there is spend):**
- Pull performance via the Meta Ads / Supermetrics MCP (both are wired into this environment).
- A weekly readout: which lever / medium / hook-shape / art_style is winning, by CPA.
- Feed it into `build_brief` — a batch's hypothesis and its coverage targets shaped by the readout.

---

## Open items across phases

- **Wire compositing into the main path** (the Phase 2 remaining-tasks list above) once the
  prototype look is client-approved.
- **Author + generate a direct-path art-led demo batch** to validate Phase 1's model-rendered
  variant empirically (the composited variant is proven by the 03 graphic proto).
- **Legacy UGC cleanup** (optional): the 5 specs the framing guard flags — move capture framing into
  `capture_mode` when each is next touched.
