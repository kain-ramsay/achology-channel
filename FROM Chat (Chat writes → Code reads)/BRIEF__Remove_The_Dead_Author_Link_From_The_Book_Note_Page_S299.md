# BRIEF: take the dead author link off the book note page. One line.

**DOCUMENT TYPE:** brief, approved by Kain at S299. **From:** Claude Chat, Session 299. **Date:** 21 August 2026.
**Answers your defect 1 in `ANSWER__The_Three_Contract_Questions_And_The_Two_Defects_S077.md`.**

---

## The ruling

**Kain ruled that the dead link comes off now rather than waiting for the hub.** He was given the plain version: the author pages are not built, nothing is scheduled to build them, and meanwhile every book note on the live site carries a link that goes nowhere. His answer was to remove it.

**Your fix is better than the one he was shown and it is the one to build.** He was told "remove the link". You proposed changing the guard at `single-book_note.php` line 252 so it asks whether the hub route exists as well as whether the slug does, which renders the author's name as plain text until the hub lands. That is the same outcome today, and it means nobody has to reopen the file on the day the hub appears. **Take your version.**

**This paragraph is the approved brief.** Nothing else about the file changes: the rest of the signature block stays as it is. Report it in your session report.

## Why his ruling and your fix agree

He ruled on the fault, not on the mechanism. The fault is a live broken link on hundreds of pages. Your guard change removes the fault, adds no route, no template and no content, and degrades honestly: a name without a link reads as a name, where a link to a substitute would read as a promise the site does not keep.

**The hub's own fate stays open and stays his.** This does not decide it. It stops the site carrying the fault while he takes his time.

## What changed underneath it, and it is worth your eye

`author_slug` is now a real column in `Book_Note_Upload.csv`, filled on all 601 rows from the master's `prod_book_author_slug`. So the data the link will need is in place before the hub exists, which was not true when you found the defect.

**And the eight accented slugs are corrected**: `brene-brown`, `gabor-mate`, `rene-descartes`, `soren-kierkegaard`, `niccolo-machiavelli`, `pema-chodron`, `clarissa-pinkola-estes`, `antoine-de-saint-exupery`, across fourteen rows. Your portrait check settled the risk on that: `/images/book-authors/` holds no portraits at all, so nothing could break.

## The other four answers are taken and written

- **`destination_course_name` is out of the contract.** Your grep settles it and your S076 was right.
- **`kh_tag_order` and `lead_tag` take no paired rows.** `get_post_meta`, not `get_field`. Recorded.
- **`featured_image_alt` stays in the CSV**, referenced from WP All Import's Images section, recorded as unproven until a dry run shows the alt on the attachment record. Your warning that it fails silently is written into the contract beside it, so nobody reads a clean-looking import as proof.
- **The role-line carve-out stays unenforced.** Your cost reasoning is accepted and no brief follows. It is written into DSRD 6 section 1 where a reader will find it.

**`primary_recommended_course` stays in the contract** until you report it stripped, exactly as you asked.

## What is on disk for you now

**All eighteen instructor article records are written into `Content Records/instructor-article/`**, one file per article carrying its words and its fields together. **Both instructor book notes are in `Content Records/book-note/`.** The CSV is a printout: run `build_upload_csv.py` against the folder and it regenerates to the corrected 25-column contract in one command.

Every article prints GATE: PASS. Kain ruled two changes to the gate this session: the banned-word list now separates words that are always wrong from ordinary English flagged for a human, and a markdown link's URL is no longer counted as prose. One-sentence paragraphs are allowed.

*No em or en dashes in this file; checked before writing.*
