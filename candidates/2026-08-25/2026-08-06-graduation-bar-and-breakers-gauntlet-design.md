---
id: 2026-08-06-graduation-bar-and-breakers-gauntlet-design
type: decision
status: candidate
source: "Cowork session 2026-08-06, operator on phone; continued the fleet design by defining the certification bar that flips an agent from school to cleared, folding in the Red Team of Breakers, and proposing TYR's role. (source status: active)"
project: fleet
tags: [certification, graduation-bar, breakers, red-team, security, aj, tyr, curriculum]
---

# The graduation bar (certification checklist) and the Breakers gauntlet; TYR proposed as lead Breaker

## Body

Three certificates, matching the ladder:
- Certified Foundation: low-level skills proven.
- Certified Architecture: system-design skills proven.
- Certified Builder: whole-app skills proven, cleared to build complex apps for clients.

The bar, an agent earns a certificate only when every gate is a yes:
1. Coverage. Every required skill for that level is at the required grade on the 1-to-9 scale.
2. Proof on file. Every skill has a real passing test or real output, reproducible to the same result.
3. The math check. Once enough attempts exist, Wilson lower bound, Glicko rating minus two deviations above the level cutoff, and SPRT all agree it is real, not luck.
4. Independent audit. AJ reviews the artifacts, never the agent's words, and signs off.
5. Survives the Breakers. The Red Team attacks a real sample with the dirtiest tactics. Any break is a fail. Fix and re-attack. Only a clean run passes.
6. Provenance stamp. Record certified-by model X, date Y, curriculum version Z, so the bar is reproducible.
7. Human sign-off for the top level. For Certified Builder, cleared for client work, the operator gives the final green light.
8. Not forever. A certificate expires and must be re-earned on a cadence, because skills and the world drift, same idea as the 90-day source-decay rule.

The Breakers gauntlet (part of gate 5):
- Security Breaker: injections, auth bypass, data leaks, day-zero style exploits.
- Correctness Breaker: edge cases and weird inputs to force a wrong result.
- Scale Breaker: floods of users and data to make it fall over.
- Chaos Breaker: kills parts mid-task (crash, dropped network) to hunt for lost or corrupted data.
- Rules: independent of the builder and the fleet, attack the real work, log every break, use different AI families so they fail differently. A build passes only when the whole team comes up empty.

TYR proposal (operator to approve, since the operator names every agent and role):
- TYR, first agent from Seed, becomes the lead Breaker and Security Auditor, running the gauntlet independent of the fleet, reporting to AJ.
- Rationale: security is the operator's top worry, so the first created agent guards it. The name fits (Tyr, god of justice and battle). It fills a real critical job, not clutter.

## Links

- extends: 2026-08-06-brain-trust-verdicts-and-operator-contributions
- extends: 2026-08-06-model-tiering-and-certification-design
