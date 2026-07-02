# Authoring CLAUDE.md & skills for best results — findings + how our system compares

Sourced research on writing high-quality agent instructions, with each principle mapped to
our current state and the pipeline impact of changing it. **Analysis only — not yet applied.**

## Sources
- Anthropic — *Claude Code best practices* (engineering blog): the CLAUDE.md section.
- Anthropic — *Claude Code memory* (docs.claude.com): CLAUDE.md structure, `@import`, what-to-include table.
- Anthropic — *Agent Skills best practices* (docs.claude.com): concision, progressive disclosure, freedom-vs-fragility, frontmatter/naming.
- Anthropic — *Equipping agents with Agent Skills* (engineering blog): the 3-level progressive-disclosure model.
- Anthropic — *Building effective agents* (engineering blog): simplest-thing-first, workflows vs agents, composable patterns.
- Anthropic — *Prompt engineering overview* (docs.claude.com): eval-driven; technique order clarity → examples → XML → role → thinking → chaining.
- Community/marketer pointers (Tavily): marmelab "Agent Experience", HN "Writing a good CLAUDE.md", Google Cloud prompt-engineering guide. (Supplementary, not authoritative.)

## The principles (Anthropic-official, verbatim where it matters)

**CLAUDE.md**
1. **Context fills fast; performance degrades as it fills.** CLAUDE.md loads every session — every token competes with the conversation.
2. **Only include what applies BROADLY.** Sometimes-relevant domain knowledge/workflows belong in **skills** (loaded on demand), not CLAUDE.md.
3. **The prune test:** "Would removing this cause Claude to make mistakes? If not, cut it." **"Bloated CLAUDE.md files cause Claude to ignore your actual instructions."**
4. **If a rule keeps getting ignored, the file is probably too long and the rule is getting lost.**
5. **Treat CLAUDE.md like code** — review, prune regularly, test by observing whether behavior actually shifts.
6. Tune adherence with emphasis ("IMPORTANT" / "YOU MUST"). Split with `@path/to/import`.
7. **Close the loop:** give the agent a check that returns pass/fail (test/build/lint) so it self-verifies instead of you being the verification loop.

**Skills**
8. **Concise is key — the context window is a public good.** "Does this paragraph justify its token cost? Only add context Claude doesn't already have."
9. **Progressive disclosure (3 levels):** (1) name+description metadata is preloaded; (2) SKILL.md body loads only when relevant; (3) bundled reference files load only as needed. Keep SKILL.md lean; push depth into referenced files.
10. **Match freedom to fragility** — "narrow bridge with cliffs" (one safe way → exact, low-freedom instructions) vs "open field" (many paths → general direction, high freedom).
11. **Frontmatter:** `name` (lowercase-hyphen, gerund form preferred) + `description` (third person, says *what it does AND when to use it* — this drives discovery).
12. **Structure for scale:** split an unwieldy SKILL.md into separate files; keep mutually-exclusive paths separate to save tokens; code can be both tool and documentation.

**Prompt-engineering science / agent design**
13. **Eval-driven:** define success criteria + an empirical test FIRST.
14. **Technique priority:** be clear and direct → examples (multishot) → XML structure → role → let-it-think (CoT) → prompt chaining.
15. **Simplest solution first;** add agentic complexity only when warranted. Workflows (predefined paths) beat autonomous agents for well-defined tasks.

## How OUR system does it now (facts)
- **CLAUDE.md ≈ 35 KB (~9k tokens), loaded every session.** ~18 major sections, many *generation-only*: full SKU color tables, ingredient mechanisms, the brand-guidelines fonts/logo rules, the competitor keyword lists, the `assets/` file tree, the full Creative-Principles catalog, "currently running ads."
- **3 skills** (`generate-ads` ~210 lines, `research`, `ad-copy`) — fairly self-contained; minimal use of the level-3 bundled-reference pattern. Names are not gerund form.
- **`tea-product-brief.md` (27 KB)** is read on demand (not auto-loaded) — already good progressive disclosure.
- **The engine (`prompt_builder` + `pb_validate`) is low-freedom** (exact templates, hard rules, claim guards) while **creative (hooks/concepts) is high-freedom** (the skill pushes divergence).
- **Closed-loop check exists as of this session:** `tests/` (`make check`) — validate-all + golden-prompts + CLAUDE↔engine fact-consistency.

