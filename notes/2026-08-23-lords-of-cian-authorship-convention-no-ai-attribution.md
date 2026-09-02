---
id: 2026-08-23-lords-of-cian-authorship-convention-no-ai-attribution
type: decision
status: ratified
ratified: "2026-08-25 — anansi-promote skill run, 9/10 (novelty 2, evidence 2, actionability 2, generality 1, non-contradiction 2). Independently re-verified 2026-08-25 by script: canon-ledger.json now contains ZERO occurrences of the string \"Claude\" across all 510 rules, confirming all twelve attributions were in fact scrubbed and stayed scrubbed. The note's own open follow-up -- whether this is standing practice or a one-time fix -- remains unanswered and is carried forward."
project: lords-of-cian
tags: [lords-of-cian, authorship, operator-contribution, canon-ledger]
sources:
  - ref: "Direct operator instruction, 2026-08-23; independently re-verified by script against canon-ledger.json on 2026-08-25 (zero \"Claude\" occurrences)"
    reliability: high
    origin: "2026-08-23 Lords of Cian session; re-verified 2026-08-25 anansi-promote run"
provenance:
  archive: research/knowledge-home/raw/2026-08-23-lords-of-cian-cult-network-and-archive-planning.jsonl
  turns: [1, 96]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Lords of Cian project documents and canon-ledger entries carry Abad's sole authorship; no AI-attribution language, retroactive or going forward

- id: 2026-08-23-lords-of-cian-authorship-convention-no-ai-attribution
- type: decision
- status: ratified
- ratified: 2026-08-25 — anansi-promote skill run, 9/10 (novelty 2, evidence 2, actionability 2, generality 1, non-contradiction 2). Independently re-verified 2026-08-25 by script: canon-ledger.json now contains ZERO occurrences of the string "Claude" across all 510 rules, confirming all twelve attributions were in fact scrubbed and stayed scrubbed. The note's own open follow-up -- whether this is standing practice or a one-time fix -- remains unanswered and is carried forward.
- class: confirmed
- source: this chat, 2026-08-23, operator instruction: "i need these documents to say i am the author and no mention of claude"
- confidence: high, direct operator instruction, applied and verified
- verified: 2026-08-23
- tags: lords-of-cian, authorship, operator-contribution, canon-ledger
- project: lords-of-cian

## Body

Twelve fields in `canon-ledger.json` (the Lords of Cian canon-rules ledger, a Claude Project doc) had attributed invention or expansion work to "Claude" in their `source` or `note` fields, for example "Proposed by Abad, expanded and world-fitted by Claude, approved by Abad." The operator instructed that project documents read as his own authorship, with no mention of Claude anywhere.

All twelve fields were rewritten to remove the AI attribution (for example, "Proposed by Abad, expanded and world-fitted by Claude, approved by Abad 2026-08-22" became "Written by Abad, approved by Abad 2026-08-22"), and every document written afterward in the same session carried an explicit "By Abad Morel" byline instead of any framing implying an assistant wrote it.

One legitimate exception was found and left alone rather than scrubbed: a reference in the project's own to-do list to which Claude model powers the writing fleet's agents ("Sonnet 5 primary inside Claude Code sessions") is a technical architecture fact about the fleet's implementation, not an authorship claim about a document, and was flagged to the operator rather than silently changed either way.

Not yet confirmed as permanent standing practice across the whole project or as a one-time fix; the operator has not yet answered that follow-up question as of this note.

## Links

- relates: 2026-08-23-halt-and-require-correction-on-underage-plus-sexualized-content-before-processing (same session, a different operator-correction pattern)
