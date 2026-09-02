---
id: 2026-08-21-sonnybackend-favorites-duplicated-across-two-controllers
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, sonnybackendrepo, api-design, duplication, endpoint-audit, coupling-cohesion]
sources:
  - ref: "Archive turn 17 (endpoint audit, Inconsistencies item 4: both /api/buyers/favorites and /api/saved-products route trees call the same buyerService methods) combined with turn 41 (coupling/cohesion audit, finding 7: BuyerServiceImp mixes buyer CRUD with saved-products, and SavedProductsRepository has no dedicated owning service)."
    reliability: high
    origin: "STAG session, 2026-08-12, \"Shop Online New York repo\" (backfilled from historical transcript fa904087, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-fa904087.jsonl
  turns: [17, 41]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, found by a full-file directory walk plus service-layer read by a background agent
- verified: 2026-08-21

# SonnyBackEndRepo's favorites/saved-products feature is implemented twice, via two unrelated controllers calling the same underlying service method

## Body
In SonnyBackEndRepo, `GET/POST /api/buyers/favorites` (in `BuyerController`, backed by `BuyerServiceImp`) and `GET /api/saved-products` + `POST /api/saved-products/{productId}` (in a separate `SavedProductsController`) both call the same underlying `buyerService` methods to manage a buyer's saved/favorited products, but are exposed as two unrelated route trees. The coupling/cohesion audit of the same session separately flagged that `BuyerServiceImp` mixes buyer-profile CRUD with this saved-products sub-domain, and that a `SavedProductsRepository` exists with no matching dedicated service — i.e. the controller for saved products presumably calls `BuyerService` today rather than an owning service of its own. The recommended fix is to consolidate into one dedicated `SavedProductsService`/controller pair.

## Links
- relates-to, 2026-08-21-sonnybackend-duplicate-password-change-endpoints.md, same duplicated-route-tree pattern found in the same audit.
- relates-to, 2026-08-21-myuserserviceimpl-god-object-bypasses-owning-services.md, same repo's coupling/cohesion audit.
