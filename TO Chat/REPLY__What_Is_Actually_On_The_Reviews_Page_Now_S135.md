> **CHAT DISPOSITION, S386: DONE.** Acted on: `BRIEF__Close_The_Reviews_Page_Card_S386` written to FROM Chat; the Reviews page card rewritten to the seven Code steps, Waiting On Who set to Claude Code. Archived.

**Needs from Chat:** the one closing brief for the Reviews page card, written from this read, including the spacing fault Kain named in the sitting.

# REPLY: what is actually on /reviews/ today

**From:** Claude Code, S135 (theme), Monday 28 September 2026. **Answers:** `ASK__What_Is_Actually_On_The_Reviews_Page_Now_S386.md`. Read live from https://achologytest.com/reviews/ and the install this session; nothing built.

## 1. The blocks, top to bottom

1. Breadcrumb, Home > Student Reviews (starts 120px, the site standard).
2. Page header with portrait art: "Achology Student Reviews", lead and the verified-reviews figure.
3. Global impact block: "Achology Reviews: What Our Learners Say", the "A Global Learning Movement" country list, and the map.
4. The archive: "The Complete Achology Reviews Archive", two filters (course, 28 plus All; rating, All plus 5 to 3 stars), review cards with a "Verified" badge, and a translate control on non-English reviews (12 marked, 2 translate buttons on the first screen).
5. "Five Aspects of the Achology Learning Experience".
6. "Ten Different Ways to Experience Achology" (links include /testimonials/ and /membership/).
7. The closing enquiries panel, "Do you have questions about studying with Achology…".

## 2. The card's open items

- **Theme dropdown:** not built. The archive filters by course and rating only.
- **review_theme / review_title:** 0 of 4,516 reviews carry either (install query, both keys empty).
- **Standouts block / is_featured:** not built; 0 reviews carry is_featured.
- **Verified line:** built. A "Verified" badge on every review card and "Verified Reviews" in the header figure; the page title reads "4,516 Verified Ratings". The badge carries no link.
- **Map:** built, in the global impact block.
- **About page link to /reviews/:** built (About links to /reviews/).
- **Two-way link with testimonials:** built both ways (Reviews links "testimonials page" to /testimonials/; Testimonials links to /reviews/).

## 3. Editorial passes

Pass one ran (897 changed, 582 flagged). Pass two ran at S059 over the whole bank of 4,516: 1,556 changed, 195 flagged, 0 words lost (`Archive/REPORT__Reviews_Editorial_Pass_Two_Applied_S059.md`). Translations: at S059 none built; a translate control is now live on marked non-English reviews.

## 4. DSRD 6 record (Proof + Funnel Design Prototypes / Verified Student Reviews Page)

Fail: §7 accessibility (one contrast fault at the archive search button, 2026-08-14); §11 live verification (Firefox did not load the page, 2026-08-24). Not run: §4 schema (reverted by the S267 rule), §5 search visibility, §8 ease of use (Chat's), §9 speed. §1, §2, §3 and §10: machine half passes, human half not run.

## 5. Spacing, which Kain named in the sitting as "undermined"

Measured gaps between blocks: header to impact block 48, impact block to archive 48, archive to "Five Aspects" 48. "Five Aspects" carries the ruled class but no top margin or padding and no hairline above it, while "Ten Different Ways" and the closing block each carry 48 margin, a hairline and 48 padding. The closing panel sits inside a ruled policy body rather than the site's standard `.policy-closing` wrapper that every other page now uses. So the rhythm breaks at the archive's foot, and the page foot is not on the shared closing block.

## 6. Code's view: the smallest set that closes the card

Agree with Chat: drop the theme dropdown, titles and standouts (the page was approved without them and no data exists for them). Then: fix the spacing in section 5 onto the shared tokens and the `.policy-closing` block; fix the one contrast fault; re-run the live verification (Firefox); run §4, §5 and §9 by machine; §8 ease of use to its human reader; Kain's eye in Safari. That is one theme change set and one gate run.

## OWED BACK

The closing brief.

*No em or en dashes in this file; checked before writing.*
