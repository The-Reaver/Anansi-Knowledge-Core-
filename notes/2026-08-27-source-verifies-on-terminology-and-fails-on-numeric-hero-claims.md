---
id: 2026-08-27-source-verifies-on-terminology-and-fails-on-numeric-hero-claims
type: lesson
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: fleet
tags: [brain-trust, verification, external-sources, citation-laundering, review]
sources:
  - ref: "Brain Trust review of five external documents, GEO Suite session 2026-08-27; the pattern was named to the operator on each recurrence across all five"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [6, 7]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# In five reviewed external documents the named technical and legal terminology verified while the numeric hero claims repeatedly did not, so correct vocabulary is no evidence for the statistics beside it

## Body
Five external documents from one source were put through Brain Trust review. A pattern held
across all five and was named to the operator each time it recurred:

- **Real named technical and legal terminology tended to verify correctly.** The documents used
  genuine framework names, genuine statutory references, genuine architectural vocabulary.
- **Specific numeric "hero claims" repeatedly failed independent verification** -- fabricated
  statistics, misattributed figures, and citation-laundering (a real citation attached to a
  number it does not support).

The trap is that the first property is what makes a reader trust the second. Correct vocabulary
reads as domain competence, and domain competence reads as a reason to accept the numbers without
checking. **These are independent.** Producing accurate terminology is cheap -- it is the part a
language model or a motivated writer gets right by default. Producing an accurate statistic
requires actually having the source. A document can be fluent and precise in every named term and
still have invented every figure in it.

Practical rule when reviewing external material: **verify the numbers separately from the
vocabulary, and never let the vocabulary raise your prior on the numbers.** Check each specific
figure against its cited source directly -- especially the memorable, quotable ones, which is
where this source's failures clustered. Where a citation is real, confirm it actually says the
thing the number claims; citation-laundering survives a naive "does this source exist" check.

Governing instruction under which these reviews ran, from the operator, verbatim: *"these are
just suggestions, whatever is good keep, whatever is not eradicate, and if nothing is good
eradicate everything"* and *"you are not obligated to keep anything."* -- an explicit licence to
return a total rejection, which is what made honest review of a persuasive document possible.

## Links
- relates-to: 2026-08-27-automated-lead-engine-declined-in-full-two-refinements-banked
- relates-to: 2026-08-27-compliance-intelligence-is-a-separate-product-geo-a-future-thin-consumer
