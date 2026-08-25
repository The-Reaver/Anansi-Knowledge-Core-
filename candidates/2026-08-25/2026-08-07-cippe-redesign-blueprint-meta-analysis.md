---
id: 2026-08-07-cippe-redesign-blueprint-meta-analysis
type: decision
status: candidate
source: Cowork session 2026-08-07; meta-analysis merging Claude's four research streams with four operator-run deep-research documents (Gemini x2, Qwen x2). Consensus items are firm; conflicts resolved; weak-sourced claims flagged. (source status: active)
project: cippe
tags: [cippe, redesign, blueprint, meta-analysis, design-tokens, neurodivergent, coga, wcag, local, rag, interview, tone]
---

# CIPP/E redesign blueprint, meta-analysis of Claude + Gemini + Qwen research (ratified design rules, tokens, and architecture)

## Body

## Confidence
- Claude research and operator's Gemini/Qwen research converged strongly. Consensus items below are firm design rules.

## Cognitive rules (consensus)
- Priority order: working-memory offloading (Externalized Thread) > task initiation > decision-fatigue reduction > gentle time.
- WCAG 3.3.7 Redundant Entry: never ask same data twice; relational auto-fill (RoPA -> DPIA -> DSAR).
- One thing at a time; progressive disclosure; hide downstream steps until prerequisite done; no "wall of red".
- Capture-then-execute split with a "Top 3" for the active session.
- Auto-save every input; restore exact state on relaunch.
- Ambient, non-punitive time cues (low-contrast depleting bar), never countdowns/alarms.

## Navigation (consensus)
- Command palette (Cmd/Ctrl+K) with fuzzy search as primary interface and action executor.
- Collapsible sidebar; features grouped into 4-5 rooms; only active group expanded.
- Opt-in focus/full-screen mode, one gesture in/out; stable layout across sessions.

## Design tokens (ratified)
- Spacing: 8pt grid {8,16,24,32,48,64}; card padding 24; section gap 48.
- Type: sans-serif; base 16px (scalable); line-height 1.6; H1 ~30/600, H2 ~22/600, label ~13/500, body 16/400, caption 14/400; left-align; no all-caps; line length ~70-80 chars. WCAG 1.4.12 text-spacing floors.
- Targets: min 24px (WCAG 2.5.8) for dense rows; 44px for primary standalone actions; control gap >=24px if <24px targets; focus ring 2px at >=3:1, never obscured (2.4.11/2.4.12).
- Color (sage + slate, low-arousal): bg #F7F9F8; secondary bg #EAEFEA; text #2D3748; text-secondary #4A5568; accent sage #7FB095 (primary/focus/progress); border #CBD5E0; error muted brick #C0564F. One accent hue; color never the only signal; body contrast aims AAA.
- Motion: crossfades/opacity only, 120-200ms; no slide/zoom/parallax; honor prefers-reduced-motion.

## Copilot help model (consensus + adopted)
- Inline contextual assistance: highlight a field -> inline suggestion, substitute only on approval. No separate chat window (avoid context switch).
- Local model with semantic retrieval (RAG) over GDPR, CPRA, CPPA ADMT rules, EDPB guidance, and local policies. Cited answers; drafting/redaction; risk categorization (Low/Med/High).
- Feature ranking: decision support > automation (templates, deadline clocks, auto-populate from import) > constrained paste-and-import integration (no live external APIs).

## DPIA / assessments (adopted)
- CNIL methodology; EDPB nine high-risk criteria threshold screening (advise if full DPIA likely not required when <2 criteria).
- Guided risk matrices with pre-built threat vectors (not a blank table); auto-calc residual risk after mitigations.
- Jurisdiction-specific templates: GDPR DPIA vs CPRA Risk Assessment vs AI/Algorithmic Impact Assessment (do not homogenize).

## Interview / onboarding (consensus + content)
- Triggers: user-initiated primary; milestone-driven secondary (natural pauses); soft calendar nudge last. One constrained (binary) question at a time; guilt-free snooze; positive-but-serious milestone acknowledgement.
- Feeds both interface customization and content suggestions.
- Questionnaire content: role/title, certifications, industry, jurisdictions of responsibility, emerging areas (AI governance), and format + work-style preferences (reminders, summary formats, drafting style, interruption sensitivity).

## Tone (consensus)
- Serious, soothing, literal (COGA 4.4.4), non-corny, no toxic positivity, no emoji cheerleading, no praise for routine actions. Each message ends with one clear next step. Microcopy example: "DPIA logged and saved locally."; errors as neutral facts ("Attention required: DPIA missing legal basis.").

## Personalization (consensus)
- Explicit-led hybrid: implicit forms hypotheses, act only on explicit confirmation; one-line "because"; visible editable memory; stable layout; suggest-never-silently-change; graceful fallback to deadline/chronological view.

## Local/offline architecture (consensus)
- 100% offline feature parity; no telemetry, no cloud sync, no hidden API calls; local LLM inference; local DB (e.g., SQLite/Postgres+pgvector). Maintenance via encrypted USB / direct cable, de-identified learnings only (see in-person connection note).

## Conflicts resolved
- Accent: sage-green primary + slate text + muted brick-red error (two sources converged on sage).
- Base font: 16px, scalable, lh 1.6.
- Assessment taxonomy: jurisdiction-specific templates, not one generic PIA.
- Governance: solo operator acts as centralized authority but the tool can output developer-friendly ("spoke") guidance.

## Held with caution (Mandate 7)
- Weak-sourced claims (e.g., "executive function 30% slower" from Instagram; some Reddit/Scribd cites): keep as motivation, not product facts.
- Stress/cost figures (shrinking teams, ~$1,524/DSAR, ~$4.24M breach, ~EUR7.1B fines, 443 breaches/day): recur across ISACA/IAPP/IBM, directionally sound; attribute, do not overstate precision.
- CPRA/ADMT 2026-2027 dates from law-firm summaries: verify against CPPA primary source before the app relies on them.

## Corpus additions (feed the gathering plan)
- CPRA 2026 rules (ADMT, risk assessments, cybersecurity audits), Transfer Impact Assessments / Schrems II, EU AI Act (Art. 4 AI literacy), EU digital laws (DMA/DSA/DGA/Data Act/NIS2) interplay with GDPR.

## Links

- extends: 2026-08-07-cippe-redesign-research-claude-half
- relates-to: 2026-08-07-cippe-research-clarifications-qwen (+ round2)
- relates-to: 2026-08-07-cippe-adaptation-engine-and-help-workflow-spec
- relates-to: 2026-08-07-cippe-in-person-connection-method
- relates-to: 2026-08-07-compliance-intelligence-gathering-plan
