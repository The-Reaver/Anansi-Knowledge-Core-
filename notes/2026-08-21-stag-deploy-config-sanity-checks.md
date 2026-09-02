---
id: 2026-08-21-stag-deploy-config-sanity-checks
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, meta_agent, validator, deploy, railway, npm, dependency-management]
sources:
  - ref: "Archive turns 482-627 show two deploy-blocking config bugs found by manual inspection (a Railway build referencing a missing requirements.txt, and npm ci with no package-lock.json) and their encoding as automatic validator checks in meta_agent.py."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [482, 627]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high — both underlying bugs were found and fixed in the live project, then encoded as automatic checks and verified clean
- verified: 2026-08-21
- REVIEW: high-impact

# STAG's validator now checks for two silent deploy-blocking config traps: a Railway build referencing a missing requirements.txt, and npm ci with no lockfile

## Body
Near the end of the 2026-07-09 session, two deploy-blocking configuration bugs were found in the `project_brief_step0_resolved` project that had nothing to do with application code correctness: (1) `backend/railway.json` ran `pip install -r requirements.txt`, but the project declared its dependencies in `pyproject.toml` via hatchling and no `requirements.txt` existed — the Railway build would have failed outright; fixed by changing the install command to `pip install --upgrade pip && pip install .`. (2) `frontend/railway.json` ran `npm ci`, which hard-fails without a `package-lock.json`, and no lockfile existed in the repo yet — fixed by running `npm install` locally to generate one. Both were found only by manually inspecting deploy config files, not by any earlier validator check or by the app's own boot check (which only covers the backend Python import graph). The operator's stated policy this session was that every recurring failure mode should become an automatic check in STAG's validator; accordingly these two were added as deterministic deploy-config sanity checks. General lesson: a codebase can be 100% correct and still fail to ship because of deploy tooling assumptions (a missing lockfile, an install command pointed at the wrong manifest file) that no amount of application-level testing will surface — these need their own dedicated checks.

## Links
- related, 2026-08-21-stag-boot-check-added-to-validator.md, both closed gaps in the same "make recurring failure modes into automatic checks" improvement pass on 2026-07-09
