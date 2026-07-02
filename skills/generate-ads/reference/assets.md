# Asset reference — where the source images live

Loaded on demand when picking refs for a spec. Blend specs ref the Original pouch; tea specs
ref the canisters; comparison specs add a competitor pouch (see `competitors.py`).

```
assets/brand/
├── product_images_blend/      ← blend pouch cutouts (blend REFS)
│   ├── original frontBIL2 .png    ← Original — cream/sand gradient on black bg
│   ├── espresso front BIL2.png    ← Espresso — near-black gradient
│   ├── matcha front BIL 2.png     ← Matcha — sage green gradient
│   └── cacao front BILL 2.png     ← Cacao — dark brown gradient
├── product_images_tea/        ← Ritual Tea canisters (tea REFS)
│   ├── MorningTeasquare.png       ← Morning — amber-gold, white bg
│   ├── AfternoonTeasquare.png     ← Afternoon — sage green, white bg
│   ├── NightTeasquare.png         ← Night — deep navy, white bg
│   ├── trifecta-tea-no-bg.png     ← Trifecta — gold→green→lavender, transparent bg
│   ├── tea ingredients.png        ← 3 pyramid sachets + ingredient breakdown
│   └── tea5.png                   ← lifestyle: 4 canisters + ceramic cup + linen
├── campaign_images/           ← brand-kit lifestyle shots
│   ├── Version 1.jpg              ← full kit: pouch + sachets + mug + frother + spoon + tote + keychain
│   ├── Version 2.jpg              ← kit without tote
│   └── Version 3.jpg              ← minimal: pouch + mug + frother + spoon
├── ingredients/               ← individual ingredient photography
│   ├── Reishi.png + Reishi_R2.png · Lion_s Mane R1.png · Cordyceps.png · Shilajit.png
│   ├── Astragalus.png · He Shou Wu.png · Polygala_R1.png · gynostemma 2.png · MUCUNA.png
├── refs/                      ← proven high-performing Alcami ads (study the thinking, not phrases to lift)
└── alcami guidelines (1).pdf  ← brand guidelines (fonts, colors, logo)
```

**Competitor assets** live in `assets/competitors_assets/` (NOT under `brand/`): `ag1_pouch.png` ·
`ag1_logo.png` · `im8_pouch.png` · `im8_logo.png`. Use for comparison creative only, and show a
rival by **pouch / form factor + brand name in text** — never a pixel-accurate logo (the model
distorts marks, worse than none). The registry + stance: [`competitors.py`](../../../competitors.py).

**Brand accessories visible in campaign_images/:** ceramic travel tumbler (cream) · slim milk
frother (white, ALCAMI) · wooden measuring spoon · canvas tote (mushroom illustration) · gold
foil single-serve sachets · mushroom keychain charm.

**Output:** generated ads land in `ad-workspace/{product}_{audience}_batch{N}/` — a deterministic
folder per campaign (a retry reuses it). A campaign may override with an explicit `run_id`.
