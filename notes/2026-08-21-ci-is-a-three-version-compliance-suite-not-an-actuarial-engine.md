---
id: 2026-08-21-ci-three-version-compliance-suite
type: decision
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [compliance-intelligence, scope, hbot, ada, hipaa, valen]
sources:
  - ref: "Operator: 'CI was meant for ADA/privacy compliance; cyber-risk engine was a Valen skill; three versions; reconcile.' Reply: 'confirmed CI=3-version compliance suite (V1 HBOT, V2 privacy/ADA, V3 enterprise/complete); README says not actuarial; v4 FAIR engine is drift; ruled re-home to Valen.'"
    reliability: high
    origin: "2026-08-21 Amadeus fleet audit / CI reconcile session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl
  turns: [24, 25]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Compliance Intelligence is a three-version compliance suite, deliberately heuristic and not actuarial
- id: 2026-08-21-ci-three-version-compliance-suite
- type: decision
- status: ratified
- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- ratification: RATIFIED (same-session, grounded in CI README/VISION)
- class: confirmed
- source: 2026-08-21 Amadeus fleet audit + CI reconciliation chat
- confidence: high — README states versions and "Heuristic enums; not actuarial" verbatim
- verified: 2026-08-21
- tags: compliance-intelligence, scope, hbot, ada, hipaa, valen
## Body
REVIEW: high-impact
Compliance Intelligence is defined by its README/VISION as three separately-testable versions: V1 HBOT (FDA/FTC/UHMS/NFPA 99), V2 privacy/ADA (HIPAA cues, ADA/WCAG, privacy), V3 enterprise/complete (SOC2/ISO27001/CIPP-E/state; "Run full v3" composes V1+V2+enterprise). Scoring is heuristic impact/likelihood enums, explicitly "not actuarial." The FAIR Monte Carlo cyber-risk engine added as v4 was scope drift and is not a product version.
## Links
- corrects, valen-cyber-risk-skill.md, the actuarial engine belongs to Valen not CI
- source: raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl lines 1-35
