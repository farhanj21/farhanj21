"""
Regenerates the animated banner and pixel section headers in assets/.

How to use:
  1. Edit the SETTINGS block below.
  2. From the root of your farhanj21 repo, run:   python tools/make_assets.py
  3. Commit and push the changed files in assets/.

Needs only Python 3 (no extra packages).
"""
import html, os

# ============================== SETTINGS ==============================

USERNAME   = "farhanj21"
PIXEL_NAME = "SYED FARHAN JAFRI"            # big pixel letters: A-Z, 0-9, space, - . ! '
NAME_LINE  = "Syed Farhan Jafri"       # small line under the pixel name...
TITLE      = "Software Engineer"       # ...shown as  NAME_LINE / TITLE
LEVEL      = 24                        # the "Lv" number in the top right
XP_PERCENT = 72                        # how full the XP bar gets (0-100)
BOTTOM_TEXT = "press start"            # blinking text in the bottom right

# Lines the typing animation cycles through (keep each under ~70 characters)
TYPING_LINES = [
    "building full-stack apps in Next.js and Typescript",
    "training models with PyTorch and TensorFlow",
    "gaming and making videos on YouTube",
]
SECONDS_PER_LINE = 4.5

# Section headers: (text shown in pixels, file name in assets/)
HEADERS = [
    ("ABOUT", "about"),
    ("MY ARSENAL", "my-arsenal"),
    ("PROJECTS", "projects"),
    ("STATS", "stats"),
]

# Project cards: one entry per card, rendered to assets/cards/<file>.svg
#   title - drawn in the pixel font, so stick to A-Z 0-9 space - . ! ' and keep it short
#   tag   - small gold chip in the top right, e.g. the project type
#   blurb - a sentence or two; it wraps automatically
#   stack - the tech chips along the bottom (they must fit on one row)
PROJECTS = [
    {
        "title": "PROJECT ONE",
        "tag": "web",
        "blurb": "Short description of what this project does and why it exists.",
        "stack": ["Next.js", "TypeScript", "MongoDB"],
        "file": "project-one",
    },
    {
        "title": "PROJECT TWO",
        "tag": "ml",
        "blurb": "Short description of what this project does and why it exists.",
        "stack": ["PyTorch", "Python", "FastAPI"],
        "file": "project-two",
    },
]

CARD_W = 480           # card width; two of these sit side by side in the README

# Colors (keep these in sync with the hex codes in README.md if you change them)
INK   = "#0E1726"   # background
FRAME = "#24365A"   # borders and divider lines
DEPTH = "#2B4C7E"   # pixel letter shadow
TEXT  = "#EAF0FA"   # main text
MUTED = "#8A9BB8"   # secondary text
GOLD  = "#F2B544"   # accent: XP bar, cursor, shine
SKY   = "#5CC8FF"   # twinkling stars

# ======================================================================

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets")
os.makedirs(OUT, exist_ok=True)

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

