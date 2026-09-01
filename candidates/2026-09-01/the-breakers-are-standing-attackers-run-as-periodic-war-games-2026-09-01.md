---
id: the-breakers-are-standing-attackers-run-as-periodic-war-games-2026-09-01
type: ruling
status: candidate
source: "Operator directive, 2026-09-01 — Abad, direct instruction in the Ambient Clinical Scribe planning session; grounded against the 2026-08-06 Breakers notes and AJ/AJ_HARDWIRING.md in The-Reaver/Stag-Fleet"
project: fleet
tags: [breakers, tyr, aj, war-games, red-team, penetration-testing, cadence]
supersedes: []
superseded_by: null
---

# The Breakers are a standing adversary on a schedule, not a one-time gauntlet a build passes once

## Body

Operator ruling, 2026-09-01: AJ's attacker agents are meant to be **constantly attacking our apps**
— building vicious tests designed to break them, trained to the standard of a professional
penetration-testing firm brought in to assess independently, and **improving at attacking over
time**. These runs happen **periodically, like war games**, and the fleet learns from each one.

This changes the existing design's shape rather than replacing it. The ratified
`2026-08-06-breakers-gauntlet-four-breaker-types-and-rules` already defines the attack surface —
**Security** (injection, auth bypass, data leaks, zero-day style), **Correctness** (edge cases and
weird inputs), **Scale** (floods until it falls over), and **Chaos** (killing parts mid-task to
hunt lost or corrupted data) — with rules that still stand: independent of the builder and the
fleet, attack the real work, log every break, **use different AI families so they fail
differently**, and a build passes only when the whole team comes up empty.

What was missing is **cadence and progression**. The gauntlet reads as a gate a build passes once.
The operator wants a standing adversary that gets better, on a rhythm, whose findings compound.
AJ's own charter already has the matching open item: it audits *"on a schedule no audited agent or
the Brain Trust can defer (schedule still to be set by the operator)"*. **These are the same
missing decision, and one cadence should serve both.**

**Two open points, deliberately not resolved here.** The operator recalls **two** attacker agents;
the ratified design specifies **four** Breaker types. Either two agents run four disciplines, or
two of the four were dropped — this needs the operator's call, not a silent reconciliation. And a
repo search found **no breaker scripts in `agents/`** — only `valen_secops.py`. The design is
detailed and, as far as the tracked repo shows, unimplemented: the fleet's dominant failure mode
again.

## Links

- extends: 2026-08-06-breakers-gauntlet-four-breaker-types-and-rules
- relates-to: 2026-08-06-tyr-lead-breaker-and-security-auditor-approved
- relates-to: a-hunting-team-closes-the-adversarial-loop-2026-09-01
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
