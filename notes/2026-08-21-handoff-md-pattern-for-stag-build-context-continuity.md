---
id: 2026-08-21-handoff-md-pattern-for-stag-build-context-continuity
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — see body correction. Operator retains veto per Mandate 1."
project: fleet
tags: [session-mechanics, handoff, context-window, stag-build, meta_agent]
sources:
  - ref: "Turns 323-334: turn 323 is the operator's ~68%-context-window question, turns 324-334 show the HANDOFF.md being drafted and the resume protocol quoted."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [323, 334]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A HANDOFF.md file at the project root let a fresh Claude Code chat resume a multi-day STAG build with zero context loss, once the operator's context window approached its limit
- id: 2026-08-21-handoff-md-pattern-for-stag-build-context-continuity
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: medium, the pattern was set up and described as sufficient in this session, but its actual success at resuming in a genuinely fresh chat was not observed within this transcript
- verified: 2026-08-21

## Body
Partway through the multi-task Small Business Tools Step 0 build, with the chat's context window at roughly 68%, the operator asked whether a new chat could pick up where this one left off, or whether a handoff document was needed. The answer given and acted on: yes, write a handoff, because while most of the state that matters (the seed file, playbook.txt with its build conventions, meta_agent.py with all its fixes, the built project on disk, and the approved plan) already lives on disk and needs no chat memory to reconstruct, what only exists in the chat is the audit pattern the agent had been applying after every task (spot-check money-critical logic, run the validator, reconcile drift, report what changed) and the specific in-flight state (which task number is next, what was fixed, what new drift patterns were just discovered). A `HANDOFF.md` was written capturing exactly that: current position, the audit pattern itself, every locked interview decision, and the exact resume command with its flags. The stated protocol for a fresh chat was simply: "Read HANDOFF.md and pick up where the last session left off, I'm ready to run task N." The handoff was kept current as new drift patterns were discovered (updated again after task 7).

**Revision (Brain Trust review, 2026-08-26):** the standing principle here — write a durable handoff artifact on disk so a fresh session can resume with zero context loss — is not new; it is already established by 2026-08-04-mandate-10-weight-watch-handoff-protocol-ratified-with-amendment.md, 2026-08-20-continuity-approach-for-new-chats.md, and 2026-08-20-durability-comes-from-artifact-location-not-chat-choice.md. This note should be read as a concrete instance/template of that standing principle for STAG builds specifically — the five pieces of state (seed file, playbook.txt, meta_agent.py, the built project on disk, the approved plan) plus the HANDOFF.md itself that captures the audit pattern and in-flight position — not as a standalone lesson. The note's original hedge is preserved: an actual fresh-chat resume from this HANDOFF.md was never observed within this transcript; the pattern was set up and judged sufficient, not exercised end-to-end.

## Links
- related, 2026-08-04-mandate-10-weight-watch-handoff-protocol-ratified-with-amendment.md, the standing handoff-protocol principle this note instantiates for a STAG build.
- related, 2026-08-20-continuity-approach-for-new-chats.md, the general cross-session continuity approach this note is one concrete example of.
- related, 2026-08-20-durability-comes-from-artifact-location-not-chat-choice.md, the underlying principle (durability lives in the artifact, not the chat) this HANDOFF.md pattern relies on.
