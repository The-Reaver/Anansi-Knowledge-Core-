---
id: 2026-08-13-meridian-naming-lock-finalized-and-session-handoff
type: note
status: ratified
ratified: "2026-08-14, same-session light pass (Mandate 8 / stag-closeout Step 4) -- a session handoff recording an already operator-confirmed lock (\"Confirmed, lock it in as its own formal lock\") plus operational notes, no further decision weight requiring full Brain Trust seats"
project: lords-of-cian
tags: [lords-of-cian, session-handoff, canon-lock, master-canon-decisions, meridian, google-docs]
sources:
  - ref: "MASTER CANON DECISIONS.docx (Drive Lore Vault, fileId 1NLOAu4Qh_ICV30Yd9tKVoBpX2GNBRiBb), new section \"SESSION LOCKS — ARCHON MERIDIAN AND THE MERIDIAN NAME (August 13, 2026)\""
    reliability: high
    origin: direct edit, this session, verified via download_file_content decoded through python-docx
  - ref: "Operator confirmation, 2026-08-13: \"Confirmed, lock it in as its own formal lock.\""
    reliability: high
    origin: chat message, this session
  - ref: "research/knowledge-home/lords_of_cian/2026-08-13-meridian-naming-archon-un-ra-leads-the-compact.md, this room, upgraded type:finding->ruling, evidence_state:SUPPORTED->SETTLED"
    reliability: high
    origin: direct edit, this session
provenance:
  archive: research/knowledge-home/raw/2026-08-12-lords-of-cian-room-intake.jsonl
  turns: [39, 44]
risk_class: B
evidence_state: CORROBORATED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Meridian naming lock finalized in MASTER CANON DECISIONS.docx — session handoff for whoever picks this up next

## What's settled, as of this session

The operator confirmed the Meridian-naming recommendation as its own formal lock ("Confirmed,
lock it in as its own formal lock"). `MASTER CANON DECISIONS.docx` now carries a standalone
"SESSION LOCKS — ARCHON MERIDIAN AND THE MERIDIAN NAME (August 13, 2026)" section: Archon Meridian
is Archon Un Ra, T.D.K.'s hidden son, placed under a name that is an unknowing echo of his father
Anu Un Ra's own ancient identity as the Ash-King of Broken Meridian and creator of the Meridian
Engine. This resolves "DECISION 2: MERIDIAN NAMING CONNECTION" (Option A, deliberate lineage) from
the operator's own "SECTION C: CONTRADICTIONS AND CONFLICTS" document. The embedded correction
note that previously carried this reasoning inline in the REXMAR LINEAGE section was trimmed to a
short pointer at the new section rather than restating it.

Synced everywhere this fleet tracks Lords of Cian state: `claude/master-to-do-list.md` (Claude
Project), the STAG room note (upgraded `finding`/`SUPPORTED` → `ruling`/`SETTLED`), the room's
README, and the raw intake log (now 44 turns, up from 42).

## What's still open (unaddressed by this lock, from the same SECTION C document)

- **Decision 1 — Verehimu Crown-Scar timing.** Was the Crown-Scar given to Verehimu before, during,
  or after his betrayal of T.D.K.? Fully open, no recommendation drafted yet.
- **Decision 3 — Anu Un Ra dossier integration scope.** How deep should the full "DOSSIER: ANU UN
  RA" backstory (Broken Meridian, the Meridian Engine, the Ionic Rite, the Exchange Protocol,
  death-tech, the warbody, the 16-era timeline) integrate into the wider Codex? Fully open.

## Also still open, unrelated to the Meridian thread (carried from earlier in this session)

- Whether **Guacanagarix Rexmar** (the ~950-year-old "Truth-Teller" from the Lords of Cian notes)
  is the uncle character the operator actually means — "Varek Rexmar," the name previously in this
  fleet's records, was confirmed this session to be a fabrication with no source anywhere in canon.
  See `2026-08-12-varek-rexmar-was-fabricated-corrected-to-guacanagarix.md`, this room.
- Book 1 structural outline confirmation.
- The Kanja psychological profile file's placement in the Drive Lore Vault (drafted and delivered
  2026-08-09, never uploaded to Drive — needs either the operator's saved copy or authorization to
  rebuild from the now-corrected canon).
- Whether the operator wants the Atlas's own region labels renamed to match the locked
  Jicome/Sovereign Trust Domain naming (a cosmetic follow-up, not required — both names already
  coexist by the existing lock).

## Operational note for whoever edits MASTER CANON DECISIONS.docx next

This session hit three live-editing failure modes worth knowing before touching this file again:

1. **Ctrl+H Find-and-Replace silently failed at least once** — the Replace-all button reported
   success but the document text was unchanged, confirmed only by a full re-download and re-parse.
   Manual text selection (click at the start, `shift+Down` N times to cover N lines, `shift+End`)
   proved more reliable than Find-and-Replace for this document in this session.
2. **A `type` action that reports a CDP timeout can still have fully succeeded.** Don't treat a
   timeout error as a failure signal on its own — verify the actual document state before retyping,
   or you risk duplicating content (see next point).
3. **Google Drive's file-export cache lags the live Google Doc edit by up to ~60 seconds.**
   `download_file_content` returned byte-identical (stale) output across two calls made about a
   minute apart, immediately after an edit. The fix: check `get_file_metadata`'s `modifiedTime`
   and `fileSize` first, and don't trust a download until those have visibly advanced past the
   edit's own timestamp. This is a general lesson, not specific to this document — see
   [[2026-08-13-google-drive-export-cache-lags-live-docs-edits]], `research/knowledge-home/notes/`
   (or wherever that candidate lands once promoted), for the fleet-wide version of this lesson.

## Who wrote this

Written directly by a Cowork session (this session), not a fleet agent — per this room's existing
convention, this and the other notes in `lords_of_cian/` have not been through a Brain Trust or AJ
ratification pass. They carry the weight of a direct, operator-confirmed record, not a ratified
fleet decision.

## Links

- lives in, `research/knowledge-home/lords_of_cian/README.md`, this room's hub note.
- supersedes the "not yet a formal lock" status of, `2026-08-13-meridian-naming-archon-un-ra-leads-the-compact.md`, this room.
- generalizes into, [[2026-08-13-google-drive-export-cache-lags-live-docs-edits]], the fleet-wide lesson from this session's verification trouble.
- recorded in, `MASTER CANON DECISIONS.docx` (Drive Lore Vault), the canon of record.
- tracked in, `claude/master-to-do-list.md` (Claude Project).
- sourced from, `research/knowledge-home/raw/2026-08-12-lords-of-cian-room-intake.jsonl`, turns 39 to 44.
