---
id: 2026-08-21-geo-platform-git-index-lock-still-active-blocking-18-days-later
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — day count corrected to 22 days and a caveat added that this checkout's live-blocking status is unconfirmed for the actively-worked GEO repo. Operator retains veto per Mandate 1."
project: geo
tags: [repo-hygiene, git, geo-platform, device-bridge, ops-infra]
sources:
  - ref: "Archive turns 218-229: STAG master-checklist refresh sweep, 2026-08-21, workstream 'Compute/cost strategy + stack/operations + repo hygiene' — live git command reproducing the index.lock failure inside projects/geo_platform"
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Compute/cost strategy + stack/operations + repo hygiene\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [218, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, directly reproduced with a live git command against the actual repo, not inferred from file listings
- verified: 2026-08-21

# The geo_platform .git/index.lock the 2026-08-03 checklist flagged as unresolved is still present today and was directly confirmed to block writes, not just a stale leftover

## Body

The 2026-08-03 master checklist (`reports/STAG_MASTER_CHECKLIST_2026-08-03.md`) flagged a stale `.git/index.lock` inside `projects/geo_platform/.git/` as an open, operator-only cleanup item. As of 2026-08-21 (22 days later) that exact file is still present (`projects/geo_platform/.git/index.lock`, filesystem timestamp 2026-08-18 14:52, so it is not even the same incident the checklist originally saw — it has recurred at least once since). It is not merely a leftover: running `git add` inside `projects/geo_platform` today fails immediately with `fatal: Unable to create '.../geo_platform/.git/index.lock': File exists`, confirming the lock is actively blocking commits right now, not just cosmetic clutter. `OPERATOR_AGENDA.md` (line ~142, itself uncommitted-modified but with this section untouched since 2026-08-03) still lists "GEO lock-file cleanup, operator-only action" as an open item, so this has never been closed out. `docs/ANIRAK_ROADMAP.md` M9 was previously reported DONE for the root repo (`reports/M9_REPO_HYGIENE_BUILD_REPORT.md`, 2026-07-27) but that report predates and does not cover this geo_platform-specific recurrence. `projects/geo_platform/` also has an untracked `_to_delete/` folder holding roughly 28 renamed-away `HEAD.lock.*` / `index.lock.*` artifacts from repeated prior incidents, consistent with the already-ratified Core finding that every git write operation through the device bridge leaves a stale lock behind (`research/knowledge-home/notes/2026-08-08-bridge-git-leaves-stale-lock.md`, `2026-08-20-read-only-git-checks-can-still-trigger-stale-lock.md`). Net: the checklist's framing of this as a single flagged incident to clear is outdated — it is a recurring, currently-live blocker, and the fix (`skills/stag-repo-hygiene/SKILL.md` hands the operator `del C:\Users\abadm\stag\.git\index.lock`-style native commands) has still not been run against `projects/geo_platform/.git/index.lock` as of today.

Caveat added at promotion (2026-08-26): this finding was reverified 2026-08-25 from the bridge-cse
stag worktree's `projects/geo_platform/` checkout, where the lock file and timestamp match exactly
and the `_to_delete/` artifact count is consistent (~27 today vs. ~28 originally claimed). A fresh
`git add` reproduction of the live-blocking failure was not re-run at that reverification, and per
this fleet's own standing guidance, GEO Suite has its own continuously-active dedicated session
elsewhere — this stag-side checkout may simply be a frozen, unattended mirror rather than current
proof that the lock is still live-blocking the repo the GEO Suite session actually works from.

REVIEW: high-impact

## Links
- relates, research/knowledge-home/notes/2026-08-08-bridge-git-leaves-stale-lock.md
- relates, research/knowledge-home/notes/2026-08-20-read-only-git-checks-can-still-trigger-stale-lock.md
- relates, reports/M9_REPO_HYGIENE_BUILD_REPORT.md
