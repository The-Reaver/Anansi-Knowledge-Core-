---
id: 2026-08-07-agent-routing-formulas-elo-trueskill-bandit
type: spec
status: ratified
source: "Google Drive inbox capture, source chat not recorded in original note (source status: pinned Anansi note, answering whether proven formulas exist beyond Wilson); mined from candidates/2026-08-25/2026-08-07-quality-and-performance-formulas.md"
project: fleet
tags: [formulas, elo, trueskill, bandit, ucb1, thompson-sampling, routing]
---

# Agent/strategy routing formulas beyond Wilson: Elo/TrueSkill for head-to-head skill rating, UCB1/Thompson-sampling multi-armed bandit to route work to better performers while still exploring

## Body

Elo / TrueSkill: skill rating for head-to-head approaches. Multi-armed bandit (UCB1 or Thompson sampling): route more work to better performers while still exploring; UCB1 picks the arm maximizing mean_i + sqrt(2*ln(total)/pulls_i). Agent reliability = its kappa against the human validator over time. (The Wilson score interval and the SPRT/Glicko-2 leveling math are already recorded separately — see legacy-formulas-recovered-gap-closed; this note covers the routing formulas this document adds beyond Wilson.)

## Links

- relates: 2026-08-07-legacy-formulas-recovered-gap-closed
