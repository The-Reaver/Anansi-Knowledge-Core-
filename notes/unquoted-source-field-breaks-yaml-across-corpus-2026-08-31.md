---
id: unquoted-source-field-breaks-yaml-across-corpus-2026-08-31
type: lesson
status: ratified
source: "This session (Anansi Knowledge Core work), 2026-08-31 — discovered after an earlier ratification/mining pass in this same session had already appended unquoted parenthetical status annotations into 108/108 notes' source: fields"
project: fleet
tags: [yaml, frontmatter, data-integrity, tooling, note-schema]
supersedes: []
superseded_by: null
---

# An unquoted colon in a YAML frontmatter value silently breaks every note it touches, and looks completely fine to a human

## Body

Appending a parenthetical like `(source status: active)` directly into a YAML `source:`
field, without quoting the value, produces invalid YAML the instant a real parser reads
it — the second colon makes YAML try to parse a nested mapping where a scalar was
expected. `yaml.safe_load` throws `mapping values are not allowed here`. This happened
silently across an entire ratification/mining pass: 108 of 108 notes in `notes/` had this
defect at once, introduced by an automated pass that treated the `source:` line as plain
text rather than a value inside a structured document. Nothing about the broken files
looked wrong to a human reading them as markdown — the corruption is only visible to
software that actually parses the frontmatter as YAML.

**Check next time an automated pass writes or edits YAML frontmatter values:** quote the
value (or otherwise escape it), then re-parse every touched file with a real YAML parser
before treating the pass as done — don't rely on the file looking correct by eye. A note
store's frontmatter is only as trustworthy as the last thing that touched it.

## Links

- relates-to: 2026-08-07-ownership-and-entity-map-2 (duplicate id caught in the same
  integrity pass this note describes)
