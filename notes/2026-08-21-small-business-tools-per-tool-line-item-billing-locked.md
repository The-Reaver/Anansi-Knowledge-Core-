---
id: 2026-08-21-small-business-tools-per-tool-line-item-billing-locked
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [small-business-tools, billing, stripe, pricing, product-decision]
sources:
  - ref: "Turns 95-101: turn 95 states the per-tool-line-item model, turn 97 adds the six tool prices, turn 100 is the operator's rewrite instruction, and turn 101 adds the $19 base fee resolving the signup gap while keeping the six per-tool prices."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [95, 101]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Small Business Tools platform bills each of the six tools as its own Stripe subscription line item, added on toggle-on and removed on toggle-off, not one flat subscription
- id: 2026-08-21-small-business-tools-per-tool-line-item-billing-locked
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, explicitly locked by the operator during the Step 0 build interview and baked into the approved build plan
- verified: 2026-08-21
- tags: small-business-tools, billing, stripe, pricing, product-decision
- REVIEW: high-impact

## Body
For the Small Business Tools platform (the "STAG" small-business SaaS build, six tools: Missed-Call Text-Back, Review Engine, Booking Recovery Bot, Database Reactivation Engine, Payment Recovery Engine, AI Voice Receptionist), the operator locked the pricing model as per-tool line items rather than a single flat platform price with toggles as mere feature switches. Each tool a client turns on adds its own Stripe subscription line item at its own monthly price ($49, $29, $39, $300, $200, $249 respectively); turning it off removes that line. This left a signup gap (what does a brand-new client with zero tools on actually subscribe to), which was resolved separately by adding a flat $19/mo base platform fee that every client pays from signup, with the per-tool lines stacked on top of it (this replaced an initially-proposed card-on-file-only signup with no base fee).

## Links
- causes, 2026-08-21-tool-toggle-billing-proration-one-month-minimum-rule.md, the billing engine rule that enforces this per-tool model without letting clients dodge charges.
