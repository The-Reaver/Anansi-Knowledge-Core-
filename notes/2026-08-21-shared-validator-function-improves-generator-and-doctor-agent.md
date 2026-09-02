---
id: 2026-08-21-shared-validator-function-improves-generator-and-doctor-agent
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, meta_agent, architecture, code-reuse, leverage-point]
sources:
  - ref: "Archive turns 448-459: 'the Doc agent (project_doctor.py) calls run_validator -> _validate_and_fix_task, so hardening that one shared function improves both the generator and the Doc agent at once' (turn 448), confirmed by reading the Doc agent's code at turn 459 ('run_validator (line 144) calls the exact function I hardened')"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [448, 459]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Because STAG's Doc/diagnostic agent calls the same shared validator function as the generator, hardening that one function improves both agents at once
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the agent confirmed by reading the Doc agent's code that its `run_validator`/`diagnose` phase calls the exact `_validate_and_fix_task` function that was hardened this session
- verified: 2026-08-21
## Body
STAG's Doc agent (`project_doctor.py`) calls `run_validator`, which in turn calls the same `_validate_and_fix_task` function the STAG generator runs after every task. This shared-function architecture means any check added to `_validate_and_fix_task` — such as the three new checks (env parity, frontend tsc gate, DB reference integrity) added during this session — is automatically inherited by both the generator's post-task validation and the Doc agent's `diagnose` phase, with no separate implementation needed for the second consumer. The general lesson for building a fleet of related agents: when two agents perform overlapping validation duties, concentrating the check logic in one shared function is the highest-leverage place to add hardening, since a single edit improves every caller.
## Links
- related, 2026-08-21-three-validator-checks-added-env-parity-tsc-gate-db-integrity.md, the concrete checks added that benefited from this shared architecture
