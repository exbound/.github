# Contributing to Exbound

Exbound builds independent, compatible, open reimplementations of proprietary
scientific and engineering software. This is the organization-wide contribution
policy. A repository with its own `CONTRIBUTING.md` (for example
[research](https://github.com/exbound/research)) overrides this one for that
repository, and each implementation repository carries an `AGENTS.md` describing
its specific architecture and commands.

## Ways to contribute

- **Evidence** — reproducible observations of what a reference product does:
  file samples, version details, manuals, computed outputs with the inputs that
  produced them. This is the scarce, high-value input, and you don't need to
  write code to provide it.
- **Implementation** — independent code for formats, numerical methods,
  instrument protocols, and applications, built against documented reference
  behavior.
- **Verification** — turning observed behavior into tests, and checking an
  implementation against them.

Research findings, format work, and behavioral specifications live in
[research](https://github.com/exbound/research). Implementation lives in
per-target repositories.

## The rule that matters most

**Never claim compatibility that has not been verified against documented
reference behavior.** A pull request must distinguish, explicitly:

1. what functionality it newly implements,
2. which tests it ran, and their result,
3. what reference evidence backs the behavior (and its source), and
4. what remains unverified or unimplemented.

This is worth far more than disclosing which model or tool you used. Every
contribution is reviewed as evidence, not trusted by default.

## Evidence standards

- Every claim carries the command, file, or source that produced it. No bare
  assertions.
- Mark each statement **ESTABLISHED** (cited or directly observed) or
  **HYPOTHESIS / NEEDS-OBSERVATION**. Don't promote one into the other.
- Report coverage as a triplet — reference *observed* / *implemented* /
  *verified* — and never report implementation as if it were verification. See
  the
  [capability model](https://github.com/exbound/research/blob/main/docs/capability-model.md).
- Negative results are welcome and held to the same standard: a format that
  can't yet be decoded, with the specific blocker, is a real contribution.

## Tests

Implementation repositories expose a standard command interface:

- `just test` — deterministic tests that need no proprietary software. These
  gate every pull request.
- `just test-reference` — optional tests against a licensed original application
  or a physical instrument. Never a hidden prerequisite: anyone can improve the
  implementation and run the default suite without owning the vendor software.

## Scope and legal boundary

Contributions must come from **lawfully held** copies and follow a documented
clean-room method where a proprietary original is involved. Do not copy vendor
code, UI artwork, icons, help text, or trademarks; describe compatibility
nominatively ("reads OriginPro projects," "<vendor>-compatible"), never by
naming an implementation after a product. Exbound does not circumvent DRM,
dongles, or activation to enable unlicensed use. Full analysis and case law:
research
[legal basis](https://github.com/exbound/research/blob/main/docs/legal-basis.md).

## Commits and pull requests

Conventional Commits (`type(scope): description`), one logical change per commit,
imperative mood. Describe what changed, not the process or tools that produced
it. Keep pull requests focused and reviewable, and fill in the pull-request
template's compatibility section.
