---
id: 2026-08-07-cippe-redesign-research-claude-half
type: finding
status: candidate
source: "Cowork session 2026-08-07; Claude conducted four parallel research streams for the CIPP/E redesign phase. Operator runs Gemini and Qwen deep research in parallel; findings to be merged in a meta-analysis. (source status: active)"
project: cippe
tags: [cippe, research, neurodivergent, adhd, coga, wcag, navigation, design-system, tone, adaptation, meta-analysis]
supersedes: []
superseded_by: null
---

# CIPP/E redesign deep research, Claude's half (four streams), for the meta-analysis

## Body

## Stream 1: Neurodivergent/ADHD UX + COGA/WCAG (top rules)
- One primary action per screen; secondary demoted or hidden.
- Never ask the same info twice; carry data forward (WCAG 3.3.7).
- Auto-save + resume: reopening restores state and shows the next step.
- No involuntary timeouts/countdowns; any limit adjustable/removable (2.2.1).
- Ambient, non-threatening time/progress; deadlines framed neutrally.
- Plain language, short sentences, low reading level; no walls of text.
- Chunk tasks with visible "Step X of Y".
- Calm muted palette, no clashing bright contrast; keep AA (4.5:1).
- No autoplay motion; honor prefers-reduced-motion; one-click low-distraction mode.
- Notifications batched, neutral, fully user-controllable; no nagging/guilt/red-alert.
- Consistent layout, nav, and help location (3.2.3/3.2.4/3.2.6).
- Blame-free errors with always-available undo.
- Key COGA objectives: help focus (O5), don't rely on memory (O6), clear content (O3), help/support (O7), personalization (O8). Key WCAG 2.2: 3.3.7, 3.2.6, 3.3.8, 2.2.1, 2.2.2, 3.2.1/3.2.2, 2.4.11, 2.5.8.

## Stream 2: Minimal nav + beloved tools
- Cap top-level items ~5; chunk the rest into 2-4 labeled groups; collapse secondary groups by default.
- Label + icon; avoid ambiguous icon-only.
- One sidebar context -> one main pane. Progressive disclosure for the rest.
- Ship sensible defaults; kill the blank page (Notion's failure for ADHD = 47 decisions before starting).
- Instant always-on capture; sub-second speed is an accessibility requirement.
- Command palette (Cmd/Ctrl+K) with fuzzy search over nav + actions + recents = pressure valve so visible nav stays minimal.
- Focus/full-screen mode opt-in, one gesture in/out, hides chrome not essentials.
- Structure the 16-item app as ~4-5 rooms (e.g., Focus / Work / Knowledge / Review / You+Settings), only the active one expanded.

## Stream 3: Calm accessible design system (tokens)
- Spacing: 8pt grid {4,8,12,16,24,32,48,64,96}; card padding 24; card gap 16; section gap 48; content max width ~680.
- Type: base 17px / lh 1.6; H1 30/600, H2 22/600, label 13/500, body 17/400, caption 14/400; weights 400/500/600; left-align, no justify. Text-spacing floors per WCAG 1.4.12.
- Buttons/controls: primary & secondary 44px tall, padX 24, radius 8; inputs 44px; min target 24px (WCAG 2.5.8), 12px between buttons, 16px between fields; 2px focus ring, 2px offset. One accent-filled primary per screen.
- Color (light): bg #F7F7F5, surface #FFFFFF, border #E3E3E0, text #1F2933 / #5A6472, accent #3B6E8F (muted slate-blue), accent-subtle #EAF1F5, success #2E7D5B, danger #B4432E. One accent hue; color never the only signal; body aims AAA 7:1.
- Motion: 120-200ms, ease-out, no bounce/parallax/autoplay; honor prefers-reduced-motion.

## Stream 4: Tone + adaptation + grounding
- Tone: trust drives desirability (NN/g: 52% trust vs 8% friendliness); humor backfires on serious topics. Bedside-manner, steady colleague, no exclamation/emoji cheerleading, no praise for routine actions, name hard things plainly, end each message with one clear next step.
- Adaptation (n=1): track only visible workflow signals (no mood/health inference); every suggestion states its "because"; thin patterns (<~3-5 obs) phrased as tentative questions; suggest never silently change; stable layout across sessions; prominent accept/dismiss/don't-suggest-again; visible editable memory; suggestions in the periphery; graceful fallback to deadline/chronological view. Calm-tech principles.
- Grounding facts (ISACA/IAPP): 63% of privacy pros say the job is more stressful than 5 years ago; median team shrank ~8 -> ~5; ~43% underfunded; #1 obstacle is the complex international legal landscape; DSARs rising in volume/complexity; AI governance added on top. Use to normalize without minimizing; never overclaim risk removal.

## Meta-analysis plan
- Operator runs Gemini + Qwen deep research (two prompts each). Claude merges both halves, dedupes, weights by evidence quality, flags disagreements, adversarially verifies shaky claims before any finding becomes a design rule.

## Sources
- W3C COGA Making Content Usable; WCAG 2.2; W3C WAI Cognitive; GOV.UK accessibility; NN/g (cognitive load, progressive disclosure, nav items, zen mode, 3-click, tone of voice, ML UX, recommendations); Material Design; Refactoring UI; Calm Tech Institute; ISACA 2025/2026; IAPP.

## Links

- relates-to: 2026-08-07-neurodivergent-specialist-agent-and-meta-analysis-plan
- relates-to: 2026-08-07-cippe-adaptation-engine-and-help-workflow-spec
- relates-to: 2026-08-07-cippe-personalized-user-profile-and-companion-spec
