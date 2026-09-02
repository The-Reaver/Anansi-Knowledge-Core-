---
id: 2026-08-21-geo-platform-rls-owner-policies-only-cover-3-of-18-tables
type: finding
status: ratified
ratified: |-
  2026-08-21 — ratified by explicit operator instruction ("ratify the 92 that hold up"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification.
project: fleet
tags: [geo_platform, rls, supabase, security, schema, gap]
sources:
  - ref: |-
      Archive line 637: the agent states "Let me do a final integrity check on the real project and map the RLS policy coverage for the report". Archive line 655 (final summary): "RLS owner policies exist only for users/clients/sites; the other 15 client-scoped tables are RLS-on-but-deny-all. Safe, but days 3-8 must add owner policies and verify them on a live Postgres. I didn't write unverifiable SQL (no Postgres here)."
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [637, 655]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# As of GEO Platform Day 1-2, row-level-security owner policies exist only for the users/clients/sites tables; the other ~15 client-scoped tables are RLS-enabled but deny-all

- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, spot-checked against archive line 655 and confirmed the 3-of-18-tables RLS coverage figure and safe-by-default framing. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-22, "GEO Day 1-2 schema/auth build" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: high — the agent mapped RLS policy coverage directly against the schema as part of finalizing the build report
- verified: 2026-08-21
- REVIEW: high-impact

## Body

At the end of GEO Platform Day 1-2 (schema + auth build), the agent mapped actual row-level-security policy coverage against the full schema. Owner-scoped RLS policies exist only for `users`, `clients`, and `sites`. The remaining roughly 15 client-scoped tables have RLS turned on but no owner policy defined, meaning they default to deny-all rather than being open or misconfigured — a safe-by-default state, not a live vulnerability, but incomplete.

This was deliberately left unfixed rather than papered over: the agent noted it could not write or verify additional RLS policy SQL against a real Postgres instance in this environment (no local Postgres was available, and the session's own test suite could only validate migrations that had a `GEO_TEST_DATABASE_URL` configured). The gap was handed off explicitly in `projects/geo_platform/HANDOFF.md` as a must-do for the days 3-8 GEO build work, to be completed and verified against a live Postgres instance, not assumed correct from schema review alone.

## Links
- co-occurs, 2026-08-21-background-engine-build-report-overclaimed-artifacts-that-didnt-exist.md, both surfaced in the same GEO Day 1-2 close-out pass that prioritized verified truth over convenient claims.
