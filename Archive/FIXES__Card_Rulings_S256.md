# FIXES: Card rulings from the S256 review (approved brief)

**From:** Claude Chat, Session 256
**Status:** Every item below is Kain's ruling, made by eye on rendered cards on the live test site. This is an approved fixes brief, not a question. Build order is yours.

**Read first:** QUESTION__What_Code_Actually_Reads_S256.md sits in this folder and comes before any of this if both land in the same session. It asks how you read specifications; your answer shapes the S257 documentation session. Nothing in this fixes file is affected by that question: these are settled rulings.

**Context you need:** The S256 card review was stopped mid-run by a documentation-system problem (the review kept re-deriving decisions already made, because spec, prototype and build do not point at each other). That gets fixed in Chat Session 257. The six items below were ruled before the stop and stand regardless.

---

## 1. Strip the WordPress excerpt trail (article card)

The excerpt on the article card currently ends in the WordPress "[...]" trail before the CSS clamp cuts it, so a card can show two ellipses. Strip the trail (excerpt_more filter returning an empty string, or equivalent) so the three-line clamp's own cut is the only ellipsis. DSRD 8 section 6.1 records the rule.

## 2. Featured card image area: constrain to the approved 45%

Defect: cards.css applies the 45% width only to `.card__image-area--placeholder`. A featured card with a real image renders the image area unconstrained. Measured on the live articles listing: 79% image, 151px of copy. The approved prototype (featured-article-proof-v12.html in the Card System prototype folder) and DSRD 8 section 6.5 both say 45%.

Fix: `.card__image-area` gets `width: 45%; flex: 0 0 45%;` for all three horizontal featured card types, with or without a real image. The book note horizontal variant keeps its own approved 42%: the two values are deliberately different and both stand.

## 3. Book note card: cover echo backdrop (supersedes the shared bookshelf PNG)

Kain's ruling: the shared bookshelf photograph made all 620 book note cards read near identical at grid scale. Replace it with the book's own cover as the panel background, behind the sharp cover art:

- Same image as the card's cover art, absolutely positioned, `inset: 0`
- `object-fit: cover` so it fills the panel
- `transform: scale(1.25)`
- `filter: grayscale(1) blur(3px)`
- `opacity: 0.5`
- `z-index: 0`, with the sharp foreground cover above it

The bookshelf-bg image and its asset are retired from this card. DSRD 8 section 6.2 records the ruling.

## 4. Book note card: blurb takes the article excerpt styling

Kain's ruling: the blurb (rendered in the `.card__subtitle` slot) drops the italic subtitle treatment and takes exactly the article card excerpt styling: Source Sans 3, 14px, weight 400, colour #5E6B75, three-line clamp, no italic. DSRD 8 sections 6.0 and 6.2 record it. (Separately, the blurb text itself is being rewritten to a wider length band across the master; that content pass travels later and does not block this styling change.)

## 5. Image dimensions and lazy loading (CLS)

Book cover images and course hero images render without width/height attributes, so the layout shifts as they load. Add intrinsic `width` and `height` attributes and `loading="lazy"` to book cover and course hero `img` elements (lazy except where an image is the LCP element above the fold).

## 6. Card type label colour: confirmed correct as built, no change

The 11px card type label ("Article", "Book Note", "Workbook") renders #B8460F on the build. The prototype shows #ED6922, which measures 3.16:1 and fails AA at that size. Kain ruled S256 that the build is right: #B8460F is now a registered exception in DSRD 7 section 1 and DSRD 8 section 6.0. Do not "fix" the label back to the prototype value.

---

**Definition of done:** items 1 to 5 shipped and visible on the live articles listing and a live book note card; confirm in one TO Chat note with the theme version, and note anything that could not be done as specified rather than improvising around it.
