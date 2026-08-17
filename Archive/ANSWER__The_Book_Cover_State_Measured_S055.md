> **DISPOSITION, Session 267, 12 August 2026.** Acted on. The book covers card is closed as Done with the measured counts written into it: 601 rows, 601 covers, 0 missing. The crossed session number is corrected on the card. The one finding that is not about covers, the upload file still carrying the nineteen removed books, is written onto the Knowledge Hub Master Spine card and put to Kain as a decision. Archived.

# ANSWER: the book cover state, measured. The cover set is whole; one downstream file is not

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Answers:** `QUESTION__Current_Status_Of_The_Book_Cover_Images_S266.md`, all five parts.
**Everything below is a count from a file, read this session. Nothing here is recalled.**

Read from `Book_Note_Master.xlsx`, sheet `Master v4 (S044 Contract)`, and the `Book Cover Images` folder, both in the Book Notes Source Bank folder.

## The short answer

**Kain is right: the cover job is finished.** Every row on the list has a cover, and every cover it names is really on disk. **But the removals stopped at the master.** The upload file still carries all nineteen removed books, and it is the file an import would read.

## 1. How many rows are on the list now

**601 rows.** Read from the data sheet's row count, excluding the header and blank rows.

The archived `Book_Note_Master__superseded_S053_pre_removal.xlsx` carries **620**, so **19 were removed**. That matches Kain's account of removing the books where no decent cover could be found.

## 2. How many rows have a cover image file that actually exists

**601 of 601, matched row by row.** Every `book_cover_image` value was resolved to a filename and looked for in the folder; none was missing. `cover_status` reads `ok` on all 601 rows, with no other value anywhere, so the `low_res` question that was open at S049 has dissolved exactly as the S260 commission hoped it might.

## 3. How many rows still have no cover

**None.** Zero rows have an empty `book_cover_image`, and zero name a file that is not there.

## 4. How many cover files sit in the folder with no row pointing at them

**Twelve, out of 613 files in the folder.** All twelve belong to removed books, so they are leftovers rather than strays:

`becoming-a-helper.jpg`, `doing-cbt-david-tolin.jpg`, `helping-skills.jpg`, `how-to-live.jpg`, `it-s-not-how-good-you-are-it-s-how-good-you-want-to-be.jpg`, `my-voice-will-go-with-you.jpg`, `person-centered-psychotherapies.jpg`, `skills-in-person-centred-counselling.jpg`, `the-bhagavad-gita.jpg`, `the-moral-animal.jpg`, `the-power-of-vulnerability.jpg`, `the-wisdom-books.jpg`.

**Nothing needs doing about them urgently.** 613 files minus 601 in use is 12, and the twelve are exactly the removed books that had found a cover before they were dropped. Deleting them is tidy, not necessary, and I have not deleted anything.

## 5. Were the removed books removed from every place they lived? No

**This is the one finding, and it is the answer to the question that was worth asking.**

`Book_Note_Upload.csv`, sitting beside the master in the same folder, **still carries all nineteen removed slugs**. It has 621 lines, so it is still the 620-row file, last written 2026-08-06, before the removals.

The nineteen still in it:

`becoming-a-helper`, `cognitive-behavioural-therapy-with-couples-and-families`, `compassion-and-self-hate`, `doing-cbt-david-tolin`, `helping-skills`, `how-to-live`, `it-s-not-how-good-you-are-it-s-how-good-you-want-to-be`, `my-voice-will-go-with-you`, `person-centered-psychotherapies`, `set-boundaries-find-peace`, `skills-in-person-centred-counselling`, `the-bhagavad-gita`, `the-cbt-toolbox`, `the-decision-book`, `the-dhammapada-easwaran`, `the-mindfulness-and-acceptance-workbook-for-anxiety`, `the-moral-animal`, `the-power-of-vulnerability`, `the-wisdom-books`.

**Why this matters more than it looks.** That folder's own Read Me makes the upload CSV a derived file, regenerated from the master. It was regenerated at S050 after the ISBN run and has not been regenerated since the removals. So the master says 601 books and the file an import would actually read says 620, and **nineteen books Kain deliberately removed would come back the moment anybody imported it.**

It is a two-minute regeneration from the master on the contract columns, and it is not commissioned, so I have not done it. Say the word and it is done in the next session.

**One place I could not check:** the live database holds **one** `book_note` post, so nothing is imported yet and no removed book is live. That is the good version of this problem: the gap is in a file, not on the site.

## What the board can say

The cover set is whole, with a measured number behind it: **601 rows, 601 covers, 0 missing.** The Knowledge Hub Article Page and Book Note Page work can begin on that basis.

The one caveat to carry onto the card: **the upload file is stale by nineteen rows and must be regenerated before any import**, or the removals undo themselves.

## One thing settled in passing

The session-number confusion in `INSTRUCTION__Harness_3_1_Session_Report_Rule_S266.md` is settled by the file names rather than by anybody's memory: the archive holds `Book_Note_Master__superseded_S053_pre_second_cover_pass.xlsx` and `Book_Note_Master__superseded_S053_pre_removal.xlsx`. **The cover work was S053, not S055.** No report is owed for a session that did not do it, and S053's own report is a separate question if you want one.

*No em or en dashes in this file; checked before writing.*
