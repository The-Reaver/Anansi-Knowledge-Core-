---
id: the-fleet-s-recurring-defect-reproduced-at-the-level-of-the-org-chart-2026-09-01
type: lesson
status: candidate
source: "Brain Trust, 2026-09-01 — Amadeus (framing seat), confirmed against AJ_HARDWIRING.md, the ratified TYR notes and verify.py:529"
project: fleet
tags: [tyr, aj, unwired-gates, governance, self-diagnosis, org-chart, correction]
supersedes: []
superseded_by: null
---

# Chartering new enforcers while the ratified one was never built is the unwired-gate defect at org-chart scale

## Body

The fleet's most-repeated defect is: a correct mechanism is designed, committed, briefed — and invoked by
nothing. `omar_security_gate.py` exists, is tested, and is wired nowhere; `verify.py:529` says so in a
parenthetical. `hook_parity_gate.py` is declared in both `.pre-commit-config.yaml` and
`install-git-hooks.sh` and runs in no clone. `prepush.py`, the migration check and the attribution trailer
are on the same list.

The security-arsenal plan named this defect as its own justification, in a principle it stated twice:
*"safeguard existence does not imply invocation."*

Then it chartered two new fleet-internal security agents while **TYR — approved 2026-08-06 as lead Breaker
and Security Auditor, explicitly independent of the fleet — exists nowhere outside knowledge notes and one
line of `skills/stag-brain-trust/SKILL.md`.** The plan even conceded, in its §7, that the new pair has
weaker independence than the Breakers.

That is the same defect, one level up: rather than build the ratified, fleet-independent auditor, charter
two fleet-internal ones. The document diagnosed the pattern and did not notice it was committing it.

## The sharpest form of it

The plan's §7 cites `2026-08-06-tyr-never-certifies-itself-aj-plus-second-breaker-do` — status ratified —
to invoke TYR's independence doctrine, **on a review panel seated without TYR.**

## The check

Before chartering a new enforcement role, ask: *is there a ratified role that already covers this, and has
it been built?* If it exists on paper and not in the repository, building it is the cheaper and more
independent move than creating a new one. A new agent that answers to the fleet is weaker than an old one
that does not.
