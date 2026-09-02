---
id: 2026-08-21-cj-dropshipping-rpc-style-not-restful
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, cj-dropshipping, api-design, endpoint-audit]
sources:
  - ref: "Archive turn 17 (background-agent HTTP Endpoint Audit of SONNY org repos): CJ-dropshipping's 49 endpoints, all under /cj/v1, confirmed as dominated by RPC-style action paths with zero PUT endpoints anywhere in the repo, and mixed camelCase/kebab-case within a single controller."
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
- confidence: high, produced by a full directory-walk endpoint audit of all 10 controller files (49 endpoints)
- verified: 2026-08-21

# CJ-dropshipping's API is RPC-style action paths, not resource/verb REST — and has zero PUT endpoints anywhere in the repo

## Body
CJ-dropshipping's 49 endpoints (all under a uniform `/cj/v1` prefix) are dominated by RPC-style action paths rather than resource-noun-plus-HTTP-verb REST semantics — e.g. `/products/query`, `/products/addToMyProduct`, `/disputes/getDisputeList`, `/setting/get`, `/webhook/set`, `/shopping/pay/getBalance`. This contrasts with SonnyBackEndRepo in the same org, which is mostly resource-noun based. Consistent with this RPC-style pattern, the repo has no PUT method anywhere at all — every update-style action is modeled as a POST or PATCH RPC call instead of a REST PUT to a resource path. Paths also mix camelCase and kebab-case within the same controller (`ShoppingController` uses both styles in one file). This is a repo-wide convention choice rather than an accident of one controller, and matters for anyone designing a shared API gateway or client library across the org.

## Links
- relates-to, 2026-08-21-sonny-org-no-shared-api-prefix-convention.md, cross-repo convention inconsistency this repo contributes to.
