---
id: a-test-that-injects-one-of-two-scopes-tests-the-machine-it-runs-on-2026-09-01
type: lesson
status: candidate
source: "Recovery session, 2026-09-01 — found while wiring omar's baseline; test_prepush passed at aad9650 and failed on identical code one branch later"
project: fleet
tags: [testing, dependency-injection, flaky-tests, prepush, gates, environment-dependence]
supersedes: []
superseded_by: null
---

# When you widen what a check inspects, widen what its tests can inject — or the test starts testing the checkout

## Body

`prepush.run_secret_stage()` originally scanned one scope, the git index, and `tests/test_prepush.py`
injected it: `_run_main(..., scan_staged_fn=_clean_scan)`. The tests were deterministic.

A later fix — correct on its own terms — added a **second** scope, the outgoing commit range, because at
pre-push time the index is empty by definition. The tests were not widened to match. `scan_staged` was
still injected; `scan_push_range` was not.

From that moment the assertion *"secrets clean"* no longer meant what it said. It meant *"clean, plus
whatever the real repository's git state happens to produce."* The tests passed at `aad9650` and failed
on **byte-identical code** one branch later, purely because the checkout's tracking refs differed.

## Why it is worth a note

The failure mode is invisible in review. The diff that broke the tests contains no test change at all —
that is the point. Nothing looks wrong; the seam simply stopped covering the surface. The tests keep
passing until an environment shifts, and then they fail for a reason that has nothing to do with the
code under test, which is the fastest way to teach a team that a red test means nothing.

It also hid a second, real defect underneath it: the range scan was failing closed on a branch that *was*
tracked, and the noise from that surfaced only because the tests were investigated rather than dismissed.

## The rule

**Every scope a check inspects needs a seam, and every seam needs a safe default.** If a stage grows a
second input, the test helper grows a second parameter in the same change — defaulted to the clean,
inert value, so an existing test that says "clean" still means clean. A test that can inject some of a
function's inputs and not others is not isolated; it is a test of the machine it runs on.

## The check

After widening what any gate inspects, grep its tests for the injection helper. If the helper's parameter
list did not grow in the same commit, the tests are now environment-dependent — whether or not they are
currently green.
