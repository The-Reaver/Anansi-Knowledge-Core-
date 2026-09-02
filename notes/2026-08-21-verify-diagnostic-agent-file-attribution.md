---
id: 2026-08-21-verify-diagnostic-agent-file-attribution
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, project_doctor, llm-diagnostics, verification, trust-but-verify]
sources:
  - ref: "Archive turns 434-442 show project_doctor's DIAGNOSTIC_REPORT.md misattributing a real bug's fix location to routers/messages.py, and the agent verifying against actual source that the nonexistent import was really in services/sms_twilio.py."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [434, 442]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent directly compared the diagnostic's claim against the actual source files and documented the discrepancy
- verified: 2026-08-21

# The project_doctor diagnostic agent got a bug's fix direction right but misattributed which file actually contained it — always verify a model's diagnostic claim against ground truth before applying it

## Body
`project_doctor.py` (a new diagnostic/repair agent built this session, running Claude "Fable 5" at max effort with thinking, deterministic checks first) produced a `DIAGNOSTIC_REPORT.md` whose top "blocker" finding stated that `routers/messages.py` imports a nonexistent `create_outbound_sms` function. When the operator asked for a walk-through before applying any fix, the agent checked this claim against the actual code and found it was wrong: `routers/messages.py` was fine — it correctly called `messages_service.create_outbound_sms_row`, which the service module did define. The bare, nonexistent name `create_outbound_sms` was actually being imported by a different file, `backend/app/services/sms_twilio.py`. The diagnostic model had correctly identified the fix direction (a name needed reconciling) but attributed it to the wrong file. Had the fix been applied automatically and blindly trusting the finding's stated file, the operator would have been directed to look in the wrong place. This is a specific, observed instance of a general rule for any LLM-based diagnostic/fix agent: even a diagnosis that is directionally correct can contain incorrect specifics (file, line, exact name), and those specifics should be checked against the real source before either a human or an automated `fix --apply` step acts on them.

## Links
- related, 2026-08-21-task8-messaging-double-write-architectural-fix.md, this is the same underlying task-8 messaging bug that the diagnostic mis-attributed
