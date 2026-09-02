---
id: 2026-08-21-hardening-agent-code-is-free-running-it-costs-credits
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, meta-agent, cost, credits, operations]
sources:
  - ref: "Archive turns 480-483 establish the cost-model distinction (editing code/services in-session is free; only running meta_agent.py spends the operator's Anthropic credits), and turns 571-573 show it acted on directly when the operator had no credits left and continued hardening work regardless."
    reliability: high
    origin: "STAG session, 2026-07-15, \"Railway frontend deployment\" (backfilled from historical transcript 23d1d7fe, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl
  turns: [480, 573]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, this distinction was worked out explicitly with the operator mid-session and acted on (agent hardening continued after account credits ran out)
- verified: 2026-08-21
- REVIEW: high-impact

# Editing the Stag meta-agent's own code or an already-deployed project costs nothing on the Anthropic account; only running the meta-agent to generate a new project spends credits

## Body
There are two separate, separately-billed activities that are easy to confuse. The first is an interactive coding session that edits the Stag meta-agent's own source code and directly operates its already-deployed services — this runs on the assistant's own session, not the operator's Anthropic API key. The second is actually running the Stag meta-agent (`meta_agent.py`) to generate a brand-new project — this calls the model using the operator's own Anthropic API key and consumes their account credits. The practical consequence, confirmed directly in this session: running out of Anthropic account credits does not block hardening the Stag agent's validator or generation logic, fixing bugs in an already-deployed platform, or any other direct code or service work done in an interactive session — it only blocks running the generator to build something new. An operator who believes they are "locked out" because credits ran out should first be asked which of the two activities they actually want to do, rather than assumed to be blocked on both.

## Links
