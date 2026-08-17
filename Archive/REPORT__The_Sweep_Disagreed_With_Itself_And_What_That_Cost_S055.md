> **DISPOSITION, Session 267, 12 August 2026.** Answered at the session close. The sweep runs one page at a time from now on: a false failure costs more than fifteen minutes of waiting. The rule that a machine fail line is evidence rather than a verdict goes into the record template itself so it travels with every record. The reviews chapter 11 line the self-referential loop destroyed is dictated back word for word as Chat's line, with its provenance, for Code to transcribe rather than re-author, and he checks every other swept page for the same loss. Nothing owed on the loop itself; it is fixed and proved. The finding inside this file, that a check is a claim about the world and an untested claim is a guess with a printout, is owed a vault note. Archived.

# REPORT: I ran the identical sweep twice and the two runs disagreed. Here is why, and what it means for the records

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Read this before anybody acts on a fail line in a DSRD 6 record.**

## What happened

I ran the machine sweep across the live pages, then ran it again over the same pages with the same code against the same site. **The two runs disagreed on four chapter lines.** Same input, different answer, which is the one thing a measuring instrument may never do.

That disagreement was not noise to be shrugged at. It had two separate causes and both are worth your attention, because one of them was quietly corrupting the records.

## Cause one: the record check was manufacturing its own failure

**This is a real defect and it is fixed.**

Check 16 reads a page's record and fails when the record carries any failing line. I had put check 16 inside chapter 11's evidence list. So:

`/reviews/` §5 fails on the sitemap → the record now carries a fail → check 16 fails → **§11 fails, purely because §5 did** → that §11 failure is written back into the same record → check 16 would fail again on the next run.

One chapter's failure was manufacturing another chapter's failure through the record they both live in, and each run made the record worse. `/reviews/` §11 had read `pass, 2026-08-11` from its real S053 gate run; the loop overwrote it with a fabricated failure.

**The fix:** a record is not the live page, so the record check was never §11's evidence. It is out of §11's list and stays in the gate's own printout where it belongs. Confirmed on a corrected sweep: the fabricated §11 failure cleared on `/reviews/`, `/testimonials/` and `/policies/` alike, so the loop was hitting every swept page and not just the one I noticed.

**One thing the loop destroyed, and I cannot put it back myself.** `/reviews/` §11 read **`pass, 2026-08-11`** before the loop overwrote it. That pass came from the real S053 twelve-chapter gate run, and it is a split machine-and-Kain's-eye judgement, not a machine line. The corrected sweep cleared the fabricated failure, but clearing resets to `not run`, because the machine may only clear what the machine wrote and can never restore a pass it did not make.

So **`/reviews/` §11 now reads `not run` and it should read `pass, 2026-08-11`**. I have not restored it, because §0 keeps me out of judgement lines on a page I built, and putting back a line I destroyed is still writing a judgement line. The exact previous value is above; whoever owns that line can restore it in one edit. I would rather cost you that round trip than quietly re-author a judgement on my own build.

**Check the other swept pages for the same loss before restoring just this one.** Any page whose §11 carried a genuine pass before today will have been reset the same way. `/reviews/` is the only one I know of, because it is the only page that had any closed lines before this session, but that is reasoning rather than a check I have run.

**Why it matters beyond the one line:** this is a self-referential check, and self-referential checks get worse every time they run rather than staying wrong at a constant level. It would have looked like the page degrading.

## Cause two: some measurements are flaky under load, and that is not fixed

Two lines went the other way. `/policies/terms-and-conditions/` §2 and §10 had been failing on `page-container: 1440px is neither 1200 nor 880` and a boundary spacing miss. On the second run **both passed and were cleared**, without a single line of the page or the theme changing in between.

The most likely cause is the sweep driving fifteen pages through one queued SSH connection: a page measured before its layout settles reports the viewport width instead of the container width. I have not proved that, and I am not going to state it as fact.

**What this means for reading the records, and please carry it onto the board:** a `fail` line written by the machine is evidence, not a verdict. A single sweep can produce a false failure. **Any fail line worth acting on should be reproduced by a second single-page run before anybody fixes anything on the strength of it.** That is one minute per line and it is cheap next to fixing a defect that was never there.

## What saved it, and it was built hours earlier for a different reason

The clearing path. Earlier today I noticed the sweep could write a fail but never clear one, so a fixed defect would look broken for ever. **That same mechanism is what let these records correct themselves** rather than carrying two false failures permanently. It only clears the machine's own fails, never a human's.

## The method, because it is the only part of this worth generalising

None of the above was found by reading the code. **It was found by running the same thing twice and requiring the two answers to match.** The standing S054 lesson was "make an instrument say no on a case whose answer you know". This is its other half: **make it say the same thing twice on the same input**, and treat any disagreement as a defect in the instrument until proved otherwise.

I have now been caught by four instrument faults in this session alone: three checks reading English as data, and this. The pattern is not carelessness in any one of them. It is that a check is a claim about the world, and a claim nobody tested against a known answer is a guess with a printout.

## What I need back

Nothing on cause one; it is fixed and proved.

On cause two, a decision I should not make alone: **should the sweep run pages one at a time rather than in batches**, trading roughly fifteen minutes of wall clock for measurements that reproduce? My reading is yes, because a false failure costs more than the wait, and the sweep runs rarely. But it slows a job you may want fast, so it is yours and Kain's to weigh.

*No em or en dashes in this file; checked before writing.*
