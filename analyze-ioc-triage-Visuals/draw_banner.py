#!/usr/bin/env python3
"""analyze-ioc-triage wordmark banner: canopy of a giant kelp forest when light arrives in shafts, camera
just under the surface looking along the bed. Tall stems rise from below the frame into a broad roof of
fronds in deep green and kelp amber, two gulls standing far back on the floating mat, an otter in the
foreground asleep wrapped in a frond with its face up into a shaft of green gold light, octopus arms curling
around a stem in the midground, coral branches in muted colour at the lower left, a slow procession of small
fish behind the otter. The name is lettered in Averia Libre in pale amber on the bright underside of the
canopy mat following the frond curve, one inscription only, no other writing in the forest."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(71)
V1 = "--v1" in sys.argv
W, H = 1200, 420
SHADOW = (14, 38, 62); GREEN = (22, 84, 52); AMBER = (216, 164, 60); PALEAMBER = (240, 208, 130)
img = Image.new("RGB", (W, H), SHADOW); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):
    t = y / H; d.line([(0, y), (W, y)], fill=(int(18 - 9 * t), int(50 - 24 * t), int(78 - 32 * t)))
# tall stems rising from depths below the frame
for x in (120, 260, 430, 700, 880, 1040, 1140):
    d.line([(x, H + 10), (x + 18, 66)], fill=(18, 68, 42), width=8)
    for t in (.3, .55, .8):
        y = H - t * (H - 70); d.ellipse([x + 4 - 7, y - 6, x + 4 + 7, y + 6], fill=AMBER)
# broad roof of fronds in deep green and kelp amber at the top
for _ in range(110):
    x, y = random.uniform(-20, W), random.uniform(-14, 66); r = random.uniform(24, 62)
    d.ellipse([x - r, y - r * .36, x + r, y + r * .36], fill=random.choice([(34, 110, 62), (46, 128, 66), (96, 132, 54), (140, 118, 44)]))
# shafts of green gold light
for gx in (330, 620, 920):
    d.polygon([(gx, 40), (gx + 60, 40), (gx + 110, 400), (gx + 4, 400)], fill=(224, 228, 160, 24))
# two gulls standing on the floating mat, far back and small
for (x, y) in [(806, 30), (850, 26)]:
    d.ellipse([x - 13, y - 6, x + 13, y + 6], fill=(228, 230, 216)); d.ellipse([x + 9, y - 11, x + 19, y - 3], fill=(234, 236, 222))
    d.line([(x - 3, y + 6), (x - 3, y + 14)], fill=(190, 170, 110), width=2); d.line([(x + 5, y + 6), (x + 5, y + 14)], fill=(190, 170, 110), width=2)
# name on the water: lettered along the curve of the largest frond's bright underside, one inscription only
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/AveriaLibre.ttf", 27)
except Exception:
    f = ImageFont.load_default()
name = "analyze-ioc-triage"
if V1:  # draft 1 flaw: name in a straight line across the middle of the water, a sign not a frond inscription
    d.text((600, 210), name, font=f, fill=PALEAMBER, anchor="mm")
else:
    cx, cy, R = 600, -330, 428
    n = len(name); a0, a1 = 58, 122
    for i, ch in enumerate(name):
        a = math.radians(a0 + (a1 - a0) * (i / max(1, n - 1)))
        x, y = cx + math.cos(a) * R, cy + math.sin(a) * R
        d.text((x, y), ch, font=f, fill=PALEAMBER, anchor="mm")
# coral branches in muted colour holding the lower left corner, fixed still
for (bx, by) in [(60, 400), (110, 408), (160, 402)]:
    for a, ln in [(-1.5, 52), (-1.1, 40), (-1.9, 38)]:
        ex, ey = bx + math.cos(a) * ln, by + math.sin(a) * ln
        d.line([(bx, by), (ex, ey)], fill=(168, 104, 96), width=6)
        d.line([(ex, ey), (ex + 12, ey - 14)], fill=(178, 116, 104), width=4)
# octopus arms curling around a stem in the midground, curling and letting go
for (cx0, cy0) in [(700, 262), (716, 308)]:
    for k in range(4):
        a = k * 1.35; x, y = cx0 + math.cos(a) * 26, cy0 + math.sin(a) * 17
        d.ellipse([x - 9, y - 8, x + 9, y + 8], fill=(150, 96, 88))
d.line([(700, 240), (700, 330)], fill=(18, 68, 42), width=8)
# slow procession of small fish crossing behind the otter
for i in range(8):
    x, y = 420 + i * 58, 268 + (i % 2) * 14
    d.polygon([(x, y), (x + 24, y - 6), (x + 32, y), (x + 24, y + 6)], fill=(148, 176, 166))
# foreground otter asleep wrapped in a frond, face turned up into the shaft of light
ox, oy = 330, 286
d.ellipse([ox - 108, oy - 42, ox + 108, oy + 42], fill=(98, 74, 52))
d.ellipse([ox - 100, oy - 26, ox + 56, oy + 30], fill=(114, 88, 62))
d.ellipse([ox - 138, oy - 34, ox - 96, oy + 22], fill=(106, 80, 56))
d.ellipse([ox - 134, oy - 22, ox - 104, oy + 10], fill=(220, 200, 168))  # pale face up into the light
for fx in (ox - 54, ox - 28):
    d.ellipse([fx, oy - 18, fx + 20, oy], fill=(88, 66, 46))
d.arc([ox - 40, oy - 48, ox + 48, oy + 50], 300, 130, fill=AMBER, width=7)  # wrapped frond strand
for k in range(4):  # the wrapping frond itself spreading from the otter
    a = .4 + k * .3; d.line([(ox + 30, oy + 20), (ox + 30 + math.cos(a) * 84, oy + 20 + math.sin(a) * 40)], fill=(30, 104, 58), width=7)
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/banner-v1.png" if V1 else "banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
