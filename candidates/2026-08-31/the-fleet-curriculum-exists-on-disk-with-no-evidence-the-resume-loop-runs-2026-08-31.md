---
id: the-fleet-curriculum-exists-on-disk-with-no-evidence-the-resume-loop-runs-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) dormant-area audit, 2026-08-31 — relayed by the operator into a recovery session; the audit itself ran against the local Knowledge Home and could not be re-run here"
project: fleet
tags: [curriculum, augustin, dormant-area, inventory, resume-protocol]
supersedes: []
superseded_by: null
---

# The fleet curriculum is real and substantial on disk; what is unevidenced is whether anything executes it

## Body

Audited 2026-08-31. Of the six dormant areas this is the best-stocked. `curriculum/` holds
genuine material, not placeholders — task specs and lessons for **ADA-200, AGT-200,
BUILD-500, DEL-200, FLT-200, INTAKE-500, LLS-200, MED-200**, plus
`Agent-Curriculum-1600.html`, `Agent-Curriculum-1800.html` and
`How-The-Machine-Works.html`.

The gap is not content. The STARS/DREAMS design specifies an execution loop: a new chat
reads `READ_FIRST.md`, then `MASTER_TODO.md`, then `curricula/<agent>/CURRICULUM.md` and
`PROGRESS.md`, finds the next unproven task, does it as one slice, and proves it. **The
audit captured no evidence of that loop having run** — no observed `PROGRESS.md` updates,
no per-task proof notes traced back.

This distinction matters for planning. Curriculum needs no build; it needs a heartbeat that
shows the loop turning, and an honest answer to whether any agent has advanced a level
through it. Stocking a curriculum and running one are separate achievements, and only the
first is evidenced.

**Caveat:** this is a relayed audit result. The file inventory was reported, not
independently re-verified here, and the execution loop's absence is an absence of captured
evidence rather than a demonstrated negative.

## Links

- relates-to: 2026-08-06-cross-agent-stars-dreams-curriculum-design
- relates-to: stars-dreams-blocked-on-an-unresolved-9-gate-routing-question-2026-08-31
- relates-to: a-stale-git-lock-froze-a-repo-for-29-days-without-erroring-2026-08-31
