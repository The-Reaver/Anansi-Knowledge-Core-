---
id: 2026-08-23-anansi-skill-file-lives-outside-any-git-repo
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i hereby ratify these notes\"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi, skill-file, git, durability, governance, tooling]
sources:
  - ref: "Operator asks to commit and push the skill update (line 898); assistant reports the file lives under AppData\\Roaming\\Claude\\local-agent-mode-sessions\\skills-plugin\\... and that git rev-parse --show-toplevel returns 'not a git repository' from that directory (lines 899-900)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [898, 900]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The live `anansi` Claude Code skill file (SKILL.md) is not inside the STAG repo and is not tracked by git anywhere — it lives under a Windows AppData Claude-app skills-plugin cache directory with no git history at all

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 784-900
- confidence: high — directly located the actual file via filesystem search, edited it, then confirmed `git rev-parse --show-toplevel` fails from that directory ("not a git repository")
- verified: 2026-08-23
- REVIEW: high-impact

The actual `anansi` skill file that Claude Code loads (the one whose description and instructions govern how an agent searches and writes to the STAG Knowledge Core) was located after a search — it lives at a path under the user's Windows `AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\...` directory, not anywhere inside the `stag` git repository. It was updated in place this session: three missing local API endpoints were added to its documentation, a section on the automatic raw-capture Stop hook was added, a section on underscore-prefixed archival folder conventions was added, and a new governance section on ratification discipline was added (stating an AI must never claim a note is ratified/approved without an explicit operator instruction given after review, citing a real prior incident by its Core note id).

When asked to commit and push that update, the check came back negative: running `git rev-parse --show-toplevel` from that directory returns "not a git repository." The skill file's containing directory has no git repository at all — not a different repo, not a submodule, nothing. This means the edit just made is a local-only file change that takes effect the next time the skill loads, but it is not version-controlled, has no commit history, cannot be diffed or rolled back through git, and is not backed up anywhere durable. It could be silently overwritten by a future Claude Code / plugin update or reinstall, in which case this session's edits (and any future edits made the same way) would simply be lost with no record they ever existed.

General lesson: before treating an edit to a Claude Code skill file as "done," check whether that file's location is actually inside a git-tracked directory. If it is not, the edit is not durable in the way a normal repo change is — the content should be mirrored into a version-controlled location (e.g. as a reference doc inside the actual project repo) if the operator wants the change to survive a plugin update or be recoverable later. This was raised as an open question at the end of this stretch, not yet resolved: whether to write a durable copy of the skill's content into the `stag` repo itself was left as the operator's call.

## Links
- relates, 2026-08-21-anansi-hub-and-mcp-server-confirmed-live-2026-08-21.md — related infrastructure-location context for the Anansi system generally.
