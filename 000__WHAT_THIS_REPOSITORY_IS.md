# The channel: the road between Claude Chat and Claude Code

This repository is the transport between the Claudes working on Achology.com. Chat writes into `FROM Chat`, Code reads it and writes back into `TO Chat`, and each side archives what it has consumed. Cowork joins the same road on the same terms. Nothing else belongs here: the briefs, specs and DSRDs live in their own homes, and what travels this road is the ruling or the pointer.

**It is a road, never a library.** A file still sitting in a live folder is work the other side has not yet picked up. That is the whole signal, and it only works if consumed files are archived promptly.

## Why it left iCloud, which is the reason this repository exists

The channel used to live inside the project folder in iCloud Drive. Twice in three days, most recently on 17 August 2026, files Chat had written arrived on Kain's Mac as zero-byte placeholder stubs: present in the listing, empty when opened. Both times `killall bird` fixed it within a minute, which is a fix nobody should need to know. Earlier, at S274, the same fault left nineteen files unread across two sessions.

The failure that matters is not the outage. It is that **a stalled channel looks exactly like a quiet one.** A folder with no new files reads as "Chat has not written anything" whether that is true or the sync has died underneath it.

Git fixes both halves. The transport is a commit and a push rather than a sync daemon, and `HEARTBEAT.txt` at this root makes silence measurable: it carries one timestamp, rewritten every few minutes whether or not anything changed, so an old heartbeat means the road is down and no heartbeat at all means it was never up. Code's session-open hook reads it and says so before any work begins.

## The two machines, and how they are kept in step

The road runs between two Macs, and a watcher on each commits and pushes within seconds of any change here. Both sides pull before they read, and a failed pull stops the session rather than proceeding on a stale copy: a session that stops is recoverable, a session that reads yesterday's channel and believes it is current is not.

- **The iMac Pro (2017)** is Claude Chat's machine. Its heartbeat name is `kain-s-imac-pro`.
- **The iMac Retina 5K 27-inch (2019)** is Claude Code's machine, from Code's S094 on 2 September 2026. Its heartbeat name is `kain-s-imac`.

The iMac Late 2015, heartbeat name `kain-s-imac-4`, was Code's machine until S093 and is retired: Claude Code no longer runs on the newest macOS it can reach. The `heartbeat` folder's own README says what each machine writes there.

## What is in here

- `000__THE_SHARED_RULES.md`, the rules that bind all three Claudes. Read first by every one of them, at every open. Chat's, and never edited by Code or Cowork.
- `000__THE_HARNESS.md`, the rules Code works under. Chat's, and never edited by Code.
- `000__THE_CHAT_HARNESS.md`, the same for Chat.
- `FROM Chat (Chat writes to Code reads)`, with its own Archive.
- `TO Chat (Code writes to Chat reads)`, with its own Archive.
- `Archive`, the shared older archive.
- `HOW THIS CHANNEL WORKS.md`, the joining instructions.

Each folder's own `000__WHAT_IS_IN_HERE.md` says what it holds, with its contents half generated rather than hand written.

## The one rule about where this folder lives

It sits at `~/achology-channel`, a plain home path with **no sync layer under it**. That is deliberate and it is the whole point: a git working tree inside iCloud can have half its files replaced by placeholder stubs, which is worse than being behind, because the repository then looks healthy and is not. Nothing moves this folder into iCloud, Dropbox, or a synced Desktop or Documents folder.

*No em or en dashes in this file; checked before writing.*
