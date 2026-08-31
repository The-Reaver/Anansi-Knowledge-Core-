---
id: 2026-08-07-cippe-research-clarifications-qwen-round2
type: decision
status: candidate
source: "Cowork session 2026-08-07; Qwen asked a second round of clarifying questions on the privacy-workflow research prompt. These are the ratified answers. (source status: active)"
project: cippe
tags: [cippe, research, workflow, features, automation, decision-support, integration, local, privacy]
supersedes: []
superseded_by: null
---

# CIPP/E research clarifications round 2 (answers to Qwen), recency, pain-point structure, feature emphasis

## Body

## Recency vs history
- Prioritize recent practice (last 2-3 years). Regulatory change and AI governance make current workflows the ones that matter. Include history only briefly, where it explains a current practice or an active shift (rising DSAR volume, emerging AI governance).

## Pain-point structure
- Do both, in order: first map pain points per workflow component (DSAR, DPIA/PIA, RoPA, vendor/TPRM, breach, access reviews, regulatory change); then synthesize cross-cutting themes (tool fragmentation, regulatory ambiguity, stakeholder coordination, manual data-finding, deadline pressure). Per-component -> features; cross-cutting -> design principles.

## Feature emphasis (ranked, given local/private/offline design)
1. Decision support first (risk-scoring templates, DPIA guidance, cited answers, prioritization).
2. Automation second (auto-populate RoPA, draft DSAR and breach responses, statutory deadline clocks).
3. Integration last and constrained. Favor paste-and-import ("bring your work here") over live external GRC/ticketing, because the tool is local, offline, and handles the employee's sensitive data. Note only light, optional, privacy-safe integrations; treat heavy external integration as out of scope.

## Links

- relates-to: 2026-08-07-cippe-research-clarifications-qwen
- relates-to: 2026-08-07-cippe-redesign-research-claude-half
- relates-to: 2026-08-07-cippe-maintenance-architecture-minimalism-and-checkin
