---
name: ad-copy
description: Write Meta ad copy (primary text + headline) for Alcami Elements static creatives — campaign-parameterized, works for any audience and angle without hardcoding
---

# Ad Copy — Alcami Elements

This skill writes the **Ads Manager text fields around the creative** — NOT in-image text (that belongs to the generate-ads pipeline and its validator):

- **Primary Text** — one long-form ad copy (the usual full Meta primary text). First ~125 chars show on mobile before "…See more"; the first line must work standalone. **One copy per output — no short/medium/variant tiers** (see How many copies + Output format).
- **Headline** — ~40 chars display, below the image. One headline per copy.
- **CTA button** — derived from the campaign objective (mapping below).

We do **not** write the Description field (~30 chars) — leave it blank.

## How many copies

- **No number specified** → write **one copy per creative** (cover every ad in the batch); each completes its own image.
- **A number specified** (e.g. "1 copy for this batch", "give me 3") → write exactly that many **batch-angle copies** — each speaks to the campaign's *whole* angle from the header (the hero copy for the set), not tied to a single creative.

Either way: each copy is **one long-form primary text** in the register that fits the angle — never a set of short/medium/long variants of the same copy.

## The three sources — read, never restate

1. **The campaign config** (`batches/blend.py` · `batches/tea.py`) — the campaign you're writing for. Its **header comment is the audience brief**: who they are, what's broken, the register, the compliance rules. Each ad's spec supplies the copy seeds: `hook` (the ad's one sentence — primary text grows from it), `format`, `archetype`, `audience`, `sku`. **Audience knowledge lives there and in CLAUDE.md — never hardcoded in this skill.** A new audience needs zero skill edits: write its campaign header well and this skill consumes it.
2. **CLAUDE.md** — brand voice and DNA, products, proof points, claim rules, competitive stance, ICP.
3. **`research/meta-ad-copy-conventions.md`** — live-category evidence (AG1/IM8 primary texts) behind the register/emoji/sectioning rules below. Refresh via Scrape Creators when it goes stale.

## Process

