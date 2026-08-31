---
id: forty-four-sourced-legal-documents-none-lawyer-reviewed-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) capability audit, 2026-08-31 — relayed by the operator into a recovery session; observed on the operator machine and NOT independently re-verified here"
project: cippe
tags: [compliance-intelligence, legal, liability, review-gate, client-facing]
supersedes: []
superseded_by: null
---

# Compliance Intelligence holds 44 sourced legal documents and not one has been lawyer-reviewed

## Body

The Compliance Intelligence corpus holds 44 sourced legal documents. **None has been reviewed
by a lawyer.** The index built from them, `atomic_notes.json`, is hand-maintained, and the
raw-to-notes converter has no deduplication — so the index also drifts from the corpus it
claims to represent, with files 42 through 44 not wired in at all.

Of every gap found across the eleven capabilities audited, this is the one carrying real
external liability. The others cost rework; this one can put an unreviewed legal claim in
front of a client under the fleet's name. Obtaining public government records needs no lawyer
— that part is sound and should continue. **Citing them as compliance guidance does.**

**The control is a hard gate: nothing client-facing may cite an unreviewed source.** Not a
warning, not a convention — a blocking check, because the failure mode is not a broken build
but a defensible-advice claim the fleet cannot actually defend. Reviewed status belongs in the
data as a field per source, so the gate can evaluate it rather than a human remembering.

Two smaller fixes follow: deduplication in the converter, and wiring 42–44 into the index so
it stops drifting.

## Links

- relates-to: a-mandate-can-name-an-enforcement-mechanism-that-does-not-exist-2026-08-31
- relates-to: a-gate-that-does-not-declare-fail-open-or-fail-closed-cannot-be-audited-2026-08-31
