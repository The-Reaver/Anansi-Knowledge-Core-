---
id: 2026-08-21-kotlin-java-toolchain-verification-stalled-18-days-still-not-promoted
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — day count corrected to 22 days and the Java-on-PATH detail corrected. Operator retains veto per Mandate 1."
project: fleet
tags: [kotlin, java, toolchain, polyglot, augustine, roadmap-drafts, stale, build-gate]
sources:
  - ref: "Archive turns 218-229: STAG master-checklist refresh sweep, 2026-08-21, workstream 'Kotlin/Java toolchain verification' — git log against the exact named paths, direct file checks, and a repo-wide search for any recorded gate output"
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Kotlin/Java toolchain verification\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [218, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, based on git log against the exact named paths, direct file checks, and a repo-wide search for any recorded gate output
- verified: 2026-08-21

# Kotlin/Java toolchain verification is unchanged and stalled 22 days after the 2026-08-03 NOT PROMOTED ruling

## Body
The 2026-08-03 `STAG_MASTER_CHECKLIST` and `AMADEUS_RULING_CAPABILITY_MINING_2026-08-03.md` (ruling three) both hold that the Java/Kotlin polyglot stacks are NOT PROMOTED: the generator, build gate, and pass/fail fixtures exist and are committed for both stacks, but only a patched-subprocess run has ever exercised them, never a real `mvn`/`gradle` build. The blocker named then was narrow: the working sandbox had Java 11 (pinned version is 17), no Maven or Gradle installed, no root, and no package-network reach, so the operator was asked directly (`reports/POLYGLOT_TOOLCHAIN_BRIDGE_LIMITATION_2026-08-02.md`, and `OPERATOR_AGENDA.md` item 3, marked "LIVE, this chat") to run four gate commands on their own machine and report back the four `Status:` lines.

As of 2026-08-21, none of that has moved. `git log --since=2026-08-03` returns zero commits touching `agents/roadmap_drafts/augustine_backend_java.py`, `augustine_backend_kotlin.py`, `reports/POLY_JAVA_BUILD_REPORT.md`, `reports/POLY_KOTLIN_BUILD_REPORT.md`, `scripts/gates/java_build_gate.py`, `scripts/gates/kotlin_build_gate.py`, `fixtures/{java,kotlin}_{pass,fail}`, `docs/POLYGLOT_ROADMAP.md`, or `OPERATOR_AGENDA.md`. Both draft agent files are still in `agents/roadmap_drafts/`, not `agents/`. A repo-wide search for the literal `Status: pass`/`Status: fail`/`Status: unavailable` markers the gate scripts print, and a search of every note and candidate dated after 2026-08-03, found no record anywhere of the operator having run the four commands or reported a result. Separately, as of the 2026-08-25 reverification, this environment's PATH now has Java 17 (Eclipse Adoptium jdk-17.0.20.8-hotspot, matching the pinned version) — a change from 2026-08-21, when no java was on PATH at all — but `mvn` and `gradle` remain absent, so the same class of blocker persists in yet another environment; this is not itself proof about the operator's actual daily-driver machine, and the substantive blocker (no verified real build) is unchanged.

Net: the old claim is still factually accurate today, nothing contradicts it, but the item was tagged "LIVE, this chat" 22 days ago and has had zero recorded activity since — it is not in-progress, it is idle, waiting on an operator action nobody has followed up on or re-surfaced.

## Links
- confirms, reports/AMADEUS_RULING_CAPABILITY_MINING_2026-08-03.md (ruling three), no new evidence contradicts it.
- confirms, research/knowledge-home/notes/2026-08-02-kotlin-java-stack-already-built-committed-unpromoted-toolchain-unproven.md
