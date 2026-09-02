---
id: 2026-08-21-tool-toggle-billing-proration-one-month-minimum-rule
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [small-business-tools, billing, stripe, proration, product-decision, abuse-prevention]
sources:
  - ref: "Turns 106-107 verbatim: turn 106 poses the toggle-billing question, turn 107 locks the exact immediate-prorated-charge-with-one-month-minimum and no-credit-on-toggle-off rule, matching the note's activation_date/min_charge_until field names and the $300-tool-for-two-days abuse example precisely"
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [106, 107]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high, explicitly locked by the operator during the Step 0 build interview, implemented in code, and verified line-by-line against the seed's wording in a later audit pass in the same session
- verified: 2026-08-21
- REVIEW: high-impact

# Tool toggle-on charges an immediate prorated invoice with a one-month minimum per activation; toggle-off issues no credit and the tool stays billed until the later of period end or that minimum

## Body
When a client toggles a tool on, the platform charges a prorated amount immediately for the remainder of the billing cycle (Stripe `create_prorations` with an immediate invoice) and activates the entitlement at once, but every activation carries a one-month minimum charge: toggling the $300/mo Database Reactivation Engine on for two days still bills a full month, closing the two-day-toggle abuse path the operator flagged as a real money leak. Toggling a tool off does not remove the line item immediately and issues no prorated credit; the tool stays active and billed until the later of the current period end or one month from activation, then the item is set not to renew. This was implemented via `activation_date` and `min_charge_until` fields stamped on the entitlement record (not left to Stripe's native proration alone, since Stripe doesn't enforce a minimum-charge rule by itself), and it was called out as the single riskiest task in the build because it moves real client money on custom rules the billing provider doesn't natively guarantee.

## Links
- extends, 2026-08-21-small-business-tools-per-tool-line-item-billing-locked.md, this is the enforcement rule for that pricing model.
