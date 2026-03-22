#!/usr/bin/env python3
"""
Generate avatar for 杨满满 - warm, intimate, design-forward
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

FONT_DIR = "/Users/yangyuan/.catpaw/skills/skills-market-external/canvas-design/canvas-fonts"
OUTPUT = "/Users/yangyuan/Documents/GitHub/Notebook/小红书/杨满满头像.png"

SIZE = 800
img = Image.new("RGB", (SIZE, SIZE), "#F5EDE3")
draw = ImageDraw.Draw(img)

# ── Color palette ──────────────────────────────────────────────
CREAM       = "#F5EDE3"
WARM_SAND   = "#E8D5C0"
TERRACOTTA  = "#C4714A"
DUSTY_ROSE  = "#D4907A"
MUTED_SAGE  = "#8FA68A"
DEEP_BROWN  = "#4A3728"
SOFT_PEACH  = "#EAC4A8"
LIGHT_SAGE  = "#B8CCAA"

# ── Background: layered warm circles ──────────────────────────
def draw_circle(draw, cx, cy, r, color, alpha=None):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)

# Soft background blobs
draw_circle(draw, 400, 380, 320, WARM_SAND)
draw_circle(draw, 420, 360, 280, "#EDD9C5")

# ── Botanical elements (leaves) ────────────────────────────────
def draw_leaf(draw, cx, cy, length, angle_deg, color, width=18):
    import math
    angle = math.radians(angle_deg)
    # stem
    ex = cx + math.cos(angle) * length
    ey = cy + math.sin(angle) * length
    draw.line([(cx, cy), (ex, ey)], fill=color, width=3)
    # leaf shape as ellipse rotated
    for t in [0.3, 0.5, 0.7]:
        mx = cx + math.cos(angle) * length * t
        my = cy + math.sin(angle) * length * t
        perp = angle + math.pi/2
        lw = width * math.sin(math.pi * t) * 1.5
        lx = math.cos(perp) * lw
        ly = math.sin(perp) * lw
        draw.ellipse([mx-lw, my-lw*0.4, mx+lw, my+lw*0.4], fill=color)

# Leaves around the composition
leaf_positions = [
    (155, 200, 90, -50, MUTED_SAGE),
    (130, 240, 70, -80, LIGHT_SAGE),
    (170, 170, 60, -20, MUTED_SAGE),
    (620, 190, 85, -130, MUTED_SAGE),
    (650, 230, 65, -100, LIGHT_SAGE),
    (600, 165, 55, -160, MUTED_SAGE),
    (160, 580, 75, 40, LIGHT_SAGE),
    (630, 590, 80, 140, MUTED_SAGE),
    (400, 680, 60, 90, LIGHT_SAGE),
    (350, 695, 50, 110, MUTED_SAGE),
    (450, 690, 55, 70, LIGHT_SAGE),
]
for lx, ly, ll, la, lc in leaf_positions:
    draw_leaf(draw, lx, ly, ll, la, lc)

# ── Small decorative dots ──────────────────────────────────────
dot_positions = [
    (200, 130, 5, DUSTY_ROSE),
    (580, 120, 4, TERRACOTTA),
    (650, 400, 3, DUSTY_ROSE),
    (140, 450, 4, TERRACOTTA),
    (480, 710, 4, DUSTY_ROSE),
    (310, 720, 3, MUTED_SAGE),
    (100, 350, 3, LIGHT_SAGE),
    (700, 300, 4, SOFT_PEACH),
]
for dx, dy, dr, dc in dot_positions:
    draw.ellipse([dx-dr, dy-dr, dx+dr, dy+dr], fill=dc)

# ── Main face circle ───────────────────────────────────────────
face_cx, face_cy = 400, 360
face_r = 195

# Shadow layer
shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
shadow_draw = ImageDraw.Draw(shadow)
shadow_draw.ellipse(
    [face_cx - face_r + 8, face_cy - face_r + 8,
     face_cx + face_r + 8, face_cy + face_r + 8],
    fill=(74, 55, 40, 40)
)
shadow = shadow.filter(ImageFilter.GaussianBlur(18))
img.paste(shadow, mask=shadow.split()[3])
draw = ImageDraw.Draw(img)

# Face background
draw.ellipse(
    [face_cx - face_r, face_cy - face_r,
     face_cx + face_r, face_cy + face_r],
    fill=SOFT_PEACH
)

# Subtle skin tone gradient via layered circles
for i in range(8):
    r = face_r - i * 4
    alpha_val = 15 - i
    overlay = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.ellipse(
        [face_cx - r, face_cy - r - 10,
         face_cx + r, face_cy + r - 10],
        fill=(234, 196, 168, alpha_val * 3)
    )
    img.paste(overlay, mask=overlay.split()[3])
    draw = ImageDraw.Draw(img)

# ── Hair ───────────────────────────────────────────────────────
hair_color = "#3D2B1F"
# Top hair mass
draw.ellipse(
    [face_cx - 175, face_cy - 210,
     face_cx + 175, face_cy + 20],
    fill=hair_color
)
# Side hair left
draw.ellipse(
    [face_cx - 200, face_cy - 160,
     face_cx - 80, face_cy + 80],
    fill=hair_color
)
# Side hair right
draw.ellipse(
    [face_cx + 80, face_cy - 160,
     face_cx + 200, face_cy + 80],
    fill=hair_color
)
# Hair highlight
draw.ellipse(
    [face_cx - 60, face_cy - 195,
     face_cx + 40, face_cy - 130],
    fill="#5C3D2A"
)

# ── Face skin (re-draw over hair bottom) ──────────────────────
draw.ellipse(
    [face_cx - 145, face_cy - 130,
     face_cx + 145, face_cy + 155],
    fill=SOFT_PEACH
)

# ── Eyes ───────────────────────────────────────────────────────
eye_y = face_cy - 10
eye_lx, eye_rx = face_cx - 48, face_cx + 48

# Eye whites
draw.ellipse([eye_lx-18, eye_y-10, eye_lx+18, eye_y+10], fill="white")
draw.ellipse([eye_rx-18, eye_y-10, eye_rx+18, eye_y+10], fill="white")

# Irises
draw.ellipse([eye_lx-11, eye_y-11, eye_lx+11, eye_y+11], fill="#3D2B1F")
draw.ellipse([eye_rx-11, eye_y-11, eye_rx+11, eye_y+11], fill="#3D2B1F")

# Pupils
draw.ellipse([eye_lx-6, eye_y-6, eye_lx+6, eye_y+6], fill="#1A1008")
draw.ellipse([eye_rx-6, eye_y-6, eye_rx+6, eye_y+6], fill="#1A1008")

# Eye shine
draw.ellipse([eye_lx+3, eye_y-7, eye_lx+8, eye_y-2], fill="white")
draw.ellipse([eye_rx+3, eye_y-7, eye_rx+8, eye_y-2], fill="white")

# Eyelashes / upper lid line
draw.arc([eye_lx-20, eye_y-13, eye_lx+20, eye_y+5], 200, 340, fill=DEEP_BROWN, width=3)
draw.arc([eye_rx-20, eye_y-13, eye_rx+20, eye_y+5], 200, 340, fill=DEEP_BROWN, width=3)

# ── Eyebrows ───────────────────────────────────────────────────
brow_y = eye_y - 28
draw.arc([eye_lx-22, brow_y-8, eye_lx+22, brow_y+8], 200, 340, fill=DEEP_BROWN, width=4)
draw.arc([eye_rx-22, brow_y-8, eye_rx+22, brow_y+8], 200, 340, fill=DEEP_BROWN, width=4)

# ── Nose ───────────────────────────────────────────────────────
nose_y = face_cy + 30
draw.arc([face_cx-14, nose_y-5, face_cx+14, nose_y+12], 0, 180, fill="#C4907A", width=2)
draw.ellipse([face_cx-16, nose_y+2, face_cx-8, nose_y+10], fill="#D4A090")
draw.ellipse([face_cx+8, nose_y+2, face_cx+16, nose_y+10], fill="#D4A090")

# ── Mouth ──────────────────────────────────────────────────────
mouth_y = face_cy + 68
# Upper lip
draw.arc([face_cx-28, mouth_y-10, face_cx, mouth_y+6], 200, 340, fill=TERRACOTTA, width=3)
draw.arc([face_cx, mouth_y-10, face_cx+28, mouth_y+6], 200, 340, fill=TERRACOTTA, width=3)
# Lower lip / smile
draw.arc([face_cx-26, mouth_y-4, face_cx+26, mouth_y+18], 10, 170, fill=TERRACOTTA, width=3)
# Lip fill
draw.ellipse([face_cx-24, mouth_y-2, face_cx+24, mouth_y+14], fill=DUSTY_ROSE)
draw.arc([face_cx-26, mouth_y-6, face_cx+26, mouth_y+16], 10, 170, fill=TERRACOTTA, width=2)

# ── Cheek blush ────────────────────────────────────────────────
blush = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
blush_draw = ImageDraw.Draw(blush)
blush_draw.ellipse([face_cx-130, face_cy+10, face_cx-60, face_cy+55], fill=(212, 144, 122, 60))
blush_draw.ellipse([face_cx+60, face_cy+10, face_cx+130, face_cy+55], fill=(212, 144, 122, 60))
blush = blush.filter(ImageFilter.GaussianBlur(14))
img.paste(blush, mask=blush.split()[3])
draw = ImageDraw.Draw(img)

# ── Neck & shoulders ──────────────────────────────────────────
neck_color = SOFT_PEACH
draw.rectangle([face_cx-30, face_cy+148, face_cx+30, face_cy+210], fill=neck_color)
# Shoulders
draw.ellipse([face_cx-160, face_cy+180, face_cx+160, face_cy+320], fill="#C4714A")
# Collar detail
draw.arc([face_cx-40, face_cy+195, face_cx+40, face_cy+240], 0, 180, fill="#A85A35", width=2)

# ── Decorative ring around face ────────────────────────────────
ring_r = face_r + 18
draw.arc(
    [face_cx - ring_r, face_cy - ring_r,
     face_cx + ring_r, face_cy + ring_r],
    30, 150, fill=TERRACOTTA, width=2
)
draw.arc(
    [face_cx - ring_r, face_cy - ring_r,
     face_cx + ring_r, face_cy + ring_r],
    210, 330, fill=DUSTY_ROSE, width=2
)

# ── Small star/sparkle accents ─────────────────────────────────
def draw_sparkle(draw, cx, cy, size, color):
    for angle in [0, 45, 90, 135]:
        rad = math.radians(angle)
        x1 = cx + math.cos(rad) * size
        y1 = cy + math.sin(rad) * size
        x2 = cx - math.cos(rad) * size
        y2 = cy - math.sin(rad) * size
        draw.line([(x1, y1), (x2, y2)], fill=color, width=2)
    draw.ellipse([cx-3, cy-3, cx+3, cy+3], fill=color)

draw_sparkle(draw, 220, 155, 10, TERRACOTTA)
draw_sparkle(draw, 575, 148, 8, DUSTY_ROSE)
draw_sparkle(draw, 165, 510, 7, MUTED_SAGE)
draw_sparkle(draw, 620, 520, 9, TERRACOTTA)

# ── Typography: 杨满满 ─────────────────────────────────────────
try:
    from PIL import ImageFont
    # Use Italiana for elegant feel
    font_large = ImageFont.truetype(
        os.path.join(FONT_DIR, "Italiana-Regular.ttf"), 52
    )
    font_small = ImageFont.truetype(
        os.path.join(FONT_DIR, "InstrumentSerif-Italic.ttf"), 22
    )
    font_tiny = ImageFont.truetype(
        os.path.join(FONT_DIR, "Jura-Light.ttf"), 16
    )

    # Name in Chinese — draw character by character with spacing
    name = "杨满满"
    # Measure total width
    bbox = draw.textbbox((0, 0), name, font=font_large)
    tw = bbox[2] - bbox[0]
    tx = (SIZE - tw) // 2
    ty = face_cy + 230

    # Shadow
    draw.text((tx+2, ty+2), name, font=font_large, fill="#C4714A40")
    # Main text
    draw.text((tx, ty), name, font=font_large, fill=DEEP_BROWN)

    # Subtitle
    subtitle = "UX Designer · New Mom · AI Explorer"
    bbox2 = draw.textbbox((0, 0), subtitle, font=font_small)
    sw = bbox2[2] - bbox2[0]
    sx = (SIZE - sw) // 2
    draw.text((sx, ty + 62), subtitle, font=font_small, fill=TERRACOTTA)

    # Tiny tagline
    tagline = "满满折腾  满满收获"
    bbox3 = draw.textbbox((0, 0), tagline, font=font_tiny)
    tw3 = bbox3[2] - bbox3[0]
    draw.text(((SIZE - tw3) // 2, ty + 96), tagline, font=font_tiny, fill=MUTED_SAGE)

except Exception as e:
    print(f"Font error: {e}")

# ── Subtle vignette ────────────────────────────────────────────
vignette = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
vd = ImageDraw.Draw(vignette)
for i in range(60):
    alpha = int(i * 1.2)
    r = SIZE // 2 - i * 4
    if r > 0:
        vd.ellipse([SIZE//2 - r, SIZE//2 - r, SIZE//2 + r, SIZE//2 + r],
                   outline=(74, 55, 40, alpha), width=8)
vignette = vignette.filter(ImageFilter.GaussianBlur(20))
img.paste(vignette, mask=vignette.split()[3])

# ── Final soft warm overlay ────────────────────────────────────
warm_overlay = Image.new("RGBA", (SIZE, SIZE), (255, 220, 180, 18))
img = Image.alpha_composite(img.convert("RGBA"), warm_overlay).convert("RGB")

# ── Save ───────────────────────────────────────────────────────
img.save(OUTPUT, "PNG", quality=95)
print(f"Saved: {OUTPUT}")
