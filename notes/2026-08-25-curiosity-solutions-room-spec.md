---
id: 2026-08-25-curiosity-solutions-room-spec
type: spec
status: active
source: this chat, implementing `2026-08-25-curiosity-solutions-room-scope-decided.md`.
project: fleet
tags: [anansi-curriculum, spec, curiosity-room, solutions-room, shift-department]
---

# Curiosity Room / Solutions Room: built as two connected folders with a real intake loop and two durable recurring Routines driving them

## Body

Implements `2026-08-08-curiosity-and-solutions-room-proposal.md` as literal running components,
per the operator's 2026-08-25 confirmation.

**Structure.** `curiosity-room/` holds a queue of open questions (`queue/`) and a claimed archive
(`claimed/`). `solutions-room/` holds a queue of worked solutions (`queue/`). Both have a README
and an entry template. Full mechanics are in each README; summary: the Solutions Room pulls an
open curiosity, works it, deposits a solution entry, moves the curiosity to `claimed/`, and
writes any newly-surfaced question back into the Curiosity Room queue. That write-back is the
"always connected, forever interacting" loop the operator described — solving feeds curiosity,
curiosity feeds solving.

**Governance.** Both queues produce candidate material only, same tier as `candidates/`. Nothing
here reaches `notes/` without the operator's pass — the rooms don't get a governance exemption
just because they're automated. Every solution entry carries a confidence label
(confirmed / believed-unconfirmed / extrapolated), inherited from the 2x2 research program's
validation-labeling rule, so Mandate 7 still applies to fast-moving automated output.

**What makes it literal, not conceptual.** Two durable Routines
(`curiosity-room-cycle` and `solutions-room-cycle`, biweekly, staggered so Solutions Room always
has fresh material) each spawn a fresh session against this repo, do one pass of their room's
job, commit, and push. This is the same mechanism (`trig_...` Routines) that already runs the
biweekly 2x2 research cycle referenced in `2026-08-08-heavy-chat-handoff-research-role.md` — not
a new kind of infrastructure, an application of the one already in use.

**Shift Department, as a worked example (per `2026-08-08-shift-department-proposal.md`'s
correction).** A curiosity like "Mojo is gaining prominence — does this change anything for us?"
enters the queue. The Solutions Room can't fully resolve that in one pass, so its solution entry
is a scoped investigation plan: stand up a small dedicated unit to track the direction closely,
expandable if the shift proves real, recallable to the main fleet if it doesn't. That
recommendation is exactly the kind of output this loop is meant to produce — the Shift Department
was never a third room, it's what a solution entry looks like when the answer is "start watching
this closely," not "here is the fact."

**What is still open.** The two Routine prompts are written to instruct a fresh session to
`add_repo` this repository and check out `claude/implementation-checklist-k5l63w` — that branch
name should be updated (or the trigger re-pointed at the default branch) once this work merges,
or the Routines will keep targeting a stale branch.

## Links

- implements, `2026-08-08-curiosity-and-solutions-room-proposal.md`, the original proposal.
- derived-from, `2026-08-25-curiosity-solutions-room-scope-decided.md`, the operator's
  literal-vs-conceptual decision.
- supersedes-in-part, `2026-08-08-shift-department-proposal.md`, by showing concretely what the
  loop produces.
- cites, `2026-08-08-heavy-chat-handoff-research-role.md`, for the existing Routine mechanism this
  reuses.
