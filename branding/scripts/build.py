#!/usr/bin/env python3
"""Deterministic Exbound brand asset build (rsvg-convert + ImageMagick)."""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SRC = HERE / "source"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "generated"
OUT.mkdir(parents=True, exist_ok=True)

P = json.loads((SRC / "palette.json").read_text())
INK, LIGHT, ACC = P["ink"], P["warm_white"], P["accent"]


def inner(svg: str) -> str:
    return svg[svg.index(">") + 1 : svg.rindex("</svg>")]


def recolor(s: str, ink: str, acc: str) -> str:
    return s.replace(INK, ink).replace(ACC, acc)


def write_svg(name: str, s: str) -> None:
    (OUT / name).write_text(s.strip() + "\n", encoding="utf-8")


def rasterize(svg_path: Path, png: str, w: int, h: int | None = None) -> None:
    cmd = ["rsvg-convert", "-w", str(w)]
    if h:
        cmd += ["-h", str(h)]
    cmd += [str(svg_path), "-o", str(OUT / png)]
    subprocess.run(cmd, check=True)


mark = (SRC / "mark.svg").read_text().strip()
fav = (SRC / "favicon.svg").read_text().strip()
word = (SRC / "wordmark.svg").read_text().strip()
mark_inner = inner(mark)
word_inner = inner(word)
vb = re.search(r'viewBox="([\d.\s]+)"', word).group(1).split()
vw = float(vb[2])
vh = float(vb[3])

# --- mark color variants (viewBox 0 0 100 100) ---
for name, ink, acc in [
    ("mark.svg", INK, ACC),
    ("mark-inverse.svg", LIGHT, ACC),
    ("mark-mono.svg", INK, INK),
    ("mark-mono-inverse.svg", LIGHT, LIGHT),
]:
    write_svg(name, recolor(mark, ink, acc))

write_svg("favicon.svg", fav)

# --- horizontal lockups (nested SVG keeps each viewBox intact) ---
# The mark is cropped to its content box and baseline-aligned with the wordmark,
# so their cap heights match instead of the mark carrying its icon padding.
MARK_VB = "11 20 78 61"
MCW, MCH = 78.0, 61.0
WH = 150.0
WW = WH * vw / vh
MKH = WH * 0.98
MKW = MKH * MCW / MCH
PAD = 18.0
GAP = 44.0
LOCK_H = round(WH + 2 * PAD)
MARK_X = PAD
MARK_Y = LOCK_H - PAD - MKH
WORD_X = MARK_X + MKW + GAP
WORD_Y = LOCK_H - PAD - WH
lock_w = round(WORD_X + WW)


def lockup(ink: str, acc: str) -> str:
    mi = recolor(mark_inner, ink, acc)
    wi = word_inner.replace(INK, ink)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{lock_w}" height="{LOCK_H}" '
        f'viewBox="0 0 {lock_w} {LOCK_H}" role="img" aria-label="exbound">'
        f'<svg x="{MARK_X:.1f}" y="{MARK_Y:.1f}" width="{MKW:.1f}" height="{MKH:.1f}" '
        f'viewBox="{MARK_VB}">{mi}</svg>'
        f'<svg x="{WORD_X:.1f}" y="{WORD_Y:.1f}" width="{WW:.1f}" height="{WH:.1f}" '
        f'viewBox="0 0 {vw} {vh}">{wi}</svg></svg>'
    )


write_svg("lockup.svg", lockup(INK, ACC))
write_svg("lockup-inverse.svg", lockup(LIGHT, ACC))
write_svg("lockup-mono.svg", lockup(INK, INK))

# --- plated square avatar (inverse mark on graphite) ---
avatar = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">'
    f'<rect width="512" height="512" rx="96" fill="{INK}"/>'
    f'<svg x="106" y="106" width="300" height="300" viewBox="0 0 100 100">'
    f"{recolor(mark_inner, LIGHT, ACC)}</svg></svg>"
)
write_svg("mark-avatar.svg", avatar)
rasterize(OUT / "mark-avatar.svg", "mark-avatar-512.png", 512, 512)
rasterize(OUT / "mark-avatar.svg", "mark-avatar-1024.png", 1024, 1024)
rasterize(OUT / "mark-avatar.svg", "apple-touch-icon-180.png", 180, 180)

# --- favicons + ICO ---
for i in (16, 32, 48):
    rasterize(OUT / "favicon.svg", f"favicon-{i}.png", i, i)
subprocess.run(
    ["magick", str(OUT / "favicon-16.png"), str(OUT / "favicon-32.png"),
     str(OUT / "favicon-48.png"), str(OUT / "favicon.ico")],
    check=True,
)

rasterize(OUT / "lockup.svg", "lockup-1400.png", 1400)

# --- social preview 1280x640 (graphite panel, inverse lockup) ---
og = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640">'
    f'<rect width="1280" height="640" fill="{INK}"/>'
    f'<rect x="80" y="118" width="14" height="404" fill="{ACC}"/>'
    f'<svg x="122" y="150" width="760" height="140" viewBox="0 0 {lock_w} {LOCK_H}">'
    f"{recolor(inner(lockup(INK, ACC)), LIGHT, ACC)}</svg>"
    f'<text x="124" y="430" font-family="DejaVu Sans, sans-serif" font-size="52" '
    f'font-weight="700" fill="{LIGHT}">Science should outlive its software.</text>'
    f'<text x="124" y="492" font-family="DejaVu Sans, sans-serif" font-size="28" '
    f'fill="#C9CFCC">Open, compatible reconstructions of scientific software.</text></svg>'
)
write_svg("social-preview.svg", og)
rasterize(OUT / "social-preview.svg", "social-preview-1280x640.png", 1280, 640)

print("generated", len(list(OUT.iterdir())), "files in", OUT)
