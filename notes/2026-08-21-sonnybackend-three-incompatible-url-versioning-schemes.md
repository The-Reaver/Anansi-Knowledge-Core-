---
id: 2026-08-21-sonnybackend-three-incompatible-url-versioning-schemes
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, sonnybackendrepo, api-design, endpoint-audit, technical-debt]
sources:
  - ref: "Archive turn 17 (background-agent HTTP Endpoint Audit, Inconsistencies items 1-2): confirms SonnyBackEndRepo's 128 endpoints across 30 controllers mix three incompatible URL prefix/versioning schemes — plain /api, /api/v1, and the support/returns family's reversed v1/api with a missing leading slash."
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
- confidence: high, produced by a full-file (not sampled) directory walk of all 30 controller files, read in full by a background agent
- verified: 2026-08-21

# SonnyBackEndRepo mixes three incompatible URL prefix/versioning schemes in one Spring Boot codebase

## Body
A full endpoint audit of SonnyBackEndRepo (the main Java/Spring Boot backend of the ShopOnlineNewYork/SONNY org, 128 endpoints across 30 controllers) found three incompatible URL prefix/versioning conventions coexisting in the same codebase: the majority of endpoints use plain `/api/{resource}` (products, categories, orders, coupons, buyers, sellers, reviews, policies, etc.), a second group uses `/api/v1/{resource}` (cart, address-book, my-coupons, my-points, recently-viewed, and the `MyOrdersController`'s `/orders`), and a third group — the entire support/returns family (`SupportController`, `SupportAdminController`, `ReturnController`) — declares its base path as `v1/api/support...` with the version and `/api` segments reversed and, worse, missing the leading slash that every other controller in the repo has. There is no shared org-wide or even repo-wide API versioning convention; each controller author appears to have picked a scheme independently. This matters for any future API-gateway, client-SDK-generation, or public-docs work on SONNY, since none of it can assume a uniform path shape.

## Links
- relates-to, 2026-08-21-sonny-org-is-shoponlinenewyork-22-repos.md, org this repo belongs to.
