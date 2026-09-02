---
id: 2026-08-21-cowork-session-claimed-local-delivery-that-never-arrived
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [cowork, disconnect, cross-session-handoff, verification-first]
sources:
  - ref: "Turns 14-30: turn 14 contains Cowork's full message including the 'next to your existing venv and .env' phrasing and its own disclaimer that it had no connection to the local machine; turns 15-20 show the agent inspecting the local filesystem and finding only venv, no .env, no deliverables; turn 30 gives a full side-by-side table confirming every deliverable was absent while Cowork's technical claims were independently confirmed accurate."
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

# A Claude Cowork session reported four deliverables placed in the local stag folder that had never actually been transferred there
- id: 2026-08-21-cowork-session-claimed-local-delivery-that-never-arrived
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, directly verified by inspecting the local filesystem in the same session (stag/ contained only venv, no .env, no deliverables)
- verified: 2026-08-21
- tags: cowork, disconnect, cross-session-handoff, verification-first
- REVIEW: high-impact

## Body
A prior Claude Cowork session sent the operator a message describing four build deliverables (meta_agent.py, playbook.txt, project_brief.txt, a setup guide) as ready to "move into your stag folder, next to your existing venv and .env" and referred to an ".env" as something the operator "already" had. When the operator asked this (separate, local Claude Code) session to confirm that message and act on it, direct inspection of `C:\Users\abadm\stag` found only a `venv` folder — none of the four files existed, and there was no `.env` at all, despite Cowork's message treating it as already present. Cowork's own message had in fact flagged the limitation correctly ("I don't have a connection to C:\Users\abadm\stag from this session, so I built all four deliverables here"), but its phrasing elsewhere ("next to your existing .env") implied a state of the local machine that did not exist. The technical content of Cowork's message (Section 4.4 model/API verification) was independently re-confirmed as accurate; only the claim about local file state was wrong. This is a concrete, verified instance of the general pattern that a remote/cloud agent session's description of local machine state cannot be trusted without independent verification before acting on it, since the remote session has no way to confirm what actually landed on disk.
