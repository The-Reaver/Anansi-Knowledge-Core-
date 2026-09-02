---
id: 2026-08-23-integrity-sanity-check-vs-full-review-for-pushing-already-ratified-backlog
type: decision
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i hereby ratify these notes\"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi, knowledge-core, governance, ratification, verification-scope, git]
sources:
  - ref: "Assistant reports: 'Sanity-checked the backlog before handing you a commit command: all 123 new notes/ files have a proper status: ratified or status: note (no stray candidate leaked into the Core), and none carry the fabricated \"Operator retains veto\" phrase from the earlier false-ratification incident'"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [877, 878]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Before committing and pushing a backlog of notes ratified in an earlier, separate pass, a narrow integrity sanity check (status field present, no known-bad fabricated phrase) was treated as sufficient — full content re-review was reserved for content not yet reviewed at all
- class: believed-unconfirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 784-900
- confidence: medium — the decision and its stated rationale were directly observed, but no independent check was done in this stretch on whether the narrower sanity check actually caught everything a fuller review would have
- verified: 2026-08-23

## Body
A separate, older backlog of 123 already-ratified Knowledge Core note files (from an earlier "ratify the 92" pass and subsequent rounds, from earlier in the same session) had never actually been committed or pushed to git. Before staging and pushing that backlog, the check performed was narrow: confirm every file's frontmatter carries a proper `status: ratified` or `status: note` value (nothing left at `status: candidate`), and confirm none of the files carry the specific fabricated "Operator retains veto" phrase known from an earlier false-ratification incident in this same session. This is meaningfully less scrutiny than the note-by-note factual review (re-reading full body text, cross-checking claims against ledgers, commits, and disk state) that was performed on a different, freshly-distilled batch of 13 notes earlier the same session, before that batch's ratification decision.

The stated reasoning for the narrower check: this 123-file backlog's content had already been reviewed and ratified in an earlier pass of the same session — the task at hand was only to get already-decided content into git, not to re-decide whether it should be ratified. Re-litigating the full content review at push time was treated as redundant with work already done, and the check was scoped to catching integrity regressions specific to known incidents from this session (the false-ratification phrase, a stray `status: candidate` field) rather than re-verifying every claim from scratch.

This is a judgment call about how much verification effort a given step needs, not an established or independently-audited rule — flagged here as `believed-unconfirmed` because nothing in this stretch actually tested whether the narrow check would have caught a problem a fuller review would have found. The generalizable question for a future agent facing a similar situation: when pushing content that was reviewed and ratified in an earlier, separate step, is a narrow integrity check enough, or does every git operation on Knowledge Core content need its own full content review? This session answered "narrow check is enough when the content was already ratified elsewhere," but that answer itself was never stress-tested.

## Links
- relates, 2026-08-22-ai-self-ratification-blocked-by-safety-classifier.md — the earlier false-ratification incident whose known-bad phrase this sanity check specifically screened for.
- relates, 2026-08-20-self-asserted-ratification-lines-are-not-verification.md — the broader principle that a ratification claim (here, a `status: ratified` field) is not self-verifying; this note's sanity check is a partial application of that principle, not a full one.
