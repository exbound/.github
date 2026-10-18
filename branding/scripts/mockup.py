#!/usr/bin/env python3
"""Compose an in-context brand mockup (header + hero + CTA + method band)."""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
GEN = HERE / "generated"
INK, LIGHT, SURF, ACC, LINK, SOFT = "#22262B", "#F7F4EE", "#FFFDF9", "#BEDA60", "#35618E", "#5B6169"


def inner(s):
    return s[s.index(">") + 1 : s.rindex("</svg>")]


lock = (GEN / "lockup.svg").read_text()
lock_vb = re.search(r'viewBox="([\d.\s]+)"', lock).group(1).split()
lw, lh = float(lock_vb[2]), float(lock_vb[3])
# header lockup target height 34
hh = 34
hw = lw * hh / lh
F = "IBM Plex Sans, sans-serif"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 760">
<rect width="1200" height="760" fill="{LIGHT}"/>
<!-- header -->
<rect x="0" y="0" width="1200" height="86" fill="{SURF}"/>
<line x1="0" y1="86" x2="1200" y2="86" stroke="#E3DDD2" stroke-width="1"/>
<svg x="48" y="{43 - hh/2:.1f}" width="{hw:.1f}" height="{hh}" viewBox="0 0 {lw} {lh}">{inner(lock)}</svg>
<g font-family="{F}" font-size="17" fill="{SOFT}">
  <text x="880" y="51">Projects</text><text x="985" y="51">Research</text><text x="1095" y="51">Contribute</text>
</g>
<!-- hero -->
<text x="56" y="210" font-family="IBM Plex Mono, monospace" font-size="15" letter-spacing="3" fill="{SOFT}">OPEN SCIENTIFIC SOFTWARE, RECONSTRUCTED</text>
<text x="52" y="300" font-family="{F}" font-weight="bold" font-size="66" fill="{INK}">Science should outlive</text>
<text x="52" y="376" font-family="{F}" font-weight="bold" font-size="66" fill="{INK}">its software.</text>
<text x="56" y="432" font-family="{F}" font-size="22" fill="{SOFT}">Independent, compatible, open reconstructions of the proprietary tools</text>
<text x="56" y="463" font-family="{F}" font-size="22" fill="{SOFT}">that researchers and engineers depend on.</text>
<rect x="56" y="500" width="232" height="56" rx="10" fill="{ACC}"/>
<text x="172" y="535" font-family="{F}" font-weight="bold" font-size="19" fill="{INK}" text-anchor="middle">Explore targets</text>
<rect x="304" y="500" width="214" height="56" rx="10" fill="none" stroke="#CFC7B8" stroke-width="1.5"/>
<text x="411" y="535" font-family="{F}" font-size="19" fill="{INK}" text-anchor="middle">Contribute evidence</text>
<!-- method band -->
<rect x="0" y="620" width="1200" height="140" fill="{INK}"/>
<text x="56" y="668" font-family="IBM Plex Mono, monospace" font-size="14" letter-spacing="3" fill="{ACC}">HOW COMPATIBILITY IS ESTABLISHED</text>
<g font-family="{F}" font-weight="bold" font-size="26" fill="{LIGHT}">
  <text x="56" y="712"><tspan fill="{ACC}" font-family="IBM Plex Mono, monospace" font-size="20">01</tspan>  Observe</text>
  <text x="456" y="712"><tspan fill="{ACC}" font-family="IBM Plex Mono, monospace" font-size="20">02</tspan>  Implement</text>
  <text x="856" y="712"><tspan fill="{ACC}" font-family="IBM Plex Mono, monospace" font-size="20">03</tspan>  Verify</text>
</g>
</svg>"""
out = GEN / "mockup.svg"
out.write_text(svg)
print("wrote", out)