FONT = {
"A": [".###.","#...#","#...#","#####","#...#","#...#","#...#"],
"B": ["####.","#...#","#...#","####.","#...#","#...#","####."],
"C": [".###.","#...#","#....","#....","#....","#...#",".###."],
"D": ["####.","#...#","#...#","#...#","#...#","#...#","####."],
"E": ["#####","#....","#....","####.","#....","#....","#####"],
"F": ["#####","#....","#....","####.","#....","#....","#...."],
"G": [".###.","#...#","#....","#.###","#...#","#...#",".####"],
"H": ["#...#","#...#","#...#","#####","#...#","#...#","#...#"],
"I": [".###.","..#..","..#..","..#..","..#..","..#..",".###."],
"J": ["..###","....#","....#","....#","....#","#...#",".###."],
"K": ["#...#","#..#.","#.#..","##...","#.#..","#..#.","#...#"],
"L": ["#....","#....","#....","#....","#....","#....","#####"],
"M": ["#...#","##.##","#.#.#","#.#.#","#...#","#...#","#...#"],
"N": ["#...#","#...#","##..#","#.#.#","#..##","#...#","#...#"],
"O": [".###.","#...#","#...#","#...#","#...#","#...#",".###."],
"P": ["####.","#...#","#...#","####.","#....","#....","#...."],
"Q": [".###.","#...#","#...#","#...#","#.#.#","#..#.",".##.#"],
"R": ["####.","#...#","#...#","####.","#.#..","#..#.","#...#"],
"S": [".####","#....","#....",".###.","....#","....#","####."],
"T": ["#####","..#..","..#..","..#..","..#..","..#..","..#.."],
"U": ["#...#","#...#","#...#","#...#","#...#","#...#",".###."],
"V": ["#...#","#...#","#...#","#...#","#...#",".#.#.","..#.."],
"W": ["#...#","#...#","#...#","#.#.#","#.#.#","#.#.#",".#.#."],
"X": ["#...#","#...#",".#.#.","..#..",".#.#.","#...#","#...#"],
"Y": ["#...#","#...#",".#.#.","..#..","..#..","..#..","..#.."],
"Z": ["#####","....#","...#.","..#..",".#...","#....","#####"],
"0": [".###.","#...#","#..##","#.#.#","##..#","#...#",".###."],
"1": ["..#..",".##..","..#..","..#..","..#..","..#..",".###."],
"2": [".###.","#...#","....#","...#.","..#..",".#...","#####"],
"3": ["####.","....#","....#",".###.","....#","....#","####."],
"4": ["#...#","#...#","#...#","#####","....#","....#","....#"],
"5": ["#####","#....","####.","....#","....#","#...#",".###."],
"6": [".###.","#....","#....","####.","#...#","#...#",".###."],
"7": ["#####","....#","...#.","..#..","..#..","..#..","..#.."],
"8": [".###.","#...#","#...#",".###.","#...#","#...#",".###."],
"9": [".###.","#...#","#...#",".####","....#","....#",".###."],
" ": ["..","..","..","..","..","..",".."],
"-": ["...","...","...","###","...","...","..."],
".": [".",".",".",".",".",".","#"],
"!": ["#","#","#","#","#",".","#"],
"'": ["#","#",".",".",".",".","."],
}

def pixels(word):
    pts, x = [], 0
    for ch in word.upper():
        if ch not in FONT:
            raise SystemExit(f"The pixel font has no '{ch}'. Use A-Z, 0-9, space, - . ! '")
        g = FONT[ch]
        for r, line in enumerate(g):
            for c, v in enumerate(line):
                if v == "#":
                    pts.append((x + c, r))
        x += len(g[0]) + 1
    return pts, x - 1

def chamfer(x, y, w, h, k):
    return (f"M{x+k},{y} H{x+w-k} L{x+w},{y+k} V{y+h-k} L{x+w-k},{y+h} "
            f"H{x+k} L{x},{y+h-k} V{y+k} Z")

