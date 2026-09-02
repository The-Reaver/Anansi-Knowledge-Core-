---
id: 2026-08-21-stag-into-context-start-at-flags-added-for-repair-builds
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [meta_agent, stag-build, cli-flags, repair, resume]
sources:
  - ref: "Turn 160 is the operator's direct prompt ('what can we do about the stag agent that will prevent the agent from writing to the wrong folder or regenerate blind?') that motivated the fix; turn 219 shows --into/--context and repair-aware generation implemented; turn 247 shows --start-at added afterward in a resumed session to jump to task 4 without re-running 1-3"
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [160, 247]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, all three flags were implemented and compile-verified in this session and used successfully on a real resumed build (task 4 onward)
- verified: 2026-08-21
- REVIEW: high-impact

# meta_agent.py gained --into, --context, and --start-at flags so a repair or resumed build targets an existing project instead of minting a new one and regenerating blind

## Body
Before this fix, meta_agent.py always derived the output folder from the seed file's own name, so pointing it at a repair or continuation seed created a brand-new `projects/<seed-name>/` folder instead of updating the existing built project, and every generation call regenerated files from the task description alone with no view of the actual code on disk (risking new drift on top of what it was supposed to fix). Three flags were added: `--into <folder>` builds into an existing project folder in place (and refuses to run if the folder doesn't exist) rather than creating a new one; `--context <file>` (repeatable) feeds real anchor files, most importantly the actual DB schema migration, into every generation call so it can't invent columns or tables that don't exist; `--start-at N` skips already-completed tasks so resuming a build (e.g. after a context-window reset or a mid-build pause) doesn't re-run and potentially overwrite earlier, already-repaired work. The build-stage generation loop was also changed to read back a file's existing content before rewriting it and to explicitly repair in place rather than blind-regenerate, and earlier-in-the-run files are now passed forward into later generation prompts to keep names and imports consistent across tasks.

## Links
- extends, 2026-08-21-stag-per-task-blind-generation-causes-cross-file-drift.md, the failure class these flags were built to prevent.
