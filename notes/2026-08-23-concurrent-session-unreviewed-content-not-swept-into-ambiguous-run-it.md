---
id: 2026-08-23-concurrent-session-unreviewed-content-not-swept-into-ambiguous-run-it
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"I ratify this\"), given after reviewing an operator-facing note-by-note review report covering all 3 (all 3 read in full, the one external cross-referenced link confirmed to resolve, no factual errors found)."
project: fleet
tags: [git, concurrent-session, operator, governance, process, ratification]
sources:
  - ref: "Operator reinstates direct git execution (line 1019) then says 'run it' with nothing of the assistant's own queued (line 1027); assistant checks git status and declines to commit the concurrent session's unreviewed 8 candidates-to-notes files, asking the operator to clarify intent instead (line 1029)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1019, 1029]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Given an ambiguous "run it" with git-execution authority already granted, the assistant declined to commit unreviewed changes it recognized as belonging to a different, concurrently running session

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 979-1029
- confidence: high, directly observed in the transcript
- verified: 2026-08-23

Immediately after the operator told the assistant to execute git commands directly ("i want you to execute the commands," see the companion note on that preference being reversible), the operator said simply "run it" with nothing of the assistant's own work actually queued to commit. The assistant checked git status rather than assuming the instruction authorized committing whatever was pending. The only uncommitted change under `research/knowledge-home/` at that moment was 8 files with a `2026-08-22c-` filename prefix that had been moved from `candidates/` to `notes/` — work belonging to a different, concurrently running Claude Code session, not this one, and not reviewed or ratified by this session's assistant. The assistant declined to commit that content on the operator's behalf without first flagging whose work it was, and instead asked the operator to clarify which of a few concrete things "run it" actually meant (nothing pending / commit the other session's 8 files anyway / run the distillation pass on newly undistilled lines instead).

The durable lesson: broad execution authority granted for one purpose ("execute git commands directly") does not extend to committing unreviewed content that the assistant can identify as belonging to a different actor or session, even under a vague "run it" that could be read as blanket permission. The correct move is to identify provenance first (git status plus recognizing the filename pattern as another session's work) and surface the ambiguity rather than silently including or silently skipping it.

## Links
- related, 2026-08-23-git-execution-preference-is-live-and-reversible-within-session.md, same incident's preceding step where direct git execution was reinstated as the active preference
- related, 2026-08-20-concurrent-session-can-modify-candidates-mid-review.md, earlier-session precedent that concurrent sessions can touch the same candidates/notes directories mid-review
