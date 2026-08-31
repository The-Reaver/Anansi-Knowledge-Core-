---
id: 2026-08-06-certification-integrity-principles-proof-as-code
type: ruling
status: ratified
source: "Cowork session 2026-08-06, operator on phone; asked how model selection works and whether the certifier must be a high model, and to research things not being considered (source status: active); mined from candidates/2026-08-25/2026-08-06-model-tiering-and-certification-design.md"
project: fleet
tags: [certification, proof-as-code, escalation, self-grading, provenance]
supersedes: []
superseded_by: null
---

# Certification integrity principles: proof as code beats proof as opinion, never self-grade, escalate on repeated failure, record the certifier, human sign-off at the top

## Body

The certifier must be strong, independent (never the builder grading its own work), and backed by deterministic test results rather than the model's opinion. Proof as code beats proof as opinion: the strongest gate is a passing test suite, not a smart model saying it looks good — invest in real test harnesses (verify.py, red-then-green) as the anti-gaming backbone. Independence, never self-grading: the builder model must not certify its own work; the fleet already has this in AJ, the unbiased auditor — no build role, no vote, reads artifacts only, never a spoken explanation. Model tiering saves large money and time: do not run the top model on everything. Escalation ladder: start a task on a cheap model, and if it fails the proof gate a few times, escalate to a stronger model, spending expensive compute only where needed. Record the certifier: every certification carries certified-by model X, on date Y, so the bar is reproducible and comparable over time, like atom-versioning provenance. Human final sign-off for the highest stakes: for clearing an agent to build for a real client, the operator gives the final green light — models propose, the human approves, the same as the compliance client-facing gate. (Diverse-reviewer independence — using different model families because they fail differently — is a related, separately-recorded lesson from an Opus review that caught two supposedly independent passes being the same model prompted twice; see the linked note rather than re-deriving it here.)

## Links

- relates: 2026-08-06-model-tier-per-adlc-stage
- relates: 2026-08-06-ci-regulatory-pipeline-opus-review-and-schema-spec
