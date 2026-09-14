# RULING: the book note's phone cover comes down to 240, and the writing takes the left column at every width above a phone

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 116. **Date:** Monday 14 September 2026.
**Authority:** Kain, live in the S116 theme sitting, on the rendered pages.
**Board cards:** Book note template; Article template.
**Read this cold.**

---

## 1. What Kain said

He had the book note and the article open below 1200 and gave one instruction, quoted here because it is the authority for everything below:

> "Claude, please have a look at the images on both the article and on the Booknotes page. I... down in mobile, the image on the book cover, both bleed outside of the actual, um, outside of the heading. It's like you haven't... like, have a look at an article, um, or a typical article post and look at the header. This is diabolical work, Claude. Will you please... I'll tell you what. Sort of this responsive layer out on both article and book note, and then come back to me once you are one hundred percent convinced that there's nothing else worth fixing. Don't ask me for any guidance or advice until you're convinced that you've done your absolute best work."

So this file is not a design proposal. It is the record of what was changed under that instruction, and of the two earlier rulings of his that it supersedes.

## 2. The fault he was looking at, named plainly

**The article's hero was drawing its own picture behind its own picture.** `.kh-hero`'s ground is `--kh-hero-image`, which `single-article.php` sets to the article's featured image, and the hero grid then draws that same file again as a card. At desktop the card is 256 wide against a 1104 band, so the ground reads as a wash. Below 1024 the card goes full width, 704 of a 736 container, and the two are one photograph at two scales with a dark gradient between them. That is what reads as an image bleeding out of its own frame.

It was built in two sittings that each made sense alone: S110 made the picture the band's ground, S112 put a picture back into the hero beside the words. Nobody looked at the two together below 1024.

**Below 1024 the ground now goes and brand dark takes its place.** Desktop is untouched, because the fault is not there and Kain approved that band on the render at S112.

## 3. Two of his own rulings are superseded, both named here

**S102, the phone cover at 320, centred.** Measured before the change at 390 by 844: the cover drew 320 by 480, the hero ran 1,175 tall, and the title began 757px down, so a phone reader met a full screen of book jacket and learned what the page was on the second screen. It is 240 now, 360 tall by its own 2:3, and the title's first line lands inside the first screen. His word "centralised" is kept and now reads as centring: at 320 the clear space was 15px, which reads as a picture that missed the left edge; at 240 it is 55px each side.

**S102's tablet badge placement, "in the bottom right hand corner of the container too".** The corner it names has moved, so the badge has moved with it, and the intent is kept rather than the mechanism. See section 4.

## 4. The change that answers "two left margins", which he has now named twice

**The writing takes the left column at every width above a phone and the cover takes the right.** It was the other way round below 1200 and this way round above it, so the cover changed sides as the window narrowed and the title lost the left edge the trail and the overline share. `page_gate`'s own words at tablet: "the trail starts at 50px and the title at 370px, so the page shows two left margins."

The markup is untouched; the cover is still written first, which is the order a screen reader hears. The two are placed on the grid, exactly as the desktop block has done since S113.

The badge follows the corner: positioned against the grid from 768 up, over the cover, as at desktop; in the flow on a phone, where the button row is the container's full width.

## 5. What else was corrected under the same instruction, all found by measuring

- The hero wash is a 100deg gradient drawn for a band 1104 wide and 500 tall. On a 390 phone the band is 1,159 tall, so the angle runs down the page and the foot of the hero, where the date, the button and the badge sit, was at 0.62 over a lit bookshelf. Below 1024 it holds its own 0.93 stop. DSRD 7 section 4.5's one-off stands; this is the phone and tablet tier it never had.
- The band gains the phone tier DSRD 7 section 4.3 asks for: 32 above the trail, not 48.
- Four DSRD 7 section 4.3 one-owner breaks closed: the gap under the band had two owners on the book note (80 where the article showed 48); the grid under the trail supplied 32 where the article supplies 48; a section inside a foot separator kept 48 below itself, so every hairline in the foot sat 48 above and 32 below on a phone; and the writing's last paragraph carried its own 16 into the boundary with the author signature.
- The author portrait declared 600 by 750 for every photograph on the site; one measures 400 by 400. It is read from the file now, by the helper written at S103 for this exact fault.
- The book cover declared 288 by 432 against files measuring 1000 by 1500. The shape now travels with the address out of `achology_book_note_cover()`, so both callers get one answer.
- The essential-reading badge is lazy loaded, being below the fold on a phone.

