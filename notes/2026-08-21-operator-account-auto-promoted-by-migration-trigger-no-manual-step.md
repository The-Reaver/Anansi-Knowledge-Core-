---
id: 2026-08-21-operator-account-auto-promoted-by-migration-trigger-no-manual-step
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, supabase, operator-role, migration, auto-promotion]
sources:
  - ref: "Archive turn 345: after reading the migration, the agent tells the operator 'You never have to manually make yourself operator. The migration auto-promotes [the operator's email] to operator the moment that account signs up (there's a trigger).'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [345, 345]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The single operator account for stag-platform is granted entirely by a migration trigger keyed to a hardcoded email; no manual SQL or admin flag-flip is needed to bootstrap the admin console
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the migration filename and auto-promotion mechanism are directly confirmed, and the note correctly avoids naming the operator's actual email. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — confirmed by reading the migration (20250101001200_operator_flag_and_seed.sql) before telling the operator they had nothing to do here
- verified: 2026-08-21
## Body
The `project_brief_step0_resolved` migration `20250101001200_operator_flag_and_seed.sql` includes both a guard trigger that blocks the anon/authenticated/service Postgres roles from ever setting a profile's `is_operator` flag directly, and a separate security-definer promote trigger that automatically flips `is_operator` to true the instant a profile row is created for one specific hardcoded operator email address. Because of this, the operator does not need to run any manual SQL, flip any admin flag, or take any special signup path to become the platform's operator — signing up normally in the deployed app with that specific email is sufficient, and the admin console becomes accessible immediately after. This is a durable fact about this specific codebase's bootstrap mechanism, useful for any future session that resumes work on this deploy or needs to reason about how the operator/admin role is granted.