## Where we ALREADY align (strengths — don't touch)
- **Freedom-matched-to-fragility (#10):** the engine locks the fragile (claims, format, render); creative is the open field. Textbook-correct.
- **Workflow-not-agent simplicity (#15):** the pipeline is a predefined spec→build→gen workflow, not an autonomous agent. The endorsed default.
- **Closed-loop check (#7, #13):** `tests/` + the validator realize exactly the self-verification loop Anthropic recommends.
- **Some progressive disclosure (#9):** tea-brief and the research outputs load on demand.

## Where we DIVERGE — the honest, full list (a first shallow read said "only size"; it's more)

### Category 1 — the operational quality-loop layer (the real gaps)
- **No automated output evaluation (evaluator-optimizer).** *Building effective agents* names it: one model generates, another evaluates against criteria in a loop. We generate images but grade "is this ad good / on-brief" 100% manually. The `tests/` harness closes the loop on prompt-assembly + facts (the deterministic engine), NOT on image quality. Biggest missing pattern for a generation pipeline.
- **Zero hooks — all enforcement is advisory CLAUDE.md.** Docs: hooks are deterministic, CLAUDE.md is advisory; use hooks for what must happen every time. Our recurring "rule gets ignored" history IS the advisory failure mode. `make check` exists but isn't wired to a Stop hook.
- **No skill-effectiveness evals.** Docs: build evals FIRST; they're the source of truth. Ours are contract tests, not "given a brief, does the skill produce a good ad vs baseline."
- **Self-grading, not fresh-model verification.** Docs recommend a verification subagent so the worker isn't the grader. Our pre-flight self-grades.

### Category 2 — content/structure hygiene
- **Time-sensitive content** in CLAUDE.md ("Currently Running Ads (June 2026)") — the exact named anti-pattern.
- **Inconsistent terminology** — specs mix adaptogens / super-herbs / mushrooms; docs say one term throughout.
- **No progressive-disclosure file-splitting** in skills (single-file; under 500 lines so not urgent).
- **CLAUDE.md ~35 KB always-loaded** — over the lean threshold; the bloat→ignored-rules failure mode is documented and we live it. *Re-tier, not delete* (marketing voice/facts can't be inferred from the repo, so the floor is higher than a code project's).

### Category 3 — polish
- Skill names not gerund; ad-copy's description lacks an explicit "Use when" trigger.
- Voodoo constants in gen.py (sleep 15, timeout 180, 19 MB, 3 retries) partly undocumented.
- No cross-model testing (Haiku/Sonnet/Opus); skills never run against the docs' QA checklist.

## Corrected verdict
Strong **architectural** alignment (locked engine + free creative, workflow-not-agent, plan-validate-execute, contract tests) but a **weak feedback/enforcement spine**: missing automated output evaluation, deterministic hooks, skill evals, and fresh-model verification. "We mostly match except size" was wrong.

## The marketing-specific nuance
Anthropic's "lean CLAUDE.md" guidance targets *coding* agents, where the codebase itself carries the context. A *marketing* agent legitimately carries more in-doc domain knowledge (brand voice, claims, ICP) because none of it is inferable from the repo. So the answer is **not** "cut CLAUDE.md to 50 lines" — it's **tier it**: a lean, always-loaded identity+rules core, with the deep generation knowledge on demand. The bloat→ignored-rules failure mode still applies; the richness just has a higher floor than a code project's.
