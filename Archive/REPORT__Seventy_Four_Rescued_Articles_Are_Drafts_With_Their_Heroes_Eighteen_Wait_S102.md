> **CHAT DISPOSITION, S342: ACTED ON.** The nine `featured_image` fields are briefed to Cowork (`BRIEF__Correct_The_Featured_Image_Field_On_Nine_Rescued_Article_Records_S342.md`, TO Cowork). The nine records with no picture wait on Kain making nine pictures in Canva; Chat writes their map rows when he does, named in the S342 handover. Kain's publishing word for the 74 drafts waits on a Safari sitting he names, also in the handover. Acknowledged to Code in section 4 of `RULING__Two_Profile_Titles_Karens_Keyword_And_The_Three_Book_Note_Keywords_S342.md`. Board cards: the Salvage card, stamped in the S342 walk.

# REPORT: 74 rescued articles are drafts on the install with their heroes attached; 18 wait on their records or their pictures

**From:** Claude Code, Session 102. **Date:** 5 September 2026, about 14:30 BST.
**Answers:** `NOTE__Records_Ready_Run_Steps_Four_And_Five_Of_The_Image_Brief_The_Count_Is_83_And_Piaget_Is_Right_S342.md`, whose OWED BACK asks for the step 5 import report and the step 4 gate result in the shape `BRIEF__The_77_Rescued_Article_Hero_Images_From_Canva_Export_To_Live_Page_S340.md` sets.
**Board cards:** the rescued field-authority articles; Image and icon optimisation.

## Step 5, the import

`import_field_authority_articles.py --push`, the registered draft-only importer, its plan run first: **92 records read, 74 pass every check, 18 refused, all 18 on one class, the named hero file is not on disk.** The 74 were sent and read back with `--verify`: **74 of 74 clean**, each a draft article with its category, its tags on the 36 locked slugs, its author key, its four H2s and its hero attached as the featured image.

**The hero uploaded is the 2x file, as you ruled this afternoon.** Read back off the first attachment (35177, for `10-ethically-dubious-experiments`): the stored file is 1360 by 649, 25.7KB, with four derived sizes, and its alt text is the record's own `featured_image_alt`. The record's `featured_image` still reads `{slug}.webp`; only the bytes sent are the larger file. The importer change is one clause in `attach_hero`, re-registered in the H9 register after a full read.

**Nothing is published.** All 74 are drafts, exactly as the brief's section 5 says, and publishing waits on Kain's word through a clearance.

## The 18 refused, in two classes, all fixable at source and none of them mine

**Nine records name a picture that exists, under the wrong name.** The picture is on disk as `{slug}.webp` and the map has the row; the record's `featured_image` field carries a placeholder or an older filename, so the S340 brief's own line, "every record was normalised to `{slug}.webp` at S335 and re-checked at S339", does not hold for these nine. The field is Cowork's; the fix is the one value, `{slug}.webp`:

| Record | Its `featured_image` field reads |
|---|---|
| a-guide-to-breaking-bad-habits | /wp-content/uploads/kh/articles/a-guide-to-breaking-bad-habits.jpg |
| compassions-test-insights-from-the-good-samaritan-experiment | NEEDS PRODUCTION: hero image of a figure pausing on a path to help another (...) |
| delayed-gratification-insights-from-the-marshmallow-test-study | marshmallow-test-delayed-gratification.jpg |
| from-roots-to-revolution | PLACEHOLDER, to be assigned in production per DSRD 2 image spec |
| how-immediacy-shapes-engaging-and-impactful-conversations | [PLACEHOLDER, image not produced in this drafting session (...)] |
| karpman-drama-triangle | karpman-drama-triangle.jpg |
| the-importance-of-self-awareness | the-importance-of-self-awareness-hero.jpg |
| the-origins-of-humanistic-psychology | humanistic-psychology-origins-hero.jpg |
| understanding-your-core-values | [PLACEHOLDER, to be assigned in production per DSRD 2 image spec] |

**Nine records have no picture at all and no row in the map.** Kain's Canva file has no page for them, so there is nothing to convert; they need a map row and a picture each, which is Kain's making and your map:

`a-guide-to-building-inner-resilience`, `character-traits-of-a-life-coach`, `starvation-insights-from-ancel-keys-the-minnesota-experiment`, `the-4-stages-of-human-evolution`, `the-psychology-of-self-improvement`, `timeless-lessons-from-the-life-and-works-of-hans-j-eysenck`, `understanding-the-cognitive-load-theory-experiment`, `what-is-counselling-psychology-a-search-for-a-definition`, and the skipped record `SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic`, which the importer refuses by its prefix anyway.

When the nine fields are corrected, the same `--push` imports them (the importer skips what it has already created and creates only what is missing); when pictures arrive for the other nine, they go through the same three steps and the same push.

## Step 4, the gate, and why it cannot fully run yet

The media gate's twelve checks run on a rendered page, and a draft has no public address to render. What could run, ran: the importer's own file checks on every hero (present, WebP, under the 200KB budget; the pipeline's printout in `REPLY__Steps_One_To_Three_Of_The_Hero_Image_Brief_Are_Done_83_Of_83_S102.md` covers format, size and naming for all 166 files), and the read-back above of what the install holds. The rendered checks (srcset and sizes from the template, width and height attributes, lazy loading and the hero's fetchpriority, the image sitemap row, the ImageObject in the schema) run on the day the pages are published, on the exemplar and a sample, and go onto their records then. That is the brief's definition of done items 1 to 3, with item 3 honestly deferred to publication.

## The two-to-one count the note asks for

83 pictures in the map, 83 masters on disk, 166 WebP files (83 at 680 wide, 83 at 1360 wide), 74 attached to draft pages today, 9 waiting on a record field, 9 records with no picture to attach (they are not among the 83).

OWED BACK: from Cowork, the nine `featured_image` fields; from Kain and you, nine pictures and nine map rows; from Kain, the publishing word for the 74 when he has looked at a sample in Safari. Nothing further from Code until one of those lands.

*No em or en dashes in this file; checked before writing.*
