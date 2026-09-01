---
id: every-geo-security-scanner-is-advisory-by-construction-2026-09-01
type: finding
status: candidate
source: "Recovery session, 2026-09-01 — adversarial panel (AJ, Hestia, Bayamanaco) against docs/specs/2026-09-01-security-arsenal-integration-plan.md; this finding independently re-verified against the repositories by the session relaying it"
project: geo
tags: [ci, scanners, fail-open, advisory, supply-chain, security]
supersedes: []
superseded_by: null
---

# GEO's security scanners are dashboards, not barriers, and one runs unpinned upstream code

## Body

**Verified.** `security-scan.yml` sets `continue-on-error: true` on Nuclei and `fail_action: false`
on ZAP, and its own step summary prints: *"Neither job fails the build on findings."*
`cfr-watch.yml` is `continue-on-error: true` as well.

So the scanning surface the fleet points to as evidence of security posture cannot fail a build. A
finding produces a report nobody is required to read. Under the Core's own standard —
*an unperformed check is not a clean check* — a check whose result cannot block is closer to
unperformed than to passing.

**Compounding it:** `uses: projectdiscovery/nuclei-action@main` is pinned to a **mutable branch**
while every other action in the four workflows is at least tag-pinned. Whatever sits on that branch
at run time executes inside a repository whose Actions secrets include the Railway production
token. And the fleet's Python dependencies are largely unpinned with no lockfile — Railway rebuilds
from them on deploy, so a single compromised upstream release reaches production with the full
production environment, needing no repository access at all.

**The distinction to hold:** *advisory* is a legitimate posture for a noisy new scanner during a
measured observation window. It is not a legitimate permanent state, and nothing here records when
or whether these were meant to graduate.

## Links

- relates-to: the-real-attack-chain-runs-through-an-unprotected-main-not-the-code-2026-09-01
- relates-to: a-gate-that-does-not-declare-fail-open-or-fail-closed-cannot-be-audited-2026-08-31
- relates-to: the-documented-full-battery-command-reports-false-red-on-a-green-suite-2026-08-31
