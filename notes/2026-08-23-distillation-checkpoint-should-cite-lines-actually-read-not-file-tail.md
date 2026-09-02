---
id: 2026-08-23-distillation-checkpoint-should-cite-lines-actually-read-not-file-tail
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i hereby ratify these notes\"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi, knowledge-core, distillation, checkpoint, governance, raw-archive]
sources:
  - ref: "Assistant advances the distillation checkpoint from 135 to 783 (not the file's then-current 810 lines), explaining it deliberately excluded the 27 newer turns nothing had actually read, to avoid overclaiming coverage"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [811, 815]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# When advancing a distillation checkpoint, record the last line the distillation agent actually read, not the raw file's current line count at the moment you update the checkpoint
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 784-900
- confidence: high — directly observed the deliberate choice and the reasoning given for it in the same turn
- verified: 2026-08-23

## Body
A background distillation agent was launched to read a raw session-transcript archive from a starting line through "the end," and it read up through line 783 before finishing and reporting its results. Because the raw archive is appended to continuously (every turn, including the agent's own completion report and the following discussion of its results, gets appended as new lines), by the time the operator said "mark the checkpoint distilled" the file had grown to 810 lines — 27 lines more than what the agent had actually read.

The checkpoint was advanced to 783, the line the agent actually finished reading, not 810, the file's line count at the moment of marking. The reasoning given: those 27 newer lines (the agent's own report being reviewed, a follow-up question, the operator's instruction to mark the checkpoint) had not been read or distilled by anything, and recording them as covered would overclaim coverage — a future distillation pass would then skip content nothing had actually processed.

General rule: a distillation or ingestion checkpoint should always be set from the actual last-processed position reported by the process that did the reading, never from the source file's line count read fresh at checkpoint-update time, because the two can diverge if anything (including the checkpoint-update conversation itself) appends to the same file in between.

## Links
- relates, 2026-08-21-distillation-reminder-built-option-a-deferred-on-broken-path.md, the broader distillation-checkpoint mechanism this specific update was operating within.
