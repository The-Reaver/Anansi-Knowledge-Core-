---
id: 2026-08-07-cippe-adaptation-engine-and-help-workflow-spec
type: decision
status: candidate
source: "Cowork session 2026-08-07; operator asked how the app actually helps day to day, adapts to her workflow scientifically, keeps a record, reduces workload, lets her plug in her work, and takes breaks, plus a research-feedback workflow into Qwen/Gemini. (source status: active)"
project: cippe
tags: [cippe, adaptation-engine, personalization, workflow, bring-your-work, break, research-loop, neurodivergent, local, privacy]
---

# CIPP/E copilot, the logical adaptation engine, the bring-your-work help flow, the break button, and the research-feedback loop

## Body

## Anti-overwhelm (rule)
- One primary focus on screen, the rest behind calm sections. Low-distraction toggle app-wide. The app detects overwhelm (piled-up open items, rapid task switching) and simplifies the view and offers a break. Exact thresholds set by the deep UX research.

## Bring your work here (the core help)
- She pastes or drops in a draft response, policy, vendor questionnaire, or DSAR. The copilot reviews it, cites relevant law, drafts or improves it, and flags risks, grounded in the validated corpus, cited, and local/private. Turns the app from a tracker into a working partner.

## Break button (Externalized Thread)
- Always-visible top-bar Break button. Saves exact state, shows a calm pause, resumes at the precise spot on return. The tour states plainly she can break any time. Reduces load, mimics real life.

## The adaptation engine (logical, measurable)
- Records locally and privately: which tasks, when, duration, starts/abandons, deferrals, breaks, overwhelm signals (rapid switching).
- Computes plain metrics: time on task, completion rate, deferral/abandonment rate, peak-focus windows.
- Forms small hypotheses from metrics (e.g., access requests finish faster in the morning; vendor reviews abandoned past 5 open).
- Offers one targeted suggestion, then measures whether accepting it moved the metric the right way. Keeps what works, drops what does not. Evidence in, evidence out.
- Guardrails: correctness and law always beat speed; she can correct or switch off any adaptation; everything local; the app always explains why (transparent, not mysterious).
- Math honesty (Mandate 7): n=1 with little early data, so use simple steady signals, require enough observations before asserting a pattern, avoid over-fitting. Deep research + Qwen/Gemini meta-analysis refine metrics and thresholds.

## Research-feedback loop (operator-in-the-loop)
- The app produces periodic de-identified summaries (patterns and metric changes only, no personal content). Operator pastes them into Qwen or Gemini. Their analysis feeds the meta-analysis. Improved rules return to the app. Loop: local measurement -> structured feedback -> outside research -> better tool.

## Justify-every-section
- Research phase deliverable: a rationale document mapping each screen and feature to the evidence justifying it. Nothing there by guess.

## Build sequencing
- Prototype now (after the polish pass): the Break button and the Bring-your-work flow, with anti-overwhelm behavior folded in.
- Deeper: the full adaptation engine and thresholds are tuned in the research phase, then built into the local single-container version via Antigravity.

## Links

- relates-to: 2026-08-07-cippe-personalized-user-profile-and-companion-spec
- relates-to: 2026-08-07-neurodivergent-specialist-agent-and-meta-analysis-plan
- relates-to: 2026-08-07-cippe-lovable-version-build-scope
