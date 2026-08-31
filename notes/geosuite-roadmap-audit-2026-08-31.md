---
id: geosuite-roadmap-audit-2026-08-31
type: finding
status: ratified
source: this chat, 2026-08-31, a full pass over The-Reaver/The-Geo-Suite-'s AUDIT_AND_REPORTS_ROADMAP.md, every item checked against the live code/schema rather than taken on the doc's word
project: geo
tags: [geosuite, roadmap, audit, backlog]
supersedes: []
superseded_by: null
---

# GeoSuite's S-3 through S-38 backlog: what's actually done vs. actually open, independently verified

## Body

The roadmap doc (`AUDIT_AND_REPORTS_ROADMAP.md`) itself has drifted in places — a bullet list in
one section calling S-35 open while a note added right after it says S-35 landed; a call-site
count that only added up once a second file was checked. So every item below was checked directly
against the current code/schema in a real clone of the repo, not trusted from the doc's own
status labels. This is a status snapshot as of 2026-08-31, not a re-derivation of the analysis —
the roadmap's own diagnosis of each item was accurate every time it was checked; what varied was
whether it had actually been fixed since being written.

**Purpose:** so the next session that opens this backlog doesn't have to re-run this same
25-item verification pass from zero.

### Genuinely done (verified in code, not just claimed)

| Item | What was verified |
|---|---|
| S-5 | `_REQUIRED_CLAIMS = {"require": ["sub", "exp"]}` (`permissions.py:76`) actually passed into both `jwt.decode()` call sites (:214, :263), not just defined. |
| S-8 | `is_unusable_jwt_secret()` actually called inside the live HS256 branch (`permissions.py:247`), guarding the placeholder-secret-committed-to-repo case. |
| S-15 | Commit `8ff22c5` real; gives the more-common pipeline load-failure path actionable copy instead of a raw reason string. |
| S-16 | `page.tsx:139`: `result.ownershipUnverified` checked *before* any `sites.length` branch — code's own comment confirms this is deliberate. |
| S-17 | Commit `7dfbc34` real; `package.json`'s `test` script (`node --test "app/**/*.test.ts"`) exists and runs. |
| S-35 | Commit `01dfaa0`; 19 real unit tests for `is_unusable_jwt_secret`, mutation-tested (a planted mutation failed 3 tests, reverted to green). |

### Still open, each independently confirmed against current code

**Ownership / auth cluster** — these six share a root cause (no shared ownership predicate) and
would mostly collapse together if S-3 landed:
- **S-3** — no `_is_owned_by()` predicate exists anywhere; three call sites (`list_pipeline`,
  `_require_site_owner`, `customize_prospect`) still each implement ownership checking their own way.
- **S-6** — `_require_site_owner` still 403s a NULL-owner site with "belongs to a different agent,"
  implicitly via `str(None) != str(caller_id)`, no explicit NULL branch.
- **S-7** — `prospects.agent_id references public.users(id)` has no `ON DELETE` clause; no endpoint
  anywhere writes `agent_id` on an existing row. No reassignment path exists; still a real product
  decision nobody's made.
- **S-9** — `contact.py`'s two `site_id` fields are still unauthenticated `str`, never passed
  through `_parse_site_id`; still only `except ValueError`, so a malformed id hitting the real
  Supabase-backed `contact_submissions` table (uuid column) would 500 instead of 422.
- **S-10** — no `SiteId` type alias, no `_site_id_dep`, no route-enumerating meta-test. S-2's fix
  is still maintained purely by convention across all 13 call sites (8 in `sites.py`, 5 in
  `site_intelligence.py`).
- **S-11** — `_parse_site_id`'s own current docstring says explicitly: "Rejecting outright...
  tracked as its own candidate, not done here." Still silently zero-pads a short malformed id
  into a different valid UUID instead of rejecting it.
- **S-12** — `site_intelligence.py:96` still imports `_load_site_facts_or_400`, `_parse_site_id`,
  `_require_site_owner` directly from `sites.py`'s private namespace.

