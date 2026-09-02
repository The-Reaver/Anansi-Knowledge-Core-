---
id: 2026-08-27-pytest-setup-function-is-a-no-op-for-tests-inside-a-class
type: lesson
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: fleet
tags: [pytest, testing, test-isolation, silent-failure, python]
sources:
  - ref: "GEO Suite, 2026-08-27: tests/test_admin_vendor_keys_router.py's setup_function had never executed since the file was authored -- every test in it lives inside a class; found only via a cross-test vendor-name collision, fixed with @pytest.fixture(autouse=True), and mutation-tested by reverting to the no-op and confirming the exact predicted collision"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [19, 19]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# pytest's setup_function never runs for tests defined inside a class, so a test file's isolation can be a silent no-op from the day it was written

## Body
`setup_function` / `teardown_function` are pytest's module-level xunit-style hooks. pytest
invokes them **only for bare top-level test functions**. For test methods defined inside a class,
they are never called -- and pytest does not warn, because a module-level function named
`setup_function` is not an error, it is just unused.

In `tests/test_admin_vendor_keys_router.py`, every test lived inside a class, so the file's
`setup_function` reset had been a silent no-op since the day the file was written. The tests
still passed the whole time -- but only by accident, because each test happened to use a
different vendor name, so nothing ever collided. The bug surfaced only when a new test needed
`"anthropic"` again, the same vendor an earlier class had already saved a real key for. The stale
row made an unrelated code path look like a valid update, which is the dangerous version of this
failure: not a red test, but a **green test asserting the wrong thing.**

The correct hooks for class-based tests are `setup_method` / `teardown_method`, or better, an
`@pytest.fixture(autouse=True)` -- which works in both shapes and does not silently vanish if the
tests are later refactored into or out of a class.

The general lesson beyond pytest: **test isolation that is never exercised is indistinguishable
from test isolation that works.** A reset hook has no failing case of its own. If it silently
stops running, the suite stays green until unrelated tests happen to collide. Worth mutation-
testing isolation machinery itself -- deliberately break the reset and confirm a test actually
fails -- which is exactly how this fix was proven.

## Links
- same-family-as: notes/2026-07-24-batch3-pytest-only-tests-false-green-hole.md — test
  machinery that appears to run, executes nothing, and reports success. There the harness
  ran zero tests and exited 0; here the isolation hook never fired. Same structural defect
  one level down, and the reason that note's rule ("the verifier itself needs verifying")
  extends to fixtures, not just runners.
- relates-to: 2026-08-27-a-zero-vulnerability-adversarial-pass-still-earned-its-cost
