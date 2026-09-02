---
id: 2026-08-21-lords-of-cian-product-repo-git-silence-hides-active-work
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [lords-of-cian, git, repo-structure, knowledge-core-room, checklist-staleness]
sources:
  - ref: "Archive turns 226-229: the master-checklist refresh sweep turn establishing that projects/lords_of_cian's single-commit git history diverges sharply from the real, dated production activity happening outside that repo."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Lords of Cian\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [226, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, directly verified via nested-repo git log and directory listing
- verified: 2026-08-21

# projects/lords_of_cian (the pushed product repo) has had zero commits since 2026-08-02, but that git silence hides 18+ days of real production work happening outside it

## Body
projects/lords_of_cian is its own nested git repo (remote https://github.com/The-Reaver/Stag-Creative-Production-Studio.git, matching the checklist's claim), currently at a single commit, 9ec8bdc, dated 2026-08-02, branch master, working tree clean, no ahead/behind gap with origin. Nothing has been committed there in the 19 days since. All ten game-plan docs on disk (AGENTS.md, GAME_PLAN_v2.0.md, SOFTWARE_REQUIREMENTS_SPEC.md, etc.) carry the same Aug 1 22:41 modification time as the original push -- confirmed unchanged.

That reads as a dead workstream if git activity on this repo is the signal being checked. It is not dead. In the same window, a dedicated Knowledge Core "room" was created at research/knowledge-home/lords_of_cian/ (2026-08-12, operator-requested: "I want to have its own knowledge core dedicated to this book"), holding five atomic notes on Atlas verification, Gazetteer data-integrity fixes, grid-code canon, and a Jicome/Sovereign Trust Domain naming reconciliation written directly into MASTER CANON DECISIONS.docx. Separately, notes/ picked up canon corrections (2026-08-09 Kanja profile), a manuscript audit finding (2026-08-09), and a production-scope decision narrowing focus to Chronicle 1 (2026-08-09, already ratified). None of this touched the git repo the checklist names, because the actual production surface for this project right now is Google Drive documents, a Google Sheet (Lords_of_Cian_Regional_Atlas), and Cowork sessions -- not projects/lords_of_cian.

Worth the operator's attention as a methodology note, not just a Lords-of-Cian-specific one: any future status check that uses "commits to the product repo" as its liveness signal for this workstream will systematically under-report activity, because the repo is not where the current work happens.

## Links
- corrects: the implicit assumption in the 2026-08-03 checklist that projects/lords_of_cian activity level reflects project activity level
- see also: research/knowledge-home/lords_of_cian/README.md, research/knowledge-home/notes/2026-08-09-lords-of-cian-chronicle-1-scope-narrowed-chronicles-2-3-paused.md
