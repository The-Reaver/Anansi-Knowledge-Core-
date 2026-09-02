---
id: 2026-08-21-assistant-cannot-see-users-usage-quota
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [agent-capability-limit, usage-quota, self-awareness]
sources:
  - ref: "Turns 12-22: the assistant explicitly disclaims visibility into the operator's Claude usage quota or reset timing three separate times across the session, with consistent phrasing each time."
    reliability: high
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [12, 22]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The agent cannot see the operator's Claude usage quota or reset amount from within a session
- id: 2026-08-21-assistant-cannot-see-users-usage-quota
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, agent stated this limitation explicitly and consistently across the session
- verified: 2026-08-21
- tags: agent-capability-limit, usage-quota, self-awareness

## Body

The agent has no visibility into the operator's Claude token/usage quota or the size of a scheduled usage reset from within a session — that information exists only in the operator's Claude account/billing UI, not in anything observable in-session. When the operator wanted to time a large diagnostic job (the SONNY/ShopOnlineNewYork org assessment) around a "Friday reset," the agent could scope and estimate the shape of the job's cost (distinguishing a cheap metadata-only tier from an expensive deep-code-review tier) but explicitly could not tell the operator whether they had enough quota left to proceed immediately. This is a durable capability boundary, not specific to this task.

## Links
- relates-to, 2026-08-21-phased-sonny-diagnostic-scope-decision.md, the decision this limitation shaped.
