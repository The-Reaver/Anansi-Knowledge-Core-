---
id: 2026-08-21-ci-json-store-blocks-go-live
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, persistence, database, go-live, deploy-blocker]
sources:
  - ref: "Agent's read of shared/workspace_store.py and its go-live sequencing naming the Postgres swap as step 4"
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (A)\" (backfilled from historical transcript c5583566, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-c5583566.jsonl
  turns: [189, 196]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — stated directly by the agent after reading shared/workspace_store.py
- verified: 2026-08-21
- REVIEW: high-impact

## Body
As of 2026-07-31, `projects/compliance_intelligence/shared/workspace_store.py` persists all client/engagement/finding data by rewriting one `clients.json` file on every change. The agent identified this as the concrete blocker standing between the current build and the operator's "move directly to testing it on a real database" request: a single rewritten JSON file won't survive a container redeploy and has no concurrency safety for multiple simultaneous users. The agent's sequenced go-live path names swapping this for a real Postgres schema (clients / engagements / evidence / runs / findings) as step 4, ahead of packaging and deploy. Until this swap happens, "real database" is not yet true of the running system regardless of what the crawler and rule engine can do.

## Links
- blocks, 2026-08-21-ci-live-crawl-endpoint-not-wired.md, both are prerequisites named the same session for taking CI from demo to production
