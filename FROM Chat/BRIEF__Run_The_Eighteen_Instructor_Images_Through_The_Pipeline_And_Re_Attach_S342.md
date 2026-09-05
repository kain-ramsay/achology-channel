> **CODE DISPOSITION, S102: DONE for the seventeen that have a page, answered by REPORT__The_Seventeen_Instructor_Heroes_Are_WebP_And_Re_Attached_S102.md.** All four steps ran: the originals sourced from the install (1760 by 840, not 2200 by 1050), 34 WebP derivatives from the pipeline in the theme and deployed, seventeen re-attached at 1360 wide with every alt text unchanged and read back, the media gate before and after on the fifteen live pages. Fifteen are live, two (I04, I14) are the S102 drafts and took their pictures without a rendered gate, and I18 has no page on the install, so its picture waits with the article. The format line passed on all fifteen; the filename line still fails on the theme's `large` request, now on the theme queue.

# BRIEF: run the eighteen instructor article images through the pipeline and re-attach them

**From:** Claude Chat, Session 342. **Date:** 5 September 2026.
**Approved by:** Kain, in session, 5 September 2026 ("Yes to commissioning Code to run the eighteen instructor images through the pipeline").
**Answers:** the offer in `REPLY__Steps_One_To_Three_Of_The_Hero_Image_Brief_Are_Done_83_Of_83_S102.md`, section "What the S097 precedent turned out to be", which named this pass and did not do it because no brief covered it.
**Board cards:** the eighteen instructor articles; Image and icon optimisation.
**PAGE GATE:** this is not a page build, so no page gate line. The acceptance test is the media gate on each of the eighteen live pages, before and after, plus the file checks the pipeline prints.

## What is wrong, in your own words

The eighteen instructor articles' featured images are the Canva PNG masters uploaded whole: 2200 by 1050, 274KB to 390KB, no crop, no resize, no WebP. The media gate flags them on every page that shows them, in the article's own hero and in every card slot. They predate DSRD 7 section 12.3's pipeline, which is why the 83 rescued-article pictures today have WebP derivatives and these eighteen do not.

## The job

1. **Source.** Take each of the eighteen from its uploaded original on the install (the 2200 by 1050 PNG already attached to the page). No Canva export is needed and Kain's hands are not needed.
2. **Convert.** Run `image_pipeline.py --slot hero --width 680` on all eighteen, exactly as for the 83 today: WebP at quality 82, two derivatives each, 680 by 325 and 1360 by 649, named `{slug}.webp` and `{slug}@2x.webp`, into `images/knowledge-hub/articles/` in the theme. Print the file checks as you did for the 166.
3. **Re-attach.** For each page, upload the 2x file as the attachment's original so WordPress derives the smaller sizes from it and the OG image is 1360 wide, the same rule as step 5 of the S340 brief (Chat's S342 note). Keep each page's existing alt text unchanged. Leave the old PNG attachments in place unless removing them is part of your normal re-attach; say which you did.
4. **Gate.** Run the media gate on each of the eighteen pages before and after, and table the two results. These pages are published, so the rendered half runs in full.

## What does not change

No copy, no metadata, no status. The eighteen are live and stay live. This pass is images only. If any page's alt text is missing or does not carry its focus keyword, name it rather than writing one: alt text is copy and comes from Chat.

## Definition of done

Eighteen pages, each with a WebP featured image whose original is 1360 by 649, media gate passing on the image lines it failed before, the before-and-after table filed. Deploy proofs as usual.

OWED BACK: one REPORT to TO Chat with the before-and-after gate table for the eighteen and the pipeline's file printout.

*No em or en dashes in this file; checked before writing.*
