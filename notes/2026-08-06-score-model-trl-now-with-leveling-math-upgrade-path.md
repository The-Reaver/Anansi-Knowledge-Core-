---
id: 2026-08-06-score-model-trl-now-with-leveling-math-upgrade-path
type: spec
status: ratified
source: "Cowork session 2026-08-06, operator on phone; chose the first agents and the score model, and asked for a documented plan to upgrade the score model soon (source status: active); mined from candidates/2026-08-25/2026-08-06-cross-agent-curriculum-decisions-and-score-upgrade-plan.md"
project: fleet
tags: [dreams, scoring, trl, wilson, glicko, sprt, upgrade-path]
---

# Score model locked: TRL 1-9 now, with a defined, non-rewrite upgrade path to the full leveling math (Wilson, Glicko-2, SPRT)

## Body

Score model now: TRL 1 to 9, the same simple readiness scale Augustin's DREAMS uses; the composite is a weighted average with a weakest-link floor. Upgrade path to the fleet's full leveling math: (1) log every task's pass or fail against its skill in PROGRESS.md from day one — the one non-negotiable step, since a clean upgrade later is impossible without this raw data; (2) reserve empty columns per skill for attempts, passes, rating, and deviation now, so adding the math later is filling in fields, not a rewrite; (3) upgrade trigger is the operator's word, or roughly 20-30 logged attempts per skill, enough for the statistics to be meaningful; (4) the upgrade step computes the Wilson 95 percent lower bound, the Glicko-2 rating and deviation, and the SPRT stopping rule per skill, adds them under each skill, and switches the composite from the TRL average to the leveling math, keeping TRL 1-9 as the friendly label on top; (5) the result is a data migration, not a rewrite, flippable whenever the operator says. The leveling math and its constants are already on record (research/quantitative-methods, Brain Trust founding verdict 3) and are reused, not reinvented.

## Links

- extends: 2026-08-06-jeremy-and-oluwole-are-the-first-two-agents-to-prove-format
- relates: 2026-08-07-legacy-formulas-recovered-gap-closed
