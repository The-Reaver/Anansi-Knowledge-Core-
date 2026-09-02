---
id: 2026-08-21-backend-stripe-env-vars-are-singular-not-what-env-example-claimed
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, stripe, env-vars, billing-config]
sources:
  - ref: "Archive turns 419-421: the agent reads app/config.py and app/billing/config.py directly and states the definitive Stripe env-var contract — STRIPE_SECRET_KEY (validated to start with sk_test_/sk_live_) and STRIPE_BASE_PRICE_ID (validated to start with price_), no STRIPE_MODE, publishable key never read by the backend"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [419, 421]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The backend reads exactly STRIPE_SECRET_KEY (singular) and STRIPE_BASE_PRICE_ID for the core billing path — no STRIPE_MODE, no _TEST_ variant, and the publishable key isn't read by the backend at all
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the exact env-var contract is directly confirmed against app/config.py and app/billing/config.py as read in-session. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — confirmed by reading app/config.py and app/billing/config.py directly, which validate STRIPE_SECRET_KEY must start with sk_test_/sk_live_ and STRIPE_BASE_PRICE_ID must start with price_
- verified: 2026-08-21
## Body
For `project_brief_step0_resolved`'s backend, the real, code-verified environment-variable contract for Stripe is just two required values: `STRIPE_SECRET_KEY` (singular, not `STRIPE_TEST_SECRET_KEY`; the billing config validates it starts with `sk_test_` or `sk_live_`, so the mode is implied by the key prefix rather than a separate flag) and `STRIPE_BASE_PRICE_ID` (validated to start with `price_`, the id of the recurring $19/mo base subscription price). There is no `STRIPE_MODE` test/live toggle read by the backend, and the Stripe publishable key is never read by the backend at all — it is only used client-side by the (not-yet-fully-wired) card-entry form. This is a durable fact specific to this codebase, useful for anyone resuming or repeating this deploy, and it directly corrects the `.env.example` template, which listed different, non-functional variable names.
REVIEW: high-impact
## Links
- related, 2026-08-21-env-example-drifts-from-config-source-of-truth.md, the template drift that this correct variable list resolves
- related, 2026-08-21-stripe-standard-secret-key-preferred-over-restricted-key-for-first-deploy.md, the related decision on which kind of Stripe key to use
