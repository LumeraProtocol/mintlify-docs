#!/usr/bin/env python3
"""Build standalone light/dark SVG images for the Lumera docs diagrams.

Same geometry as components/diagram.tsx. Colors resolved per theme and the
Shantell Sans font subset embedded as a data URI so <img> rendering works.
"""
import base64
import json
import subprocess
import html
from pathlib import Path

SRC = Path(__file__).parent
REPO = SRC.parent
OUT = REPO / "images" / "diagrams"

with open(SRC / "diagrams.json") as f:
    DIAGRAMS = json.load(f)
with open(SRC / "diagrams-extra.json") as f:
    DIAGRAMS.update(json.load(f))

EXPORTS = {
    "architecture": ("cascade-architecture", {}),
    "how-cascade-works": ("how-cascade-works", {}),
    "erasure-coding": ("erasure-coding", {}),
    "interchain-accounts": ("interchain-accounts", {}),
    "encrypted-storage": ("encrypted-storage", {}),
    "collaboration-flow": ("collaboration-flow", {}),
    "sdk-architecture": ("sdk-architecture", {}),
    "node-architecture": ("node-architecture", {}),
    "supernode-architecture": ("supernode-architecture", {}),
    "injective-pattern-a": ("pattern-user-signed", {"Injective\n(your CW)": "Your chain\n(contract)"}),
    "injective-pattern-b": ("pattern-server-signed", {"Injective\n(your CW)": "Your chain\n(contract)", "sign Injective tx": "sign your chain tx"}),
    "injective-integration": ("cross-chain-integration", {"Injective contract": "Your chain contract", "signs Injective txs": "signs your chain txs"}),
    "everlight-flow": ("everlight-flow", {}),
    "execution-environments": ("execution-environments", {}),
    "protocol-stack": ("protocol-stack", {}),
}

THEMES = {
    "light": {"box": "#078a8a", "text": "#1e293b", "muted": "#64748b"},
    "dark": {"box": "#47c78a", "text": "#e2e8f0", "muted": "#94a3b8"},
}

# Clean titles for the SVG aria-label, keyed by output name. Overrides the
# source title where it names a specific chain or uses punctuation we avoid.
TITLES = {
    "pattern-user-signed": "Pattern A user signed Cascade write",
    "pattern-server-signed": "Pattern B server signed through a backend",
    "cross-chain-integration": "Cross-chain integration shape",
    "node-architecture": "Browser-first Cascade architecture",
}

# ── collect used characters for the font subset ──────────────────────────────
chars = set(" ")
for src, (out_name, subs) in EXPORTS.items():
    for el in DIAGRAMS[src]["elements"]:
        for key in ("label", "text"):
            v = el.get(key, "")
            for a, b in subs.items():
                v = v.replace(a, b)
            chars.update(v)
        for item in el.get("items") or []:
            for a, b in subs.items():
                item = item.replace(a, b)
            chars.update(item)
CHARSET = "".join(sorted(chars - {"\n"}))

VENV = None  # uses pyftsubset from PATH
fonts_b64 = {}
for weight in (400, 700):
    src = SRC / "fonts" / f"shantell-{weight}.woff2"
    sub = SRC / "fonts" / f"shantell-{weight}-sub.woff2"
    subprocess.run([
        "pyftsubset", str(src),
        f"--text={CHARSET}",
        "--flavor=woff2",
        f"--output-file={sub}",
        "--layout-features=*",
        "--no-hinting",
        "--desubroutinize",
        "--instancer=wght=" + str(weight) if False else "--no-notdef-outline",
    ], check=True, capture_output=True)
    fonts_b64[weight] = base64.b64encode(sub.read_bytes()).decode()
    print(f"subset {weight}: {sub.stat().st_size} bytes ({len(CHARSET)} chars)")

FONT_CSS = (
    "@font-face{font-family:'Shantell Sans';font-weight:400;"
    f"src:url(data:font/woff2;base64,{fonts_b64[400]}) format('woff2');}}"
    "@font-face{font-family:'Shantell Sans';font-weight:700;"
    f"src:url(data:font/woff2;base64,{fonts_b64[700]}) format('woff2');}}"
    "text{font-family:'Shantell Sans','Segoe Print','Comic Sans MS',cursive;}"
)


def esc(s):
    return html.escape(str(s), quote=True)


def num(v):
    out = f"{v:.2f}".rstrip("0").rstrip(".")
    return out if out else "0"


def settings(d):
    label_size = d.get("labelSize", 16)
    item_size = d.get("itemSize", 14)
    return {
        "labelSize": label_size,
        "itemSize": item_size,
        "arrowLabelSize": d.get("arrowLabelSize", 13),
        "labelLineHeight": d.get("labelLineHeight", label_size + 6),
        "itemLineHeight": d.get("itemLineHeight", item_size + 5),
        "itemGap": d.get("itemGap", 6),
        "pad": d.get("pad", 10),
        "borderRadius": d.get("borderRadius", 16),
        "strokeWidth": d.get("strokeWidth", 1.3),
        "arrowWidth": d.get("arrowWidth", 1.3),
    }


