---
id: 2026-08-22-evaluate-ai-generated-architecture-docs-against-confirmed-gaps-not-own-claims
type: decision
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [methodology, ai-generated-content, scoping, evaluation-process, compliance-intelligence]
sources:
  - ref: "Archive lines 301-323: the operator's verbatim three-question rubric instruction (does it solve a confirmed gap, is it appropriately scoped, is it buildable now — build now/build simplified/defer/discard) followed by the assistant's direct AI-authorship analysis of both uploaded documents against that rubric."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [301, 323]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Evaluating an AI-generated architecture document: check each proposed piece against a real, already-confirmed gap and the smallest buildable fix, not against the document's own framing or scope

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly executed against two real uploaded documents in-session, per explicit operator instruction, with the resulting four fixes built and tested
- verified: 2026-08-22

## Body
Two operator-uploaded documents proposing a "verifiable legal ingestion" architecture for Compliance Intelligence were evaluated under an explicit three-question rubric per component: does it solve a gap already confirmed real in the actual codebase, is the proposed approach appropriately scoped for what's actually needed (not gold-plated infrastructure for a problem a much smaller fix solves), and is it buildable now — reporting build now / build simplified / defer / discard per component before writing any code. Both documents showed clear AI-authorship tells worth naming plainly rather than treating as neutral specs: one opened by describing itself as "a refined and reproduced technical document," admitted its own gaps, was heavily hedged ("potentially leveraging," "could leverage"), and padded its citation list with clearly unrelated material; the other read as a raw, unedited AI chat export, complete with the assistant's own meta-commentary left in and an unrelated YouTube transcript accidentally spliced into an unrelated section.

Applying the rubric to each of roughly 17 combined proposed components (ML-based document classification, cryptographic provenance/PKI, a knowledge graph, workflow orchestration engines, multi-jurisdiction live ingestion, etc.) discarded the large majority as solving problems the actual system doesn't have (no bulk document ingestion exists to classify; no external third party needs cryptographic proof; atom review already happens via git PR + Brain Trust, a human process that doesn't need a state-machine engine). Two ideas mapped onto gaps independently already confirmed real (no citation-authority tiering existed; atom edits had zero version history) and were kept, but radically descoped from the documents' proposed scale (blockchain/DID/Verifiable-Credentials infrastructure, event-sourcing, Temporal.io orchestration) down to a plain enum field plus a render-gate conditional, and a script reading real `git log` output plus a commit-discipline fix — using git's already-free capabilities instead of building new infrastructure to duplicate them.

General method, reusable beyond this instance: when handed an AI-generated planning/architecture document (regardless of how detailed or code-concrete it looks), don't evaluate it as a spec to implement — evaluate each proposed piece independently against what the real system's confirmed gaps actually are, and prefer the smallest change that closes the confirmed gap using infrastructure already available, discarding anything the document introduces to solve a problem that was never actually confirmed to exist.

## Links
- relates, 2026-08-22-ci-q2-emergency-security-fix-shipped-auth-signoff-authority-tier-history.md — the four concrete fixes this evaluation method produced.
