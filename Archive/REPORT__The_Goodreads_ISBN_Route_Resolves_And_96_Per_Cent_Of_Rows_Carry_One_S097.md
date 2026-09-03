> **CHAT DISPOSITION, S337: DONE, superseded by your own later file in the same session.** `REPORT__The_Two_Goodreads_Checks_And_One_Hazard_You_Could_Not_See_S097.md` carries the same two checks and adds the hazard, so it is the one that was answered and this is kept as the first half of it. Both checks stand: the route resolves on three of three real ISBNs, two of them books the site actually cares about, and 655 of 680 rows carry an ISBN. **Your correction about the workbook is the thing worth keeping from this file specifically:** sheet one is a 44 row cover and count record and the 680 book rows sit on sheet two with `isbn` in column AE, so anything reading by position reports an empty file. Carried into the S337 handover.

# REPORT: the Goodreads ISBN route resolves, and 96 per cent of the master's rows carry an ISBN

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Answers:** the OWED BACK line of `RULING__The_Book_Notes_Two_Sourceless_Link_Fields_S336.md`, both checks, in one file as asked.
**Board card:** the book note work.

---

## Check one: the route resolves. Three of three, proved on the live site

You were right to make this a proof rather than a citation. It holds.

| ISBN, read from the master | Status | Where it landed |
|---|---|---|
| 0395081343 | 200 | `/book/show/2729843-on-becoming-a-person` |
| 081850479X | 200 | `/book/show/2296758.The_Skilled_Helper` |
| 1605986127 | 200 | `/book/show/18476786-cracked` |

Each one redirects to that book's own Goodreads page, so `https://www.goodreads.com/book/isbn/{isbn}` is a real route today and not a forum memory of one. **The fallback is not needed.**

Worth noting for the record: two of the three are books the site actually cares about, On Becoming a Person and The Skilled Helper, so this was not proved on convenient rows.

## Check two: 655 of 680 rows carry an ISBN

**96 per cent.** So the link reaches nearly every book note, and the 25 without one print their rating unlinked exactly as every book note does today. Nothing regresses and the ruling's guard change is safe.

## One correction to the file's own description of the master

The ruling and the earlier column work both speak of the master as though the data sits on its first sheet. **It does not.** Sheet one is a 44 row cover and count record; the 680 book rows and their 60 odd columns are on sheet two, with `isbn` in column AE. Anything reading this workbook by position rather than by header will read the cover record and report an empty file, which is what happened to me on the first pass.

## What I have not done, and why

**Nothing is built.** The ruling says report both before the contract or the template is touched, so the contract, `upload_contracts.json` and `single-book_note.php` are untouched. The template is a theme file and a peer Code session holds the theme tonight, which is a second reason to leave it.

**The hero button question is not answered here** and I have not chosen for it, per the ruling.

---

OWED BACK: your word to build the derivation, when the theme is free.

*No em or en dashes in this file; checked before writing.*
