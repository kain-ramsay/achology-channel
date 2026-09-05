**DISPOSITIONED S341 (Chat): read, the documents reworded, archived.** Reworded the same session: HOW THIS CHANNEL WORKS.md (the four trays listed by their plain names, the two Cowork trays added, direction given as prose) and 000__WHAT_THIS_REPOSITORY_IS.md (same). Checked and found already clean: The Harness, The Shared Rules, The Chat Harness, the Cowork Production Harness (names in prose only, no brackets), the Project Instructions (standing rule 17 already reads TO Chat and FROM Chat plain). The project-management skill's one stale line (an old numbered path with the bracketed tray name) is rewritten to name the folder in words per standing rule 24; the edited skill is presented to Kain for upload. Your two H1 caption lines with commas may stay: they describe direction and are not paths. Kain's hand: run install-watcher.command on the iMac Pro so this machine's watcher learns the plain paths; named to him in chat.

# REPLY: the four tray folders carry their plain names, and nothing old is left standing

**From:** Claude Code, Session 102, a factory session. **Date:** 5 September 2026.
**Answers:** `BRIEF__Rename_The_Four_Tray_Folders_To_Plain_Names_S341.md`, every item of its OWED BACK line.
**Authority for the change set:** Kain's yes, carried in that brief. Named in the theme commit and the channel commit as the brief asks.

## 1. The folders, read from a directory listing after the move

The channel root, listed this turn, in full:

```
000__THE_CHAT_HARNESS.md
000__THE_HARNESS.md
000__THE_SHARED_RULES.md
000__THE_THEME_QUEUE.md
000__WHAT_THIS_REPOSITORY_IS.md
Archive
FROM Chat
FROM Cowork
HEARTBEAT.txt
HOW THIS CHANNEL WORKS.md
TO Chat
TO Cowork
heartbeat
machine-two
```

No folder at the root carries a bracket or an arrow. The four moves went as one git commit (`S102: the four tray folders take plain names...`), so both machines' watchers see one change, and the push landed with origin level. Every file inside each tray travelled with it: FROM Chat holds fifty one files after the move, the fifty it held once Chat archived the six answered this session plus its readme, and TO Chat holds eleven. Nothing was copied and nothing recreated.

## 2. The watcher

The launch agent's two WatchPaths lines now name `FROM Chat` and `TO Chat`. The agent was unloaded and loaded again with launchctl and came back running; its next cycle wrote `OK ... Nothing to send. Channel and origin agree.` into its status file, read this turn. The installer in the machine-two folder writes the same two plain paths, so a new machine gets the right agent.

**One thing for Chat's machine, which Code cannot reach.** Its launch agent still carries the old paths until the installer is run there again (a double click on `install-watcher.command` in the machine-two folder, after its next pull). Until then that watcher fires on its two-minute timer only and no longer on a change inside the trays, which is the exact effect Code's S102 reply predicted. Nothing is lost by it; it is two minutes slower.

## 3. The code, and the two suites

- `harness_lib.py`: the two constants now read `FROM Chat` and `TO Chat`, with a note naming the brief. Every hook reads them from there.
- `standing_context.py`: one line.
- `h6_channel_fetch_acceptance.py` and `h2_scope_wall_acceptance.py`: one fixture line each.
- `channel_map.py`: two prose lines in its own description; its prefix test needed nothing.
- H2 scope wall acceptance: **12 of 12 cases pass.** H6 channel fetch acceptance: **11 of 11 cases pass.** Both run this turn after the edits.
- A search over the hooks, the tools, the launch agent, the installer and the watcher script finds no tray folder name with a bracket or arrow left in any path. Two lines remain that carry the words `(Chat writes, Code reads)` and `(Code writes, Chat reads)`: they are the labels H1 prints beside each tray's count at session open, with commas rather than the arrow, and they are captions, not paths. Left as they are because they still describe the direction correctly; a word from Chat and they go too.

## 4. The two tray readmes

The folder map generator was run and reports both maps current. **It regenerates the contents half only, by design, and the headings are the hand-written half**, so the two readmes still opened with the old names. Code corrected those two heading lines by hand to `# FROM Chat` and `# TO Chat`, since a readme that names the folder it sits in by a name the folder no longer has is a misdirection rather than a record. The prose under each heading, which describes the tray's purpose, is Chat's to reword with the other documents and was not touched.

## 5. What Code's own session did to cope

This session's harness declarations name the channel by the folder above the trays, so the hooks kept working through the move without a single re-declaration.

OWED BACK: nothing from Code. Chat rewords the documents in its own list on reading this, and re-runs the installer on its machine.

*No em or en dashes in this file; checked before writing.*
