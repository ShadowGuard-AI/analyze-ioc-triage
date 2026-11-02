#!/usr/bin/env python3
"""analyze-ioc-triage intro: the kelp forest alone and unnamed. Fronds at arm's length with amber bladders
beaded along a rising stem, the near flank of the sleeping otter entering from the right with one folded paw
and its looped anchor strand in sharp detail, the otter whole in the midground asleep on its back at the
surface, shafts of light standing in the water, a band of small fish hanging motionless heads all one way,
stems descending in rows into shadow blue deepening to near black, the canopy roof bright overhead, and two
gulls as pale shapes standing on the mat against the light. No letters, numerals, gauges, logos or screens."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(67)
V1 = "--v1" in sys.argv
W, H = 1200, 520
SHADOW = (14, 38, 62); GREEN = (22, 84, 52); AMBER = (216, 164, 60); PALE = (238, 226, 180)
img = Image.new("RGB", (W, H), SHADOW); d = ImageDraw.Draw(img, "RGBA")
# water deepening to near black at the bottom
for y in range(H):
    t = y / H; d.line([(0, y), (W, y)], fill=(int(18 - 10 * t), int(48 - 26 * t), int(74 - 34 * t)))
# canopy roof bright overhead: broad frond mat across the top
for _ in range(90):
    x, y = random.uniform(-20, W), random.uniform(-16, 74); r = random.uniform(22, 58)
    d.ellipse([x - r, y - r * .38, x + r, y + r * .38], fill=random.choice([(34, 110, 62), (46, 128, 66), (90, 130, 52)]))
for _ in range(36):  # amber lit edges where the mat meets the light
    x, y = random.uniform(0, W), random.uniform(30, 92); d.arc([x - 20, y - 8, x + 20, y + 8], 0, 180, fill=AMBER + (150,), width=3)
# two gulls as pale shapes standing on the mat against the light, no detail that could read as marks
for (x, y) in [(392, 44), (452, 38)]:
    d.ellipse([x - 17, y - 8, x + 17, y + 8], fill=(226, 228, 214)); d.ellipse([x + 12, y - 14, x + 24, y - 4], fill=(232, 234, 220))
    d.line([(x - 4, y + 8), (x - 4, y + 18)], fill=(190, 170, 110), width=2); d.line([(x + 6, y + 8), (x + 6, y + 18)], fill=(190, 170, 110), width=2)
# shafts of light standing in the water
for gx in (240, 520, 800):
    d.polygon([(gx, 60), (gx + 66, 60), (gx + 120, 470), (gx + 6, 470)], fill=(220, 226, 160, 26))
# stems descending in rows into the depths
for x in (90, 210, 350, 700, 860, 1010, 1120):
    d.line([(x, 70), (x - 14, 500)], fill=(18, 66, 42), width=7)
    for t in (.2, .45, .7):
        y = 70 + t * 400; d.ellipse([x - 16 - t * 4 - 8, y - 6, x - 16 - t * 4 + 8, y + 6], fill=AMBER)
# band of small fish hanging motionless beyond the otter, heads all one way
for i in range(9):
    x, y = 180 + i * 62, 300 + (i % 3) * 16
    d.polygon([(x, y), (x + 26, y - 7), (x + 34, y), (x + 26, y + 7)], fill=(150, 178, 168))
    d.polygon([(x + 30, y), (x + 40, y - 6), (x + 40, y + 6)], fill=(130, 158, 148))
# THE otter whole, midground: asleep on its back at the surface, kelp anchor looped in place
ox, oy = 620, 216
d.ellipse([ox - 118, oy - 46, ox + 118, oy + 46], fill=(96, 72, 52))  # body along the surface
d.ellipse([ox - 112, oy - 30, ox + 60, oy + 34], fill=(112, 86, 60))  # belly catching light
d.ellipse([ox - 150, oy - 38, ox - 104, oy + 26], fill=(104, 78, 54))  # head
d.ellipse([ox - 146, oy - 26, ox - 114, oy + 12], fill=(216, 196, 164))  # pale face turned up
d.ellipse([ox - 133, oy - 8, ox - 127, oy - 2], fill=(30, 24, 18))  # closed eye line only in shipped calm
d.polygon([(ox + 108, oy - 10), (ox + 148, oy - 26), (ox + 146, oy + 2)], fill=(88, 64, 44))  # tail
for fx in (ox + 84, ox + 102):  # crossed hind flippers
    d.ellipse([fx, oy + 22, fx + 30, oy + 38], fill=(84, 62, 42))
for fx in (ox - 62, ox - 34):  # forepaws folded on the chest
    d.ellipse([fx, oy - 20, fx + 22, oy - 2], fill=(88, 66, 46))
# kelp anchor: one amber strand looped loosely around the body, stem running down
d.arc([ox - 44, oy - 52, ox + 52, oy + 54], 300, 130, fill=AMBER, width=7)
d.line([(ox + 30, oy + 44), (ox + 52, 470)], fill=(26, 92, 54), width=6)
for t in (.3, .55, .8):
    y = oy + 60 + t * 330; d.ellipse([ox + 40 + t * 10 - 7, y - 5, ox + 40 + t * 10 + 7, y + 5], fill=AMBER)
# fronds spreading around the otter
for (x, y, a) in [(470, 250, 2.6), (770, 252, 0.5), (520, 160, -2.8), (740, 158, -0.3)]:
    for k in range(4):
        ex, ey = x + math.cos(a + k * .16) * 74, y + math.sin(a + k * .16) * 34
        d.line([(x, y), (ex, ey)], fill=(30, 102, 58), width=6)
# foreground fronds at arm's length, edges soft: one stem rising past the frame beaded with amber bladders
fg = Image.new("RGBA", (W, H), (0, 0, 0, 0)); fd = ImageDraw.Draw(fg)
fd.line([(66, 530), (96, -10)], fill=(28, 98, 56, 255), width=13)
for t in (.12, .3, .48, .66, .84):
    x, y = 66 + t * 30, 530 - t * 540; fd.ellipse([x - 11, y - 9, x + 11, y + 9], fill=AMBER + (255,))
for (x, y, a) in [(30, 470, -0.6), (1170, 480, 2.7), (1140, 90, 2.2)]:
    for k in range(5):
        ex, ey = x + math.cos(a + k * .2) * 120, y + math.sin(a + k * .2) * 60
        fd.line([(x, y), (ex, ey)], fill=(32, 106, 60, 255), width=10)
fg = fg.filter(ImageFilter.GaussianBlur(4)); img.paste(fg, (0, 0), fg); d = ImageDraw.Draw(img, "RGBA")
# near flank of the otter entering from the right: folded paw and looped strand in sharp detail
d.ellipse([1052, 300, 1210, 396], fill=(108, 82, 58))
d.ellipse([1072, 322, 1110, 356], fill=(88, 66, 46))  # one folded paw, sharp
d.arc([1046, 288, 1180, 404], 90, 260, fill=AMBER, width=8)  # the looped strand, sharp
if V1:  # draft 1 flaw: an extra otter pup face at the left, a second animal the prose forbids in frame
    d.ellipse([120, 330, 196, 392], fill=(104, 78, 54)); d.ellipse([136, 342, 180, 380], fill=(216, 196, 164))
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/intro-v1.png" if V1 else "intro-banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
