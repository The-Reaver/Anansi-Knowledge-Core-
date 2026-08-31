---
id: geo-pushes-straight-to-main-with-no-staging-environment-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — verified directly against The-Reaver/The-Geo-Suite- at 73a58ce and against this repo"
project: geo
tags: [ci, deployment, staging, production-risk, geosuite]
supersedes: []
superseded_by: null
---

# GEO pushes straight to main with no PR gate, and production is the first environment its code meets

## Body

Verified in the repo's own workflow files. `tests.yml` records that *"this repo pushes
straight to `main`, no PR gate"*, and until that workflow was added *"every commit has been
landing on `main` with its test result known only to whoever ran pytest locally before
pushing."* Separately, `security-scan.yml` states plainly that *"no staging environment
exists for this project"*, and scans the production target for want of one.

Two distinct gaps, often conflated. The **test** gap is now closed: CI runs the real battery
on push and pull request. The **environment** gap is not: there is still nowhere for code to
run before customers see it, so a passing test suite is the only thing standing between a
commit and production for the revenue product.

Notably, the repo's own comments estimate the real footprint at ~0.002 vCPU / ~65MB RAM at
idle — the honest note being that a staging environment is cheap here, and its absence is a
decision rather than a constraint.

**The distinction worth keeping:** "the tests pass" and "this has run somewhere that is not
production" are different assurances. Closing the first does not close the second, and a
remediation list that treats CI and staging as one item will mark the whole thing done when
only half is.

## Links

- relates-to: the-documented-full-battery-command-reports-false-red-on-a-green-suite-2026-08-31
- relates-to: an-expected-result-must-state-a-future-condition-not-restate-the-current-complaint-2026-08-31
