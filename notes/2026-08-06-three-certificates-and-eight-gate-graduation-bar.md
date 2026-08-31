---
id: 2026-08-06-three-certificates-and-eight-gate-graduation-bar
type: spec
status: ratified
source: "Cowork session 2026-08-06, operator on phone; defined the certification bar that flips an agent from school to cleared (source status: active); mined from candidates/2026-08-25/2026-08-06-graduation-bar-and-breakers-gauntlet-design.md"
project: fleet
tags: [certification, graduation-bar, gates, aj]
supersedes: []
superseded_by: null
---

# Three certificates (Foundation/Architecture/Builder) and the eight-gate graduation bar an agent must clear on every gate

## Body

Certified Foundation (low-level skills proven), Certified Architecture (system-design skills proven), Certified Builder (whole-app skills proven, cleared to build complex apps for clients). An agent earns a certificate only when every gate is a yes: (1) Coverage — every required skill for that level is at the required grade on the 1-9 scale; (2) Proof on file — every skill has a real passing test or real output, reproducible to the same result; (3) The math check — once enough attempts exist, Wilson lower bound, Glicko rating minus two deviations above the level cutoff, and SPRT all agree it is real, not luck; (4) Independent audit — AJ reviews the artifacts, never the agent's words, and signs off; (5) Survives the Breakers — the Red Team attacks a real sample with the dirtiest tactics, any break is a fail, fix and re-attack, only a clean run passes; (6) Provenance stamp — certified-by model X, date Y, curriculum version Z, so the bar is reproducible; (7) Human sign-off for the top level — for Certified Builder, the operator gives the final green light; (8) Not forever — a certificate expires and must be re-earned on a cadence, same idea as the 90-day source-decay rule.

## Links

- relates: 2026-08-06-breakers-gauntlet-four-breaker-types-and-rules
- relates: 2026-08-06-model-tier-per-adlc-stage