## 6. Where the gate stands, and what is not closed

`page_gate` on the book note went from 24 failures to 15, and on the article from 11 to 10. Every one of the fifteen that remains is content, asset, record or registry work rather than layout: the missing DSRD 6 record, the stale Rank Math score, keyword density, the cover shipping as a master JPG and over its size budget, no srcset on eighteen pictures, the breadcrumb hierarchy the S356 ruling already owns, and an orphan verdict the crawl could not reach.

Two chapters fail that are worth a decision rather than a fix, and both are Kain's:

1. **`hairline-present`, the boundary between the writing and the author signature, at all three widths.** There is no line there and the gate wants one. Whether that boundary carries a hairline is a design decision, not a build fault.
2. **`header-to-content`, at all three widths on both page types.** The chapter measures the distance from the header to the first content and wants 48. On a page with a hero band it measures the band, so it can never pass as written. It looks like a registry question rather than a page fault.

## 7. Added later the same sitting: the foot takes one way out below 1200

Kain, looking at the foot of the article on a phone: "Can you see the problem we have at the bottom of mobile view, you haven't deleted these two links from your code it seems?" The two are "More Articles in this Category" and "Browse the Whole Knowledge Hub".

**This is his own S112 ruling reaching a shape it had never been applied to.** He gave it on the rail then: "can you think of nothing better to put in here than two conflicting arrows that look terrible?", and he wrote the replacement himself: "How about View All Articles, and point to the articles home page instead?"

**Why the pair works at the foot of a page and not here.** The theme's own note draws the distinction and it was lost when the foot block came back below 1200 in this sitting: the pair earns its place under a block running the full width of a page, where the two sit on one line at opposite ends and read as a pair rather than as a contradiction. On a phone this block is the full width of the page and that width is 350, so they stack, one arrow pointing left and one pointing right. That is the exact thing he rejected in the rail.

**The trade, named rather than hidden.** Between 768 and 1199 the block is about 700 wide and the pair would have sat on one line perfectly well. It is given up so this block has one answer rather than a third breakpoint of its own. His S088 pair is untouched on every page type that still draws the full-width foot block.

## 8. Added the same sitting: the banner badge is deleted, the closing badge goes left, and the writing gets its text wrapping back

**Kain's words, on the rendered page:** "i think we can lose the banner badge completely, and in the last paragraph, just left align it to the container, and do text wrapping around it."

**What he was looking at.** The hero badge was positioned against the grid's bottom right corner. That corner is the one the cover occupies, so the badge drew over the lower right quarter of the jacket: on this book, the author's name and the last line of the subtitle. A seal pinned to a container rather than attached to anything lands on whatever is in that corner, and what is in that corner changes with the width and with the book. It is deleted, markup and rules together, along with the two clearances the rest of the hero was paying it: the standfirst's measure came in four letters and the button row kept 152px clear, both only so the badge had room. His S102 placement is superseded. The rating itself is untouched: it is still the standfirst's last sentence in his own words and still in the page's structured data.

**The closing badge moves to the left with the writing running round it**, superseding his own S102 right edge.

**And the fault underneath both, which is mine from S112.** The closing badge was not on the right at all, it was on the left with the words pushed underneath it. A floated element inside a grid is not floated: the float is dropped and the element becomes a grid item. The writing was made a grid at S112 so the strip could sit beside it, and three floats inside the writing silently stopped working at every width from 1200 up: the book author's photograph, the course card, and the closing seal. Each still appeared, in the wrong shape, which is why nobody caught it.

**The writing is a plain column again.** It keeps normal flow and holds a column's worth of space open down its right; the strip is taken out of flow into that space. Every width, gutter and position is the grid's own, read from the same tokens, and the rendered page was measured before and after: the strip at 256 wide on the same left edge, the writing at 800 on the same left edge, the strip's top on the same line. What changed is that the three floats work again.

---

OWED BACK: DSRD 8 section 31 and DSRD 9 section 32.3 carry the superseded S102 values and are owed the correction, including the hero badge's removal and the closing badge's side. DSRD 9 section 22.8 records nine links and the two ways out and is owed the narrow-width exception in section 7. Nothing else.

*No em or en dashes in this file; checked before writing.*
