---
id: 2026-08-07-confidence-calibration-bar-brier-and-ece
type: spec
status: ratified
source: "Google Drive inbox capture, source chat not recorded in original note (source status: pinned Anansi note, answering whether proven formulas exist beyond Wilson); mined from candidates/2026-08-25/2026-08-07-quality-and-performance-formulas.md"
project: fleet
tags: [formulas, calibration, brier-score, ece]
supersedes: []
superseded_by: null
---

# Confidence calibration bar: track Brier score and Expected Calibration Error per extractor, recalibrate when ECE drifts past a set band

## Body

Brier score = mean((predicted_probability - actual_outcome)^2), lower is better. Expected Calibration Error (ECE): bin by stated confidence, compare average confidence to actual accuracy per bin. Together these answer whether a stated confidence is honest, not just present.

## Links

- relates: 2026-08-07-extractor-agreement-kappa-bar-and-dawid-skene-weighting
