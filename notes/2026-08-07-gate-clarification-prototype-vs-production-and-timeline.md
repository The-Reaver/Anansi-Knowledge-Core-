---
id: 2026-08-07-gate-clarification-prototype-vs-production-and-timeline
type: finding
status: ratified
source: "Cowork session 2026-08-07; operator noted the in-person interview happens about a week after the app is tried, with nothing deployed and no domain yet. Clarifies the Build Readiness Gate does not block trials. (source status: active)"
project: cippe
tags: [build-readiness-gate, prototype, production, timeline, cippe, interview]
supersedes: []
superseded_by: null
---

# Gate clarification, prototypes are not gated, only production builds; CIPP/E interview timeline

## Body

## Clarification (no contradiction with the gate)
- The Build Readiness Gate only fires when a project folder carries a READY_TO_BUILD marker. Prototypes and trials carry no marker, so the gate stays out of the way. The marker (and a green gate) is added only for the real production build.
- Therefore prototype-first, interview-after is the intended path, not a violation. The trial she tries is a learning artifact; the gate governs the production build that follows the interview.

## CIPP/E timeline (operator-set)
1. She tries an early version (prototype). Nothing deployed, no domain yet.
2. About a week after she has tried it, the operator runs the in-person interview (Elijah protocol + Brain Trust routing).
3. Requirements lock (Elijah + operator), AJ certifies.
4. Celestina tech-stack decision from the requirements.
5. Mark READY_TO_BUILD + green gate -> production build on Antigravity.
6. Buy the domain, deploy private for her.

## Practical note
- The Lovable prototype is at its pre-redesign state and the workspace is out of credits. The trial she tries will most likely be the first Antigravity build, or a refreshed Lovable version if credits are added. Either stays unmarked (ungated).

## Links

- clarifies: 2026-08-07-build-readiness-gate-and-anti-skip-mandate
- relates-to: 2026-08-07-elijah-interview-protocol-cippe, 2026-08-07-brain-trust-interview-routing-cippe
