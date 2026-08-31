---
id: 2026-08-06-model-tier-per-adlc-stage
type: spec
status: ratified
source: "Cowork session 2026-08-06, operator on phone; asked how model selection works across the plumbing (source status: active); mined from candidates/2026-08-25/2026-08-06-model-tiering-and-certification-design.md"
project: fleet
tags: [model-tiering, adlc, cost, certification]
---

# Model tier assigned per ADLC stage: cheap/mechanical for Assign/Level-up/Log, matched-to-difficulty for Build, code (not a model) for Prove, mid model for Capture, strong+independent for Certify

## Body

Assign, Level up, Log: cheap or no model — mechanical, pulling the next task and recording pass or fail. Build: match the model to the task — hard low-level work gets a strong model, simple mechanical work a mid or cheap model, routed by difficulty. Prove: mostly code, not a model — verify.py runs the tests and returns green or red, a test cannot be flattered or fooled; where judgment is genuinely needed (is the architecture sound), use an independent reviewer, not the builder. Capture the atomic note: a mid model, since it is structured writing. Certify: a strong, independent model that reads only the artifacts (code, tests, results), never the builder's explanation, backed by the real test outcomes, with the operator signing the final green light for the biggest steps.

## Links

- relates: 2026-08-06-certification-integrity-principles-proof-as-code
- relates: 2026-08-06-three-certificates-and-eight-gate-graduation-bar
