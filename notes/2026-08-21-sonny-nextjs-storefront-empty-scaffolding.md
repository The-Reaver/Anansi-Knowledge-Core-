---
id: 2026-08-21-sonny-nextjs-storefront-empty-scaffolding
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, sonny-nextjs, storefront, scaffolding, endpoint-audit]
sources:
  - ref: "Archive turn 17 (background-agent HTTP Endpoint Audit): git ls-files on sonny-nextjs shows only 4 tracked files (README.md, empty .env.local, next.config.js, package.json), with no app/ or pages/ directory checked in, confirming zero implemented endpoints as of the audit."
    reliability: high
    origin: "STAG session, 2026-08-12, \"Shop Online New York repo\" (backfilled from historical transcript fa904087, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-fa904087.jsonl
  turns: [17, 17]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

- class: confirmed
- confidence: high, confirmed via git ls-files showing the entire tracked tree is 4 files
- verified: 2026-08-21

# sonny-nextjs (the SONNY storefront repo) has zero implemented API routes as of 2026-08-12 — it is pre-implementation scaffolding

## Body
The `sonny-nextjs` repo, which is meant to be the customer-facing storefront for the SONNY/ShopOnlineNewYork org, contains zero endpoints as of the 2026-08-12 audit. `git ls-files` on the cloned repo confirms its entire tracked tree is only 4 files: `README.md`, an empty `.env.local`, `next.config.js`, and `package.json` (under a `Sonny/` subfolder) — there is no `app/` or `pages/` directory checked in at all. The README describes an intended structure including `app/api/webhooks/stripe/` for payment webhooks, and `package.json` lists `next-auth`, `stripe`, and `prisma` as dependencies, but none of that code exists yet in this clone/branch. This means there is currently no client-side webhook handling (e.g. Stripe) or storefront-to-backend proxy layer to audit, and any assumption that the storefront is functional or even started should be checked against this before being relied on.

## Links
- relates-to, 2026-08-21-sonny-admin-dashboard-fake-persistence-layer.md, sibling repo finding from the same audit.
