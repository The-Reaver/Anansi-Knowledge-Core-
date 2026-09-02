---
id: 2026-08-27-a-committed-migration-is-not-an-applied-migration
type: lesson
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [migrations, supabase, deployment, drift, production-config, geo]
sources:
  - ref: "GEO Suite production audit, 2026-08-27: `vendor_credentials_table`, `content_pages_add_terms_type` and `content_pages_add_contact_type` all existed in supabase/migrations/ and had never been run against live project lhzxmvjwqllmnqecfxpm; all three applied via the Supabase MCP that session"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [19, 20]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A migration committed to the repo is not an applied migration: three separate correct migrations sat unrun against production for days

## Body
Three separate, correct, reviewed migration files sat in `supabase/migrations/` for days
having never been executed against the live database. The consequences were live and silent:

- `vendor_credentials_table` -- the table the entire vendor-keys feature reads and writes simply
  did not exist in production, so the feature was dead on arrival despite shipping green.
- `content_pages_add_terms_type` and `content_pages_add_contact_type` -- both widen
  `content_pages.page_type`'s CHECK constraint. Terms and Contact pages had been **failing to
  save in production ever since they were built**, and no one knew.

The failure mode is that writing a migration and applying a migration feel like one act and are
two. Nothing in the commit, the test suite, or the deploy pipeline distinguishes "this file
exists" from "this DDL has run." A repo with a perfect migrations directory and a database that
has never seen it looks identical, from inside the repo, to one that is fully in sync.

What to do differently: after writing a migration, verify it is applied -- query the live schema
for the object it creates, or list the applied migrations on the platform -- and treat that
verification as part of shipping, not as a follow-up. When auditing an unfamiliar deployment,
diff the migrations directory against the platform's applied-migrations list *first*; it is cheap
and, in this case, it would have found three real production defects in one query.

## Links
- instance-of: 2026-08-27-green-unit-suite-does-not-detect-production-config-drift
- relates-to: notes/2026-08-21-jobs-table-column-drift-two-competing-migrations.md
- relates-to: notes/origin-class-c-db-schema-drift.md
