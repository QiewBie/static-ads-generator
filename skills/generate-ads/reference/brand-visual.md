# Brand visual reference — colors, per-flavor palettes, typography, logo

Loaded on demand when generating. The engine (`prompt_builder.py`) already encodes the SKU
color worlds and the `TYPE_PERSONALITIES`; this file is the human-readable rationale.

## Color palette
| Role | HEX | RGB | Use |
|------|-----|-----|-----|
| Primary Dark | `#282111` | 40 / 33 / 17 | Logo, text on light backgrounds |
| Primary Light | `#FFFDF5` | 255 / 253 / 245 | Backgrounds, light packaging base |
| Secondary Gold | `#867353` | 135 / 115 / 83 | Accents, packaging gradient mid-tone |
| Secondary Sand | `#D2C299` | 210 / 194 / 153 | Highlights, subtle accents |

**Per-flavor creative palettes (ad generation):**
- **Original** — #FFFDF5 → #D2C299 (cream-to-sand gradient), gold foil text
- **Cacao** — #282111 → #867353 (near-black to bronze)
- **Matcha** — sage green → cream (earthy green dominant)
- **Espresso** — near-black to dark espresso brown

(Creative uses the **Original** pouch only — the others are reference, not for current ads.)

## Typography
| Role | Font | Usage |
|------|------|-------|
| Primary | **Canva Sans** | Headlines, titles |
| Secondary | **Calisto MT** | Subheadings |
| Supporting | **Canva Sans Italic** | Body copy |

Image models can't load these fonts — describe **personality**, not font name. Pick the one
that feels inevitable for the concept (never default to condensed bold):

| Personality | How to describe in the prompt | When |
|---|---|---|
| Condensed ultra-bold sans | "ultra-bold ultra-condensed geometric sans-serif, like Bebas Neue / Impact" | confrontational, declarative |
| High-contrast serif | "high-contrast editorial serif with thin and thick strokes, like Didot / Bodoni" | premium, editorial trust |
| Light / italic serif | "elegant thin serif italic, refined and personal" | voice, quotes, intimate moments |
| Mixed weights | "large thin serif headline paired with small bold all-caps sans subtext" | two contrasting ideas |
| Oversized numeral | "massive bold numeral as graphic element dominating the composition" | a number is the whole concept |

A personal ad in condensed bold feels wrong; a confrontational declaration in delicate italic feels wrong.

## Logo
- Full primary logo: websites, footers, stationery. Logo mark only: small spaces (profile pics, favicons).
- Always gold (`#867353` / `#D2C299`) or dark `#282111` — never flat black.
