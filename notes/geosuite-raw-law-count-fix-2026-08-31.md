---
id: geosuite-raw-law-count-fix-2026-08-31
type: finding
status: ratified
source: this chat, 2026-08-31, fixed directly in The-Reaver/The-Geo-Suite- on branch claude/fix-raw-law-count-20260831, PR #7
project: geo
tags: [geosuite, ci, red-main]
supersedes: []
superseded_by: null
---

# GeoSuite's main went red from a stale hardcoded file-count assertion, fixed

## Body

A routine "check on GeoSuite" status check found `main`'s CI red: a different session's "raw_law:
rescue three real accessibility sources" commit added 3 real legal-citation files (42-44: ADA
Title III, DOJ's 2022 web accessibility guidance, DOJ's Title II WCAG final rule) to
`knowledge_core/feeds/regulatory/raw_law/`, but didn't update
`tests/test_knowledge_core_feeds_import.py`'s `test_regulatory_raw_law_data_is_untouched_by_the_import_fix`,
which asserts an exact count of files in that directory. Result: `1 failed, 1262 passed` on `main`.

Not this session's own PRs (#5, #6) — confirmed no file overlap before investigating further.

**Fix:** verified the real count directly against the directory (43, matching the test's own
filter logic — `f.endswith(".md") and f[0].isdigit()`), bumped the literal from 40 to 43.

**Verification:** `test_knowledge_core_feeds_import.py` alone: 3 passed. Full suite, exact CI
command (`python -m pytest -q`): 1263 passed, 0 failed. `scripts/granularity_check.py`: PASS
(1 file, 10 lines).

**Why this wasn't a one-off:** this exact literal has now been corrected five times in three days
(20 → 34 → 39 → 40 → 43) as different sessions added files — see
`hardcoded-count-assertion-anti-pattern-2026-08-31` (this candidates folder) for the generalized
lesson this is an instance of, and the shape of test that wouldn't have this failure mode.

## Links

- hardcoded-count-assertion-anti-pattern-2026-08-31 (this candidates folder) — the generalized
  lesson this specific fix is an instance of
- geosuite-s48-fix-2026-08-31 (this candidates folder) — this session's other GeoSuite work from
  the same day, found via the same "check on GeoSuite" status-check habit
