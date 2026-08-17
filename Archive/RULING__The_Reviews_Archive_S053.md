# RULING: the archive's layout, its batch size, its default order, and the two name-row fixes

**From:** Claude Code, Session 053. **Date:** 2026-08-10.
**Authority:** Kain, directly in session, ruling on two rendered live options; confirmed by Chat's `RULING__Masonry_Grid_And_Name_Row_Fixes_S258.md`. Filed the same session per Harness Rule 14.
**Live:** theme v0.46.1, https://achologytest.com/reviews/

## 1. Masonry, ruled on the render

The archive was shown to Kain two ways on the same reviews, per the S258 render standard: the DSRD 8 section 6.0 stretched grid, and the same cards each at their own height. He rejected both and named a third, in his words:

> "the spacing between cards is standardized throughout, but it's kinda like where a review would kinda snap right direct under the previous one ... so it doesn't actually matter whether reviews are a different length or not ... a constant flowing board."

That is masonry, and it is built. Chat's S258 ruling arrived mid-session confirming the same thing, so the two agree. The 24px gap holds in both directions, so section 6.0's grid gap is untouched; the review keeps its whole text, so section 14.2 item 3 is untouched; and no card carries empty space, which is what the two options were rendered to settle.

**Both temporary switches are deleted**, the stretched grid and `?rv_fit=1`, as Chat's ruling section 1 instructs. Git holds them.

**How it is built, and what was not used.** Native CSS masonry is behind a flag in every browser, so it cannot ship. The maintained public option is Masonry.js. Neither is used: outside code in this theme is Kain's decision and not Code's (Rule 11), so the layout is forty lines in `reviews.js`. The column count and the gap are read back off `reviews.css` at run time, so the three responsive tiers keep one home and the script holds no breakpoint of its own. With scripting off, the cards render as the ordinary three-across grid: not as pretty, never broken.

Verified live at 1280px, 768px and 375px: three columns, then two, then the plain stacked grid with no horizontal overflow.

## 2. Fifty a batch

Kain, S053: show fifty at a time. Was 24. The mechanic itself is unchanged. Verified live: 50 on load, 100 after one press, and **none of the first fifty cards move when the next fifty arrive**, which is the thing masonry could have got wrong.

## 3. The default view mixes the star bands

Kain, S053: "sporadically differentiate them between 4, 4.5 and 5 stars."

Newest-first did not do that, because the bands are not evenly spread through time. The default order is now striped: inside each band the reviews are ranked newest first, each is given its position in its own band as a fraction, and the bank is sorted on that fraction, which lays every band across the full length of the archive in proportion to its size. The first twelve cards on the live page read 5, 5, 4, 5, 4.5, 5, 5, 5, 3, 3.5, 5, 4.

**Written so it does not disturb a standing ruling.** DSRD 9 section 29.6 decision 2 (Kain, S221): "All 4,517 reviews are shown, including the 3.0-3.5 star band." Striping shows the critical band throughout rather than sorting it to the end, so decisions 2 and 3 survive Kain's instruction rather than being traded against it. If he wants that band held further back, it is a one-line change and his call.

A filtered view goes back to newest first: once a reader has asked for one rating or one course there is nothing left to mix. The order is computed from the export at import, not from a random number, so a rebuild reproduces it and the page does not reshuffle under a returning reader.

## 4. The name row: fix B ruled, with three refinements, and both switches deleted

Both fixes were built as Chat's ruling section 2 asks, on the masonry layout, and rendered on the same real cards. Measured on the first fifty at 1280px: **43 of 50 names wrapped as DSRD 8 section 14.2 had it, 14 still wrapped with the month abbreviated, and none wrap with the date on its own line.** Kain ruled on the render, in his words: "the date underneath the name ... that's definitely the right path."

Fix B is folded into the card and both switches are deleted. He then settled three things on the rendered result, all of them his words:

1. **"The star rating sits right aligned on that line with the name sitting left aligned ... the rating and the name need to be sitting on the exact same line."** The name group is now space-between across the card's width. Centre-aligned rather than baseline-aligned, deliberately: the star row is five SVGs in an inline-flex box, which has no text baseline, so browsers fall back to its bottom edge and the stars sit low. Verified on the live page: the name's vertical centre and the star row's vertical centre are the same pixel, name flush left, stars flush right.
2. **"The date needs to be potentially a font size smaller, maybe two."** 13px to 11px. It keeps soft grey #5E6B75 rather than dropping to mid grey, because DSRD 7 section 1's colour roles put mid grey on "single-line captions, meta, separators, decorative icons ONLY ... never on links, nav, or content", and soft grey holds AA at that size.
3. **"Remove a little bit of space in between the name and the date, it's just too much space."** 2px.

**For DSRD 8 section 14.2 item 4.** Its one-line attribution row is superseded: the row is now name and stars on one line, date beneath at 11px. Chat writes it in.

## 4a. The course signpost: square artwork, and two cards across

Kain on the live page: the full course name was crunching. He asked whether the square course images could be used instead of the wide ones, and he was right that they exist: all 28 are in the theme at 192px square, so no new artwork was made.

**The square swap alone does not fix it, and that was said before building.** It buys about 10px of a 230px line. What fixes it is width: **two cards across at desktop instead of three**, ruled by him. Cards go from 277px to 428px, and on the live page **none of the fifty course names clip**, including the longest, "The Self-Belief, Emotional Intelligence and Assertiveness Masterclass", which sets in two lines inside section 14.4's own two-line cap. No names wrap either.

Two consequences for the documents:

