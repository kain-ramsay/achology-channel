# RULING: the foot of every content page is one standard, and eleven decisions that set it

**From:** Claude Code, Session 088. **Date:** 31 August 2026.
**Ruled by:** Kain, in the sitting, every one of them on the rendered page in Safari.
**Board card:** Knowledge Hub Page Designs, lines 1 and 2.
**Shipped:** theme v0.118.0, deployed and proved.

This file carries the rulings so DSRD 9 and the signed article spec can be corrected. `SESSION_REPORT__S088.md` carries what was built.

---

## 1. The standard Kain set, in his own words

> "we need to definitely only have three blocks at the bottom of each article page, which is gonna be true for articles, book notes, quote articles, and workbooks when we eventually design these templates as well. This is gonna allow us to standardize every single article page apart from, um, the hero banner, which is what's gonna distinguish each one."

**Three blocks under the body on every content page:** the two course cards, Related Further Reading, and the trial panel. The page types differ at the hero and nowhere else.

Measured on both rendered pages at the close: the two feet are now identical, block for block, to the pixel.

---

## 2. The eleven rulings

**Heading five of the book note changed three times in one day**, each on the rendered page: the S314 wording, then "Where Could Further Exploration Lead?", then the live one, **"What are Your Next Learning Steps?"** DSRD 9 §32.7 is owed the correction; only the last stands.

**The courses block is one heading and one sentence on both pages.** "Want to Expand Your Understanding?" over "If you liked this article, these course options could be the next step in your learning journey." He gave the copy for both, then overruled this build's one edit to it: I changed "article" to "book note" on the book note page and he refused it, **"please accept the copy i gave you."** The sentence is identical everywhere, deliberately.

**The grey "Next possible steps after this Book Note" block is retired.** It was the only one of the four that existed on one page type. Its copy is preserved in section 4 so it is recoverable from the record.

**Related Further Reading is nine links**, and this went the long way round. He said the foot gave too many options; I proposed three or none; he corrected me to six, **"rather than removing the links (which wasnt what I wanted anyway)"**; then saw six rendered and ruled nine. The complaint was four competing blocks, not the links.

**A way back and a way forwards sit beneath them, with no rule between.** His labels: **"More Articles in this Category"** and **"Browse the Whole Knowledge Hub"**. On the hairline: **"please lose the hairline between the 6 links and the forward and back arrows."**

**The trial panel replaces the enquiries panel on both content pages**, as one shared block. His word for what he wanted was **"token"**. The copy and the picture are his; he replaced his own first wording with the second. The enquiries panel is unchanged and still closes About, Reviews, Testimonials, Our People and the Founders' Letter.

**The section header keeps its stretched icon box**, his S082 form: **"what I would like is the larger icon next to the text, next to the title, so it's kinda like two parts merged in."**

**The hairline in the S282 section header record is refused**, as a design judgement: **"I don't understand why you're putting hairlines underneath a heading title and subtitle when you have, like, the articles right underneath it."** `COMPONENT_DATA__section-header.json` carries that hairline and needs correcting: it belongs to the listing headers it was drawn for, where a View all control shares the line, not to a content page's section heading.

**The gap under every Hub section heading is 32, not 20.** Ruled on the measurement: the heading block is 51px tall, and 20 bound it more tightly to the row than the cards were to each other.

**The meta strip moves out of the hero to the head of the writing** on both pages: **"place this above the opening paragraph title, within the main article container."** The book note's carries no "Achology Publications". `SIGNED_SPEC__The_Individual_Article_Page_S302` block 3 and DSRD 9 §22.4 both place this line in the hero and are superseded.

**The author signature loses its band on the book note too**, extending his S082 article ruling: **"look the band on the book note template too please claude, so we can consistency across all templates."** DSRD 9 §22.7's card anatomy, the off-white ground, the 10px corner and the 20px padding, is withdrawn everywhere. Only two pages carry the block, so the rules moved onto the component in people.css.

---

## 3. What Chat is owed

DSRD 9 §32.7 (heading five), §22.4 (the meta line's placement), §22.7 (the card anatomy), §22.8 (nine links and the two ways out), §22.10 (the courses copy, both pages). `SIGNED_SPEC__The_Individual_Article_Page_S302` block 3. `COMPONENT_DATA__section-header.json`, the hairline. DSRD 7 §5.2 is owed one row: `arrow-left`, added to the icon registry for the way back.

---

## 4. The retired block's copy, preserved

Title: **Next possible steps after this Book Note**. Lead: **Three ways to deepen the integration of ideas inside the Knowledge Hub.**

Rows: *Browse the Articles that have been inspired by this book*, "Each article focuses on a core idea from this book and explores it thoroughly." *Explore our interpretation of Quotes taken from this book*, "We do quotes differently. We reflect on them carefully and discuss them in full." *Read the other Book Notes we have written in this category*, "We might inspire your next book buying decision, or simply inspire you, period."

All Kain's own words from the book note brief §6, kept here because they are his to bring back.

OWED BACK: the DSRD corrections above.

*No em or en dashes in this file; checked before writing.*
