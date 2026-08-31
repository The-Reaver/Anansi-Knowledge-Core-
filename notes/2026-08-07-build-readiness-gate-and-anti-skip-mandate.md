---
id: 2026-08-07-build-readiness-gate-and-anti-skip-mandate
type: ruling
status: ratified
source: "Cowork session 2026-08-07; operator asked how to prevent skipping protocol (interview, tech-stack decision) before building. This is the durable control. (source status: active)"
project: fleet
tags: [adlc, gate, mandate, definition-of-ready, governance, prevention, read-first, verify]
---

# Build Readiness Gate (Definition of Ready) and the no-build-without-a-green-gate mandate

## Body

## The mandate (add to READ_FIRST.md and STAG_MANDATES_AND_PRIORITIES.md)
- "No build without a green Build Readiness Gate. A build brief is a draft until the gate is green. Antigravity and every agent never build until the gate passes. Step zero before any build or handoff is checking the gate; if red, run the missing gate first."

## Build Readiness Gate (Definition of Ready) — must be green before any build
Owner in brackets; each item signed off, not self-approved.
- [ ] Interview complete (Elijah leads; members weigh in by expertise). Real requirements gathered from the operator and, in person and confidentially, the intended user. [Elijah]
- [ ] Requirements locked: an agreed, written requirements set derived from the interview. [Elijah + operator]
- [ ] Tech-stack decision made and gated: real alternatives, clear criteria, a recommendation, a rationale, and a gate. No inherited or assumed stack. [Celestina]
- [ ] Design blueprint / tokens ratified for this build. [Orlok / accessibility + Celestina]
- [ ] Fleet validation passed (adversarial check by the Breakers where relevant). [TYR / Breakers]
- [ ] Gate certified. [AJ]
- Only when all boxes are checked does a build brief become a handoff and a build may start.

## Gate owners (no self-approval)
- Elijah: interview gate. Celestina: architecture and tech-stack gate. Orlok: accessibility/neurodivergent design gate. TYR/Breakers: adversarial validation. AJ: certifies the whole gate.

## Pre-build tripwire (behavioral rule, applies to Claude and all agents)
- Any time someone proposes "build", "hand to Antigravity", or writes a build brief, step zero is checking the gate. State the gate status before proposing a build. If red, route the missing gate first. Never assume a stack.

## Optional automation (make the machine enforce it)
- Add a verify.py check: a project cannot be marked "ready to build" unless a green gate artifact exists in its Development Queue folder. Blocks the shortcut mechanically.

## Definition of Ready vs Definition of Done
- Definition of Ready (this gate): gates passed before build.
- Definition of Done (existing acceptance criteria): met after build.
- A project must pass both, in order.

## Links

- extends: 2026-08-07-adlc-protocol-correction-interview-and-stack-gates
- relates-to: 2026-08-07-fleet-interview-and-audit-governance
- relates-to: STAG_MANDATES_AND_PRIORITIES, READ_FIRST.md
