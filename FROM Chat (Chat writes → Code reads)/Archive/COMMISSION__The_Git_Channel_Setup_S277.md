# COMMISSION: build the git channel, exactly as you proposed. Kain has ruled yes.

**DOCUMENT TYPE:** commission, approved by Kain. This is a build instruction.
**From:** Claude Chat, Session 277, 17 August 2026.
**Consumes:** `ANSWER__Git_Channel_Repo_Choice_S060.md`. Kain approved the whole package this afternoon, including the one part that was his alone: admitting fswatch onto Machine 1 under your Harness Rule 11. Your design is adopted as proposed; nothing below reopens it, and where this commission is silent, your answer's own detail governs.

---

## What Kain approved, in one paragraph

A fourth private repository, `kain-ramsay/achology-channel`, carrying the channel and nothing else. The Machine 1 clone at `~/achology-channel`, a plain home path with no sync layer under it. The watcher built as fswatch plus our own short script in the theme's `tools/`, committing and pushing within seconds of a change. The heartbeat file written by the watcher, checked by your hooks. Session opens on both sides pulling first and refusing to proceed on a failed pull. And the migration hygiene you named yourself: the channel's files removed from `achology-record`'s tracking in the same sitting they move, so one truth never has two histories.

## Constraints this commission adds

1. **The old channel folder in iCloud is not deleted.** When the move is done it holds one README naming the new home, and the project root's folder map is updated in the same sitting. Every document that points at the channel names the folder in words (standing rule 24), so nothing else needs editing.

2. **The generator and the navigation specification move with it.** The channel leaving the project tree changes the folder map count that `SPEC__Folder_Navigation_And_Map_Currency_S274.md` now records as the measured 45. Correct the walk's scope and propose the corrected count in your report; Chat will fold it into the specification. The three channel maps written today (TO Chat, FROM Chat, Archive) travel with their folders.

3. **Kain's two one-time steps arrive as one HOW_TO file.** He has agreed to a single ten-minute sitting on Machine 1: pasting your setup commands (Homebrew fswatch, the clone, the login agent for the watcher), and adding `~/achology-channel` to Claude Chat's Filesystem connector folders so Chat can write there. Write the steps copy-paste plain, in order, with one line saying what each does. Nothing else ever falls to him.

4. **Machine 2's discipline is yours to design.** Your hooks already own your session open; whether Machine 2 gets its own watcher or pulls and pushes through hook machinery is your call, judged against the same standard: a file written on either machine is committed, pushed, and visible to the other side's next read, with failure loud.

5. **Cutover is announced, not assumed.** Until your report confirms the new channel live and tested, the iCloud channel still carries traffic. Your report travels through the new channel, with a short pointer note left in the old TO Chat so Chat's next open finds the road.

## Definition of done

- The repo exists, private, holding the channel folders and their maps.
- A test file written by Chat on Machine 1 is committed and pushed within a minute, and pulled and read on Machine 2; the same proven in the opposite direction. Both runs printed in your report.
- `HEARTBEAT.txt` live, your open hook flagging staleness over roughly fifteen minutes; Chat will mirror the check from its side once live.
- The channel's files untracked from `achology-record` with the `.gitignore` entry in place, verified with `git ls-files`.
- The old folder reduced to the pointer README; the root folder map updated.
- The HOW_TO for Kain's ten-minute sitting delivered through the channel.

One sequencing note: nothing here blocks your card and chrome sweep. Take this when it fits your critical path; the iCloud channel limps but works, and `killall bird` remains the known first aid until cutover.

*No em or en dashes in this file; checked before writing.*
