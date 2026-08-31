---
id: 2026-08-07-cippe-personalization-companion-and-local-first-spec
type: decision
status: candidate
source: "Cowork session 2026-08-07; operator described the intended real user (a specific neurodivergent privacy professional, referred to as \"her\"), and asked for deep personalization, a caring but non-sycophantic adaptive tool, confidential identity, and local-on-her-computer deployment. (source status: active)"
project: cippe
tags: [cippe, personalization, companion, neurodivergent, caring, anti-sycophancy, confidentiality, local-first, single-container, adaptive]
supersedes: []
superseded_by: null
---

# CIPP/E copilot, the personalization and Companion layer, the caring-but-correct principle, confidentiality, and local-first setup

## Body

## Intended user (confidential)
- Built for one specific person: a skilled privacy professional who is neurodivergent (ADD/ADHD). Referred to as "her".
- Identity is confidential and a privacy matter. Never state her name. The software stores it locally and personalizes around it. Claude is not given the name.

## Core principle: caring AND correct (not sycophantic)
- The copilot is warm and caring in tone, but never bows to her. When she heads toward a wrong or non-compliant step, it says so plainly and cites the law. Warmth in tone, firmness in substance. The goal is her professional work done right, not flattery. This protects her professional well-being.

## Personalization and Companion layer
- The tool adapts and morphs to her: it studies her workflow, learns what she does day to day, and suggests improvements to that workflow.
- Gentle first-run that asks a few thoughtful questions and stores her profile locally.
- Adaptive suggestions: notice repeated actions, offer shortcuts, suggest the next helpful step. Calm and non-intrusive, never nagging.
- Personable touches: remember small things she shares (for example a favorite book) and occasionally offer something rich and in-depth about it. Little caring things on the side, personable but not corny or falsely motivational.
- It asks questions to understand her better over time. Its only aim is to be the best, most intuitive tool that changes based on her needs.

## Local-first setup (everything in one place)
- The real local product is the single-container build: app plus a local database (Postgres + pgvector) packaged to run entirely on her computer. Matches the ratified CIPP/E spec. Antigravity builds it. All data stays local, nothing forced to the cloud.
- The Lovable version is the fast prototype and design surface where we perfect the personalization, tone, adaptivity, and calm navigation. That design becomes the local single-container build she runs.
- Cloud is optional (backup/sync only if she chooses). Default is local and private.

## Build plan (finish as a prototype now)
1. Guided tour (calm, warm).
2. Calm Notion-style navigation pass.
3. Personalization and Companion layer prototype (first-run profile stored locally, adaptive suggestions, caring touches, corrective law-abiding guidance tone).
4. Then done as a prototype, set up to be refined by the deep neurodivergent research + Gemini/Quinn meta-analysis, and handed to Antigravity as the local single-container build.

## Links

- relates-to: 2026-08-07-cippe-lovable-version-build-scope
- relates-to: 2026-08-07-cippe-nav-drawer-and-adaptive-feedback-requirements
- relates-to: 2026-08-07-neurodivergent-specialist-agent-and-meta-analysis-plan
