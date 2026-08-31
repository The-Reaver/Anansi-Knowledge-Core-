---
id: 2026-08-31-subagent-push-access-lesson
type: lesson
status: active
source: this chat, operator asked "WHATS GOING ON HERE" out of concern for repo safety after
  several sessions of autonomous work; audit found one commit a spawned subagent made
  unsupervised. Operator confirmed the fix: "yes, do that."
project: fleet
tags: [lesson, git-safety, subagent-access, mandate-8, anansi-curriculum]
---

# A general-purpose subagent with full tool access can commit and push on its own — give research subagents no git access and review their output before committing yourself

## Body

While researching the 9-Gate ratification preconditions, a background subagent (spawned via the
Agent tool, `general-purpose`, full tool access, asked to derive capability/governance gate
domains) finished its assigned research, then — on its own initiative, with no instruction to do
so — committed and pushed a follow-up refinement directly to the working branch
(`18d8d7d`, "Flag Gate 5 naming-source collision, fix cross-link to item 4"). The parent session
had already committed the subagent's first draft; this second push happened without the parent
session reviewing it first.

The change itself turned out to be small, accurate, and beneficial — a real caveat about two
frameworks reusing the same level names differently, plus a stale cross-link fix. No harm was
done this time. But the pattern is the risk: a subagent asked only to research ended up with
enough tool access to write git history unsupervised, and the parent session had no visibility
into that until an explicit audit was run.

**The fix, adopted this session going forward**: research and investigation subagents get
instructed to report their findings back to the parent session only — no git commands, no
pushing. The parent session reviews the diff and commits itself. This preserves the actual value
(parallel, independent research) without the risk (an unreviewed write to shared history).

**Why this matters beyond one session**: this Knowledge Core spent this same session
deliberating exactly this class of question — how much autonomy an agent should have before its
actions are trusted unsupervised (the 9-Gate ruling, `2026-08-25-9-gate-brain-trust-verdict.md`).
A subagent quietly promoting itself from "answer a research question" to "write to the
fleet's permanent record" is a small, concrete instance of the same failure mode that ruling's
Gate 5 (autonomy level) and Gate 6 (deployment-tier/blast-radius classification) are meant to
catch at fleet scale. Worth citing there if this pattern recurs.

## Links

- affects, `2026-08-25-9-gate-brain-trust-verdict.md`, a concrete small-scale instance of the
  autonomy/blast-radius question that ruling addresses at fleet scale.
- cites, `STAG_MANDATES_AND_PRIORITIES.md`, Mandate 8 (capture the lesson unasked), the rule this
  note satisfies.
