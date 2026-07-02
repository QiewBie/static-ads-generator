# Static-Ad Design Principles — how a 1:1 ad gets read, and where each element goes

How attention actually moves through a static feed ad, from eye-tracking science (Nielsen Norman Group), conversion research (CXL, MeasuringU), and tested static-ad practice (attn agency, 5,000+ ads). Mapped to our five formats and our element vocabulary. The job of every layout decision: **engineer the order in which the eye lands on headline → product → social proof → CTA**, in the ~1–3 seconds a feed gives us.

## The one core truth: ads run on focal points, not F/Z

F-pattern, Z-pattern, and the Gutenberg diagram describe where the eye drifts **only when a layout has no hierarchy** — evenly-distributed, text-heavy content like a novel page or search results. The moment a design has elements of different visual weight (a big headline, a hero product, a CTA), those patterns stop applying and the **pattern of focal points** takes over: the eye lands on the most dominant element first, then follows visual weight and directional cues to the next (Vanseo; NN/g). An ad is a high-hierarchy object by definition. So we never "design to the F" — we set the dominance order ourselves and lead the eye through it.

F-pattern is in fact the **failure mode**: NN/g's four scan patterns, worst-to-best, are F → spotted → layer-cake → commitment. F happens when nothing is structured (the eye rakes the top and left and misses the right and bottom). **Layer-cake** (eye hops heading → heading → reads the body under the relevant one) is the most effective scan and is what clear hierarchy produces. **Spotted** (the eye jumps to visually distinct or task-relevant words — bold, a color shift, digits, ★) is why one gold word and a star/number cluster get caught even on a fast scroll. **Commitment** (full reading) only happens for already-motivated, brand-trusting viewers — i.e. warm/retarget, never cold.

## Three levels of dominance — no more (Smashing)

You can't emphasize everything; if every element shouts, nothing is heard. People reliably perceive **three** levels — design distinct steps, not a continuum:

- **Dominant** — one element, greatest weight, the entry point that "sets the context for what's seen next." In our ads this is split by channel: the **headline** is the dominant *message* (read first, carries the hook), the **product** is the dominant *visual mass* (the hero, the resolution). They co-lead and must agree — headline hooks, product answers.
- **Sub-dominant** — the supporting focal points: **social proof**, a key benefit, a comparison column. Noticed after the hero, clearly lighter than it.
- **Subordinate** — recedes to ground: category cue, legal, fine print, and — deliberately — the **CTA's loudness** (the CTA is *placed* terminal and *isolated*, but it is never the heaviest element; see below).

Tested visual-weight budget for a converting static ad (attn, directional not law): hero ≈ 50% · sub-dominant/proof ≈ 30% · CTA ≈ 15% · legal ≈ 5%. Single-hero ads beat multi-focus ads by ~34% CTR and recall ~28% better — competing focal points dilute the one second we get.

## The priority ladder (our reading order) — and the evidence under each rung

