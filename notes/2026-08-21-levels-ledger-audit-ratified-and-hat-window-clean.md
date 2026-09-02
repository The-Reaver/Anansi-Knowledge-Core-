---
id: 2026-08-21-levels-and-hat-audit-clean
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [leveling, discrimination-harness, audit, governance, anirak, amadeus-hat]
sources:
  - ref: "Ledger audit turn: '8 of 24 leveled skills PROVEN...47/49 fleet tests green; RATIFIED, no revocations' and hat-window audit turn: 'operator-authorized standing order, no governance files edited during window, citation 51/51 green -> PASS.'"
    reliability: high
    origin: "2026-08-21 Amadeus fleet audit / CI reconcile session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl
  turns: [21, 23]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The self-leveling ledger audit ratified all moves with no revocations, and the operator-authorized Amadeus-hat window respected its limits
- id: 2026-08-21-levels-and-hat-audit-clean
- type: finding
- status: ratified
- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- ratification: RATIFIED (same-session, verified by reproduction + file mtimes)
- class: confirmed
- source: 2026-08-21 Amadeus fleet audit + CI reconciliation chat
- confidence: high — 8 leveled skills independently reproduced PROVEN; governance files untouched in window
- verified: 2026-08-21
- tags: leveling, discrimination-harness, audit, governance, anirak, amadeus-hat
## Body
Amadeus independently audited Anirak's machine-gated self-leveling: the discrimination harness mutates the module (never the test), verifies byte-identical restore, and requires red-then-green; 8 of 24 leveled skills were reproduced PROVEN in a sandbox interpreter with RED reasons matching the ledger verbatim; 47/49 fleet tests reproduced green. Verdict: RATIFIED, no revocations. Separately, the "Amadeus-hat" window was operator-authorized by standing order and edited no governance files (FLEET_SOP, AGENTS, operating model, delegated authority all pre-window), and the citation gate reproduced 51/51 green. Follow-up: seven proving tests used bare asserts and should name specific reasons.
## Links
- extends, (existing leveling-protocol notes), records the first audit outcome
- source: raw/2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl lines 1-35
