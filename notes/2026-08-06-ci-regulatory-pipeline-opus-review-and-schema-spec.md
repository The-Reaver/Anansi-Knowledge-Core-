---
id: 2026-08-06-ci-regulatory-pipeline-opus-review-and-schema-spec
type: artifact
status: ratified
source: "this chat, 2026-08-05/06, Abad asked for the gameplan's own closing instruction, review by Opus model or higher, to actually run (source status: active)"
project: ci
tags: [compliance-intelligence, ci, regulatory-pipeline, opus-review, schema, operator-contribution]
---

# CI Regulatory Pipeline Gameplan Got an Independent Opus Review and a Follow-Up Engineering Spec

## Body

The CI regulatory pipeline gameplan (`reports/CI_REGULATORY_PIPELINE_GAMEPLAN_2026-08-05.md`) and its
lawyer-partnership addendum ended with an explicit instruction to be reviewed by Opus model or higher
before anyone builds on them. That review ran for real this session, dispatched to an Opus-tier agent
with the full gameplan and addendum text, tasked with an independent, non-rubber-stamp pass. Verdict:
approve to build, with five named conditions, filed at
`reports/CI_REGULATORY_PIPELINE_GAMEPLAN_OPUS_REVIEW_2026-08-05.md`. The review also flagged a real
process gap in how this project's own governance pattern works: the two "independent" Brain Trust
passes inside the original gameplan were the same model prompted twice, not genuinely independent
reviewers, and both missed the same six things, including a professional-conduct and fee-sharing risk
in the lawyer partnership and a completely unaddressed confidentiality question for his clients' data.

Three of the five conditions were engineering work and are now answered in a follow-up spec,
`reports/CI_REGULATORY_PIPELINE_SCHEMA_AND_CORRECTION_PATH_SPEC_2026-08-05.md`: an amended atom
schema (adds jurisdiction, a binding-vs-labeled-comparator flag, reviewer sign-off fields, and a link
from every delivered audit to the exact atom versions it cited), a labeling rule resolving a real
contradiction in the addendum (its scope rule excluded non-binding sources while its own seed list
included them, PubMed studies and professional-society guidance among them), and a real correction
path with a severity lane for anything already delivered to a client. Two conditions remain open and
are not engineering: written terms with the attorney, and a professional-conduct read from an outside
lawyer who is not the partner attorney. Neither is done.

## Links

- extends: 2026-08-05-anansi-inbox-wrong-location-corrected
- affects: 2026-08-06-ci-regulatory-pipeline-next-target-attorney-terms-first
