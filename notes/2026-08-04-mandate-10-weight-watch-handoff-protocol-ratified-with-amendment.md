---
id: 2026-08-04-mandate-10-weight-watch-handoff-protocol-ratified-with-amendment
type: ruling
status: ratified
source: this chat, 2026-08-04, a second simulated 6-seat Brain Trust dispatch on Abad's proposal, ratified with amendment (source status: active)
project: fleet
tags: [mandate-10, weight-watch, handoff, brain-trust, governance, operator-contribution]
---

# Mandate 10: Sessions Must Proactively Write Knowledge Core Handoffs, Measured Honestly

## Body

Abad proposed a standing mandate that every Cowork chat's context weight get watched, and once a limit is hit, the session write a handoff document into Knowledge Core so a future session only needs to be told to check Knowledge Core for the latest. The Brain Trust ratified this with amendment, because there is no tool that gives Claude a live, precise token or context count mid-conversation; the only hard signal available is that a session has already gone through an automatic compaction, which is a lagging indicator, not a proactive one. The mandate's trigger is defined honestly as a heuristic bundle instead of a measurement: message and tool-call counts, number of large file reads, and number of subagent dispatches, treated as soft proactive signals, with a completed compaction event treated as a hard, mandatory trigger, meaning a session that compacts without a prior handoff has violated the mandate, not satisfied it by writing one afterward. Jasiah set acceptance criteria for a valid handoff document: it must be written to a discoverable, named location in Knowledge Core, contain the session's goal, decisions made with rationale, open items and blockers, a concrete next action, and links to artifacts touched, and it must pass the test that a different, fresh session told only to check Knowledge Core could resume work without Abad re-explaining anything.

## Links

- extends: 2026-08-04-mandate-9-compounding-assets-ratified (same governance precedent and process)
