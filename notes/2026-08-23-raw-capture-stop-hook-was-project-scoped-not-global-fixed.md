---
id: 2026-08-23-raw-capture-stop-hook-was-project-scoped-not-global-fixed
type: decision
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"promote and push\"), given after the operator's own prior pattern of requesting review before ratification in this session and after a review confirming all 5 accurate, cross-references resolved, and no injection/security concern in the flagged subagent output."
project: fleet
tags: [anansi, hooks, mcp, knowledge-core, settings-scope, automation, gotcha]
sources:
  - ref: "Operator: \"i want to make sure anansi is recording all of my chats and ingesting the raw transcripts in all chats all the time. how do i ensure this?\" Assistant, after checking config: \"right now, Anansi's automatic capture does not cover all your chats, only chats where Claude Code's working directory is stag. The Stop hook that archives every turn (live_transcript_capture.py) is registered in stag/.claude/settings.local.json — a project-scoped settings file, not the global one.\" Followed by the fix confirmation: \"Both files updated and validated: Global ~/.claude/settings.json: now has the Stop capture hook... Project-local stag/.claude/settings.local.json: the duplicate Stop hook removed.\""
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [955, 973]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The automatic raw-transcript-capture Stop hook only fired inside the stag project, so every chat in any other project was never being captured by Anansi at all; fixed by moving it to the global settings file

- id: 2026-08-23-raw-capture-stop-hook-was-project-scoped-not-global-fixed
- type: decision
- status: ratified
- ratified: 2026-08-23 — operator directly ratified via explicit operator instruction ("promote and push"), given after the operator's own prior pattern of requesting review before ratification in this session and after a review confirming all 5 accurate, cross-references resolved, and no injection/security concern in the flagged subagent output.
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 901-978
- confidence: high, directly observed in the settings files and confirmed by direct instruction to fix
- verified: 2026-08-23
- tags: anansi, hooks, mcp, knowledge-core, settings-scope, automation, gotcha

REVIEW: high-impact

## Body

The operator asked directly whether Anansi was capturing all of their chats, across all projects, all the time. Checking the actual hook registration (rather than assuming) found that `live_transcript_capture.py`, the Stop hook that appends every turn to the raw archive, was registered in `stag/.claude/settings.local.json` — a project-scoped settings file that only applies when Claude Code's working directory is inside the `stag` repo. This directly contradicts what an earlier note about this same hook's build described as merely "personal, gitignored scope" — the practical consequence of that scoping, not fully spelled out at build time, is that any Claude Code session opened in a different project or an unrelated folder never fired this hook, so nothing from those sessions ever reached the Knowledge Core's raw archive. This had been true since the hook was first built and had gone unnoticed until this session's direct question surfaced it.

The fix: the same hook command was added to the global `~/.claude/settings.json` (which applies to every Claude Code session on the machine, regardless of working directory), and the now-duplicate Stop-hook entry was removed from the project-local `stag/.claude/settings.local.json` so it only lives in one place going forward. Both files were validated as syntactically correct JSON after editing. The underlying script itself needed no code changes to support this — it already read the session id and transcript path generically from whatever Claude Code handed it, and only ever wrote output to the one canonical `stag/research/knowledge-home/raw/` location regardless of which project the session started in, so making capture global was a config change, not a code change.

Caveat carried into the next note: the config change is saved to disk, but the currently-running session had already loaded the old (project-scoped) hook config at its own start, so this session's capture kept working as before either way; it does not itself prove the global hook is now firing elsewhere.

## Links
- extends, 2026-08-21-live-transcript-capture-stop-hook-built.md, describes the original build and its "personal, gitignored scope" framing; this note is the later discovery that project-scoped also meant project-limited coverage, and the fix that made it truly global.
- relates, 2026-08-23-session-start-distillation-reminder-kept-project-scoped-by-choice.md, the paired decision made in the same exchange to deliberately leave the other Anansi hook project-scoped.
