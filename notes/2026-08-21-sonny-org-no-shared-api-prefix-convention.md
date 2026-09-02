---
id: 2026-08-21-sonny-org-no-shared-api-prefix-convention
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, api-design, endpoint-audit, cross-repo]
sources:
  - ref: "Archive turn 17 (background-agent HTTP Endpoint Audit, cross-repo section): confirms SonnyBackEndRepo (/api with pockets of /api/v1 and a broken v1/api), CJ-dropshipping (uniform /cj/v1), and sonny-admin-dashboard (plain /api, no version segment) each use a different, mutually incompatible URL prefix/versioning scheme."
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
- confidence: high, produced by a full cross-repo endpoint audit (192 endpoints across 4 repos)
- verified: 2026-08-21

# Across the SONNY org's 3 API-serving repos, each one uses a completely different URL prefix/versioning scheme

## Body
Across the three SONNY/ShopOnlineNewYork repos that actually serve HTTP endpoints (`sonny-nextjs`, the intended storefront, serves zero — see separate note), each one picked its own, mutually incompatible URL prefix/versioning convention with no org-wide standard: SonnyBackEndRepo mostly uses `/api` with pockets of `/api/v1` and a broken `v1/api` (see separate note on that repo's internal inconsistency), CJ-dropshipping uses `/cj/v1` uniformly for all 49 endpoints, and sonny-admin-dashboard uses plain `/api` with no version segment at all. This means any API gateway, reverse proxy routing, or shared client SDK built for the org has to special-case each backend individually rather than relying on a shared prefix or versioning rule — there is currently no cross-repo API contract to build against.

## Links
- relates-to, 2026-08-21-sonnybackend-three-incompatible-url-versioning-schemes.md, the same inconsistency problem but scoped inside one repo instead of across the org.
- relates-to, 2026-08-21-sonny-nextjs-storefront-empty-scaffolding.md, the repo excluded from this count because it has no implemented endpoints.
