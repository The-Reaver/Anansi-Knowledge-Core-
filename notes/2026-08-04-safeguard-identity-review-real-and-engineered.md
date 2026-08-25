---
id: 2026-08-04-safeguard-identity-review-real-and-engineered
type: finding
status: ratified
source: this chat, 2026-08-04, direct code review of the SafeGuard Identity Lovable project (source status: active)
project: fleet
tags: [safeguard-identity, lovable, security, build-outcome]
---

# SafeGuard Identity's Verification Core Is Real and Carefully Built, Two Things Are Unconfirmed

## Body

SafeGuard Identity, an identity/age verification product for meeting strangers met online, has a genuinely solid core. Its Stripe identity webhook verifies signatures and fails closed if the secret is missing, deduplicates retried events, and blocks a late event from downgrading an account that already passed. Age is computed server-side from a verified birthdate, never trusted from the client. One shared decision function handles both the real Stripe path and the demo path, so the demo cannot quietly diverge from the real rules over time. Two things were not confirmed in this pass: whether row-level security is actually enforced at the database level (only one small recent migration was read, not the ones defining the policies), and there is no visible data retention or deletion policy for the identity documents and biometric liveness data this product handles.

## Links

- touches: 2026-08-04-agent-foundry-review-ui-shell-no-execution-engine (both came out of the same review pass, requested together)
