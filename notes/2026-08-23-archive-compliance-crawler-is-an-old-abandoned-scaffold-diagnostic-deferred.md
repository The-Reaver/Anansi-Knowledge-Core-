---
id: 2026-08-23-archive-compliance-crawler-is-an-old-abandoned-scaffold-diagnostic-deferred
type: decision
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"ratify\"), given directly after the note was written and presented for review."
project: fleet
tags: [archive, compliance-crawler, compliance-intelligence, submodule, deferred-work, diagnostic]
sources:
  - ref: "Operator instructs: leave the compliance crawler archived, write a note that it's the old compliance crawler, defer a diagnostic (line 1375); assistant reports the characterization — stock create-next-app + shadcn/ui scaffold, default README/AGENTS.md, no crawler business logic found in this pass — and writes the note (line 1380)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1375, 1380]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Archive/compliance-crawler is an old, abandoned compliance-crawler attempt — a stock Next.js + shadcn/ui scaffold with no crawler business logic found, left archived; a future diagnostic should check for extractable value against the current Compliance Intelligence project

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), Claude Code chat session f810b6ef-6b06-41a9-a7e6-8dda137ce834
- confidence: high for what was directly checked (file listing, README, AGENTS.md, CLAUDE.md, a component list); medium for "no crawler logic anywhere" since this was a quick characterization pass, not an exhaustive audit of every file's full content or git history
- verified: 2026-08-23

`Archive/compliance-crawler` is a git submodule sitting under this repo's `Archive/` directory —
already flagged earlier this session as having roughly 30 modified files with unclear intent
(real work versus incidental build-tool noise). The operator's decision: leave it archived, do not
touch it now, but record what it actually is and defer a proper diagnostic to later.

Checked directly rather than assumed: the submodule's file listing, `README.md` (the unmodified
default `create-next-app` boilerplate text), `AGENTS.md` (the stock Next.js agent-rules notice
that scaffolding tools auto-generate), `CLAUDE.md` (a one-line reference to `AGENTS.md`), and the
component directory (`components/ui/*.tsx` — a standard shadcn/ui set: alert, badge, button, card,
dialog, input, label, progress, scroll-area, sheet, table) all point the same way: this looks like
an early, abandoned attempt at a compliance crawler that never got past initial scaffolding — a
fresh `create-next-app` project with a UI component library added, before being set aside and
archived. No crawler-specific business logic (scraping code, a rule engine, compliance-checking
logic of any kind) was found anywhere in this pass.

This is not a confident "there is nothing worth extracting" claim — it is a scaffold-only
characterization from a quick pass, not an exhaustive audit. The operator's own instruction
anticipates this distinction: come back later and run a real diagnostic specifically asking
whether anything in this archived project is worth extracting into the current Compliance
Intelligence product (`projects/compliance_intelligence`), unless whatever it might have offered
is already covered there. Given what was found today, the honest expectation going in is that this
diagnostic will likely conclude "nothing to extract, it was scaffold-only" — but that conclusion
should be reached deliberately by the diagnostic itself, not assumed now from a characterization
pass that wasn't looking for it specifically.

## Links
- relates, 2026-08-23-uncommitted-files-pile-triaged-and-committed-with-session-provenance.md, the earlier triage pass that first flagged this submodule's uncertain status and deferred it to the operator.