def hero():
    W = 1000
    pts, ncols = pixels(PIXEL_NAME)
    S = min(12, int(860 / ncols))        # shrink the pixels if the name is long
    GAP = S / 8
    ox, oy = 56, 96
    sub_y = oy + 7 * S + 48
    ty = sub_y + 44
    H = ty + 68

    cols = {}
    for c, r in pts:
        cols.setdefault(c, []).append(r)
    name = []
    for i, c in enumerate(sorted(cols)):
        x = ox + c * S
        d = 0.35 + i * 0.022
        sh = "".join(f'<rect x="{x+S/3:g}" y="{oy+r*S+S/3:g}" width="{S-GAP:g}" height="{S-GAP:g}"/>' for r in cols[c])
        fc = "".join(f'<rect x="{x}" y="{oy+r*S}" width="{S-GAP:g}" height="{S-GAP:g}"/>' for r in cols[c])
        name.append(f'<g class="px" style="animation-delay:{d:.3f}s"><g fill="{DEPTH}">{sh}</g><g fill="url(#shine)">{fc}</g></g>')

    CW, tx = 12.05, 82
    n_lines = len(TYPING_LINES)
    period = SECONDS_PER_LINE * n_lines
    longest = max(len(t) for t in TYPING_LINES)
    if longest > 70:
        print(f"Warning: a typing line is {longest} characters; it may run off the banner.")
    typing, kf = [], []
    for i, t in enumerate(TYPING_LINES):
        n = len(t)
        w = round(n * CW + 4)
        delay = -((period - i * SECONDS_PER_LINE) % period)
        kf.append(f"@keyframes t{i}{{0%{{transform:translateX(0)}}18%,29%{{transform:translateX({w}px)}}"
                  f"31%,100%{{transform:translateX(0)}}}}"
                  f"@keyframes v{i}{{0%,{100/n_lines-1:.2f}%{{opacity:1}}{100/n_lines:.2f}%,100%{{opacity:0}}}}")
        typing.append(
            f'<g class="ln" style="animation:v{i} {period:g}s linear {delay:g}s infinite">'
            f'<text x="{tx}" y="{ty}" class="mono" font-size="20" fill="{TEXT}">{html.escape(t)}</text>'
            f'<g class="cv" style="animation:t{i} {period:g}s steps({n},end) {delay:g}s infinite">'
            f'<rect x="{tx}" y="{ty-19}" width="11" height="24" fill="{GOLD}" class="blink"/>'
            f'<rect x="{tx+11}" y="{ty-20}" width="{longest*CW+40:.0f}" height="28" fill="{INK}"/></g></g>')

    stars = [(930, 70, SKY), (952, 128, GOLD), (905, 160, SKY), (968, 206, SKY), (918, 236, GOLD),
             (620, 58, SKY), (684, 74, GOLD), (40, 300, SKY), (500, 312, SKY), (948, 280, SKY)]
    star_svg = "".join(f'<rect x="{x}" y="{y*H/340:.0f}" width="4" height="4" fill="{c}" class="tw" '
                       f'style="animation-delay:{(i*0.73)%4:.2f}s"/>' for i, (x, y, c) in enumerate(stars))

    bx, by, bw, bh = 780, 38, 176, 12
    fill_w = round(bw * max(0, min(100, XP_PERCENT)) / 100)
    segs = "".join(f'<rect x="{bx+s}" y="{by}" width="2" height="{bh}" fill="{INK}"/>' for s in range(16, bw, 16))

    css = f"""
.mono{{font-family:{MONO}}} .sans{{font-family:{SANS}}}
.px{{animation:pop .45s cubic-bezier(.2,.9,.3,1.2) both}}
@keyframes pop{{from{{opacity:0;transform:translateY(-14px)}}to{{opacity:1;transform:none}}}}
.fade{{animation:fade .8s ease-out both}}
@keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
.blink{{animation:blink 1s steps(1,end) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
.tw{{animation:tw 4s ease-in-out infinite;opacity:.25}}
@keyframes tw{{0%,100%{{opacity:.15}}50%{{opacity:.9}}}}
{''.join(kf)}
@media (prefers-reduced-motion: reduce){{
  *{{animation:none!important}}
  .ln{{opacity:0}} .ln:first-of-type{{opacity:1}} .cv{{transform:translateX(900px)}}
}}"""

    e = html.escape
    desc = f"{NAME_LINE}, {TITLE}. " + " ".join(t[0].upper() + t[1:] + "." for t in TYPING_LINES)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">{e(NAME_LINE)}</title>
<desc id="d">{e(desc)}</desc>
<defs>
  <linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="-2000" y1="0" x2="3000" y2="0">
    <stop offset="0" stop-color="{TEXT}"/><stop offset=".29" stop-color="{TEXT}"/>
    <stop offset=".31" stop-color="{GOLD}"/><stop offset=".33" stop-color="{TEXT}"/>
    <stop offset="1" stop-color="{TEXT}"/>
    <animateTransform attributeName="gradientTransform" type="translate"
      values="0 0; 1500 0; 1500 0" keyTimes="0; .32; 1" dur="7s" begin="2.2s" repeatCount="indefinite"/>
  </linearGradient>
  <clipPath id="typeclip"><rect x="40" y="{ty-32}" width="920" height="50"/></clipPath>
