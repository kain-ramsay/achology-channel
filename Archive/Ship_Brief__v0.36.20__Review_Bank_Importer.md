# Ship brief — v0.36.20, the Notion Review Bank importer

From: Claude Code · 2026-07-24 · pushed, zip rebuilt, uploaded, verified live.

Connects the `review` content type built in v0.36.13 to its data. The 23 March
distilled export travels with the theme, and an admin screen under Reviews turns
its 4,517 rows into review posts.

**Nothing is published.** Every row lands as a draft. Kain's rule is that
Displayable reviews go live and Insight ones stay back, but how a student's name
appears beside their words is unsettled, and publishing 4,000 real people's names
is not a step an importer takes on its own. Selecting and publishing stays a
separate, deliberate action.

**How it behaves.** Batches of 200, self-continuing, so a timeout or a closed tab
costs one batch rather than the run. Safe to run twice: each row carries a
fingerprint of course number, date, student and the opening of the text, and
every existing fingerprint is read in one query per batch, so a re-run skips
rather than duplicates. When Notion is re-exported, replacing the file imports
only what is new.

**Two decisions worth your record.**

1. **The export is not web readable.** A plain `data/reviews.csv` inside a theme
   folder is a public URL anyone can guess, and this file holds 4,517 real
   students' names beside their words. It ships as `data/reviews.csv.php`,
   opening with an `exit`, with an `.htaccess` beside it. Verified after upload:
   the file, the directory, the `.htaccess` and the old `.csv` path all return
   403, and no row of the data appears in any response. If any future data file
   travels with the theme, it takes the same treatment, and that is worth a line
   in DSRD 10 §5 or §6 so it is a rule rather than something I remembered.
2. **Course number is kept as plain meta**, `_ach_course_number`. The ACF group
   has no home for it: `source_course` is a post_object pointing at a course
   PAGE, and the 28 course pages do not exist. Keeping the number binds every
   review to its course later without re-reading the export. If DSRD 10 §8 lists
   the review fields, this one belongs in the list with that reason.

**Dry run before shipping**, using a port of the importer's own row logic over
all 4,517 rows: every row parses, 4,517 unique fingerprints with zero collisions,
no incomplete rows, every school label maps to its slug, every date and star
rating readable, tiers split 4,060 Displayable and 457 Insight.

**Verified live after upload.** Theme reads v0.36.20. Seven page types fetched,
all 200, zero PHP errors, every schema block intact and unchanged by the new
admin-only include. The review type exposes nothing publicly: its REST endpoint
returns zero, `?post_type=review` falls through to the homepage, and there are no
single review URLs, which is what `public => false` is for.

**Not verifiable from outside.** Whether the 4,517 drafts have landed is only
visible inside wp-admin, which I have no way to reach. Kain runs the import and
the screen reports the count as it goes.

---

## Still with you

The three schema decisions in `Report__Per_Page_Type_Schema_Inventory.md` §3, and
the `.about-grid__paths` scope question from the v0.36.18 brief.

Two questions of yours from earlier are still worth an answer when you have one:
whether the Notion bank still matches this 23 March export, and whether any prior
rule exists on displaying student names. The second is now the one thing standing
between 4,517 drafts and live social proof.
