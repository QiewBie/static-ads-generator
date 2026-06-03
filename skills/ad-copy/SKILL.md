---
name: ad-copy
description: Write Meta ad copy (primary text, headlines, descriptions) for Alcami Elements static image creatives
---

# Ad Copy Writer — Alcami Elements

Write Meta ad copy for static image creatives. Each ad gets:
- **Primary Text** (above the image) — 1–3 short paragraphs, max 125 chars visible before "See more"
- **Headline** (below the image) — max 40 chars, punchy
- **Description** (below headline) — max 30 chars, supporting line
- **CTA Button** — derived from campaign objective (see CTA mapping below)

## Process

1. Read `CLAUDE.md` for all brand, product, audience, and proof details
2. Understand the campaign objective from the provided ad images and/or input message — purchase, lead-gen, giveaway entry, awareness, etc. Do not assume purchase intent by default.
3. Look at each creative — copy must match the visual angle, mood, and layout. Don't repeat proof points already prominent in the image.
4. Write copy variations per creative — number and length guided by the campaign objective and what the creative actually needs (see Copy Length below)
5. Group output by creative filename

## Campaign Objective → CTA Mapping

Derive the CTA from what the ad is actually asking the viewer to do:

| Objective | CTA Button |
|-----------|------------|
| Direct purchase | Shop Now |
| Lead-gen / giveaway entry | Sign Up |
| Awareness / educational | Learn More |
| Bundle or limited offer | Get Offer |

Never hardcode "Shop Now" — always read the objective from context first.

## Brand Voice Rules (always follow)

- Warm, premium, aspirational — not casually conversational, not clinical. The tone is a trusted friend who lives this ritual, not a brand shouting benefits.
- Empowering, not fearmongering — "achieve your highest self" not "fix your broken body"
- Functional spirituality — ancient ingredients + modern science; ritual + real results
- Anti-jitter, anti-crash framing where relevant — contrast coffee without being preachy
- Specific proof over vague claims — for blend: "200,000 customers." For tea: "thousands" is intentional and correct — no specific count exists for tea.
- Never lead with price — it's corroboration, not the hook
- Earned trust angle: no celebrity endorsements, no podcast deals — real customers
- Do not name celebrities or influencers — not by name, not by implication ("the longevity podcaster," "the football star")
- AG1 and IM8 can be named when running direct comparison ads — competitors are fair game by brand name
- Ritual identity matters: speak to who the customer is becoming, not just what they're buying

## Copy Frameworks

Choose the framework that fits the image format and campaign objective. Don't rotate mechanically — pick the one that matches what this specific ad is doing.

- **Pain → Ritual Solution**: Name the familiar failure (coffee crash, 3pm slump, 2am wake-ups) → offer the ritual that fixes it. Best for `scene` and `ugc` on cold traffic. Open with the pain, not the product.
- **Problem / Symptom First**: Lead with a question or observation about the problem: "Waking up tired after 8 hours?" / "3pm hitting you like a wall?" — then position the product as the answer in the body. Good for `scene` cold traffic and `ugc`.
- **Earned Trust**: Lead with 200,000 real customers or outcome data → make them curious how. Good for `blocks — social_proof` and warm audiences.
- **Us vs Them**: One specific parameter where Alcami clearly wins — taste, transparency, price, trial evidence. Best matched to `comparison` format. Name competitor brands when appropriate.
- **Pattern Interrupt**: Say something unexpected about supplements or morning routines that stops the scroll. Works across all formats as the opening line.
- **Ingredient Credibility**: Ingredients belong in body copy as supporting proof — never as the hook. "9 adaptogens, 10:1 extract, every dose disclosed" works as a trust paragraph after the hook lands, not before. Best for `blocks — ingredient_breakdown`.
- **Identity Hook**: "The kind of person who…" — speak to the aspiration, not the problem. Works for `scene` lifestyle and retarget.
- **UGC Voice**: For `ugc` format — write as if you are a real customer, not a brand. First-person, one specific detail, no benefit lists, no clinical language. "I've had it on my nightstand for three weeks and haven't skipped a night." Not: "Experience the benefits of Reishi for improved sleep quality."
- **Offer + Entry**: For lead-gen and giveaway campaigns — lead with what they get for free, then name the prize. Clear, action-forward: what to do, what they get. No friction.

## Copy by Image Format

The image format determines the copy register, length, and what the copy should add vs. what the image already handles. Never repeat proof points already prominent in the image.

**`scene`** — The image carries the mood. Copy completes the thought the scene opens.
- Register: first-person, warm, specific. Sounds like someone telling you what happened to them.
- Length: short or medium. Long copy fights the visual.
- Don't repeat: the scene, the product name if it's obvious, generic benefits.
- Do add: the specific outcome the scene implies but doesn't state, or a belief-building detail.
- Example: image shows an unplugged coffee maker + Alcami pouch → copy: "Three weeks ago I stopped reaching for it. I haven't missed it once."

