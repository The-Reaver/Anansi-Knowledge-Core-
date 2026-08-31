---
id: 2026-08-06-cross-agent-curriculum-decisions-and-score-upgrade-plan
type: decision
status: candidate
source: "Cowork session 2026-08-06, operator on phone; chose the first agents and the score model, and asked for a documented plan to upgrade the score model soon. (source status: active)"
project: fleet
tags: [training, curriculum, stars, dreams, leveling, upgrade-plan, jeremy, oluwole]
supersedes: []
superseded_by: null
---

# Cross-agent curriculum decisions locked; Jeremy and Oluwole first, TRL now with a plan to upgrade the score

## Body

Decisions locked:
- First agents: Jeremy (knowledge core) and Oluwole (research and sourcing). Prove the format on these two, then roll out to the rest of the fleet.
- Score model now: TRL 1 to 9, the same simple readiness scale Augustin's DREAMS uses. The composite is a weighted average with a weakest-link floor.

Plan to upgrade the score to the fleet's full leveling math (Wilson lower bound, Glicko-2, SPRT), because the operator may want it very soon:
1. Log from day one. Every task, on proof or on failure, records a pass or a fail against its skill in PROGRESS.md. This pass/fail history is the raw data the upgrade needs. Without logging it from the start, a clean upgrade later is impossible. This is the one non-negotiable step.
2. Reserve the fields. Each skill row in the DREAMS tracker carries empty columns for attempts, passes, rating, and deviation, so adding the math later is filling in fields, not a rewrite.
3. Upgrade trigger: the operator's word, or when a skill has about 20 to 30 logged attempts, enough for the statistics to be meaningful.
4. Upgrade step: from the logged history, compute the Wilson 95 percent lower bound on pass rate, the Glicko-2 rating and deviation, and the SPRT stopping rule, per skill. Add them under each skill. Switch the composite from the TRL average to the leveling math. Keep the TRL 1 to 9 as the friendly label on top.
5. Result: the upgrade is a data migration, not a rewrite, and can be flipped whenever the operator says.

The leveling math and its constants are already on record (research/quantitative-methods, and Brain Trust founding verdict 3, which set Jeremy's numbers). The upgrade reuses those, it does not invent new ones.

Next machine session builds: curricula/README.md (the resume protocol), then curricula/jeremy/ and curricula/oluwole/ each with CURRICULUM.md (STARS) and PROGRESS.md (DREAMS), with the reserved stat fields and per-task pass/fail logging in place from the first task.

## Links

- extends: 2026-08-06-cross-agent-stars-dreams-curriculum-design
