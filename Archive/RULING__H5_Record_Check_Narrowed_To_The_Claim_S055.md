> **DISPOSITION, Session 267, 12 August 2026.** Written home. The Harness's H5 description now carries Code's proposed wording word for word: the check refuses a turn that calls a page finished while its record is open, and every other turn passes with the open chapters named unconditionally. Kain's instruction is quoted beside it, and the reason the earlier wording failed is recorded so nobody re-introduces it. Recorded at Harness Version 3.2. Archived.

# RULING: H5's DSRD 6 record check refuses the claim, not the turn (Kain, S055)

**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Filed under Harness Rule 14:** a ruling given in session, acted on the same session and recorded here so the owning document carries it.
**Owning document:** `000__THE_HARNESS.md`, Layer 2, the H5 description. Version 3.0's sentence about H5 needs one clause changed; the exact wording is proposed at the foot of this file.

## Kain's instruction, in his words

"H5's DSRD 6 record check blocks SESSION END, not just page completion. It armed on every attempt to close S054 once a page template had been edited. Narrow it so it refuses only a page being declared done, and reports 'built, gate open: {chapters}' at session close instead. This is Code's own S054 design error, and as written it will block the end of every future session that touches a page template until that page's record is fully closed."

## The defect, stated plainly and owned

It is mine, from S054, and it is a design error rather than a bug. H5 is wired to the Stop event, which fires at the end of **every assistant turn**, not at the moment a page is called finished. I wrote the record check as a refusal of that event. The consequence, which I did not see when I built it: once a single-page template had been edited anywhere in a session, no turn could end, and therefore the session could not close, until that page's record was completely filled. That includes the four lines Code is explicitly forbidden to fill (chapters 6, 7, 8 and 9 on `/reviews/`), so the only escape was a rule break.

It armed on every attempt to close S054. Left as written it would have blocked the end of every future session that touched a page template.

The deeper error is worth naming because it is a pattern: I read Rule 6 as being about the moment work stops, when what it actually governs is **the word**. Rule 6's sentence is "The word 'done' may only appear with two things attached". Ending a turn is not the word.

## What it does now

**It refuses only a completion claim.** The block arms where the turn's closing text carries a completion word (`done`, `complete`, `completed`, `finished`, `ready`, `signed off`, `good to go`) and something naming that page, in the same sentence, while that page's record is missing or open. Requiring both halves in one sentence is what stops an unrelated "the About stylesheet deletion is done" reading as a page claim in a turn that also touched a page template.

`shipped` is deliberately not on the list. A ship is a change set, proved by Rule 9's push and Rule 6's gate printout, and "shipped v0.60.16 with the reviews heading fix" is a true sentence about a page whose record is properly still open.

**Every other turn passes, and prints Rule 6's own sentence.** The notice reads:

```
H5 DSRD 6 RECORD: /reviews/ built, gate open: §6 AI visibility, §7 Accessibility,
§8 Ease of use, §9 Speed.
Rule 6 asks for those words in any report of this page. Not a block: the turn ends normally.
```

**The notice is not conditional on the refusal.** It prints whether or not anything was claimed, and prints again whenever the record's state changes. This is the S054 lesson applied to my own fix: a check that goes quiet when it decides not to refuse is a check that reads as clean, and five instruments did exactly that in one session. There is no silent pass here. The worst outcome the permissive half can produce is an **unrefused** claim, never an unreported one.

## The acceptance run, in both directions

Kain's standing lesson from S054 is that a check must be made to say no on a case whose answer is already known before its yes means anything. The run is a file, `harness/h5_record_acceptance.py`, so it can be re-run rather than re-argued. Seven cases, all passing:

```
PASS  the real /reviews/ record reads open at 6,7,8,9 (expected 6,7,8,9)
PASS  SILENT expected SILENT  case 1  nothing but a stylesheet edited
PASS  NOTICE expected NOTICE  case 2  page edited, ordinary turn (S054 used to refuse this)
      notice says: H5 DSRD 6 RECORD: /reviews/ built, gate open: §6 AI visibility, §7 Accessibility, §8 Ease of use, §9 Speed.
PASS  BLOCK  expected BLOCK   case 3  page edited, the turn calls the page done
PASS  BLOCK  expected BLOCK   case 4  page edited, no record at all, the turn calls it done
PASS  SILENT expected SILENT  case 5  page edited, record fully closed, the turn calls it done
PASS  NOTICE expected NOTICE  case 6  page edited, Rule 6's own honest form

7 of 7 passed.
```

Case 2 is the S054 defect: that turn used to be refused. Case 5 is the one that makes the rest mean anything, and it is the case I skipped at S054 on other instruments: **a fully closed record allows a page to be called done.** Case 0 runs the real reader against the real `/reviews/` file with nothing substituted, so a synthetic record set that flattered cases 5 and 6 would still be caught there.

## One judgement call, flagged rather than hidden

Kain's words were "reports at session close". A Stop hook cannot tell a session close from any other turn end, so I cannot implement that literally. What I built instead: the notice prints on the first turn after a page template is edited, and again on any turn where the record's state has changed since it last printed. Repeating an identical line at the end of every turn would make it wallpaper, and this line has to still be read on the turn that matters. If Kain wants it on every single turn instead, that is a one-line change.

## The document change this needs

Harness Version 3.0's H5 sentence currently reads that H5 "blocks completion while the record is missing, or any chapter line reads fail or not run". Proposed replacement, for Chat to write with Kain's approval:

> where the finished work is a page, H5 opens that page's `DSRD6_RECORD.md`. A turn that calls the page finished while the record is missing or open is refused. Every other turn passes, with the open chapters named in Rule 6's own words: "built, gate open: {the open chapters}". The naming is unconditional, so an open record is never passed in silence.

## Shipped

Committed and pushed as `0c81d28`, "harness: H5's record check refuses the claim, not the turn". Files: `harness/h5_completion.py`, `harness/h5_record_acceptance.py` (new), `harness/README.md`. No theme output changed, so there is no page to render.

*No em or en dashes in this file; checked before writing.*
