---
id: 2026-08-06-model-tiering-and-certification-design
type: decision
status: candidate
source: "Cowork session 2026-08-06, operator on phone; asked how model selection works across the plumbing, whether the certifier must be a high model, and to research things not being considered. (source status: active)"
project: fleet
tags: [modeling, model-tiering, certification, aj-auditor, proof, adversarial, mandate-7, strategy]
supersedes: []
superseded_by: null
---

# How the models work across the ADLC, and how certification stays honest

## Body

Operator hypothesis: the certifier should be a high (strong) model. Verdict: yes, and sharpen it three ways. The certifier must be strong, independent (never the builder grading its own work), and backed by deterministic test results rather than the model's opinion.

Model tier per stage of the engine and ladder:
- Assign, Level up, Log: cheap or no model. Mechanical, pulling the next task and recording pass or fail.
- Build: match the model to the task. Hard low-level work gets a strong model, simple mechanical work a mid or cheap model. Route by difficulty.
- Prove: mostly code, not a model. verify.py runs the tests and returns green or red. A test cannot be flattered or fooled. Where judgment is genuinely needed (is the architecture sound), use an independent reviewer, not the builder.
- Capture the atomic note: a mid model, since it is structured writing.
- Certify: a strong, independent model that reads only the artifacts (code, tests, results), never the builder's explanation, backed by the real test outcomes, with the operator signing the final green light for the biggest steps.

Things that are easy to miss and should be built in:
- Proof as code beats proof as opinion. The strongest gate is a passing test suite, not a smart model saying it looks good. Invest in real test harnesses (verify.py, red-then-green) as the primary gate. This is the anti-gaming backbone.
- Independence, never self-grading. The builder model must not certify its own work. The fleet already has this in AJ, the unbiased auditor from the Brain Trust founding verdict: no build role, no vote, reads artifacts only, never a spoken explanation. AJ or an AJ-like independent certifier runs certification.
- Model tiering saves large money and time. Do not run the top model on everything. Cheap for bulk and mechanical, strong for hard builds and certification. This keeps a big fleet affordable.
- Escalation ladder. Start a task on a cheap model. If it fails the proof gate a few times, escalate to a stronger model. Spend expensive compute only where needed.
- Adversarial checking. To certify, ask a model to try to break the work, not is this good. If it cannot break it, it is more likely real. Multiple skeptics, majority to pass.
- Diverse reviewers. Different model families fail differently, so a panel of different models catches more than one model asked twice. The repo already learned this: an Opus review caught that two supposedly independent passes were the same model prompted twice.
- Record the certifier. Every certification carries certified-by model X, on date Y, so the bar is reproducible and comparable over time, like atom-versioning provenance.
- Human final sign-off for the highest stakes. For clearing an agent to build for a real client, the operator gives the final green light. Models propose, the human approves, the same as the compliance client-facing gate.

The good news: the fleet already holds most of these instincts (AJ, verify.py, the leveling math, the red-then-green proof, the diverse-review lesson). What is new and needs adding to the plan is the explicit model-tiering layer: which model tier runs which stage, the escalation ladder, and recording the certifier model.

## Links

- extends: 2026-08-06-agent-development-lifecycle-adlc-gameplan
- relates-to: 2026-08-06-cross-agent-stars-dreams-curriculum-design
