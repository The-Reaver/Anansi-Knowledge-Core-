---
id: 2026-08-21-railway-redeploy-replays-pinned-commit-reconnect-forces-latest
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, railway, deploy, github-webhook, troubleshooting, project-brief-step0]
sources:
  - ref: "Archive turns 385-401: turn 385 shows a fresh push (b7c1eea, the watchPatterns removal) still serving 404, proving Redeploy/push-with-old-config was insufficient; turn 398 gives the exact disconnect/reconnect fix (branch-level first, full Source reconnect as fallback); turns 399-401 confirm 200 after the operator performs the reconnect."
    reliability: high
    origin: "STAG session, 2026-07-17, \"Project brief step 0 deployment handoff\" (backfilled from historical transcript db88cef4, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-17-backfill-db88cef4.jsonl
  turns: [385, 401]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, reproduced across multiple failed fix attempts and confirmed fixed with an objective 404->200 curl check
- verified: 2026-08-21
- REVIEW: high-impact

# Fixing a Railway service's watchPatterns bug doesn't unfreeze it if the GitHub trigger itself has gone stale; Redeploy replays the pinned commit, only a Source disconnect/reconnect force-builds latest

## Body
In `project_brief_step0_resolved`, fixing the frontend Railway service's `watchPatterns` misconfiguration (see the companion note on that bug) did not, by itself, unfreeze the service. After removing the bad `watchPatterns`, a fresh push to `main` still only triggered the backend service's deployment -- the frontend's GitHub webhook trigger had itself gone stale, independent of the `watchPatterns` bug and independent of the service's visible Settings, which showed everything correct (right repo, branch `main`, Root Directory `/frontend`, auto-deploy enabled, no watch paths).

Clicking "Redeploy" on the frontend's Deployments tab did not help either: Redeploy replays the exact commit already pinned to that deployment row, it does not pull the latest commit from the branch. Several rounds of "redeploy, check curl, still 404" confirmed this before the actual fix was found.

The fix that worked: on the frontend service's **Settings -> Source**, disconnect and reconnect the branch/repo. Reconnecting re-establishes the GitHub webhook and force-builds the latest commit on `main`. Environment variables (including `NEXT_PUBLIC_*`) survive the reconnect; the Root Directory field may need to be re-entered.

Detection method used throughout, kept as the standing verification pattern: `curl` the served app for a route path that only exists in the new code and check for 404 (stale bundle) vs 200 (live). Never infer frontend freshness from the backend being green -- they are separate Railway services on the same repo, and a push can redeploy one without the other.

## Links
- related, 2026-08-21-railway-watchpatterns-evaluated-relative-to-repo-root-not-service-root.md, the necessary-but-not-sufficient watchPatterns fix that preceded this stale-webhook fix; removing watchPatterns alone did not unfreeze the frontend, both fixes were required.
