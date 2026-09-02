---
id: 2026-08-21-operator-admin-access-shared-auth-with-flag-not-separate-login
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [small-business-tools, supabase, auth, admin, security, product-decision]
sources:
  - ref: "Turns 122-136: turn 122 poses the admin-access-security question, turn 123 locks the is_operator-flag-outside-memberships model with the guarded /admin route, and turn 136 confirms the founder account seeding matches the note's description."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [122, 136]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Small Business Tools operator (founder) admin access reuses the same Supabase auth as clients, gated by a manually-set operator flag, not a separate credential system
- id: 2026-08-21-operator-admin-access-shared-auth-with-flag-not-separate-login
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, explicit design decision made under the operator's "decide and explain" standing instruction, baked into the approved build plan
- verified: 2026-08-21
- tags: small-business-tools, supabase, auth, admin, security, product-decision
- REVIEW: high-impact

## Body
Rather than a separate admin login system apart from client authentication, the platform-operator (founder) admin view logs in through the same Supabase auth clients use, gated by a platform-level `is_operator` flag (or small operators table) that sits outside the client `owner`/`staff` membership roles entirely, so operator power can never mix with a client's own role. The flag is set manually in the database and seeded for the founder account (`abadmorel@gmail.com` in this build); it is never grantable through the normal signup or invitation flow. The reasoning given: running two separate credential systems is more attack surface and more maintenance than the separation actually requires, which is authorization (what an already-authenticated user can do), not a second login path. The guarded `/admin` route requires the operator flag and gets row-level-security read access across all client accounts, while normal client-facing RLS still scopes clients to their own data. Two-factor auth on the operator login was flagged as a pre-live hardening item, not built in Step 0.

## Links
- related, 2026-08-21-multi-tenant-owner-staff-roles-built-in-step-0.md, the client-side role model this operator flag sits deliberately outside of.
