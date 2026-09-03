# SHIP: v0.161.0, Our People and the sixteen profile pages now close on the article foot's panel

**From:** Claude Code, Session 097. **Date:** 3 September 2026.
**Board card:** Our People and the instructor profile template.

---

## What changed

The closing enquiries panel is gone from the Our People hub and from every instructor profile page. Both now close on `achology_trial_panel()`, which is the block every article, book note and help answer already ends with.

**Kain's instruction, on a screenshot of the block:** *"we currently have the attached banner at the footer of all Our People profile pages, including the hub page, could we please replace this with the same block that we place at the bottom of all articles instead, this makes a bit more sense to me."*

He is right, and the reason is worth recording: a person's profile ends better on an invitation in than on a support desk, and the enquiries route is already carried in the footer of every page on the site, so nothing is lost by removing it from these two.

## What did not move

The trial panel is the same `achology_warm_room()` component the enquiries panel was, so the shape, the column and the boundary above it are unchanged. Only the words, the picture and where the button goes.

Read back on both pages rather than assumed: hairline above at 48 and 48, panel centred in the 880 reading column, the image fetched at its full 720 square, and the button opening the trial checkout in a new tab.

## The tidy that came with it

Each page had the seven panel values typed out in full, because the profile page copied them character for character from the hub at S097. Both are now one call. That is the S088 ruling read straight: *"one token, one template we're using site wide."*

**The enquiries copy is untouched and is not lost.** About, Reviews, Testimonials and the Founders' Letter still close on it, and `achology_warm_room()` renders it for them unchanged.

## Two things for the record

**Two comments in the templates still described the enquiries panel** as the block that ships there, one of them dated S062. Both were corrected in the same pass rather than left standing, because a comment that describes a block the file no longer renders is the kind of thing a future session reads and believes.

**DSRD 9 will need a line.** The Our People hub and the profile template are described somewhere as closing on the enquiries panel; that is now wrong on both. Chat's to place, since the standard is Chat's.

---

OWED BACK: the DSRD 9 correction, if the standard names the closing block on either page.

*No em or en dashes in this file; checked before writing.*
