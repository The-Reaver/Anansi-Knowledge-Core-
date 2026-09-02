---
id: 2026-08-23-hook-config-changes-need-hooks-reload-or-fresh-session
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"promote and push\"), given after the operator's own prior pattern of requesting review before ratification in this session and after a review confirming all 5 accurate, cross-references resolved, and no injection/security concern in the flagged subagent output."
project: fleet
tags: [claude-code, hooks, session-lifecycle, gotcha, cli]
sources:
  - ref: "After updating global and project-local settings.json Stop-hook scope, assistant tells operator the current session already has the old config loaded and that '/hooks' must be opened once, or a fresh session started, to reload it, since it can't trigger that reload itself mid-session; operator then says 'open /hooks and reload' and assistant confirms it can't run /hooks itself, an interactive terminal-UI command"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [973, 975]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Editing a Claude Code settings file's hooks does not affect the currently running session; taking effect requires either the interactive /hooks command or a fresh session start, and /hooks itself cannot be invoked programmatically from inside a session
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 901-978
- confidence: high, directly attempted and directly stated as a known limitation in-session
- verified: 2026-08-23

## Body

After editing both `~/.claude/settings.json` (global) and `stag/.claude/settings.local.json` (project-local) to move the raw-transcript-capture Stop hook to global scope, the operator asked to "open /hooks and reload" to confirm the change. This could not be done from within the session: `/hooks` is an interactive terminal-UI slash command that opens a settings panel, and is not available to invoke programmatically from an agent session — there is no equivalent tool call that triggers it.

Claude Code loads hook configuration once at session start. This means an edit to a settings file's hooks does not affect the session already in progress; the currently-running session keeps using whatever hook config it started with. Two ways to make a hook-config edit take effect: open `/hooks` in an interactive terminal (which forces a reload of hook config as a side effect of opening the panel, even without changing anything inside it), or simply start a fresh Claude Code session (exit and reopen, or a new terminal tab), which reloads hook config from disk the same way. `/hooks` also serves as the way to verify which settings file a given hook is attributed to (user-level, project, or project-local), which is the concrete way to confirm a scope fix like the one described in the paired note actually took effect — each hook entry, grouped by event type (`Stop`, `SessionStart`, etc.), shows which file it came from.

## Links
- relates, 2026-08-21-mcp-server-registration-mid-session-requires-restart-to-take-effect.md, the same underlying Claude-Code-loads-config-once-at-session-start pattern, but for MCP server registration rather than hooks.
- context, 2026-08-23-raw-capture-stop-hook-was-project-scoped-not-global-fixed.md, the specific hook-scope edit this reload limitation applies to.
