---
id: 2026-08-21-geo-platform-now-has-own-github-repo-and-ci-but-local-checkout-26-commits-behind
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — added a caveat that this checkout appears dormant and is not proof of current upstream state. Operator retains veto per Mandate 1."
project: geo
tags: [geo-suite, geo-platform, git, ci, checklist-drift]
sources:
  - ref: "Archive turns 226-229: STAG master-checklist refresh sweep, 2026-08-21, workstream 'GEO Suite' — git remote/log/status run live inside projects/geo_platform"
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"GEO Suite\""
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
- confidence: high — `git remote -v`, `git log`, and `git status` run live inside projects/geo_platform this sweep
- verified: 2026-08-21

# The checklist's "no CI" finding for GEO Suite is now false upstream (CI + 11 merged PRs exist), but true again locally: the repo checkout is 26 commits stale with its own uncommitted changes

## Body
The 2026-08-03 checklist's finding was: "projects/geo_platform/ working tree uncommitted, no CI." Two things
have changed since, in opposite directions, which is why this is stated as a conflict rather than a single
verdict:

1. **"No CI" is now false, upstream.** `projects/geo_platform` is its own git repository (confirmed via
   `git -C projects/geo_platform remote -v`: `origin = https://github.com/The-Reaver/Stag-GEO-Platform.git`),
   separate from the outer stag repo, which explicitly gitignores `projects/` with the comment "The product
   lives in its own repo ... do not embed it here." That upstream repo now has a real CI workflow at
   `.github/workflows/geo-verify.yml` (triggers on push/PR to main, installs backend deps, runs
   `ci_verify_geo.py`) and 11 merged pull requests visible in `origin/main`'s history, dated through
   2026-08-19 — real fixes including a frontend healthcheck path bug, a duplicate `--port` flag breaking the
   frontend container, a `/dashboard/geo` and `/sales` auth bug (cookies vs. localStorage), and a documented
   Railway "Redeploy vs. latest commit" gotcha.

2. **"Working tree uncommitted" is still true, locally, but for a different reason than the checklist
   implied.** The local checkout's `HEAD` is `2344354` ("Find and fix Railway deploy root cause, wire real
   law citations into compliance findings, build live-citation script") — this is **26 commits behind**
   `origin/main`'s `5f3f063`, meaning none of the 11 merged PRs above are reflected in the working directory
   on this machine. On top of that gap, `git status` shows the local working tree itself has active
   uncommitted modifications right now (`.env.example`, `GEO_DEVELOPMENT_LOG.md`, several backend routers
   and services, `frontend/Dockerfile`, `frontend/app/dashboard/layout.tsx`, and
   `knowledge_core/feeds/regulatory/raw_law/MANIFEST.md`) — including the real WCAG-citation work described
   in the companion verify.py finding.

So: CI exists and is being used (11 real merged PRs prove it), which flatly contradicts the "no CI" half of
the 2026-08-03 finding. But the specific machine this sweep ran on is both stale (26 commits behind a
working, CI-gated main) and has its own uncommitted local diff, which is a live version of the same "working
tree uncommitted" condition the checklist named 18 days ago — just for different, newer content. Anyone
treating this local checkout as the source of truth for "what's live" would be wrong on two independent axes
at once.

Caveat added at promotion (2026-08-26): reverified 2026-08-25 from the bridge-cse stag worktree's
`projects/geo_platform/` checkout — `HEAD` was still exactly `2344354`, `git fetch origin main` still
showed exactly 26 commits behind, and the uncommitted-file list was consistent. That the local `HEAD`
and behind-count are byte-identical four days later strongly suggests this checkout is dormant rather
than actively worked, consistent with this fleet's standing guidance that GEO Suite runs in its own
continuously-active dedicated session elsewhere. This checkout should therefore be read as an unchanged
snapshot, not as proof of the current upstream or actively-worked state.

## Links
- related-to, research/knowledge-home/candidates/2026-08-21/2026-08-21-geo-verify-geo-battery-currently-red-64-of-73-not-25-25.md, the uncommitted WCAG-citation change that is part of this local diff.
- related-to, research/knowledge-home/candidates/2026-08-21/2026-08-21-geo-platform-projects-dir-gitignored-reports-dir-is-tracked-deliverable.md, explains why the outer stag repo's git log shows nothing for this path.
