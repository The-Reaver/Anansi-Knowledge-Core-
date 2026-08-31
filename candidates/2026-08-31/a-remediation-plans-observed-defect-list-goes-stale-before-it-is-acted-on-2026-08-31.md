---
id: a-remediation-plans-observed-defect-list-goes-stale-before-it-is-acted-on-2026-08-31
type: lesson
status: candidate
source: "Recovery session, 2026-08-31 — verified directly against The-Reaver/The-Geo-Suite- at 73a58ce and against this repo"
project: fleet
tags: [planning, audit, verification-discipline, stale-findings, remediation]
supersedes: []
superseded_by: null
---

# Two of the plan's observed defects were already fixed by the time anyone read the plan

## Body

A remediation plan written this session listed, as **observed** defects in GEO: no CI runs
the tests, and `facts_floor` has no writer. Checked against the repository the same day,
both were already false.

`.github/workflows/tests.yml` exists and runs `python -m pytest -q` on push to main, on
pull request, and on manual dispatch. `facts_floor` has a writer — it is computed in
`sites.py` and threaded through `site_pipeline.py`, and the repository's HEAD commit is
literally *"S-52 — facts_floor has a writer, and a production landmine was found."*

Neither claim was wrong when written. Both were overtaken by slices landing in parallel
while the plan was being drafted. In a fleet running many concurrent sessions, an audit's
findings decay in hours, not weeks — the same concurrency that makes the fleet productive
makes its own status reports stale fastest.

**Check before acting on any audit or plan item:** re-verify the defect still exists against
the current HEAD, not against the plan. Acting on a stale item wastes the work; worse,
"fixing" something already fixed can revert the fix. The corollary for writing plans: date
every observed defect and name the commit it was observed at, so a reader can tell what to
re-check rather than guessing.

## Links

- relates-to: an-expected-result-must-state-a-future-condition-not-restate-the-current-complaint-2026-08-31
- relates-to: geo-pushes-straight-to-main-with-no-staging-environment-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
