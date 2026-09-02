---
id: 2026-08-27-audit-report-standard-the-twenty-properties
type: spec
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: fleet
tags: [audit-report, standard, reporting, spec, quality-floor, methodology]
sources:
  - ref: "Structural analysis of the 2026-07-24 OWC website advertising risk memo (606 lines extracted) and its supplement (457 lines), read in full by the harvesting session via pdftotext -layout; properties abstracted from the documents themselves, not from a description of them"
    reliability: high
    origin: "bridge-cse stag session, 2026-08-27, on the operator's mandate that these documents set the fleet's audit-report floor"
provenance:
  archive: research/knowledge-home/raw/2026-08-27-audit-report-standard-mandate.jsonl
  turns: [2, 3]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The twenty properties that make the OWC memo an audit-report standard, stated so they transfer to any domain

## Body
These are abstracted from the exemplars at
`research/knowledge-home/reference/audit-report-standard/`, which
`2026-08-27-audit-report-quality-floor-mandate` makes binding. Each property is stated
domain-generally, with the memo's own execution shown so the abstraction stays anchored.

### A. Scope and calibration (before any finding)

1. **A defined rating scale, published up front, with a written meaning per level.** The memo
   uses an MPA-style scale — NC-17 / R / PG-13 / PG / G — and defines each ("highly risky and, in
   my opinion, unlawful on its face" … "no meaningful risk; not illegal at all"). The scale is
   chosen to be *intuitive to the reader*, not to the author's profession. Severity words like
   "critical/high/medium" are only meaningful if you say what they mean.
2. **An explicit scope statement: what was examined, against what, and by whom.** "I have
   reviewed every page of the Website that you provided to me, together with the clinic's current
   and new patient consent forms," measured against a named list of authorities.
3. **A default rule that closes the silence gap.** *"If I have not specifically addressed language
   in this memo, you may assume that I believe the risk … is low (PG or better)."* Without this,
   silence is ambiguous — the reader cannot tell "reviewed and fine" from "never looked at."
   **This is the single most-skipped property and one of the most valuable.**
4. **An overall verdict, plus the verdict after remediation.** "Overall rating … today: **R** …
   If the specific fixes recommended in this memo are made, I believe the Website as a whole
   would come down to **PG**." The reader learns both where they stand and what the work buys.
5. **A named-and-dated authority section with pinpoint citations.** Not "FTC rules" but
   `16 C.F.R. § 255.2(a)`; not "Iowa law" but `Iowa Code § 148.6(2)(a)` and
   `Iowa Admin. Code r. 653—23.1(17)`; with amendment dates where they matter ("most recently
   amended effective May 21, 2025").
6. **Binding authority separated from persuasive guidance.** An entire subsection titled *"Guides,
   not binding rules."* The audit says which standards *govern* and which merely *inform* — and
   then explains why the non-binding ones still matter ("language that would be a violation in
   five states … is exactly the kind of language a hostile investigator will characterize as
   misleading").

### B. The findings themselves

7. **A findings-at-a-glance table: every item, every rating, on one screen.** Scannable by
   someone who will not read the body.
8. **Findings ordered by severity, in labelled tiers.** "NC-17 Items — Take These Down or Rewrite
   Them Now," then R, then PG-13, then PG and G. Tier headings carry the required action.
9. **Quote the offending material verbatim; never paraphrase it.** The memo reproduces the exact
   sentences — *"is a permanent treatment for many kinds of chronic pain," "ideal therapeutic
   molecule."* A paraphrased finding cannot be verified by the reader and cannot be searched for
   in the artifact.
10. **Say specifically why it fails, naming the rule it fails under.** Not "this is risky" but
    "'Permanent' is a guarantee … Wisconsin's rule makes representing that a condition 'can or
    will be permanently cured' per se unprofessional conduct; Illinois bans guarantees outright;
    ASPS bans predictions … and Iowa's 653—23.1(17) reaches the same conduct."
11. **Supply concrete replacement material, not an instruction to fix it.** Every serious finding
    carries a *"Consider instead:"* block containing publishable copy. The supplement goes
    further and writes the finished replacement for every R and NC-17 item. **"Consider
    revising this section" is not a finding; it is a deferral.**
12. **Rank by real-world consequence, not by tidiness.** The memo's severity reflects what an
    actual adversary would act on first, informed by named precedent with outcomes: *FTC v.
    Regenerative Medical Group* ($3.31M), the Stem Cell Institute of America case ($5.1M).
    Consequence is quantified where it can be.

### C. Honesty properties (what separates this from a good report)

13. **An explicit not-evaluated section, marked as unsafe rather than absent.** Section VI:
    *"I have not evaluated any of this linked media content, and until I do, it is not to be
    considered safe."* Unreviewed scope is stated as live exposure, not omitted. **An audit that
    silently skips something reports a false all-clear over that area.**
14. **The recommended remedy's own limits stated before the remedy is given.** The supplement
    opens by explaining where attributed quotation *fails* — the net-impression rule, the raised
    bar of an establishment claim, cherry-picking — and only then supplies the technique.
    Handing over a fix without its failure modes invites confident misuse.
15. **A triage of where the fix works, partly works, and does not work.** A three-bucket table
    with a reason per row: *"Yes — strongest case," "Partly, heavily hedged," "No — this is the
    important one."* Refuses the pretence that one remedy covers everything.
16. **State what was deliberately left out, and why.** *"Note what this rewrite deliberately
    leaves out: stroke, diabetic peripheral neuropathy, and TBI/post-concussion"* — with the
    evidence reasoning for each omission. Silent omission and reasoned omission look identical
    on the page unless you say which one it is.
17. **Anti-cherry-picking: every favourable citation carries its own counter-evidence.** Each
    quoted study is paired with that study's stated limitation, and where the literature is split
    the split is disclosed *on the face of the page.*
18. **Evidence attributed to named, independently verifiable sources.** Author, journal, year,
    and a stable identifier (PMID) — 25 of them, listed in full. Plus a standing instruction to
    the implementer: *"confirm every quotation letter-for-letter against the study's abstract
    before it is published."*

### D. Making it act

19. **A priority list in urgency order, each item tagged with its severity.** Nine numbered
    actions, each carrying its rating. Ends with the process fix that prevents recurrence —
    *"route all future edits … through this office before publication … the one that would have
    prevented every item in this memo."* **A finding list without an ordered action list makes
    the reader do the triage.**
20. **A stated internal-consistency check, and a clean line between author's judgement and
    reader's decision.** The memo audits the website *against the client's own consent forms*,
    finds the gap, names it (*"a litigation exhibit waiting to be assembled"*), and derives a
    reusable drafting rule from it: *"no page of the Website should promise more than the consent
    form for that therapy admits."* It then draws the line explicitly: *"The risk-reward calculus
    on the remaining PG-13 items is ultimately yours to make; my job is to make sure you make it
    with clear eyes."*

### How to use this
Properties 1–3, 13, 19 are the cheapest and most often missing; a report lacking any of them is
below the floor on its face and can be self-caught before delivery. Properties 14–17 are what
distinguish an audit that is *trustworthy* from one that is merely thorough — they are the
places where the author volunteers information against their own apparent interest, which is
precisely why a reader can rely on the rest.

## Links
- mandated-by: 2026-08-27-audit-report-quality-floor-mandate
- exemplars: research/knowledge-home/reference/audit-report-standard/ (see its README for the
  privilege caveat and the pdftotext extraction command)
- relates-to: 2026-08-27-source-verifies-on-terminology-and-fails-on-numeric-hero-claims —
  property 18's verify-the-citation discipline is the direct countermeasure to the
  citation-laundering pattern found in the reviewed external documents.
- relates-to: 2026-08-27-a-zero-vulnerability-adversarial-pass-still-earned-its-cost — property 13
  is why that pass's "two findings deliberately not fixed" were flagged rather than dropped.
