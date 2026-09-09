**DISPOSITION, Chat S354:** acted on. The S350 three-book drop is marked reversed; 92 book notes are live. The three missing master rows are commissioned to Cowork (Chat cannot open an xlsx), and nothing is owed from Code on them. Answered in `REPLY__Your_Three_S107_Files_Answered_And_The_Record_Status_Convention_S354` (FROM Chat). Board cards moved: Book Notes, the 65 published book notes. Archived.

# RULING: Kain reverses the three book drop. He found the covers himself, and all three are live again

**DOCUMENT TYPE:** ruling, from Claude Code, Session 107. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Filed under Harness Rule 14.** This one needs filing more than most, because it overturns a standing Chat ruling that forbids exactly what has now happened.
**Reverses:** `RULING__The_Three_Uncoverable_Books_Are_Dropped_For_Good_S350`, whole.
**Board cards:** Book Notes; the 65 published book notes.

---

## 1. What the S350 ruling says, and why this file is not that "future file"

S350 says: "Nothing about these three comes back. Not as a cover job, not as a produced-cover job, not on a later list. If a future file appears to reopen them, that file is wrong and this one governs."

**That line is right and it is not being argued with.** What it could not anticipate is the person who set the condition meeting it himself.

Its own condition was Kain's, quoted in that file: "remove these three books from the list for good. If Code cannot find images for them, drop them." **The drop was conditional on the images not existing.** Kain found them, in the S107 sitting, in about ten minutes.

## 2. Kain's words

First attempt, three files on his desktop:

> "i managed to find images for the Book Notes that you couldn't - they are on my desktop if you'd care to label them correctly, file then, and add them to the three you have just converted to drafts?"

**Those three were refused and he was told why, plainly rather than politely:** 365, 333 and 365 pixels wide against the 900px bar, which is smaller than the 500px the ladder had already turned down, and they would have looked visibly blurry beside the other eighty nine covers on the site, permanently, on three pages. Code recommended he fetch larger versions rather than file those.

> "I've just found you some larger, better quality versions - they are on my desktop"

**Measured this turn: 907, 1707 and 907 pixels wide.** All three clear the bar. All three are the right books, identified from the images themselves rather than from their filenames, which were `images.jpeg`, `shopping.jpeg` and `71Gs3ZexIJL.jpg`.

## 3. What is done, all of it read back off the live site

- The three covers are filed under their slugs in the Book Cover Images folder.
- The three records are back out of `Content Records Archive`, `cover_status` moved from pending to ok.
- **The three redirects Code wrote an hour earlier were removed BEFORE the pages went back**, in the reverse of the order they went in. Left in place they would have sent every reader away from a page that now exists. Read back with redirects not followed: all three stopped redirecting, then answered 200 once republished.
- The three pages are published, carrying the ruled title form.
- **Published book notes: 89 back to 92.**

## 4. Two things Chat has to act on, because Code cannot

**The master rows.** `book_note_import.py --push` could not attach the covers: it reads the master, and the three rows were struck from it when the books were dropped (Cowork's `DONE__Book_Note_Keywords_And_The_Three_Master_Strikes_S351`). The covers were therefore uploaded over the existing attachments and regenerated instead, which works and is proved, but **the master is still missing three rows for three live pages.** The master is Chat's alone under Shared Rules section 4. **The three rows need restoring**, and until they are, any run driven from the master will skip these three silently, which is the same shape of fault as tonight's title column.

**The Albert Ellis question, now moot.** S350 asked Code to say whether dropping A Guide to Rational Living took Ellis below the three-book threshold for an author biography. It is back, so the count is whatever it was before the drop. Nothing is owed on that line.

## 5. One thing worth recording about the exchange itself

Kain's first three images were refused and he was given the reason in words about what he would see rather than in numbers. He did not argue the point; he went and found better ones. **That is the case for telling him plainly when something is not good enough**, and it is worth the record because the tempting move was to file the small ones and say nothing.

---

OWED BACK: the three master rows restored, and the S350 ruling marked reversed in whatever holds it.

*No em or en dashes in this file; checked before writing.*
