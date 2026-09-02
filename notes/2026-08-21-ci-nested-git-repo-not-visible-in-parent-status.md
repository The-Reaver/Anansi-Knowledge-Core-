---
id: 2026-08-21-ci-nested-git-repo-not-visible-in-parent-status
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, git, repo-structure, operational-gotcha]
sources:
  - ref: "Archive turns 90-96: agent runs `git status` from the stag repo root after a Compliance Intelligence build pass and finds none of the CI changes shown; confirms from inside projects/compliance_intelligence's own nested git repo that the real change set (kb/seed edits, shared/snapshot.py, new rule modules, tests) is there, alongside pre-existing untouched dirty files in v4/, shared/actuarial_engine.py, the frontend, and kb/."
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (B)\" (backfilled from historical transcript fc69f93c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-fc69f93c.jsonl
  turns: [90, 96]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high, agent directly discovered and verified this while trying to confirm its own changed files were visible for operator review
- verified: 2026-08-21

# projects/compliance_intelligence is its own nested git repo, so its changes never show up in the parent stag repo's git status

## Body
After finishing a build pass inside projects/compliance_intelligence/, the agent ran `git status` from the parent stag repo root to confirm its new/modified files were present for the operator's review, and only the progress report showed up — none of the actual code changes (kb/seed edits, new shared/snapshot.py, new rule modules, new tests). Investigating, the agent found that projects/ is gitignored by the parent stag repo, and projects/compliance_intelligence is itself a separate nested git repository with its own history. Running `git status` inside that nested repo showed the real change set, including pre-existing uncommitted changes in v4/, shared/actuarial_engine.py, the frontend, and kb/__init__.py/loader.py that the agent had not touched and flagged as needing separate untangling. Anyone auditing or committing CI work must `cd` into projects/compliance_intelligence and run git commands there — the parent repo's status is not a reliable signal for this project.
