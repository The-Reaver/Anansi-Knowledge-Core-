---
id: 2026-08-21-operator-flag-postgres-only-no-signup-path
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (absolute 'no signup path can ever grant operator status' claim narrowed to exclude a single hardcoded bootstrap-seed email auto-promoted via a SECURITY DEFINER trigger). Operator retains veto per Mandate 1."
project: fleet
tags: [auth, rls, supabase, operator, access-control, security]
sources:
  - ref: "Archive turns 100-116: signup creates a tenant owner only, and a database trigger blocks the anon/authenticated/service_role roles from ever setting is_operator; a prior handoff document's claim of signup-triggered auto-promotion was checked against the code and found false as of 2026-07-13. A later migration (found during 2026-08-25 review) narrowly scopes one bootstrap exception; see Body correction."
    reliability: high
    origin: "STAG session, 2026-07-15, \"Railway frontend deployment\" (backfilled from historical transcript 23d1d7fe, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl
  turns: [100, 116]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, verified directly against the schema trigger and signup code, then exercised live
- verified: 2026-08-21
- REVIEW: high-impact

# Operator status can only be granted by a direct SQL statement run as postgres, never through signup or any API call

## Body
In this platform's data model, signing up always makes the signer the owner of a brand-new client (tenant) — never a cross-tenant operator — and a database trigger actively blocks the `anon`, `authenticated`, and `service_role` Supabase roles from ever setting `is_operator` on a user row. No signup, invitation, or API call can grant operator status; the only way to promote an account to operator is a manual SQL `UPDATE` run as `postgres` (for example in the Supabase SQL editor), followed by the user logging out and back in so the flag is re-read on the next session. A prior handoff document's claim that a specific email address would be "auto-promoted to operator by migration trigger" was checked against the actual trigger and signup code and found to be false. This is a concrete example of a handoff document drifting from the code it describes, and stands on its own as a durable fact about how operator promotion actually works in this codebase's data model.

**Correction (2026-08-25, Brain Trust + Augustin + AJ review):** The absolute framing above ("no signup, invitation, or API call can grant operator status") is now inaccurate. A later migration (`supabase/migrations/20250101001200_operator_flag_and_seed.sql`, present in `projects/geo_platform`, `Archive/project_brief_step0_resolved`, and `projects/sandbox_training_env`) adds a `SECURITY DEFINER` trigger, `promote_seeded_operator()`, that auto-promotes exactly one hardcoded email the moment a matching `auth.users`/`public.users` row is inserted — a deliberate, narrowly-scoped bootstrap exception, not a general signup-to-operator path. Revised claim: **no signup path grants operator status to an arbitrary account; exactly one hardcoded seed email is auto-promoted via a `SECURITY DEFINER` trigger for bootstrap purposes, and the guard trigger still blocks every other account/role from ever setting `is_operator`.** Augustin additionally found the current backend code's own comment (`operator_guard.py:15-18`) still asserts the old absolute claim, contradicting the migration's trigger within the same codebase — that comment should be corrected alongside this note. The security implications of the trigger itself (is it truly one-shot, is email confirmation enforced) are a separate, still-open item — see `2026-08-25-operator-seed-trigger-security-hardening-needed.md`.

## Links
- relates, _archived-base-platform-2026-08-12/origin-s12-handoff-doc-drifted-from-code.md, another instance of a handoff claim disagreeing with the actual code, from the same session.
