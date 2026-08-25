---
id: 2026-08-07-ci-intelligence-pipeline-raw-feed-to-validated-rule
type: spec
status: ratified
source: Cowork session 2026-08-07, operator on phone; asked for the plan to gather valid compliance information that the lawyer then validates, to feed the Knowledge Core (source status: active); mined from candidates/2026-08-25/2026-08-07-compliance-intelligence-gathering-plan.md
project: ci
tags: [ci, pipeline, lawyer-review, provenance, knowledge-core]
---

# CI intelligence pipeline: ingest, relevance filter, candidate atomic note, change detection, lawyer review queue, live rule with re-review date

## Body

(1) Ingestion agents pull each feed on a schedule. (2) A relevance agent filters for medical-practice marketing, AI visibility, and patient data, and drops noise. (3) Each keeper becomes a candidate atomic note with source and date, status pending review. (4) Change detection diffs against existing rules and flags new, changed, or superseded. (5) The candidate lands in the Compliance Library as Pending review; the lawyer approves, edits, or rejects; approved becomes a live rule with the lawyer's certification and citation. (6) Each rule carries a re-review date and re-flags automatically when its source updates. (7) Provenance: every rule links to its source document and the certifying lawyer.

## Links

- extends: 2026-08-07-ci-intelligence-source-tiers-locked
