#!/usr/bin/env python3
"""analyze-ioc-triage logo: sea otter floating on its back at the surface of a kelp bed, drawn from slightly
above so animal, fronds and water read in one plane. Otter along a diagonal, forepaws folded on its chest,
hind flippers crossed, one kelp amber strand looped loosely around its body as its anchor against the drift.
Fronds spread outward in deep green with amber bladder beads along each stem, one abalone shell catching an
iridescent edge between two fronds at the lower edge. Water shadow blue darkening to the corners. Name
beneath in Averia Libre in kelp amber. If the loop vanishes the mark fails, so the loop is drawn last and bold."""
import math, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
V1 = "--v1" in sys.argv
W, H = 900, 560
SHADOW = (16, 42, 66); GREEN = (24, 92, 56); AMBER = (216, 164, 60)
img = Image.new("RGB", (W, H), SHADOW); d = ImageDraw.Draw(img, "RGBA")
# water darkening toward the corners
for (x, y, r) in [(0, 0, 260), (W, 0, 260), (0, H, 260), (W, H, 260)]:
    d.ellipse([x - r, y - r, x + r, y + r], fill=(10, 26, 44, 90))
# fronds spreading outward in deep green, bladders as amber beads along each stem
import random; random.seed(9)
cx, cy = 450, 208
for a_deg in range(0, 360, 24):
    a = math.radians(a_deg + random.uniform(-6, 6)); ln = random.uniform(120, 178)
    ex, ey = cx + math.cos(a) * ln, cy + math.sin(a) * ln * .78
    d.line([(cx, cy), (ex, ey)], fill=GREEN, width=8)
    for t in (.38, .62, .86):
        x, y = cx + (ex - cx) * t, cy + (ey - cy) * t
        d.ellipse([x - 7, y - 6, x + 7, y + 6], fill=AMBER)
    d.ellipse([ex - 16, ey - 7, ex + 16, ey + 7], fill=(30, 108, 62))
# the otter along a diagonal, drawn rotated by building on a layer and rotating
layer = Image.new("RGBA", (460, 240), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
ld.ellipse([70, 62, 390, 178], fill=(98, 74, 52))  # body
ld.ellipse([84, 82, 330, 168], fill=(114, 88, 62))  # belly
ld.ellipse([28, 78, 116, 168], fill=(106, 80, 56))  # head
ld.ellipse([40, 94, 100, 152], fill=(218, 198, 166))  # pale face
ld.ellipse([60, 112, 68, 120], fill=(28, 22, 16)); ld.ellipse([76, 126, 86, 133], fill=(40, 30, 20))  # eye, nose
ld.polygon([(378, 96), (428, 74), (424, 118)], fill=(88, 64, 44))  # tail
for fx in (330, 356):  # crossed hind flippers
    ld.ellipse([fx, 158, fx + 36, 180], fill=(84, 62, 42))
for fx in (150, 182):  # forepaws folded on the chest
    ld.ellipse([fx, 88, fx + 26, 112], fill=(88, 66, 46))
layer = layer.rotate(-14, expand=True, resample=Image.BICUBIC)
img.paste(layer, (222, 92), layer); d = ImageDraw.Draw(img, "RGBA")
if not V1:
    # the anchor loop: one kelp amber strand looped loosely around the body, drawn last and bold
    d.arc([cx - 74, cy - 66, cx + 88, cy + 72], 285, 135, fill=AMBER, width=9)
    d.line([(cx + 62, cy + 52), (cx + 96, cy + 118)], fill=(28, 98, 56), width=6)
    d.ellipse([cx + 88, cy + 104, cx + 104, cy + 120], fill=AMBER)
# one abalone shell between two fronds at the lower edge, iridescent edge of light
sx, sy = 330, 348
d.ellipse([sx - 34, sy - 16, sx + 34, sy + 16], fill=(70, 88, 84))
d.arc([sx - 34, sy - 16, sx + 34, sy + 16], 180, 340, fill=(150, 220, 210), width=4)
d.arc([sx - 26, sy - 11, sx + 26, sy + 11], 180, 340, fill=(226, 160, 200), width=3)
for i in range(5):
    d.ellipse([sx - 22 + i * 11, sy - 4, sx - 16 + i * 11, sy + 2], fill=(30, 40, 38))
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/AveriaLibre.ttf", 44)
except Exception:
    f = ImageFont.load_default()
d.text((450, 486), "analyze-ioc-triage", font=f, fill=AMBER, anchor="mm")
img = img.filter(ImageFilter.GaussianBlur(0.3))
out = "scratch/logo-v1.png" if V1 else "logo.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out)
if not V1:
    img.resize((103, 64)).save(__file__.rsplit("/", 1)[0] + "/scratch/logo64-ship.png")
print("saved", out)
