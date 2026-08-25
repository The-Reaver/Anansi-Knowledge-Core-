---
id: 2026-08-25-gate-1-threshold-candidates
type: finding
status: candidate, pending Brain Trust table decision
source: this chat, item 4 of the 9-Gate verdict's ratification preconditions. Research agent,
  web search (direct WebFetch to metr.org/arxiv.org/deepmind.google was blocked by this session's
  network egress proxy — figures cross-checked via search-result snippets from those primary
  sources plus independent secondary sources, not fetched full pages).
project: fleet
tags: [brain-trust, 9-gate, gate-1, metr, deepmind, levels-of-agi, time-horizon]
---

# Gate 1 threshold candidates: three concrete, citable options grounded in METR Time Horizon and DeepMind Levels of AGI — not a decision, a table input

## Body

Per `2026-08-25-9-gate-brain-trust-verdict.md`: "the specific Time Horizon threshold or autonomy
rung that constitutes 'cleared for Gate 1' is a table decision, not one this ruling can make."
This note is that table input — real published data and three concrete candidates, not a picked
number.

## METR Time Horizon — what's actually published

The metric: the human-task-duration at which a model's success probability crosses 50%
("50%-time-horizon"), from *"Measuring AI Ability to Complete Long Software Tasks"*
(arXiv:2503.14499, March 2025), built from three task sets (HCAST, RE-Bench, SWAA) that skew
toward software/ML-engineering work. Live leaderboard: metr.org/time-horizons.

Trend: frontier time horizons doubled roughly every 7 months from 2019-2024/25 (GPT-2 ~2 seconds
in 2019; Claude 3.7 Sonnet ~50 minutes in March 2025; o3 ~1.5 hours, above trend). Some
independent (non-METR-headline) analyses report the doubling accelerating to ~4 months from 2024
onward — flagged below as directional, not load-bearing.

Most recent published figures found:

| Model | 50%-time-horizon | Notes |
|---|---|---|
| Claude 3.7 Sonnet (~Mar 2025) | ~50 min | — |
| o3 (~2025) | ~1.5 hrs | above long-run trend line |
| GPT-5 | 2h 17m | 95% CI 65m-4h25m |
| Claude Opus 4.5 | ~4h 49m | — |
| Claude Opus 4.6 | ~14.5 hrs | 95% CI 6h-98h — very wide |

METR's own standing notice (added May 8, 2026, on the live leaderboard): **"Measurements above 16
hrs are unreliable with our current task suite."** A floor at or above that zone would currently
only be clearable by one model, with a confidence interval too wide to function as a bright line.

A **1-4 hour** floor is defensible given current data: above general-purpose/non-agentic models
(tens of minutes and below), below METR's own unreliable-zone, and in the band where
2025-to-early-2026 frontier agentic models actually landed.

## DeepMind "Levels of AGI" — the actual ontology

Morris et al. (Google DeepMind), arXiv:2311.02462, Nov 2023. Two independent axes:

**Performance (0-5)**: 0 No AI, 1 Emerging (roughly GPT-4-class, per the paper), 2 Competent
(>=50th percentile skilled adults), 3 Expert (>=90th percentile), 4 Virtuoso (>=99th percentile),
5 Superhuman.

**Autonomy (0-5)**: 0 No AI, 1 AI as Tool, 2 AI as Consultant, 3 AI as Collaborator, 4 AI as
Expert, 5 AI as Agent (fully autonomous). The paper itself gates full autonomy (Level 5) behind
high performance (Virtuoso/Level 4 or Superhuman/Level 5) — directly relevant to a fleet
onboarding ladder.

**Real gap**: this is a conceptual taxonomy, not an operational test suite. Assigning an actual
agent to "Competent" vs. "Expert" requires the Brain Trust to also adopt or commission a
measurement procedure — that dependency doesn't disappear just because the ontology is real and
citable.

## Three candidates

**A — METR-only**: Gate 1 requires an independently-measured METR 50%-time-horizon of at least 1
hour on the current suite. Roughly where frontier agentic capability crossed in 2025 (below
Claude 3.7 Sonnet, below o3) — a real recently-crossed line. Weakness: single instrument, and the
doubling trend could make it look trivial within a year or two without a scheduled revisit.

