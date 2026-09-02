---
id: 2026-08-21-content-schema-fields-silently-dropped-by-template
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [content-schema, astro, silent-data-loss, agame-sports]
sources:
  - ref: "Turns 368-566: line 372 confirms InfoTemplate never rendered FactList (dropping the /calendar/ scheduleNote); line 442 confirms HubTemplate's identical gap was latent, not active, data loss; line 566 confirms the fix (FactList wired into all templates) was verified live in the browser."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [368, 566]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A content schema shared across multiple page templates let two of four templates silently drop authored pricing/hours fields with a clean, passing build
- id: 2026-08-21-content-schema-fields-silently-dropped-by-template
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — confirmed against the built dist/ output ("At a Glance" block absent) by two independent review agents, for specific named pages with specific authored content
- verified: 2026-08-21
- tags: content-schema, astro, silent-data-loss, agame-sports
- REVIEW: high-impact

## Body
The A-Game Sports rebuild's Zod content schema allowed every page — regardless of which of 4 page templates it used — to declare `facts`, `ageRange`, `priceNote`, and `scheduleNote` fields. Only one template (`DetailTemplate`, used for program/camp pages) actually rendered these as an "At a Glance" info block. `InfoTemplate` shared the same omission and, unlike the other affected template, had real authored content in these fields that was silently dropped by it. `HubTemplate` had the identical code-level gap — it also never imported or rendered the display component — but the gap was latent at review time: no hub page yet carried content in `facts`/`ageRange`/`priceNote`/`scheduleNote`, so no live content was actually lost through it, even though the same bug would silently drop hub-page content the moment such content is authored. Because the schema validated successfully and the build produced no warning, both templates' gaps were invisible until an adversarial review pass grepped the built HTML for the block. Concretely, three already-live pages lost real content this way: the `/calendar/` page's `scheduleNote` (the facility's actual operating hours) never appeared anywhere on the page; `/specials/`'s `facts` entry for a 15%-off veteran discount was dropped; and `/customized-programs/`'s full 1-on-1-through-4-on-1 `priceNote` rate table was dropped. General lesson: when a content schema is shared across multiple render templates, either every template must render every schema field it accepts, or the schema needs to be scoped per-template (e.g. a discriminated union) — otherwise real authored content can pass validation and a green build while never reaching a live page, with nothing in the toolchain to catch it.

## Links
- see-also, 2026-08-21-stale-facility-hours-data-contradicts-hoursnote-caveat.md, a related case of authored facility data never being wired into any rendered output
