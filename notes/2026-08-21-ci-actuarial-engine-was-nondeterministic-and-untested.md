---
id: 2026-08-21-actuarial-engine-nondeterministic-untested
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [actuarial, determinism, testing, audit, valen]
sources:
  - ref: "Amadeus-hat window audit turn: 'Found CI actuarial engine non-deterministic (unseeded np.random) + untested -> MUST-FIX; wrote AMADEUS_AUDIT_HAT_CI + MSG-049.'"
    reliability: high
    origin: "2026-08-21 Amadeus fleet audit / CI reconcile session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl
  turns: [23, 23]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The CI actuarial engine shipped non-deterministic (unseeded RNG) and untested
- id: 2026-08-21-actuarial-engine-nondeterministic-untested
- type: finding
- status: ratified
- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- ratification: RATIFIED (same-session, verified by code grep)
- class: confirmed
- source: 2026-08-21 Amadeus fleet audit + CI reconciliation chat
- confidence: high — grep confirmed no seed anywhere; no test references the engine
- verified: 2026-08-21
- tags: actuarial, determinism, testing, audit, valen
## Body
shared/actuarial_engine.py calls np.random.beta and np.random.poisson with no seed, so identical inputs yield different risk numbers each run, contradicting the "deterministic engine" claim. No test exercises it (only v4/engine.py consumes it). Before any underwriter-facing use it must be seeded (np.random.default_rng(seed) threaded through run_monte_carlo and _beta_pert) and covered by a determinism + percentile/LEC test. Until then label outputs "preliminary — not for underwriting."
## Links
- supports, actuarial-engine-is-valen-skill.md, fix is part of re-homing
- source: raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl lines 1-35
