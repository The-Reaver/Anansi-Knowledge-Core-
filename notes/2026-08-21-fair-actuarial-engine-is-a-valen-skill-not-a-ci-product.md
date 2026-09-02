---
id: 2026-08-21-actuarial-engine-is-valen-skill
type: decision
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [valen, cybersecurity, actuarial, fair, compliance-intelligence, scope]
sources:
  - ref: "Reconciliation turn ruling re-home to Valen, followed by the relocation-status turn: 'Relocation NOT done (files still in CI tree, no Valen home, no log entry)...mapped coupling (api/app.py, App.tsx, v4/engine.py); pinned status into MSG-050.'"
    reliability: high
    origin: "2026-08-21 Amadeus fleet audit / CI reconcile session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl
  turns: [25, 27]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The FAIR Monte Carlo cyber-risk engine is a Valen agent skill, not a Compliance Intelligence product version
- id: 2026-08-21-actuarial-engine-is-valen-skill
- type: decision
- status: ratified
- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- ratification: RATIFIED (same-session, operator-directed + doc-grounded)
- class: confirmed
- source: 2026-08-21 Amadeus fleet audit + CI reconciliation chat
- confidence: high — operator stated intent; CI docs confirm CI is non-actuarial
- verified: 2026-08-21
- tags: valen, cybersecurity, actuarial, fair, compliance-intelligence, scope
## Body
REVIEW: high-impact
The FAIR/Beta-PERT Monte Carlo engine (shared/actuarial_engine.py, v4/engine.py, loss-exceedance UI) was meant to be a skill for the cybersecurity agent Valen (like the UI library was a skill for Amaya), not part of the compliance product. Disposition: relocate it out of the CI tree into a Valen skill, keep the code, unwire the three CI couplings (api/app.py, frontend-vite/src/App.tsx, v4/engine.py), and record it under Valen. CI stays heuristic.
## Links
- depends-on, ci-three-version-compliance-suite.md, CI identity ruling
- source: raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl lines 1-35
