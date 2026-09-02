---
id: 2026-08-21-stag-ast-based-dependency-check
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, meta_agent, validator, python-dependencies, static-analysis, false-positive]
sources:
  - ref: "Archive turns 102-134 show STAG's regex-based undeclared-dependency check false-positiving on docstring prose, and its rewrite using ast.parse plus sys.stdlib_module_names, which then surfaced 6 real pre-existing dependency debts."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [102, 134]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent narrated the exact failure and the rewrite, then ran it against the whole project tree
- verified: 2026-08-21

# STAG's undeclared-dependency check had to move from regex to AST parsing because docstring prose caused false positives

## Body
When STAG's task 9 output imported `apscheduler` with no corresponding entry in `backend/pyproject.toml`, the operator asked for a general improvement pass. The agent's first attempt at an "undeclared third-party dependency" check used a regex over file text, which immediately misfired: it matched ordinary English words inside docstrings (for example, "from an environment..." was parsed as `from an import environment`-shaped text and flagged `an` as a package). The agent rewrote the check using Python's `ast` module to parse only real `import`/`from ... import` statements, cross-referenced against `sys.stdlib_module_names` plus a manual alias table mapping import names to their install names (e.g. `dotenv` → `python-dotenv`, `jwt` → `pyjwt`). Run against the whole existing codebase, the corrected check immediately surfaced 6 real pre-existing dependency debts (`stripe`, `twilio`, `pyjwt`, `asyncpg`, `psycopg`, plus a broken import in `backend/app/routes/__init__.py`) that the project had been silently carrying. General lesson: any "does this dependency exist" or "does this name appear" check built from LLM-generated code should be built on the language's real parser, not string/regex matching — free-text docstrings and comments will produce false positives that a regex cannot distinguish from real syntax.

## Links
- related, 2026-08-21-stag-config-folder-collision-autofix.md, part of the same operator-requested "improve the STAG agent" pass on 2026-07-09
