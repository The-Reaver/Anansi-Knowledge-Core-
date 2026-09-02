---
id: 2026-08-21-multi-tenant-owner-staff-roles-built-in-step-0
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [small-business-tools, multi-tenant, rls, supabase, product-decision]
sources:
  - ref: "Turns 110-111: turn 110 poses the multi-user account model question, turn 111 locks the clients/users/memberships three-table model with owner-vs-staff roles and unlimited seats, including the owner-only money-gating rule."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [110, 111]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Small Business Tools platform builds owner/staff multi-user roles into the schema at Step 0 rather than retrofitting them after the six tools ship
- id: 2026-08-21-multi-tenant-owner-staff-roles-built-in-step-0
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, explicitly locked by the operator during the Step 0 build interview and baked into the approved build plan
- verified: 2026-08-21
- tags: small-business-tools, multi-tenant, rls, supabase, product-decision
- REVIEW: high-impact

## Body
A client business can have multiple team members from Step 0 onward, on the stated reasoning that retrofitting multi-user support after six live tools ship on top of the platform would be far more expensive than building it into the foundation now. The model uses three tables: `clients` (the business account), `users` (Supabase auth identities), and `memberships` (links a user to a client with role `owner` or `staff`). The first signup creates the client and becomes its owner. Only the owner can commit any action that moves money — tool toggles, card updates, inviting or removing members, provisioning/releasing numbers — enforced at both the FastAPI layer and via Supabase row-level security, so an office manager (staff) can operate the dashboard without being able to switch on the $300/mo tool or change the payment method. Seats are unlimited under the flat $19/mo base fee, since metering seats for small-business clients was judged to add billing friction for little gain.

## Links
- related, 2026-08-21-operator-admin-access-shared-auth-with-flag-not-separate-login.md, the parallel decision on how platform-operator (not client) access is modeled on the same auth system.
