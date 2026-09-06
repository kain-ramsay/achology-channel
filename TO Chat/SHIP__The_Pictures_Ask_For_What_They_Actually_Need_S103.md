# SHIP: the pictures ask for what they actually need, and the card sheet gets its hairline

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Shipped:** theme v0.167.38, v0.167.39, v0.167.40 and v0.167.41, each deployed with its three proofs.
**Closes:** four theme queue lines, and strikes two more that re-measuring found already true.
**Authority:** Kain, in the sitting, naming the site-wide image lines, hairlines and boundaries as this session's third body of work. Filed as a ruling beside this file, because a change touching more than one page is a sweep.
**Board card:** Image and icon optimisation.

---

## The one fault behind two queue lines

The article hero and all five Knowledge Hub card renderers asked WordPress for its `large` size. **WordPress writes the `sizes` attribute from the size it was asked for**, so every hero and every card on the site told every browser the picture would be drawn 1024 pixels wide.

Measured on the rendered pages: a hero is 680 on a desktop, 704 on a tablet, 350 on a phone. A card picture is 352 at its widest anywhere on the site and 275 at its narrowest. A browser that believes 1024 downloads for 1024.

For one card image the candidates are 300, 768, 1024 and 1360 wide, at 2.9KB, 8.6KB, 12.5KB and 15.8KB. The page was asking for the 1024 on an ordinary screen and the 1360 on a retina one; it now asks for the 768. On a twenty four card listing page at retina that is about 170KB that no longer travels.

Both now request the original rather than `large`, which also ends the second half of the fault: any WordPress-generated size carries a resize suffix in its filename, which the media gate reads as an editor resize. **The gate's filename line went from FAIL to PASS on the sample article**, which is the line that had stayed red on all fifteen live instructor articles even after their pictures went through the pipeline clean.

Every width in the two `sizes` strings is a measurement taken this session at 1440, 1024, 768 and 390. The card rule states the widest of them, so no slot is ever under-served.

## Width and height now say what the file is

Thirteen images on one article declared a size that was not the file's. The logo said 130 by 32 on every page of the site; the file is 405 by 100. Each school icon said 44; every file is 96.

The interesting one is the course artwork. It was typed as 600 by 500, and the comment beside it said that was "the real size of every course-NNN.webp in images/courses, measured rather than assumed; they are one generated set and all 28 share it". Five of the set measure 704 by 370. **The set was regenerated at some point and the typed pair stayed behind**, so every course card has been holding a box of the wrong shape, 1.2 against the file's 1.9, while its own comment insisted the number had been measured.

It had been. That is the whole argument for the change: a measurement typed into a template is true on the day it is written and silent for ever after. `achology_image_dimensions()` reads the file, caches per request, and returns nothing rather than something wrong when it cannot read it.

Every one of these images has an explicit CSS width and height with `object-fit: cover`, checked on the rendered page before the change, so nothing moved. **13 mismatches before, 0 after.**

## The card sheet's hairline

The boundary between the sheet's title block and its first card family was the one block boundary on the page with no separator. DSRD 7 section 4.3, quoted from the document read this session: "A hairline separates every pair of blocks. There is no block boundary anywhere on the site without one."

48 above and 48 below, 32 and 32 on phones, one owner supplying both sides. Measured on the rendered page at 1440 and 390.

**One correction for the record, and it is mine.** I have been carrying a note saying every hairline is 48/48 with no phone tier, and that section 4.3's 32px tier was superseded. Read this turn, the document says the opposite: ruling 4 is "48px on desktop and tablet, 32px on phones", amended at S245 to explain that the phone tier is hand written per separator. My note was wrong and the document is right; I have corrected the note.

## Two lines struck with no change at all

Re-measuring found them already true. The largest above-the-fold image is not lazy and carries `fetchpriority="high"` at all three widths. All 70 icons the theme draws are either hidden from a screen reader or named.

Both were measured at S090, fixed at some point between, and nobody struck the lines. **That is worth a note on the queue itself, and I have added one:** a line describing a measurement taken six sessions ago is not evidence, and the first act on any line there is to measure again. I nearly spent this session's remaining time building two things that already existed.

## What is left on the responsive line, and why it is not a template job

The article hero and every card now carry `srcset` and a true `sizes`, from the attachment. What still carries neither is the theme's own pictures: the two logos, the seven school icons, the course artworks, the author photographs, the trial panel. Those need derivative files made before any markup can point at them. That is an asset pass, not a template edit, and it sits beside the avatar and testimonial background jobs already on the queue.

---

OWED BACK: nothing. The remaining responsive work is named on the queue as an asset job.

*No em or en dashes in this file; checked before writing.*
