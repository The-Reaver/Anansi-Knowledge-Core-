---
id: 2026-08-21-anansi-hub-and-mcp-server-confirmed-live-2026-08-21
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, mcp, hub, status, windows]
sources:
  - ref: "Turns 1-2: operator asks to confirm the Hub API and MCP server registration; assistant finds port 8787 down and no MCP servers registered, starts `python anansi_hub.py`, and runs `claude mcp add anansi --scope user -- python C:\\Users\\abadm\\stag\\anansi_mcp.py`, verified live via `curl http://localhost:8787/api/health` (687 notes, 349 links) and `claude mcp get anansi` (Connected)."
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

# Anansi Hub API and MCP server were both confirmed running and registered as of 2026-08-21
- class: confirmed
- source: STAG session, 2026-08-21, "Anansi local API + MCP registration"
- confidence: high, verified by direct HTTP calls and `claude mcp get`
- verified: 2026-08-21

## Body

Prior to this session, `python anansi_hub.py` was not running (port 8787 unreachable) and no MCP servers were registered in Claude Code (`claude mcp list` returned "No MCP servers configured"). Both were set up and verified in this session:

Hub API: started with `python anansi_hub.py` in the background from `C:\Users\abadm\stag`. Verified live via `curl http://localhost:8787/` (200) and `curl http://localhost:8787/api/health`, which returned `{"ok": true, "notes": 687, "links": 349, ...}` — 687 notes in the Core at the time of this session. `/api/status` does not exist as an endpoint (a guess that returned a 404 `{"error": "not found"}`); the correct status endpoint is `/api/health`.

MCP server: registered at user scope, `claude mcp add anansi --scope user -- python C:/Users/abadm/stag/anansi_mcp.py` (see [[2026-08-21-claude-mcp-add-strips-backslashes-from-windows-paths-in-posix-shell]] for the path-escaping bug hit along the way). `claude mcp get anansi` confirmed `Status: Connected`.

This registration is durable across sessions (stored in the user-scope Claude Code config), but the Hub process itself is not — it runs in the foreground/background of whatever terminal started it and stops when that terminal closes. `ANANSI_CONNECT.md` documents a Startup-folder shortcut (Step 3, Way A) for making it survive reboots; absent that, it must be started manually (`python anansi_hub.py` or `start_anansi.bat`) at the start of a work session.

## Links
- extends, 2026-08-08-anansi-reaches-every-tool-through-one-mcp-server-and-the-das.md, the setup this session executed and verified end-to-end.
