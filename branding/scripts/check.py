#!/usr/bin/env python3
"""Verify the Exbound brand build: tools present, outputs exist, SVGs reproducible."""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
GEN = HERE / "generated"
EXPECTED = [
    "mark.svg", "mark-inverse.svg", "mark-mono.svg", "mark-mono-inverse.svg",
    "favicon.svg", "lockup.svg", "lockup-inverse.svg", "lockup-mono.svg",
    "mark-avatar.svg", "mark-avatar-512.png", "mark-avatar-1024.png",
    "apple-touch-icon-180.png", "favicon-16.png", "favicon-32.png",
    "favicon-48.png", "favicon.ico", "lockup-1400.png",
    "social-preview.svg", "social-preview-1280x640.png",
]


def fail(msg: str) -> None:
    print("CHECK FAIL:", msg)
    sys.exit(1)


# 1. required rasterizers present (missing tool must fail, not skip)
for tool in ("rsvg-convert", "magick"):
    if not shutil.which(tool):
        fail(f"required tool missing: {tool}")

# 2. every declared output exists and is non-empty
for name in EXPECTED:
    p = GEN / name
    if not p.exists() or p.stat().st_size == 0:
        fail(f"missing or empty output: {name}")

# 3. SVG outputs reproduce byte-for-byte from a clean rebuild
tmp = Path(tempfile.mkdtemp(prefix="exbrand-"))
try:
    subprocess.run([sys.executable, "-I", str(HERE / "scripts" / "build.py"), str(tmp)],
                   check=True, stdout=subprocess.DEVNULL)
    svgs = [n for n in EXPECTED if n.endswith(".svg")]
    for n in svgs:
        if (GEN / n).read_bytes() != (tmp / n).read_bytes():
            fail(f"non-reproducible: committed {n} differs from a clean rebuild")
finally:
    shutil.rmtree(tmp, ignore_errors=True)

print(f"CHECK OK: {len(EXPECTED)} outputs present, {len(svgs)} SVGs reproducible")