**`comparison`** — The image makes the argument. Copy extends it with a human voice.
- Register: direct, factual, confident. Not combative — the comparison speaks for itself.
- Length: medium. The image already has the data; copy gives it a voice.
- Don't repeat: the comparison points already in the image.
- Do add: the emotional implication ("which one would you actually look forward to tomorrow morning?") or the guarantee/trust angle.

**`blocks` — benefit_highlights / social_proof**
- Register: punchy, declarative. Copy mirrors the energy of the image.
- Length: short. The image is dense; copy should be light.
- Do add: a personal framing of the proof ("84% of people reported more energy — I was one of them.") or a CTA hook.

**`blocks` — ingredient_breakdown**
- Register: curious, educational. Copy answers "why does this work?"
- Length: medium. A short education is appropriate here.
- Do add: one sentence connecting the ingredient stack to the human experience ("nine different systems. one morning.").

**`blocks` — testimonial_text**
- Register: match the voice of the testimonial. Don't write over it.
- Length: short. The testimonial is the copy. Add only a brief frame or CTA.
- Do add: attribution context or a question that bridges the testimonial to the reader.

**`ugc`** — The image looks organic. The copy must sound equally organic.
- Register: first-person, casual, conversational. Not branded. Not clinical. Sounds like a DM.
- Length: short only. Long copy destroys the UGC illusion.
- Don't use: formal brand language, benefit lists, medical-adjacent claims.
- Do add: one specific detail that makes it feel lived ("it's been sitting on my nightstand for three weeks and I haven't skipped a night").
- No CTA in the image — put the button text in the copy: "Trying this → [link]" or just "Shop link in bio."

**`how_it_works`** — The image explains the mechanism. Copy frames the why.
- Register: educational but human. Not a textbook. Not a press release.
- Length: medium. The skeptic wants to understand before they buy.
- Don't repeat: the step-by-step already in the image.
- Do add: the human emotional context for why the mechanism matters ("I didn't need a longer ingredients list. I needed to understand why the ones in here actually work.").

---

## Copy Length

Let the format and campaign objective guide length — not a fixed formula:

- **`scene` / `ugc`**: Short (under 125 chars) or medium (2–3 sentences). Long copy fights the visual.
- **`comparison`**: Medium. The image handles the data; copy gives it a human voice.
- **`blocks`**: Short. Dense image + dense copy = overloaded.
- **`how_it_works`**: Medium or long. The skeptic needs more room.
- **Giveaway / lead-gen**: Short and medium only — friction kills conversion.
- **Cold awareness**: Short only — open the loop, don't close it.

Write long copy only when the format and objective clearly call for it.

## Output Format

For each creative, output only the variations appropriate for the image format (see Copy Length above):

```
### [filename]  [format: scene / comparison / blocks / ugc / how_it_works]

**Primary Text (Short — under 125 chars):**
[copy]

**Primary Text (Medium — 2–3 sentences):**
[copy — omit if format calls for short only (ugc, blocks)]

**Primary Text (Long — 3–4 sentences with line breaks):**
[copy — only if format calls for it (how_it_works, Trifecta discovery, social proof story)]

**Headline:** [max 40 chars]
**Description:** [max 30 chars]
**CTA:** [derived from campaign objective — never hardcode "Shop Now"]
```

## Anti-Patterns (never do these)

- Never use: "unlock", "unleash", "supercharge", "skyrocket", "game-changer", "revolutionary"
- Never use medical claim language: "cure", "treat", "diagnose", "clinically proven" (unless directly quoting NSF certification)
- Never use excessive woo-woo: "vibrational", "cosmic", "universe" — keep it grounded
- No emojis unless the image tone strongly calls for it (1–2 max, or none)
- For `scene` / `comparison` / `blocks` / `how_it_works` — premium brand voice. Not a landing page, not a DM.
- For `ugc` — deliberately casual and first-person. This is the one format where "sounds like a DM" is correct. Formal brand language breaks the UGC register.
- Don't start every variation the same way
- Don't lead with price as the hook
- Don't name celebrities or influencers anywhere in ad-facing copy
- Don't repeat proof points already prominent in the image
- Don't use fake scarcity ("limited time", "act now") unless an actual promotion is running
- Don't default to Shop Now — read the campaign objective first

---

## RITUAL TEA LINE — Copy Addendum

This section governs copy for the **Alcami Ritual Tea Line** (Morning / Afternoon / Nighttime / Trifecta). Read the full product details in `tea-product-brief.md`. Rules below override or extend the blend-specific guidance above.

> **Tea copy fast-start:** `tea-product-brief.md` → section "Key Hooks & Headlines by SKU" is the fastest starting point for writing tea ad copy. The frameworks below tell you how to structure it; the brief tells you what to say.

---

### Product facts — see canonical sources (do not restate here)

SKU table, price anchor, status, kit, proof points, caffeine, claim guards (no mg, 4.9★ no count, "thousands" not 200,000+): **CLAUDE.md → Ritual Tea Line** and **tea-product-brief.md**. Those own the facts; this skill owns only the *copywriting craft* below.

---

