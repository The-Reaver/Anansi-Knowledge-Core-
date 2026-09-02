---
id: 2026-08-27-audit-report-quality-floor-mandate
type: ruling
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: fleet
tags: [mandate, audit-report, quality-floor, governance, reporting, operator-ruling]
sources:
  - ref: "Operator mandate issued directly, 2026-08-27, on uploading the 2026-07-24 OWC website advertising risk memo and its supplement: 'this is the standard of our audit report from now on... it is the absolute minimum quality of reporting I want under no circumstances can it be under this quality there must be above this quality do you understand this is a mandate'"
    reliability: high
    origin: "bridge-cse stag session, 2026-08-27; operator's own words, verbatim, in the session that placed the exemplar documents into the Core"
provenance:
  archive: research/knowledge-home/raw/2026-08-27-audit-report-standard-mandate.jsonl
  turns: [1, 3]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Every audit report the fleet produces must meet or exceed the OWC memo standard — an absolute floor, never a target

## Body
**Operator mandate, issued 2026-08-27, verbatim:** *"this is the standard of our audit report
from now on... I have uploaded the audit report standard it is the absolute minimum quality of
reporting I want under no circumstances can it be under this quality there must be above this
quality do you understand this is a mandate."*

**The exemplars** are the two documents now held at
`research/knowledge-home/reference/audit-report-standard/`: outside counsel's 2026-07-24 website
advertising-risk memo for a healthcare clinic, and its same-day supplement supplying
evidence-attributed rewrite language. Registered as mandate `audit-report-floor` in
`governance/mandates.json` (enforcement: contract).

**2026-08-28 correction — no individual's name belongs anywhere in this standard.** This note and
`reference/audit-report-standard/README.md` both originally named the memo's author and the named
clinic/physician it concerns. That material is attorney/client-privileged, marked "not for
distribution outside the clinic," and the operator ruled directly: the standard this mandate
establishes must never carry the lawyer's name or anyone else's. Both files are scrubbed to
generic descriptors as of this correction; nothing about the *structure* the mandate governs
depended on the identities, so nothing substantive changed. The two source PDFs themselves cannot
be redacted without destroying them as work product — they are kept local-only (see the README's
current caveat) rather than committed.

**Three things about how this mandate is worded, which matter for applying it:**

1. **It is a floor, not a target.** The operator said the standard is the *minimum* and that
   reports *"must be above this quality."* An audit report that merely matches the exemplars has
   met the bar, not exceeded it. "As good as the memo" is the failing grade, not the passing one.
2. **It is unconditional.** *"Under no circumstances"* admits no exception for a small scope, a
   quick turnaround, an internal-only audience, or a cheap model. If a report cannot be produced
   to this standard under the constraints given, the correct move is to **say so and renegotiate
   the constraints** — not to ship a thinner report and call it an audit.
3. **It is domain-general.** The exemplar is a legal memo, but nothing in the operator's wording
   limits the mandate to legal work. It governs security audits, code reviews, compliance
   findings, SEO/GEO audits, production-readiness sweeps — every report the fleet calls an audit.
   The exemplar's *structure* transfers even where its subject matter does not.

**The transferable content of the standard** — the twenty specific properties that make those
memos what they are — is specified separately in
`2026-08-27-audit-report-standard-the-twenty-properties`. This note establishes *that* the floor
exists and is binding; that note specifies *what* the floor consists of. Read both.

**Why the operator raised it now.** The mandate was issued in the same breath as *"this should
have been in the [Core]"* — the standard existed since July and had never been captured, so
sessions producing audit-shaped work had no way to know what bar they were being measured
against. That is the failure this mandate closes: not that the fleet's reports were bad, but that
the definition of good was held only in the operator's head.

**Self-check before delivering anything called an audit:** does it define its rating scale, state
what it did *not* examine, quote the actual offending material rather than describe it, cite
pinpoint sources, give concrete replacement language rather than "consider revising," rank
findings by urgency, and separate the author's judgement from the operator's decision? If any
answer is no, it is below the floor.

## Links
- specifies: 2026-08-27-audit-report-standard-the-twenty-properties
- registered-as: governance/mandates.json mandate `audit-report-floor`
- exemplars: research/knowledge-home/reference/audit-report-standard/
- relates-to: notes/2026-08-20-knowledge-core-first-mandate.md — the same failure mode one level
  up: durable material that existed but never reached the Core, so no agent could act on it.
- relates-to: 2026-08-27-green-unit-suite-does-not-detect-production-config-drift — an audit that
  reports "985/985 green" without stating what that does not cover is exactly the kind of
  incomplete-scope reporting this standard's not-evaluated rule forbids.
