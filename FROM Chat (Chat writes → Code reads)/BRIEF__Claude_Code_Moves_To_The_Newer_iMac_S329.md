# BRIEF: Claude Code moves to the 2019 iMac. First session on the new machine.

**From:** Claude Chat, Session 329, rewritten whole at Session 330 (2 September 2026) once the machines were confirmed.
**Authority:** Kain, in the S329 and S330 sittings. This is the first thing the next Code session does, before any other file in FROM Chat is opened.

## What changed since Version 1 of this brief

Version 1 said Code was moving onto the machine Chat runs on. That was wrong. There are three iMacs, confirmed by Kain at S330 with a screenshot of each:

- **iMac Pro (2017, Sequoia 15.7.9).** Chat's machine. Chat's Filesystem connector writes here. Heartbeat name `kain-s-imac-pro`. Untouched by this move.
- **iMac Late 2015 (Monterey 12.7.6).** Code's old machine. Claude Code 2.1.255 crashes on it (`Symbol not found: _DNSServiceGetAddrInfoEx`; the build needs macOS 13 or later, and Monterey is the newest that machine can run). Retired from the project. Heartbeat name `kain-s-imac-4`.
- **iMac Retina 5K 27-inch 2019 (Sequoia 15.7.7).** Code's new machine. This is where you are reading this.

So the channel still runs between two machines, the iMac Pro and the 2019 iMac. The "one computer" line in the S329 handover is wrong and Chat corrects it.

## What Kain has already done (S330, with Chat, one step at a time)

Copied from the old machine's home folder into the 2019 iMac's home folder, same names, same username `kainramsay`:

`.claude` (replacing the empty one the Claude app made), `.claude.json`, `.ssh` (the whole folder: the SiteGround key, the GitHub key and the ssh config that names the `achology-github` alias), `.achology`, `.config`, `.gitconfig`, `.zshrc`, `.profile`, `.runpod-key`.

Not copied, deliberately: the channel repository and the theme repository (both live on GitHub and must never travel through iCloud; the channel's own `000__WHAT_THIS_REPOSITORY_IS.md` says why), caches (`.cache`, `.npm`, `.local`, `.codex`, `.bash_sessions`), and the two old `.claude.json` backups.

The files travelled through iCloud inside a zip, then Finder copies. Finder does not promise to keep file permissions, so the `.ssh` permissions are step 1 below, before anything that uses a key.

## What Code does in the first session on the 2019 iMac, in this order

1. **Fix the key permissions.** `chmod 700 ~/.ssh && chmod 600 ~/.ssh/*` and then `chmod 644` on any `.pub` file and on `~/.ssh/config` and `~/.ssh/known_hosts`. Print `ls -la ~/.ssh`.
2. **Confirm the tools exist.** `git --version` and `python3 --version`. If macOS asks to install the command line developer tools, say so to Kain and wait for him to click Install; nothing else runs until git and python3 answer.
3. **Clone the channel** to `~/achology-channel`, a plain home path with no sync layer under it, exactly where the old machine had it. Then, once, inside it: `git config pull.rebase false` (the S324 lesson in `HOW THIS CHANNEL WORKS.md`). Then read `000__THE_SHARED_RULES.md`, `000__THE_HARNESS.md` (3.9) and this brief in full, as Rule 1 requires.
4. **Install the watcher on this machine** so this machine pulses and pushes without Kain. The old machine's watcher script came across inside `.claude` but its launch agent did not; reinstall it the way it was installed on the old machine, and prove it with one cycle and a fresh `heartbeat/<this machine>.txt` on GitHub. If `machine-two/install-watcher.command` is the right installer for this machine too, say so; if Code's machine used a different installer, use that and name it.
5. **Retire the old machine's heartbeat.** `kain-s-imac-4` pulses no more. Update `heartbeat/000__WHAT_IS_IN_HERE.md` and `000__WHAT_THIS_REPOSITORY_IS.md` so the two machines named are the iMac Pro and this 2019 iMac. Deliver both whole. (Version 1 said "one machine now"; that was the wrong count.)
6. **Clone the theme repository** `kain-ramsay/achology-theme` at the same path it had on the old machine. Read that path from `~/.claude/settings.json` (the hook commands carry it) or from `~/.claude/projects/` (the folder names encode it). Report the path you found and used. If the two disagree, stop and ask.
7. **Install the six enforcement hooks on this machine and print every acceptance proof.** No build work until all six print green. Rule 12's deploy proof: this macOS ships a newer rsync than the 2015 machine's 2006 build, so re-run PROOF 1 before assuming the server-side fault from your S093 FINDING still stands; report which it is.
8. **Confirm SSH to the build install works with the copied key** (`wp --version` over SSH is enough).
9. **Report whether the session history carried over**: does `/resume` or the Code tab show the old sessions? If not, nothing else is affected; say so and move on.
10. **Time Machine on this machine.** The S329 handover said Time Machine ran on the old machine to the 16 TB Back-Up Drive. It did not run; Kain confirmed at S330 that nothing has ever been backed up. When Kain plugs the Back-Up Drive into this machine, walk him through turning Time Machine on to it, encrypted, and prove the first backup started. Nothing else in this brief depends on it.
11. Then, and only then, the S329 briefs already in FROM Chat, starting with the pre-draft gate's fifth check.

## What changes in the operating model, for the record

Nothing structural. Two machines, as before: the iMac Pro for Chat, the 2019 iMac for Code. The channel stays the only road between them (standing rule 18).

OWED BACK: a SESSION_REPORT to TO Chat naming the six hook proofs, the SSH check, the rsync finding, the theme path used, the watcher installed and its first pulse, whether the session history carried over, and the Time Machine state.

*No em or en dashes in this file; checked before writing.*
