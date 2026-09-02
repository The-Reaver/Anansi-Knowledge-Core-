---
id: 2026-08-21-sonny-admin-dashboard-id-in-body-vs-id-in-path
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, sonny-admin-dashboard, api-design, endpoint-audit, technical-debt]
sources:
  - ref: "Archive turn 17 (background-agent HTTP Endpoint Audit): sonny-admin-dashboard's orders resource uses a dynamic path segment for GET but an id-in-body convention for PUT, manually re-parses the URL pathname instead of using Next.js's {params} argument, and is missing POST/DELETE entirely."
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
- confidence: high, confirmed by direct read of all 5 route.ts files in the repo
- verified: 2026-08-21

# sonny-admin-dashboard mixes id-in-URL-path and id-in-JSON-body conventions for the same resource type

## Body
In `sonny-admin-dashboard` (Next.js App Router), `orders` supports `GET /api/orders/{id}` via a true dynamic route segment, but `PUT /api/orders` updates a specific order by passing `id` inside the JSON request body instead of using the same `/api/orders/{id}` path — so the read-by-id and update-by-id operations for the *same resource* don't use the same addressing convention. The other three resources (`admin`, `inventory`, `vendors`) are at least internally consistent: all of them take `id` in the JSON body for both PUT and DELETE, and none of them use a dynamic path segment at all. Separately, `app/api/orders/[id]/route.ts`'s GET handler manually re-parses `id` out of `request.url`'s pathname instead of using Next.js's standard `{ params }` route-handler argument — the only Next.js-convention violation found in this repo. Also, `orders` is missing POST (create) and DELETE entirely, breaking the CRUD symmetry the other three resources have.

## Links
- relates-to, 2026-08-21-sonny-admin-dashboard-fake-persistence-layer.md, same repo, same audit.
