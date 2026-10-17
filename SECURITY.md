# Security Policy

This policy covers two things: the security of Exbound's own code, and the
legal/ethical scope that keeps the project defensible.

## Reporting a vulnerability in Exbound code

Report privately through GitHub's private vulnerability reporting — the
**"Report a vulnerability"** button on the **Security** tab of the affected
repository. If that isn't available, contact a maintainer directly (see
[SUPPORT](SUPPORT.md)). Do not open a public issue for an unfixed vulnerability.

Include the repository and version, what an attacker can do, and a reproduction.
We'll acknowledge the report, agree on a disclosure timeline, and credit you if
you'd like.

Exbound ships tools that analyze untrusted binaries and files. Treat any sample
under analysis as hostile input; analysis and build jobs for contributed
binaries must run unprivileged, with no access to repository secrets or write
tokens.

## Project scope and lawful use

Exbound exists for interoperability and preservation, and that boundary is what
keeps it lawful. Contributors and maintainers must:

- Work only from **lawfully held** copies of any proprietary software or data.
- Follow a documented clean-room method; copy no vendor code, artwork, or
  trademarks.
- Not circumvent DRM, dongles, or activation on currently sold software to
  enable unlicensed use, and not distribute circumvention tools.
- Never upload proprietary installers, license files, or sensitive laboratory
  data to a public repository.

The full legal analysis, including the interoperability case law this rests on,
is in the research
[legal basis](https://github.com/exbound/research/blob/main/docs/legal-basis.md).
It is orientation, not legal advice.

## Reporting misuse

If you believe an Exbound repository or contributor is crossing that boundary —
redistributing vendor binaries, circumventing protections, or publishing
copyrighted vendor assets — report it the same way as a vulnerability so a
maintainer can act.
