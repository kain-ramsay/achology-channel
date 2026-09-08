> **CHAT DISPOSITION, S353: acted on, archived.** All three owed backs closed: the title form is written into DSRD 2 section 3.1; the master's `post_title` column is briefed to Cowork whole, with the unpublished records (`BRIEF__Bring_The_Masters_Title_Column_And_The_Unpublished_Records_To_The_Ruled_Title_Form_S353.md`, TO Cowork), because Chat cannot write a spreadsheet file; and Kain ruled yes to `.bn-body` joining `PROSE_HOSTS` and to the 92 machine chapters re-running, carried in `RULING_AND_BRIEF__Apply_The_Fifteen_Placements_Push_The_39_Add_bn_body_To_The_Page_Gate_S353.md` (FROM Chat). Board: Book Notes and the 65 published book notes, updated at close.

# RULING: Kain rules the book note title form, and orders the publish gate fixed properly

**DOCUMENT TYPE:** ruling, from Claude Code, Session 107. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Filed under Harness Rule 14:** both rulings were given by Kain directly in the S107 sitting and were acted on in the same sitting. This file exists so Chat writes them into the documents that own them.
**Board cards:** Book Notes; the 65 published book notes; the harness and instruction sets.

---

## 1. The ruling on the title form, in Kain's own words

He raised it himself, unprompted, having looked at the pages:

> "many of the book notes you have just published, don't have their titles optimised to make them more enticing to click into - : Summary and Key Ideas or the like - do you know what needs to happen with these?"

Code brought back the measurement and one recommendation, that all 92 match the 66 already carrying the form. His ruling:

> "Yes, please do all 92 tonight Claude - thank you"

**So the book note's `post_title` is the book's title, then a colon, then "Summary and Key Ideas".** That is now the type's title form. The one live exception is `what-do-you-say-after-you-say-hello`, whose title ends in a question mark and therefore reads "What Do You Say After You Say Hello? Summary and Key Ideas" with no colon. That is correct English and is not a drift.

**The document that owns this:** DSRD 2's book note section, beside the type's other field rules. Chat's to write.

## 2. What the measurement found, because the cause is not what it looked like

The good titles were never lost. **Every one of the 25 records already held a fuller title**, written as "Understanding {Book}: Key Ideas". The install carries the bare book name because `book_note_import.py` keeps the **master spreadsheet's** value for any column the run does not name in `--overwrite-columns`, and `post_title` was not named. The master's `post_title` column is the bare book title, checked by hand on three rows rather than inferred.

**This is the trap the S106 close already recorded, reaching a new column.** It was recorded for the keyword columns; it is not specific to them. **Every future book note import names `post_title` in `--overwrite-columns` too**, and Kain instructed the same thing at the S107 open in general terms.

**Kain has ruled the master column, in the same sitting, in his own words:**

> "tell chat to fix the spreadsheet column"

**So this is not a question and it is not Code's recommendation any more. It is his instruction and it is Chat's to carry out.** The master spreadsheet's `post_title` column still holds the bare book titles on all 25 rows, so a future import that forgets `--overwrite-columns` reverts every one of them. **The column is brought into line with the ruled form: the book's title, a colon, then "Summary and Key Ideas".** Code has not touched the master and will not, because the Shared Rules section 4 makes the Book Note master Chat's alone.

**The reason he was given before he ruled, recorded so nobody re-derives it:** the alternative was making the flag mandatory in the importer, and a rule that depends on somebody remembering a flag is the exact shape of the fault this file is about. Fixing the column removes the fault rather than guarding it.

**Two things worth doing in the same pass, named rather than assumed.** The 25 rows are the ones measured tonight, but the column should be walked whole: if any of the other 121 rows carries a bare title, it will do the same thing on its first import. And the record's own `post_title` and the master's should now read the same string, so a future disagreement between them is visible rather than silent.

**Also for Chat, and it is a record-shape defect rather than a content one:** 13 of the 25 book note records had no title heading on their first line at all, against the pattern every other record follows. Code inserted one carrying the ruled title, in the same pass, and the diff carries no other kind of line.

## 3. The ruling on the gate, in Kain's own words

The title change could not reach the install because `publish_gate.py` refused all 25. Code hand-checked one page before believing the refusal, found the pages perfect and the gate at fault, and used `--override` quoting Kain's ruling rather than touching the wall to get its own change through. Kain, told that the gate's own fault would go to Chat as a question:

> "yes, fix the gate properly please soo Claude"

**Acted on in the same sitting. Theme commit `2af3133`.**

## 4. What the gate fault actually was, because half of it would have stayed hidden

**First half.** `BODY_BLOCK` opened only on `kh-article__body`, the article template's wrapper. A book note's body is `bn-body` and a help answer's is `help-single__body`, so `rendered_body` returned `None` on both types, and `None` is a refusal on that wall by Kain's own ruling.

**Why it was never seen.** Two things at once. `rendered_faults` waives an unreadable body on a **first** publish, which is how 92 book notes and 250 help answers went live without it ever mattering; and nothing had ever run `--update` against either type until this ruling did.

**Second half, and it is the part worth Chat's attention.** Widening the openers alone made the gate return a string, so the obvious test would have gone green. It would still have been wrong: the tail ended the block at the first `<aside`, and a book note carries its Table of Contents as an `<aside class="kh-aside">` **inside** the body, four lines in. The gate would have read **14 words of a 1,160 word note** and every check downstream would have been measuring the meta strip. **A fragment reads as readable.**

So the acceptance suite is judged on the page's own declared word count rather than on readability. `publish_gate_body_acceptance.py`, 13 cases, and it was **proved red before it was proved green**: 5 failures against the original pattern, 2 against the half fix. Per the S050 rule, the question asked first was what would make it go red.

## 5. One thing Code did not take, and it is a question for Chat

**`page_gate.py` carries the same blind spot.** Its `PROSE_HOSTS` reads `.kh-article__body, .help-single__body, .policy-body--doc`. **`.bn-body` is absent**, so on a book note the headings inside the prose are not recognised as prose headings.

**Code has not changed it, deliberately.** Adding `.bn-body` there would **remove** results from a check rather than make a check run, which is a loosening, and a gate loosening itself at night on its own judgement is the exact shape this project refuses. It also touches every published book note's DSRD 6 machine chapters, so the answer changes records rather than only code.

**The question:** should `.bn-body` join `PROSE_HOSTS`, and if so, do the 92 published book notes' machine chapters need re-running against the corrected check?

---

OWED BACK: the title form written into DSRD 2; the master spreadsheet's `post_title` column brought into line on Kain's instruction, walked whole rather than only the 25, with the row count confirmed; and the answer on `page_gate.py`'s `PROSE_HOSTS`.

*No em or en dashes in this file; checked before writing.*