**B — DeepMind-only**: Gate 1 requires assessed "Competent" performance (>=50th-percentile-skilled
-adult in the agent's domain) at Autonomy Level 3 (Collaborator) or higher. Weakness: no
operational test defined by DeepMind — adopting this candidate means also commissioning a
measurement procedure, an unresolved dependency, not a footnote.

**C — Combined either/or** (mirrors the prior ruling's own "and/or" framing): Gate 1 requires
EITHER a verified METR 50%-time-horizon of at least 2 hours, OR documented DeepMind "Competent"
performance combined with Autonomy Level 3. The 2-hour figure sits right at GPT-5's measured
score, with Opus 4.5/4.6 comfortably above it and well clear of METR's own unreliable-above-16h
line. The either/or structure covers agents outside METR's software-engineering-skewed task
distribution.

## Recommendation (input, not decision)

Candidate C is the strongest starting point: it honors the prior ruling's "and/or" framing, its
METR figure is anchored to an actual recent frontier crossing point rather than a round number,
and its DeepMind branch covers agents METR's task suite doesn't fit. The actual number, and
whether to require both criteria or either, remains the table's call.

## Honest gaps, not glossed over

- METR's own numbers get unreliable at the top of the range (Opus 4.6's 95% CI spans 6-98 hours).
- The "doubling every ~7 months" trend is METR's own claim for 2019-2024/25; the claimed
  acceleration to ~4 months is from secondary/community analysis, not a METR headline figure.
- The benchmark is domain-skewed toward software/ML-engineering tasks — a Gate 1 rule stated
  purely in METR hours implicitly privileges software-agent-shaped work.
- DeepMind's ontology has no attached test; using it requires the Brain Trust to also adopt a
  measurement procedure.
- Whatever number is picked will decay fast given the doubling trend — a ratified threshold
  should probably carry a scheduled revisit rather than being treated as permanent.
- Gate 1 language should require the METR-published (or independently reproduced) figure
  specifically, not vendor or social-media claims about very recent models.

## Tooling caveat

Direct WebFetch to metr.org, arxiv.org, and deepmind.google was blocked by this session's network
egress proxy; the figures above were assembled via WebSearch result snippets that quote the
primary sources directly, cross-checked against independent secondary sources (METR's own notes,
LessWrong/AlignmentForum writeups), not by fetching and reading the full original pages. If the
Brain Trust wants the primary pages fetched and quoted directly for the ratification record, that
needs an environment without this restriction.

## Citations

- METR, "Measuring AI Ability to Complete Long Software Tasks," arXiv:2503.14499 — https://arxiv.org/pdf/2503.14499
- METR, Time Horizons live leaderboard — https://metr.org/time-horizons/
- METR, "Time Horizon 1.1" (Jan 29, 2026) — https://metr.org/blog/2026-1-29-time-horizon-1-1/
- METR, "Clarifying limitations of time horizon" (Jan 22, 2026) — https://metr.org/notes/2026-01-22-time-horizon-limitations/
- METR, "Measuring Time Horizon using Claude Code and Codex" (Feb 13, 2026) — https://metr.org/notes/2026-02-13-measuring-time-horizon-using-claude-code-and-codex/
- METR, GPT-5 evaluation — https://metr.org/evaluations/gpt-5-report/
- METR, "How Does Time Horizon Vary Across Domains?" (Jul 2025) — https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/
- Morris et al. (Google DeepMind), "Levels of AGI," arXiv:2311.02462 — https://arxiv.org/pdf/2311.02462
- LessWrong, "Claude Opus 4.5 Achieves 50%-Time Horizon Of Around 4 hrs 49 min" — https://www.lesswrong.com/posts/q5ejXr4CRuPxkgzJD/claude-opus-4-5-achieves-50-time-horizon-of-around-4-hrs-49
- LessWrong, "Interpreting the METR Time Horizons Post" — https://www.lesswrong.com/posts/fRiqwFPiaasKxtJuZ/interpreting-the-metr-time-horizons-post

## Links

- extends, `2026-08-25-9-gate-brain-trust-verdict.md`, item 4 of its ratification preconditions.
- affects, `2026-08-25-9-gate-precondition-tracker.md`, which tracks this item's status.
