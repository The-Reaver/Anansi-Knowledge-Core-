---
id: 2026-08-23-lords-of-cian-canon-ledger-as-seed-for-archive-extraction-tool
type: finding
status: ratified
ratified: "2026-08-25 — anansi-promote skill run, 7/10 (novelty 2, evidence 1, actionability 1, generality 1, non-contradiction 2). Promoted WITH REVISION: the ledger half is now verified; the archive half remains an untested hypothesis."
project: lords-of-cian
tags: [lords-of-cian, canon-ledger, archive, extraction]
sources:
  - ref: "Structural observation raised in chat 2026-08-23; ledger-side figures verified by script 2026-08-25, archive-side still unvalidated"
    reliability: medium
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

# The Lords of Cian canon-ledger's hand-extracted, source-cited atomic facts are a ready-made seed set for the interactive archive's still-missing writer-reference-to-reader-facing extraction tool

- id: 2026-08-23-lords-of-cian-canon-ledger-as-seed-for-archive-extraction-tool
- type: finding
- status: ratified
- ratified: 2026-08-25 — anansi-promote skill run, 7/10 (novelty 2, evidence 1, actionability 1, generality 1, non-contradiction 2). Promoted WITH REVISION: the ledger half is now verified; the archive half remains an untested hypothesis.
- class: believed-unconfirmed
- source: this chat, 2026-08-23, connecting canon-ledger.json's method to a gap named in the operator's supplied archive game plan
- confidence: medium, a structural observation, not yet acted on or validated against the real archive schema
- verified: 2026-08-23
- tags: lords-of-cian, canon-ledger, archive, extraction
- project: lords-of-cian

## Body

The Lords of Cian interactive archive's reconciled game plan (see linked note) identifies a real gap: nothing in the described system extracts sections of Writer-Reference material (Character Codex, Arsenal Dossier, Tactical Architecture, Threat Blueprint entries) into reader-facing rows (chronicle entries, world briefings, archive documents). Without that tool, writer-reference content has no legitimate path to readers, and the plan names this P1-3, blocking the whole Book-1 unlock cascade.

`canon-ledger.json`, this project's canon-rules ledger, has been doing a version of exactly that extraction by hand all session: 510 locked rules as of 2026-08-23, each one an atomic, cross-checked, source-cited fact pulled from the project's Writer-Reference-equivalent source documents (Arsenal of Cian, the Maw Codex, and others already processed; the Character Codex zip and other writer-reference material still queued).

Once the archive's own extraction tooling (P1-3) exists and the repository sync (P0-1) has landed, the canon-ledger's already-vetted rules are a plausible seed set for populating World Briefings and Archive Documents, rather than something the archive needs to build from a blank slate. This is a structural observation raised in chat, not yet validated against the archive's real schema or acted on.

## Links

- relates: 2026-08-23-lords-of-cian-archive-repo-empty-and-possible-live-security-exposure
- relates: 2026-08-23-lords-of-cian-cult-network-execution-plan-complete

## Revision, 2026-08-25

The ledger-side claim is **verified**: `canon-ledger.json` is at v2.4 with exactly 510 rules across 21
batches and zero duplicate rule IDs, each rule carrying a source citation. The seed set genuinely exists
and is genuinely vetted.

The archive-side claim remains **unvalidated**. It has not been checked against the real archive schema,
and the repository inspection on 2026-08-25 could not even confirm which codebase the deployed archive
runs. Read this note as a well-founded proposal, not a plan of record; validating it requires the P0-1
repo reconciliation to land first.
