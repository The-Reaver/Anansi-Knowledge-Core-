---
id: 2026-08-21-effort-max-thinking-can-starve-visible-output
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [claude-api, effort, adaptive-thinking, meta_agent, truncation, reliability]
sources:
  - ref: "Turns 74-131: turns 74/82-83 show diagnosis of a fully empty raw reply at effort=max on the plan stage; turns 127/131 show a second, related failure where the build stage's full-task-as-one-JSON-blob approach truncated at max effort even after raising max_tokens."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [74, 131]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Setting effort="max" on a large structured-output call can let hidden thinking consume the entire token budget and return zero visible text
- id: 2026-08-21-effort-max-thinking-can-starve-visible-output
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, reproduced twice in this session (empty plan reply, then a truncated one) and the root cause was confirmed by reading the raw (empty) API reply
- verified: 2026-08-21
- tags: claude-api, effort, adaptive-thinking, meta_agent, truncation, reliability
- REVIEW: high-impact

## Body
When a STAG-style meta-agent (here, meta_agent.py) calls the API with `effort="max"` and adaptive thinking enabled for a large structured task (in this case, generating a full multi-section build plan), the model can spend the entire token ceiling on hidden thinking and emit no answer text at all — the raw reply comes back completely empty, not merely truncated. Small calls (like a single interview question) survive because they need little thinking; large calls (a full plan, a big JSON payload) are where the budget gets consumed first. This happened twice in one build before the cause was isolated: first a "did not return a parseable plan" failure with an empty raw reply, then (after raising the token ceiling) a related failure where the file-generation stage tried to emit an entire task's files as one JSON blob and the JSON got truncated at max effort. Raising `max_tokens` alone was not sufficient — the effort level itself needed handling. This is the same underlying failure mode (effort=max thinking starving the visible answer on large calls) that later independently showed up in the GEO dry-run's empty ERD (data-model.md rendered "(none captured)" while a smaller call in the same stage succeeded) — a different codebase hitting the identical mechanism eleven days later.

## Links
- caused-by, 2026-08-21-opus-4-8-adaptive-thinking-replaces-budget-tokens.md, this is the failure mode that locking both models to effort=max exposed.
- extends, 2026-08-21-stag-auto-degrade-effort-max-to-high-on-empty-reply.md, the mitigation built for meta_agent.py in this session.
- related, 2026-07-18-geo-dry-run-g1-empty-erd-truncation.md, the same effort=max-starves-output mechanism recurring independently in the GEO pipeline's largest structured call.
