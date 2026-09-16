# REPORT: every book note read off the install, twice. 124 of 125 at the ceiling, one short, and it is the same file rewritten rather than a second copy

> **CHAT DISPOSITION, S365: READ AND CLOSED.** 124 of 125 at the ceiling noted; boundaries-cloud's link and the 74 older records commissioned to Cowork (`BRIEF__Rebuild_The_74_Older_Format_Book_Note_Records_S365.md`). Board: Book notes card.

**Filed by Claude Code, Session 119. Date:** 15 and 16 September 2026.
**This file was rewritten on Kain's instruction, "rescore all of the 125 book notes and reset the table".** The earlier table it carried, 112 at 88 with thirteen short, was true when it was written and is now superseded by the run below. It is not kept beside this one: one canonical file, one canonical place, so nobody can quote the old numbers by accident.

---

## The run

Every book note on the install, read one page at a time in its own editor with `score_run.py --ids`, plain, no `--refresh`. The id list was rebuilt off the install for this run rather than reused from earlier in the session. **125 posts, all published, no drafts.**

One page came back as a zero, flagged by the tool itself as "zero held to deadline, check the stored score", which is the tool saying it failed to read rather than that the page scores nothing. It was read again on its own and is included below at its real value. No zero is reported as a score in this file.

## The table

| Score | How many |
| --- | --- |
| 88 | 124 |
| 82 | 1 |

**124 of 125 sit at 88, which is the ceiling a book note can reach** (its one image is the cover, and Rank Math scores images at 1 of 6; measured and filed at S103). Kain's bar for the type is 88, ruled at S344 in his own words: "I'm happy with the 88 score, to be honest."

**One page is short: `boundaries` at 82.** Its cause is measured and is not shared with anything else on this list.

## What changed between the two runs, and why

The first run tonight found thirteen short: seven at 21, one at 24, one at 82, five at 86. All twelve of the low ones except `boundaries` were stuck behind the same wall, and that wall was in Code's own tooling rather than in anybody's writing:

- Their records are an older generation that `book_note_import.py` could not parse, so the importer refused the whole record and no correction could ever reach their pages.
- **The correct values were already sitting in those records.** `resilient` held the keyword "Resilient" while its page held "resilient rick hanson book summary"; all five of the 86s held a cover alt while their cover attachments held none.

Kain ruled: "yes, fix the importer". `--fields-only` now writes meta and terms and nothing else, so a record whose body cannot be parsed can still carry a correction, while a body that cannot be parsed is never sent near a page. **No body was touched and no modified date moved**, per DSRD 6 section 6. Theme commit `ccbef87`.

Three faults were found while proving it, each caught on one page before the other twelve were touched, and all three are named in full in that commit. The one worth repeating here: **pushing the records' own keywords took three pages from 86 down to 72**, because those records hold the `{book} by {author}` form. Corrected to the book's own title, read from each record's `source_book_title`, which is what DSRD 6 section 5 item 11 requires in Kain's S349 ruling, "Book note: the book's title". All three then read 88.

## The one still short, and the one thing it needs

`boundaries`, post 35940, 82. Read with `score_breakdown.py`: it loses 5 points on `linksHasInternal` and nothing else is failing. **Its body carries no link to any other page on the site.** Its own record plans exactly one, in its Search and Citation Brief item 7: "Internal: [/learn/personal-growth/](/learn/personal-growth/)". That link was never placed. A passing note, `utilitarianism`, carries two in its body.

Placing it means choosing which sentence becomes the link, and Harness Rule 8's own test is that if a reasonable person could write it two ways, Code does not write it. So it waits on Cowork, and the moment it lands it is one `--fields-only` run and a re-score.

## Still owed to Chat, and unchanged by this run

**Six book note records hold a focus keyword with the author's surname in it**, against the S349 ruling. Three are named in `ASK__Three_Book_Note_Keywords_Still_Carry_The_Authors_Surname_S119.md` (authentic-happiness-seligman, difficult-conversations-patton, the-republic-plato). The other three are the ones that scored 72 tonight: emotional-leonard-mlodinow, free-will-sam-harris, nature-emerson. Their **pages** are corrected and at 88; their **records** still hold the wrong form, so the next person to run a full import from those records would undo tonight's correction. That is the reason this matters rather than being tidiness.

**And the larger finding stands:** 74 of the 153 book note records still carry the older section headings. `--fields-only` means a metadata correction can now reach all of them, which is what tonight proved. A body correction still cannot, and would need the records rebuilt. That question, and its cost, is in `ASK__Twelve_Book_Note_Records_Are_An_Older_Generation_And_Their_Pages_Cannot_Be_Corrected_Until_They_Are_Rebuilt_S119.md`.

OWED BACK: Cowork placing one internal link in `boundaries`, and the six keyword records corrected.

No em or en dashes in this file; checked before writing.