**Ephemeral-storage cluster:**
- **S-13 (= the roadmap's own P0)** — this session set `GEO_USE_SUPABASE_SITE_REPOS=1` on the live
  Railway backend (see `geosuite-p0-site-repos-flag-fixed-2026-08-31`, this same candidates
  folder) after confirming the four prerequisite tables exist live in Supabase. **Not fully
  closed** — see S-14.
- **S-14** — `_use_supabase_site_repos()` still does bare `except Exception: return False`, zero
  logging, no boot-time failure. Checked the live deploy's logs directly: filtering for
  "supabase" returns zero lines, in either direction. This means the P0 flag flip above cannot be
  confirmed working or broken from logs alone — a real site save (or fixing S-14 itself) is the
  only way to know.

**Frontend copy / UX cluster (all from the S-15 review panel, none folded into that diff):**
- **S-18** — `PipelineRow.tsx` still renders raw reason codes (`(timeout)`, `(backend-503)`)
  directly into rep-facing copy, the same defect S-15 fixed elsewhere on the same page.
- **S-19** — `granularity_check.py`'s no-args mode still only does `git diff --cached`/`git diff
  HEAD`; still blind to untracked files.
- **S-20** — `reason` is still plain `string` end to end in `actions.ts` (lines 52, 131), not a
  literal union — a missing copy case still isn't a compile error.
- **S-21** — confirmed by direct comparison: `globals.css`'s real `.nv-btn.solid` is a
  `linear-gradient` plus inset shadow; `RetryButton.tsx` still uses a flat `background:
  "var(--nv-accent)"`. The "matching globals.css" comment is still false.
- **S-22** — no `middleware.ts` exists anywhere in `frontend/`. `/nova/*` has no edge auth gate;
  auth is enforced only inside `fetchPipelineList()`.
- **S-23** — the `ownershipUnverified` panel's headline is literally "Your pipeline didn't load,"
  identical vocabulary to a genuine load failure despite being a deliberate HTTP-200 withholding.
  No reference code. Its inline style object is copied verbatim three times in `page.tsx` (lines
  90, 164, 201).
- **S-24** — `backend-${res.status}` is still the entire "reference" a rep can give support — no
  request id, no timestamp, confirmed absent anywhere in the failure path.
- **S-25** — mixed: the panel's headline *is* now a real `<h2>` (done), but the outer container
  still has no `role="alert"`/`aria-live`; the "tell-manager" states still have `controls: []`
  (genuinely nothing to press); no ESLint config exists anywhere in `frontend/` (`npm run lint`
  would drop into `next lint`'s interactive setup); `RetryButton` still has no cooldown timer
  despite the 429 copy telling the rep to "give it a minute."

**Auth-module cluster (opened by the S-29 panel):**
- **S-36** — `get_jwks_client()` (`permissions.py:145`) still raises `HTTPException` from what's
  meant to be a pure `@lru_cache`d factory. Currently has exactly one caller (inside `verify_token`
  itself), so this is a forward-looking risk (S-26/S-27, if built, would call it from a non-HTTP
  context) rather than a live bug today.
- **S-37** — `verify_token` (local JWT decode → dict) and `get_current_user` →
  `resolve_profile_from_token` (live Supabase round-trip per request → `ProfileResult`) are still
  two incompatible mechanisms in one module. Visible symptom: `require_owner_membership` couldn't
  be named `require_owner` — that name was already taken by the other mechanism's version.
- **S-38** — `tests/test_jwt_hs256_gate.py`'s own docstring still cites `backend/tests/` and
  `QUARANTINE.md`; neither exists anywhere in the repo (confirmed directly).

### Separately noted, not part of the roadmap

While checking S-13/S-14's live deploy logs, found the backend's logs are dominated by heavy,
constant automated vulnerability-scanner traffic (hundreds of known-CVE/credential-harvesting
paths probed), enough to hit Railway's own log-rate limit and drop 735 of the app's own log
messages in one ~1-second window. Not evidence of a breach — routine background noise for any
public endpoint — but worth knowing the app's own legitimate log output is competing with that
volume for the same rate limit.

## Links

- geosuite-p0-site-repos-flag-fixed-2026-08-31 (this candidates folder) — the P0/S-13 action this
  audit's S-14 finding directly qualifies
- geosuite-build-ledger-ruling-2026-08-25 (notes/) — this backlog is exactly the kind of thing
  `docs/build-ledger.md` in The-Reaver/The-Geo-Suite- could eventually index, once GeoSuite's own
  ledger-trigger criteria are applied retroactively to items like these (not done here — that
  ledger's scope is non-obvious build decisions already shipped, not an open backlog)
