---
id: build-a-real-world-failure-corpus-from-practitioner-forums-2026-09-01
type: ruling
status: candidate
source: "Operator directive, 2026-09-01 — Abad, direct instruction in the Ambient Clinical Scribe planning session; grounded against the 2026-08-06 Breakers notes and AJ/AJ_HARDWIRING.md in The-Reaver/Stag-Fleet"
project: fleet
tags: [corpus, research, failure-modes, sourcing, knowledge-core, practitioner-forums]
supersedes: []
superseded_by: null
---

# Harvest real bugs, breaks and fixes from practitioner forums into a well the fleet can draw on mid-problem

## Body

Operator ruling, 2026-09-01: the fleet should gather **real-life occurrences — real code bugs,
breaks and fixes** — from reputable practitioner sources, document them, and feed them to the team,
"so that we have a wealth of knowledge when we're developing and running into problems and we have
similar cases that we can draw from."

Named sources: Reddit-style forums dedicated to a technique, Quora, and comparable venues where
developers discuss what they built, **what broke, and how they fixed it**. The operator's
qualifier is the important part — *"reputable sources or sources that check out"* — so this is a
sourcing problem before it is a scraping problem.

Why this is worth building rather than relying on the model: a forum thread carries the **failure
and the fix together, with the symptom as it actually appeared**. That pairing is what makes a case
retrievable when someone is mid-problem and only has the symptom. It is also exactly the shape the
Core already stores — this Core's own most valuable notes are of the form "X reported success while
Y was true; check Z next time."

**Three constraints this must inherit, not reinvent:**

1. **The existing source-rating discipline.** The Core already carries `source_rating`,
   `evidence_state` and `risk_class` fields. Forum content is low-rated by default and must be
   marked as such, never promoted to ratified on popularity.
2. **Corroboration before capture.** A single unreplicated forum claim is an anecdote. The
   Compliance Intelligence precedent — 44 sourced documents, none reviewed — is the warning: volume
   without a review gate produces a corpus nobody can safely cite.
3. **It feeds the Breakers too.** Real recorded breaks are attack material. A failure corpus and an
   attacker library are the same asset read from two directions.

**Scope check:** this is a continuous ingestion programme with its own pipeline, dedup, and review
gate — not a one-off scrape. It should be sized honestly before it is scheduled.

## Links

- relates-to: the-breakers-are-standing-attackers-run-as-periodic-war-games-2026-09-01
- relates-to: forty-four-sourced-legal-documents-none-lawyer-reviewed-2026-08-31
- relates-to: session-transcripts-are-reachable-so-the-harvest-backlog-is-a-choice-not-a-limit-2026-08-31
