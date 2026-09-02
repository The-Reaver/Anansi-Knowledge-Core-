---
id: 2026-08-27-verify-a-check-constraints-real-name-before-dropping-it
type: lesson
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: fleet
tags: [postgres, migrations, ddl, silent-failure, supabase]
sources:
  - ref: "GEO Suite migration 20260827020000_vendor_credentials_add_places_and_url.sql, 2026-08-27: the live constraint name was confirmed via pg_constraint before writing the DROP CONSTRAINT IF EXISTS, rather than trusting Postgres's default <table>_<column>_check convention"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [24, 24]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Query pg_constraint for a CHECK constraint's real name before DROP CONSTRAINT IF EXISTS, because a wrong guess silently no-ops instead of erroring

## Body
To widen a CHECK constraint you must drop and recreate it, and to drop it you must name it.
Postgres's default naming convention (`<table>_<column>_check`) is regular enough that it is
tempting to just write the predicted name into `DROP CONSTRAINT IF EXISTS`.

The trap is `IF EXISTS`. If the guessed name is wrong, the statement **silently succeeds as a
no-op** -- it does not error, because not existing is precisely the case `IF EXISTS` is there to
tolerate. The subsequent `ADD CONSTRAINT` then succeeds too, and you are left with **two CHECK
constraints coexisting invisibly**: the old narrow one still rejecting the new values the
migration was written to permit, and a new one that appears to have worked. The migration reports
success. The feature stays broken. Nothing in the logs points at the cause.

The convention is not guaranteed: a constraint declared inline with an explicit `CONSTRAINT name`
clause, one created by an earlier migration under a different name, or a second constraint on the
same column all break it.

So: query `pg_constraint` (filtered by `conrelid` and `contype = 'c'`) for the real name first,
then write the DDL against what is actually there. In this case that cost exactly one extra tool
call and eliminated the risk entirely -- an unusually good trade, given the failure it prevents
is both silent and hard to attribute later.

Generalisation: `IF EXISTS` / `IF NOT EXISTS` guards convert "wrong identifier" from a loud error
into a silent no-op. That is what they are for, and it is also why any DDL that depends on
naming a pre-existing object should verify the name rather than predict it.

**Evidence status: this is a near-miss, not an incident.** The silent no-op described here
never actually happened — `pg_constraint` was queried first, so the guessed-name failure was
prevented rather than observed. The Postgres semantics are real and checkable (`IF EXISTS`
turns a wrong identifier into a successful no-op by design), but a future reader should know
this note records a hazard that was avoided, not one that bit us.

## Links
- relates-to: 2026-08-27-a-committed-migration-is-not-an-applied-migration
