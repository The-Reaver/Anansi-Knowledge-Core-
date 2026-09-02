---
id: 2026-08-30-six-oluwole-design-briefs-piled-up-with-zero-folded-into-design-principles
type: finding
status: ratified
ratified: "2026-08-30 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
class: confirmed
source: "Oluwole weekly design-research scheduled task, 2026-08-30 run and closeout; direct filesystem/git verification in the same session"
project: fleet
tags: [oluwole, design, design-principles, knowledge-core, harvest-gap, amaya, process-verification]
sources:
  - ref: "git log --oneline -- references/design/DESIGN_PRINCIPLES.md returns exactly one commit (fccae86, the file's creation); stat shows mtime 2026-07-24 20:43:11, unchanged since; ls references/design/briefs/ lists six dated briefs (2026-07-24, 2026-07-25, 2026-08-01, 2026-08-08, 2026-08-22, 2026-08-29); grep of .anansi_embeddings.json for 'design-brief' and 'DESIGN_PRINCIPLES' returns zero hits for both"
    reliability: high
    origin: "direct filesystem and git inspection, 2026-08-30, same session that produced design-brief-2026-08-29.md"
provenance:
  archive: research/knowledge-home/raw/2026-08-30-oluwole-design-brief-and-closeout.jsonl
  turns: [1, 17]
risk_class: B
evidence_state: SUPPORTED
next_review: 2026-11-30
classified: 2026-08-30
---

- class: confirmed
- confidence: high — verified directly via git log, file mtime, and a grep of the live embeddings file, not inferred or operator-relayed
- verified: 2026-08-30 (author, direct filesystem/git inspection); 2026-08-30 (independent adversarial-review subagent, CONFIRMED with one correction applied — the review itself is logged at `research/knowledge-home/raw/2026-08-30-oluwole-design-brief-and-closeout.jsonl` turns 10–11, not merely asserted here); 2026-08-30 (independently re-derived a third time by a 4-seat Brain Trust panel — Amaya, Oluwole, Celestina, Jasiah — convened per the operator's explicit instruction to let the Brain Trust decide the pipeline fix; unanimous RATIFY on this note's Q3. Full seat verdicts and the ruling: `reports/DESIGN_BRIEF_PIPELINE_BRAIN_TRUST_RESULTS_2026-08-30.md`, ledger row in `reports/STAG_BRAIN_TRUST_LEDGER.md`. Note: Jasiah, the QA seat, independently spot-checked this note and could not find a trace of the adversarial-review claim in the repo at the time it checked — a fair catch, since that review had happened in the live session but had not yet been archived; this correction closes that gap by pointing to the specific archive lines rather than re-asserting the claim).

# Six weekly Oluwole design-research briefs have accumulated since 2026-07-24 with zero findings folded into DESIGN_PRINCIPLES.md — the Amaya review step this pipeline depends on has not run once

## Body

`references/design/DESIGN_PRINCIPLES.md` states its own growth mechanism: "Oluwole researches continuously... and Amaya folds accepted findings into these tokens and rules." Checked directly this session: `git log --oneline -- references/design/DESIGN_PRINCIPLES.md` returns exactly one commit, the file's original creation (`fccae86`), and its mtime is `2026-07-24 20:43:11`, unchanged since. In that same span, six dated briefs have been written to `references/design/briefs/`: 2026-07-24, 2026-07-25, 2026-08-01, 2026-08-08, 2026-08-22, and 2026-08-29 (this session's). Every one carries the required line "DRAFT — Vanguard research. Not authoritative until Amaya folds accepted findings into DESIGN_PRINCIPLES.md." Only three of the six (08-08, 08-22, 08-29) actually end with a "Recommended next steps for Amaya" list; the first three (07-24, 07-25, 08-01) end with a "Sources" section only, no explicit recommendations block. Across the three briefs that do carry concrete recommendations, a line-by-line check of DESIGN_PRINCIPLES.md's current tokens and rules against every listed recommendation (OKLCH tokens, dark-mode set, weight-band shift, `font-feature-settings`, `section-gap` token, pill radius, icon stroke/grid, settings-page pattern, toast rules, progressive-loading sequence, workspace-switcher pattern, and more) found zero adoption, even partial — the one surface-level echo (both the original 07-24 file and the 08-22 brief mention "shadow as border") predates any brief with recommendations, since it's already in the file's original 07-24 content, not something folded in afterward. (Note also the roughly two-week gap between 08-08 and 08-22 — no brief dated 08-15 — a minor cadence miss on top of the larger issue.)

Separately, verified this session that no design brief is embedded in the Anansi Knowledge Core: `grep -o "design-brief" .anansi_embeddings.json` and the same for `"DESIGN_PRINCIPLES"` both return zero matches. That part is correct behavior, not a bug — per `docs/adr/0005-two-store-memory-archive-and-core.md`, research artifacts like these are drafts pending a human-equivalent review gate before they'd even be candidates for the notes/Core pipeline, and the Core's own embedding pipeline (Phase 2, `specs/SPEC_KNOWLEDGE_CORE.md`) "is still not started" fleet-wide regardless. This is a different failure class from `2026-08-21-hbot-usa-sonners-research-ran-2026-08-07-but-never-reached-the-knowledge-core` (research that should have been routed into the Core and simply wasn't) — here the intended consumer of the research is a named role (Amaya) acting on a named file (DESIGN_PRINCIPLES.md), and the gap is that the role has never executed a single review across six cycles.

The actionable risk: the "how this library grows and stays modern" mechanism DESIGN_PRINCIPLES.md describes is, as of this check, entirely unproven — there is no evidence any of the ~60+ cumulative findings across six briefs has ever been consumed, evaluated, or rejected. The research is real and well-sourced (each brief cites live URLs per finding), but the loop that is supposed to close on it has not closed once in five weeks.

## Links
- relates-to: 2026-08-21-hbot-usa-sonners-research-ran-2026-08-07-but-never-reached-the-knowledge-core — same class of finding (research produced, not consumed downstream), different mechanism (a named reviewer role vs. Core harvesting)
- relates-to: 2026-08-27-reload-wiped-the-embedding-cache-so-semantic-search-could-never-become-ready — unrelated bug, but establishes the pattern of verifying claims about Core state directly rather than assuming; this note follows the same discipline (checked the embeddings file and git history directly rather than assuming the briefs were or weren't embedded)
- see-also (flagged by the 2026-08-30 adversarial review, not independently deep-checked in this note): `references/patterns/design-tokens-states-accessible-craft.md` is marked "Promoted from `references/research/design-advanced-2026-07-26.md`" with owner skill Amaya, but that promoted file is itself still headed "DRAFT — pending Amadeus review" (a different named reviewer) and was also never folded into DESIGN_PRINCIPLES.md. Suggests the broader research-to-DESIGN_PRINCIPLES fold-in gate may be stalled fleet-wide, not just for Oluwole's six weekly briefs — worth its own dedicated note and check in a future session rather than asserted here as confirmed.
