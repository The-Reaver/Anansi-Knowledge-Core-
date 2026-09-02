---
id: 2026-08-23-uncommitted-files-pile-triaged-and-committed-with-session-provenance
type: decision
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"I ratify\"), given directly after the note was written and presented for review."
project: fleet
tags: [git, commit-hygiene, provenance, session-tracking, governance]
sources:
  - ref: "Operator: \"what is your advice on what to do with them and what are they specifically and simply\", followed by the assistant's per-item triage table (launch.json, Archive/compliance-crawler submodule, two SESSION_HANDOFF files, design brief, 3 PDFs) and recommendations; operator: \"I'll go with your advice make a note on all of them so they know what chat and what session made this change\"; assistant confirms: \"Committed (b0a89ca): .claude/launch.json, both SESSION_HANDOFF_*.md files, and the design brief... Note written, documenting the whole triage with explicit session provenance — the full chat session id (f810b6ef-6b06-41a9-a7e6-8dda137ce834).\""
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1350, 1366]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A pile of unrelated uncommitted files sitting since earlier in this session was triaged item-by-item and committed, with explicit session provenance recorded on the operator's direct request

- id: 2026-08-23-uncommitted-files-pile-triaged-and-committed-with-session-provenance
- type: decision
- status: ratified
- ratified: 2026-08-23 — operator directly ratified via explicit operator instruction ("I ratify"), given directly after the note was written and presented for review.
- class: confirmed
- source: this session (STAG repo, 2026-08-23), Claude Code chat session f810b6ef-6b06-41a9-a7e6-8dda137ce834
- confidence: high, each item was directly inspected before a recommendation was given, and the operator's own instruction to proceed is recorded verbatim
- verified: 2026-08-23
- tags: git, commit-hygiene, provenance, session-tracking, governance

## Body
Six unrelated files had been sitting uncommitted in the `stag` working tree since earlier in this
session, flagged repeatedly in status checks but left untouched pending the operator's intent.
When the operator finally asked what they specifically were and what to do with them, each was
investigated directly rather than guessed at: `git diff`/`git status` for the tracked ones, direct
file reads for the untracked ones, and an attempted PDF text extraction for the three PDFs (no
PDF-reading tool was available in this environment, so those three could not be characterized
beyond filename and metadata).

Findings and recommendation given, item by item:
- `.claude/launch.json` — a small, additive browser-preview launch-config entry for the A-Game
  Sports rebuild project. Recommended: commit.
- `Archive/compliance-crawler` (a git submodule) — roughly 30 modified files, all generic
  scaffolding boilerplate (shadcn/ui components, Next.js config, favicon assets). Sitting under
  `Archive/`, meaning the project itself is retired/inactive. Could not distinguish intentional
  work from incidental noise left by a build tool. Recommended: leave alone, ask first — this one
  was NOT committed.
- Two `SESSION_HANDOFF_*.md` files (2026-08-21, 2026-08-22) — real, substantive session handoff
  documents matching this repo's own established close-out convention. Recommended: commit.
- `references/design/briefs/design-brief-2026-08-22.md` — a real draft design-research brief,
  already self-labeled "DRAFT — not authoritative until Amaya folds it in." Recommended: commit,
  since it doesn't overstate its own authority.
- Three PDFs (`stag-geo-live-preview-demo.pdf`, `stag-platform-dashboard.pdf`,
  `stag-site-generator-gameplan.pdf`) — content unreadable in this environment; only filenames and
  a shared creation-time cluster (2026-08-20) were available as evidence. Recommended: operator's
  call, not committed.

The operator accepted the recommendation as given ("I'll go with your advice") and separately
asked for explicit session/chat provenance to be recorded on the change, distinct from the routine
"this session" phrasing every other note already carries — specifically so a future reader can
tell which chat session made this particular commit. The four approved files were committed as
`b0a89ca`, with both the commit message and this note citing the full session id
(`f810b6ef-6b06-41a9-a7e6-8dda137ce834`) directly, not just a date.

## Links
- relates, 2026-08-23-antigravity-dispatch-queue-found-dormant-11-plus-days.md, an earlier finding
  in the same broader "what's actually pending" advisory thread this triage was part of.