1. **Load the campaign** — header brief + every ad spec. Note the `audience` field and any compliance spine in the header.
2. **Settle the count** (How many copies, above): one per creative by default, or exactly the number requested as batch-angle copies.
3. **Know where the click lands** — the campaign's destination (product page, bundle page, lead form). Copy may promise only what that page immediately confirms (see The funnel).
4. **Look at the source** — per-creative copies complete the actual PNG in `ad-workspace/` (never repeat what's already prominent in it); batch-angle copies answer the campaign header's whole angle.
5. **Choose the register** (Axis 1) that fits the angle, and write **one long-form primary text** in it + one headline.
6. **Run the compliance floor** (below) plus every campaign-specific rule from the header.
7. **Output** grouped by creative filename (per-creative) or numbered (batch-angle), each labeled with its register.

---

## The parameter axes — chosen per ad, never defaulted

### Axis 1 — Register (the voice of the one long copy)

The output is always one long-form primary text. Register sets its **voice and structure**, not its length — pick the one that fits the angle:

| Register | When | Emoji | Caps | Voice & structure |
|---|---|---|---|---|
| **Outcome voice** | ugc/testimonial creatives; audience-locked campaigns; warm specifics | 0–2, only what a real person types | none | First-person, a few sentences: one specific lived outcome, then the why, then the soft close. Reads like a person, not a brand. |
| **Structured DR** | blocks/comparison creatives; offers, launches, bundles (blend acquisition) | functional bullets (✅ ⚡ 🍄 🌿 ☕) + max one bracket-pair on the hook line | single words only (FREE, NEW) | Hook line above the fold → blank line → 1–3 sentence paragraph → emoji-bullet benefit/offer block → close (+ fine print if a claim carries †). |
| **Advertorial PAS** | cold structured ads where the mechanism or problem-story is the ad | sparse or none | none | 80–200 words: problem → agitate → resolve, blank-line paragraphs of 1–2 sentences, first line still hooks standalone. |
| **Editorial restraint** | scene/editorial/poster creatives; tea; premium-trust angles | none | none | The quietest long copy — a tight 2–4 sentences, spare and confident. Long ≠ loud; restraint reads as confidence. Never collapse to a single slogan line. |

The register varies with the angle — a loud blend-acquisition batch and a quiet tea launch don't get the same voice. When writing one copy per creative, let the register follow each creative's format/archetype.

### Axis 2 — Audience temperature (`audience` field)

- **acquisition (cold):** introduce. Assume zero brand knowledge; the first line earns the stranger's next three seconds. Hooks from pain/outcome/curiosity; proof builds trust before any ask.
- **retarget (warm):** announce and extend. "You know us" grammar; the news is the hook ("We made tea now"). Never re-educate, never lean on authenticity proof — they already trust us.

### Axis 3 — Audience lock (when the campaign names an audience)

Universal rules for ANY locked audience (parents, GLP-1, athletes, whoever comes next) — the specifics ride in the campaign header:

- **Carry the match.** The landing page is generic, so the copy makes the audience visible in the text itself. A cool-but-generic line wastes the targeting.
- **Name the stakes, not just the label.** Copy says what changes in *their* life ("got me through 5pm with the kids, no third coffee, no crash") — never only an in-group wink or a possessive joke.
- **Sensitive-audience compliance** (any health-adjacent audience): third-person product-fit only ("the GLP-1 morning", "built for the GLP-1 stomach") — never second-person status ("if you're on…", "your GLP-1"), never a drug or condition brand name, never treatment/outcome-of-medication claims. Meta's personal-attributes policy bites hardest in primary text — when in doubt, describe the product's fit, not the reader's condition.

### Axis 4 — Angle (the framework library)

Pick what this specific ad is doing — tagged by fit:

- **Pain → Ritual Solution** (cold · scene/ugc · quiet or outcome): name the familiar failure, offer the ritual. Open with the pain, not the product.
- **Problem/Symptom Question** (cold · scene/ugc · quiet): "3pm hitting you like a wall?" — then the answer in the body.
- **Earned Trust** (cold or warm · blocks/social_proof · structured DR): 200,000 real customers, zero celebrity endorsements — make them curious how.
- **Us vs Them** (cold · comparison · structured DR): one parameter where Alcami clearly wins; competitor brands nameable (AG1, IM8, RYZE) — people never.
- **Pattern Interrupt** (any · any · quiet or DR opening line): say the unexpected thing about supplements or mornings.
- **Ingredient Credibility** (cold · blocks · structured DR/PAS body): ingredients are supporting proof after the hook lands — never the hook.
- **Identity Hook** (warm or lifestyle scene · quiet): who the customer is becoming, not what they're buying.
- **UGC Voice** (cold · ugc · outcome): a real customer telling one friend one specific honest thing. No benefit lists, no clinical language.
- **Offer + Entry** (lead-gen/giveaway · structured DR): what they get, what to do — zero friction.
- **Launch / Announcement** (warm retarget · quiet or structured DR): the news is the value. Insider framing welcome ("our customers get it first").
- **Advertorial Mechanism** (cold · blocks/how_it_works/comparison · PAS): the longest register — why the problem exists, why this solves it. The category proves 200-word feed copy converts when the first line hooks.

### Axis 5 — What the creative already does

Copy completes the image; the division of labor depends on the creative:

- **poster / before_after archetypes** — the image already shouts its one statement or tells its story. Copy NEVER restates it; add the human context, the next beat, or the proof.
- **scene** — the image carries mood; copy states the outcome the scene implies.
- **comparison** — the image carries the data; copy adds the emotional implication ("which one would you actually look forward to tomorrow?") or the guarantee.
- **blocks** — the image is dense; copy stays restrained (editorial or a lean structured DR), or goes full PAS for skeptics when the campaign calls for it.
- **ugc / testimonial** — the image looks organic; copy must sound like the same person. Breaking register breaks the ad.
- **how_it_works** — the image explains; copy frames why the mechanism matters to a human.

---

## The funnel — every field has ONE job, and the click has a destination

The ad unit is a micro-funnel. A viewer travels: image stops the scroll → first line earns the next three seconds → expanded text builds belief → headline + CTA close → the landing page confirms. Each field does its own step and never repeats another's:

| Field | Funnel job | Failure mode |
|---|---|---|
| **First line** (~125 chars) | Hook — works WITH the image to earn the expand or the click. | Restates the image's headline; wastes the only guaranteed-seen line on a brand slogan. |
| **Expanded body** | Belief — read only by the already-interested. Handle the objection, give the proof, make the offer concrete. Sequence: claim → proof → risk-reversal → action. | Re-hooking people who are already hooked; burying proof above the fold where strangers skim. |
| **Headline** | The close — it sits beside the CTA button at the decision moment. Crystallize the outcome or offer in ≤40 chars. | Duplicating the first line; being clever instead of clear at the exact point of action. |
| **CTA button** | Name the action the landing page actually opens with. | "Shop Now" leading to a quiz; "Learn More" leading to a checkout. |

(The Description field is left blank — fold its risk-reversal/proof into the close of the body instead.)

**Message match (the handoff):** the click lands on a page that must immediately confirm what the copy promised — same offer, same price anchor, same claim. Never promise a kit/discount/flavor the page doesn't show. For **audience-locked campaigns the landing page is generic** — the copy carries the audience match (that's Axis 3), but the *product promise* must be one the generic page fulfills. The ad may speak to the GLP-1 morning; it may not imply a GLP-1-specific product page exists.

