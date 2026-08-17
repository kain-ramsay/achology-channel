# REPORT: the Reviews page SEO metadata and image audit, plus one bug fixed

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.58.2, live.
**Commissioned by:** Kain, in session.
**Method:** measured on the rendered live page after a cache purge. Nothing recalled.

## 1. The emoji bug, found, diagnosed and fixed

Kain reported an emoji inside a review "consuming a huge proportion of the block". **It was ours, not WordPress's.**

**What is happening.** 25 of the 4,517 reviews contain an emoji. WordPress replaces the character with an `<img class="emoji">` pointing at its own 150px SVG. Core normally ships a stylesheet holding that image at 1em and inline; **that stylesheet is not reaching our pages**. The only rules left touching it were our own `base.css` reset, `img { display: block; max-width: 100% }`. So the emoji left the line it was written on and painted at its natural 150px, in a card whose body text is 16px.

**Fixed** by giving `img.emoji` and `img.wp-smiley` an explicit inline, 1em treatment in base.css. Measured after: **16 by 16, display inline, sitting inside the text box, matching the 16px body size.**

**Deliberately not fixed by stripping the emoji.** DSRD 9 §29.6 decision 4 requires a review to display in the reviewer's own words, and an emoji they typed is one of their words. This changes how it is drawn and nothing about what is said. Written against the class rather than the review card, because the same defect exists anywhere an emoji appears in content.

## 2. Images: 65 on the page, and they are in good order

| Check | Result |
|---|---|
| Missing alt attribute | **0 of 65** |
| Correctly empty alt (decorative) | 58 |
| Real descriptive alt | 7, all specific: "A smiling Achology student with open hands...", "Four members of the Achology customer support team", "An Achology student working through an on-demand course at a desk" |
| Format | 63 webp, 2 svg (both emoji) |
| Lazy loaded | 54; the 11 eager are the header logo, the seven school glyphs in the navigation, and the hero, which is correct because the hero is the LCP element |
| Intrinsic dimensions | one real gap, now fixed. See below |

**The one real gap, fixed.** `grid-courses.webp` in the gateway block was the only image in the theme's shared parts with no width and height, which is a layout-shift risk wherever that block appears, and it appears on About, Reviews and the policy family.

**Worth knowing how it was fixed, because the obvious fix was wrong.** The four routes-grid images are not one size: `grid-courses` is 900x506 and the other three are 760x428. Hardcoding one pair would have been wrong for one of them and would have caused the exact shift the attributes exist to prevent. The dimensions are now read from each file at render. Verified live: `width="900" height="506"`, no PHP notice.

**One thing I have not done.** No image on the site carries a `decoding` attribute. That is a micro-optimisation across 65 images on this page and many more elsewhere; it is a sweep and needs a brief, not a decision from me.

## 3. Metadata: this is the chapter that fails, and it is yours

| Item | State |
|---|---|
| Page title | `Reviews \| Achology TEST Site`, 28 characters. **WordPress's default pattern, not a written title** |
| Meta description | **MISSING** |
| og:description | **MISSING** |
| og:title | Inherits the default title, so it is unwritten too |
| og:type | `article`. **Worth a decision:** this page is a library, not an article. `website` is the better fit |
| Canonical | Absent, and correct. The build ground is noindex and Rank Math withholds it by design (S245 carve-out) |
| robots | `nofollow, noindex`, correct for the build ground and set by `blog_public=0` |
| Language | `en-GB`, correct |
| h1 | One, "Achology Student Reviews", correct |
| Structured data | WebPage plus BreadcrumbList, exactly what DSRD 10's map assigns this page type |

**Under Rule 8 metadata text arrives written and approved, so the title and description are owed from you.** This is the same item that has stood on the DSRD 6 gate record all day; it is repeated here because Kain asked for the metadata test and this is its result.

**One new item for you within it:** the `og:type` of `article` on a reviews library. Kain has not seen that and it is a wording-adjacent decision.

## 4. Internal linking: the page gives generously and receives almost nothing

**Outbound is strong.** 25 distinct internal links in the body: 16 course pages carried by the review cards' own course signposts, plus the gateway block to courses, schools, accreditation, pricing, the Knowledge Hub, quotes and membership, plus enquiries.

**The gap is a pair of pages that should obviously reference each other and do not.**

1. **Reviews does not link to `/testimonials/`, and testimonials does not link to `/reviews/`.** These are the site's two proof pages. One holds 4,517 written reviews, the other holds filmed member stories with transcripts. A reader who has just read the reviews and wants to see a person say it has nowhere to go, and the reverse is equally true. **This is my strongest recommendation and it is worth doing in both directions.**
2. **Reviews does not link to `/about/`.** Kain has already asked for About to link to Reviews; the return link is the same argument.

**Not a linking gap, but worth recording:** four of the gateway destinations do not exist yet, `/courses/`, `/academy/schools/`, `/accreditation/` and one school page. The gate reports them as planned rather than broken, which is correct, but they are links a visitor can click today and land on nothing.

**I have built none of these.** Where a link sits inside a page Kain has approved is his call or yours, and the wording is yours under Rule 8. What I need is the anchor text and the placement, and I will build both directions in one change set.

*No em or en dashes in this file; checked before writing.*
