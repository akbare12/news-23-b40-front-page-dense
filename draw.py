#!/usr/bin/env python3
"""news-23 b40 front-page-dense: draw THE WORLD TODAY, Monday 23 November 2026."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (212, 175, 55)
DARKGOLD = (176, 141, 30)
RED = (200, 30, 30)
NAVY = (10, 35, 90)
TEAL = (0, 148, 136)
PURPLE = (118, 66, 168)
GREEN = (34, 139, 60)
GRAY = (96, 96, 96)
LGRAY = (232, 232, 232)
CREAM = (250, 244, 224)
MAPBG = (198, 220, 240)
LAND = (139, 199, 120)
DARKNAVY = (8, 24, 64)

def fb(sz):
    return ImageFont.truetype(BOLD, sz)

def fr(sz):
    return ImageFont.truetype(REG, sz)

def wrap(d, text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def chip(d, right_edge, y, text, fill):
    f = fb(9)
    tw = d.textlength(text, font=f)
    x = right_edge - (tw + 10)
    d.rectangle([x, y, right_edge, y + 14], fill=fill)
    d.text((x + 5, y + 2), text, font=f, fill=WHITE)
    return tw + 10

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 56], fill=BLACK)
d.text((12, 8), "THE WORLD TODAY", font=fb(40), fill=WHITE)
t = "MONDAY 23 NOVEMBER 2026"
d.text((W - 12 - d.textlength(t, font=fb(19)), 17), t, font=fb(19), fill=GOLD)

# ---- kicker ----
kick = "AI rout hits Asia  \u00b7  UN chief urges AI rules  \u00b7  US lead over China at record low  \u00b7  Anthropic IPO $107.3B"
d.text((12, 62), kick, font=fb(15), fill=RED)

# ---- number strip: 5 cols x 2 rows ----
nums = [
    ("-3.3%", RED, "KOSPI"),
    ("5.3", NAVY, "US-CHINA POWER GAP"),
    ("11,762", GREEN, "EBOLA CASES, DRC"),
    ("10T won", DARKGOLD, "SEOUL STABILISATION FUND"),
    ("2%", PURPLE, "BILLIONAIRE TAX IN PARIS"),
    ("$450M", PURPLE, "SKUBAL DEAL"),
    ("165", RED, "RUSSIAN MISSILES IN A WEEK"),
    ("12,000", NAVY, "CLEARED IN MANCHESTER"),
    ("264 kg", DARKGOLD, "EXPLOSIVES SEIZED IN LEBANON"),
    ("$107.3B", PURPLE, "ANTHROPIC IPO \u2014 LARGEST"),
]
colw = 204
for i, (num, col, lab) in enumerate(nums):
    cx = 12 + (i % 5) * colw
    cy = 88 + (i // 5) * 36
    d.text((cx, cy), num, font=fb(21), fill=col)
    d.text((cx, cy + 23), lab, font=fb(9), fill=BLACK)

# ---- region bar ----
regs = [("ASIA-PACIFIC 7", 7, TEAL), ("AMERICAS 8", 8, NAVY),
        ("MIDDLE EAST 6", 6, DARKGOLD), ("EUROPE 5", 5, PURPLE),
        ("AFRICA 3", 3, RED), ("WORLD 2", 2, GRAY)]
rx = 0
tot = sum(c for _, c, _ in regs)
for name, cnt, col in regs:
    segw = int(round(W * cnt / tot))
    d.rectangle([rx, 164, rx + segw, 186], fill=col)
    f = fb(11)
    tw = d.textlength(name, font=f)
    d.text((rx + (segw - tw) / 2, 169), name, font=f, fill=WHITE)
    rx += segw

# ---- UTC strip ----
d.rectangle([0, 188, W, 208], fill=NAVY)
utc = "THE DAY IN UTC   ~00:00 Kospi dives   ~06:30 Guterres opens   ~09:00 Power Index   ~12:00 Paris 2% tax   ~15:00 Kyiv missiles   ~18:00 IPO $97.17"
d.text((12, 192), utc, font=fr(11), fill=WHITE)
ap = "~ APPROX"
d.text((W - 12 - d.textlength(ap, font=fr(11)), 192), ap, font=fr(11), fill=(180, 200, 230))

# ---- hero scenes ----
HX = [8, 348, 688]
HW = 328
HY = 212
# hero 1: Kospi chart
x = HX[0]
d.rectangle([x, HY, x + HW, HY + 128], fill=DARKNAVY)
d.text((x + 10, HY + 6), "-3.3%", font=fb(30), fill=(255, 90, 70))
# skyline
import random
random.seed(40)
bx = x + 8
while bx < x + HW - 14:
    bw = random.randint(16, 30)
    bh = random.randint(24, 52)
    d.rectangle([bx, HY + 128 - bh, bx + bw, HY + 128], fill=(24, 48, 96))
    for wy in range(HY + 128 - bh + 6, HY + 122, 12):
        for wx in range(bx + 4, bx + bw - 4, 9):
            if random.random() < 0.6:
                d.rectangle([wx, wy, wx + 4, wy + 5], fill=(255, 214, 90))
    bx += bw + 4
# red line chart
pts = [(x + 12, HY + 78), (x + 60, HY + 64), (x + 110, HY + 74), (x + 160, HY + 56),
       (x + 210, HY + 68), (x + 260, HY + 52), (x + 315, HY + 62)]
d.line(pts, fill=(255, 80, 60), width=3)
for px, py in pts:
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 214, 90))
d.rectangle([x, HY + 128, x + HW, HY + 144], fill=BLACK)
d.text((x + 8, HY + 131), "KOSPI 4,708.54  \u00b7  -161 PTS", font=fb(12), fill=WHITE)

# hero 2: Guterres
x = HX[1]
d.rectangle([x, HY, x + HW, HY + 128], fill=TEAL)
d.text((x + 10, HY + 8), "150 DELEGATES", font=fb(27), fill=GOLD)
d.text((x + 10, HY + 40), "BACK A RISK", font=fb(27), fill=WHITE)
d.text((x + 10, HY + 72), "FRAMEWORK", font=fb(27), fill=WHITE)
# globe top-right
gx, gy, gr = x + HW - 42, HY + 22, 20
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(190, 235, 225))
d.ellipse([gx - gr + 4, gy - gr + 4, gx + gr - 4, gy + gr - 4], outline=(0, 120, 110), width=2)
d.line([gx - gr + 4, gy, gx + gr - 4, gy], fill=(0, 120, 110), width=1)
d.line([gx, gy - gr + 4, gx, gy + gr - 4], fill=(0, 120, 110), width=1)
d.rectangle([x, HY + 128, x + HW, HY + 144], fill=BLACK)
d.text((x + 8, HY + 131), "UN  \u00b7  BRIDGETOWN", font=fb(12), fill=WHITE)

# hero 3: power index bars
x = HX[2]
d.rectangle([x, HY, x + HW, HY + 128], fill=CREAM)
d.text((x + 10, HY + 6), "NARROWEST SINCE 2018", font=fb(12), fill=BLACK)
d.text((x + HW - 8 - d.textlength("GAP 5.3", font=fb(12)), HY + 6), "GAP 5.3", font=fb(12), fill=DARKGOLD)
bars = [("78.9", NAVY, 92), ("73.6", RED, 86), ("40.5", DARKGOLD, 52)]
labels = ["US", "CHINA", "INDIA"]
base = HY + 112
for i, ((val, col, bh), lab) in enumerate(zip(bars, labels)):
    bx = x + 22 + i * 106
    d.rectangle([bx, base - bh, bx + 62, base], fill=col)
    d.text((bx + 31 - d.textlength(val, font=fb(15)) / 2, base - bh + 8), val, font=fb(15), fill=WHITE)
    d.text((bx + 31 - d.textlength(lab, font=fb(11)) / 2, base + 2, ), lab, font=fb(11), fill=BLACK)
d.rectangle([x, HY + 128, x + HW, HY + 144], fill=BLACK)
d.text((x + 8, HY + 131), "ASIA POWER INDEX 2026", font=fb(12), fill=WHITE)

# hero headlines + bodies
heroes = [
    (HX[0], "1", "AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE", "REPORTED", NAVY),
    (HX[1], "2", "GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 delegates back a risk framework.",
     "UNITED NATIONS", "REPORTED", NAVY),
    (HX[2], "3", "US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 \u2014 gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE", "REPORTED", NAVY),
]
for x, num, head, body, src, chiptext, chipcol in heroes:
    y = HY + 150
    d.ellipse([x, y + 2, x + 18, y + 20], fill=RED)
    d.text((x + 6, y + 3), num, font=fb(12), fill=WHITE)
    hl = wrap(d, head, fb(16), HW - 26)
    yy = y
    for ln in hl[:2]:
        d.text((x + 24, yy), ln, font=fb(16), fill=BLACK)
        yy += 19
    by = y + 40
    bl = wrap(d, body, fr(11), HW - 4)
    for ln in bl[:2]:
        d.text((x, by), ln, font=fr(11), fill=BLACK)
        by += 14
    sy = y + 70
    d.text((x, sy + 1), src, font=fr(10), fill=GRAY)
    chip(d, x + HW, sy, chiptext, chipcol)

# ---- MORE OF THE DAY ----
d.rectangle([0, 450, W, 470], fill=BLACK)
d.text((12, 454), "MORE OF THE DAY  \u2014  10 STORIES", font=fb(13), fill=WHITE)

cards = [
    ("AMERICAS", TEAL, "BESSENT: NVIDIA ANSWERS", "Treasury chief wants China answers.", "Reuters", "REPORTED", NAVY),
    ("FBI", PURPLE, "FBI PROBES NCIC HACK", "Hackers hit police NCIC database.", "AP", "REPORTED", NAVY),
    ("WHITE HOUSE", DARKGOLD, "TRUMP: IRAN STRIKES MAY RESUME", "Strikes may resume in New Year.", "Reuters", "REPORTED", NAVY),
    ("MARKETS", GREEN, "US FUTURES JUMP 3%", "Holiday rally lifts futures 3%.", "Bloomberg", "REPORTED", NAVY),
    ("SPORT", RED, "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED", NAVY),
    ("SPORT", RED, "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice, dies.", "ESPN", "REPORTED", NAVY),
    ("LEGAL", PURPLE, "STATES SUE SPACEX", "Ten states challenge AI claims.", "AP", "REPORTED", NAVY),
    ("TECH", NAVY, "ANTHROPIC IPO: $107.3B", "Raised at $83; closes $97.17.", "WSJ", "REPORTED", NAVY),
    ("EUROPE", DARKGOLD, "POLAND: 3 MISSILES CROSSED AIRSPACE", "Kyiv: three Kh-101s crossed.", "AP", "CLAIM", RED),
    ("SPACE", GRAY, "RUSSIAN NUCLEAR SATELLITE", "Intel: satellite may carry a nuke.", "Reuters", "CLAIM", RED),
]
CW = 200
for i, (cat, ccol, head, body, src, chiptext, chipcol) in enumerate(cards):
    cx = 8 + (i % 5) * 204
    cy = 476 + (i // 5) * 78
    d.rectangle([cx, cy, cx + CW, cy + 14], fill=ccol)
    d.text((cx + 4, cy + 1), cat, font=fb(10), fill=WHITE)
    n = str(i + 1)
    d.text((cx + CW - 6 - d.textlength(n, font=fb(10)), cy + 1), n, font=fb(10), fill=WHITE)
    hl = wrap(d, head, fb(12), CW - 6)
    yy = cy + 17
    for ln in hl[:2]:
        d.text((cx, yy), ln, font=fb(12), fill=BLACK)
        yy += 14
    by = cy + 17 + 30
    d.text((cx, by), body, font=fr(10), fill=BLACK)
    sy = cy + 17 + 30 + 15
    d.text((cx, sy + 1), src, font=fr(9), fill=GRAY)
    chip(d, cx + CW, sy, chiptext, chipcol)

# ---- map + ALSO ----
d.rectangle([0, 638, W, 658], fill=BLACK)
d.text((12, 642), "WHERE IT HAPPENED", font=fb(13), fill=WHITE)
d.text((348, 642), "ALSO ON MONDAY", font=fb(13), fill=WHITE)

# map
mx, my, mw, mh = 8, 664, 322, 148
d.rectangle([mx, my, mx + mw, my + mh], fill=MAPBG)
for gx in range(mx, mx + mw, 16):
    d.line([gx, my, gx, my + mh], fill=(175, 205, 230), width=1)
for gy in range(my, my + mh, 16):
    d.line([mx, gy, mx + mw, gy], fill=(175, 205, 230), width=1)
# continents (stylised blobs)
d.ellipse([mx + 18, my + 12, mx + 118, my + 78], fill=LAND)   # N America
d.ellipse([mx + 82, my + 82, mx + 128, my + 132], fill=LAND)  # S America
d.ellipse([mx + 168, my + 8, mx + 212, my + 40], fill=LAND)   # Europe
d.ellipse([mx + 168, my + 46, mx + 216, my + 104], fill=LAND) # Africa
d.ellipse([mx + 218, my + 8, mx + 306, my + 66], fill=LAND)   # Asia
d.ellipse([mx + 252, my + 92, mx + 300, my + 122], fill=LAND) # Australia
pins = [(288, 26), (96, 96), (272, 20), (52, 30), (72, 24), (214, 34),
        (42, 20), (28, 36), (52, 46), (58, 56), (192, 16), (208, 20), (228, 12)]
for i, (px, py) in enumerate(pins, 1):
    d.ellipse([mx + px - 8, my + py - 8, mx + px + 8, my + py + 8], fill=RED, outline=WHITE, width=1)
    n = str(i)
    d.text((mx + px - d.textlength(n, font=fb(9)) / 2, my + py - 6), n, font=fb(9), fill=WHITE)
d.text((mx, my + mh + 4), "Pins 1\u201313: 1 Seoul \u00b7 2 Bridgetown \u00b7 3 Beijing", font=fr(9), fill=BLACK)
d.text((mx, my + mh + 17), "4 Washington \u00b7 5 New York \u00b7 6 Tehran \u00b7 7 Chicago", font=fr(9), fill=BLACK)
d.text((mx, my + mh + 30), "8 San Francisco \u00b7 9 Denver \u00b7 10 Austin \u00b7 11 Warsaw \u00b7 12 Kyiv \u00b7 13 Moscow", font=fr(9), fill=BLACK)

also_l = [
    "14. Paris: 100+ back 2% billionaire tax",
    "15. Manchester: 12,000 cleared",
    "16. Zelenskyy: 165 missiles in a week",
    "17. COP31: the day after pact rejected",
    "18. Benghazi: UN demands port probe",
    "19. Israel unity talks resume",
    "20. Gaza: two killed in Israeli strike",
    "21. West Bank settler attacks",
    "22. Iran war: no deal in sight",
]
also_r = [
    "23. Lebanon seizes 264 kg explosives",
    "24. Bahrain: strike hits plant, 2 hurt",
    "25. Sudan: defences down drones",
    "26. DRC: fighting traps Ebola teams",
    "27. Bangladesh: Hasina jailed if she returns",
    "28. Seoul minister quits in exam row",
    "29. SK Telecom -7.3% as hype cools",
    "30. China eases margin rules",
    "31. Seoul readies 10T-won fund",
]
for i, t in enumerate(also_l):
    d.text((348, 664 + i * 17), t, font=fr(11), fill=BLACK)
for i, t in enumerate(also_r):
    d.text((688, 664 + i * 17), t, font=fr(11), fill=BLACK)

# ---- DATE CHECK ----
dx, dy, dw, dh = 8, 854, W - 16, 84
d.rectangle([dx, dy, dx + dw, dy + dh], outline=RED, width=2)
d.text((dx + 8, dy + 5), "DATE CHECK", font=fb(14), fill=RED)
rt = "READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY"
d.text((dx + dw - 8 - d.textlength(rt, font=fb(9)), dy + 7), rt, font=fb(9), fill=RED)
left = "LEFT OUT \u2014 NOT 23 NOV: Democrats reach 258 seats (22 Nov) \u00b7 Sparta II fire (22 Nov) \u00b7 El Chapo Isidro captured (22 Nov) \u00b7 EU-Indonesia pact (21 Nov) \u00b7 Nigeria boat (21 Nov) \u00b7 ICJ Myanmar ruling (19 Nov)"
ll = wrap(d, left, fr(11), dw - 16)
yy = dy + 24
for ln in ll[:2]:
    d.text((dx + 8, yy), ln, font=fr(11), fill=BLACK)
    yy += 15
ny = "NOT YET: Dymer search continues (14 missing) \u00b7 4 House races uncalled \u00b7 COP32 venue not set \u00b7 WHO evacuating trapped Ebola staff"
d.text((dx + 8, yy + 2), ny, font=fr(11), fill=BLACK)

# ---- footer ----
d.text((12, 944), "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 AFP \u00b7 Yonhap \u00b7 BBC \u00b7 WSJ \u00b7 NYT \u00b7 ESPN \u00b7 Lowy Institute (Asia Power Index 2026).", font=fr(10), fill=GRAY)
d.text((12, 958), "CHIPS: REPORTED = confirmed by wires \u00b7 CLAIM = one side's claim, not independently confirmed \u00b7 ONGOING = still developing", font=fr(10), fill=GRAY)
ft = "Scenes are drawn illustrations, not photographs.  \u00b7  THE WORLD TODAY  \u2014  Monday 23 November 2026  \u00b7  31 stories  \u00b7  6 regions"
d.rectangle([0, 972, W, H], fill=BLACK)
d.text(((W - d.textlength(ft, font=fb(12))) / 2, 986), ft, font=fb(12), fill=GOLD)

img.save("entry.png")
print("saved entry.png", img.size)
