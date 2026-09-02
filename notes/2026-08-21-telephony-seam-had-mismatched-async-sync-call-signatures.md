---
id: 2026-08-21-telephony-seam-had-mismatched-async-sync-call-signatures
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, project-brief-step0, telephony, mypy, latent-bug, twilio]
sources:
  - ref: "Archive turns 211 and 261 independently spot the async/sync signature drift (turn 211: the voice webhook calls resolve_number_route(To) awaited against a sync signature; turn 261: log_event and resolve_number_route are both sync but the webhook's calls await both); turn 306 shows the mypy-isolated-to-touched-files methodology that surfaced it; turns 313/315 show the fix committed as 14454f0."
    reliability: high
    origin: "STAG session, 2026-07-17, \"Project brief step 0 deployment handoff\" (backfilled from historical transcript db88cef4, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-17-backfill-db88cef4.jsonl
  turns: [211, 315]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, confirmed against the real function signatures and fixed with a gate-verified commit
- verified: 2026-08-21

# The pre-existing telephony seam called two sync functions with await and wrong argument order, a latent bug only mypy on the specific file surfaced

## Body
While wiring Tool 1 (Missed-Call Text-Back)'s webhook, reading the actual signatures of `resolve_number_route()` and `log_event()` in `project_brief_step0_resolved`'s backend -- both synchronous functions -- against how the pre-existing `/twilio/voice` webhook and `inbound_routing.py` actually called them (with `await`, and in `inbound_routing.py`'s case, `supabase` passed positionally where the function expects it as the `client=` keyword) revealed both call sites were broken: they would raise `TypeError` or misbehave the moment that code path actually ran.

This had gone undetected because the telephony path was "latent, unreached" per the project's own handoff -- no live Twilio number was exercising it yet. It surfaced only when mypy (the project's Check 15 type gate) was run scoped to the specific file being touched; it was invisible in an aggregate ~57-error mypy run across the whole backend, because that run mixed the real bug in with a large volume of pre-existing, unrelated type-noise errors from other latent subsystems (permissions/entitlements).

Both sites were fixed in this session: the `/twilio/voice` webhook was corrected as part of the Tool 1 rebuild, and `inbound_routing.py`'s three broken `log_event()` calls were fixed as a small, separate, atomic commit, verified mypy-clean and import-clean afterward.

Lesson: running a type gate against an entire legacy codebase can bury a real, high-value finding under a wall of pre-existing noise. Isolating the gate to just the file(s) actually being touched or reasoned about is what makes a genuine latent bug visible.
