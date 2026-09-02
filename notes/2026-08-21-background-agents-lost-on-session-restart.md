---
id: 2026-08-21-background-agents-lost-on-session-restart
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [background-agents, session-restart, reliability, multi-agent, agame-sports]
sources:
  - ref: "Turns 192-213: line 202 is the resume-time task-notification reporting no completion record for any of the 8 background agents; line 205 is the agent's disk-state check finding only Batch A (9/9 files) actually landed; line 213 records the decision to relaunch the other 7 batches fresh."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [192, 213]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Overnight process restart silently dropped 7 of 8 background content-build agents; only disk state revealed which survived
- id: 2026-08-21-background-agents-lost-on-session-restart
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — directly observed: task-notification on resume reported "no completion record" for all 8, and a disk check found only 1 of 8 batches had actually written its files
- verified: 2026-08-21
- tags: background-agents, session-restart, reliability, multi-agent, agame-sports
- REVIEW: high-impact

## Body
The agent dispatched 8 parallel background subagents (via the Agent tool) to each build a batch of content pages for the A-Game Sports rebuild, then the operator stepped away ("im leaving my machine") and the host Claude Code process exited or was restarted overnight. On resume the next session received a task-notification stating no completion record was found for any of the 8 background agents, with a note that their work might not be lost since transcripts are saved to disk. Rather than trust that summary either way, the agent checked actual disk state directly and found that only 1 of the 8 batches (9 files) had actually landed; the other 7 batches (~75 pages) had produced nothing recoverable, so their agents did not survive the restart. The agent relaunched the 7 missing batches fresh with the same instructions rather than attempting a fragile resume. Lesson: a host-process restart while background agents are running does not reliably preserve their work, and the task-notification summary alone ("no completion record found") is not sufficient to know what actually happened — checking real output (files on disk, git status, etc.) before deciding whether to resume, relaunch, or treat work as complete is necessary every time.

## Links
