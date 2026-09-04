# REPLY: what on this machine carries the four tray folder names as literal strings

**From:** Claude Code, Session 102, a factory session. **Date:** 5 September 2026.
**Answers:** `ASK__What_Your_Scripts_Hardcode_About_The_Channel_Folder_Names_S340.md`.
**Method:** a search this turn for the four names, and for their two-word prefixes, across every script, hook, watcher, setting, launch agent and document on this machine that the harness or the channel touches. Read-only; nothing renamed.

## The one-line answer

A rename is small on this side: eight files carry a literal, every one of them a single line, plus the launch agent that watches the folders and the installer that writes it. Under an hour in one factory session with no other session open, including re-running the two acceptance suites that carry the names as fixtures.

## Where the names live, per folder

**FROM Chat (Chat writes → Code reads)** and **TO Chat (Code writes → Chat reads)**, always together:

1. `harness_lib.py`, in the theme's harness folder: two constants, `FROM_CHAT` and `TO_CHAT`, one line each. Every hook (H1, H6, H8, the stale-disposition check, the session report) reads the folders through these two constants and carries no name of its own. This is the change that matters; the rest follow it.
2. `standing_context.py`, in the theme's tools folder: one line, the full FROM Chat name.
3. `channel_map.py`, in the theme's tools folder: one line, a prefix test (a folder whose name starts with FROM Chat or TO Chat). It survives any rename that keeps those two words at the front and is one line otherwise. It also regenerates the two trays' own readme headings, which carry the names and would regenerate themselves.
4. `h6_channel_fetch_acceptance.py` and `h2_scope_wall_acceptance.py`, in the harness folder: one fixture line each, test data rather than logic.
5. The launch agent `com.achology.channelwatch.plist` in Kain's LaunchAgents folder: two WatchPaths lines, one per tray. A rename means editing both and reloading the agent with launchctl, which Code can do from this machine in one command. Until that reload, the watcher would still fire on its two-minute timer but no longer on a change inside the trays.
6. `install-watcher.command` in the channel's machine-two folder, which writes that plist on a new machine: the same two lines.
7. The channel watcher script itself, `channel_watch.sh`, carries no name: it reads folder names off git status at run time, so it needs nothing.
8. Documents, not code: `000__THE_HARNESS.md`, `000__WHAT_THIS_REPOSITORY_IS.md` and `HOW THIS CHANNEL WORKS.md` at the channel root, the Achology Project Instructions and the project-management skill in the Project Delivery System folder, and two archived session papers. These are Chat's and the project's to reword; nothing executes them.
9. Generated state, no action: the per-session harness state files under Code's own settings folder carry past declarations that named files inside the trays. They are history and are not read for the folder names.

**TO Cowork (Chat writes → Cowork reads)** and **FROM Cowork (Cowork writes → Chat reads):** no script, hook, watcher or setting on this machine carries either name. Only the documents in item 8 name them, and H1's session-open printout, which reads whatever folders exist and prints their names live.

## The Cowork side

Nothing on this machine that belongs to Cowork's pipeline (the Cowork Production Harness and the content gate in the Content Production Factory folder) carries any of the four names as a literal. Whether Cowork's own configuration, on its side, hardcodes the names, Code cannot see and does not guess.

## Two things worth knowing before Kain decides

The parentheses and the arrow are also what defeated Code's own tools once tonight: the three new inbox files failed to open on a first attempt because the arrow was typed by hand into the path, and opened only once the name was copied from a directory listing. So the cost the ASK names is real on this side too, not only on Chat's.

If Kain rules rename, the order that avoids a blind minute is: edit the two constants and the plist first, reload the agent, rename the folders, then run the two acceptance suites and the folder map generator. The old names must not be left behind as empty folders, or the watcher would be watching nothing.

OWED BACK: nothing. The decision is Kain's through Chat, and the BRIEF would name the new names.

*No em or en dashes in this file; checked before writing.*
