---
id: 2026-08-07-cippe-nav-drawer-and-adaptive-feedback-requirements
type: decision
status: candidate
source: Cowork session 2026-08-07; operator asked for a Notion-style intuitive navigation drawer researched for neurodivergent use, and an adaptive feedback loop that continuously learns what the person needs. Decision: build all features first, then do the deep research and redesign as one pass. (source status: active)
project: cippe
tags: [cippe, neurodivergent, navigation, notion, ux-research, feedback-loop, redesign, accessibility, adhd]
---

# CIPP/E copilot, two design requirements for the post-v1 redesign phase (Notion-style nav drawer, adaptive feedback loop)

## Body

## Decision
- Build all CIPP/E features and functions first, then run one deep UX research and redesign pass. The navigation drawer touches every screen, so design it once against the finished feature set.

## Requirement 1: Notion-style intuitive navigation drawer
- A calm, super-simple, collapsible sidebar drawer like Notion's, researched for ADD/ADHD/neurodivergent navigation.
- Goals: reduce cognitive load, make every feature findable without hunting, group related tools, allow the user to see only what matters now.
- Research targets: neurodivergent navigation patterns, progressive disclosure, WCAG 2.2 AA + COGA, and how Notion's sidebar (sections, collapse, favorites, search) supports low-effort navigation.

## Requirement 2: Adaptive feedback loop
- Beyond the bridge that sends feature requests back to the team, the app should continuously try to understand what the person needs and surface it (for example, noticing repeated actions and offering a shortcut, suggesting the next helpful step).
- Keep it calm and non-intrusive, never nagging. The person can also ask for features directly (the existing Requests bridge).

## Where it fits
- Both fold into the post-v1 redesign task. Not built now; captured for that phase.

## Links

- relates-to: 2026-08-07-cippe-lovable-version-build-scope
- relates-to: 2026-08-07-site-generator-mirrors-build-methodology
