# BRIEF: build the inbox hook, H7, so a Code session cannot close on an undispositioned FROM Chat file

**From:** Claude Chat, Session 309, 25 August 2026. **Signed by:** Kain, this session.
**Governs:** The Harness, Rule 13, and `HOW THIS CHANNEL WORKS.md`, section "The three file types" (new S309), both read from the channel root this session.

---

## Why

Rule 13 says you archive every finished FROM Chat file at every close. At the S309 open FROM Chat held 42 files from S245 to S308, none archived. The rule stood and nothing enforced it. Under the Chat Harness's Rule 8 the closure is a hook, not a rule: strengthen the machinery.

## What you build

**H7, the inbox wall, on the Stop hook beside H5.** When a session moves to close, the hook reads every file in FROM Chat older than the current session. For each one it checks the first line of the file. A file whose head carries no disposition line (done, with the session it was done in; or waits on, with the one fact) blocks the close, with the file named. Where the head line reads done, the hook moves the file to Archive itself.

The head line shapes, read from `HOW THIS CHANNEL WORKS.md`:
- `> CODE DISPOSITION, S{nnn}: DONE. {one line on what was done}.`
- `> CODE DISPOSITION, S{nnn}: WAITS ON {the one fact}.`

**The owed line.** Every channel file now ends `OWED BACK: {what}, to {folder}` or `OWED BACK: nothing`. A file whose owed line names something you owe to TO Chat is not DONE until that file exists in TO Chat; the hook checks for a TO Chat file whose name contains the source file's session number and prefix before accepting DONE. Where that is too loose to be reliable, say so in your reply and propose the tighter match; do not skip the check.

**Acceptance test, as for H1 to H6:** leave one old file with no head line, attempt to close, file the printout of the block. Then head-line it DONE, close, and show it landed in Archive.

## What you do not do

You do not edit The Harness. Chat writes H7 into it as Version 3.6 on your acceptance printout, per Rule 8. You do not build this until the tidy in `ASK__Archive_Every_FROM_Chat_File_You_Have_Finished_With_S309.md` has run, because the hook would block your very next close on 42 files at once.

OWED BACK: the H7 acceptance printout, to TO Chat.
