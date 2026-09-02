---
id: 2026-08-21-opus-4-8-adaptive-thinking-replaces-budget-tokens
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — see body correction. Operator retains veto per Mandate 1."
project: fleet
tags: [claude-api, opus-4-8, fable-5, thinking, effort, model-policy, meta_agent]
sources:
  - ref: "Turns 14-30: turn 14 is Cowork's claimed correction (Opus 4.8 rejects budget_tokens, moves to adaptive+effort); turn 30 is this session's own independent check confirming the mechanism against the Claude API reference."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [14, 30]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Opus 4.8 rejects a manual extended-thinking token budget and must use adaptive thinking plus the effort parameter, same as Fable 5
- id: 2026-08-21-opus-4-8-adaptive-thinking-replaces-budget-tokens
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, confirmed directly against the live Claude API reference during the session (not taken on Cowork's word)
- verified: 2026-08-21
- REVIEW: high-impact

## Body
As of this session, sending `thinking: {budget_tokens: N}` to `claude-opus-4-8` returns a 400 error. Opus 4.8 has moved to the same reasoning-control mechanism as `claude-fable-5`: `thinking: {type: "adaptive"}` combined with the `output_config.effort` parameter (values `low`, `medium`, `high`, `xhigh`, `max`). Any STAG-family document or code that still describes a separate manual token budget for Opus (as the Master Build Document's Section 2 did at the time) is stale on that one point, even though it was accurate when written. The fix that preserves the original intent (maximum reasoning depth on every call) is to wire both models to adaptive thinking with `effort="max"`, not to keep trying a `budget_tokens` value on Opus. Pricing at the time was confirmed at $10/$50 per million input/output tokens for Fable 5 and $5/$25 for Opus 4.8, both current as of this session.

**Revision (Brain Trust review, 2026-08-26):** the core mechanism this note describes (budget_tokens rejected, adaptive thinking + output_config.effort required) remains accurate for Opus 4.8, but Opus 4.8 is no longer the current default Opus model — it has since been superseded, and the current default Opus model has materially different thinking defaults (thinking on by default, unlike Opus 4.8/4.7's opt-in effort model). Readers relying on this note for current model-policy behavior should treat it as historically accurate for Opus 4.8 specifically and verify current defaults against the live claude-api reference rather than assuming they still apply to whichever Opus model is current.

## Links
- causes, 2026-08-21-effort-max-thinking-can-starve-visible-output.md, the max-effort setting this correction produced is what later caused empty replies on large calls.
