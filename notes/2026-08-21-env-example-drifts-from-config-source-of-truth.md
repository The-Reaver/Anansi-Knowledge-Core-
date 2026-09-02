---
id: 2026-08-21-env-example-drifts-from-config-source-of-truth
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, env-config, dotenv, drift, deploy]
sources:
  - ref: "Archive turns 415-421: the agent discovers .env.example lists STRIPE_TEST_SECRET_KEY/STRIPE_MODE/STRIPE_BASE_PLAN_PRICE_ID while app/config.py and app/billing/config.py actually read STRIPE_SECRET_KEY and STRIPE_BASE_PRICE_ID, and states 'the source of truth is app/config.py, not the example'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [415, 421]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The stag-platform backend's .env.example template had drifted from the config module that actually reads environment variables, misleading the operator mid-deploy
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the specific mismatched variable names are directly confirmed against app/config.py and app/billing/config.py as read in-session. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly confirmed by reading app/config.py and app/billing/config.py, and the mismatch is what caused the operator to chase the wrong Stripe variable names during Step 3 of the deploy
- verified: 2026-08-21
## Body
For the STAG-generated `project_brief_step0_resolved` backend, `.env.example` documented Stripe variables `STRIPE_TEST_SECRET_KEY`, `STRIPE_MODE`, and `STRIPE_BASE_PLAN_PRICE_ID`, but the real code (`app/config.py` and `app/billing/config.py`) actually reads `STRIPE_SECRET_KEY` (singular, validated to start with `sk_test_`/`sk_live_`) and `STRIPE_BASE_PRICE_ID` (validated to start with `price_`) — there is no `STRIPE_MODE` split and the publishable key is never read by the backend at all. This drift sent the operator hunting for a Stripe publishable key and the wrong variable names during a live deploy walkthrough before the agent caught it by reading the actual config module. The general lesson: an `.env.example` template should be treated as a derived artifact validated against the config module, not a hand-maintained document trusted at face value, because it can silently fall out of sync with the code that actually consumes it.
REVIEW: high-impact
## Links
- related, 2026-08-21-backend-stripe-env-vars-are-singular-not-what-env-example-claimed.md, the specific corrected variable names found by this investigation
- related, 2026-08-21-three-validator-checks-added-env-parity-tsc-gate-db-integrity.md, the automated check added this session to catch this class of drift going forward