</defs>
<style>{css}</style>
<path d="{chamfer(1,1,W-2,H-2,14)}" fill="{INK}" stroke="{FRAME}" stroke-width="2"/>
{star_svg}
<g class="fade">
  <rect x="{ox}" y="36" width="16" height="16" fill="{GOLD}"/>
  <text x="{ox+7.5}" y="48.5" text-anchor="middle" class="mono" font-size="11" font-weight="700" fill="{INK}">P1</text>
  <text x="{ox+26}" y="49" class="mono" font-size="15" fill="{MUTED}">{e(USERNAME)}</text>
  <text x="{bx-12}" y="49" text-anchor="end" class="mono" font-size="15" fill="{TEXT}">Lv {LEVEL}</text>
  <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="#1B2A45"/>
  <rect x="{bx}" y="{by}" width="{fill_w}" height="{bh}" fill="{GOLD}">
    <animate attributeName="width" values="0;0;{fill_w}" keyTimes="0;.3;1" dur="2.2s" fill="freeze"
      calcMode="spline" keySplines="0 0 1 1;.2 .8 .3 1"/>
  </rect>
  {segs}
</g>
{''.join(name)}
<text x="{ox}" y="{sub_y}" class="sans fade" style="animation-delay:1.1s" font-size="22" fill="{MUTED}">{e(NAME_LINE)} <tspan fill="{FRAME}">/</tspan> <tspan fill="{TEXT}">{e(TITLE)}</tspan></text>
<g class="fade" style="animation-delay:1.4s" clip-path="url(#typeclip)">
  <text x="{ox}" y="{ty}" class="mono" font-size="20" fill="{GOLD}">&gt;</text>
  {''.join(typing)}