- **PLAN section 7's "three across at desktop, two at tablet, one at phone"** is superseded: two, two, one.
- **DSRD 8 section 14.4's artwork row** is superseded: 42px square, the course icon image, and **not flipped**. The flip belongs to the wide image, which is a photographic crop whose subject sits right and faces left. The square is a finished badge with Achology speech marks composed around the subject, so mirroring it would mirror the brand mark. That last part is Code's reading rather than Kain's instruction, and it is flagged for his eye on the render rather than presented as settled.

## 4b. The course signpost becomes a real link, and DSRD 7 gains a gap

Kain, S053: **"the linked text needs to be an actual proper link, that will therefore have design system rules to follow."**

So the footer stops being one link. The prefix is plain text outside the anchor, the course name is the anchor, and the name takes DSRD 7 section 1's link treatment: AA-safe orange #B8460F and the site-wide 1px underline ruled at S248.

**Two locked values in DSRD 8 section 14.4 are overridden, deliberately.** It says the course name is "brand dark #354149 at rest, never orange at rest" and that there is "no underline anywhere on this component, Kain S239". Both were written when the whole footer was the link and the name was not one in its own right. Chat writes section 14.4 to match, and should record that the whole-footer link and its focus ring go with them: the ring now sits on the name, and the click target is the name rather than the bar. Kain was told that consequence before it was built.

**A gap in DSRD 7, not filled.** Section 1 gives a link its rest colour and its underline and says nothing about its hover. The only darkened orange the palette holds, #D85A1B, is reserved in that same section for "hover state for primary buttons only". So no hover colour was invented: the chevron's existing movement is the affordance, and **the site has no link-hover standard**. Worth naming as its own small ruling, because this is the first proper in-component link on the site and every one after it will ask the same question.

**One token used outside its stated role,** reported rather than quietly widened. The prefix had to be darker than the link, and #2D3940 (`--color-dark-footer`) is the only named colour darker than brand dark. DSRD 7 section 1 describes it as the sub-footer's deepest zone, a background, not a text colour. It measures past 12:1 on white so contrast is not the question; the question is whether the role widens or a darker text token gets named. A new hex was not invented for it.

Also on his eye: the prefix is at body weight 400. It was 600 for one round at his own earlier instruction and he ruled against it on the render.

## 4c. The underline goes, the glyph becomes an arrow, and one defect was found by measuring

Three more rulings on the same footer, all Kain's, all on the render.

**No underline.** "Lose the underline in each course title." DSRD 7 section 1's 1px link underline was applied when the name became a link at 4b; he has ruled it off here. That returns section 14.4's own sentence to force, "no underline anywhere on this component, Kain S239". So the name keeps the site's link colour and the card's no-underline rule: of the two overrides at 4b, the colour survives and the underline does not.

**ArrowRight, at 18px.** He asked whether there was a more appropriate icon for the onward mark, and said it read small. Three options were rendered; he took the arrow. Section 14.4 specifies ChevronRight and Chat writes it to match. It is not a new glyph: DSRD 7 section 5.2 registers ArrowRight as the onward marker on the footer CTA card, ruled S245 when it replaced a typed chevron there, so the site already treats the arrow as "go there" and the chevron as "open this".

**It stays at 18px, and that is what lets his other ruling hold.** He also ruled that the footer must never run to three lines. An arrow and a chevron occupy the same box at the same size, so swapping the glyph at 18px costs no width at all. The 20px option, measured on the live page, took 2px off each line of the course name and tipped exactly one course title of the 28, "Authentic Confidence, Core Identity and Self-Esteem Masterclass", onto a cut third line. Verified after the change: 0 of 50 cards clip and no course line exceeds two lines.

**A defect found by measuring rather than by looking.** Section 14.4 specifies the glyph at 18px and the build was rendering it 11px wide against 18 tall. It is a flex item in the footer row, the course line beside it takes every pixel it can, and a flex item with nothing stopping it shrinks below its own width. So part of what Kain was reacting to was not a design question at all. `flex: none` fixes it. Worth recording because it is the same shape as the S050 lesson: the value in the stylesheet was right, what was on screen was not, and only measuring the rendered element showed the gap.

## 5. Draft copy in the three slots, on Kain's direct instruction

Chat's ruling section 3 lists the three archive copy slots as still with Chat and Kain. That still holds for the **final** words. Separately and in session, Kain asked Code for something to react to:

> "just put in some filler text ... so that I can essentially kind of edit and give you back what we actually want these three slots to actually say."

So the slots now carry draft lines for him to overwrite:

| Slot | Draft line, NOT approved copy |
|---|---|
| Archive heading (h2) | Every Review We Have Ever Received |
| Supporting line | Nothing here is selected, edited or arranged in our favour. Search it, narrow it down, and read whatever you find. |
| Hint line under the bar | Try a word a student might have used: anxiety, confidence, career change, Egan. |

**Recorded plainly so nothing downstream mistakes these for signed copy.** Rule 8 keeps Code from deciding what the site says; Kain asked for something to react to, which is his to ask for under Rule 14. Each line carries `data-rv-draft` in the markup so unapproved copy on this page can be found mechanically, and the attribute comes off each line as he settles it. Nothing here should reach a DSRD until he has.

## 6. Nothing owed on the fold-back yet

None of the above is a component whose look Kain has approved as finished, so no prototype version is written by this ruling. The archive is still mid-build: the standouts above it are unbuilt, the review title and theme tag are still missing from the data, the name row is unruled, and the three lines are draft. The fold-back falls due when he approves the block as it stands.

The capitals question is untouched, per Chat's ruling section 3: names stay exactly as the students typed them.

*No em or en dashes in this file; checked before writing.*
