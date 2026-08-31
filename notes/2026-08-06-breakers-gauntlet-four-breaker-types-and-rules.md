---
id: 2026-08-06-breakers-gauntlet-four-breaker-types-and-rules
type: spec
status: ratified
source: "Cowork session 2026-08-06, operator on phone; defined the certification bar that flips an agent from school to cleared, folding in the Red Team of Breakers (source status: active); mined from candidates/2026-08-25/2026-08-06-graduation-bar-and-breakers-gauntlet-design.md"
project: fleet
tags: [breakers, red-team, security, correctness, scale, chaos]
supersedes: []
superseded_by: null
---

# The Breakers gauntlet: Security, Correctness, Scale, and Chaos Breakers, independent of the builder and fleet, using different AI families, all must come up empty

## Body

Security Breaker: injections, auth bypass, data leaks, day-zero style exploits. Correctness Breaker: edge cases and weird inputs to force a wrong result. Scale Breaker: floods of users and data to make it fall over. Chaos Breaker: kills parts mid-task (crash, dropped network) to hunt for lost or corrupted data. Rules: independent of the builder and the fleet, attack the real work, log every break, use different AI families so they fail differently. A build passes only when the whole team comes up empty.

## Links

- extends: 2026-08-06-three-certificates-and-eight-gate-graduation-bar
- relates: 2026-08-06-tyr-lead-breaker-and-security-auditor-approved
