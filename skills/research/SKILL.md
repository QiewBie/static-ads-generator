---
name: research
description: Research Alcami audiences (micro-pains + real, frequent situations in their own words), competitors (what they're actually running), and product/category facts — before writing ad specs. Use when investigating a pain point, persona, rival, offer, or claim. Findings save to research/ and feed the generate-ads skill.
---

# Research — Alcami Elements

Three research jobs, one skill. Findings save to `research/` and feed `generate-ads`. **Never WebFetch/WebSearch** — use the four tools below.

## Why this exists (the strategic frame)
The account data is blunt: **broad and generic loses; hyper-specific wins.** Our generic batches (numbered AI sets, broad-persona Parents/GLP-1) underperformed; the ads that worked were narrow, concrete angles. So research's job is not "who is the audience" in general — it's to surface **micro-pains that are specific AND frequent**, in the audience's own words, each ready to become one sharp ad.

## Tools — match the task, never WebFetch/WebSearch
| Need | Tool | Why |
|---|---|---|
| The audience's pain **in their own words** — real threads, reviews, comments, the specific recurring situations | **Firecrawl** (Reddit, forums, Amazon/Trustpilot, TikTok/IG comments) | Raw voice + concrete scenarios that Tavily smooths into generic summaries |
| What a rival is **actually running** — live ad copy, hooks, offers, faces, active-ad counts | **Scrape Creators** → company search → `/company/ads` | The real Meta Ad Library creative; nothing else pulls it |
| Real creator / UGC reference — how people actually shoot & caption (for `ugc` cuts) | **Scrape Creators** (IG/TikTok/YouTube profiles, posts, transcripts, comments) | Real social artifacts, not descriptions |
| Verifiable facts + synthesized sentiment — prices, certs, ingredients, "is X true", category trends/gaps | **Tavily** | Fast, sourced, no credits; also scouts WHERE to mine |
| Spec → prompt assembly, claim guards, validation, divergence | **local pipeline** (`prompt_builder.py` / `gen.py --policy`) | Engine already owns it — don't research what the pipeline does |

**Efficiency rule:** Tavily for anything factual (cheap, synthesized). **Firecrawl** for the raw voice. **Scrape Creators is metered** — spend it only on what *only it* can do (real live ads / UGC artifacts). Save findings to `research/`.

## Mode 1 — Audience micro-pain deep-dive (the main job now)
Turn one broad theme (productivity, sleep, gut, coffee-quit) into a ranked set of **specific, frequent** micro-pains with real-voice copy fuel. This is **cold-acquisition** work — retarget is a product *launch* to people who already bought, so it runs on news/offer angles, not pain-mining.

**Process:**
1. **Frame** the theme + which audience/product it serves (focus → the blend's Lion's Mane; gut → gut-balance; sleep → tea Night).
2. **Scout & find threads (Tavily + Firecrawl search/map):** map the landscape with Tavily, then surface the specific high-engagement thread/review URLs with Firecrawl search/map. Use the **big-community map** below — don't settle for one subreddit.
3. **Mine raw voice (Firecrawl scrape):** scrape those threads/reviews for the exact words and recurring situations. Save raw pulls to `research/_raw/`.
4. **Cluster** the complaints into 5–10 distinct **micro-pains** — each a specific manifestation, never the broad theme.
5. **For each micro-pain, capture:**
   - **Persona** + the **specific, frequent situation** (the concrete recurring moment — "opens the laptop at 9am and re-reads the same email for 20 minutes").
   - **3–5 verbatim quotes** (their exact words — the copy gold).
   - **Frequency** (roughly how often it recurred — prevalence in the corpus, not a guess).
   - **Angle seed** (the hook direction).
   - **Alcami fit** — the surgically-true mechanism/claim that answers it, and whether a **competitor-quit** framing ("why I quit RYZE") fits.
6. **Rank with the frequency filter** (below), then write the artifact.

### Where to mine — big-community map (start here, extend per theme)
**Source weighting — pain-first.** ~65% **pain-first, product-agnostic** threads (the Communities column — where the raw micro-pain and frequent situation live, and where the cold majority is); ~25% **similar/competitor product** threads (the Reviews column — objections, what-actually-works language, and the "why I quit ___" competitor angle); ~10% **our own Alcami reviews** (verified user outcomes for compliant proof, plus complaints to avoid). Over-weighting product threads narrows the hook to people already category-aware — mine the *pain* in the audience's words; pull objections and comparisons from the product layer.

| Theme | Communities (Reddit unless noted) | Reviews / comments |
|---|---|---|
| Focus / ADHD / productivity | r/ADHD · r/Nootropics · r/productivity · r/getdisciplined · r/cscareerquestions | Amazon reviews of nootropic/focus supps; TikTok/YouTube comments on "focus supplement" videos |
| Coffee-quit / jitters / crash | r/decaf · r/Coffee · r/caffeine · r/Anxiety (caffeine threads) | RYZE / MUD\WTR / Four Sigmatic reviews + "why I quit ___" threads; mushroom-coffee TikTok comments |
| Gut / bloat / digestion | r/GutHealth · r/ibs · r/bloating · r/Supplements | gut/greens product reviews; "coffee wrecks my stomach" threads |
| Sleep / wind-down (tea Night) | r/sleep · r/insomnia · r/decaf | sleep-tea/supp reviews; "can't shut my brain off at night" threads |
| Energy / burnout / depleted | r/Supplements · r/xxfitness · r/workingmoms · r/beyondthebump | energy/greens product reviews |

Quora + brand review pages (Trustpilot, Amazon, the brand's own reviews) supplement every theme. **Mine competitors' negative / "why I quit ___" reviews directly — that's where competitor-quit copy (the proven RYZE angle) lives; it's a Mode 1 + Mode 2 hybrid.**

### Breadth & depth standard (so the dive is actually deep)
- **Breadth:** ≥4 distinct big communities **+ ≥1 competitor-review source** per theme. One subreddit is not research.
- **Depth = engagement-weighted frequency:** rank a micro-pain by how often it recurs *and* how much engagement (upvotes/replies) its threads carry — a 2k-upvote "3pm crash" thread outweighs ten dead posts. Record the rough counts; that's the signal the frequency filter ranks on.
- **Verbatim or it didn't happen:** every micro-pain carries 3–5 real quotes pulled from `_raw`, never paraphrases.

**The frequency filter — "specific BUT frequent":** rank each micro-pain by how often it recurs, not by how clever it is.
- **Keep** the intersection: concrete AND common (the 3pm crash, can't-start-the-morning, bloated-by-afternoon).
- **Cut** absurd one-offs — high specificity, near-zero frequency (the "fix your marriage" trap: a lucky joke, not a repeatable angle).
- **Cut** broad generics — frequent but not specific ("more energy", "be productive").

**Compliance bridge:** the specificity lives in the **scenario and the felt outcome**, never in invented magnitude. Vivid situation + **surgically-true** mechanism — no mg doses, no "10x earnings", no medical claims (these break our claim-guards even though a past winner used "1000mg / 85% off / 10x RYZE"). Mine the pain truthfully; let the engine's guards hold the claim.

**Output → `research/painpoints-{theme}.md`:**
```
# {Theme} — micro-pain taxonomy ({date})
## Micro-pain 1: {short name}   ·   frequency: high/med/low   ·   persona: {who}
- Situation: {the specific recurring moment}
- Real voice: "{quote}" · "{quote}" · "{quote}"
- Angle seed: {hook direction}
- Alcami fit: {mechanism/claim}  |  competitor-quit: yes/no
## Micro-pain 2: …
```
One micro-pain ≈ one tight campaign brief — it drops straight into `generate-ads`.

## Mode 2 — Competitor / artifact research (Scrape Creators)
Pull what a rival is actually running, or real UGC references.
- **Find the page:** `GET /v1/facebook/adLibrary/search/companies?query=` → take the right `page_id`.
- **Get the ads:** `/v1/facebook/adLibrary/company/ads?pageId=&country=US&trim=true`.
- Save analyses to `research/` (see `research/competitor-im8-ag1.md`).

## Mode 3 — Product / category facts (Tavily)
Prices, certifications, ingredients, "is this taste/claim true", category trends and positioning gaps. Synthesized answer + sources, no credits burned.

## Calling conventions
- **curl, not Python urllib** — `urllib` raises `CERTIFICATE_VERIFY_FAILED` here; `curl` uses the system cert store. Read keys from `.env`, then `curl -s -H "x-api-key: $KEY" …` (Scrape Creators) and `curl -s -X POST -d '{…}'` (Tavily). Firecrawl runs through its own CLI/skill.
- **Scrape Creators company search matches broadly** — `query=AG1` also returns people/shows with "AG". Query the **full brand name** ("Athletic Greens", "IM8 Health") and pick by `category` + `likes` for the right `page_id`. Ads come from `/company/ads` (with `pageId`) — `/adLibrary/ads` is not a valid path.
- **Scrape Creators credits are metered** — each response carries `credits_remaining`; an exhausted key returns HTTP 402. Top up the `.env` key when that happens.
- **Tavily's synthesized `answer` is sometimes content-filtered/blank** — read the `results[]` array, don't depend on `answer`.
- **Firecrawl** — scrape to a file, then grep/read it (don't re-scrape the same page); scope to the specific threads/reviews you need; `--only-main-content` for clean text.

---
Findings feed `generate-ads`: a `painpoints-{theme}.md` micro-pain becomes one campaign brief; a competitor pull informs a comparison or a counter-angle.
