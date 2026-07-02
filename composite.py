#!/usr/bin/env python3
"""Compositing prototype — Phase 2 of the prompt-architecture redesign (the keystone).

The deterministic layer (the REAL pouch PNG + code-typeset copy in real fonts) is pasted
over a model-generated BACKGROUND PLATE — the model never renders the label or the words,
so the whole garbled-label / dropped-word / duplicate-claim defect class cannot occur.

This file is the self-contained SPIKE the roadmap calls for (prototype on gut concepts
before wiring into the main path). Everything prototype-scoped lives here — the background
prompts, the layout presets, the type system, the demo specs — so it graduates into
prompt_builder / gen.py as one deliberate step once the look is approved.

    python3 composite.py --proto              generate backgrounds (flash, cached) → composite → grade
    python3 composite.py --proto --dry-run    print the background prompts, touch nothing
    python3 composite.py --proto --recomposite  re-typeset over the cached backgrounds (no API)

Output: ad-workspace/composite_proto/  (backgrounds cached in bg/, finals at the root).
"""
import sys, os, json, base64, ssl, math, time, urllib.request
from pathlib import Path
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompt_builder import BLEND_SKUS, CATEGORY
from brand_facts import CUSTOMER_COUNT

ROOT = Path(__file__).resolve().parent
OUT  = ROOT / "ad-workspace" / "composite_proto"
BG_MODEL = "gemini-3.1-flash-image-preview"   # backgrounds are drafts — flash tier
CANVAS = 1080

# ── Brand palette (reference/brand-visual.md) ─────────────────────────────────
DARK  = (40, 33, 17)      # #282111 primary dark
CREAM = (255, 253, 245)   # #FFFDF5 primary light
GOLD  = (134, 115, 83)    # #867353 secondary gold — the accent on light grounds
SAND  = (210, 194, 153)   # #D2C299 highlight gold — the accent on dark grounds

# ── Type system: TYPE_PERSONALITIES → real font files (macOS system fonts) ────
_SUP = "/System/Library/Fonts/Supplemental/"
FONTS = {
    "condensed_bold":     (_SUP + "DIN Condensed Bold.ttf", 0, True),    # (path, ttc index, force caps)
    "editorial_serif":    (_SUP + "Bodoni 72.ttc",          0, False),
    "light_serif_italic": (_SUP + "Georgia Italic.ttf",     0, False),
    "mixed_weights":      (_SUP + "Didot.ttc",              0, False),
    "oversized_numeral":  (_SUP + "Impact.ttf",             0, False),
    "sans":               ("/System/Library/Fonts/Helvetica.ttc", 0, False),   # chips/CTA/captions
    "sans_bold":          ("/System/Library/Fonts/Helvetica.ttc", 1, False),
}

def _font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    path, idx, _ = FONTS[kind]
    return ImageFont.truetype(path, size, index=idx)

def _caps(kind: str) -> bool:
    return FONTS[kind][2]


# ── Layout presets — the small declarative layout spec the plan asks for ──────
# Fractions of the canvas. text_zone holds the headline/subhead stack; the pouch is
# anchored by its bottom edge; supporting marks take named slots.
LAYOUTS = {
    # text column upper-left, pouch lower-right — the editorial-scene default
    "pouch_right": {
        "text_zone":  (0.07, 0.08, 0.58, 0.55), "text_align": "left",
        "pouch":      {"anchor": "right", "height": 0.46, "mx": 0.05, "my": 0.045},
        "cta_slot":   (0.07, 0.86), "proof_slot": "under_text", "social_slot": "under_text",
    },
    # centered text block on top, pouch lower-right beside the scene's own object (a cup)
    "poster_top": {
        "text_zone":  (0.10, 0.07, 0.90, 0.46), "text_align": "center",
        "pouch":      {"anchor": "right", "height": 0.44, "mx": 0.07, "my": 0.085},
        "cta_slot":   (0.40, 0.905), "proof_slot": "under_text", "social_slot": "under_text",
    },
    # pouch lower-center-left, text column upper area, chips down the right
    "pouch_center": {
        "text_zone":  (0.08, 0.07, 0.92, 0.38), "text_align": "center",
        "pouch":      {"anchor": "center", "height": 0.50, "mx": 0.0, "my": 0.04},
        "cta_slot":   (0.50, 0.93), "proof_slot": "sides", "social_slot": "under_text",
    },
}


