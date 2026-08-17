> **DISPOSITION, Session 267, 12 August 2026.** Recorded and superseded. Its H5 description is overtaken by the narrowing ruling filed the following session, which is now in the Harness at Version 3.2. What it delivered that still stands is written onto the page readiness records board card: the record machinery, the record template, and the three faults Code found and fixed on the way, including the one that mattered most, a gate that was failing open in silence. Archived.

# BRIEF: H5 now actually reads the DSRD 6 record

**From:** Claude Code, Session 054. **Date:** 2026-08-12.
**Authority:** Kain, directly in session: "fix the harness gate so that it actually checks the record".
**Delivers:** the H5 half of `COMMISSION__DSRD6_Gate_Machinery_Backfill_And_Why_Question_S264.md` Part 1, with its acceptance printout. The rest of Part 1, the per-page records and the scoreboard, is not built.

## 1. What was wrong

**Harness Version 3.0 says H5 was strengthened at S264 to "open that page's `DSRD6_RECORD.md` and block completion while the record is missing, or any chapter line reads fail or not run". The document said it. The code never did.** Checked at the S054 close: `h5_completion.py` contained no mention of a record, and no page on the site had one.

That is worse than the gap it replaced. The old gap was known: everyone understood the full gate had run on one page. This one reads as closed, so the next person to look, including me, would have trusted it.

## 2. What is built now

A fourth check in H5, after the component gate and before the push. It arms only on an edit to a template that renders exactly one page (`page-{slug}.php`, `policies-content/{slug}.php`), finds that page's record **by the record's own `Page:` line** rather than by folder name, and blocks while the record is missing or any chapter row reads `not run` or `fail`, naming the open chapters.

Finding a record by its own declaration rather than by a mapping table in the hook is deliberate: a list kept in the hook is one more thing to go stale, which is what standing rule 24 exists for.

**A record template is filed** at the root of the website pages folder, matching DSRD 6 §0's definition: the four states, the runner per chapter, the separation-of-duties note, and the §12 exemptions block.

## 3. Three faults of my own, found on the way

Each was caught by running the check against a case where the answer was already known. Each is written into the code beside the fix.

1. **It searched for a folder named "Achology Website Pages". The folder is numbered "03. Achology Website Pages".** So it found no records and reported every page as having none. It failed safe, but a check that always says the same thing is not a check.
2. **The open-line pattern did not allow the space in `| not run |`.** It matched nothing, so the gate passed every open record in silence. **Failing open is the one direction a gate must never be wrong**, and this is the third time this session an instrument has done exactly that.
3. **H3 blocked the record files themselves.** Its mirror rule matches any filename beginning `DSRD` plus a digit, and DSRD 6 §0 names the file `DSRD6_RECORD.md`. Every record was refused before one could be written. Fixed with an exception for exactly two filenames, kept as a closed list rather than a prefix so the mirror rule keeps its teeth. Proved: records allowed, `DSRD_6_...md` and `DSRD 7 copy.md` still blocked, writes into the DSRD folder still blocked.

## 4. The acceptance printout

Five cases. The fourth is the one that matters.

| Case | Required | Result |
|---|---|---|
| Page whose record carries `not run` lines | block | **blocked**, naming §6, §7, §8, §9 |
| Page with no record at all | block | **blocked**, quoting DSRD 6 §0 |
| Non-page work (`shared-parts.php`, `cards.css`, `page_gate.py`) | do not arm | **allowed**, correct |
| **A fully closed record** | **allow** | **allowed** |
| One line flipped to `fail` | block again | **blocked**, naming §9 |

**Case four is why the others mean anything.** A gate that can only ever refuse proves nothing when it refuses. It was tested by closing every line in a real record, confirming the pass, then restoring the file to its true state.

## 5. The first record exists

`/reviews/` has its `DSRD6_RECORD.md`, filed in its own design folder. **Machine lines only**, written from this session's gate run. Chapters 6, 7, 8 and 9 read `not run` and Code has not touched them: chapter 8 is Chat's by Kain's S263 ruling, and 6, 7 and 9 need checks Part 2 of the commission has not built yet.

## 6. What this does NOT do, stated plainly per Rule 5

- **The blast radius is narrower than the truth.** It arms only on single-page templates. Editing `shared-parts.php`, `header.php` or `cards.css` changes many pages and arms nothing, because nothing in the system maps a shared file to the pages it affects. That mapping is a real piece of design and it is not mine to invent.
- **No records exist for the other 21 pages.** That is Part 3, the backfill.
- **No scoreboard.** That is Part 1's third bullet.
- **`page_gate` does not read records yet.** Only H5 does.
- **Nothing verifies that Code did not fill a judgement line for its own build.** The rule is written into the template in words and enforced by nothing. Worth knowing before it is trusted.

## 7. What I need back

Nothing to unblock it. The remaining parts of the S264 commission are the next session's opener, and this half is done and proved.

*No em or en dashes in this file; checked before writing.*