def render_box(el, s, subs, c):
    label = el.get("label", "")
    for a, b in subs.items():
        label = label.replace(a, b)
    lines = label.split("\n")
    items = el.get("items") or []
    if items:
        label_y = el["y"] + s["labelSize"] + 6
    else:
        label_y = el["y"] + el["h"] / 2 - ((len(lines) - 1) * s["labelLineHeight"]) / 2
    sw = s["strokeWidth"] * 0.75 if el.get("dashed") else s["strokeWidth"]
    dash = ' stroke-dasharray="6 4"' if el.get("dashed") else ""
    parts = [
        f'<rect x="{num(el["x"] - s["pad"])}" y="{num(el["y"] - s["pad"])}" '
        f'width="{num(el["w"] + s["pad"] * 2)}" height="{num(el["h"] + s["pad"] * 2)}" '
        f'rx="{num(s["borderRadius"])}" fill="none" stroke="{c["box"]}" stroke-width="{num(sw)}"{dash}/>'
    ]
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        parts.append(
            f'<text x="{num(el["x"] + el["w"] / 2)}" y="{num(label_y + i * s["labelLineHeight"])}" '
            f'fill="{c["text"]}" font-size="{num(s["labelSize"])}" text-anchor="middle" dominant-baseline="middle">{esc(line)}</text>'
        )
    for i, item in enumerate(items):
        for a, b in subs.items():
            item = item.replace(a, b)
        y = label_y + len(lines) * s["labelLineHeight"] + s["itemGap"] + i * s["itemLineHeight"]
        parts.append(
            f'<text x="{num(el["x"] + el["w"] / 2)}" y="{num(y)}" '
            f'fill="{c["muted"]}" font-size="{num(s["itemSize"])}" text-anchor="middle" dominant-baseline="middle">{esc(item)}</text>'
        )
    return "".join(parts)


def render_arrow(el, name, s, subs, c):
    mid = f"ah-{name}-{el['id']}"
    pts = el["points"]
    d = f"M {num(pts[0][0])} {num(pts[0][1])} " + " ".join(f"L {num(p[0])} {num(p[1])}" for p in pts[1:])
    parts = [
        f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<polygon points="0 0, 10 5, 0 10" fill="{c["muted"]}"/></marker>'
    ]
    if el.get("bidirectional"):
        parts.append(
            f'<marker id="{mid}-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<polygon points="10 0, 0 5, 10 10" fill="{c["muted"]}"/></marker>'
        )
    defs = "<defs>" + "".join(parts) + "</defs>"
    dash = ' stroke-dasharray="6 4"' if el.get("dashed") else ""
    start = f' marker-start="url(#{mid}-s)"' if el.get("bidirectional") else ""
    out = [
        defs,
        f'<path d="{d}" fill="none" stroke="{c["muted"]}" stroke-width="{num(s["arrowWidth"])}"{dash} marker-end="url(#{mid})"{start}/>',
    ]
    if el.get("label") and el.get("labelPos"):
        label = el["label"]
        for a, b in subs.items():
            label = label.replace(a, b)
        out.append(
            f'<text x="{num(el["labelPos"][0])}" y="{num(el["labelPos"][1])}" '
            f'fill="{c["muted"]}" font-size="{num(s["arrowLabelSize"])}" text-anchor="middle" dominant-baseline="middle">{esc(label)}</text>'
        )
    return "".join(out)


def render_text(el, subs, c):
    text = el.get("text", "")
    for a, b in subs.items():
        text = text.replace(a, b)
    lines = text.split("\n")
    sz = el.get("size", 13) + 3 if el.get("size") is not None else 16
    lh = sz + 4
    start_y = el["y"] - ((len(lines) - 1) * lh) / 2
    fill = c["muted"] if el.get("muted") else c["text"]
    weight = ' font-weight="700"' if el.get("bold") else ""
    spacing = ' letter-spacing="0.06em"' if el.get("bold") and sz <= 12 else ""
    anchor = el.get("anchor", "middle")
    parts = []
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        parts.append(
            f'<text x="{num(el["x"])}" y="{num(start_y + i * lh)}" fill="{fill}" '
            f'font-size="{num(sz)}"{weight} text-anchor="{anchor}" dominant-baseline="middle"{spacing}>{esc(line)}</text>'
        )
    return "".join(parts)


OUT.mkdir(parents=True, exist_ok=True)
for src, (out_name, subs) in EXPORTS.items():
    d = DIAGRAMS[src]
    s = settings(d)
    for theme, c in THEMES.items():
        body = []
        for el in d["elements"]:
            if el["type"] == "box":
                body.append(render_box(el, s, subs, c))
            elif el["type"] == "arrow":
                body.append(render_arrow(el, out_name, s, subs, c))
            elif el["type"] == "text":
                body.append(render_text(el, subs, c))
        title = esc(TITLES.get(out_name, d.get("title", out_name)))
        svg = (
            f'<svg viewBox="{d["viewBox"]}" role="img" aria-label="{title}" xmlns="http://www.w3.org/2000/svg">'
            f"<style>{FONT_CSS}</style>"
            + "".join(body)
            + "</svg>"
        )
        path = OUT / f"{out_name}-{theme}.svg"
        path.write_text(svg)
    print(f"built {out_name} (light+dark)")
print("done")
