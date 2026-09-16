# ASK: three book note records still carry the author's surname in the focus keyword, against the S349 ruling

> **CHAT DISPOSITION, S365: CLOSED.** Kain ruled rebuild all 74; the three keywords are folded into `TO Cowork/BRIEF__Rebuild_The_74_Older_Format_Book_Note_Records_S365.md`. Board: Book notes card.

**Filed by Claude Code, Session 119. Date:** 15 September 2026.
**On Kain's instruction in this sitting:** shown the finding, he said "that makes sense - please send to chat".
**Answers nothing; this is new, found while checking the 26 draft book notes were whole before he published them.**

---

## The ruling this is measured against

`RULING__The_Book_Note_Keyword_Is_The_Books_Title_S349.md`, read this turn, quoting DSRD 6 section 5 item 11 word for word: **"Book note: the book's title."** The same ruling says plainly why the `{book} book summary` form was wrong: "The book's title is in all four. The phrase with 'book summary' bolted on is in none of them."

## The three

Read off the install this turn, and matching their records exactly, so the records are the thing out of step and not the import:

| Slug | Keyword on the page, and in the record | The book's title |
| --- | --- | --- |
| authentic-happiness-seligman | `authentic happiness seligman` | Authentic Happiness |
| difficult-conversations-patton | `difficult conversations patton` | Difficult Conversations |
| the-republic-plato | `the republic plato` | The Republic |

It is the same fault the S349 ruling closed, with an author's surname bolted on in place of "book summary". The address, the SEO title and the cover alt all carry the book's title; the surname is in none of them.

## What this is not

**Not a publish blocker.** All three score 88, which is Kain's bar for the type, so they went to him ready alongside the other 23.

**Not the S342 exception.** That exception covers three `{book} by {author}` keywords and was granted, in the S349 ruling's own words, "because three live addresses could not move". These three are drafts, and a focus keyword is an internal field: changing it moves no address, no title and no word of the body.

**Not mine to fix.** The S349 ruling says it in three words, "Do not edit a record", and Harness Rule 8 says the same. I have touched none of them.

## The ask

Do these three go into the same Cowork correction as the twelve older-generation records in `ASK__Twelve_Book_Note_Records_Are_An_Older_Generation_And_Their_Pages_Cannot_Be_Corrected_Until_They_Are_Rebuilt_S119.md`, or are they small enough to go on their own?

**Either way it is one run on my side once they land:** `book_note_import.py --write --overwrite-columns prod_rm_focus_keyword --slugs <the three>`, then `--push`, then `--verify`, then a fresh score read off the install. The expected movement is none, since 88 is already the ceiling; the point is the record being right, not the number.

One more thing worth having with it: the other fourteen of the seventeen redrafted notes carry their keyword in lower case (`the power of now`, `thinking fast and slow`). Rank Math does not care about case and nothing fails on it, so I have not raised it as a fault, but if the register wants one form it is the same one-line fix at the same time.

OWED BACK: your answer on where the three go.

No em or en dashes in this file; checked before writing.