# ── The 3 demo concepts (gut_relief copy, compositor fields) ──────────────────
# Backgrounds only describe the WORLD + the reserved clean zones; every word and the
# pouch itself are deterministic. Concept C runs an editorial_graphic background —
# the Phase 1 × Phase 2 combination (art-led medium, zero fidelity risk).
_BG_RULES = (
    "\n\nSTRICT — BACKGROUND PLATE ONLY: render NO product, NO packaging, pouch, canister, bottle "
    "or box, NO logos, and NO text, words, letters, or numbers anywhere in the frame. The reserved "
    "areas described above stay as clean, natural negative space (a clear stretch of surface, a calm "
    "field of tone) — never an empty drawn box, frame, or placeholder outline. Full-bleed 1:1 square, "
    "sharp corners, no borders."
)

PROTO_ADS = [
    {
        "file": "01_wasnt_my_stomach.png",
        "layout": "pouch_right",
        "type_personality": "light_serif_italic",
        "headline": "It wasn't my stomach.\nIt was the coffee.",
        "emphasis": "the coffee",
        "subhead": "Swapped it for a creamy, low-acid cup. Mornings sit easy again.",
        "chips": [],
        "social_proof": True,
        "cta": ("Make the swap", "text_link"),
        "category_cue": True,
        "bg_prompt": (
            "A real morning kitchen photographed on medium format, 80mm — warm, premium, quietly "
            "hopeful. On the counter at the LEFT edge, partly out of frame: an abandoned dark black "
            "coffee in a plain glass cup, reading cold and grey. Toward the right, a warm ceramic mug "
            "holding a pale golden creamy drink with a hint of rising steam, lit by soft window light. "
            "The light warms from cool grey at the far left to soft cream-and-amber daylight on the "
            "right. COMPOSITION: the counter's LOWER-RIGHT quarter is a clear, empty stretch of warm "
            "wood surface (room for something to stand there later), and the UPPER-LEFT two-thirds of "
            "the frame is calm, softly out-of-focus kitchen depth — quiet negative space with no busy "
            "detail. No people." + _BG_RULES
        ),
    },
    {
        "file": "02_like_cream_not_acid.png",
        "layout": "poster_top",
        "type_personality": "editorial_serif",
        "headline": "Goes down like cream.\nNot acid.",
        "emphasis": "cream",
        "subhead": "Low-acid, dairy-free, gentle on an empty stomach.",
        "chips": [],
        "social_proof": False,
        "cta": ("Switch your cup", "button"),
        "category_cue": True,
        "bg_prompt": (
            "A dark premium still-life plate: a deep near-black ground (very dark warm brown-black, "
            "like #282111 unlit velvet) filling the whole frame. In the LOWER-LEFT third sits one warm "
            "ceramic mug of pale golden creamy liquid, gently steaming — the single warm, lit object, "
            "glowing out of the dark with a soft gold rim light. Everything else is calm darkness with "
            "the faintest warm falloff around the cup. COMPOSITION: the UPPER HALF of the frame is pure "
            "deep dark negative space; the LOWER-RIGHT quarter of the surface is empty dark tabletop "
            "with room for something to stand there later." + _BG_RULES
        ),
    },
    {
        "file": "03_gut_balance_graphic.png",
        "layout": "pouch_center",
        "type_personality": "mixed_weights",
        "headline": "Gut balance,\nbuilt into the label.",
        "emphasis": "the label",
        "subhead": "Not a promise in an ad. A line on the pouch.",
        "chips": ["NSF Certified", "Dairy-free", "Low-acid"],
        "social_proof": True,
        "cta": ("See what's inside", "pill"),
        "category_cue": True,
        "bg_prompt": (
            "A premium flat EDITORIAL GRAPHIC DESIGN field, not a photograph — museum-poster restraint: "
            "a warm cream ground (#FFFDF5) with two or three large, soft-edged flat color fields in warm "
            "sand and muted gold sweeping diagonally through the lower half, one thin darker sand band "
            "as a quiet horizon line. Crisp geometry, generous negative space, the feel of a high-end "
            "print spread. No depth-of-field, no photographic texture — flat, refined color. COMPOSITION: "
            "the CENTER of the lower half is a calm, unbroken field (room for an object to sit there "
            "later); the TOP THIRD is nearly empty cream negative space." + _BG_RULES
        ),
    },
]


