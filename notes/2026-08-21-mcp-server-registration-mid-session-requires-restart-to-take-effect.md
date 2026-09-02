---
id: 2026-08-21-mcp-server-registration-mid-session-requires-restart-to-take-effect
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [claude-code, mcp, session-lifecycle, anansi]
sources:
  - ref: "Turns 1-2: assistant finds no MCP servers registered, registers the `anansi` MCP server mid-session, and `claude mcp get anansi` shows Connected — but the anansi_recall/anansi_capture tools remain unavailable in the current session's tool list until a restart, since MCP servers are only loaded at session start."
    reliability: high
    origin: "STAG session, 2026-08-21, \"Anansi local API + MCP registration\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-anansi-hub-mcp-setup-and-closeout.jsonl
  turns: [1, 2]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Registering an MCP server mid-session does not make its tools available until the session restarts
- class: confirmed
- source: STAG session, 2026-08-21, "Anansi local API + MCP registration"
- confidence: high
- verified: 2026-08-21

## Body

Claude Code loads MCP servers only at session start. Running `claude mcp add` (or editing `.mcp.json`/user config) while a session is already in progress registers the server for *future* sessions but does not inject its tools into the current one. In this session, after registering the `anansi` MCP server and confirming `claude mcp get anansi` showed `Connected`, the `anansi_recall`/`anansi_capture`/etc. tools were still not present in this session's tool list — a restart (or, in an interactive session, `/mcp` to trigger a reconnect) is required before they appear.

Practical implication: after registering a new MCP server, tell the operator explicitly that a restart is needed and that the current session cannot exercise the new tools to self-verify the registration — verification has to go through the underlying mechanism directly instead (here, `claude mcp get <name>` and direct HTTP calls to the Hub API), not through the MCP tool interface itself.

## Links
- extends, 2026-08-21-anansi-hub-and-mcp-server-confirmed-live-2026-08-21.md, the registration this finding was observed during.
