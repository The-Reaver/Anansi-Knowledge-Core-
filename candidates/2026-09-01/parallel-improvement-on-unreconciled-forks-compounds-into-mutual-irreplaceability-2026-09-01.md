---
id: parallel-improvement-on-unreconciled-forks-compounds-into-mutual-irreplaceability-2026-09-01
type: lesson
status: candidate
source: "Recovery session, 2026-09-01 — first field-level measurement of the two Knowledge Core forks, docs/2026-09-01-knowledge-core-fork-reconciliation.md; the two workstreams named are my own from this same session"
project: fleet
tags: [knowledge-core, forks, divergence, migrations, schema, evidence-standard, supersede, correction]
supersedes: []
superseded_by: null
---

# Improving two forks in parallel does not average out — it makes each one irreplaceable

## Body

The Knowledge Core lives in two git repositories. The size gap was known — 125 ratified notes against
860 — and read as "one is behind." It is not. **Neither contains the other**: 102 ratified notes exist
only in the smaller repository, 837 only in the larger, and just 23 are in both.

The measurement that mattered was field coverage, not file count:

| Field | smaller fork | larger fork |
|---|---|---|
| `status`, `project`, `supersedes`, `superseded_by` | **100%** | 84% / 47% / 0.2% / **0%** |
| `risk_class`, `evidence_state`, `next_review`, `classified` | **0%** | **89%** |

The forks are complementary and almost perfectly **disjoint**. One holds the ratification status and the
supersede chain; the other holds the entire Evidence Standard classification. Of the 23 notes present in
both, all 23 differ — and the bodies are identical. Every difference is header.

**A merge in either direction silently destroys data.** Neither repository can be restored from the
other.

## How it happened, which is the part worth remembering

Two workstreams in a single session, each correct, run on **opposite sides** of the fork:

- a supersede backfill — 166 files, 331 insertions, 0 deletions, guarded by parse-before/parse-after
  equality — applied to the smaller fork;
- Evidence Standard Pass One — 230 files classified — applied to the larger.

Neither was careless. Both were verified. Together they converted a *size* difference, which a copy
could have fixed, into a *schema* difference, which only a field-level union can.

## The rule

**Before improving a forked store, reconcile it — or confine every improvement to one side.** Parallel
improvement on unreconciled forks does not converge; each pass makes both copies more load-bearing and
the eventual merge more expensive. The cheap moment is before the first pass, and it never comes back.

## The check

When a store exists in two places, measure **field coverage**, not file count, before touching either.
Equal counts can hide disjoint schemas, and unequal counts are routinely misread as "one is stale" when
the truth is "each is authoritative for a different column." Then either merge, or declare a sync
direction and put every subsequent pass on the upstream side.
