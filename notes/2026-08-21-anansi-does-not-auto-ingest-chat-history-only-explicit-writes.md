---
id: 2026-08-21-anansi-does-not-auto-ingest-chat-history-only-explicit-writes
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, mcp, knowledge-core, closeout, structural-lesson]
sources:
  - ref: "Turns 3-4: operator asks whether restarting the session would lose this chat's content; assistant confirms Anansi's Core only reflects what's written to disk as notes, does not ingest chat history automatically, and invokes the stag-closeout skill to archive the session before the restart."
    reliability: high
    origin: "STAG session, 2026-08-21, \"Anansi local API + MCP registration\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-anansi-hub-mcp-setup-and-closeout.jsonl
  turns: [3, 4]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Anansi's Knowledge Core never automatically ingests chat history — only content explicitly written to disk becomes part of it
- class: confirmed
- source: STAG session, 2026-08-21, "Anansi local API + MCP registration"
- confidence: high
- verified: 2026-08-21
- structural-lesson: registering a plug (the MCP server) is not the same operation as writing knowledge through it; an operator can reasonably but wrongly assume the two are the same act.

## Body

Registering the Anansi MCP server (or having the Hub API running) does not, by itself, capture anything from a conversation into the Knowledge Core. Anansi only knows what exists as note files on disk under `research/knowledge-home/`. A chat session's reasoning, debugging steps, and decisions are ephemeral unless something explicitly writes them out — via `anansi_capture` (an MCP tool call), a direct POST to `/api/capture`, or a closeout pass like the `stag-closeout` skill that archives the raw transcript and drafts candidate atomic notes.

Consequence observed directly in this session: after registering the MCP server and confirming the Hub API was reachable, restarting the Claude Code session (needed for the newly-registered `anansi_recall`/`anansi_capture` tools to appear at all, see [[2026-08-21-mcp-server-registration-mid-session-requires-restart-to-take-effect]]) would have silently discarded the entire session's content — including the backslash-path bug and its fix — if the `stag-closeout` skill had not been run first to archive the raw transcript and harvest atomic notes before the restart.

Practical rule: before restarting or closing a session that did substantive work, capture first (closeout or explicit `anansi_capture` calls), restart second. The order is not interchangeable.

## Links
- extends, 2026-08-21-mcp-server-registration-mid-session-requires-restart-to-take-effect.md, the restart requirement that makes this ordering matter in practice.
