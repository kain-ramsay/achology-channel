> **CHAT DISPOSITION, S343: ARCHIVED.** The badge's file, pipeline sizes, condition and empty alt are written into DSRD 9 section 32.3's badge paragraph and tier table. Its two questions were answered by Kain at v0.167.19 (the stars stay; the standfirst clause goes), both recorded. Card: Book note page template second look.

# RULING AND SHIP: v0.167.18, Kain's Essential Reading badge sits in the book note hero's top right corner, for his eye

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**Asked by:** Kain, in the S102 sitting, spoken and transcribed, bringing a badge he designed himself.
**His words, quoted exactly as transcribed:** *"Claude, I've created, uh, an essential reading badge, alright, which I would love to be able to incorporate into the hero banner. And what I'm thinking is that the hero banner has a container. The container that the book image and the breadcrumbs are pressed up against on the left hand side. On the right hand side, I'm thinking, um, we might be able to position this badge I've created. It's in the it's in the book notes folder within the knowledge hub prototypes folder. Um, it's it's quite a large image, but it only... we just want this to be really, really quite small, but I think it'll actually just add a new layer of, you know, visual credibility to what it is we're trying to create here. Um, well, what do you think? Can you have a look at the image I've created? It's just transparent background. It's a really nicely designed, uh, badge, to be honest with you. And, uh, yeah, be interesting to hear your thoughts."*
**Status:** built into the theme and deployed to the build ground so he can judge it on the real page, as every hero change tonight was. **Not yet approved by his eye**, and two questions are put to him below. If his word is no, the commit reverts.
**Filed under Harness Rule 14.** Theme commit `aa9ffb8`.
**Board card:** Knowledge Hub page designs.

## The badge

His file is `Book Note Essential Reading Badge.png` in the Book Note Page folder's `Page Images`: 1080 square, transparent, a hexagonal seal with an orange border on the site's dark slate, the Achology mark with "Book Notes" beneath it, an orange band reading "Essential Reading" with a check, and a row of five yellow stars under the band. It went through `tools/image_pipeline.py` at the square slot, 128 wide: `book-note-essential-reading-badge.webp` (128, 5.2KB) and `@2x` (256, 11.8KB), transparency kept, against the slot's 20KB budget; both in the theme's `images/knowledge-hub/`.

## Where it sits, and what moved to make room

The badge hangs in the top right corner of the 880 container, its right edge on the container's right edge and its top level with the top of the hero's text stack (the grid's own 32 above it), absolutely positioned so it takes no grid cell. It renders only when the record's rating is `essential-reading`; the two lower ratings show no badge and their hero is untouched. Alt text is empty on purpose: the standfirst already says "Essential Reading" (v0.167.17), so a screen reader hears the fact once and the badge is its visual seal.

Sizes: 128 square on desktop (his "really, really quite small", and the smallest size at which the band's words still read), 96 where the grid stacks below 1024, 88 on a phone. On desktop the overline and the title keep 152px clear on the right (the badge plus one 24 gap); below 1024 the stack sits under the cover, so the badge sits in the free space to the right of the cover and nothing else moves.

**Measured on the deployed page.** At 1440: badge 128 square at x 1032 to 1160, y 173 to 301; the title's text ends at x 1002, 30 clear of it; the title now wraps to three lines on this page (it was two), which lifts the stack to 401 and the hero grows by 17px; the standfirst, the author line and the button are unchanged. At 1024: the same, at x 824 to 952. At 768: badge 96 at x 640 to 736 beside the cover's top right, title full width below. At 390: badge 88 at x 282 to 370, 6px clear of the 256 cover. The badge loads (natural width read), the 2x file is chosen on the retina pane, no horizontal overflow at any width. Stylesheet served at ver 0.167.18.

## Shipped

Theme v0.167.18, `deploy.py` three proofs passed: server identical to local, zip 700 files matching the theme, server reporting 0.167.18. Commit pushed. Opened in Safari for Kain as a new tab.

## Two things put to Kain, in the chat, for his yes or no

1. **Five stars.** DSRD 9 section 32.9 item 1 says the rating renders "in the editorial scale's own words and never as stars", approved by him on the rendered page at S250. The badge carries five stars beneath the band. It is his design and his rule, so the render is in front of him and the call is his; if the stars stay, section 32.9 item 1 is yours to reword.
2. **"Essential Reading" twice in one hero.** The badge says it and the standfirst says it (v0.167.17, an hour earlier). Both are left in tonight, on the reading that the words serve search and screen readers and the badge serves the eye; if he would rather the badge carry it alone, the standfirst's clause and its ticks come out in one edit and the alt text becomes the badge's words.

## Owed to the documents

DSRD 9 section 32.3's hero table has no badge row and gains one if Kain keeps it (position, sizes, the rating condition, the empty alt); section 32.9 item 1 as above. Yours, after his word.

OWED BACK: nothing until Kain's word on the render, which Code will relay in a RULING file.

*No em or en dashes in this file; checked before writing.*