**Funnel stage sets the ask:** cold copy sells the click and the belief (low-friction close: the guarantee does the heavy lifting); warm copy sells the action now (the news/offer is the close). One copy carries the whole micro-funnel — hook, belief, close — so the long form has room for all three; don't strand the proof or the close.

**Risk-reversal placement:** the 90-day guarantee is the funnel's lubricant — it belongs at the close (end of the body), never as the hook.

## Compliance floor — every copy, every audience

- **Surgically true.** Loud is fine; inflated is not. Every claim survives a literal read. No invented stats, counts, or studies.
- **Proof numbers:** blend = "200,000+"; tea = "thousands" + 4.9★, never a count. Customer-outcome stats only the ones CLAUDE.md lists.
- **Coffee is the villain, never the product.** Coffee/latte language frames the problem; "latte" is never what we sell ("my morning latte" reads as a coffee brand — the validator can't see primary text, so this skill enforces it here).
- **Blend = Original only.** No flavor-variety claims ("four flavors"), no matcha/cacao/espresso copy.
- **No celebrities or influencers** — by name or implication. Competitor *brands* are fair game in comparison angles.
- **Price is corroboration, never the hook.** Anchors: blend "From $39/month", tea "From $37.40/month" — only when the ad's idea earns price.
- **No medical claims** — cure/treat/diagnose/"clinically proven" (NSF certification quoted exactly is fine). FDA-style fine print when a † claim needs it.
- **No fake scarcity** ("act now", "limited time") unless a real promotion is running.
- **No full-caps sentences, no emoji spam** — Meta suppresses low-quality text; the evidence shows top spenders never do either.
- **Banned filler:** "unlock", "unleash", "supercharge", "skyrocket", "game-changer", "revolutionary".
- **When writing one copy per creative, don't open them all the same way; don't repeat proof already prominent in the image.**

## CTA button mapping

Derive from what the ad asks the viewer to do — never default:

| Objective | CTA |
|---|---|
| Direct purchase | Shop Now |
| Launch / retarget cross-sell | Try the Tea · Be the First |
| Trifecta / entry product | Get the Trifecta |
| Lead-gen / giveaway | Sign Up |
| Awareness / education | Learn More |
| Bundle / limited offer | Get Offer |
| Gifting | Give the Ritual |

## Output format

One block per copy — one long-form primary text, one headline, no variants, no description.

Per-creative (default — one per ad):
```
### [filename]  [format/archetype · audience · register]

**Primary Text:**
[one long-form copy]

**Headline:** [max 40 chars]
**CTA:** [from mapping]
```

Batch-angle (when a number is requested — that many, each covering the whole batch angle):
```
### [campaign] — copy [n]  [register]

**Primary Text:**
[one long-form copy speaking to the batch's full angle]

**Headline:** [max 40 chars]
**CTA:** [from mapping]
```

---

## Product-line voice (stable brand DNA — not an audience hardcode)

The two lines speak differently (CLAUDE.md → Brand DNA owns the philosophy):

| | Blend | Tea |
|---|---|---|
| Mode | **Declares.** Direct, confident, sometimes confrontational. | **Observes.** Precise, quiet — names what the reader already felt. |
| Example | "Stop the chaos." / "200,000 people made the switch." | "The morning finally holds." / "One herb won't do three jobs." |
| Default registers | any; structured DR and PAS welcome on cold | editorial restraint and outcome voice; emoji ≈ none |

**Tea craft notes** (facts live in CLAUDE.md → Ritual Tea Line + `tea-product-brief.md`; the validator enforces the claim guards):
- **Circadian precision** is the unique angle: time + mushroom + outcome ("7am. Cordyceps. The slow-rising kind."). The specificity IS the hook.
- **The brewing pause** ("Four minutes, covered. No phone.") — no supplement ad sounds like this; use it.
- "Ritual" carries real weight in tea copy because brewing IS one — use it precisely, never as filler.
- Never "everything at once" / stack-replacement angles (those are the blend's); never tea-replaces-blend (complementary, ever); no Pre-Order dates anywhere.
- Trifecta is ONE product: "Get the Trifecta," never "try all three."
