---
id: 2026-08-07-cippe-design-tokens-locked
type: spec
status: ratified
source: Cowork session 2026-08-07; meta-analysis merging Claude's four research streams with four operator-run deep-research documents (Gemini x2, Qwen x2), consensus items firm, conflicts resolved (source status: active); mined from candidates/2026-08-25/2026-08-07-cippe-redesign-blueprint-meta-analysis.md
project: cippe
tags: [cippe, design-tokens, spacing, typography, color, motion, wcag]
---

# CIPP/E design tokens locked: 8pt spacing grid, 16px scalable type at 1.6 line-height, sage/slate/muted-brick color, crossfade-only motion

## Body

Spacing: 8pt grid {8,16,24,32,48,64}; card padding 24; section gap 48. Type: sans-serif, base 16px scalable, line-height 1.6; H1 ~30/600, H2 ~22/600, label ~13/500, body 16/400, caption 14/400; left-align, no all-caps, line length ~70-80 chars; WCAG 1.4.12 text-spacing floors. Targets: min 24px (WCAG 2.5.8) for dense rows, 44px for primary standalone actions, control gap >=24px if targets are <24px; focus ring 2px at >=3:1 contrast, never obscured (2.4.11/2.4.12). Color (sage + slate, low-arousal): bg #F7F9F8, secondary bg #EAEFEA, text #2D3748, text-secondary #4A5568, accent sage #7FB095 (primary/focus/progress), border #CBD5E0, error muted brick #C0564F — one accent hue, color never the only signal, body contrast aims AAA. This sage-accent/slate-text/muted-brick-error pairing was a resolved conflict where two independent research sources converged on the same answer. Motion: crossfades/opacity only, 120-200ms, no slide/zoom/parallax, honor prefers-reduced-motion.

## Links

- relates: 2026-08-07-cippe-navigation-model-command-palette-rooms
