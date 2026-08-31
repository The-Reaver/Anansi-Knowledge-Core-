---
id: the-knowledge-home-carries-two-incompatible-note-formats-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — VERIFIED by auditing all 1,038 files in The-Reaver/Stag-Fleet research/knowledge-home at branch anansi-home-dashboard (b19dd5f)"
project: fleet
tags: [knowledge-core, schema, note-format, adr-0005, drift, anansi]
supersedes: []
superseded_by: null
---

# 501 of the Knowledge Home's 845 notes use an older format that no YAML parser can read

## Body

Audited every file in `Stag-Fleet/research/knowledge-home/`: **845 ratified notes and 193
candidates**. Of the 845, **501 do not have YAML frontmatter at all**, and a further 20 have
frontmatter that fails to parse. Only the remaining ~324 match the shape ADR-0005 and
`templates/note-template.md` describe.

The 501 are not corrupt — they use an **older list format**, where the fields sit as markdown
bullets beneath the title rather than in a frontmatter block:

```
---
# G1: the GEO dry run's data-model.md rendered empty because ...

- id: 2026-07-18-geo-dry-run-g1-empty-erd-truncation
- type: finding
- status: active
```

Two consequences. **Any tool that reads notes as YAML silently sees a corpus of ~324, not
845** — it will not error, it will just not find the other 501, which is the same silent
under-reporting shape as a cold meaning-search. And the old format uses `status: active`, a
value outside ADR-0005's `candidate | ratified` vocabulary, so the confidence tier that
ratification depends on is simply absent from 59% of the ratified store.

This is very likely what the "312 notes fail ADR-0005 schema" figure was pointing at, measured
against a different subset. The honest number depends entirely on which parser asks.

**Before any gate enforces the schema, the two formats must be reconciled** — otherwise
`archive_notes_separation_gate` blocking on schema failure would reject the majority of the
Core's own history.

## Links

- relates-to: the-knowledge-core-is-forked-between-a-local-store-and-this-git-repo-2026-08-31
- relates-to: validate-the-measuring-tool-before-trusting-its-aggregate-2026-08-31
- relates-to: meaning-search-runs-cold-and-silently-degrades-to-keyword-2026-08-31
