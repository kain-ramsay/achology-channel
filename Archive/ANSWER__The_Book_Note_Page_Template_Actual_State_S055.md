> **DISPOSITION, Session 267, 12 August 2026.** Acted on. Its four answers are written onto the Book Note page board card: the page is built and deployed to the approved design, and only two things are genuinely missing, the hero's rating ticks and the 598 book notes that do not exist in the database yet. The two listing routes have their hook but are unproved. The docblock correction the earlier brief asked for cannot be found in the file, so it is held until the exact line is quoted or struck. Archived.

# ANSWER: the Book Note page template, its actual state, read from the theme this session

**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Answers:** `QUESTION__Book_Note_Page_Template_Actual_State_S261.md`, all four parts.
Everything below was read from the files and the live database this session, not from memory.

## 1. Did the S251 brief reach me? Yes, twice

It arrived as two pointer files, both now in the FROM Chat Archive: `POINTER__Book_Note_Page_Brief_Is_In_Its_Page_Folder_S251.md` and `POINTER__Book_Note_Page_Brief_S252.md`. It was archived after being read, which is why it is not in my S053 standing-files list. The brief itself was read from its one home in the Book Note Page folder, exactly as the pointers intended, and the template's own docblock cites it by name.

## 2. Has build work started? It is built

`single-book_note.php` is 26,107 bytes, last touched 2026-08-11. `book-note.css` is 25,845 bytes. The template's docblock names its sources: the S251 brief, DSRD 9 §32, DSRD 8 §20 (the travelling shelf), DSRD 8 §13 (the closing panel) and DSRD 7 §1.0, and it records the brief's own precedence rule, that where the brief and the approved page disagree the page is correct.

**The nine blocks in the docblock's stated order are built:** header, full-bleed hero, reading zone (note left, shelf right), author signature, hairline, related courses, hairline, next possible steps, rainbow stripe and footer. The docblock also records that the article grid, quote grid, related book note cards and tag pills were removed by Kain at S249 on the rendered page and are not to be reinstated.

**Deployed:** yes. It is in the theme at v0.60.16, which is live on the test site.

**What the template itself records as not built:** the hero's rating ticks, one item, noted at the tick block. One earlier gap closed at S255: the related-courses block used to depend on `primary_recommended_course`, which was never populated; that field is retired and the block now fills from the page's own tags under DSRD 1 §5.7.

**The two per-book listing routes:** the template reads `ach_listing`, which `knowledge-hub-setup.php` §8 sets, so the routing hook exists. I have not verified end to end that both listing routes resolve, and I am not going to say they do on the strength of the query var being read.

## 3. Does the theme do anything when a book_note URL is requested? Yes, and there is exactly one to request

`functions.php` branches on `is_singular('book_note')` in two places (asset loading and schema), and `single-book_note.php` is the template WordPress reaches for. Nothing falls through.

**But: there is one `book_note` post in the database, of any status.** The docblock says "One template, 598 notes"; the 598 are not imported. So the template is built and wired against a corpus that does not exist yet. That is the single most useful fact in this answer and it is the one I would not have known without querying: any re-brief written on the assumption that the content is there will be wrong.

## 4. The people-setup.php docblock correction: no, and I can find no trace of it

The brief's extra job was correcting a docblock in `people-setup.php` that claimed the routing key was verified when it was not. Searching that file this session for "routing key" and for "verified" returns nothing, so either the wording has changed since the brief was written or it was never there in the form the brief described. **I have not corrected anything, because I cannot see the claim the brief says is wrong**, and rewriting a docblock to match a description of it is how a file comes to say something nobody checked.

If Chat can quote the exact line the S251 brief objected to, I will find it and fix it in one pass. If the line is genuinely gone, the job is closed by someone else's edit and should be struck from the re-brief.

## What this means for the re-brief

Nothing here needs redoing. The page is built to the S251 brief and the approved S250 page, it is deployed, and it has a DSRD 6 record as of this session (created by the backfill, every line reading `not run`, in `Knowledge Hub Design Prototypes/Book Note Page/`). The two things the re-brief should carry are the 598 missing notes and the rating ticks; everything else is a verification job rather than a build job.

*No em or en dashes in this file; checked before writing.*
