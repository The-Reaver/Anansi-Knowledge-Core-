---
id: 2026-08-21-three-validator-checks-added-env-parity-tsc-gate-db-integrity
type: decision
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, meta_agent, validator, env-parity, typescript, db-integrity]
sources:
  - ref: "Archive turns 452-459: the agent implements the three checks and runs the enhanced validator ('The new checks work — and they even surfaced a brand-new latent bug: account_state.py queried account_status_transitions ... the real table is account_state_transitions'), then re-runs after tightening noise and confirms the exact Stripe-var flag at turn 457"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [452, 459]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Three new generation-time checks (env-var parity, a frontend tsc gate, DB table-reference integrity) were added to STAG's shared validator and immediately found two real latent bugs
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the three checks and the newly found phantom-table bug (account_status_transitions vs account_state_transitions) match the session's regression-pass results. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the agent implemented all three, ran them against the live project, and reported concrete before/after results including a newly found phantom-table bug
- verified: 2026-08-21
## Body
On the operator's request for a "full diagnostic report" and "meticulous documentation and implementation" of STAG/Doc-agent improvements, three new checks were added to the shared `_validate_and_fix_task` function used by both the generator and the Doc agent: (8) env parity — AST-parse the config module's settings fields plus regex-scan for `os.environ`/`alias=`/`_require_env` usage to get the real set of environment variables the code reads, then diff against `.env.example`; (9) a frontend type gate that runs `tsc --noEmit` when `node_modules` is present, as the frontend analog of the existing backend `import app.main` boot check; (10) DB reference integrity — every table referenced by `supabase.table("X")` calls or by a migration's `alter`/`create index`/`create policy` statement must be created by some migration in the chain. Run against the already-fixed project as a regression check, the new battery passed on everything already repaired, correctly flagged the still-drifted `.env.example` (missing `STRIPE_SECRET_KEY` and `STRIPE_BASE_PRICE_ID`), and found a brand-new latent bug on its own: `account_state.py` queried a table named `account_status_transitions` that no migration creates (the real table is `account_state_transitions`).
REVIEW: high-impact
## Links
- related, 2026-08-21-shared-validator-function-improves-generator-and-doctor-agent.md, why implementing this once benefits two separate agents
- related, 2026-08-21-contract-drift-single-root-cause.md, the failure pattern these three checks target