### Tea Copy Frameworks

Mapped to image format for faster framework selection:

**Best for `scene` / `ugc`:**
- **Circadian Precision**: Name the time + the mushroom + the outcome. "7am. Cordyceps. The slow-rising kind." The specificity IS the hook. Works for any single-SKU ad.
- **The Brewing Pause**: Lead with the 4-minute ritual as the value. "Four minutes, covered. No phone. The pause is half the point." Unique to tea — no supplement ad sounds like this.
- **Pain / Symptom First**: "Waking up at 2am again?" / "3pm hitting you like a wall?" Open with the moment, not the product. Strong for cold `scene` traffic.

**Best for `comparison`:**
- **Not Just Tea**: Contrast against regular tea or sleep aids. "Regular tea: flavored water. No dose. No system. Often microplastic-laced. Alcami Night: Reishi, chamomile, lavender. The nervous system finally gets a proper close."
- **Replace the Wrong Thing**: For Night — "Replace melatonin and magnesium with something that works with your parasympathetic system, not around it."

**Best for `blocks` / `how_it_works`:**
- **Rhythm Problem**: "Most people don't have an energy problem. They have a rhythm problem." Then introduce the three-blend system. Best for Trifecta, system-level ads, and `how_it_works` format.
- **Felt Sleep Outcome**: For Night. Lead with the felt result — "The 2am wake-ups stopped." / "Wake up actually rested." Describe the experience; never invent stats or specific numbers (no "+18% HRV", no day-counts — unverified).

**Best for `ugc`:**
- **First-Person Discovery**: Write as a real customer who found this and is telling one friend. "I've had the night one on my nightstand for three weeks. My sleep tracker noticed before I did." No brand voice, no benefit lists — just one specific honest thing.

**Best for Trifecta (any format):**
- **The Trifecta Discovery**: "All three. Three weeks. Let the body decide." Curiosity-driven, experiment-framing. Good for both cold purchase and gifting.

**Best for RETARGET / launch (existing blend customers — the cross-sell):**
This is a product LAUNCH to people who already love Alcami. Share the news; don't educate or prove. Pair with a two-product (blend + tea) scene where possible.
- **We Made Tea**: pure announcement. "We made tea now." / "It's here." / "New from Alcami." Warm, excited, no proof needed.
- **Loved This? Try This**: the cleanest cross-sell. Make it specific, not generic: "Loved your morning blend? Now there's a tea for 3pm." / "You know the blend. Meet the tea." Extends the ritual — never gap-fills ("what your ritual is missing" is banned: it implies the blend is incomplete).
- **Insider / Early Access**: reward loyalty with first dibs. "Our customers get it first." / "You first." Keep it date-free in the image (no "Pre-Order", no ship dates).
- **One of the First**: pioneer framing — usable. "One of the first mushroom teas." / "The first tea built for morning, afternoon, and night."

---

### CTA Mapping for Tea

| Objective | CTA Button |
|---|---|
| Direct purchase | Shop Now |
| Launch / retarget (existing customers) | Try the Tea · Be the First |
| Trifecta / entry product | Get the Trifecta |
| Gifting angle | Give the Ritual |
| Awareness / circadian education | Learn More |

---

### Tea Copy Length Rules

| Format | Length | Notes |
|---|---|---|
| `scene` (single SKU) | Short or medium | Precise concept — long copy over-explains |
| `ugc` | Short only | Casual first-person — one specific thing |
| `comparison` | Medium | Image handles data; copy gives it voice |
| `blocks` | Short | Dense image needs light copy |
| `how_it_works` | Medium | The skeptic needs context for the mechanism |
| Trifecta (any format) | Medium or long | Discovery narrative needs room to land |
| Night — sleep proof angle | Medium | HRV / 2am story needs one setup sentence to be credible |

---

### Tea Tone — What Changes vs Blend

**Blend copy:** Direct, declarative, sometimes confrontational. "Your coffee is missing 9 things." "Unsubscribe from the stack."

**Tea copy:** Precise, observed, quieter. It doesn't shout — it names something the reader already felt but couldn't articulate.

| Blend copy voice | Tea copy voice |
|---|---|
| "Stop the chaos." | "The morning finally holds." |
| "Your stack is a problem." | "One herb won't do three jobs." |
| "200,000 people made the switch." | "The body chose. Week three." |

Avoid the word "ritual" as a generic filler — in tea copy it has real weight, because the brewing act IS a ritual. Use it precisely: "The closing ritual nobody designs anymore." Not: "Start your wellness ritual today."

---

### Tea Anti-Patterns (specific to tea line)

- Do NOT use "everything at once" or the supplement-stack replacement angle — those belong to the blend
- Do NOT position tea as a replacement for the blend — they are complementary (tea at first light, latte after breakfast)
- Do NOT use date-based CTAs ("Pre-Order Now", ship dates) in ad images
- Factual guards (caffeine, sedation, price, social proof, mg, review counts) are enforced by the engine validator and owned by CLAUDE.md / tea-product-brief.md — don't restate; just write within them
