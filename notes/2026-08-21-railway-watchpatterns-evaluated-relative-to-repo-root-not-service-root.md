---
id: 2026-08-21-railway-watchpatterns-evaluated-relative-to-repo-root-not-service-root
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision: softened the body's 'silently froze... for a large stretch' framing to make clear the watchPatterns fix was necessary but not sufficient, and added a cross-reference from the companion Redeploy/reconnect note. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, railway, deploy, watchpatterns, ci-cd, frontend, project-brief-step0]
sources:
  - ref: "Archive turns 373-386: turn 375 spots the asymmetry (backend has no watchPatterns and always deploys; frontend's watchPatterns -- app/**, components/**, etc. -- never match because Railway evaluates them against the real repo paths, frontend/app/**); turn 378 pushes the removal fix."
    reliability: high
    origin: "STAG session, 2026-07-17, \"Project brief step 0 deployment handoff\" (backfilled from historical transcript db88cef4, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-17-backfill-db88cef4.jsonl
  turns: [373, 386]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, root-caused and fixed with an objective before/after curl check
- verified: 2026-08-21
- REVIEW: high-impact

# Railway's watchPatterns are evaluated against the repo root, not a service's own Root Directory, so a subfolder service's globs can silently never match

## Body
On Railway, a service's `railway.json` `watchPatterns` field is evaluated relative to the **repository root**, not the service's own Root Directory setting. In `project_brief_step0_resolved`, the frontend Railway service has its Root Directory set to `frontend/`, and `frontend/railway.json` declared `watchPatterns` (`app/**`, `components/**`, `hooks/**`, `lib/**`, etc.) written as if they were relative to that service root. Because Railway actually matches these globs against the real repository paths (`frontend/app/**`, not `app/**`), none of them ever matched, so any push that only touched frontend files never triggered a rebuild of that service -- while the backend service, which had no `watchPatterns` at all, redeployed on every push without issue.

Removing `watchPatterns` was a necessary but not sufficient fix. The frontend was in fact stuck on an old commit (`07da90d`) for a large stretch of the session, but as the companion note on Redeploy/reconnect behavior documents, a second, independent cause -- a stale GitHub webhook trigger -- also existed and had to be fixed separately (via a Source disconnect/reconnect) before the frontend actually resumed deploying on push. Both fixes were required; neither alone unfroze the service. The failure was invisible from the Railway UI (the service's config looked correct at a glance) and was only surfaced by noticing that `curl` against a known-new route path returned 404 while an existing route returned 200 -- i.e. by checking the actually-served app rather than trusting the dashboard or a "Redeploy" click.

Fix applied: remove `watchPatterns` from `frontend/railway.json` entirely, matching how the backend service (which has none and always deploys) is configured.

Rule for future services in this or similar repos: never set `watchPatterns` on a service whose Root Directory is a subfolder unless every pattern is explicitly prefixed with that subfolder (e.g. `frontend/app/**`). This is exactly the kind of gate the project's own deploy-config validator (S1) was flagged as missing during this session, since the failure mode is silent rather than a build error.

## Links
- related, 2026-08-21-railway-redeploy-replays-pinned-commit-reconnect-forces-latest.md, the second, independent stale-webhook fix that was also required to actually unfreeze the frontend after this watchPatterns fix.
