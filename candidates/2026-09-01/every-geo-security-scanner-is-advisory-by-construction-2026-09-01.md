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

# GEO's security *scanners* are dashboards, not barriers, and one runs unpinned upstream code

## Body

**Verified.** `security-scan.yml` sets `continue-on-error: true` on Nuclei and `fail_action: false`
on ZAP, and its own step summary prints: *"Neither job fails the build on findings."*
`cfr-watch.yml` is `continue-on-error: true` as well.

So the *scanning* surface the fleet points to as evidence of security posture cannot fail a build. A
finding produces a report nobody is required to read. Under the Core's own standard —
*an unperformed check is not a clean check* — a check whose result cannot block is closer to
unperformed than to passing.

**Compounding it:** `uses: projectdiscovery/nuclei-action@main` is pinned to a **mutable branch**
while every other action in the four workflows is at least tag-pinned. Whatever sits on that branch
at run time executes inside a repository whose Actions secrets include the Railway production
token.

**The distinction to hold:** *advisory* is a legitimate posture for a noisy new scanner during a
measured observation window. It is not a legitimate permanent state, and nothing here records when
or whether these were meant to graduate.

## CORRECTION — 2026-09-01, cold security review F3 and F4, ratified in BRAIN_TRUST_DECISION_RECORD_2026-09-01

Two claims in the original note overreached and are withdrawn. What is verified above stands.

**Withdrawn 1 — GEO is not without a blocking CI check.** The original framing invited the reading,
carried into the v2 plan as the flat claim "GEO has no PR gate," that GEO's CI cannot fail. It can.
`the-geo-suite-/.github/workflows/tests.yml:29-33` is `on: push: branches:[main]` **and
`pull_request:`**, running `pip install -e "backend/.[dev]"` then `python -m pytest -q` with **no**
`continue-on-error`. It is a PR-triggered, hard-failing check. `deploy-verify.yml` is a second real
gate — its own header reads *"This is a real gate, not a visibility-only job… a BLOCKER fails the job
outright."* What GEO lacks is **branch protection requiring** those checks — a different claim with a
different remedy, and one this session could not verify from a clone.

**Withdrawn 2 — the dependency sentence described the wrong repository.** GEO has **no
`requirements.txt`**. Its manifests are `backend/pyproject.toml`, where all thirteen runtime
dependencies are range-bounded (`fastapi>=0.111,<1.0` … `weasyprint>=69,<70`), and
`frontend/package-lock.json`, which is a lockfile and which `frontend/Dockerfile` consumes via
`npm ci`. The file pinning 2 of 10 is **Stag-Fleet's** `requirements.txt`, and Stag-Fleet has no CI and
nothing Railway deploys. This note is tagged `project: geo` and made a Stag-Fleet claim.

The real GEO supply-chain finding is narrower and survives: `backend/pyproject.toml` carries a security
floor `pyjwt[crypto]>=2.13.0` whose own comment concedes it is *"not enforced mechanically… a bare
`pip install .` with no lockfile resolves whatever is newest on PyPI at build time."* Unbounded
resolution at every Railway rebuild is real. "No lockfile anywhere" is not.

## Links

- relates-to: the-real-attack-chain-runs-through-an-unprotected-main-not-the-code-2026-09-01
- relates-to: a-gate-that-does-not-declare-fail-open-or-fail-closed-cannot-be-audited-2026-08-31
- relates-to: the-documented-full-battery-command-reports-false-red-on-a-green-suite-2026-08-31
