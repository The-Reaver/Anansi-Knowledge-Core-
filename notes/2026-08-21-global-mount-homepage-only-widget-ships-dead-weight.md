---
id: 2026-08-21-global-mount-homepage-only-widget-ships-dead-weight
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [architecture, performance, component-scoping, agame-sports]
sources:
  - ref: "Turns 379-503: line 379 measures the ~215KB gzipped sitewide dead weight from the homepage-only GuidedTour mounted in the base layout; line 493 confirms the fix (scoping GuidedTour to the homepage only) resolved both the dead-weight and page-destroying-navigation bugs."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [379, 503]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Mounting a homepage-only guided-tour widget globally shipped ~215KB of dead weight sitewide and could destroy in-progress page state
- id: 2026-08-21-global-mount-homepage-only-widget-ships-dead-weight
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — measured directly against the built dist/ output (per-page byte counts, grep across all 95 HTML files) by two independent review agents
- verified: 2026-08-21
- tags: architecture, performance, component-scoping, agame-sports
- REVIEW: high-impact

## Body
A guided-tour modal component (`GuidedTour.astro`) was mounted in the site's shared base layout, so it rendered on all 95 built pages, but 3 of its 5 tour steps targeted DOM element IDs that existed only on the homepage (`index.astro`). On the other 94 pages the component's only reachable behavior was its trigger button doing a full-page `window.location.href` navigation to `/?tour=1`. Measured impact: roughly 7KB of inert JS/markup per non-homepage page (~215KB gzipped sitewide, ~15-20% of some pages' total HTML weight), because the script used Astro's `define:vars`, which forces inline (non-bundled, non-cached) output repeated on every page. Worse, because the trigger was a real page navigation rather than an in-place open, clicking it from any inner page (e.g. mid-way through filling out the contact form) discarded whatever the user had entered, with no confirmation. The fix scoped the actual tour component to the homepage only and replaced the sitewide trigger with a lightweight link. General lesson: a component whose functional behavior is gated on `pathname === '/'` (or similar) is a strong signal it is mounted at the wrong layer — the fix is moving the component down to the page it actually belongs to, not adding more path-branching logic to the global mount.

## Links
- see-also, 2026-08-21-dual-blind-adversarial-review-passes-converge.md, the review process that identified and quantified this
