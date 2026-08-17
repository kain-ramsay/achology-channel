# RECORD: the share image alt is set on all three pages, and your two questions answered

**From:** Claude Code, S049. **Date:** 2026-08-06.
**Answers:** `BRIEF__About_Family_Share_Image_Alt_And_Artwork_Gap_S251.md`, build item 1 and both questions.

## Build item 1: done, verified on all three rendered pages

```
/about/                    og:image:alt  A glowing filament light bulb inside a wireframe
                                         outline of a human head, with the words Know Your Psychology
/about/founders-letter/    og:image:alt  (identical)
/testimonials/             og:image:alt  (identical)
```

Read back off the rendered pages with the cache purged, character-compared against your brief rather than read. Dash check clean.

**One thing you should know about the mechanism, because it reaches further than three pages.** The alt was never a per-page value. Rank Math takes `og:image:alt` from the image attachment's own alt text, and the default share image (attachment 98) had an empty one, so Rank Math fell back to each page's title. That is why the three pages showed three different strings for one identical picture: `About` and `Founders' Letter` are page titles and `testimonials` is a slug. None of them was ever a description of anything.

So the fix was to give the picture its description, once, on the attachment. That means **every page currently falling back to the default share image now carries this string**, not only these three. On your own reasoning that is the correct outcome rather than a side effect: it is one identical picture, and one true description of it beats each page describing itself and calling that a picture. It retires per page exactly as you said, the moment bespoke artwork lands.

## Question 1: how the ten policy share images are wired

**They are the WordPress featured image. Nothing Rank Math specific, and no filter.**

Read from the live database rather than inferred: `/policies/privacy-policy/` is page 126, and its only image meta is `_thumbnail_id` = 913. Attachment 913 is `2026/07/Achology-Privacy-Policy.jpg` in the media library, and its `_wp_attachment_image_alt` is the string that renders on the page. Rank Math derives `og:image` from the featured image and the alt from that attachment.

**What that means for the three new files.** No wiring is needed. Upload each to the media library, set its alt text, and set it as that page's featured image. The whole job is three uploads and three page edits.

**One boundary on it.** Setting a featured image is editing the page, and pages are Kain's, never mine (Rule 8, and the standing rule in `functions.php`). So when the artwork exists I can upload the files and set their alt text, but the featured image assignment is his three clicks, or an explicit instruction from him that I may do it on his behalf. Worth deciding which before the artwork brief is written, so it does not stall at the last step.

## Question 2: is there a repeatable producer

**No, not for these.** There is a template, and it is for something else.

`6. Quote + Book Note OG TEMPLATES (FINAL).html` exists, in `02. Page + Components (HTML Design Files)/Early Prototypes (HTML Claude Files)/`. Two things about it:

1. It is for the Knowledge Hub's quote and book note cards, which are typographic: brand ground, text laid out to a template, one card per quote. That is a template run because the only variable is the words.
2. The ten policy images are not that. Read from the files: 1200 x 630 JPEGs of illustrated scenes, one per document, each a different picture. The privacy policy's own alt text describes its: "an ancient handwritten scroll lit in amber against a dark background." Nothing about that comes out of an HTML template, and there is no producer for it in the project.

**So the three missing images are a design job, not a template run.** They are three illustrated scenes in the same family as the ten, and on the standing rule that is Kain's to approve by eye, and his to commission however he makes the other ten.

**A caution on the file I found.** `6. Quote + Book Note OG TEMPLATES (FINAL).html` is currently an iCloud placeholder on this machine, 198 bytes, not downloaded. So I have read what it is for and where it sits, but not its contents, and I am not going to describe a producer I have not opened. If the quote and book note run needs it, it needs downloading first. Three other prototype files in that folder are in the same state.

*No em or en dashes in this file; checked before writing.*
