---
id: 2026-08-23-anansi-hub-api-gained-candidates-ratify-reject-endpoints
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i hereby ratify these notes\"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi, anansi-hub, api, http-server, knowledge-core, ratification]
sources:
  - ref: "Assistant greps anansi_hub.py's do_GET/do_POST handlers directly and reports /api/candidates, /api/ratify, /api/reject as real endpoints added this session, not documented in the skill or the 2026-08-09 architecture note (line 893), then confirms the skill file update against the actual handlers (line 897)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [890, 897]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# `anansi_hub.py`'s HTTP API grew three new endpoints this session — `/api/candidates`, `/api/ratify`, `/api/reject` — the real mechanism for moving a capture from raw into the trusted Core, not previously documented in the hub's architecture reference note

## Body
- class: believed-unconfirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 784-900
- confidence: medium — confirmed by grepping `anansi_hub.py`'s `do_GET`/`do_POST` handlers directly during this stretch, but this note relies on that grep being described accurately rather than re-reading the handler code itself
- verified: 2026-08-23

The existing architecture-reference note for `anansi_hub.py` (dated 2026-08-09) documents only one data endpoint, `GET /api/data`, plus an optional `/api/semantic`. While updating the `anansi` skill file's documentation this session, the operator's request to fix outdated skill content prompted a direct check of `anansi_hub.py`'s actual request handlers rather than trusting the skill file's existing text, and found three endpoints the skill (and the older architecture note) did not mention: `/api/candidates`, `/api/ratify`, and `/api/reject`. These were described as having been added this session and as the real, live mechanism for moving a capture out of the raw archive and into the permanent Core (`research/knowledge-home/notes/`) — i.e., an operational alternative to (or wrapper around) the `ratify.py` CLI script used elsewhere in this same session's work.

This note is marked `believed-unconfirmed` because it is based on a description of a grep result reported in the same conversation turn, not on this distillation pass independently re-reading `anansi_hub.py`'s source. A future agent relying on this should re-verify the endpoints' exact request/response shape directly against `anansi_hub.py` before building on them.

## Links
- extends, 2026-08-09-anansi-hub-architecture-reference.md — that note's endpoint list (`/api/data`, `/api/semantic`) is now incomplete; this note adds the three endpoints found missing, without restating the rest of that note's still-accurate architecture facts.
- relates, 2026-08-22-ratify-py-cli-missing-underscore-folder-exclusion-dashboard-had.md — the CLI-side ratification tooling in the same system this HTTP API also covers.
