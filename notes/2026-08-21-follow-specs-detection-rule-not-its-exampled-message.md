---
id: 2026-08-21-follow-specs-detection-rule-not-its-exampled-message
type: decision
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [meta_agent, spec-interpretation, sprint-a2, pragmatic-decision]
sources:
  - ref: |-
      Archive line 42: operator says "do what is best for us please". Archive line 43: the agent resolves to keep the Resend branch, reasoning that spec section 4.1's detection rule "explicitly names both providers", only the example message was Stripe-only, and dropping Resend "would leave a real S11-class seam" that fails silently.
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [42, 43]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# When a spec's detection rule names two cases but its example message only shows one, the pragmatic call is to implement what the rule says, not just what the example shows

- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- class: confirmed
- source: STAG session, 2026-07-18, "A2 provisioning environment gates" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: medium — a specific, reasoned instance of a general judgment call, not independently re-verified across other specs
- verified: 2026-08-21

## Body

Spec A2's environment-alignment gate (S11) detection rule explicitly named both providers — "STRIPE_WEBHOOK_SECRET or RESEND_WEBHOOK_SECRET" and "STRIPE_SECRET_KEY or RESEND_API_KEY" — but the spec's example alignment-flag message text only showed Stripe wording. The agent initially flagged this as an open question ("keep the Resend branch, or drop it to match the spec literally?"), and the operator responded "do what is best for us." The resolution: keep the Resend branch. Reasoning — the spec's detection rule, not its example message, is the actual specification of scope; "emit a single alignment flag" reads as one flag per matched provider pair, not one flag for the whole gate; and dropping Resend would leave a real silent-failure gap (a Resend webhook secret misaligned with its API key fails exactly as silently as the Stripe case), which is the exact class of bug S11 exists to catch. The decision was also backed with a dedicated test rather than left unverified, since it went beyond what the spec's four required tests covered.

General rule for future spec-ambiguity calls when a spec's detection/logic rule and its illustrative example disagree in scope: follow the rule, treat the example as illustrative not exhaustive, and add test coverage for the extra branch taken.

## Links
