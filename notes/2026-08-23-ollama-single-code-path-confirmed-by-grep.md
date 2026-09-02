---
id: 2026-08-23-ollama-single-code-path-confirmed-by-grep
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify\"), given after reviewing an operator-facing review report covering all 7 (all read in full, all 6 unique cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi-hub, anansi-mcp, ollama, semantic-search, architecture]
sources:
  - ref: "Operator asks 'when do I need Ollama'; assistant says it will verify rather than guess, greps the codebase, and reports Ollama is used in exactly one place, embed() in anansi_hub.py, called only by /api/semantic and transitively by anansi_recall, which falls back to keyword search"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1291, 1295]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Ollama touches exactly one code path in the whole Anansi system, confirmed by grepping the codebase, and anansi_mcp.py independently implements the same semantic-first/keyword-fallback pattern
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1238-1324
- confidence: high, confirmed by grepping every Ollama reference across the codebase rather than reasoning from memory
- verified: 2026-08-23

## Body
When asked "when do I need Ollama," the assistant grepped the entire codebase for every Ollama reference instead of answering from general knowledge, and confirmed Ollama is used in exactly one place: the `embed()` function in `anansi_hub.py`. That function is called only by `semantic_search()` (backing the `/api/semantic` HTTP endpoint) and, transitively, by the `anansi_recall` MCP tool.

The specific detail confirmed here beyond "Ollama is optional": `anansi_mcp.py`'s own source independently implements the same graceful-degradation pattern as the HTTP side — `anansi_recall` tries semantic search first and falls back to keyword search if Ollama/semantic search is unavailable, rather than failing outright. Nothing else in the system (the rest of the dashboard, `anansi_search`, `anansi_read`, `anansi_capture`, the Hub server itself) touches Ollama at all. This makes Ollama purely optional quality-of-search infrastructure — it improves recall quality when running, and its absence degrades gracefully rather than breaking anything.

## Links
- related, 2026-08-23-anansi-hub-semantic-search-first-call-blocked-by-synchronous-full-corpus-embedding.md, covers a real outage-causing bug in the same `/api/semantic` code path this note describes; that note is about a latency/hang bug, this note is about the dependency's scope.
- related, 2026-08-08-terminal-glossary-semantic-search-needs-ollama-running.md, general prior note that semantic search needs Ollama; this note adds the exact confirmed code path and the anansi_mcp.py-specific fallback behavior.
