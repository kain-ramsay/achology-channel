**DISPOSITION (S284): set 8 written into DSRD 7 section 12.2 with the fields this note supplies. The SVG-or-WebP ship format is recorded there as open, Kain to rule; DSRD 7 carries that wait. No board card moved. Archived.**

# NOTE: the lockup has no entry in the image registry, and the master library the DSRD names is not on this machine

**DOCUMENT TYPE:** note. Not a page spec. **From:** Claude Code, Session 063. **Date:** 18 August 2026.
**Raised by:** Kain asking a plain question in session: what formats do the approved logos need for the website, and where in the filesystem do they go.
**Reads with:** your `RULING__The_School_Lockup_Is_A_Site_Wide_Device_S282`, which is what makes both gaps below matter.

---

## The question had a written answer, and following it found two holes

DSRD 7 section 12.2 is the right place to look and it answers most of it. Quoted:

> "Production standard for all of the above: WebP, roughly 2x display size, transparency preserved (DSRD 3 §13B). Masters are PNG/SVG and stay in the asset library; only the WebP derivatives are committed to the theme."

So the answer to Kain's "PNG or SVG" is **neither, for the website**: masters are PNG and SVG and live in the library, the theme gets WebP. That part is settled and I have told him so.

## Hole one: the registry has seven sets and the lockup is not one of them

Section 12.2's table runs 1 to 7. Set 7 is **"School logo lockups (white + dark), 797x197"**, marked **"NO USE ASSIGNED YET"** and **"OPEN, Kain to decide"**. That is a different asset from the Know Your Psychology lockup: different artwork, different proportions, and the KYP mark is 1058.8 by 407.0 points.

The KYP wordmark appears in the registry only as something **baked into** sets 2 and 5, the course and school images that carry it. **There is no set for the KYP lockup standing on its own**, because until your S282 ruling it never stood on its own anywhere.

**So it needs to become set 8**, and that is yours rather than mine. What the entry has to carry, from where the work has actually got to:

| Field | Value |
|---|---|
| Set | School lockups, Know Your Psychology, one per school |
| Master size | 1058.8 by 407.0 points, from `Know_Your_Psychology_Graphic.ai` |
| Purpose | The site-wide school device ruled at S282: one per school, each linking to its school page |
| Formats | PNG and SVG masters in the library, WebP derivative in the theme |
| Status | Artwork approved by Kain at S063; master not yet recoloured; SVG does not exist |

**And your S282 ruling probably breaks the WebP rule for this one asset**, which is worth deciding rather than discovering. That production standard was written for photographic artwork: course heroes, school heroes, book covers. A logo used as a navigation device at many sizes across a site is the one case where SVG beats WebP outright, and it is exactly what set 7's white/dark pair was presumably drawn for. **I am not deciding it.** If the lockup ships as SVG rather than WebP, section 12.2 needs to say so, or the next person follows the general rule and produces a raster.

## Hole two: the master library at the path DSRD 7 gives does not exist here

Section 12.2 states:

> "Master library: `~/Documents/GitHub/website-assets/website-images/`. Every set exists in both PNG and SVG."

**There is no `GitHub` folder in `~/Documents` on this machine at all.** I searched for `website-assets` anywhere under `~/Documents` and found nothing.

Reported rather than worked around, because the consequences are not small: it is the stated home of every master for all seven sets, it is where a corrected Know Your Psychology master would belong, and DSRD 7 asserts as fact that every set exists there in both formats. If it is on Kain's other machine, or was moved, or was never created, the document is currently pointing at nothing and has been for some time.

**I have not created it.** A master library invented by me at a guessed path is worse than an absent one, because it looks authoritative.

## What I have done instead, so nothing is stuck

The approved seven live in `_proposed_S063` beside the artwork in Website-Wide Assets, at both the original size and 3x, with their specification and the contour mask. That is a holding place chosen because the folder survives, not a claim to be the library.

## The one thing that genuinely cannot be produced yet, and it is not a blocker I can clear

**The WebP derivative needs a display size, and there is not one.** Section 12.2 holds sets 2 and 5 out of the theme for exactly this reason, in its own words: "Producing a derivative now means guessing the 2x target and redoing all 28 when the real width lands."

The same logic applies here and more strongly, because your S282 ruling puts the lockup on surfaces that mostly do not exist yet and says the placements land page by page as each page is specified. **So the derivative is produced the day the first page's spec states the width, not before.**

**The SVG cannot be produced at all until the master is recoloured**, because the glow and the contour pattern are not effects that survive being traced out of a raster.

*No em or en dashes in this file; checked before writing.*
