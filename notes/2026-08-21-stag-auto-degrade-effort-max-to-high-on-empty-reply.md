---
id: 2026-08-21-stag-auto-degrade-effort-max-to-high-on-empty-reply
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [meta_agent, effort, adaptive-thinking, resilience, stag-build]
sources:
  - ref: "Turns 65-90: turn 65 shows the WinError 10054 network-drop diagnosis and the decision to switch to non-streaming plus add connection-drop retries; turns 86/90 show the effort=max-then-auto-retry-at-high fix being wired through and compile-verified."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [65, 90]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# meta_agent.py now auto-retries a call at effort="high" when effort="max" returns no usable text
- id: 2026-08-21-stag-auto-degrade-effort-max-to-high-on-empty-reply
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, code change made and compile-verified in this session; not yet proven across many future builds
- verified: 2026-08-21
- tags: meta_agent, effort, adaptive-thinking, resilience, stag-build
- REVIEW: high-impact

## Body
To fix the empty-plan failure caused by effort="max" thinking consuming the whole token budget on large calls, meta_agent.py was changed so every call still tries `effort="max"` first (honoring the locked model policy of maximum reasoning depth), but if that attempt returns no usable answer text, the same call is automatically retried once at `effort="high"` — still deep reasoning, but leaving enough token headroom to actually write the answer. The build stage was separately reworked to generate one file at a time as a plain code block (rather than asking for an entire task's files as one JSON blob), specifically at `effort="high"` rather than `max`, since writing a single file doesn't need max-effort reasoning and max was the exact setting that caused empty output. Max effort was kept for the interview and planning stages where the deepest reasoning matters most. The wrapper also gained network-level resilience: connection drops (WinError 10054, seen mid-run) are now caught and retried, and calls switched from streaming to non-streaming (the SDK's own retry logic covers non-streaming failures, and streamed connections were the ones a network blip or antivirus/proxy inspection kept breaking).

## Links
- extends, 2026-08-21-effort-max-thinking-can-starve-visible-output.md, this is the fix built in response to that failure.
