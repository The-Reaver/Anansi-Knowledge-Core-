---
id: 2026-08-21-sonnybackend-duplicate-password-change-endpoints
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, sonnybackendrepo, api-design, duplication, endpoint-audit]
sources:
  - ref: "Archive turn 17 (background-agent HTTP Endpoint Audit, Inconsistencies item 3): confirms POST /api/account/change-password (AccountController) and POST /api/auth/change-password (AuthController) both change the same user's password under two separate route trees."
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
- confidence: high, found by a full-file directory walk of all controller files
- verified: 2026-08-21

# SonnyBackEndRepo exposes password-change through two separate, unrelated controllers

## Body
SonnyBackEndRepo has two separate endpoints that both change a user's password under two entirely different route trees: `POST /api/account/change-password` in `AccountController` and `POST /api/auth/change-password` in `AuthController`. This is one of several duplicated-functionality findings from the endpoint audit (the other being favorites/saved-products, captured separately) and signals the codebase grew multiple controllers per concern without a clear single owner for account-related actions. Before any client integration or docs work assumes one canonical password-change endpoint, this duplication needs to be resolved (deprecate one, or document why both exist).

## Links
- relates-to, 2026-08-21-sonnybackend-favorites-duplicated-across-two-controllers.md, same pattern (duplicated route trees for one concern) found in the same audit.
