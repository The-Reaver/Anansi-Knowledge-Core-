---
id: 2026-08-20-hub-api-not-running-2026-08-20-session
type: note
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 7/10 on the promotion rubric (novelty 2, evidence 2, actionability 1, generality 0, non-contradiction 2). Directly observed at session start; note the Hub is running again by the time of this ratification pass. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, tooling]
sources:
  - ref: "This session's own review, verification, and gate-closure work, 2026-08-20"
    reliability: high
    origin: "direct observation and verification, this session"
provenance:
  archive: research/knowledge-home/raw/2026-08-20-anansi-candidate-promotion-and-gate-closure-session.jsonl
  turns: [1, 20]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The local Anansi Hub dashboard API was not running for most of this review session, so candidate review and promotion was done by direct file access instead

## Body

During this review session, the local Anansi Hub dashboard API, normally reachable at http://localhost:8787 and the preferred way to search and read the Knowledge Core, was not running. All candidate review and promotion work was instead done by reading and writing the underlying markdown files directly, per the anansi-promote skill's documented fallback order (MCP tools, then the local Hub API if running, then direct file access).

## Links
(none)