# ── Background generation (interactive flash — a 3-image spike; production wiring
#    runs through gen.py's --batch path) ──────────────────────────────────────────
def _load_env() -> dict:
    env = {}
    p = ROOT / ".env"
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env

def _ssl_ctx(env) -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    if env.get("GEMINI_VERIFY_SSL") != "1":
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    return ctx

def gen_background(prompt: str, dst: Path, api_key: str, ctx) -> bool:
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"],
                             "imageConfig": {"aspectRatio": "1:1"}},
    }).encode()
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"{BG_MODEL}:generateContent?key={api_key}")
    for attempt in (1, 2, 3):
        try:
            req = urllib.request.Request(url, data=payload,
                                         headers={"Content-Type": "application/json"})
            body = json.loads(urllib.request.urlopen(req, timeout=180, context=ctx).read())
            for part in body.get("candidates", [{}])[0].get("content", {}).get("parts", []):
                if "inlineData" in part:
                    img = Image.open(BytesIO(base64.b64decode(part["inlineData"]["data"])))
                    img.convert("RGB").save(dst, format="PNG")
                    return True
            print(f"      attempt {attempt}: no image in response")
        except Exception as e:
            print(f"      attempt {attempt}: {str(e)[:80]}")
            time.sleep(8)
    return False


# ── Drawing helpers ────────────────────────────────────────────────────────────
def _zone_luminance(img: Image.Image, box) -> float:
    z = img.crop([int(v) for v in box]).convert("L").resize((24, 24))
    return sum(z.getdata()) / (24 * 24)

NBSP = "\u00a0"

def _wrap(draw, text, font, max_w, keep_together: str = ""):
    """Wrap on explicit \\n first, then by width. `keep_together` (the emphasis phrase)
    is treated as one unbreakable token so the accent never splits across lines."""
    if keep_together and keep_together in text:
        text = text.replace(keep_together, keep_together.replace(" ", NBSP))
    lines = []
    for raw in text.split("\n"):
        # split on plain space ONLY — bare .split() treats the NBSP join as whitespace too
        words, cur = [w for w in raw.split(" ") if w], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial.replace(NBSP, " "), font=font) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur); cur = w
        if cur:
            lines.append(cur)
    return lines

def _fit_headline(draw, text, kind, max_w, max_h, start=96, floor=44, keep_together=""):
    """Largest size whose wrapped block fits the zone."""
    size = start
    while size > floor:
        f = _font(kind, size)
        lines = _wrap(draw, text, f, max_w, keep_together)
        line_h = int(size * 1.14)
        if len(lines) <= 4 and len(lines) * line_h <= max_h:
            return f, lines, line_h
        size -= 4
    f = _font(kind, floor)
    return f, _wrap(draw, text, f, max_w, keep_together), int(floor * 1.14)

