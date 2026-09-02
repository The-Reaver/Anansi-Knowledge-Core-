---
id: 2026-08-21-stale-facility-hours-data-contradicts-hoursnote-caveat
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [agame-sports, data-integrity, seo, structured-data, real-world-impact]
sources:
  - ref: "Turns 567-580: line 567 is the gap-sweep agent's finding that the site's published Sunday JSON-LD hours contradict the crawl-derived hoursNote caveat that was never rendered anywhere, with the real-world 'parent drives there Sunday and finds it closed' consequence spelled out; line 578 confirms the fix (surfacing hoursNote in the site footer)."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [567, 580]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Published Sunday hours in the site's Google-facing JSON-LD contradicted a captured "actually closed Sundays" caveat that was never wired into any rendered output
- id: 2026-08-21-stale-facility-hours-data-contradicts-hoursnote-caveat
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — confirmed by an adversarial review agent cross-referencing the two data fields against the crawled source and the rendered JSON-LD; the underlying real-world hours were not independently re-verified against the live business (out of scope for the review)
- verified: 2026-08-21
- tags: agame-sports, data-integrity, seo, structured-data, real-world-impact
- REVIEW: high-impact

## Body
The A-Game Sports rebuild's facility data file stored two separate hours-related fields: `facility.hours` (Saturday–Sunday 8am–7pm), which was duplicated into the site's `SportsActivityLocation` JSON-LD structured data shown to Google/Maps on all 95 pages, and a separate `facility.hoursNote` field — captured during the original live-site crawl — stating the facility is actually closed Sundays except for parties and special events. `hoursNote` was never referenced by any rendered component or by the hand-written JSON-LD, so the contradiction between the two fields was invisible in the built site until a gap-sweep review agent cross-referenced them directly. If shipped unfixed, the practical consequence is a real-world harm distinct from a typical UI bug: a customer trusting the business-hours panel Google surfaces from this structured data could drive to the facility on a Sunday expecting it to be open and find it closed. The fix surfaced the caveat visibly (in the site footer) rather than only fixing the JSON-LD, since the JSON-LD schema itself has no clean way to express "closed except for X." General lesson: when crawling live-site facts into structured data fields, a field captured as a caveat/exception (not just the headline value) needs an explicit check that it is actually rendered somewhere — an unused field that was clearly meant to correct another field is a specific, checkable smell.

## Links
- see-also, 2026-08-21-content-schema-fields-silently-dropped-by-template.md, a related pattern of authored facility/content data never reaching any rendered output
