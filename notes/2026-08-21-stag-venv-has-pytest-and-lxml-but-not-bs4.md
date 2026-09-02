---
id: 2026-08-21-stag-venv-has-pytest-and-lxml-but-not-bs4
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (retitled and reframed from a standing present-tense claim to an explicitly dated 2026-07-22 snapshot, with the 2026-08-25 drift finding — bs4 now present, lxml no longer present — appended so the package-state claim is not re-trusted as current). Operator retains veto per Mandate 1."
project: fleet
tags: [stag, environment, venv, python, dependencies, testing]
sources:
  - ref: "Turns 17-24 accurately support the note as a point-in-time build-day observation: turn 19 shows the default/system python lacking pytest/bs4/lxml, turn 22 identifies the D1 venv, and turn 24 states 'it has lxml and pytest but no bs4'."
    reliability: medium
    origin: "STAG session, 2026-07-22, \"GEO days 3-5 audit engine\" (backfilled from historical transcript d4e8f900, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-22-backfill-d4e8f900.jsonl
  turns: [17, 24]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: medium, directly observed in this session by inspecting the venv, but the raw command output was stripped from this transcript, and an existing memory note describes a seemingly conflicting venv state
- verified: 2026-08-21

# As of 2026-07-22, the stag project venv (C:\Users\abadm\stag\venv\Scripts\python.exe) had pytest and lxml installed but not bs4 — this package state has since drifted

## Body
During the GEO days 3-5 audit-engine build, the agent first checked a default/system Python and found no pytest, bs4, or lxml available, which would have forced a stdlib-only implementation. It then recalled that the earlier D1 build report had used a specific project virtual environment, `C:\Users\abadm\stag\venv\Scripts\python.exe`, switched to it, and confirmed that, as of 2026-07-22, that venv had `lxml` and `pytest` installed, but not `bs4`. The agent chose to write the new audit engine using only the standard library's HTML/XML parsing (`html.parser`, `xml.etree`) anyway, to keep it dependency-matched with the existing standalone-plus-pytest test pattern and avoid adding `bs4` as a new dependency, even though `lxml` was technically available at that time.

**Package-state drift (as of 2026-08-25):** this venv's package contents are not stable and this note's package claim must not be read as a standing fact. A 2026-08-25 re-check found the state had moved, and in the opposite direction from the 2026-07-22 snapshot above: `pytest` was still installed (matching the original claim), but `bs4`/`beautifulsoup4` (4.15.0) was now installed (contradicting the original "not bs4" claim) and `lxml` was no longer installed (contradicting the original "has lxml" claim). Treat any pytest/bs4/lxml claim about this venv as a point-in-time snapshot only — re-verify by direct inspection (e.g. `pip list` / `pip show`) before relying on it for a build decision.

Note for whoever reconciles this: an existing memory note ("Stag backend test env") states the venv lacks pytest, which appears to describe a different venv or a different invocation context (e.g. running `python` without activating the venv, or a since-changed environment) rather than contradicting this finding outright. Anyone relying on either claim should re-verify which Python/venv is actually being invoked before trusting either statement.

## Links
- related-to, 2026-08-21-geo-d3-audit-engine-real-implementation-replaces-always-95-stub.md, the build session where this environment fact was confirmed.
