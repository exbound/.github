# Exbound

Independent, compatible, open reimplementations of proprietary, abandoned, and
monopolized scientific and engineering software.

Scientists and engineers lose work when the software that produced it is
discontinued, priced out of reach, or locked to hardware that still runs fine.
Exbound reconstructs that software in the open — not just readers for the file
formats, but working implementations of what the original *did*: open, edit,
compute, fit, graph, script, save, and run.

## What we build

An Exbound reconstruction is an independent application, built clean-room, that
is *compatible* with a proprietary original — it reads the native projects,
reproduces the computations, and runs the workflows, verified against documented
reference behavior. We describe a target by compatibility ("reads OriginPro
projects," "<vendor>-compatible"), never as a clone and never using a vendor's
branding.

Reconstruction is measured against a nine-part capability model (C1–C9:
acquisition, data, documents, computation, workflow, programmability, instrument
integration, the user-facing application, and overall replacement coverage)
rather than a single "done." See the
[capability model](https://github.com/exbound/research/blob/main/docs/capability-model.md).

## How the work is organized

- **[research](https://github.com/exbound/research)** — the public research
  program: the target inventory, per-target technical dossiers, verification
  methods, the legal basis, and prioritized work packages.
- **Implementation repositories** — one per target, created as each becomes
  ready, each with its own code, tests, and roadmap.
- **this `.github` repository** — organization-wide contribution, security, and
  governance policy.

## The first targets

Twelve scientific and engineering applications, chosen for user lock-in and
preservation value — materials testing, chromatography, spectroscopy, thermal
analysis, diffraction, and data analysis. The full inventory, with the objective
and initial technical approach for each, is in the
[research target inventory](https://github.com/exbound/research/blob/main/dossiers/README.md).
The pilot is an Origin-compatible data-analysis environment.

## How to contribute

You don't have to be a reverse engineer to help.

- **Scientists & instrument owners** — contribute representative files, software
  versions, manuals, and reproducible observations of what the original software
  does. (Never upload proprietary installers or sensitive lab data to a public
  repository.)
- **Developers & reverse engineers** — file formats, numerical methods,
  instrument protocols, and independent implementation.
- **AI-assisted contributors** — take a bounded, test-backed issue, reproduce
  the failing case, implement, verify, and submit with evidence.

Start with [CONTRIBUTING](https://github.com/exbound/.github/blob/main/CONTRIBUTING.md),
then the research program. Propose targets and ask research questions in
[research](https://github.com/exbound/research) — in its Discussions, or
via issues.

## Scope

Exbound works only on lawfully held copies, documents its clean-room method, and
copies no vendor code, artwork, or trademarks. It does not defeat DRM, dongles,
or activation on currently sold software. See
[SECURITY](https://github.com/exbound/.github/blob/main/SECURITY.md) and the
research
[legal basis](https://github.com/exbound/research/blob/main/docs/legal-basis.md).

Exbound is not affiliated with, authorized by, or endorsed by any software
vendor. Product names are used only to describe compatibility.
