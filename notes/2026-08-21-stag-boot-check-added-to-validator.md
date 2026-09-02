---
id: 2026-08-21-stag-boot-check-added-to-validator
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, meta_agent, validator, runtime-verification, name-drift, python]
sources:
  - ref: "Archive turns 216-479 show the operator requesting a boot check be added to STAG's validator, its implementation as python -c \"import app.main\", and its resulting cascade through pre-existing name-drift bugs across tasks 5-9, culminating in a clean boot with 18 routes."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [216, 479]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent verified it against the live project and it immediately surfaced a real cascade of pre-existing bugs across tasks 4, 5, 6, and 7
- verified: 2026-08-21
- REVIEW: high-impact

# A single `python -c "import app.main"` boot check was STAG's highest-value validator addition, catching every remaining name-drift bug at once

## Body
During the task 10 audit, the agent found repeated cases where STAG-generated code called functions, classes, or config attributes that didn't actually exist in the modules it imported them from ("written against an imagined counterpart") — router-vs-service name drift, service-vs-schema drift, and cross-file signature drift. Static per-file checks (compile, per-task validator rules) could not catch these because each file was individually syntactically valid; only actually importing the running app surfaced them. The agent explicitly recommended, and on the operator's instruction ("add the boot check to stag") implemented, a new step in `_validate_and_fix_task` that runs `python -c "import app.main"` from the `backend/` directory using the STAG-managed interpreter and surfaces the traceback's actionable last line as a validator flag. Once added, this single check cascaded through and surfaced a chain of pre-existing name-drift bugs left over from tasks 4 through 8 that had never been caught, because the boot check only reports the first failure encountered — each fix advances the boot to the next latent bug behind it. This is a general lesson for any code-generation pipeline with typed/named cross-module contracts: an actual runtime import/boot check catches an entire class of drift bugs that no combination of static per-file checks can, and it should be added early rather than after the fact.

## Links
- related, 2026-08-21-stag-config-folder-collision-autofix.md, both are validator hardening added during the 2026-07-09 "improve the STAG agent" pass
- related, 2026-08-21-imagined-api-recurring-drift-pattern.md, the boot check is the concrete fix for the general "imagined counterpart API" failure mode this note documents
