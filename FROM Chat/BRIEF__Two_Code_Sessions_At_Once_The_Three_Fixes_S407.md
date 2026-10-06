> CODE DISPOSITION, S150: WAITS ON a factory session opening (tooling and harness work; S150 is a theme session).

**For Code: build the three fixes that let a theme session and a factory session run at the same time. Kain's ruling, S407. Factory session; nothing here changes how a page looks.**

# BRIEF: two Code sessions at once, the three fixes (Kain, S407)

**From:** Claude Chat, S407, Tuesday 6 October 2026. **To:** Claude Code. **Built from:** your `REPLY__Two_Sessions_At_Once_What_Breaks_S150`.

## The ruling

Kain wants to run one theme session and one factory session side by side, to stop waiting for turns. The terms are written into The Harness, Version 3.15, Rule 1 ("Two sessions at the same time") and Rule 13 (the number claimed at open). Read them there. Term 6 says no double sitting runs until the fixes below pass, so this brief is what unlocks it.

## The three fixes

1. **The factory worktree.** Set up a git worktree of the theme repository for factory sessions, in a folder beside the deployed one, on its own branch. Confirm every factory tool (import, gate, publish, score, the register builders) runs unchanged from it, as you expect. Write the open step (create or refresh the worktree from main) and the close step (merge the branch into main, resolving nothing silently: a conflict stops and is reported). Confirm H5's deploy check reads only the deployed folder, so factory edits in the worktree never fail a theme close. Acceptance: a factory session in the worktree commits and merges while the theme folder holds uncommitted work, and neither touches the other's files.
2. **Clearances keyed to their session.** `publish_gate.py` writes the session's id into every clearance it mints, and H9 accepts only a clearance carrying its own session's id. Acceptance cases red and green: a clearance minted by session A refused to session B; accepted to A.
3. **The number claimed at the open.** The first act after the opening line writes the empty `SESSION_REPORT__S{nnn}.md` under the next free number. Build it so a second session opening the same minute cannot claim the same number (a create that fails if the file exists is enough). Each session type keeps its own next-session note. Acceptance: two opens in a row take two different numbers.

## Two small lines alongside

- The theme session writes each deploy's version into its heartbeat file, and the factory's measuring tools record the theme version they measured, as your reply proposed.
- Where it helps your tools, the commit step adds named files only; `git add -A` is never used by either session (Harness Rule 1, term 1).

## Report back

One DONE file in TO Chat: each fix with its acceptance printout, the worktree's folder named in words, and one line stating whether a double sitting is now safe to run. Chat tells Kain from that line.

*No em or en dashes in this file; checked before writing.*
