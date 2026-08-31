---
id: 2026-08-06-tyr-curriculum-lead-breaker
type: decision
status: candidate
source: "Cowork session 2026-08-06, operator on phone; Brain Trust ruled to design TYR's curriculum next. TYR is the first agent from Seed, approved as lead Breaker and Security Auditor, reporting to AJ. (source status: active)"
project: fleet
tags: [tyr, curriculum, stars, breaker, security, red-team, aj, certification]
supersedes: []
superseded_by: null
---

# TYR curriculum (STARS), the lead Breaker and Security Auditor

## Body

## Brain Trust verdict
Quorum: Amadeus, Celestina, Elijah, Oluwole, Jasiah, plus Sentinel (security). Unanimous: design TYR's curriculum next. Rationale: real phone-doable progress, readies the first agent to build at the machine, and security is the operator's top worry so it should be ready early. Docx conversion is trivial and can happen anytime.

## TYR role
Lead Breaker and Security Auditor. Independent of the fleet, reports to AJ, runs the Breakers gauntlet. TYR audits others, so TYR never certifies itself; AJ plus a second different Breaker certify TYR.

## TYR curriculum (STARS), skills in order, each proven before the next
Proof discipline: seeded targets. A build with a planted flaw is the red, the fixed version is the green. TYR levels up only when it reliably finds the planted flaw and confirms the fix holds (red-then-green applied to security).

- Phase 1, audit discipline. Read only the artifacts, never the builder's explanation. Reproduce a claimed result independently. Proof: re-run a build's tests and confirm or refute, citing only evidence.
- Phase 2, correctness breaking. Bad and edge-case inputs; timing and concurrency attacks. Proof: force a wrong result and a data race on seeded buggy builds, then confirm the fixes hold.
- Phase 3, security breaking (core). Injection (including prompt injection), login and permission bypass, leaked secrets and PII hunting. Proof: break in on a seeded vulnerable app, then confirm the fix blocks it.
- Phase 4, scale and chaos breaking. Flood to failure; kill parts mid-task to hunt for lost or corrupted data. Proof: topple a fragile seeded target and confirm the hardened version survives.
- Phase 5, day-zero and supply chain. Flag known-vulnerable dependencies; red-team a real GEO Suite slice end to end. Proof: a full attack run with a written break report.
- Phase 6, the gauntlet as a tool. Turn the attacks into a rerunnable gauntlet the fleet can invoke on any build. Proof: it runs on a fixture, breaking the broken and passing the fixed.

## Modeling for TYR
Strong models for security judgment; different AI families, since different attackers find different holes. Certification of TYR is done by AJ plus a second independent Breaker, never by TYR itself.

## Tracker (DREAMS)
Score the six skill areas on the 1-to-9 scale now; graduate to the leveling math later; log every attempt from day one.

## Links

- extends: 2026-08-06-graduation-bar-and-breakers-gauntlet-design
- relates-to: 2026-08-06-cross-agent-stars-dreams-curriculum-design
- relates-to: 2026-08-06-DEFINITIVE-BLUEPRINT
