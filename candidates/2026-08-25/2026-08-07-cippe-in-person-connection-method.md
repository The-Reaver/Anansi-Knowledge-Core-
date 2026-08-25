---
id: 2026-08-07-cippe-in-person-connection-method
type: decision
status: candidate
source: Cowork session 2026-08-07; operator required the audit, maintenance, and interview to be done in person only, connecting via Bluetooth or USB, and asked for the best method. (source status: active)
project: cippe
tags: [cippe, maintenance, in-person, offline, usb, ethernet, bluetooth, privacy, security]
---

# In-person, offline connection method for CIPP/E audit, maintenance, and interview

## Body

## Rule
- Audit, maintenance, and the interview are in person only. No remote, no internet. Fits the user's employer privacy rules and is a product strength.

## Recommended connection method (best to least)
- Best default: encrypted USB drive (sneakernet). She exports an encrypted, de-identified feedback bundle to the drive; the fleet reads it on the operator's machine; fixes go back on the same drive; she applies them. Fully air-gapped, strongest privacy, simplest audit trail.
- Faster for large diagnostics: a direct Ethernet cable, point-to-point between the two laptops, no internet. Acts as a tiny private link for the transfer, then unplug.
- Bluetooth: fallback only, for tiny transfers. Slower and less reliable; not the primary.

## Security wrap (any transport)
- Encrypt the bundle end to end.
- Only de-identified improvement data leaves her machine (patterns, not content). Her actual work never leaves.
- She reviews and approves exactly what moves before it moves.
- Every exchange logged on both sides.

## Links

- relates-to: 2026-08-07-cippe-maintenance-architecture-minimalism-and-checkin
- relates-to: 2026-08-07-fleet-interview-and-audit-governance
