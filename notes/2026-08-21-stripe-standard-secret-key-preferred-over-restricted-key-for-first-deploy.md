---
id: 2026-08-21-stripe-standard-secret-key-preferred-over-restricted-key-for-first-deploy
type: decision
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, stripe, api-keys, security, deploy]
sources:
  - ref: "Archive turns 400-401: the operator pastes Stripe's Restricted-key permission builder (0 of 29 categories selected), and the agent recommends 'use the plain Standard secret key ... Restricted keys are a nice hardening step later ... ~8 resources ... missing one causes confusing failures ... use the Standard secret key now'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [400, 401]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# For a backend that creates customers, subscriptions, invoices and prices, use Stripe's Standard secret key for initial deploy rather than a Restricted key
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: medium — this was the agent's stated recommendation and the path the operator followed, but it is a pragmatic operational tradeoff rather than an independently verified security analysis
- verified: 2026-08-21
## Body
When the operator was confronted with Stripe's Restricted-key permission builder (29 resource categories, none pre-selected) while trying to get a secret key for the backend, the recommendation given was to use the plain Standard secret key instead, because the backend's billing config explicitly rejects restricted (`rk_`) and publishable (`pk_`) key prefixes anyway, and correctly scoping a restricted key would require selecting roughly 8 specific resources (Customers, Subscriptions, Subscription Items, Invoices, Products, Prices, Payment Methods, Setup Intents) where missing even one causes confusing runtime failures. The explicit tradeoff stated: use the Standard key to get deployed and working now, and tighten to a properly-scoped Restricted key later once everything is confirmed working — treating security hardening as a follow-up rather than a blocker for the first deploy.
## Links
- related, 2026-08-21-backend-stripe-env-vars-are-singular-not-what-env-example-claimed.md, the env-var contract this key gets loaded into
