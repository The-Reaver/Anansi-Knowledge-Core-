---
id: 2026-08-21-sonny-admin-dashboard-fake-persistence-layer
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [sonny, shoponlinenewyork, sonny-admin-dashboard, persistence, technical-debt, prisma]
sources:
  - ref: "Archive turn 35 (direct main-thread read of lib/db.ts) and turn 45 (coupling/cohesion audit synthesis): confirm a single 243-line lib/db.ts backs all four dashboard entities via Node's fs/promises (a JSON-file-on-disk store), despite the project's own package.json listing prisma as a dependency."
    reliability: high
    origin: "STAG session, 2026-08-12, \"Shop Online New York repo\" (backfilled from historical transcript fa904087, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-fa904087.jsonl
  turns: [35, 45]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, confirmed by direct read of lib/db.ts and package.json in the sonny-admin-dashboard repo
- verified: 2026-08-21
- REVIEW: high-impact

# sonny-admin-dashboard's data layer writes to the filesystem via fs/promises instead of the Prisma ORM its own package.json declares

## Body
`sonny-admin-dashboard` (the Next.js App Router admin dashboard in the SONNY/ShopOnlineNewYork org) has no service or repository layer at all — every one of its 5 API route files (admin, inventory, orders, vendors) imports from a single 243-line `lib/db.ts` that backs all four unrelated entities. That file uses Node's `fs/promises` to read/write what is effectively a JSON-file-on-disk store, not a real database, even though the project's own `package.json` lists `prisma` (and other production-DB dependencies) as a dependency. In other words, the persistence layer this dashboard's routes actually call at runtime is fake/local-file-based despite the project's declared intent to use Prisma-backed storage — a real gap between what the dependency manifest promises and what the code does, discovered only by reading the actual route handlers rather than trusting package.json.

## Links
- relates-to, 2026-08-21-sonnybackend-three-incompatible-url-versioning-schemes.md, same audit session, sibling repo.
