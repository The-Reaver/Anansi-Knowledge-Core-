---
id: 2026-08-21-response-model-required-fields-crash-unused-data
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [pydantic, response-model, api-design, backend]
sources:
  - ref: "Archive turns 344-353: a pydantic ValidationError on a proration summary model (required amount_due_cents/period_start/period_end fields, but only invoice_id populated on a legitimate no-invoice code path), fixed by making the derived fields optional/tolerant."
    reliability: high
    origin: "STAG session, 2026-07-15, \"Railway frontend deployment\" (backfilled from historical transcript 23d1d7fe, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl
  turns: [344, 353]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high, reproduced the exact pydantic ValidationError live and fixed it
- verified: 2026-08-21

# A response model's required fields must be satisfiable by every code path that returns it, not just the happy path

## Body
A pydantic response sub-model (a proration summary) declared required fields — an amount-due figure and a billing-period start and end — that the code constructing it only ever populated with an invoice id. One legitimate code path (reactivating a tool with no new invoice to bill) has no data for those fields at all, so every call through that path raised a pydantic `ValidationError` and surfaced to the client as an opaque 500, even though the frontend never actually reads the proration sub-object in its response handling. The durable pattern: a response model's required fields must be satisfiable by every code path that returns that model, not only the one that was tested. When a derived or informational field isn't consumed downstream, making it optional is the pragmatic fix — while still populating real data on it where that's cheaply available — rather than forcing every producer to fabricate values just to satisfy the schema.

## Links
- relates, _archived-base-platform-2026-08-12/origin-s6-subscribe-endpoint-three-layer-drift.md, a companion internal-backend-drift bug from the same billing subsystem, on a different endpoint (toggle, not subscribe).
