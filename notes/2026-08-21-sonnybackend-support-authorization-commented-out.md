---
id: 2026-08-21-sonnybackend-support-authorization-commented-out
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, sonnybackendrepo, security, authorization, support-tickets]
sources:
  - ref: "Archive turn 17 (background-agent HTTP Endpoint Audit, Inconsistencies item 12): confirms SupportController and SupportAdminController both have their class-level @PreAuthorize(...) role-check annotations commented out in source, leaving ticket admin/buyer endpoints without enforced role checks in code."
    reliability: high
    origin: "STAG session, 2026-08-12, \"Shop Online New York repo\" (backfilled from historical transcript fa904087, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-fa904087.jsonl
  turns: [17, 17]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, found by direct source read of the controller classes during a full-file (not sampled) audit
- verified: 2026-08-21
- REVIEW: high-impact

# SonnyBackEndRepo's support-ticket admin and buyer endpoints have their role-authorization checks commented out in code

## Body
In SonnyBackEndRepo, both `SupportController` (buyer-facing support tickets) and `SupportAdminController` (admin-facing support ticket management) have their `@PreAuthorize(...)` class-level role-check annotations commented out in the source code, meaning ticket admin/buyer endpoints currently run in production (or whatever branch was checked) with no enforced Spring Security role checks at the code level — anyone who can reach the endpoint can call it regardless of role. This was surfaced as part of a broader endpoint audit and was not something the operator asked to look for specifically; it needs a security-focused follow-up (check whether the commented-out state is on the deployed branch, and re-enable or fix the underlying auth check) rather than being treated as a stylistic finding.

## Links
- relates-to, 2026-08-21-sonnybackend-three-incompatible-url-versioning-schemes.md, same audit, same repo.
