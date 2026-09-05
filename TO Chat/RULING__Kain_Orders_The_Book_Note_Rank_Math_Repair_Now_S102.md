# RULING: Kain orders the book note Rank Math repair now, and the titles with it

**From:** Claude Code, Session 102. **Date:** 5 September 2026, about 14:05 BST.
**Ruled by:** Kain, in the S102 sitting, in chat.
**His words, quoted exactly as typed:** *"Claude, all of the book note articles in the website are mailing rank math really poorly - and the titles are also really poor - what full solution can you impliment right now to fix this?"*
**Filed under Harness Rule 14.** These words are also the override quoted on the update clearance minted for the 65 live book note pages this afternoon, because the pages carry failing readiness lines (images, icons, the record) that the S096 override route exists for, and nothing about this repair publishes a page: all 65 are already published and the update leaves their status untouched.
**Board cards:** Book Notes, the psychologist expansion; Page readiness records.

## What he was looking at

Every one of the 65 live book notes scores 20 or thereabouts on Rank Math (61 at exactly 20; one each at 4, 13, 22 and 76), and their Rank Math titles run to the pattern "{Book} by {Author}: Book Notes | Achology", 23 of them over the 60 character limit and 18 carrying a stray backslash where the pipe should be ("Book Notes \ Achology").

## Why, measured this turn and not guessed

One page read test by test with `score_breakdown.py`: every keyword test scores nothing, because the focus keyword on the install is "{book title} book summary" and that phrase appears nowhere: not in the title, the description, the address, the opening, the headings or the picture's alt text. Cowork corrected all 65 records at S338 (`Batch_Report__65_Live_Book_Notes_Keyword_Fix_S338.md`): keyword trimmed to the book title, the phrase written into the opening, alt text, one external link each. **Those corrections never reached the site**, and the batch report says so in its own last section. Two mechanisms held them back: the master's rule that a record never overwrites an approved value, which kept the master's junk keywords; and the importer's field reader, which kept the markdown escape on the pipe, which is the backslash.

## What this ruling authorises, and what it does not

**Authorised:** bringing the 65 live pages level with their corrected records in one update run (body, keyword, title, description), the master and upload sheet refreshed from the records first, every page's score read back afterwards and tabled, and the 22 record titles that ran over 60 characters shortened by dropping the author clause, which is the pattern the other 43 already carry. **Not authorised by these words and not done:** a new title formula. That is wording, it is Kain's, and it is put to him as one yes or no in the same sitting.

OWED BACK: nothing from Chat. The result travels in `REPORT__The_65_Book_Notes_Repaired_And_Rescored_S102.md` when the run completes.

*No em or en dashes in this file; checked before writing.*
