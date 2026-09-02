---
id: 2026-08-21-positional-hub-convention-nav-data-fragile
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [data-modeling, navigation, breadcrumbs, architecture, agame-sports]
sources:
  - ref: "Turns 365-468: line 370 documents the self-referencing/broken breadcrumb bug on School Break Camps and School Holiday Camps pages caused by the positional entries[0]-as-hub assumption; line 468 confirms the fix (an explicit hub field in navHelpers.ts / sitemap.ts) replacing the positional inference."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [365, 468]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Inferring a nav group's "hub" page from array position (entries[0]) broke breadcrumbs and produced self-referencing links
- id: 2026-08-21-positional-hub-convention-nav-data-fragile
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — confirmed against the built dist/ output by multiple independent review agents across two passes, and fixed/re-verified in the same session
- verified: 2026-08-21
- tags: data-modeling, navigation, breadcrumbs, architecture, agame-sports

## Body
The A-Game Sports rebuild's navigation helpers (`getHub`, `getSiblings`, `getBreadcrumb`) all determined which page was a sitemap group's "hub" (parent) page by taking `group.entries[0]` — the first array element — rather than an explicit field. This worked for most of the 17 nav groups, but 2 groups ("School Break Camps" and "Site-wide / Utility") had no real hub page at all, so their first array entry was actually an ordinary sibling/leaf page. The bug was real and shipped: a "Spring Break Camps" page rendered a sidebar link reading "← Back to School Holiday Camps" (a sibling presented as the parent), and the "School Holiday Camps" page itself — being its own group's `entries[0]` — rendered a "Back to" link pointing at itself, a dead no-op control. Separately, the breadcrumb helper used a URL-prefix test (`href.startsWith(hub.href)`) to decide nesting, which is a different and also-fallible proxy for the same "who is my parent" question, and it disagreed with the hub helper on 21 of 94 pages (e.g. seasonal `/fall-*/` pages whose URL doesn't nest under their sport's hub URL). The fix made `hub` an explicit, nullable field on each sitemap group instead of inferring it positionally. General lesson: when a data structure has more than a couple of exceptions to a positional convention (first-item-is-special, order-implies-meaning), encode the special relationship as its own explicit field — the convention becomes silently wrong exactly where it matters most (the entries that don't fit the common case).

## Links
- see-also, 2026-08-21-dual-blind-adversarial-review-passes-converge.md, the review process that surfaced this as the top root-cause bug