</g>
<text x="{W-44}" y="{H-30}" text-anchor="end" class="mono blink" font-size="14" fill="{GOLD}">&#9660; {e(BOTTOM_TEXT)}</text>
</svg>'''
    with open(os.path.join(OUT, "hero.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def header(title, fname):
    S, GAP, pad, H = 4, 0.6, 18, 52
    pts, ncols = pixels(title)
    tabw = ncols * S + pad * 2 + 18
    face = "".join(f'<rect x="{pad+18+c*S}" y="{12+r*S}" width="{S-GAP}" height="{S-GAP}"/>' for c, r in pts)
    shadow = "".join(f'<rect x="{pad+20+c*S}" y="{14+r*S}" width="{S-GAP}" height="{S-GAP}"/>' for c, r in pts)
    label = html.escape(title.title())
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {H}" width="1000" height="{H}" role="img" aria-label="{label}">
<title>{label}</title>
<path d="{chamfer(1,1,tabw,H-2,8)}" fill="{INK}" stroke="{FRAME}" stroke-width="2"/>
<rect x="{pad}" y="{12+2*S}" width="{S*2}" height="{S*3}" fill="{GOLD}"/>
<g fill="{DEPTH}">{shadow}</g><g fill="{TEXT}">{face}</g>
<rect x="{tabw+1}" y="{H/2-1}" width="{999-tabw-1}" height="2" fill="{FRAME}"/>
<rect x="996" y="{H/2-3}" width="4" height="6" fill="{FRAME}"/>
</svg>'''
    with open(os.path.join(OUT, f"{fname}.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def wrap(text, width):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if len(trial) > width and line:
            lines.append(line)
            line = word
        else:
            line = trial
    if line:
        lines.append(line)
    return lines


def card(p):
    """One project card: the same chamfered panel, pixel title and gold accents as the hero."""
    W = CARD_W
    S, GAP = 4, 0.5              # pixel size for the title
    pts, ncols = pixels(p["title"])
    pad = 22
    while ncols * S > W - pad * 2 - 76 and S > 2:
        S -= 1
    GAP = S / 8
    title_y = 34
    face = "".join(f'<rect x="{pad+c*S:g}" y="{title_y+r*S:g}" width="{S-GAP:g}" height="{S-GAP:g}"/>' for c, r in pts)
    shadow = "".join(f'<rect x="{pad+2+c*S:g}" y="{title_y+2+r*S:g}" width="{S-GAP:g}" height="{S-GAP:g}"/>' for c, r in pts)

    body_y = title_y + 7 * S + 32
    lines = wrap(p["blurb"], int((W - pad * 2) / 7.35))
    blurb = "".join(
        f'<text x="{pad}" y="{body_y+i*21}" class="mono" font-size="13" fill="{MUTED}">{html.escape(t)}</text>'
        for i, t in enumerate(lines))

    chip_y = body_y + (len(lines) - 1) * 21 + 20
    chips, x = [], pad
    for t in p["stack"]:
        w = round(len(t) * 7.4 + 18)
        chips.append(f'<path d="{chamfer(x, chip_y, w, 22, 5)}" fill="none" stroke="{FRAME}" stroke-width="1.5"/>'
                     f'<text x="{x+w/2:g}" y="{chip_y+15}" text-anchor="middle" class="mono" font-size="12" '
                     f'fill="{SKY}">{html.escape(t)}</text>')
        x += w + 8
    if x - 8 > W - pad:
        print(f"Warning: the stack chips on '{p['title']}' run past the edge of the card.")

    H = chip_y + 22 + pad

    tag = html.escape(p["tag"].upper())
    tw = round(len(tag) * 7.4 + 16)
    tag_svg = (f'<rect x="{W-pad-tw}" y="{title_y-2}" width="{tw}" height="18" fill="{GOLD}"/>'
               f'<text x="{W-pad-tw/2:g}" y="{title_y+11.5:g}" text-anchor="middle" class="mono" font-size="11" '
               f'font-weight="700" fill="{INK}">{tag}</text>')

    label = html.escape(f'{p["title"].title()}. {p["blurb"]} Built with {", ".join(p["stack"])}.')
    css = ".mono{font-family:%s}.blink{animation:blink 1s steps(1,end) infinite}" % MONO
    css += "@keyframes blink{50%{opacity:0}}"
    css += "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'role="img" aria-label="{label}">\n'
        f'<title>{html.escape(p["title"].title())}</title>\n'
        f'<style>{css}</style>\n'
        f'<path d="{chamfer(1, 1, W-2, H-2, 12)}" fill="{INK}" stroke="{FRAME}" stroke-width="2"/>\n'
        f'<rect x="{pad}" y="{title_y-14}" width="{S*3}" height="{S}" fill="{GOLD}"/>\n'
        f'{tag_svg}\n'
        f'<g fill="{DEPTH}">{shadow}</g><g fill="{TEXT}">{face}</g>\n'
        f'{blurb}\n'
        f'{"".join(chips)}\n'
        f'<text x="{W-pad}" y="{H-12}" text-anchor="end" class="mono blink" font-size="10" '
        f'fill="{GOLD}">&#9654;</text>\n'
        f'</svg>')


def cards():
    out = os.path.join(OUT, "cards")
    os.makedirs(out, exist_ok=True)
    for p in PROJECTS:
        with open(os.path.join(out, f'{p["file"]}.svg'), "w", encoding="utf-8") as f:
            f.write(card(p))


if __name__ == "__main__":
    hero()
    for text, fname in HEADERS:
        header(text, fname)
    cards()
    print("Updated assets/hero.svg,", ", ".join(f'assets/cards/{p["file"]}.svg' for p in PROJECTS), "and", ", ".join(f"assets/{f}.svg" for _, f in HEADERS))