def _draw_rich_line(draw, xy, line, font, base_fill, accent_fill, accent_phrase, align_w=None):
    """Draw one line word-by-word so an emphasis phrase can carry the accent color.
    The wrap step NBSP-joins the phrase, so here it arrives as one token."""
    x, y = xy
    if align_w is not None:                      # center inside align_w
        x += (align_w - draw.textlength(line.replace(NBSP, " "), font=font)) / 2
    acc = (accent_phrase or "").lower()
    for tok in line.split(" "):
        seg = tok.replace(NBSP, " ")
        is_acc = acc and seg.strip(".,!?").lower() == acc
        draw.text((x, y), seg, font=font, fill=accent_fill if is_acc else base_fill)
        x += draw.textlength(seg + " ", font=font)

def _star(draw, cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    draw.polygon(pts, fill=fill)

def _shadowed_pouch(pouch: Image.Image, h_px: int):
    """Scaled pouch + its soft drop shadow layer (blurred alpha, warm-dark)."""
    w_px = int(pouch.width * h_px / pouch.height)
    p = pouch.resize((w_px, h_px), Image.LANCZOS)
    pad = 60
    sh = Image.new("RGBA", (w_px + 2 * pad, h_px + 2 * pad), (0, 0, 0, 0))
    a = p.split()[3].point(lambda v: int(v * 0.45))
    dark = Image.new("RGBA", p.size, (24, 18, 8, 255))
    dark.putalpha(a)
    sh.paste(dark, (pad + 8, pad + 16), dark)
    return p, sh.filter(ImageFilter.GaussianBlur(14)), pad


# ── The compositor ─────────────────────────────────────────────────────────────
def composite_ad(bg_path: Path, ad: dict, out_path: Path):
    canvas = Image.open(bg_path).convert("RGB").resize((CANVAS, CANVAS), Image.LANCZOS)
    layout = LAYOUTS[ad["layout"]]
    overlay = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    tz = [v * CANVAS for v in layout["text_zone"]]
    on_dark = _zone_luminance(canvas, tz) < 118
    text_col   = CREAM if on_dark else DARK
    accent_col = SAND  if on_dark else GOLD
    centered   = layout["text_align"] == "center"
    zone_w     = tz[2] - tz[0]

    # Soft scrim sized to the text zone — only when the zone is mid-tone/busy.
    lum = _zone_luminance(canvas, tz)
    if 95 <= lum <= 175:
        scrim = Image.new("L", (CANVAS, CANVAS), 0)
        sd = ImageDraw.Draw(scrim)
        for i in range(int(tz[3] - tz[1])):
            alpha = int(70 * (1 - i / max(1, tz[3] - tz[1])))
            sd.line([(tz[0] - 20, tz[1] + i), (tz[2] + 20, tz[1] + i)], fill=alpha)
        scrim = scrim.filter(ImageFilter.GaussianBlur(24))
        tone = Image.new("RGBA", (CANVAS, CANVAS),
                         (CREAM + (0,)) if not on_dark else ((15, 12, 6, 0)))
        tone.putalpha(scrim)
        overlay = Image.alpha_composite(overlay, tone)
        draw = ImageDraw.Draw(overlay)

    # ── Headline (per-word accent) + subhead ──
    kind = ad["type_personality"]
    head = ad["headline"].upper() if _caps(kind) else ad["headline"]
    f_head, lines, line_h = _fit_headline(draw, head, kind, zone_w, (tz[3] - tz[1]) * 0.72,
                                          keep_together=ad.get("emphasis", ""))
    y = tz[1]
    for ln in lines:
        _draw_rich_line(draw, (tz[0], y), ln, f_head, text_col, accent_col,
                        ad.get("emphasis"), align_w=zone_w if centered else None)
        y += line_h
    y += int(line_h * 0.25)
    f_sub = _font("sans", 34)
    for ln in _wrap(draw, ad.get("subhead", ""), f_sub, zone_w * 0.94):
        x = tz[0] + ((zone_w - draw.textlength(ln, font=f_sub)) / 2 if centered else 0)
        draw.text((x, y), ln, font=f_sub,
                  fill=text_col + (235,))
        y += 46

    # ── Social proof: five stars + the blend trust line (brand_facts) ──
    if ad.get("social_proof"):
        y += 18
        star_r, gap = 13, 34
        row_w = 5 * gap + 14 + draw.textlength(CUSTOMER_COUNT, font=_font("sans", 30))
        sx = tz[0] + ((zone_w - row_w) / 2 if centered else 0)
        for i in range(5):
            _star(draw, sx + star_r + i * gap, y + star_r + 2, star_r, accent_col)
        draw.text((sx + 5 * gap + 14, y + 2), CUSTOMER_COUNT, font=_font("sans", 30),
                  fill=text_col + (225,))
        y += 52

    # ── Proof chips ──
    chips = ad.get("chips") or []
    if chips and layout["proof_slot"] == "under_text":
        y += 14
        f_chip = _font("sans_bold", 26)
        cx = tz[0]
        for c in chips:
            w = draw.textlength(c, font=f_chip) + 44
            draw.rounded_rectangle([cx, y, cx + w, y + 48], radius=24,
                                   outline=text_col + (200,), width=2)
            draw.text((cx + 22, y + 10), c, font=f_chip, fill=text_col + (230,))
            cx += w + 14

    # ── Pouch + shadow (the deterministic product layer) ──
    pouch_src = Image.open(ROOT / BLEND_SKUS["original"]["ref_path"]).convert("RGBA")
    pl = layout["pouch"]
    h_px = int(pl["height"] * CANVAS)
    p, sh, pad = _shadowed_pouch(pouch_src, h_px)
    if pl["anchor"] == "right":
        px = CANVAS - int(pl["mx"] * CANVAS) - p.width
    elif pl["anchor"] == "center":
        px = (CANVAS - p.width) // 2
    else:
        px = int(pl["mx"] * CANVAS)
    py = CANVAS - int(pl["my"] * CANVAS) - p.height
    overlay.alpha_composite(sh, (px - pad, py - pad))
    overlay.alpha_composite(p, (px, py))
    draw = ImageDraw.Draw(overlay)

    # chips down the free side when the pouch holds the center
    if chips and layout["proof_slot"] == "sides":
        f_chip = _font("sans_bold", 26)
        cy = py + 40
        for c in chips:
            w = draw.textlength(c, font=f_chip) + 44
            cx0 = (px - w) / 2                    # centered in the left gap beside the pouch
            draw.rounded_rectangle([cx0, cy, cx0 + w, cy + 48], radius=24,
                                   fill=CREAM + (235,), outline=GOLD + (255,), width=2)
            draw.text((cx0 + 22, cy + 10), c, font=f_chip, fill=DARK + (255,))
            cy += 72

    # ── CTA geometry first (the cue avoids it), then cue, then the CTA itself ──
    cta_text, cta_style = ad["cta"]
    f_cta = _font("sans_bold", 30)
    cw = draw.textlength(cta_text, font=f_cta)
    cx_f, cy_f = layout["cta_slot"]
    cx, cy = cx_f * CANVAS, cy_f * CANVAS
    if cta_style in ("button", "pill"):
        pad_x, pad_y = 34, 18
        x0 = cx - (cw / 2 + pad_x if centered else 0)
        cta_box = [x0, cy, x0 + cw + 2 * pad_x, cy + f_cta.size + 2 * pad_y]
    else:
        cta_box = [cx, cy, cx + cw + 46, cy + f_cta.size + 16]

    # ── Category cue — small caption fused to the product lockup. Sits under the pouch;
    #    when that band would collide with the CTA (or run off-canvas) it moves above the pouch.
    if ad.get("category_cue"):
        cue = CATEGORY["blend"]
        f_cue = _font("sans", 24)
        cue_w = draw.textlength(cue, font=f_cue)
        cue_x = px + (p.width - cue_w) / 2
        cue_y = py + p.height + 6
        cue_box = [cue_x, cue_y, cue_x + cue_w, cue_y + 30]
        collide = not (cue_box[2] < cta_box[0] - 16 or cue_box[0] > cta_box[2] + 16
                       or cue_box[3] < cta_box[1] - 8 or cue_box[1] > cta_box[3] + 8)
        if collide or cue_y + 30 > CANVAS - 8:
            cue_y = py - 36
        cue_dark = _zone_luminance(canvas, (cue_x, cue_y, cue_x + cue_w, cue_y + 30)) < 118
        draw.text((cue_x, cue_y), cue, font=f_cue,
                  fill=(CREAM if cue_dark else DARK) + (215,))

    # ── CTA ──
    if cta_style in ("button", "pill"):
        btn_dark = _zone_luminance(canvas, cta_box) < 118
        if cta_style == "pill":
            fill, tfill = SAND + (255,), DARK + (255,)
        else:
            fill = (CREAM + (255,)) if btn_dark else (DARK + (255,))
            tfill = (DARK + (255,)) if btn_dark else (CREAM + (255,))
        draw.rounded_rectangle(cta_box,
                               radius=int(cta_box[3] - cta_box[1]) // 2 if cta_style == "pill" else 14,
                               fill=fill)
        draw.text((cta_box[0] + 34, cta_box[1] + 16), cta_text, font=f_cta, fill=tfill)
    else:  # text_link — underline + a drawn arrow (no font-dependent glyph)
        link_dark = _zone_luminance(canvas, cta_box) < 118
        col = (CREAM if link_dark else DARK) + (255,)
        draw.text((cx, cy), cta_text, font=f_cta, fill=col)
        ay = cy + f_cta.size / 2 + 2
        ax0, ax1 = cx + cw + 14, cx + cw + 40
        draw.line([(ax0, ay), (ax1, ay)], fill=col, width=3)
        draw.line([(ax1 - 9, ay - 8), (ax1, ay), (ax1 - 9, ay + 8)], fill=col, width=3)
        draw.line([(cx, cy + f_cta.size + 8), (cx + cw, cy + f_cta.size + 8)], fill=col, width=3)

    Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB").save(
        out_path, format="PNG", optimize=True)
    print(f"      ✓ composited → {out_path.name}")


