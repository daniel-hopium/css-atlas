"""Erzeugt favicon.svg, favicon.ico und apple-touch-icon.png aus EINER Geometrie.

Aufruf aus dem Repo: python tools/make_icons.py (braucht Pillow).

Farben und Linienstil wie bei der Schwester-App Daumenregel: dunkler Grund, blasses Blau,
ein goldener Akzent. Jede Form steht einmal in SHAPES und wird daraus für SVG (Pfad) wie
für PNG (Pillow kann kein SVG lesen) gezeichnet.
"""
from pathlib import Path

from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent.parent  # Repo-Wurzel
BG, LINE, GOLD = "#0F1418", "#C2D6EA", "#E0C48A"
W = 2.2
NAME = "Layout-Raster"
# ("line", Punkte, Farbe, Deckkraft, geschlossen) · ("fill", Punkte, Farbe) · ("dot", cx, cy, r, Farbe)
SHAPES = [
    ('line', [(7, 7), (25, 7), (25, 12), (7, 12)], LINE, 0.45, True),
    ('line', [(7, 16), (13.5, 16), (13.5, 25), (7, 25)], LINE, 1.0, True),
    ('line', [(18.5, 16), (25, 16), (25, 25), (18.5, 25)], LINE, 1.0, True),
    ('dot', 21.75, 20.5, 1.7, GOLD),
]


def svg():
    out = []
    for s in SHAPES:
        if s[0] == "line":
            _, pts, col, op, closed = s
            d = "M" + " L".join(f"{x:g} {y:g}" for x, y in pts) + (" Z" if closed else "")
            out.append(f'  <path d="{d}" fill="none" stroke="{col}" stroke-width="{W}" '
                       f'stroke-linecap="round" stroke-linejoin="round"'
                       + (f' stroke-opacity="{op}"' if op < 1 else "") + "/>")
        elif s[0] == "fill":
            _, pts, col = s
            out.append(f'  <path d="M' + " L".join(f"{x:g} {y:g}" for x, y in pts) + f' Z" fill="{col}"/>')
        else:
            _, cx, cy, r, col = s
            out.append(f'  <circle cx="{cx:g}" cy="{cy:g}" r="{r:g}" fill="{col}"/>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">\n'
            f'  <!-- {NAME} im Linienstil der Daumenregel. Erzeugt von tools/make_icons.py. -->\n'
            f'  <rect width="32" height="32" rx="7" fill="{BG}"/>\n' + "\n".join(out) + "\n</svg>\n")


def rgba(hexcol, a=1.0):
    h = hexcol.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (round(255 * a),)


def png(size, rounded, ss=16):
    """In ss-facher Größe zeichnen und verkleinern – ergibt glatte Kanten."""
    k = size * ss / 32
    img = Image.new("RGBA", (size * ss, size * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, size * ss - 1, size * ss - 1], radius=7 * k, fill=rgba(BG))
    else:  # iOS rundet die Ecken selbst ab; transparente Ecken würden schwarz
        d.rectangle([0, 0, size * ss, size * ss], fill=rgba(BG))
    w = W * k
    for s in SHAPES:
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        op = 1.0
        if s[0] == "line":
            _, pts, col, op, closed = s
            pts = [(x * k, y * k) for x, y in pts]
            if closed:
                pts = pts + pts[:2]
            ld.line(pts, fill=rgba(col), width=round(w), joint="curve")
            for x, y in pts:  # runde Ecken und Linienenden
                ld.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=rgba(col))
        elif s[0] == "fill":
            _, pts, col = s
            ld.polygon([(x * k, y * k) for x, y in pts], fill=rgba(col))
        else:
            _, cx, cy, r, col = s
            ld.ellipse([(cx - r) * k, (cy - r) * k, (cx + r) * k, (cy + r) * k], fill=rgba(col))
        if op < 1:
            layer.putalpha(layer.getchannel("A").point(lambda v: round(v * op)))
        img = Image.alpha_composite(img, layer)
    return img.resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    (OUT / "favicon.svg").write_text(svg(), encoding="utf-8", newline="\n")
    icons = {s: png(s, True) for s in (16, 32, 48)}
    icons[48].save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)],
                   append_images=[icons[16], icons[32]])
    png(180, False).save(OUT / "apple-touch-icon.png")
    print("favicon.svg, favicon.ico, apple-touch-icon.png geschrieben")
