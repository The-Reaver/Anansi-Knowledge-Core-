---
id: 2026-08-21-dashboard-tool-toggle-requires-explicit-confirm-dialog
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [frontend, ux, billing, toggle, product-spec]
sources:
  - ref: "Archive turns 472-477: an account with an active base subscription but no tool entitlement, traced to an unconfirmed ToggleConfirmDialog rather than a backend bug."
    reliability: high
    origin: "STAG session, 2026-07-15, \"Railway frontend deployment\" (backfilled from historical transcript 23d1d7fe, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl
  turns: [472, 477]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: medium, confirmed by reading the frontend wiring and matching it to a real account's observed state; not independently re-verified after this session
- verified: 2026-08-21

# The dashboard tool toggle is a deliberate two-step confirm, not a broken button — clicking it alone bills and activates nothing

## Body
On this platform's dashboard, clicking a tool's toggle does not by itself activate it — it opens a confirmation dialog showing the exact prorated charge, and only clicking confirm inside that dialog fires the actual toggle-on request that bills the card and activates the entitlement. This is deliberate design, not a bug: during this session a real signed-up account that had a fully working, independently verified backend showed no tool entitlement after the operator "toggled" a tool in the browser, and the cause turned out to be that the confirm dialog had been opened but never confirmed. Anyone debugging "the toggle doesn't seem to do anything" on this dashboard should check whether the confirmation step was actually completed before assuming a backend failure.

## Links