# ── Runner ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if "--proto" not in sys.argv:
        print(__doc__)
        sys.exit(0)
    dry = "--dry-run" in sys.argv
    recomp = "--recomposite" in sys.argv
    env = _load_env()
    api_key = env.get("GEMINI_API_KEY", "")
    ctx = _ssl_ctx(env)
    (OUT / "bg").mkdir(parents=True, exist_ok=True)

    for ad in PROTO_ADS:
        print(f"  [{ad['file']}]")
        if dry:
            print("      --- BACKGROUND PROMPT ---")
            print("      " + ad["bg_prompt"].replace("\n", "\n      "))
            continue
        bg = OUT / "bg" / ad["file"]
        if not bg.exists() and not recomp:
            if not api_key:
                print("      ✗ GEMINI_API_KEY missing"); sys.exit(1)
            print(f"      generating background ({BG_MODEL}) …")
            if not gen_background(ad["bg_prompt"], bg, api_key, ctx):
                print("      ✗ background failed — skipping"); continue
        if bg.exists():
            composite_ad(bg, ad, OUT / ad["file"])

    if not dry:
        print(f"\n  → {OUT}/   (grade with: python3 composite.py --proto --grade)")
    # optional grading pass over the composited finals
    if "--grade" in sys.argv and not dry:
        from evaluate import grade_image
        for ad in PROTO_ADS:
            f = OUT / ad["file"]
            if not f.exists():
                continue
            spec = {"format": "scene", "product_type": "blend",
                    "headline": ad["headline"].replace("\n", " "),
                    "subhead": ad.get("subhead", "")}
            v = grade_image(str(f), spec, api_key, ctx)
            mark = "✓" if v.get("overall_pass") else "✗"
            print(f"  {mark} {ad['file']}: {v.get('worst_issue', '?')}")
