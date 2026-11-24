"""Draw the news-image-20261123 v2 front page (1024x1024).

Fresh code written for this version. All 31 stories were first reported
Monday 23 November 2026; nothing from any other day is included.
Fonts: Google Sans (OFL), four static weights under fonts/.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BASE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BASE, "fonts")

PAPER = (247, 243, 234)
INK = (20, 33, 61)
NAVY = (20, 33, 61)
RED = (179, 39, 30)
RED_DK = (140, 28, 22)
CARD = (255, 255, 255)
BORDER = (196, 198, 202)
MUTED = (90, 96, 110)
GOLD = (232, 181, 77)
OCEAN = (234, 241, 247)
LAND = (203, 213, 225)
LAND_LN = (100, 116, 139)

REGION_COLORS = {
    "Europe": (36, 86, 166),
    "Asia": (179, 39, 30),
    "Americas": (14, 124, 107),
    "Africa": (176, 118, 26),
    "Middle East": (108, 52, 131),
    "Global": (93, 109, 126),
    "Oceania": (46, 125, 50),
}

# (n, region, headline, deck, source, lon, lat) for leads + medium cards.
# Pins 1-13 appear on the map. All first reported 23 Nov 2026.
LEADS = [
    (1, "Europe", "Kyiv region strikes kill 11",
     "Monday strikes across the Kyiv region kill at least 11, including a "
     "teenager; a supermarket attack in Vyshneve kills 2 and injures 8.",
     "AP", 30.5, 50.4, "kyiv"),
    (2, "Americas", "Nvidia brings Huang back; shares jump 31%",
     "Board unanimously reinstates Jensen Huang as chief; shares jump about "
     "31% and the Nasdaq gains 6.5% as the AI sell-off reverses.",
     "REUTERS", -122.0, 37.4, "chip"),
    (3, "Global", "UN chief seeks global AI safety rules",
     "Guterres calls on states to agree a multilateral framework for AI risk "
     "within a year, at a Bridgetown summit on AI safety.",
     "AL JAZEERA", -59.6, 13.1, "globe"),
]

MEDIUM = [
    (4, "Global", "14 nations back World Court Rohingya ruling",
     "Fourteen foreign ministers acknowledge the court's genocide ruling; "
     "Britain formally recognises it and sanctions five generals.",
     "AFP", -0.1, 51.5),
    (5, "Middle East", "US eyes Iran in ship cyberattacks",
     "Washington probes suspected Iranian cyberattacks on up to 50 ships "
     "carrying oil and chemicals; four ships got US cyber teams.",
     "WSJ", 56.5, 26.5),
    (6, "Asia", "Nepal PM meets Modi in Delhi",
     "Nepal's prime minister meets Modi on his first bilateral visit abroad; "
     "energy, rail and hydropower on the table.",
     "THE HINDU", 77.2, 28.6),
    (7, "Asia", "More remains found after Indonesia factory fire",
     "Search resumes at the Cikande candy factory as more remains are found; "
     "34 workers are still missing.",
     "AP", 106.1, -6.1),
    (8, "Europe", "Poland: Russia twice tried to kill rapper",
     "Warsaw says Russia allegedly twice tried to kill a Ukrainian American "
     "rapper.",
     "AP", 21.0, 52.2),
    (9, "Europe", "EU proposes 22nd sanctions package on Russia",
     "The European Union proposes a new round of sanctions against Russia.",
     "ONETURN", 4.35, 50.85),
    (10, "Europe", "NATO Berlin meeting warns Russia",
     "NATO ends its Berlin meeting pledging to defend every inch of its "
     "territory, including in space.",
     "ONETURN", 13.4, 52.5),
    (11, "Americas", "Nine shot at California concert",
     "Nine people shot at a private concert in Strathmore; one is in "
     "critical condition.",
     "AP", -119.0, 36.1),
    (12, "Americas", "US stocks rebound after AI sell-off",
     "S&P 500 up 4.73% and Nasdaq up 6.5% on Monday; Japan's Nikkei falls "
     "5.06% and India's Sensex 1.77%.",
     "ONETURN", -74.0, 40.7),
    (13, "Africa", "Congo halts cobalt exports",
     "DR Congo, the world's top cobalt producer, will suspend cobalt exports "
     "from November 30 to tackle oversupply.",
     "REUTERS", 23.0, -3.0),
]

# (n, region, one-line headline, source) for the ALSO ON list.
BRIEFS = [
    (14, "Europe", "French factories shrink to six-month low", "REUTERS"),
    (15, "Europe", "German growth fastest since March 2022", "REUTERS"),
    (16, "Europe", "UK growth slows slightly; Q4 still robust", "REUTERS"),
    (17, "Asia", "India factory demand lifts PMI to 56.3", "REUTERS"),
    (18, "Asia", "Indian shares open higher on foreign inflows", "REUTERS"),
    (19, "Asia", "Kospi falls 3.31% to lowest since January", "REUTERS"),
    (20, "Asia", "Indonesia to name VP candidates Monday", "REUTERS"),
    (21, "Asia", "Eala tops win rate against top 10", "MANILA TIMES"),
    (22, "Americas", "Army to detonate five tons of unstable chemicals", "AP"),
    (23, "Americas", "US seeks answers on Nvidia chip sales to China", "REUTERS"),
    (24, "Americas", "Carney enlists fake Trump for dinner laughs", "AP"),
    (25, "Americas", "US business growth eases to 54.6", "REUTERS"),
    (26, "Africa", "SPLA-IO attack kills 24 civilians in South Sudan", "AFP"),
    (27, "Africa", "Fighting near Congo Ebola area disrupts response", "REUTERS"),
    (28, "Africa", "Kenya and DR Congo restore full ties", "ONETURN"),
    (29, "Oceania", "COP31 flop: blame game erupts in Australia", "REUTERS"),
    (30, "Middle East", "US sanctions Iran shadow banks", "REUTERS"),
    (31, "Middle East", "Iran says it downed US drone near Hormuz", "AL JAZEERA"),
]

STATS = [
    ("11", "KILLED IN KYIV\nREGION STRIKES"),
    ("+31%", "NVIDIA SHARES ON\nHUANG RETURN"),
    ("50", "SHIPS IN US\nCYBERATTACK PROBE"),
    ("14", "NATIONS BACK WORLD\nCOURT RULING"),
    ("34", "MISSING AFTER\nINDONESIA FIRE"),
    ("24", "KILLED IN SOUTH\nSUDAN ATTACK"),
]

REGION_STRIP = [("Europe", 7), ("Asia", 7), ("Americas", 7), ("Africa", 4),
                ("Middle East", 3), ("Global", 2), ("Oceania", 1)]

EXCLUDED = ("COP31 collapse \u00b7 Dymer drone strike \u00b7 Hormuz tanker "
            "attacks \u00b7 Skubal's $450m Mets deal \u00b7 Marquez eighth "
            "title \u00b7 Democrats' 258 House seats \u00b7 Miss Universe "
            "prelims")

# Rough continent outlines in (lon, lat). Stylised, recognisable at 300px.
CONTINENTS = [
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73), (-75, 62),
     (-55, 47), (-65, 45), (-75, 35), (-80, 25), (-90, 20), (-97, 16),
     (-105, 20), (-115, 30), (-125, 40), (-125, 49), (-145, 60), (-165, 60)],
    [(-80, 10), (-60, 8), (-50, 0), (-40, -5), (-35, -10), (-40, -20),
     (-48, -28), (-58, -35), (-65, -45), (-70, -55), (-73, -40), (-75, -20),
     (-80, -5)],
    [(-10, 36), (-5, 44), (0, 48), (5, 55), (10, 58), (18, 56), (25, 60),
     (30, 70), (40, 68), (45, 60), (30, 55), (25, 45), (20, 40), (15, 38),
     (10, 37), (0, 36)],
    [(-17, 15), (-10, 30), (0, 36), (10, 37), (20, 32), (30, 31), (35, 28),
     (40, 15), (48, 11), (51, 10), (45, 0), (40, -10), (35, -20), (30, -30),
     (20, -35), (15, -30), (12, -18), (9, -5), (9, 4), (-8, 5), (-15, 12)],
    [(40, 68), (60, 70), (80, 73), (110, 76), (140, 72), (160, 70),
     (170, 66), (160, 60), (140, 50), (130, 42), (127, 35), (122, 30),
     (115, 22), (108, 10), (105, 5), (100, 8), (95, 15), (90, 22), (85, 20),
     (80, 10), (75, 8), (70, 20), (60, 25), (50, 28), (45, 30), (40, 35)],
    [(113, -22), (125, -15), (135, -12), (142, -11), (150, -20), (153, -27),
     (150, -37), (140, -38), (130, -32), (120, -35), (113, -30)],
]

# Badge offsets (dx, dy in px) for clustered pins on the map.
BADGE_OFF = {4: (-36, -30), 9: (-8, -36), 10: (28, -32), 8: (40, -8),
             1: (36, 18), 2: (-16, -16), 11: (16, 12)}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


F = {
    "reg": lambda s: font("GoogleSans-Regular.ttf", s),
    "med": lambda s: font("GoogleSans-Medium.ttf", s),
    "semi": lambda s: font("GoogleSans-SemiBold.ttf", s),
    "bold": lambda s: font("GoogleSans-Bold.ttf", s),
}


def wrap(d, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def ellipsize(d, text, fnt, max_w):
    if d.textlength(text, font=fnt) <= max_w:
        return text
    while text and d.textlength(text + "\u2026", font=fnt) > max_w:
        text = text[:-1]
    return text + "\u2026"


def draw_art(d, kind, x, y, w, h):
    """Flat geometric vignette for a lead card (x, y, w, h box)."""
    if kind == "kyiv":
        d.rectangle([x, y, x + w, y + h], fill=(38, 52, 82))
        # buildings
        for bx, bw, bh in [(8, 34, 30), (48, 26, 38), (80, 40, 26),
                           (128, 30, 36), (164, 36, 28), (206, 28, 34),
                           (240, 34, 26), (272, 30, 30)]:
            d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h],
                        fill=(22, 30, 52))
            for wy in range(y + h - bh + 5, y + h - 4, 9):
                d.rectangle([x + bx + 5, wy, x + bx + 9, wy + 4],
                            fill=(232, 181, 77))
        # smoke plume + drone
        for cx, cy, r in [(150, 14, 9), (162, 8, 7), (138, 10, 6)]:
            d.ellipse([x + cx - r, y + cy - r, x + cx + r, y + cy + r],
                      fill=(120, 120, 128))
        d.polygon([(x + 268, y + 8), (x + 276, y + 12), (x + 268, y + 16),
                   (x + 260, y + 12)], fill=(10, 12, 20))
    elif kind == "chip":
        d.rectangle([x, y, x + w, y + h], fill=(16, 66, 46))
        # circuit traces
        for ty in (10, 24, 38):
            d.line([x + 8, y + ty, x + 90, y + ty], fill=(46, 160, 110),
                   width=2)
            d.ellipse([x + 88, y + ty - 3, x + 94, y + ty + 3],
                      fill=(46, 160, 110))
        # chip
        d.rectangle([x + 180, y + 6, x + 236, y + h - 6], fill=(240, 240, 235),
                    outline=(120, 200, 160), width=2)
        d.rectangle([x + 196, y + 12, x + 220, y + h - 12], fill=(16, 66, 46))
        d.text((x + 208, y + h // 2), "AI", font=F["bold"](13),
               fill=(120, 220, 170), anchor="mm")
        # rising arrow
        d.line([x + 250, y + h - 12, x + 272, y + 22, x + 288, y + 30,
                x + 306, y + 8], fill=(255, 255, 255), width=3)
        d.polygon([(x + 306, y + 8), (x + 296, y + 8), (x + 306, y + 18)],
                  fill=(255, 255, 255))
    else:  # globe
        d.rectangle([x, y, x + w, y + h], fill=(23, 68, 128))
        cx, cy, r = x + w // 2 - 40, y + h // 2, 20
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 190, 235),
                  outline=(255, 255, 255), width=2)
        d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(255, 255, 255),
              width=2)
        d.ellipse([cx - r - 14, cy - r - 8, cx + r + 14, cy + r + 8],
                  outline=(255, 255, 255), width=2)
        d.ellipse([cx + r + 26, cy - r - 2, cx + r + 32, cy - r + 4],
                  fill=(232, 181, 77))
        d.text((x + w - 78, y + h // 2), "AI RULES", font=F["bold"](15),
               fill=(255, 255, 255), anchor="lm")


def lead_card(d, x, y, w, h, n, region, headline, deck, source, art):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=BORDER, width=1)
    draw_art(d, art, x + 1, y + 1, w - 2, 46)
    # number badge on the art
    d.ellipse([x + 8, y + 8, x + 30, y + 30], fill=RED)
    d.text((x + 19, y + 19), str(n), font=F["bold"](13), fill=(255, 255, 255),
           anchor="mm")
    by = y + 47
    d.rectangle([x, y + 47, x + w, y + 65], fill=REGION_COLORS[region])
    d.text((x + 10, y + 56), region.upper(), font=F["bold"](11),
           fill=(255, 255, 255), anchor="lm")
    d.text((x + w - 10, y + 56), source, font=F["semi"](11),
           fill=(255, 255, 255), anchor="rm")
    hy = y + 72
    for i, ln in enumerate(wrap(d, headline, F["bold"](19), w - 20)[:2]):
        d.text((x + 10, hy + i * 23), ln, font=F["bold"](19), fill=INK)
    dy = y + 122
    for i, ln in enumerate(wrap(d, deck, F["reg"](13), w - 20)[:3]):
        d.text((x + 10, dy + i * 16), ln, font=F["reg"](13), fill=(52, 58, 72))
    d.text((x + 10, y + h - 10), "MONDAY 23 NOVEMBER 2026",
           font=F["semi"](9), fill=MUTED, anchor="lb")


def medium_card(d, x, y, w, h, n, region, headline, deck, source):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=BORDER, width=1)
    d.rectangle([x, y + 17, x + 17, y + 34], fill=RED)
    d.text((x + 8, y + 25), str(n), font=F["bold"](11),
           fill=(255, 255, 255), anchor="mm")
    d.text((x + 23, y + 25), region.upper(), font=F["bold"](10),
           fill=REGION_COLORS[region], anchor="lm")
    d.text((x + w - 7, y + 25), source, font=F["semi"](9), fill=MUTED,
           anchor="rm")
    hy = y + 40
    for i, ln in enumerate(wrap(d, headline, F["bold"](13), w - 14)[:2]):
        d.text((x + 7, hy + i * 16), ln, font=F["bold"](13), fill=INK)
    dy = y + 74
    for i, ln in enumerate(wrap(d, deck, F["reg"](10.5), w - 14)[:2]):
        d.text((x + 7, dy + i * 13), ln, font=F["reg"](10.5),
               fill=(52, 58, 72))


def render(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # side margin

    # --- masthead ---
    d.rectangle([0, 0, W, 44], fill=NAVY)
    d.text((M, 22), "THE WORLD IN ONE DAY", font=F["bold"](23),
           fill=(255, 255, 255), anchor="lm")
    d.text((W - M, 22), "31 STORIES  \u00b7  7 REGIONS", font=F["semi"](13),
           fill=GOLD, anchor="rm")

    # --- giant date ---
    d.text((W // 2, 88), "MONDAY 23 NOVEMBER 2026", font=F["bold"](58),
           fill=INK, anchor="mm")

    # --- red sub-headline ---
    d.text((W // 2, 145),
           "KYIV STRUCK  \u00b7  NVIDIA CHIEF RETURNS  \u00b7  UN SEEKS GLOBAL AI RULES",
           font=F["semi"](17), fill=RED, anchor="mm")

    # --- stat strip ---
    d.line([M, 158, W - M, 158], fill=BORDER, width=1)
    col_w = (W - 2 * M) / 6
    for i, (num, label) in enumerate(STATS):
        cx = M + col_w * i + col_w / 2
        d.text((cx, 178), num, font=F["bold"](28), fill=RED, anchor="mm")
        for j, ln in enumerate(label.split("\n")):
            d.text((cx, 200 + j * 13), ln, font=F["semi"](10.5), fill=INK,
                   anchor="mm")
        if i:
            d.line([M + col_w * i, 166, M + col_w * i, 214], fill=BORDER,
                   width=1)
    d.line([M, 220, W - M, 220], fill=BORDER, width=1)

    # --- region strip (each region in its own colour) ---
    parts, total_w = [], 0
    for name, cnt in REGION_STRIP:
        seg = "%s %d" % (name.upper(), cnt)
        parts.append((seg, REGION_COLORS[name]))
        total_w += d.textlength(seg, font=F["semi"](13))
    total_w += d.textlength("  \u00b7  ", font=F["semi"](13)) * (len(parts) - 1)
    x = (W - total_w) / 2
    for i, (seg, col) in enumerate(parts):
        d.text((x, 231), seg, font=F["semi"](13), fill=col, anchor="lm")
        x += d.textlength(seg, font=F["semi"](13))
        if i < len(parts) - 1:
            sep = "  \u00b7  "
            d.text((x, 231), sep, font=F["semi"](13), fill=MUTED, anchor="lm")
            x += d.textlength(sep, font=F["semi"](13))

    # --- 3 lead cards ---
    lw = (W - 2 * M - 24) // 3
    for i, (n, region, hl, deck, src, _lon, _lat, art) in enumerate(LEADS):
        lead_card(d, M + i * (lw + 12), 242, lw if i < 2 else W - M - (M + 2 * (lw + 12)),
                  190, n, region, hl, deck, src, art)

    # --- 10 medium cards, 5 x 2 ---
    mw = (W - 2 * M - 40) // 5
    for i, (n, region, hl, deck, src, _lon, _lat) in enumerate(MEDIUM):
        row, col = divmod(i, 5)
        cx = M + col * (mw + 10)
        cy = 432 + row * 116
        cw = mw if col < 4 else W - M - cx
        medium_card(d, cx, cy, cw, 108, n, region, hl, deck, src)

    # --- ALSO ON brief list (2 columns x 9 rows) ---
    d.text((M, 664), "ALSO ON MONDAY 23 NOVEMBER \u2014 18 MORE STORIES",
           font=F["bold"](14), fill=INK, anchor="lm")
    d.line([M, 676, W - M, 676], fill=RED, width=2)
    col_w2 = (W - 2 * M - 24) // 2
    for i, (n, region, hl, src) in enumerate(BRIEFS):
        col, row = divmod(i, 9)
        bx = M + col * (col_w2 + 24)
        by = 682 + row * 17
        d.text((bx, by), "%d \u00b7" % n, font=F["bold"](12), fill=RED,
               anchor="la")
        num_w = d.textlength("%d \u00b7  " % n, font=F["bold"](12))
        src_w = d.textlength("  " + src, font=F["semi"](9.5))
        head = ellipsize(d, hl, F["med"](12),
                         col_w2 - num_w - src_w - 4)
        d.text((bx + num_w, by), head, font=F["med"](12), fill=INK,
               anchor="la")
        d.text((bx + col_w2, by), src, font=F["semi"](9.5), fill=MUTED,
               anchor="ra")

    # --- bottom band: map (left) + DATE CHECK (right) ---
    # map panel
    d.rectangle([M, 838, 560, 998], fill=CARD, outline=BORDER, width=1)
    d.text((M + 12, 850), "WHERE IT HAPPENED \u2014 STORIES 1\u201313",
           font=F["bold"](11.5), fill=INK, anchor="la")
    mx0, my0, mx1, my1 = 40, 868, 548, 990
    d.rectangle([mx0, my0, mx1, my1], fill=OCEAN)
    sx = (mx1 - mx0) / 360.0
    sy = (my1 - my0) / 136.0

    def proj(lon, lat):
        return (mx0 + (lon + 170) * sx, my0 + (78 - lat) * sy)

    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=LAND_LN)
    pins = [(n, lon, lat) for (n, _r, _h, _de, _s, lon, lat, *_a) in LEADS]
    pins += [(n, lon, lat) for (n, _r, _h, _de, _s, lon, lat) in MEDIUM]
    for n, lon, lat in pins:
        px, py = proj(lon, lat)
        dx, dy = BADGE_OFF.get(n, (10, -10))
        bx, by = px + dx, py + dy
        d.line([px, py, bx, by], fill=RED, width=1)
        d.ellipse([px - 3.5, py - 3.5, px + 3.5, py + 3.5], fill=RED)
        d.ellipse([bx - 7, by - 7, bx + 7, by + 7], fill=RED,
                  outline=(255, 255, 255), width=1)
        d.text((bx, by), str(n), font=F["bold"](8.5), fill=(255, 255, 255),
               anchor="mm")

    # DATE CHECK panel
    d.rectangle([572, 838, W - M, 998], fill=CARD, outline=RED, width=2)
    d.text((588, 850), "DATE CHECK", font=F["bold"](13), fill=RED, anchor="la")
    d.text((W - M - 16, 850), "23 NOV 2026", font=F["bold"](11), fill=RED,
           anchor="ra")
    body = ("Every story on this page was first reported Monday 23 November "
            "2026. Left out of this edition: " + EXCLUDED + ".")
    by = 874
    for ln in wrap(d, body, F["reg"](12), W - M - 588 - 32):
        d.text((588, by), ln, font=F["reg"](12), fill=(52, 58, 72), anchor="la")
        by += 16
    d.text((588, by + 8),
           "No story from any other day appears on this page.",
           font=F["semi"](12), fill=INK, anchor="la")

    # --- footer ---
    d.text((W // 2, 1011),
           "Sources named beside each story  \u00b7  Original drawings  \u00b7  "
           "Every story first reported Monday 23 November 2026",
           font=F["reg"](11), fill=MUTED, anchor="mm")

    img.save(out_path, "PNG")


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.png"
    try:
        render(target)
    except OSError:
        render(os.path.join(BASE, "entry.png"))
    print("rendered", target)
