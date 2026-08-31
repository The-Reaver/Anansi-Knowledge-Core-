---
id: geosuite-s48-fix-2026-08-31
type: finding
status: ratified
source: this chat, 2026-08-31, S-48 fixed directly in The-Reaver/The-Geo-Suite- on branch claude/s48-repo-flag-boot-checks, PR #5
project: geo
tags: [geosuite, testability, mutation-testing, s48]
supersedes: []
superseded_by: null
---

# GeoSuite's S-48 (the 4 siblings of S-14's silent-swallow bug) is fixed, and mutation testing found a second copy of S-14's own testability bug

## Body

`geosuite-s14-fix-2026-08-31` (this same candidates folder) fixed `_use_supabase_site_repos()`'s
silent `except Exception: return False`, and deliberately left four sibling functions with the
identical pattern open as a new tracked candidate (S-48 in `AUDIT_AND_REPORTS_ROADMAP.md`), to
avoid widening that fix's scope without review. This note captures picking S-48 back up in a
follow-on session, per the operator's explicit "yes, pick up S-48 now."

**What shipped** (`The-Reaver/The-Geo-Suite-` PR #5, branch `claude/s48-repo-flag-boot-checks`):
the identical two-part fix S-14 used, applied to all four siblings —
`_use_supabase_analytics_tracking_approvals_repo` and `_use_supabase_citation_observations_repo`
(`sites.py`), `_use_supabase_compliance_repo` (`compliance.py`), `_use_supabase_contact_repo`
(`contact.py`): a `logger.exception(...)` in the per-request fallback, plus a new
`verify_*_configuration()` wired into `main.py` before `app = FastAPI(...)`.

**The finding worth keeping independent of GeoSuite:** S-14's own closure note had already
recorded a testability bug — the original `sites.py` function re-imported `get_supabase_admin`
*locally* inside the function body, shadowing the module-level import and making it invisible to
`unittest.mock.patch("app.routers.sites.get_supabase_admin", ...)`. Picking up S-48 found the
**same bug independently present** in `compliance.py` and `contact.py` — neither had been touched
by the S-14 fix, so this wasn't inherited, it was the same anti-pattern occurring twice more on its
own. It was **reproduced directly, not assumed**: mutation-testing pass 3 (of 3) deliberately
reintroduced the local import as a mutation and re-ran the tests, and got the exact same failure
mode S-14's own investigation had found — `patch(...)` became invisible, the real unmocked client
ran instead, and a test expecting `False` got `True`.

**Why this is the durable lesson, not just "another bug fixed":** a local re-import that shadows an
already-existing module-level import of the same name is a pattern that (a) reads as completely
inert in a normal test run — it changes nothing about program behavior, so a suite with no test
targeting that exact function can pass forever with the bug present — and (b) is only caught by
mutation testing that specifically tries reintroducing the exact suspected defect and checking the
tests actually respond, not just by writing more tests. Three occurrences of the identical
copy-pasted anti-pattern in one small file family is itself a signal: whenever fixing "function A
had a testability bug from a local shadowing import," check every sibling function copied from the
same original pattern, not just the one instance in front of you — this is what finding it in 2 of
4 siblings, on the very next slice, means in practice.

**Verification performed**, matching S-14's own discipline: 24 new parametrized tests
(`tests/test_repo_flags_config.py`), three-way mutation testing (stripping the new log calls →
exactly those 4 assertions failed; no-opping the new boot checks → exactly those 4 assertions
failed; reintroducing the local-import shadow → reproduced the exact S-14 failure mode), full suite
at the exact CI command (1243 passed, 0 failed), and `scripts/granularity_check.py` PASS on both of
the two commits the fix was split into (split because the combined diff tripped the repo's own p90
size gate — same reasoning the repo's own S-47 slices used for splitting).

**Status:** no further sibling functions of this shape are known to remain in GeoSuite; S-14 and
S-48 together close the pattern.

## Links

- geosuite-s14-fix-2026-08-31 (this candidates folder) — the fix and testability bug this note's
  own finding extends
- geosuite-roadmap-audit-2026-08-31 (this candidates folder) — named S-14; S-48 was the sibling gap
  S-14's own closure note opened
