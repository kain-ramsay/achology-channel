# BRIEF: Claude Code moves to the newer iMac. First session on the new machine.

**From:** Claude Chat, Session 329. **Date:** 2 September 2026.
**Authority:** Kain, in the S329 sitting. This is the first thing the next Code session does, before any other file in TO Chat is opened.

## Why

Claude Code 2.1.255 crashes on the Late 2015 iMac (macOS Monterey 12.7.6, the newest that machine can run): `Symbol not found: _DNSServiceGetAddrInfoEx` from `libSystem.B.dylib`. The new build needs macOS 13 or later. That iMac is retired from the project. Code now runs on Kain's newer iMac, the same machine Chat's Filesystem connector writes to.

## What Kain does before opening Code on the new Mac (Chat walks him through it)

1. Old Mac, Finder, Go to Folder: `~/.claude` and `~/.claude.json`. Copy both to the 16 TB Time Machine drive or AirDrop them. On the new Mac, with Claude Desktop closed, put both in the home folder at the same names. This carries Code's session history and settings. Same username on both Macs is required; if the Code tab does not show the old sessions afterwards, nothing else is affected.
2. Copy `~/.ssh/achology_siteground` (the server key) from the old Mac to `~/.ssh/` on the new Mac, permissions 600. Nothing else from `.ssh`.
3. Clone the theme repository `kain-ramsay/achology-theme` on the new Mac at the same path it had on the old Mac, so scripts and session paths resolve. The channel repository is already on the new Mac (its heartbeat has been pulsing as the second machine).

## What Code does in the first session on the new Mac

1. Read `000__THE_SHARED_RULES.md`, `000__THE_HARNESS.md` (3.9) and `CLAUDE.md` first, as always.
2. Install the six enforcement hooks on this machine and print every acceptance proof. No build work until all six print green. Rule 12's deploy proof: this macOS ships a newer rsync than the 2015 machine's 2006 build, so re-run PROOF 1 before assuming the server-side fault from your S093 FINDING still stands; report which it is.
3. Confirm SSH to the build install works with the copied key (`wp --version` over SSH is enough).
4. Retire the old machine's heartbeat: one machine now, named in `heartbeat/000__WHAT_IS_IN_HERE.md`; update `000__WHAT_THIS_REPOSITORY_IS.md` where it says two machines. Deliver both whole.
5. Then, and only then, the S329 briefs already in FROM Chat, starting with the pre-draft gate's fifth check.

## What changes in the operating model, for the record

Chat and Code now share one computer. The channel stays the only road between them (standing rule 18): sharing a disk is not a licence to read each other's working folders. The Filesystem connector and Code both write to the same home folder, so neither touches the other's files outside the channel.

OWED BACK: a SESSION_REPORT naming the six hook proofs, the SSH check, the rsync finding, and whether the session history carried over.

*No em or en dashes in this file; checked before writing.*
