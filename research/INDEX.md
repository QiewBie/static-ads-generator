# Research index — what we know, and which ad it drove

Connective tissue: each research artifact → the campaign(s) it fed → status. Keeps the
chain from insight to ad traceable. (Generated = images on disk; spec = written, not yet run.)

## Audience micro-pain research → campaigns
| Research file | Theme / product | Campaign(s) | Status |
|---|---|---|---|
| [painpoints-productivity.md](painpoints-productivity.md) | coffee-anxiety + 3pm crash · blend | `productivity_coffee_anxiety`, `productivity_3pm_crash` | generated (7 + 3) |
| [painpoints-sleep-blend.md](painpoints-sleep-blend.md) | sleep displacement · blend | `sleep_wave1`, `sleep_wave2` | generated (6 + 7) |
| [painpoints-sleep.md](painpoints-sleep.md) | wind-down · **tea Night** | — (no campaign yet) | — |
| [painpoints-gut.md](painpoints-gut.md) | gut / low-acid · blend | `gut_relief_v1` | generated (5) |
| [glp1-user-research.md](glp1-user-research.md) | GLP-1 routine · blend | `glp1_v1` | spec |

## Competitor intel → registry + comparison campaigns
The structured registry is [`competitors.py`](../competitors.py) (render-capable: AG1, IM8; intel-only: RYZE, MUD\WTR, Everyday Dose, Four Sigmatic, Cymbiotika, Bloom, Onnit, Thesis).
| Research file | Covers | Campaign(s) | Status |
|---|---|---|---|
| [competitor-im8-ag1.md](competitor-im8-ag1.md) | AG1 + IM8 deep-dive | `vs_ag1_v1`, `vs_im8_v1` | spec |

## Reference (cross-campaign, not tied to one)
| File | Use |
|---|---|
| [ad-design-principles.md](ad-design-principles.md) | layout/hierarchy theory — informs every spec |
| [meta-ad-copy-conventions.md](meta-ad-copy-conventions.md) | Meta copy conventions — the ad-copy skill |
| [superscale-teardown.md](superscale-teardown.md) | competitor pipeline teardown — informed the strategic layer (lever/rationale/brief) |
| [claim-caffeine-free-blend.md](claim-caffeine-free-blend.md) | claim verification: Original is caffeine-free (brand-stated) |
| [authoring-claude-md-and-skills.md](authoring-claude-md-and-skills.md) | meta: how this project's CLAUDE.md/skills should be written |
| [competitor-creative-teardown.md](competitor-creative-teardown.md) | AG1/IM8/RYZE ad-level visual teardown (badges, proof placement, density, connectors) |
| [prompt-architecture-redesign.md](prompt-architecture-redesign.md) | the engine redesign roadmap — P0 + P1 DONE (P0 validated on the gut reroll), P2 compositing prototype shipped (`composite.py`, 3/3 pass), P3 analytics LATER |

## Campaigns with no research file yet
`energized_v1`, `tired_parents_v1`, `core_portfolio_v1` (blend) · `launch_v1`, `acquisition_v1`, `pioneer_v1` (tea) — strategy lives in the batch comments / `tea-product-brief.md`.

_Raw pulls are in `_raw/` (gitignored scratch); the distilled files above are the keepers._
