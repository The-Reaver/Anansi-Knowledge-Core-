---
id: 2026-08-21-sonnyny-one-gb-bloat-mostly-images-and-history
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision, provenance turns range extended to include turn 46 (source of the Sonny-Python data-outputs detail). Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, sonnyny, repo-bloat, git-history, images]
sources:
  - ref: "Turn 44 (the live diagnostic reply) confirms the core split — ~1 GB total, ~2.5 MB real code, ~204 MB unoptimized images in the working tree, ~800 MB dead weight in history; the finer detail (63 images over 1 MB) and the separate Sonny-Python data-outputs paragraph (pipeline_logs.json, scraped CSVs) are confirmed only in turn 46, the assistant's later note-extraction pass. Citation range corrected on Brain Trust review to include turn 46."
    reliability: high
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [44, 46]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# SonnyNY's ~1 GB repo size was almost entirely unoptimized images and dead git history, not code
- id: 2026-08-21-sonnyny-one-gb-bloat-mostly-images-and-history
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, based on a recursive git-tree pass with per-blob sizes
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, sonnyny, repo-bloat, git-history, images

## Body

The ShopOnlineNewYork `SonnyNY` repository measured about 1 GB on disk despite containing only roughly 2.5 MB of actual application code. A git-tree metadata pass (no cloning) attributed the bloat to roughly 204 MB of unoptimized images committed under `src/` in the current working tree (503 image files, 63 of them over 1 MB, including one 7.6 MB PNG), plus roughly 800 MB of dead weight left over in git history from artifacts committed and later removed but never purged from history. Separately in the same pass, the `Sonny-Python` repo was found committing generated pipeline outputs as if they were source code — a 12.5 MB `pipeline_logs.json` and several scraped CSV files (`scraped_products.csv`, `alibaba_*.csv`) — which should be gitignored or moved to external data storage rather than version-controlled. Recommended remediation for the image bloat was moving large media to a CDN or Git LFS, compressing/resizing images, and pruning history.

## Links
- relates-to, 2026-08-21-metadata-only-github-repo-diagnostic-technique.md, the technique used to find this without cloning.
