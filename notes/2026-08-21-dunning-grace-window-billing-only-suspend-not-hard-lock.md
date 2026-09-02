---
id: 2026-08-21-dunning-grace-window-billing-only-suspend-not-hard-lock
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [small-business-tools, billing, dunning, twilio, product-decision]
sources:
  - ref: "Turns 108-109: turn 108 poses the dunning-window question, turn 109 locks the 7-day grace / billing-only-suspended / 30-day number-hold model with the churn-avoidance reasoning."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [108, 109]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Small Business Tools dunning: 7-day payment-failure grace window, then a billing-only suspended state (not a full account lockout), with the client's dedicated number held 30 days before release
- id: 2026-08-21-dunning-grace-window-billing-only-suspend-not-hard-lock
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, explicitly locked by the operator during the Step 0 build interview and baked into the approved build plan
- verified: 2026-08-21
- tags: small-business-tools, billing, dunning, twilio, product-decision
- REVIEW: high-impact

## Body
When a client's card fails on renewal, the account enters a 7-day grace window driven by Stripe Smart Retries; entitlements stay active during grace and the dashboard shows a billing warning banner. If payment is still failing after 7 days, the account moves to suspended: every tool's entitlement pauses and no data is deleted, but rather than a full lockout the dashboard drops to a billing-only state where the client can still log in, see why they're suspended, and fix their card — the reasoning given was that a hard lockout increases churn and makes recovery harder than a self-serve billing-only screen. Separately, the client's dedicated Twilio number (a real, effectively irreplaceable business phone line) is held for 30 days after suspension or cancellation at the platform's own ~$1.15/mo cost before a scheduled job releases it permanently; reinstating within that 30-day window restores the same number and every tool wired to it. This mirrors the same reasoning as the toggle-off billing rule: protect the client from losing something hard to get back, at a cost the platform can absorb.

## Links
- related, 2026-08-21-dedicated-twilio-number-at-signup-not-lazy.md, the number-lifecycle decision this hold-then-release policy governs.
