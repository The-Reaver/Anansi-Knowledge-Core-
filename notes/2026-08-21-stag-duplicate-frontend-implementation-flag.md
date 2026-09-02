---
id: 2026-08-21-stag-duplicate-frontend-implementation-flag
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, meta_agent, validator, frontend, code-duplication, false-positive]
sources:
  - ref: "Archive turns 304-627 show a duplicate-implementation validator check initially false-positiving on legitimate backend router/schema layering, then being rescoped to frontend/components|lib|hooks only and re-verified clean."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [304, 627]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent narrated tuning the check after it produced false positives, then verified it ran clean
- verified: 2026-08-21

# STAG's duplicate-implementation validator check is scoped to frontend components/lib/hooks to avoid false-positiving on legitimate backend router/schema/service layering

## Body
While reconciling the frontend, the agent discovered two entirely parallel, competing implementations of the same dashboard product had been generated across different STAG tasks: a complete "World B" dashboard under `app/dashboard/` using `components/dashboard/*`, `lib/auth/roles`, `lib/api/billing`, `lib/api/toggles`; and a fragmentary "World A" duplicating billing and team management via thinner parallel modules (`lib/roles`, a generic `lib/api.ts` client, `components/team/*`) at different routes (`/billing`, `/settings/team`). This kind of duplication had not been caught by anything in the validator. The agent added a same-basename duplicate-file check, but its first version fired on the backend too, flagging intentional FastAPI layering like `routers/accounts.py` next to `schemas/accounts.py` as if they were duplicates — a false positive, since separate router/schema/service files sharing a resource name is the correct pattern there. The check was rescoped to only compare same-basename files within `frontend/components/`, `frontend/lib/`, and `frontend/hooks/`, which is where the real duplication in this project actually lived, and re-verified clean. Lesson for anyone writing duplicate-detection or drift-detection lint rules over LLM-generated codebases: the same structural pattern (same file basename appearing in multiple places) can be a bug in one layer of the stack and the intended design in another; scope the rule to where the failure mode actually occurs rather than applying it project-wide.

## Links
- related, 2026-08-21-two-dashboard-implementations-consolidation-decision.md, this validator check exists to catch the exact duplication that decision describes fixing