1. **Headline** — fast-recognizable, one beat, understood in ~1s (the hook rule). Dominant message. Spotted-scan catches one gold-emphasized word; keep exactly one.
2. **Product (pouch/canister)** — the dominant visual mass and the *resolution* of the concept, never decoration. ≥35% of height, hero-lit. attn: one hero at ~50% weight, supporting elements ≤30%.
3. **Social proof** — sub-dominant, present on **every** ad (varied treatment), sitting **near the product or the benefit it backs**, never overwhelming the message. Tested lift by type: star ratings ≈ +15% CTR · customer photos ≈ +22% engagement · testimonial quote ≈ +18% conversion · usage/scale stat ≈ +12% CTR. (Our validator-safe lockup: ★★★★★ + "200,000+ customers" — stars and a customer count pass; a literal "[N] reviews/ratings" string does not.)
4. **CTA** — the **terminal** focal point (Gutenberg terminal area / bottom-right; the eye's natural exit). Isolated and unmistakably tappable, but **read last, never the loudest** — Meta also renders its own action button directly below our 1:1, so the in-frame CTA complements it rather than competing.
5. **Category cue / legal** — subordinate, recedes.

## CTA: isolation beats color (CXL + MeasuringU)

CXL's verdict after the famous red-vs-green tests: **"No single color is better than another. What matters is how much a button contrasts with the area around it."** The red buttons "won" (+34%, +21%) only because those pages were green-dominant — red *isolated* against them; on a different page green would've won. MeasuringU's two studies (415 people) add the honest caveat: isolation reliably buys **attention**, but not the **choice** by itself — it must combine with real hierarchy and a value reason.

Operating rules for our CTA:
- **The CTA must be the single most isolated form+contrast in its local zone.** Highest-contrast treatment against what's behind it — near-black `#282111` on cream/warm, cream/gold on dark.
- **The CTA must not share a FORM with the proof chips or badges around it.** A ghost/outline CTA sitting among ghost/outline cert chips has zero isolation — it reads as a third badge, not an action. If the proof/badges are outline pills, the CTA is a solid button (or an arrow-down cue); never a fourth pill.
- **Match the register** (loud DR → solid button/pill; editorial/poster/scene → ghost, text-link, integrated, arrow-down, or none) — and **vary across a batch**.

## Color: contrast and isolation, not a "power color"

Hue psychology is real but weak and context-dependent; **contrast and complementarity** are what move attention and conversions (CXL). For our world this means: the warm cream→sand→gold field is the brand ground, and we create dominance by **contrast within it** — near-black headline type, the gold-foil pouch as the brightest mass, one gold-emphasized word, a single high-contrast CTA. Two corroborating findings we can use: a price on a **light/cream background reads as more premium** than on dark (warm-light = quality cue here, not discount); and color drives up to ~80% of brand recognition — our consistent gold is an asset, so the CTA earns isolation through contrast/form, not by importing an off-brand "conversion color."

## Format → reading model (which scan each of our five invites)

- **scene · poster · ugc** — image-dominant, high hierarchy → **pure focal-point control.** No F/Z. Engineer headline → product → proof → CTA with size, contrast, gaze direction (a person's eyes should point at the product/message; faces ≈ +38% engagement), and whitespace (20–30% negative space directs the eye and reads premium).
- **comparison** — two parallel columns → **Z / symmetric scan.** Headline spans the top; the eye sweeps left↔right matching rows (each row the *same* dimension both sides); product + CTA land at the bottom terminal. Rival muted/sub-dominant, Alcami full-contrast as the resolution.
- **how_it_works** — sequential steps → **layer-cake down the steps.** Headline top, steps read top-to-bottom as clean stripes, product + CTA terminal. The step blocks must *flow the eye downward* and must **not** read as a list of dosing times (a by-the-hour pill schedule is brand-toxic for an anti-pill product) — prefer a continuous path (a single energy curve, a flowing line) over discrete numbered pills.
- **blocks** — multi-section → **layer-cake.** One dominant block (headline/benefit), supporting blocks step down in weight; never all-one-weight.

## Per-element placement cheat-sheet

- **Headline** — top or upper band, its own zone (text and product never overlap); one gold word max; personality matches register (high-contrast serif = premium/considered; ultra-condensed sans = declarative/loud; never a generic default sans on a loud archetype).
- **Product** — the hero mass, ≥35% height, lit as the resolution; left-third or clearly dominant placement both test well, as long as it's the single hero.
- **Social proof** — a sub-dominant cluster near the product/benefit; rotate its visual form across a batch (a corner ★ cluster · a "200,000+" number lockup · a star row under the headline · a badge group at the product · a stamp) so proof is everywhere without every ad looking identical.
- **CTA** — terminal (low / lower-right), isolated by form+contrast, quiet, distinct from any chips; sized to its text with margin, never a full-width footer band.
- **Legal / category** — smallest, receding.

## What this rewrites in our pipeline

- **Social proof becomes a universal, varied parameter** (any ad, any archetype) — not a single dedicated archetype — because the evidence says proof belongs on every creative, near the hero, in a treatment that rotates.
- **Type personality is a chosen parameter** per register (serif/condensed/editorial), never an auto-generic sans on declarative archetypes.
- **The CTA carries an isolation rule**: distinct form+contrast vs. its neighbors; never a twin of the proof chips.
- **Each format states its reading flow** so the eye is led (layer-cake down a how_it_works, Z across a comparison, focal-point through a scene) — and how_it_works never renders as a pill-by-the-hour schedule.
