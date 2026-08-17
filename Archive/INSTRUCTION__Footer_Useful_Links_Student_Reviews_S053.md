# INSTRUCTION: DSRD 8 section 19.5 Column 3, one row changed by Kain

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.57.4, live and verified.
**Authority:** Kain, in session S053, immediately after being told the Reviews page was an orphan.

## The ruling

> "On the footer, I would like you to replace one of our links. So in the useful links section, I would like you to replace Free Public Events with Student Reviews, and then link that up."

## What DSRD 8 section 19.5 Column 3 now needs to read

| Link | URL |
|------|-----|
| **Student Reviews** | **`/reviews/`** |
| Get Free Coaching | `/free-coaching/` |
| The Knowledge Hub | `/learn/` |
| SoMAP Accreditation | `/accreditation/` |
| Latest Testimonials | `/testimonials/` |
| Help Desk / FAQs | `/help/` |
| Achology Pricing | `/pricing/` |

Row 1 only. The column keeps seven links, the order of the remaining six is unchanged, and no other footer column is touched.

## Built and verified

Live on v0.57.4, measured on the rendered About page after a cache purge: the link reads "Student Reviews", points at `/reviews/`, that address answers 200, and its type and colour are byte-identical to its six siblings, so it inherited the column's styling rather than acquiring any of its own.

## Two things worth recording with it

**This closes the orphan.** The finding filed an hour earlier in `QUESTION__The_Reviews_Page_Is_An_Orphan_S053.md` was that nothing on the site linked to `/reviews/`, which DSRD 6 section 5 item 7 fails a page for. The footer is sitewide, so one row fixes it everywhere at once, and that item is now closed on the gate record.

**Nothing was orphaned by the removal.** Checked before making the change rather than after: `/free-events/` keeps three other inbound links in the theme, on the About page, in the manifesto and in the policy template. Had the footer been its only route in, I would have raised it rather than made the swap.

## What is still open, and why I am flagging it here

The orphan question also asked where else the Reviews page should be linked from. Kain's answer named the footer **and the About page**, and he believed both already carried it. The footer is now done. **The About page still does not link to the Reviews page**, and I have not added one, because where a link sits inside a page Kain designed and approved is a placement decision rather than a technical one. It needs either his instruction on where it goes or your recommendation. Worth doing: the About page is where a reader who is weighing Achology up is standing, and 4,517 verified reviews is the answer to the question they are asking.

*No em or en dashes in this file; checked before writing.*
