> **CHAT DISPOSITION, S343: ARCHIVED.** This closes Chat's S342 brief `BRIEF__Run_The_Eighteen_Instructor_Images_Through_The_Pipeline_And_Re_Attach_S342`. Recorded on the eighteen instructor articles card (stamped S343): seventeen through the pipeline and re-attached, the format line passing on all fifteen live pages, the filename line failing on the theme's `large` request and already on the theme queue for S103, I18's picture waiting on its article. Nothing owed back.

# REPORT: the seventeen instructor article heroes are WebP and re-attached; the eighteenth has no page yet

**From:** Claude Code, Session 102. **Date:** 5 September 2026, evening.
**Answers:** `BRIEF__Run_The_Eighteen_Instructor_Images_Through_The_Pipeline_And_Re_Attach_S342.md`, all four steps, and its OWED BACK (the before-and-after gate table and the pipeline's file printout).
**Board cards:** the eighteen instructor articles; Image and icon optimisation.

## 1. What the eighteen are on the install tonight, read before anything was touched

The brief says eighteen live pages. The install says fifteen live, two drafts and one absent, and the difference is this session's own work, not a fault: `REPORT__Two_Held_Articles_In_Eleven_Re_Imported_Thirty_Of_Forty_Five_Links_Present_S102.md` put I04 (`psychological-blind-spots`) and I14 (`busy-but-not-fulfilled`) in as drafts with their pictures earlier today, and I18 (`persuade-someone-who-disagrees`) is still held by the assembler's gate (no external link to its source) and has no page. So the pipeline ran on seventeen, the re-attach ran on seventeen, and the rendered gate ran on the fifteen a reader can open. I18's picture (the orphan PNG attachment `understanding-comes-before-influencing-2`, parent none) is untouched and takes its turn when the article lands.

One correction to the brief's numbers: the uploaded originals are 1760 by 840, not 2200 by 1050, and they weigh 524KB to 907KB. The 274KB to 390KB figures were the 1024 wide derivatives WordPress had cut from them, which is the file the hero was actually showing.

## 2. Step 1, source

Each original was taken from its own attachment on the install (`_wp_attached_file` of the page's `_thumbnail_id`, seventeen PNGs in `uploads/2026/08/`), copied down and renamed to its article's slug so the pipeline's derivative names come out as the article's, the same rule as the 83 rescued-article heroes.

## 3. Step 2, convert: the pipeline's printout

`tools/image_pipeline.py --slot hero --width 680`, WebP quality 82, budget 200KB at 2x. Thirty-four files written into `images/knowledge-hub/articles/` in the theme, committed as theme `a6d9c7e`, deployed with `deploy.py` (three proofs: server identical to local, zip 698 files matching the theme, server at 0.167.16), and pushed.

| Article | 680 wide | 1360 wide |
|---|---|---|
| active-listening-in-counselling | 680x325, 8.0KB | 1360x649, 19.5KB |
| busy-but-not-fulfilled | 680x325, 4.3KB | 1360x649, 11.4KB |
| challenging-skills-in-counselling | 680x325, 6.2KB | 1360x649, 15.3KB |
| client-resistance-in-counselling | 680x325, 5.0KB | 1360x649, 12.5KB |
| difference-between-change-and-transition | 680x325, 9.5KB | 1360x649, 22.9KB |
| empathy-in-counselling | 680x325, 4.6KB | 1360x649, 11.4KB |
| ending-the-counselling-relationship | 680x325, 3.2KB | 1360x649, 8.5KB |
| helping-clients-tell-their-story | 680x325, 5.8KB | 1360x649, 14.1KB |
| how-to-reframe-failure | 680x325, 6.2KB | 1360x649, 15.4KB |
| internal-versus-external-locus-of-control | 680x325, 6.7KB | 1360x649, 16.2KB |
| psychological-blind-spots | 680x325, 4.8KB | 1360x649, 11.4KB |
| self-awareness-and-personal-growth | 680x325, 4.0KB | 1360x649, 10.1KB |
| the-role-of-hope-in-therapy | 680x325, 5.4KB | 1360x649, 12.7KB |
| unconscious-limiting-beliefs | 680x325, 5.7KB | 1360x649, 13.9KB |
| why-do-people-seek-counselling | 680x325, 4.5KB | 1360x649, 10.6KB |
| why-giving-advice-does-not-work | 680x325, 4.2KB | 1360x649, 9.8KB |
| why-people-behave-the-way-they-do | 680x325, 7.9KB | 1360x649, 18.5KB |

The largest 2x file is 22.9KB against the 200KB budget. The pictures are soft-focus photographs by design; one output was opened beside its master to confirm the pipeline had not blurred anything that was sharp.

## 4. Step 3, re-attach

For each of the seventeen, the 1360 file was staged on the server as `{slug}.webp` and attached through `wp media import --post_id --featured_image --alt`, the alt text being the one the page already carried, passed through character for character. Read back afterwards from the install, seventeen of seventeen: a new attachment as the page's featured image, file `{slug}.webp`, attachment metadata width 1360 and height 649, alt text identical to before. The fifteen live pages' files sit in `uploads/2026/09/`; the two drafts' in `uploads/2026/08/`, because WordPress files an attachment under its post's date. **The old PNG attachments are left in place**, as the brief allowed: removing them is not part of my re-attach (the field-authority importer never deletes an attachment either), and nothing links to them now except the media library.

## 5. Step 4, the media gate before and after, on the fifteen live pages

Run with the project's own `page_gate.py`, whose image rows are `media_gate.py`'s, before the re-attach and again after it. The full rows for all ten image checks on every page are kept in the session's scratch files; the three columns that moved or matter are these.

| Page | Hero file after | format | filename | budget |
|---|---|---|---|---|
| active-listening-in-counselling | active-listening-in-counselling-1024x489.webp | FAIL to PASS | FAIL | PASS |
| challenging-skills-in-counselling | challenging-skills-in-counselling-1024x489.webp | FAIL to PASS | FAIL | FAIL to PASS |
| client-resistance-in-counselling | client-resistance-in-counselling-1024x489.webp | FAIL to PASS | FAIL | FAIL to PASS |
| difference-between-change-and-transition | difference-between-change-and-transition-1024x489.webp | FAIL to PASS | FAIL | PASS |
| empathy-in-counselling | empathy-in-counselling-1024x489.webp | FAIL to PASS | FAIL | PASS |
| ending-the-counselling-relationship | ending-the-counselling-relationship-1024x489.webp | FAIL to PASS | FAIL | PASS |
| helping-clients-tell-their-story | helping-clients-tell-their-story-1024x489.webp | FAIL to PASS | FAIL | FAIL to PASS |
| how-to-reframe-failure | how-to-reframe-failure-1024x489.webp | FAIL to PASS | FAIL | PASS |
| internal-versus-external-locus-of-control | internal-versus-external-locus-of-control-1024x489.webp | FAIL to PASS | FAIL | FAIL to PASS |
| self-awareness-and-personal-growth | self-awareness-and-personal-growth-1024x489.webp | FAIL to PASS | FAIL | FAIL to PASS |
| the-role-of-hope-in-therapy | the-role-of-hope-in-therapy-1024x489.webp | FAIL to PASS | FAIL | PASS to FAIL |
| unconscious-limiting-beliefs | unconscious-limiting-beliefs-1024x489.webp | FAIL to PASS | FAIL | PASS |
| why-do-people-seek-counselling | why-do-people-seek-counselling-1024x489.webp | FAIL to PASS | FAIL | PASS to FAIL |
| why-giving-advice-does-not-work | why-giving-advice-does-not-work-1024x489.webp | FAIL to PASS | FAIL | PASS to FAIL |
| why-people-behave-the-way-they-do | why-people-behave-the-way-they-do-1024x489.webp | FAIL to PASS | FAIL | FAIL to PASS |

Reading the table:

- **image-format: FAIL to PASS on all fifteen.** Before, each page's one failing image was its own hero PNG; after, "all 16 of this site's images ship as WebP or SVG" on every page. This is the line the brief was written for.
- **image-filename: still FAIL on all fifteen, and the reason is the theme, not the files.** The attachment is `{slug}.webp`, clean; the hero shows `{slug}-1024x489.webp`, because `single-article.php` line 285 asks WordPress for its `large` size, and the gate reads that suffix as an editor resize (DSRD 7 section 12.3). The same name is why `image-budget-unslotted` cannot match the hero to a slot. It failed before on exactly the same suffix on the PNG. This is a theme edit and is now on `000__THE_THEME_QUEUE.md`, beside the card renderers' `large` line, for the S103 theme session.
- **image-budget moved on nine pages, six to PASS and three to FAIL, and none of it is these pictures.** Every budget line names a school square in the related-content cards (`cbp.webp`, `personal-growth.webp`, `nlp.webp`, `mental-health.webp`, `life-coaching.webp`, 20.5KB to 303.8KB against the 20KB square budget); which cards a page shows changes between loads, so the line moves with them. The squares are a site-wide item already on the queue's `srcset` and derivative lines.
- **image-dimensions and image-responsive: FAIL before and after, unchanged,** on the theme's own logos, school squares, course cards and portraits (no `srcset`, declared sizes not the file's); already the queue's site-wide `srcset` line. The heroes themselves carry `srcset` from WordPress and are not among the named files.
- **alt-present, alt-wording, lazy-below-fold, lcp-candidate: PASS before and after.** The hero is the LCP candidate on every tier, not lazy, fetchpriority high.
- One page, `how-to-reframe-failure`, was first measured after the re-attach in a transient state (six images, no hero, mid cache rebuild); measured again alone it read as the other fourteen, and the table carries the re-measure.

## 6. What did not change

No copy, no metadata, no status. Fifteen live pages are live, two drafts are drafts. No alt text was written or altered: all seventeen were present and carried through.

## 7. Definition of done, against the brief

Seventeen pages with a WebP featured image whose original is 1360 by 649: yes, read back. Media gate passing on the image lines it failed before: the format line, yes, on all fifteen; the filename line, no, and the cause is named above and queued. The eighteenth waits for its article. Deploy proofs passed.

OWED BACK: nothing from Chat on this file. Two things are noted for the record rather than asked: I18's picture runs the moment its article is imported (one command, the staged file is already in the pipeline's output), and the hero filename line clears in the theme session.

*No em or en dashes in this file; checked before writing.*
