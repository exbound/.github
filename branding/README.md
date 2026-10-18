# Exbound brand

Source of truth for the Exbound visual identity. Edit `source/`, run the build,
commit the regenerated `generated/`. Other repositories consume the released
assets here — they do not redraw the logo.

## Identity

- **Mark** — a bound stack of three bars (a closed boundary) with an accent
  arrow breaking up and out through the top: *ex-bound*, beyond the boundary.
- **Wordmark** — lowercase `exbound`, IBM Plex Sans SemiBold, outlined to paths
  so it renders without the font installed.
- **Accent** — signal chartreuse `#BEDA60` on graphite `#22262B`, over a
  warm-white `#F7F4EE` canvas.

## Colors

| Token      | Hex       | Use                                                     |
|------------|-----------|---------------------------------------------------------|
| Ink        | `#22262B` | text, mark, dark bands                                  |
| Warm white | `#F7F4EE` | canvas, inverse mark                                    |
| Surface    | `#FFFDF9` | cards / raised surfaces                                 |
| Accent     | `#BEDA60` | arrow, CTAs, small accents — a fill behind dark text    |
| Link blue  | `#35618E` | functional links and focus                              |

Accent contrast on ink is 9.7:1. It is a background for dark text, **never** a
text color on the pale canvas (≈1.4:1).

## Type

IBM Plex Sans for the wordmark and body; IBM Plex Mono for versions, hashes,
status and eyebrow labels. Self-host where used; the published wordmark is
outlined, so rendering the mark needs no font.

## Files

- `source/` — editable masters: `mark.svg`, `wordmark.svg`, `favicon.svg`,
  `palette.json`. **Edit these.**
- `generated/` — built variants (mark light/inverse/mono, lockups, favicon +
  `.ico`, avatar, apple-touch, social preview). Do not hand-edit.
- `scripts/build.py` — regenerates `generated/` from `source/`.
- `scripts/check.py` — verifies tools, outputs and SVG reproducibility.
- `scripts/mockup.py` — optional in-context preview (header/hero/band).

## Rebuild

Needs `rsvg-convert` (librsvg2-bin) and ImageMagick (`magick`).

    python3 scripts/build.py      # regenerate generated/
    python3 scripts/check.py      # verify tools, outputs, reproducibility

## Usage

- Org avatar: `generated/mark-avatar-512.png`.
- Profile README / site header: `generated/lockup.svg` (light) or
  `generated/lockup-inverse.svg` (dark).
- Favicon: `generated/favicon.svg` + `favicon.ico`; Apple touch:
  `apple-touch-icon-180.png`.
- Social preview: `generated/social-preview-1280x640.png`.
- One-color / print: `generated/mark-mono.svg`.

The wordmark is outlined IBM Plex Sans SemiBold; it is not a commissioned
custom letterform. No vendor assets are used.
