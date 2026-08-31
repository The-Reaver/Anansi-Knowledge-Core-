---
id: 2026-08-07-extractor-agreement-kappa-bar-and-dawid-skene-weighting
type: spec
status: ratified
source: "Google Drive inbox capture, source chat not recorded in original note (source status: pinned Anansi note, answering whether proven formulas exist beyond Wilson); mined from candidates/2026-08-25/2026-08-07-quality-and-performance-formulas.md"
project: fleet
tags: [formulas, kappa, extractor-agreement, dawid-skene]
---

# Extraction reliability bar: Cohen's/Fleiss' kappa >= 0.70 on note-worthiness and category; below that, fix the rubric before pushing the batch

## Body

kappa = (p_o - p_e) / (1 - p_e), corrects for chance agreement between extractors (Cohen's kappa for two, Fleiss' kappa for more than two); use Krippendorff's alpha if raters skip items. BAR: kappa >= 0.70 on note-worthiness and category. When extractors differ in skill, use the Dawid-Skene EM model to weight by each agent's estimated reliability instead of plain majority vote.

## Links

- relates: 2026-08-07-note-quality-rubric-and-dedup-threshold
- relates: 2026-08-07-confidence-calibration-bar-brier-and-ece
