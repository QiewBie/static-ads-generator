# Competitor creative teardown — AG1, IM8, RYZE (visual/structural)

Element-by-element teardown of 24 live competitor ads (`assets/competitors_assets/`: 6 AG1,
7 IM8, 11 RYZE) — not positioning/pricing (that's [competitor-im8-ag1.md](competitor-im8-ag1.md)),
but how each ad is *built*: hierarchy, badge shapes, proof placement, product treatment, density.
Read this alongside [ad-design-principles.md](ad-design-principles.md) — that file is the theory,
this file is the evidence from real spend.

## The one structural law that holds across all 24 ads, zero exceptions

**Headline (top) → proof/context (anchored, never floating alone) → product (the largest single
mass, lower-middle to center) → CTA/offer (bottom).** Not one of the 24 ads puts a star rating or
customer-count line *above or beside* the headline competing for first read. Social proof is either
(a) a bottom-anchored trust row, or (b) folded into the headline itself as a testimonial quote — never
a loose top-corner badge. This is the direct, independent confirmation that the 3pm-crash ad-01
failure (stars stealing the top-left slot, pushing the headline down) isn't a one-off rendering glitch
— it's a violation of something literally every competitor dollar respects.

## AG1 — background is the cheap variable, product+lime is the fixed signature

6 ads, 6 different background colors (dark teal, cream, blue, brown photo, cream, white-tulip photo).
What never changes: the dark-green product packaging and a lime/yellow-green accent (CTA pill,
emphasis word, badge fill) — that pairing alone is "AG1" even with the background swapped every time.
**Lesson: background color is the cheapest, most disposable variation lever — vary it freely. What
must stay constant is a small, specific signature (one accent color + the product), not the whole
palette.** Our `color_world` field already varies per ad (good) — but our *constant* across a batch is
backwards: we repeat CTA copy and trust-mark sets (the things that should carry the brand signature
distinctly) while only the field meant to be freely variable changes.

- **Badge shapes carry meaning, not decoration:** a *heart* = seasonal/emotional offer (Father's Day),
  a *price-tag* = literal discount, a *rounded pill* = a verifiable claim ("Now Clinically-Backed"),
  a *speech bubble* = an announcement ("New Formula"). Shape is chosen per job, never one generic chip
  reused for everything.
- **The connector-line device (ad 5, "Results You Can Feel"):** every product in the lineup hangs from
  a thin vertical line + dot down to its own caption. The line is what tells the eye "this label
  belongs to that object" — it's the literal fix for an orphaned floating label. We have no equivalent
  in our prompt language; `items` blocks float near the product with no explicit visual tether.
  Same device, different geometry, in ad 4: three floating callout chips each have a thin pointer
  line aimed at the specific product detail they describe (gut bacteria claim → the pouch).
- **Density scales with photographic realism, not richness of claim:** the flatlay grid ads (1, 2, 3,
  5) are dense (5-6 SKUs) because they're selling a *bundle*, not because AG1 likes clutter — when the
  ad is a single emotional/seasonal beat (ad 6, Father's Day), it drops to one product, one badge, one
  CTA. Density is a function of what's being sold, not a fixed brand density.

## IM8 — repetition is the brand system, not a flaw, because only the *frame* repeats

3 of 7 IM8 ads (Gold Standard / What Makes IM8 Premium / I Tried Everything) are the **identical
skeleton**: 5 stars → bold 2-line headline → a testimonial-style quote subhead → product centered →
huge negative space top and bottom. Only the background color and the words change. This is
deliberate: a recognizable silhouette trains scroll-stop pattern recognition across a feed, while
color + copy still carry a fresh angle each time. **This reframes the "why do we use the same takes
every time" complaint: identical *structure* is fine and even strategic — IM8 proves it. What's not
fine is identical *content* layered onto identical structure (same proof set, same CTA copy) — that's
where ours fails, because nothing is varying, not even the part meant to carry the news.**

- **Whitespace itself is a premium signal.** IM8's sparsest ads (1 headline + 1 quote + 1 product,
  nothing else) read distinctly more premium than AG1's dense bundle grids or any RYZE ad. Density is
  a register choice: clutter reads "value/deal," whitespace reads "premium/trust." Our blend (loud,
  declare) vs tea (quiet, observe) register split should also modulate *element count*, not just type
  size and color — right now both registers get a similar element count regardless of funnel stage.
- **One real exception to no-CTA-button:** several IM8 ads have *no visible CTA element at all*,
  relying on the platform's native Shop Now button. That's the real-world precedent behind our
  grader's "if intentionally no CTA, pass" rule — it's not a hypothetical edge case, IM8 ships it.
- **The symptom-checklist ad (10 Signs Your Brain Might Need a Boost)** is the one IM8 ad that breaks
  from minimalism — a dense bulleted pain-point list against a moody red liquid-wave background. Used
  exactly once in seven ads: text density is reserved for one specific job (diagnostic self-recognition
  hooks), not a default treatment.

## RYZE — the densest brand, and the only one that consistently shows the *finished drink*

RYZE is cold-acquisition, price-led, and visually the busiest of the three (badges, stat callouts,
prop styling, multiple claims per frame) — consistent with AG1's pattern that density tracks the sales
job, not brand identity. Two RYZE-specific devices worth lifting:

- **Nearly every RYZE ad shows the prepared latte/drink, not just the dry pouch.** RYZE's core
  objection to overcome is "does this still work like coffee" — so the ad does the work of proving it
  visually every time: pouch + finished creamy cup, side by side. **Gap check: none of our three
  3pm-crash ads show a finished latte despite "Latte" being in the product's literal name** — we show
  the pouch (correctly, per CLAUDE.md's "product never decoration") but never the prepared drink that
  proves the ritual is real and enjoyable. Worth testing as an added element, not a replacement.
- **The villain is always the category, never a named rival** ("Traditional Coffee" vs RYZE, a plain
  unbranded bag — no logo). This is the same rule Alcami already follows for people (never name a
  person) extended one level further by RYZE: even brand-vs-brand comparison ads here choose the
  *generic* villain over a named one when the claim is about the category, not a specific competitor.
  Matches our existing "coffee is the villain" rule almost exactly — independent validation, not a gap.
- **Ingredient-ladder format (ad 1):** a vertical list, each ingredient with a small icon and an arrow
  pointing toward the product/drink — visually narrating "these go IN to become THIS." Our
  `blocks/spec_card` items float near the pouch with no directional connector; RYZE's arrow makes the
  cause→effect explicit in one glance.
- **Numbered kit-contents (ryze1.png):** a single grouped photo with small numbered pins (①②③④) tying
  each accessory to one caption line below — solves the same "free welcome kit" idea as AG1's grid of
  separate cutouts, but as one cohesive scene instead of a flatlay grid. A second viable geometry for
  the same job, worth knowing exists.

## On emojis specifically (you asked)

**None of the 24 ads use an actual emoji glyph.** Every star, checkmark, arrow, leaf, heart, and
speech-bubble is a bespoke vector icon rendered in the brand's exact palette (RYZE's checkmarks are
brand-orange, not generic green; AG1's stars are gold or lime depending on background) — never a
platform emoji. Emoji would break the premium register instantly; vector icons recolored to the
brand's system is what reads as designed rather than slapped-together.

## The global "vibe" — bg + color + elements + copy as ONE signal, not four

Looking at all 24 ads as wholes rather than dissecting elements: **each brand has exactly one tonal
register, and every layer — background, color, element style, AND the words themselves — points the
same direction.** None of them ever mix registers inside a single ad.

- **AG1 = clinical-calm.** Backgrounds rotate (teal, cream, blue, photo) but the *temperature* never
  does — always measured, ordered, reassuring. The copy matches word-for-word: "Because YOU matter,"
  "Results You Can Feel" — confident but never loud. Even urgency badges (the red heart, "FOR A SHORT
  TIME ONLY") stay small and contained rather than dominating, because shouting would break the calm
  register the whole brand is built on.
- **IM8 = luxury-medical.** Deep crimson + soft pastel grounds, huge whitespace, a first-person
  superlative quote as the headline ("I have found the ultimate... going to be the best selling
  product in the world"). This is skincare-brand visual grammar borrowed for a powder supplement —
  every layer (minimal layout, jewel-tone red, luxury whitespace, messianic testimonial copy)
  reinforces "this is a premium transformation, not a supplement-aisle product." The one ad that
  breaks the template (the symptom-checklist on the red liquid-wave bg) does it on purpose — that job
  needs dread/urgency, so the *whole register* drops to something wetter and more visceral for that
  one ad, then returns to luxury-calm everywhere else.
- **RYZE = artisanal-blunt.** Browns, wood, steam, latte foam, dried mushroom — real sensory coffee-
  shop cues, never clinical. Copy is tabloid-direct ("Bloating? Try RYZE," "POTBELLY?") with hard
  numeric specificity (1000mg, 48mg caffeine). The synergy: earthy visuals say "natural, real, cozy,"
  blunt copy says "we'll just tell you the dose" — bridging "crunchy" and "credible" at once, which is
  exactly the tension RYZE's actual buyer has to resolve before purchase.

**The takeaway: vibe is a brand-level constant, not an ad-level choice.** Background color, specific
badge, and offer vary ad-to-ad; the emotional register (calm / luxury / blunt) never does. None of
these brands ever let one layer say one thing while another layer says something else.

### Does our ad work the same way? — partially, and the break is diagnosable

Checking the 3pm-crash batch against this lens (not hierarchy — register coherence):

- **Ad 02 (comparison) and ad 03 (spec_card) hold together.** Ad 02 pairs a cool-grey/warm-amber
  split with blunt, RYZE-style copy ("Third coffee at 3, and still foggy?") — color and copy agree.
  Ad 03 pairs `editorial_serif` (a quiet, observing type choice) with a soft cream-gold glow and calm
  copy ("Steady past 3. No crash.") — closer to IM8's luxury-calm, and every layer agrees there too.
- **Ad 01 is the broken one, on a different axis than the orphaned-stars finding.** Its
  `type_personality` is `condensed_bold` — CLAUDE.md's own "declare" register: loud, confrontational,
  fills the frame. But its `color_world` is a soft warm-cream-and-gold glow — a *whisper* palette. The
  ad is shouting in a typeface built for confrontation while wearing a color world built for calm.
  None of the 24 competitor ads ever do this — AG1's loud bundle ads keep punchy color AND confident
  copy together; IM8's soft ads keep gentle type AND soft color together. **We have no equivalent
  discipline: `type_personality` and `color_world` are two fully independent spec fields
  (`prompt_builder.py`) with no pairing logic, so nothing stops a spec from picking a loud type
  treatment and a quiet color world for the same ad** — which is exactly what happened here.

## What this changes about how we judge our own ads

1. **Proof placement is now a hard, evidenced rule, not a stylistic opinion** — bottom-anchored trust
   row or testimonial-fold, never a floating top-corner badge. (Already encoded as `evaluate.py`'s
   `proof_not_orphaned` criterion — this teardown is independent confirmation the fix targets the
   right thing.)
2. **A connector/anchor device (line or arrow) for every secondary callout** is the literal mechanism
   competitors use to prevent orphaning — something `prompt_builder.py` doesn't currently direct.
3. **Badge/chip shape should be chosen per job** (urgency = circle/starburst, verified claim = pill,
   announcement = speech-bubble, seasonal = a literal shape like a heart) — not one generic
   rounded-rectangle reused regardless of what the badge is for.
4. **Element density is a register + funnel-stage parameter**, not a constant. Cold/offer-led can run
   dense; premium/retention should run sparse. Currently undifferentiated in our specs.
5. **Showing the finished prepared drink** alongside the pouch is a RYZE-proven device for products
   whose objection is "does the ritual actually work" — worth testing on blend latte ads.
6. **Identical structure across a batch is not itself the failure** (IM8 proves it can be the brand
   system) — the failure is identical *content* (same proof set, same CTA copy) on top of identical
   structure, which is what actually happened in `productivity_3pm_crash`.
7. **`type_personality` and `color_world` need a register pairing check** — loud/condensed types want
   high-contrast or saturated worlds; quiet/editorial types want soft or desaturated ones. Nothing
   enforces this today, and ad 01's mismatch (condensed_bold shouting inside a soft cream-gold whisper)
   is the direct result.
   - **Quantified, not a one-off:** auditing every `type_personality`/`color_world` pair across
     `batches/blend.py` (9 `condensed_bold` ads), at least 2 of 9 pair the confrontational type with a
     soft, flat warm-cream wash and no real contrast or darkness — the same mismatch as ad 01,
     repeated. The rest pair `condensed_bold` with genuine contrast (a cool-vs-warm split, a
     dark-to-gold gradient) and read fine. So roughly a quarter of our loudest-type ads currently
     fight their own color world.
   - **`oversized_numeral` is defined in `TYPE_PERSONALITIES` and used in zero specs** across
     `blend.py` and `tea.py` — a built tool nobody has reached for yet.
   - **Root cause confirmed in code, not inferred:** `_social_proof_line()` in `prompt_builder.py`
     places proof with the instruction *"placed near the product or the benefit it backs"* — prose,
     not a coordinate or a connector device. `_chip_render_line()` says only *"in one aligned row"* —
     no anchor either. Neither function tells the model WHERE "near" is relative to the headline,
     which is exactly how a chip lands in the one place that competes hardest for first read: the
     top corner.
