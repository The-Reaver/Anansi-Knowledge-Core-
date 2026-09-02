---
id: 2026-08-21-pydantic-settings-extra-forbid-crashes-import-from-unrelated-cwd
type: finding
status: ratified
ratified: |-
  2026-08-21 — ratified by explicit operator instruction ("ratify the 92 that hold up"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification.
project: fleet
tags: [geo_platform, pydantic, config, robustness, fastapi]
sources:
  - ref: |-
      Archive line 631: "Important real finding surfaced: importing the app from a directory that has an unrelated .env (like the stag root) crashes -- Settings() forbids extra inputs, so a .env with ANTHROPIC_API_KEY blows up... this is a genuine config robustness bug. Let me fix it (ignore extras) and verify from multiple CWDs."
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [631, 631]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# GEO Platform's backend could not be imported from any directory whose .env had keys the app's Settings class didn't declare, because Pydantic's default extra="forbid" rejects unknown fields

- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, fixed a wrong source date/session label (was misattributed to the "A2 provisioning environment gates" session; corrected to the "GEO Day 1-2 schema/auth build" session the events actually occurred in). This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-22, "GEO Day 1-2 schema/auth build" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: high — reproduced directly (import crashed from the stag repo root, which has its own .env with ANTHROPIC_API_KEY), fixed, and guarded with a regression test
- verified: 2026-08-21
- REVIEW: high-impact

## Body

`projects/geo_platform`'s backend `Settings()` class used Pydantic's default `extra="forbid"` behavior. This meant the app could not even be imported (let alone run) if invoked from a working directory whose `.env` file contained any key not explicitly declared on `Settings` — for example, running from the stag repo root, whose `.env` carries `ANTHROPIC_API_KEY` for unrelated tooling, crashed the import entirely with a validation error. This surfaced while running the gate battery's throwaway-copy check, which happened to execute from a different CWD than the project's own root.

Fix applied: set `extra="ignore"` on the Settings model config, so unrelated `.env` keys from other projects sharing the same machine no longer break import. A regression test (`test_config_robustness`, part of `tests/test_auth_and_schema.py`) now asserts the app imports cleanly from multiple CWDs. This is a durable environment-robustness requirement for any FastAPI/Pydantic-settings-based service that might be invoked or tested from outside its own project root.

## Links
- surfaced-by, 2026-08-21-run-gate-battery-against-throwaway-copy-not-live-tree.md, found while running the throwaway-copy gate-battery check from a different CWD.
