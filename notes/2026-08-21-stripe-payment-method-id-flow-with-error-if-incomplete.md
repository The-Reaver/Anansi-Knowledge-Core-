---
id: 2026-08-21-stripe-payment-method-id-flow-with-error-if-incomplete
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stripe, billing, payment-flow, architecture-decision]
sources:
  - ref: "Archive turns 211-234: two competing billing implementations found (a default_incomplete path requiring separate client confirmation, and a payment_method_id + error_if_incomplete path that was the live/mounted one); the latter was kept because it matched the deployed schema and settled synchronously."
    reliability: high
    origin: "STAG session, 2026-07-15, \"Railway frontend deployment\" (backfilled from historical transcript 23d1d7fe, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl
  turns: [211, 234]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high, implemented and verified live against Stripe test mode end to end
- verified: 2026-08-21
- REVIEW: high-impact

# Billing subscribe was built on Stripe's payment-method-id + error_if_incomplete flow for synchronous activation

## Body
The billing subscribe path was standardized on Stripe's payment-method-id flow: Stripe.js/Elements creates a PaymentMethod client-side so raw card data never reaches the app's own servers, the backend attaches that payment method to the customer as the default, and creates the subscription with `payment_behavior="error_if_incomplete"` — which, given a valid default payment method, settles the first invoice immediately and returns status `active` synchronously in one round trip. This was chosen over a competing implementation that also existed in the codebase, which used `payment_behavior="default_incomplete"` and returned an `incomplete` subscription plus a client secret requiring a separate client-side confirmation step. The payment-method-id flow won because it matched the already-deployed request schema, produced an active subscription synchronously for the golden-path smoke test, and kept the frontend simpler.

Note-writer's outside-knowledge inference (not discussed or verified in the source session): `error_if_incomplete` is not designed to handle 3D Secure / Strong Customer Authentication challenges, which the rejected client-secret/confirmation flow would have supported. If the product later needs SCA-compliant cards (for example EU customers), this trade-off should be re-examined — but the session itself never raised 3DS/SCA, so treat this as a flag for future review rather than a verified finding.

## Links
