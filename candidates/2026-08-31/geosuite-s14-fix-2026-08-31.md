---
id: geosuite-s14-fix-2026-08-31
type: finding
status: candidate
source: this chat, 2026-08-31, S-14 fixed directly in The-Reaver/The-Geo-Suite- on branch claude/s14-site-repos-boot-check, PR #4
project: geo
tags: [geosuite, production, data-loss, s14, testability]
supersedes: []
superseded_by: null
---

# GeoSuite's S-14 (silent Supabase-fallback swallow) is fixed, and it made the P0 flag flip verifiable

## Body

`geosuite-p0-site-repos-flag-fixed-2026-08-31` (this same candidates folder) flipped
`GEO_USE_SUPABASE_SITE_REPOS=1` on Railway but left it unconfirmed: `_use_supabase_site_repos()`
in `sites.py` did `except Exception: return False` with zero logging, so nothing in the live logs
could say whether the flag was actually working. `geosuite-roadmap-audit-2026-08-31` named this
gap explicitly as S-14 and flagged it as the next thing worth prioritizing. The operator then said
"prioritize S-14 next" and, given the choice, chose to have it actually fixed in GeoSuite rather
than just written up — a deliberate, explicit exception to the standing "GeoSuite is being worked
in another session, read-only" constraint, scoped to this one fix.

**What shipped** (`The-Reaver/The-Geo-Suite-` PR #4, branch `claude/s14-site-repos-boot-check`):

1. The per-request fallback now `logger.exception(...)`s, naming S-14, before returning `False` —
   so a client that stops working *after* boot (a rotated key, a Supabase outage) leaves a trace.
2. A new `verify_site_repos_configuration()`, wired into `main.py` to run before
   `app = FastAPI(...)`, fails the process at import time if the flag is on but the Supabase admin
   client can't be built at all. A misconfigured deploy now fails to start instead of starting and
   silently degrading into the ephemeral in-memory repo.
3. Both checks are kept deliberately separate: boot catches a config that was never going to work;
   the per-request log catches anything that stops working after boot already passed.

**A second, pre-existing bug found for free, by mutation testing rather than by inspection:** the
original `_use_supabase_site_repos()` had a *local* `from ..core.supabase_client import
get_supabase_admin` re-import inside the function body, shadowing the module-level import already
present at the top of the file. `unittest.mock.patch("app.routers.sites.get_supabase_admin", ...)`
— this suite's own established mocking convention — could never see that local binding. A test
written against the convention would silently exercise the real, unmocked client instead of the
mock. Caught only because reverting the fix and re-running the new tests produced 2 unexpected
passes instead of failures; root-caused, then fixed by deleting the redundant local import in
favor of the module-level one that was already there.

**Verification performed**, matching this repo's own documented discipline:
- 7 new tests (`tests/test_site_repos_config.py`), covering flag-unset / flag-off /
  client-builds / client-fails for both functions.
- Mutation-tested: reverted the fix, 5/7 tests failed for the right reason; the other 2 passed
  even reverted, which is what surfaced the local-import bug above.
- End-to-end: importing `main.py` with the flag on and `SUPABASE_URL` blank now raises
  `SupabaseConfigError` at import time; before the fix it imported cleanly.
- Full suite, the exact CI command (`python -m pytest -q`, matching `.github/workflows/tests.yml`,
  not the legacy per-file-subprocess `ci_verify_geo.py` the roadmap itself flags as producing
  false-reds): 1184 passed, 0 failed.
- `scripts/granularity_check.py`: PASS (4 files, 229 lines, one top-level directory).

**Deliberately not fixed in this slice:** four sibling functions share the identical
`except Exception: return False`-with-no-logging pattern —
`_use_supabase_analytics_tracking_approvals_repo` and `_use_supabase_citation_observations_repo`
in `sites.py`, `_use_supabase_compliance_repo` in `compliance.py`, `_use_supabase_contact_repo` in
`contact.py`. Left open as a new tracked candidate, **S-48**, in
`AUDIT_AND_REPORTS_ROADMAP.md`, rather than widened into this fix — matching this repo's own
established convention (seen already in the S-15 review panel, which opened S-18 through S-25
rather than folding them in).

**What this closes, and what it still doesn't:** the P0 flag flip is now *observable* — a future
Supabase misconfiguration on this flag will either fail the deploy outright or show up in logs
naming S-14. It still hasn't been confirmed against a real site save, by the operator's own earlier
choice to wait for organic use rather than forge sales-agent auth for a test write.

## Links

- geosuite-p0-site-repos-flag-fixed-2026-08-31 (this candidates folder) — the P0 action this fix
  makes verifiable
- geosuite-roadmap-audit-2026-08-31 (this candidates folder) — named S-14 as the gap; this note
  closes it
- geosuite-build-ledger-ruling-2026-08-25 (notes/) — this is exactly the kind of non-obvious build
  decision (why two separate checks, why the sibling functions were left open) that repo's own
  ledger is meant to index, once it exists
