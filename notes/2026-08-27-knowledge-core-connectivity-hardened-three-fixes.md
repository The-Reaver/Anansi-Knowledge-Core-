---
id: 2026-08-27-knowledge-core-connectivity-hardened-three-fixes
type: artifact
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: anansi
tags: [anansi, infrastructure, autostart, hooks, connectivity, claude-md, artifact]
sources:
  - ref: "Built and verified end-to-end 2026-08-27: scripts/knowledge_home/ensure_hub.py, a Startup-folder launcher, a user-scope SessionStart hook, and ~/.claude/CLAUDE.md. The autostart was proven by killing the live hub (pid 24108) and confirming the launcher brought it back in ~1s"
    reliability: high
    origin: "bridge-cse stag session, 2026-08-27, on the operator's instruction to guarantee Knowledge Core connectivity in every session"
provenance:
  archive: research/knowledge-home/raw/2026-08-27-audit-report-standard-mandate.jsonl
  turns: [3, 3]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Knowledge Core connectivity hardened: an idempotent launcher, a logon autostart, a session-start check, and a Core-first directive

## Body
**The gap.** The `anansi` MCP server is registered at USER scope, so every local Claude Code
session already gets the `anansi_*` tools. But those tools are a thin client over
`anansi_hub.py` on `localhost:8787`, and the hub's only launcher was `start_anansi.bat` — a
manual double-click, no scheduled task, no autostart. **When the hub is down the MCP server still
registers and still reports "connected"; every call then fails.** A session could run for hours
with a dead Core behind it and nothing would say so.

**What was built.**

1. `scripts/knowledge_home/ensure_hub.py` — one idempotent code path, stdlib only (a health check
   that can fail on a missing dependency is not a health check). Checks `/api/health`; if the hub
   is down, spawns it detached via `pythonw` (so no console window) with output to
   `.anansi_hub.log`. `--check-only` never starts it; `--quiet` is silent when healthy; `--hook`
   is the SessionStart mode.
2. **Logon autostart** — `%APPDATA%\...\Startup\AnansiHub.vbs`, a stable three-line launcher that
   invokes the repo script hidden. All logic stays in the repo so the Startup file should never
   need editing.
3. **SessionStart hook**, in `~/.claude/settings.json` (USER scope — every project, every
   session), running `ensure_hub.py --hook`. The existing Stop hook was preserved.
4. `~/.claude/CLAUDE.md` — a Core-first directive, because **connection is not usage**. Nothing
   previously made a session actually consult the Core.

**Two design decisions worth keeping.**

*The hook must never block a session.* The first version waited up to 25s for readiness and
reported a false failure — a warm start is ~1.5s, but the first start after any code change pays
Python's bytecode-compile cost for the whole import graph, measured at over 25s here. The fix was
not a longer timeout but a **split deadline**: the logon path (nobody waiting) waits up to 120s;
the hook path waits 6s and then reports "started it, still coming up" and exits 0 regardless. A
SessionStart hook's job is to inform, not to interfere with a session already underway.

*The failure path is the only part worth testing.* The healthy path was green immediately and
proved nothing. The real tests were: `--check-only` against a dead port, the full spawn path on a
spare port, and finally **killing the live hub and confirming the Startup launcher brought it
back** (~1s). That last test is what caught the 25s bug — it would have shipped invisibly
otherwise, since it only misfires on a cold start.

**Still not closed: cloud and Remote Control sessions.** None of this reaches them; they cannot
see `localhost:8787` at all. `anansi_remote_mcp.py` exists for exactly this, but
`ANANSI_CONNECT.md:199` states it is "written and tested, but not yet deployed," and the remaining
steps are operator-only (a Voyage AI API key, a Railway deploy, then adding it as a claude.ai
custom connector).

## Links
- closes: the local half of the connectivity gap; see
  2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally for the remote half.
- enforces: 2026-08-27-audit-report-quality-floor-mandate (restated in ~/.claude/CLAUDE.md)
- relates-to: notes/2026-08-20-knowledge-core-first-mandate.md — the 2026-08-20 mandate said
  Core-first; this is the first mechanism that makes a session notice when it cannot comply.
