---
id: 2026-08-21-stag-convention-scanner-and-post-task-validator-added
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [meta_agent, stag-build, drift, validation, playbook, self-improvement]
sources:
  - ref: "Turn 300 contains an almost word-for-word match to the note's Level 1/2/3 plan (playbook conventions, convention scanner, post-task validator) and the same six root-cause drift patterns; turns 306-313 show implementation; turns 328/331/334 show the validator auto-fixing task 6's router-wiring miss and task 7's issues"
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [300, 334]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, both were implemented, compile-verified, and exercised on two subsequent real tasks (6 and 7) in the same build, auto-fixing 2-3 of the recurring issues each time without manual repair
- verified: 2026-08-21
- REVIEW: high-impact

# meta_agent.py gained a convention scanner (injects the project's real folder/naming conventions into every generation prompt) and a post-task validator (auto-fixes and flags drift after each task)

## Body
After the same six drift patterns (see linked finding) kept recurring across tasks 3-5 of a build, three further layers were added to meta_agent.py and its playbook, on the operator's standing instruction to make project-best changes proactively and explain the reasoning afterward: (1) a new playbook section ("Project conventions") codifying the hard-earned rules — canonical migration timestamp naming, routers must live in `routers/` and be wired into `main.py`, permission dependencies live in `core/`, workers live in a single `worker/` folder, one root-level `.env.example`, and names for tables/columns/enum values/status strings must match verbatim across migration, service, worker, model, and schema within a task; (2) a convention scanner that runs at the start of every `stage_build()` when `--into` targets an existing project, auto-detecting the project's actual migration scheme, current folder layout, and `main.py`'s existing router includes, and injecting them as an authoritative block into every file-generation prompt; (3) a post-task validator that runs after each task's files are written, auto-renaming non-canonical migrations, auto-wiring new routers into `main.py`, and flagging misplaced `.env.example` files, plus a standalone `stag_validate.py` script that runs the same checks against any existing project folder outside of a full STAG run. A plan-persistence feature (`plan.json` written on approval) was added alongside so a resumed run doesn't need to re-run the interview. Effectiveness observed in-session: task 6 (built before the validator was live) still needed manual repair, but the validator's first real run on it auto-fixed the router-wiring issue; task 7 (built after) had the validator auto-fix 2 of 3 recurring issues on its own, leaving only new (previously unseen) drift patterns for manual repair.

## Links
- extends, 2026-08-21-stag-per-task-blind-generation-causes-cross-file-drift.md, the failure class these three layers were built to reduce.
- precedes, origin-scaffold-emission-hardens-projects-on-day-one.md, a later, more general evolution of the same meta_agent.py idea (planting hardening scaffold into every project at build end) recorded separately in STAG_CHANGELOG.md.
