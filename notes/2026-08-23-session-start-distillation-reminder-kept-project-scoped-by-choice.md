---
id: 2026-08-23-session-start-distillation-reminder-kept-project-scoped-by-choice
type: decision
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"promote and push\"), given after the operator's own prior pattern of requesting review before ratification in this session and after a review confirming all 5 accurate, cross-references resolved, and no injection/security concern in the flagged subagent output."
project: fleet
tags: [anansi, hooks, knowledge-core, settings-scope, distillation, operator-decision]
sources:
  - ref: "Assistant surfacing the tradeoff while fixing the Stop hook's scope: \"One tradeoff worth deciding before I touch it: the other hook, distillation_reminder.py (the SessionStart nag about undistilled backlog), is also currently project-scoped. If I make that one global too, you'd get an 'Anansi backlog' reminder at the start of every Claude Code session on this machine... Making just the capture hook global and leaving the reminder project-scoped avoids that noise.\" (AskUserQuestion follow-up), then the assistant proceeding to add only the capture hook globally while leaving distillation_reminder.py in the project-local settings file."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [960, 973]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The SessionStart hook that nags about undistilled Anansi backlog was deliberately left project-scoped to stag, even while the Stop capture hook was made global, to avoid nagging in unrelated-project sessions

- id: 2026-08-23-session-start-distillation-reminder-kept-project-scoped-by-choice
- type: decision
- status: ratified
- ratified: 2026-08-23 — operator directly ratified via explicit operator instruction ("promote and push"), given after the operator's own prior pattern of requesting review before ratification in this session and after a review confirming all 5 accurate, cross-references resolved, and no injection/security concern in the flagged subagent output.
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 901-978
- confidence: high, directly observed operator choice via an explicit question-and-answer exchange in this session
- verified: 2026-08-23
- tags: anansi, hooks, knowledge-core, settings-scope, distillation, operator-decision

## Body

When fixing the raw-transcript-capture Stop hook to fire globally instead of only inside the `stag` project (see the paired note on that fix), a second Anansi hook was in scope for the same question: `distillation_reminder.py`, a SessionStart hook that flags undistilled raw-archive backlog at the start of a session. That hook was also only registered in the project-local `stag/.claude/settings.local.json`.

Before touching it, the tradeoff was surfaced explicitly to the operator: making the reminder global too would mean an "Anansi backlog" notice firing at the start of every Claude Code session on the machine, including sessions in unrelated client work that have nothing to do with STAG or the Knowledge Core. The operator's choice, made via a direct question-and-answer exchange rather than assumed: make only the capture hook global, and leave the distillation-backlog reminder scoped to the `stag` project only. The practical effect is that raw-transcript capture now happens everywhere, but the "you have undistilled backlog" nag only appears when someone is actually working inside `stag` — chats in other projects get archived silently without any reminder that they need a later distillation pass.

## Links
- extends, 2026-08-21-distillation-reminder-built-option-a-deferred-on-broken-path.md, describes the original build of this SessionStart reminder hook, which this note's scoping decision leaves unchanged in its project-local registration.
- relates, 2026-08-23-raw-capture-stop-hook-was-project-scoped-not-global-fixed.md, the paired fix made in the same exchange that made the sibling Stop hook global instead.
