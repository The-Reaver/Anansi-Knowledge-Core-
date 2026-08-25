---
id: skill-eval-gate-2026-08-25
type: ruling
status: candidate
source: Architecture, Redlined — Rev. 3 (artifact 924c39f2), Part IV; live-tested end-to-end on the adversarial-review skill; captured via GeoSuite session handoff, 2026-08-25
project: fleet
tags: [skills, eval, quality-gate]
---

# No SKILL.md edit ships without a with-vs-without eval delta

## Body

No `SKILL.md` wording change ships without a re-run of this loop. This isn't a proposal —
it was already run end-to-end on the `adversarial-review` skill before that skill was
packaged, so this note is a transcript of what actually ran.

1. Every skill gets an `evals/` folder next to its `SKILL.md`: one `evals.json` of real
   test cases pulled from actual runs where the skill mattered, each with assertions a
   correct run must satisfy.
2. Run each case twice per revision — with the skill loaded, and without (baseline). Two
   subagents, same prompt, same source, no shared context.
3. Grade both against the same assertions, recording `evidence` (a quoted transcript
   line), not just pass/fail.
4. Aggregate per condition; the number that matters is the with-skill-vs-baseline gap, not
   the with-skill score alone.
5. Gate: a two-line SKILL.md edit gets the same "small does not mean untested" treatment
   as a one-line bug fix under the mutation-testing mandate.
6. Write the result down — skill name, revision, pass-rate delta, what changed — as its
   own atomic note, not just a benchmark run nobody will find again.

The gate activates itself the moment someone edits a `SKILL.md` — it does not require a
retroactive sweep of every existing skill today.

## Links

- Architecture, Redlined Rev. 3, Part IV
- model-tiering-ruling-2026-08-25
