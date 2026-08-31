---
id: 2026-08-07-harvest-completeness-bar-capture-recapture-chao1
type: spec
status: ratified
source: "Google Drive inbox capture, source chat not recorded in original note (source status: pinned Anansi note, answering whether proven formulas exist beyond Wilson); mined from candidates/2026-08-25/2026-08-07-quality-and-performance-formulas.md"
project: fleet
tags: [formulas, completeness, chao1, capture-recapture, harvest]
supersedes: []
superseded_by: null
---

# Harvest completeness bar: two-pass capture-recapture / Chao1 estimate, completeness >= 0.95 before a track counts as harvested

## Body

You cannot prove you found everything by looking only at what you found — you need a way to estimate what you missed. Run two independent extraction passes over the same source, ideally by two differently-prompted agents. Lincoln-Petersen estimate of the true total: N_hat = (a * b) / m, where a = notes found by pass 1, b = notes found by pass 2, m = notes found by both; completeness = unique found / N_hat. Chao1, with f1 = notes seen by exactly one pass and f2 = notes seen by exactly two: S_hat = S_observed + (f1*f1)/(2*f2); the gap between S_hat and what you have is the estimated miss count — estimated, not eyeballed. Loop-until-dry, made rigorous: keep launching passes until K consecutive passes (K = 2 or 3) add nothing new, OR Chao1 completeness crosses the bar. BAR: estimated completeness >= 0.95 before a track is marked harvested; log the estimate, never a silent "done."

## Links

- relates: 2026-08-07-note-quality-rubric-and-dedup-threshold
