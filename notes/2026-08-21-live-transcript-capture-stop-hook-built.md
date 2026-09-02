---
id: 2026-08-21-live-transcript-capture-stop-hook-built
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — provenance citation corrected to archive turns 99-120 and the scope claim updated for the 2026-08-23 global-hook fix. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, mcp, hooks, adr-0005, knowledge-core, automation]
sources:
  - ref: "Archive turns 99-120: pipe-test extracting 97 real turns from this session's own transcript, hook wiring, and the live-fire confirmation showing lines_processed advancing 295 to 336 with no manual intervention"
    reliability: high
    origin: "STAG session, 2026-08-21, \"Anansi local API + MCP registration\" (continuation)"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [99, 120]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, pipe-tested directly against this session's own real transcript before wiring
- verified: 2026-08-21

# A Stop hook now appends every session's transcript to the Anansi raw archive automatically, closing the gap the stag-closeout skill itself flagged

## Body

The `stag-closeout` skill's own text names a known gap: raw-archive capture (ADR-0005) only happens as "a batch write triggered by the close-out phrase... not a live per-turn hook," and states that true real-time capture "requires a standing hook outside a skill's reach." The operator asked directly for that gap to be closed — a raw transcript of every chat, not just chats where someone remembers to say "close out this chat."

Built and wired this session: `scripts/knowledge_home/live_transcript_capture.py`, registered as a `Stop` hook in `.claude/settings.local.json` (personal, gitignored scope — this is a per-machine automation preference, not a team-wide requirement). On every assistant turn, Claude Code invokes it with the session's own `session_id` and `transcript_path` (Claude Code's own per-session JSONL transcript, found this session at `C:\Users\abadm\.claude\projects\C--Users-abadm-stag\<session_id>.jsonl`). The script tracks a per-session checkpoint (lines already processed) outside `research/knowledge-home/` entirely (`.claude/anansi_live_capture/checkpoints/`), reads only the new lines since last run, extracts user-turn text and assistant text/tool-call-names, and appends them in the ADR-0005 `{ts, role, text, tool_calls}` schema to `research/knowledge-home/raw/<date>-live-<session8>.jsonl` via plain append (`open(..., "a")`), never rewriting the file.

Verified before wiring: piped a synthetic Stop-hook payload (matching this session's real `session_id`/`transcript_path`) directly into the script and confirmed it produced a correctly-formed archive file with 97 real extracted turns from this actual session, and a checkpoint recording 295 transcript lines processed.

**Confirmed live-firing, same session, next turn:** the checkpoint's `lines_processed` advanced from 295 to 336 with no manual invocation between checks, and `.claude/anansi_live_capture/hook_input_debug.log` recorded the real Stop-hook payload — `hook_event_name: "Stop"`, `session_id`/`transcript_path` in exactly the snake_case form the script expects. This is not a theoretical wiring; it is proven working, in production, in this repo, as of 2026-08-21.

**Open question, not yet resolved:** whether an already-running session (started before this hook was registered) picks it up live, versus only sessions that start fresh afterward. Direct evidence cuts against "all open sessions get it automatically" — a second Claude Code session was found active in this same repo at the same time (producing unrelated candidate notes on an LLM-judge feature), and no checkpoint file exists for that session's id, meaning its Stop hook has not yet fired with the new config. It may simply not have hit a Stop boundary since the edit landed, or its own settings watcher may not be covering the change the way this session's did — undetermined from here.

**Consequence for `stag-closeout`:** for any session where this hook fires successfully, the skill's own Step 0 (manually reconstructing and appending turns) becomes redundant — the archive already exists before closeout ever runs. Step 0 should become "confirm the live archive file for this session exists and is current" rather than re-deriving it by hand. The skill's own file lives outside this repo (under the Claude app's skill package directory) and was not edited as part of this session; flagging the needed update here rather than silently leaving the skill's documented gap stated as still-open when it may no longer be.

**Scope correction (2026-08-23, applied at 2026-08-26 promotion):** the project-scoped registration in
`.claude/settings.local.json` described above meant sessions outside the stag project were never
captured. The hook was moved to the global `~/.claude/settings.json` on 2026-08-23 (see
`research/knowledge-home/notes/2026-08-23-raw-capture-stop-hook-was-project-scoped-not-global-fixed.md`)
— confirmed directly during this promotion pass: the project's `.claude/settings.local.json` now holds
only the SessionStart hook, and `~/.claude/settings.json` holds the Stop hook. The "personal, gitignored
scope" framing above is therefore accurate only for the period 2026-08-21 through 2026-08-22.

## Links
- extends, 2026-08-21-anansi-does-not-auto-ingest-chat-history-only-explicit-writes.md, this hook is the concrete fix for the gap that note describes.
- relates, docs/adr/0005-two-store-memory-archive-and-core.md, this hook is a new write path into the same archive store ADR-0005 defines, not a change to the ADR itself.
