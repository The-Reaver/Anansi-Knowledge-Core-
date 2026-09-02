---
id: 2026-08-21-context-budget-triage-agent-improvements-vs-mechanical-work
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — added a scope caveat to Body noting this is generic session-management guidance rather than a sharp technical finding. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, session-management, context-budget, handoff, meta-agent-improvement]
sources:
  - ref: "Archive turns 616-627 show the operator asking whether to finish remaining work now or hand off to a fresh session, and the agent banking two STAG validator checks into meta_agent.py in-session while writing a dedicated HANDOFF_NEXT.md for the mechanical frontend TypeScript work."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [616, 627]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent stated this triage rule explicitly and executed on it (STAG validator improvements done in-session, frontend TypeScript grind handed off via a written handoff file)
- verified: 2026-08-21

# When context budget runs low mid-session, do agent/tooling improvements that need the accumulated context now, and hand off mechanical/resumable work to a fresh chat

## Body
Near the end of a long session (spanning tasks 8 through the start of a frontend TypeScript reconciliation), the operator flagged that the agent's context window was shrinking and asked whether the remaining work — finishing frontend error fixes, and further STAG agent improvements — should be completed now or handed off to a new chat. The agent's stated triage rule: work that depends on nuance accumulated during the current session and would be expensive for a fresh session to reconstruct (in this case, the specific failure modes discovered — API contract drift, duplicate parallel implementations, imagined APIs, deploy-config traps) should be done now, while the current context still holds that nuance. Work that is mechanical and fully resumable from a written artifact (in this case, the remaining TypeScript error list plus the established fix patterns) should be handed off to a fresh chat with a full context budget, since a fresh session can execute a well-specified mechanical task at least as well and with more room. Concretely, the agent banked two new validator checks (deploy-config sanity, duplicate-frontend-implementation) into `meta_agent.py` in the current session, then wrote a dedicated, tightly-scoped `HANDOFF_NEXT.md` (deliberately separate from the large existing `HANDOFF.md`, to avoid spending remaining context editing a big file) capturing exact frontend state, the real-vs-imagined API names, and the runtime caveat that a type-clean build still needs a live-backend integration pass — sufficient for a new chat to resume without needing this session's history.

This triage rule is fairly generic session-management guidance rather than a sharp technical finding; it generalizes across projects, but it carries less specific technical weight than the STAG validator findings it accompanies.
