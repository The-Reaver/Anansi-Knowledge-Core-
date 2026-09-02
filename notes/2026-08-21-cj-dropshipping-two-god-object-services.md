---
id: 2026-08-21-cj-dropshipping-two-god-object-services
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, cj-dropshipping, coupling-cohesion, god-object, technical-debt]
sources:
  - ref: "Archive turn 39 (background-agent Coupling/Cohesion audit of CJ-dropshipping): confirms CJShoppingService (270 LOC, 16 methods, orders/payments/shipping-docs) and CJProductService (338 LOC, 14 methods, catalog/inventory/sourcing) each bundle 3-4 unrelated sub-domains, with recommended service splits given."
    reliability: high
    origin: "STAG session, 2026-08-12, \"Shop Online New York repo\" (backfilled from historical transcript fa904087, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-fa904087.jsonl
  turns: [39, 39]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, produced by a full-file read of all 10 service classes and 10 controllers in CJ-dropshipping by a background agent
- verified: 2026-08-21

# CJ-dropshipping's CJShoppingService and CJProductService are god-objects, each bundling 3-4 unrelated sub-domains into one class

## Body
In the CJ-dropshipping repo (SONNY org's Java/Spring dropshipping integration service), `CJShoppingService` (270 LOC, 16 public methods) mixes three distinct bounded contexts with different callers and change reasons: order lifecycle (create/list/confirm/cancel/change-warehouse), payments (balance/pay), and shipping-document upload (waybill info, POD picture edits). `CJProductService` (338 LOC, 14 public methods, the largest file in the service layer by LOC) bundles catalog browsing, variant lookup, inventory/stock (three near-identical methods differing only by lookup key: vid/sku/pid), and sourcing. Unlike SonnyBackEndRepo's god-object (`MyUserServiceImpl`, which has a genuine high fan-in of 12 injected dependencies), neither CJ-dropshipping service injects more than 2 dependencies — the problem here is "too many verbs under one noun" rather than excessive fan-in. Recommended fix: split `CJShoppingService` into `CJOrderService`/`CJPaymentService`/`CJShippingDocumentService`, and split `CJProductService` into `CJProductCatalogService`/`CJInventoryService`/`CJSourcingService`.

## Links
- relates-to, 2026-08-21-myuserserviceimpl-god-object-bypasses-owning-services.md, sibling god-object finding from the same coupling/cohesion audit, different repo.
