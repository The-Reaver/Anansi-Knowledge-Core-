---
id: 2026-08-23-dashboard-ratify-page-and-graph-color-sliders-committed-after-hub-restart
type: decision
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify this\"), given after reviewing an operator-facing review report covering all 6 (all read in full, all 6 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi-hub, dashboard, ratify, graph-mission-control, commit-hygiene, provenance]
sources:
  - ref: "Assistant finds anansi_hub.py's diff is bigger than its own fix, identifies the extra code as the pre-existing Ratify page + Graph color-shade sliders, reasons it's safe to commit given independent provenance evidence, and confirms commit 6ddbf1a pushed"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1226, 1232]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Anansi Hub dashboard's Ratify page and two Graph Mission Control color-shade sliders were committed once the Hub restart needed to fix the semantic-search hang finally made a restart possible
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1085-1237
- confidence: high, verified against independent provenance evidence in already-swept-in notes before committing, and done at the operator's explicit direction
- verified: 2026-08-23

## Body
Fixing the `/api/semantic` synchronous-embedding hang (recorded separately) required restarting the Hub process to pick up the code change. In the course of doing that, the assistant found that `anansi_hub.py` already carried a larger uncommitted diff than just its own fix. Diffing what was pre-existing against what it had just added, the extra code turned out to be the dashboard's Ratify page — a `GET /api/candidates` endpoint plus `POST /api/ratify` and `POST /api/reject` endpoints, built to reuse the existing `scripts/knowledge_home/ratify.py` functions rather than reimplement ratification logic — and two new Graph Mission Control sliders controlling orb and link color shade. Both had been built and tested earlier in the same session but never committed, because the real Hub process could not be restarted at the time to actually exercise the change end-to-end.

Rather than commit this blind, the assistant checked for independent evidence the code path had already run correctly in production: several GEO Suite Knowledge Core notes swept into the Core earlier in this same session carry a "ratified via the Anansi Hub dashboard" provenance line, which is only possible if this exact Ratify-page code had already executed successfully against real data. On that basis, the dashboard feature and slider code were committed together with the unrelated `/api/semantic` fix in the same commit, rather than left sitting uncommitted indefinitely for lack of a matching restart window. (The harness timeout fix from earlier in the session was committed separately, as commit `52f7e46`; this dashboard-plus-semantic-fix commit followed as `6ddbf1a`.)

## Links
- relates, 2026-08-23-anansi-hub-semantic-search-first-call-blocked-by-synchronous-full-corpus-embedding.md, the fix that forced the Hub restart which surfaced this pending, uncommitted work
