---
id: geosuite-p0-site-repos-flag-fixed-2026-08-31
type: finding
status: ratified
source: this chat, 2026-08-31, live Railway + Supabase check from a session working on Anansi-Knowledge-Core-
project: geo
tags: [geosuite, production, data-loss, p0]
supersedes: []
superseded_by: null
---

# GeoSuite's P0 (sites discarded on redeploy) had its flag flipped, unconfirmed by real use yet

## Body

GeoSuite's own `AUDIT_AND_REPORTS_ROADMAP.md` names its own P0, ranked above every other
open item: `GEO_USE_SUPABASE_SITE_REPOS` unset (or set but unable to reach Supabase) makes
`sites.py` silently fall back to a process-local in-memory repo. `_use_supabase_site_repos()`
swallows *any* exception from `get_supabase_admin()`, so the failure is invisible — a rep is
told "nothing saved yet" about work that is genuinely gone on the next redeploy. As of
2026-08-30 this was still listed `open, operator`.

**What was checked and done, from this session:**
1. Read Railway's variable *names* for the backend service (`The-Geo-Suite-`, project "The
   GEO Suite") — values are redacted here (OAuth connection, not an API token/session), but
   confirmed `GEO_USE_SUPABASE_SITE_REPOS` existed as a variable (not literally absent) and
   `SUPABASE_JWT_ALLOW_HS256` (the separate S-8 concern) did not exist at all, which the
   roadmap says is one of the two safe states for that one.
2. Before touching anything, verified the real prerequisite the roadmap names: the four
   tables (`content_pages`, `schema_records`, `optimization_files`, `audit_results`) actually
   exist live in the production Supabase project (`lhzxmvjwqllmnqecfxpm`), via
   `list_tables` — all four present, RLS enabled, 0 rows (consistent with the flag being off
   until now).
3. Set `GEO_USE_SUPABASE_SITE_REPOS=1` on the Railway backend service. The API confirmed the
   write and that it triggered a redeploy.
4. Attempted to verify with a real write: the actual persist path
   (`POST /{site_id}/audit` in `sites.py`) requires `require_sales_agent` — a genuine signed-in
   agent JWT plus a site-ownership check. No real login was available, and forging or
   bypassing that auth to manufacture a test write was correctly refused rather than
   attempted. Row counts in all four tables were still 0 immediately after the flag flip —
   inconclusive (no real save event had happened yet), not evidence of failure.

**Left open, by the operator's own choice:** verification against a real save waits for
organic use rather than a synthetic test write. If the next real site save still doesn't
show up in `audit_results` etc., the next thing to check is whether `SUPABASE_URL` (also
redacted, unverifiable from here) has a trailing newline — `S-14`/the S-29 closure section
name this as a live, separate way the same silent-downgrade exception can fire.

## Links

- geosuite-build-ledger-proposal-2026-08-25 (this is exactly the kind of build-ledger entry
  that proposal describes — landed here as a regular finding instead, since the ledger itself
  is still just a proposal, not yet built)
