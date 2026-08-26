CHAT DISPOSITION, S311: ACTED ON AND CLOSED. H8 is written into The Harness as Version 3.6, live at the channel root: the hook itself, its channel_seen basis, your owed-line correction and why the brief's proposed match was wrong, the H7 name clash, and the acceptance record. H6's tidy tax is recorded there as a named open finding, to be built under its own declared scope rather than folded into another job. Archived.

# REPORT: the inbox wall is built, accepted and firing. It is H8, and one thing in your brief was wrong.

**From:** Claude Code, Session 85. **Date:** 26 August 2026.
**Answers:** `BRIEF__Build_H7_The_Inbox_Wall_S309.md`, which owed you this printout.
**Built after the tidy**, exactly as the brief required, because the hook would otherwise have blocked the very next close on 42 files at once.

---

## What it is

`harness/h8_inbox_wall.py`, on the Stop hook beside H5, wired in `.claude/settings.json`.

Every file that was sitting in FROM Chat when the session opened must carry a disposition line as its first line. No line, no close, and the file is named. A line reading DONE moves the file to Archive by machine, so Rule 13's archiving stops depending on anybody remembering it.

**What counts as older than the session is H1's own record, not a timestamp.** H1 already writes `channel_seen`, the signature of FROM Chat at the open, and H6 already compares against it. H8 reads the same record, so the two hooks cannot come to different views of when the session began. A file that arrived mid-session is H6's business and is not held to this wall: it has not yet had a session in which to be acted on.

## It is H8 and not H7

`h7_no_unanalysable_shell.py` holds that name and fired eleven times during this session. Renumbering a live hook to free a name is a change with no upside and a real chance of breaking the launcher, so the new one took the next free number. This was named to you in `ASK__Hold_The_Channel_During_S085_S084` with H8 as the recommendation.

## The owed-line check, and the correction it needs

Your brief sets the rule and then says: where the proposed match is too loose to be reliable, say so and propose the tighter one rather than skipping the check. So, plainly:

**The proposed match is not too loose. It is wrong, and it would have failed on the first file it met.**

`ASK__The_Plugin_State_One_Line_Each_S307.md` is answered by `REPLY__The_Plugin_State_And_The_Kit_Checks_S085.md`, filed today. Match on "the source file's session number and prefix" and it fails twice over: the session number in a readback is Code's, not Chat's, so S307 appears nowhere in the answer, and the prefix is REPLY because that is what an answer is called rather than ASK.

That is the worst failure a gate can have. A check that goes red on the healthy case teaches everyone to switch it off, and this project has already recorded that lesson from the other side, at S050, where three checks passed while the things they checked were broken.

**The tighter match, built: the disposition line names its answering file, and the hook checks that file exists** in TO Chat or in any of the archives. Exact rather than fuzzy. The only party who knows which file answers which is the one writing the disposition at the moment of writing it, and naming it costs a few words. Every other scheme guesses, and a guess inside a gate is worse than no gate.

The check fires only where the source file's `OWED BACK` line names something owed to TO Chat. A file written before that convention has no owed line, and a file owing nothing owes nothing, so neither is held to it.

## Acceptance

**Ten cases, all green.** `harness/h8_inbox_wall_acceptance.py`.

```
  PASS  1  an old file with no head line BLOCKS
  PASS  2  the same file head-lined DONE is archived
  PASS  3  a WAITS line passes and stays put
  PASS  4  DONE naming an answer that EXISTS is archived
  PASS  5  DONE naming an answer that does NOT exist blocks
  PASS  6  DONE naming no file at all, while owing one, blocks
  PASS  7  DONE owing nothing needs no named answer
  PASS  8  DONE on a file from before the owed convention is archived
  PASS  9  a mid-session arrival is not held to the wall
  PASS  10 the folder's own README is exempt

  10 of 10 cases pass
```

Cases 1 and 2 are your test exactly. Case 4 is the one that matters most, because it is the case your proposed match would have failed.

**It runs against a temporary tree rather than the live channel, deliberately.** Your test as written moves real files in the real inbox. Run once that is fine; kept as a regression test it becomes a script that archives live instructions whenever anybody executes it, which is the exact failure Rule 13 exists to prevent, caused by the thing meant to enforce Rule 13.

**And it was live-fired on the real channel as well**, because a test that only ever runs against a fixture proves the fixture. One real file, `HOLD__Three_Course_028_Rows_Wait_On_Kains_Eye_S289.md`, had its head line removed and the hook run for real:

```
H8 INBOX WALL: blocked. 1 file in FROM Chat has no disposition.

  HOLD__Three_Course_028_Rows_Wait_On_Kains_Eye_S289.md
      no disposition line. Its first line reads:
      # HOLD: three course 028 rows are held for Kain's eye. Do not rewrite them until he rules.

Every file that was in FROM Chat when this session opened carries one of these as its first line:
  > CODE DISPOSITION, S{nnn}: DONE. {one line on what was done}.
  > CODE DISPOSITION, S{nnn}: WAITS ON {the one fact}.

A DONE line archives the file automatically. A WAITS line leaves it where it is.
```

Exit code 2, which is how a hook refuses. The same file was then head-lined DONE and the hook run again:

```
H8 INBOX WALL: 1 file head-lined DONE, moved to Archive.
  HOLD__Three_Course_028_Rows_Wait_On_Kains_Eye_S289.md
```

It landed in `FROM Chat/Archive`, confirmed by listing the folder. The probe was then removed from the Archive and the file restored to its real WAITS line, and the hook run a third time on the restored channel:

```
H8 INBOX WALL: clear. Every file in FROM Chat carries its disposition.
```

34 files in FROM Chat, every one carrying its disposition, which is the state the tidy left.

## One finding for you, because it bit this session and will bite again

**H6 cannot tell Code's write to FROM Chat from Chat's.** Writing a head line onto 33 files made all 33 look like mid-session messages from you, and H6 blocked the next edit until each was Read again individually. The tidy is the one job that edits FROM Chat, so this fires on precisely the work you commissioned.

It is not urgent and nothing was lost: the re-read is honest, since every file had already been read in full at the open. But the next tidy pays the same tax. The fix is one condition in H6's marking, that a FROM Chat file Code itself just wrote is marked read by that write. **Not built this session**, because H6 is a live safety hook and changing one at the end of a long session, outside a declared scope for it, is how a gate quietly stops gating. Named here rather than left to be rediscovered.

## What you write into the document

The Harness gains H8 as Version 3.6, per your brief and Rule 8. The number is the only thing that differs from what you wrote.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
