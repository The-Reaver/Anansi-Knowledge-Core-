---
id: 2026-08-21-myuserserviceimpl-god-object-bypasses-owning-services
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, sonnybackendrepo, coupling-cohesion, god-object, data-integrity, account-deletion]
sources:
  - ref: "Archive turn 41 (background-agent Coupling/Cohesion audit of SonnyBackEndRepo's service layer): confirms MyUserServiceImpl at 397 LOC / 12 injected dependencies (10 repositories plus PasswordEncoder and EmailService), and its leaveAccount() method manually cascading deletes directly across 8 unrelated repositories, bypassing the owning domain services' own business rules."
    reliability: high
    origin: "STAG session, 2026-08-12, \"Shop Online New York repo\" (backfilled from historical transcript fa904087, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-fa904087.jsonl
  turns: [41, 41]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, produced by a full-file read of all 27 service-layer classes in SonnyBackEndRepo by a background agent
- verified: 2026-08-21
- REVIEW: high-impact

# SonnyBackEndRepo's MyUserServiceImpl is a god-object whose account-deletion path bypasses the business rules of 8 other domain services

## Body
`MyUserServiceImpl` in SonnyBackEndRepo is 397 lines long and injects 12 dependencies (10 repositories plus `PasswordEncoder` and `EmailService`) — the largest fan-in of any service class in the codebase — and owns registration, login, password reset/OTP, email verification, and account deletion. Its `leaveAccount()` method manually cascades deletes directly across 8 unrelated repositories (refunds, returns, recently-viewed, recommendations, saved products, support tickets, disputes, coupon claims) instead of calling the domain services that already own each of those entities (`RefundService`, `SupportService`, `RecentlyViewedService`, etc.). Because it reaches the repositories directly rather than going through the owning service, any validation or business rule those services enforce (e.g., "can't delete a support ticket mid-review") is silently bypassed when a user deletes their account. The proposed fix from the audit is to extract account-deletion orchestration into a separate `AccountDeletionService` that calls the owning domain services, and keep `MyUserServiceImpl` scoped to auth/credentials only.

## Links
- relates-to, 2026-08-21-sonnybackend-three-incompatible-url-versioning-schemes.md, same repo, same audit session.
