# RULING: the article page's reading column is centred, and the breadcrumb comes with it

**From:** Claude Code, Session 81. **Date:** 24 August 2026.
**Authority:** Kain, in the S081 sitting, on the rendered page in Safari.
**Shipped:** theme v0.86.0 and v0.86.1, deployed and verified.
**Board card:** Knowledge Hub Page Designs, line 1.

---

## The ruling, in Kain's words

> "This container is left aligned on the page. This is stupid. It's ridiculous. I need centered in the page. Understand. This isn't a complex design decision, its very, very basic. Please just fix this"

He was asked whether he wanted it tabbed against the current state to judge by eye, and he ruled it directly instead. So no comparison was rendered.

## What was there, and what it rested on

`.kh-article__inner` carried `margin: 0`, pinning the 880px reading column to the left edge of the 1200px frame and leaving 224px of dead space down the right at every width.

**The entire record for that was a comment in `knowledge-hub.css`:** "Left-aligned to the page container edge so the content lines up vertically with the header and footer logos (Kain, 2026-07-12)", repeated in the template's own docblock. No signed specification, no DSRD section and no channel file mentions it anywhere. It has been carried in the build sheet as Q1 for exactly that reason.

**Everything written says centred.** DSRD 7 §4.1 defines the shared reading column and `base.css` builds it as `.article-container`, "880px centred", with `margin-left: auto; margin-right: auto`. DSRD 9 §22.2 fixes the width and is silent on horizontal position. Measured at S081: `/code-of-ethics/` at a 1280px viewport renders its column with 160px on both sides. **This page was the only reading page on the site opting out of the system's own column**, and it differed from `.article-container` in nothing except those two margins, which is why it now takes them rather than a new value.

## The second half, which the first was hiding

Centring the column stranded the breadcrumb 112px out to its left. The trail had been sitting in the bare `.page-container` at the 1200px frame, and while the column was pinned to that same left edge the two started at the same pixel: **the page looked aligned by accident.**

The trail now sits inside the reading column with everything else. Three reasons, none of them preference:

1. **The site already answers it.** The policy family puts its trail inside `.article-container`. Measured on `/code-of-ethics/` at 1280px: the frame starts at 40, and the trail, the column and the H1 all start at 200.
2. **The gate requires it.** The `breadcrumb-align` check Kain commissioned at S080 passes only where the trail and the title start at the same place. It now reads "trail and title both start at 280px" at desktop, 32 at tablet, 20 at mobile.
3. Leaving it would have reintroduced by hand the exact misalignment he had just called ridiculous.

## What DSRD 9 is owed, and it is a correction rather than an overrule

**§22.3 and §27 both say the breadcrumb sits at the 1200px frame, and §27 cites the built theme as one of four sources agreeing.** The built theme does not agree and did not agree when that line was written at S281: the policy pages have rendered their trail inside the reading column throughout, which is the measurement above.

So §27's four-source agreement is three sources and a claim about the code that was never checked against the code. **The row needs rewriting**, and this file carries the measurement it should rest on rather than a second opinion. What is true site-wide is that the trail aligns with the reading column, whatever that column's width, and that it sits at the 1200px frame only on pages whose content is also at 1200.

## Where the fold-back is written

Harness Rule 14 and its S258 tightening. This page has no approved prototype and no component build sheet of its own; its one home is `BUILD_SHEET__The_Article_Page.md` in the Article Page folder under Knowledge Hub Design Prototypes, and Q1 there is now answered and dated to this ruling. Nothing was written about this page anywhere else, per Kain's S303 instruction that the article page has one home and neither side writes about it elsewhere.

*No em or en dashes in this file; checked before writing.*
