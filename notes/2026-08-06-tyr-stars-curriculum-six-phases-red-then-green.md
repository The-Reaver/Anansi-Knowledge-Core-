---
id: 2026-08-06-tyr-stars-curriculum-six-phases-red-then-green
type: spec
status: ratified
source: "Cowork session 2026-08-06, operator on phone; Brain Trust ruled to design TYR's curriculum next (source status: active); mined from candidates/2026-08-25/2026-08-06-tyr-curriculum-lead-breaker.md"
project: fleet
tags: [tyr, curriculum, stars, red-then-green, breaker]
---

# TYR's STARS curriculum: six phases from audit discipline through security/scale/chaos breaking to the gauntlet as a reusable tool, each proven via red-then-green on seeded targets

## Body

Proof discipline: a build with a planted flaw is the red, the fixed version the green; TYR levels up only when it reliably finds the planted flaw and confirms the fix holds. Phase 1, audit discipline: read only the artifacts, never the builder's explanation; reproduce a claimed result independently. Phase 2, correctness breaking: bad and edge-case inputs, timing and concurrency attacks. Phase 3, security breaking (core): injection including prompt injection, login and permission bypass, leaked secrets and PII hunting. Phase 4, scale and chaos breaking: flood to failure, kill parts mid-task to hunt for lost or corrupted data. Phase 5, day-zero and supply chain: flag known-vulnerable dependencies, red-team a real GEO Suite slice end to end. Phase 6, the gauntlet as a tool: turn the attacks into a rerunnable gauntlet the fleet can invoke on any build. Strong models, different AI families, for security judgment. Score the six skill areas 1-9 now; graduate to the leveling math later; log every attempt from day one.

## Links

- extends: 2026-08-06-tyr-lead-breaker-and-security-auditor-approved
- relates: 2026-08-06-tyr-never-certifies-itself-aj-plus-second-breaker-do
