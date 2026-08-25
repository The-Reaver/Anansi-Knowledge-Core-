---
id: 2026-08-25-stars-citation-edit-draft
type: spec
status: applied
source: this chat, item 6 of the 9-Gate verdict's ratification preconditions.
project: fleet
tags: [brain-trust, 9-gate, stars-dreams, stars-docx]
---

# Applied: the citation-only text pointing STARS.docx to the new Gate ladder is now in the document

## Body

`2026-08-25-9-gate-brain-trust-verdict.md` ruled that STARS.docx stays unchanged in substance —
its composite index, floor cap, and ceiling-durability discount are untouched — and gains only a
citation noting that Augustin's fleet-wide onboarding/graduation status is tracked separately via
the Gate ladder.

**Applied text**, inserted directly after the document's introductory block ("Owner: Abad Morel"
/ "Reconstructed from The Training Brain's Locked Decisions Register...") and before "1. Roadmap
architecture":

> Note: this scale governs Augustin's CTO-training competency depth only. His fleet-wide
> onboarding/graduation status (whether he is cleared to operate, and at what checkpoint) is
> tracked separately under the fleet's Gate ladder — see the 9-Gate ruling,
> `2026-08-25-9-gate-brain-trust-verdict.md`. The two are independent: a Gate advance does not
> change a STARS score, and a STARS score does not change a Gate.

**Ratification authority**: STARS.docx's own header states "Owner: Abad Morel" — no separate
edit-approval clause exists anywhere else in the document (checked: every "sign-off"/"approv"/
"authority" mention in the text concerns TRL gate-reviewer certification of Augustin's training
progress, not approval of the STARS document itself). Abad Morel is the operator; asked directly
who signs off on STARS.docx edits, this is the answer the primary source itself gives.

**How the edit was made and verified**: unpacked the .docx, inserted a new `<w:p>` paragraph
matching the surrounding italic body-text formatting, repacked, and validated against the
original with the docx skill's schema validator (`+1 paragraph, all validations passed`). Visual
rendering (LibreOffice → PDF) was attempted but failed in this environment even on the
unmodified original file — an environment limitation, not evidence of a bad edit — so correctness
was confirmed instead by re-extracting the plain text of the edited file and checking the new
paragraph lands exactly between the intro block and "1. Roadmap architecture," with nothing else
in the document changed.

## Links

- extends, `2026-08-25-9-gate-brain-trust-verdict.md`, item 6 of its ratification preconditions.
