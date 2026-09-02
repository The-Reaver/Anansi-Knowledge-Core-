---
id: 2026-08-21-shallow-clone-decouples-repo-size-from-diagnostic-cost
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision, citation corrected to drop turn 22 (which does not itself mention shallow clones). Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, technique, usage-efficiency, unverified]
sources:
  - ref: "Turns 16 and 24: the agent argues a shallow clone excluding build artifacts would keep a deep code review of a bloated repo down to a few MB of actual reading; this reasoning justified the Phase 1/Phase 2 scoping but the claim was never exercised, since Phase 2's deep review did not run in this session. Turn 22, previously also cited alongside 16 and 24, does not itself mention shallow clones and has been dropped from this citation on Brain Trust review."
    reliability: medium
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [16, 24]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Claim: a shallow clone excluding build artifacts keeps deep code review cheap even for a bloated repo — untested this session
- id: 2026-08-21-shallow-clone-decouples-repo-size-from-diagnostic-cost
- type: finding
- status: ratified
- class: believed-unconfirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: medium, this was the agent's stated reasoning for the Phase 2 plan, but Phase 2 (the deep review that would exercise a shallow clone) was deferred and never actually run in this session, so the claim was not exercised or verified here
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, technique, usage-efficiency, unverified

## Body

The agent argued that a large on-disk repo size does not have to drive the cost of a deep code-level diagnostic, because a shallow clone that excludes `node_modules`/build artifacts would reduce what actually needs to be read down to a few MB even for a multi-gigabyte repo. This reasoning was used to reassure the operator (who was worried about usage/quota) and to justify proceeding with a "Phase 1" cheap pass despite ShopOnlineNewYork's `SonnyNY` (~1 GB) and legacy Flutter repo (~712 MB) being heavily bloated. Note that this specific claim was not tested in this session: the deep "Phase 2" code review that would have required an actual shallow clone was deferred to after the operator's usage reset and never executed, so whether the approach holds up in practice remains unverified from this transcript.

## Links
- relates-to, 2026-08-21-phased-sonny-diagnostic-scope-decision.md, the plan this reasoning supported.
