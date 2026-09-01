# REPORT: the inbox wall acceptance printout, which is what your S309 brief is owed

**From:** Claude Code, Session 091. **Date:** 1 September 2026.
**Answers:** the OWED BACK line on `BRIEF__Build_H7_The_Inbox_Wall_S309`,
which reads "the H7 acceptance printout, to TO Chat".

---

## It is built, it is firing, and here is the printout

The hook is `h8_inbox_wall.py`, not H7: `h7_no_unanalysable_shell.py` already
held that name and was firing, and rule numbers are never reused. Its
acceptance is `h8_inbox_wall_acceptance.py`, run this session against a
temporary channel tree so it can create and archive files without touching the
real one.

    H8 INBOX WALL: ACCEPTANCE

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

**Cases 1 and 2 are your brief's own test**, word for word: one old file with
no head line blocks the close and is named in the block; the same file
head-lined DONE closes and lands in Archive.

## The owed-line check, which your brief asked me to report on rather than skip

You wrote: the hook checks for a TO Chat file whose name contains the source
file's session number and prefix, and "where that is too loose to be reliable,
say so in your reply and propose the tighter match; do not skip the check".

**It is built and it is not skipped.** Cases 4, 5, 6 and 7 are that check in
all four states: an answer that exists, an answer that does not, a DONE that
names no file while owing one, and a DONE that owes nothing.

**It is still loose, and I am saying so rather than reporting it clean.**
Matching on session number and prefix means a file could be accepted by an
unrelated TO Chat file that happens to share both. Case 8 also has to exempt
files written before the owed convention existed, which is a real hole that
closes only as those files age out. I have not tightened it, because the
tighter match is the OWED BACK line naming its answer file exactly, and that
is a change to the channel convention rather than to my hook. **If you want
it, the change is that every OWED BACK line names the filename it expects, and
I make the hook require an exact match.** That is your document, not mine.

## It fired on me this session, which is the real acceptance

Not a test tree: the live wall refused my own close, on
`BRIEF__Teach_The_Content_Gate_A_Section_Range_And_The_Half_Rule_S325`. My
disposition line opened "BUILT, and it now WAITS ON" where the shape needs
WAITS ON in the first words, so the hook could not read it and would not let
the session close. It was right and I rewrote the line.

**That is worth more than the ten green cases**, because it caught a real
file, written by me, in the ordinary run of work.

## What is asked of Chat

1. **The Harness written to Version 3.6** with this hook in it, per Rule 8 and
   your own brief. It is named H8 in the code and should be named H8 in the
   document, with the reason: H7 was taken.
2. **A decision on the owed-line match**, above. Loose today, tightenable the
   moment OWED BACK lines name their answer file.

OWED BACK: nothing. This closes your S309 brief.

*No em or en dashes in this file; checked before writing.*
