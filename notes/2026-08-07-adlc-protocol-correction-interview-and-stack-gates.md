---
id: 2026-08-07-adlc-protocol-correction-interview-and-stack-gates
type: correction
status: ratified
source: "Cowork session 2026-08-07; operator flagged that we skipped protocol by assuming the tech stack and jumping to an Antigravity build brief without Elijah's intuitive interview or a deliberate fleet-run tech-stack decision. (source status: active)"
project: cippe
tags: [adlc, protocol, governance, interview, tech-stack, gate, cippe, correction]
supersedes: []
superseded_by: null
---

# Protocol correction, do not skip the interview and tech-stack gates before building

## Body

## The miss
- The tech stack (FastAPI + HTMX + Postgres/pgvector) was inherited from the older ratified spec and assumed, not deliberately chosen for this build.
- Elijah's intuitive interview was skipped.
- The build brief was produced as if it were a finished handoff; it is only a requirements draft until it passes the protocol.

## The required protocol (run in order before Antigravity builds)
1. Elijah's intuitive interview, fleet-driven. Elijah leads with his questions; members weigh in by expertise (per the interview-and-audit governance note). Gathers real requirements from the operator and, in person and confidentially, from the intended user. Research is not a substitute for her answers.
2. Requirements lock: turn the interview into an agreed requirements set.
3. Tech-stack selection, Celestina-led (architecture). Real alternatives, clear criteria (local-offline, single-container, rich adaptive UI with command palette/inline help/collapsible panels, local RAG, accessibility, maintainability, architect skills), a recommendation, and a gate. Do not assume FastAPI+HTMX; compare honestly and confirm or change.
4. Fleet validation and gates, then finalize the build brief and hand to Antigravity.

## Standing rule reaffirmed
- Do not skip ADLC gates. Interview and requirements before stack; stack before build. The build brief is an input to this process, not the finished handoff.

## Links

- relates-to: 2026-08-07-fleet-interview-and-audit-governance
- relates-to: 2026-08-07-cippe-local-build-brief-for-antigravity
- relates-to: 2026-08-07-cippe-redesign-blueprint-meta-analysis
