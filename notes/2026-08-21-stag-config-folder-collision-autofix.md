---
id: 2026-08-21-stag-config-folder-collision-autofix
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, meta_agent, validator, backend-structure, python-imports, recurring-bug]
sources:
  - ref: "Archive turns 102-140 show the recurring app/config/ folder-vs-config.py collision hitting tasks 7 and 8, and STAG's validator being given an automatic fix (move file, rewrite imports, delete empty folder) plus a passing smoke test."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [102, 140]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent narrated the exact code change and a passing smoke test against the real project tree
- verified: 2026-08-21
- REVIEW: high-impact

# STAG's validator now auto-fixes the recurring `app/config/` folder-vs-`config.py` collision

## Body
In the STAG project generator (`meta_agent.py`, used to scaffold the `project_brief_step0_resolved` backend), generated tasks repeatedly created a `backend/app/config/` folder sitting next to an existing `backend/app/config.py` module. In Python this silently breaks imports of `config.py` because the package shadows the module. This exact trap hit STAG-generated task 7 and then task 8 again, each requiring a manual fix (moving the new file into `backend/app/services/` and rewriting every `app.config.<sub>` import). After task 9, the operator asked whether STAG itself could be improved; the agent added an automatic check to `_validate_and_fix_task` that detects any new file under `app/config/`, moves it to `backend/app/services/<name>.py`, rewrites every project-wide import of `app.config.<sub>`, and deletes the now-empty `config/` folder. This was smoke-tested end-to-end against a synthetic scenario before being trusted. The underlying lesson for anyone scaffolding a similarly-named Python package/module pair: a folder and a module cannot share a name in the same parent package, and this is exactly the kind of drift an LLM code generator will reintroduce across tasks unless a deterministic check catches it every time.

## Links
- related, 2026-08-21-stag-boot-check-added-to-validator.md, both are STAG validator hardening additions from the same session, aimed at catching import-breaking drift before runtime
