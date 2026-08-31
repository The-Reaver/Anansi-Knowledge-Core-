---
id: 2026-08-05-anansi-inbox-wrong-location-corrected
type: finding
status: ratified
source: "this chat, 2026-08-05, Abad reported \"Anansi said the inbox is empty\" after this session created a git-repo file believing this served as the inbox (source status: active)"
project: fleet
tags: [anansi, knowledge-core, inbox, naming-collision, mistake, operator-contribution]
---

# ANANSI_INBOX.md Was Written to the Wrong Location, This Drive Folder Is the Real Inbox

## Body

Abad reported Anansi's inbox as empty after this session announced a Knowledge Core update. The report was accurate, not a system error. Earlier this session created a file named ANANSI_INBOX.md inside the git repository at C:\Users\abadm\stag, on the assumption this location served as the real inbox. The real, established inbox is this Google Drive folder, Anansi Atomic Notes Inbox, created 2026-08-04 and already holding roughly 23 atomic notes in a fixed format: an H1 title, a metadata block (id, type, status, source, tags), a Body section, and an optional Links section naming relationships to other notes (derived-from, extends, affects, touches, corrects, corrected-by). The git-repo file never reached this folder, so Anansi never saw its content. The git-repo file now carries a banner pointing back here. The content originally written there, the announcement of Knowledge Core's real state and business case, is now filed properly as the linked note below.

## Links

- affects: 2026-08-05-knowledge-core-benefits-and-honest-risk-reference
