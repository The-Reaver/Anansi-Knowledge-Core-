---
id: 2026-08-07-quality-and-performance-formulas
type: note
status: candidate
source: "Google Drive inbox capture, source chat not recorded in original note"
project: fleet
tags: []
supersedes: []
superseded_by: null
---

# Quality and Performance Formulas for Harvesting and the Fleet

## Body

Pinned Anansi note. Purpose: answer the operator's question directly. Yes, there are proven formulas beyond Wilson. This note lists the ones worth implementing, what each one answers, the exact math, and the bar to gate on. No formula gives absolute certainty. What they give is a measured, defensible confidence with a stated threshold. Certainty comes from a formula clearing a bar plus a human gate on the high-impact items.

## The honest framing first
You cannot prove you found everything by looking only at what you found. You need a way to estimate what you missed. Two families of formula do this: capture-recapture estimates completeness, and agreement statistics estimate reliability. Together with retrieval metrics and calibration, they are the toolkit.

## 1. Did we catch everything? Completeness of a harvest
### Capture-recapture (Lincoln-Petersen, then Chao1)
Run two independent extraction passes over the same chat, ideally by two differently-prompted agents.
- a = notes found by pass 1
- b = notes found by pass 2
- m = notes found by both
Lincoln-Petersen estimate of the true total: N_hat = (a * b) / m. Completeness = (unique found) / N_hat.
Chao1: with f1 = notes seen by exactly one pass, f2 = notes seen by exactly two passes: S_hat = S_observed + (f1*f1)/(2*f2). The gap between S_hat and what you have is your estimated miss count. This answers "how do I know we got all the relevant details." You estimate it, you do not eyeball it.
### Loop-until-dry, made rigorous
Keep launching passes until K consecutive passes add nothing new (K = 2 or 3) OR Chao1 completeness crosses the bar.
BAR: estimated completeness >= 0.95 before a track is marked harvested. Log the estimate, never a silent "done."

## 2. Is each note good? A scored rubric, not one number
- Atomicity: exactly one claim per note.
- Provenance completeness (must be 100%): source, capture date, confidence, at least one typed link.
- Non-duplication: max cosine similarity to any existing note < 0.92. At or above, merge instead of add.
- Self-containedness: understandable alone, no dangling pronouns.
- Calibrated confidence (section 4).
Composite note score = weighted sum. BAR: enters the Core only above threshold and with provenance at 100%.

## 3. Are we parsing consistently? Extraction reliability
### Cohen's kappa (two extractors), Fleiss' kappa (more than two)
kappa = (p_o - p_e) / (1 - p_e). Corrects for chance agreement. BAR: kappa >= 0.70 on note-worthiness and category. Below that, fix the rubric, do not push the batch. Krippendorff's alpha if raters skip items.
### Dawid-Skene
When extractors differ in skill, use the Dawid-Skene EM model to weight by each agent's estimated reliability instead of plain majority vote.

## 4. Is the confidence honest? Calibration
- Brier score = mean((predicted_probability - actual_outcome)^2). Lower is better.
- Expected Calibration Error (ECE): bin by stated confidence, compare average confidence to actual accuracy per bin.
BAR: track Brier and ECE per extractor. Recalibrate when ECE drifts past a set band.

## 5. Is the Core useful? Retrieval quality
Run against a fixed eval set of query-and-expected-note pairs. Precision@k, Recall@k, F1 = 2PR/(P+R), MRR, nDCG@k, MAP. The benchmark subsystem already computes recall. BAR (tune with data): Recall@10 >= 0.90, nDCG@10 >= 0.80. This is also how you defend the local embedding-model choice: pick the model that wins on this set.

## 6. Which agents and strategies are working? Fleet performance
- Wilson score interval (already in use): rank agents on the confidence-adjusted lower bound of success rate, not raw average.
- Elo / TrueSkill: skill rating for head-to-head approaches.
- Multi-armed bandit (UCB1 or Thompson sampling): route more work to better performers while still exploring. UCB1 picks the arm maximizing mean_i + sqrt(2*ln(total)/pulls_i).
- Agent reliability = its kappa against the human validator over time.

## 7. The auto-approve rule
Collect votes from N agents, weight each by its Wilson-scored reliability. Auto-accept only if weighted agreement >= 2/3 AND the note clears the section-2 quality bar. Below that, or any high-impact rule, routes to the human review queue.

## In place vs new to build
- In place: Wilson, the benchmark recall metric, the human review queue with confidence and diff.
- New (small, gated): two-pass capture-recapture harvester with Chao1 gate, note-quality rubric scorer with 0.92 dedup, kappa reporting, Brier/ECE tracking, full retrieval metric set on a fixed eval set, weighted-consensus auto-approve.

## Close-out checklist per track
- Estimated completeness (Chao1) >= 0.95
- Extractor agreement kappa >= 0.70
- Every accepted note: provenance 100%, dedup cosine < 0.92, above composite quality threshold
- Confidence calibrated (Brier and ECE within band)
- High-impact notes approved in the review queue
- Coverage estimate and any dropped material logged, never a silent "done"

## Links

(none recorded in source)
