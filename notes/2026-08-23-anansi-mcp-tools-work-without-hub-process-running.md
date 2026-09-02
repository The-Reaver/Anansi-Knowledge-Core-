---
id: 2026-08-23-anansi-mcp-tools-work-without-hub-process-running
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify\"), given after reviewing an operator-facing review report covering all 7 (all read in full, all 6 unique cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi-hub, anansi-mcp, architecture, operations]
sources:
  - ref: "Assistant runs a live anansi_status check before an agent_breakers run and finds the Hub isn't currently running, starts it only to run the HTTP test itself (lines 1146-1147), consistent with the MCP tools' disk-fallback behavior described separately at lines 1289-1290"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1146, 1150]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Most Anansi MCP tools don't require the Hub server process to be running at all — they fall back to reading files directly from disk

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1238-1324
- confidence: high, confirmed via a live `anansi_status` check performed in this session with the Hub not running
- verified: 2026-08-23

The operator asked how to instruct other chat sessions to run the Hub. Part of the answer, confirmed live rather than assumed: most day-to-day Anansi usage doesn't actually need the Hub process (`python anansi_hub.py`) running at all. The MCP tools (`anansi_recall`, `anansi_capture`, `anansi_search`, `anansi_read`, etc.) fall back to reading and writing files directly on disk when the Hub isn't up. This was confirmed via a live `anansi_status` check in this session that returned "Anansi Hub dashboard is not running... Everything still works."

The Hub process itself is only needed for: the browsable dashboard UI, the HTTP API (`/api/*` endpoints), and semantic search (which needs Ollama warmed up through the Hub's `embed()` function). Plain keyword-based recall and capture work with no Hub process at all.

## Links
- related, 2026-08-23-anansi-hub-single-instance-enforced-by-disabled-port-reuse.md, same conversational thread about running the Hub across multiple chat sessions.
- related, 2026-08-09-anansi-hub-stats-without-running-server.md, a different angle on the same theme — that note covers replicating the Hub's own stats-compute logic without a running server; this note covers the MCP tools' own built-in disk fallback.
