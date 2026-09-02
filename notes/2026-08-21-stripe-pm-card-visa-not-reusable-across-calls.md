---
id: 2026-08-21-stripe-pm-card-visa-not-reusable-across-calls
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stripe, testing, payment-method, gotcha]
sources:
  - ref: "Archive turns 242-245: running create_base_subscription against live Stripe test mode with pm_card_visa across an attach-then-set-default sequence produced a 'not attached' error because each reference to the magic token resolves to a fresh cloned PaymentMethod; minting one concrete PaymentMethod first fixed it."
    reliability: high
    origin: "STAG session, 2026-07-15, \"Railway frontend deployment\" (backfilled from historical transcript 23d1d7fe, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl
  turns: [242, 245]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high, reproduced directly and confirmed the fix by minting a concrete payment method instead
- verified: 2026-08-21

# Stripe's pm_card_visa magic test token cannot be reused across two API calls; each reference clones a fresh, unattached payment method

## Body
Stripe's magic test payment-method token `pm_card_visa` cannot be reused across two separate API calls in the same test script — for example attaching it to a customer, then setting it as that customer's default payment method — because each reference to the token resolves to a freshly cloned `PaymentMethod` object. The second call ends up referencing a payment method the customer was never actually attached to, producing a "not attached" error that looks exactly like a real bug in an attach-then-default code path. This is purely a test-fixture quirk: a real Stripe.js-produced payment method is a concrete, stable `pm_...` id, so the identical two-step attach-then-default backend code works correctly for real browser-submitted cards. Anyone writing a local reproduction script against Stripe test mode should mint one concrete PaymentMethod object first (via a raw create call) rather than reusing the magic token across multiple calls.

## Links
- relates, 2026-08-21-stripe-payment-method-id-flow-with-error-if-incomplete.md, the same billing rewrite this reproduction script was verifying.
