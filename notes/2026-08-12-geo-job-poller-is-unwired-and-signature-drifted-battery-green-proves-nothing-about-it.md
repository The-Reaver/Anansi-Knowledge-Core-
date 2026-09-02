---
id: 2026-08-12-geo-job-poller-is-unwired-and-signature-drifted-battery-green-proves-nothing-about-it
type: finding
status: ratified
ratified: "2026-08-12, operator instruction, direct re-verification by this session's Claude; the note's own body states exactly what was re-checked (ci_verify_geo.py run, a module-import plus signature-introspection check, the commit hashes on origin/main)"
project: geo
tags: [geo, scheduler, poller, jobs, contract-drift, quarantine, mocked-tests, verification, deploy-readiness, resolved]
sources:
  - ref: "projects/geo_platform/backend/app/scheduler/poller.py, app/repositories/jobs_repo.py, app/main.py, app/models/job.py"
    reliability: high
    origin: direct code read, this session
  - ref: "backend/tests/test_scheduler_poller.py"
    reliability: high
    origin: direct code read, this session, confirms the quarantined test targets a third, non-existent API
  - ref: "ci_verify_geo.py battery run; commits 0755fad and 1260445 on origin/main"
    reliability: high
    origin: run live and pushed live, this session
provenance:
  archive: research/knowledge-home/raw/2026-08-12-geo-poller-fix-and-platform-identity-session.jsonl
  turns: [1, 14]
risk_class: B
evidence_state: CORROBORATED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# GEO's background job poller was unwired AND signature-drifted, and its only tests are quarantined phantoms, so the 64/64 battery proved nothing about the scheduler (fixed same day)

## Resolved, same day

Items 1 and 2 below are fixed: `poller.py` reconciled against the real `JobsRepository`/
`handlers.dispatch` contracts, `JobPoller` wired into `app/main.py` via a guarded FastAPI
`lifespan`, `reset_stuck_jobs()` now called on startup. Commits `0755fad` (fix) and `1260445`
(a correction to this same session's dev-log entry, see below) are pushed to `origin/main`.
Verified: `ci_verify_geo.py` still 64/66 locally (2 pre-existing, unrelated failures); module
import + signature-introspection check confirmed the poller calls only parameters
`JobsRepository` actually accepts. **Item 3 (quarantined phantom test) is NOT fixed** — still
open, still tracked below.

Also correcting this note's own paragraph 2 and its "relates" link: **"sister-platform (Base
Platform)" was never a second product.** `The-Reaver/stag-platform` (the name `HANDOFF_DEPLOY.md`
and the old clone at `projects/project_brief_step0_resolved` used) and
`The-Reaver/Stag-GEO-Platform` are the same GitHub repository — confirmed via `gh repo view`
(identical repo ID/createdAt/pushedAt) and `git merge-base --is-ancestor` (the old clone's tip is
an ancestor of this repo's real `origin/main`, zero unique history). Full detail in the sibling
note `2026-08-12-two-platforms-not-to-conflate-...md`. What `HANDOFF_DEPLOY.md` documents is an
**earlier poller bug in this same repo's own deploy history** (a missing-pool `TypeError` in the
lifespan, already fixed at that time, two methods), not a second product independently
re-discovering the same drift. There was one poller, one drift, found twice at different points
in this one repo's timeline. The old clone has since been moved to
`Archive/project_brief_step0_resolved`.

## Original body (2026-08-12, before the fix)

A read-only drift check of GEO's (The-Reaver/Stag-GEO-Platform) background job system found three
compounding problems, all static-confirmed from the code, no pytest run (the venv lacks pytest and
these tests are quarantined anyway).

1. The poller is never wired into the running app. app/main.py builds `app = FastAPI(...)` and
   includes six routers with no lifespan and no startup hook; the only references to `JobPoller` live
   in its own module and a docstring/`__all__` in app/scheduler/__init__.py. `uvicorn app.main:app`
   therefore runs with no scheduler at all. Net effect in production today: the entire timed-job
   system does nothing. Missed-call SMS follow-ups and Twilio number auto-release never fire. This is
   not a crash; it is silent absence.

2. If it were wired, it would raise TypeError on the first claim of every poll pass. poller.py calls
   the real JobsRepository with keyword arguments the repo does not accept:
   `claim_due_jobs(now=..., limit=...)` — repo signature is `claim_due_jobs(self, limit=50)`, no `now`;
   `mark_succeeded(job_id=..., result=..., finished_at=...)` — repo is `mark_succeeded(self, job_id,
   result=None)`, no `finished_at`; `mark_failed(job_id=..., error=..., finished_at=...)` — repo is
   `mark_failed(self, job_id, error, retry_at=None)`, no `finished_at`. `_safe_poll` catches and logs
   the TypeError so the web server stays up, but zero jobs would ever execute. This is broader than the
   earlier poller drift this same repo's own HANDOFF_DEPLOY.md records from a prior deploy attempt
   (a missing-pool TypeError, two methods, already fixed at that time); here it is three, on the
   claim/succeed/fail path directly. (See "Resolved, same day" above — the "sister-platform" framing
   originally here was wrong; there is one repo, not two.)

3. The green battery is blind to all of it. backend/tests/test_scheduler_poller.py targets a third,
   phantom contract matching neither real file: it constructs `JobPoller(repo=, handlers=, clock=, ...)`
   (the real __init__ has no `handlers` or `clock`), its FakeJobsRepo uses `mark_succeeded(job_id,
   completed_at)` / `mark_failed(job_id, error, completed_at)` (real poller passes `finished_at`, real
   repo accepts neither), and `make_job(..., started_at=None)` asserts `job.started_at` though the real
   Job dataclass has no `started_at` field (it carries `claimed_at`/`completed_at`). Those tests would
   error at construction. They live in backend/tests/, the quarantined orphan dir excluded from the
   battery (STATUS.md + backend/tests/QUARANTINE.md), so 64/64 green says nothing about the scheduler.

Secondary: both poller.py and jobs_repo.py docstrings claim the poller calls `reset_stuck_jobs` on
startup; poller.start() never calls it, so a job left `running` by a crash would never recover even
after the other fixes.

Verdict: not a web-app deploy blocker (the app boots; the poller is simply absent), but a real,
untested functional gap in anything time-delayed. Fix is a self-contained pass: reconcile the three
signatures poller.py <-> jobs_repo.py, wire JobPoller into a main.py lifespan (build its asyncpg pool
from SUPABASE_DB_URL, ssl=require, wrapped so a scheduler failure cannot take down the web server),
call reset_stuck_jobs on startup, then rewrite test_scheduler_poller.py against the real contract and
pull it out of quarantine.

## Links

- extends, 2026-08-09-mocked-boundary-tests-prove-the-caller-not-the-mocked-functions-internals.md — a
  concrete, dated instance: the poller tests exercise a FakeJobsRepo whose signatures match neither the
  real repo nor the real caller, so they prove nothing about the live path.
- depends, backend/tests/QUARANTINE.md — the quarantine is exactly why these broken tests never turned
  the battery red; a quarantined suite that also targets a phantom API is doubly worthless.
- relates, HANDOFF_DEPLOY.md — documents an earlier, already-fixed poller drift in this same repo's
  own deploy history (not a second product; see "Resolved, same day" above for the correction).
- relates, 2026-08-12-two-platforms-not-to-conflate-geo-suite-is-stag-geo-platform-not-base-platform.md
  — the full correction of the one-repo-not-two finding this note's original body got wrong.
