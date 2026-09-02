---
id: 2026-08-21-phased-sonny-diagnostic-scope-decision
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, decision, usage-management, scoping]
sources:
  - ref: "Turns 22-26 and 44: the agent proposes a two-phase plan (cheap Phase 1 metadata pass now, deep Phase 2 code review deferred to after a usage reset), the operator approves it, and turn 44 confirms Phase 1 completed with Phase 2 explicitly deferred."
    reliability: high
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [22, 44]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The SONNY/ShopOnlineNewYork diagnostic was scoped as a cheap Phase 1 now, deep Phase 2 deferred to after a usage reset
- id: 2026-08-21-phased-sonny-diagnostic-scope-decision
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, explicit operator approval ("save the org map and go with your rec") followed by the described Phase 1 execution
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, decision, usage-management, scoping

## Body

For the ShopOnlineNewYork/SONNY assessment, the operator was usage-conscious and wanted to weigh timing against a Friday quota reset. The agent proposed and the operator approved a two-phase plan: Phase 1, a cheap health/security/dependency/git-bloat pass across the 7 active repos plus a "safe to archive" list for the ~15 dead ones, executed immediately using GitHub API metadata only (no cloning); Phase 2, a deep per-language code/architecture/dependency-CVE/test-coverage review of the active repos (starting with `SonnyBackEndRepo` and `SonnyNY`), deferred until after the operator's usage reset. A full-depth diagnostic across all 22 repos was explicitly considered and rejected as expensive and mostly wasted, since roughly 15 of the 22 are dead duplicates whose deep review would yield little value. Phase 1 was completed in this session (2026-08-01); Phase 2 was not started as of session end.

REVIEW: high-impact

## Links
- relates-to, 2026-08-21-shallow-clone-decouples-repo-size-from-diagnostic-cost.md, the cost reasoning behind this scoping.
- relates-to, 2026-08-21-assistant-cannot-see-users-usage-quota.md, the constraint that drove the phasing.
