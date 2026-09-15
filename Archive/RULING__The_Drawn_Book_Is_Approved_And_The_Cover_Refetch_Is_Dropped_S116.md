> CHAT DISPOSITION, S360: CLOSED, ARCHIVED. Recorded at DSRD 8 §31 (cover-crop correction, withdrawn normalise-at-fetch plan) and new §33 (the ach-book component in full). The brief this answers is superseded; a corrected version is being written separately.

# RULING: the drawn book is approved, the cover re-fetch is dropped, and the brief's sequencing hold is lifted

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 116. **Date:** Monday 14 September 2026.
**Authority:** Kain, live in the S116 theme sitting, on the rendered page.
**Answers:** `BRIEF__The_Book_Cover_Becomes_A_Drawn_Book_Everywhere_From_Clean_Covers_Fetched_By_ISBN_With_A_Baked_PNG_S360.md`, which arrived mid-sitting while this was being built.
**Board card:** Book note page template: second look in Safari.
**Read this cold.**

---

## 1. Three of Kain's words, in the order he said them

**He asked for this next, ahead of the quote page.** "I think it might be worthwhile taking on the book image first before we move on to the quote page." The S360 brief's section 0 says "do not start yet" pending two prerequisites. His word lifts that, and the S357 version's own section 5 had already allowed for it in the words "unless Kain says otherwise". Named here rather than left for Chat to find.

**He stopped the re-fetch.** He interrupted the moment he saw what I was doing: "are you away researching to see if you can find book covers for books that we already have book covers for ... I don't think that we need to go and resource all the book images all over again." He was right, and section 2 is the evidence.

**He said what he actually wanted.** "All we need to do here is take the images that we have and make them look a bit more three d ... a tool that spits out a three d style image that doesn't look totally cliched."

## 2. The re-fetch is dropped, and here is why it could not have worked

Measured before anything ran, on this machine, against the live services:

- The cover this site serves for The Ultimate Life Coaching Handbook is **1000 by 1500**.
- Open Library's **largest** cover for these titles is about **320 by 500**. A sample of eight ISBNs returned 316x500, 265x400, 325x500, 321x500, 314x500, 329x499, one at **128 by 193**, and one 404.
- Google Books, the brief's named fallback, answers **429, quota exceeded**, to every call.

So the fetch would have replaced good files with files a third of the size, and **section 2's gate line, "the cover must come from the ISBN fetch at or above 1200px", cannot be met by the source section 1 names.** That gate line should not be built.

**One correction for whoever rewrites this.** The brief says to read each book's ISBN from the master workbook's Books tab. There is no ISBN column there; the columns are ID, title, author, author link, subtitle, the two categories, the Genius link, the Amazon search URL, the cover image, slug, three tag sets, keyphrase, title tag, meta description, synonyms, course, blurb, related and source. The ISBNs are in the records themselves: **103 of the 153 book note records carry one, 50 do not.**

## 3. What was built instead, and approved

`ach-book`, a sealed component that draws the cover the record already holds as a physical book. Kain approved it on the rendered book note hero with one word: yes.

**It is nearly straight on, and that is the ruling's substance rather than a detail.** His one constraint was that it must not look cliched. The stock version of this effect is a jacket at forty five degrees with a fat spine and a hard drop shadow: it reads as clip art beside photography and typesetting, and it tilts the book designer's own title onto a slant nobody chose. Every part of the depth here is something a real book has: the block of pages down the fore-edge with the banding of leaves, the crease where the front board meets the spine, and one soft shadow sitting close underneath.

**Sealed per DSRD 8 section 26.** A caller passes a cover and its alt. The depth, the paper, the crease and the shadow are the component's and are set once for the site.

**Where it is drawn today:** the book note hero, the quote page's source book block, and the article's source book callout, which renders on no article today and is changed with the others so that the day one does, it draws the same book.

**Where it is not drawn yet, named rather than left quiet:** the book note side column's thumbnail, which sits inside the band that opens as the hero scrolls away, which is Kain's own S112 behaviour; changing what is inside that band unseen is how that behaviour breaks, so it waits for its own sitting. With it, the book note card, the Knowledge Hub home page and the author biography's book list.

## 3a. What he changed after the first yes, and the state he locked

The first yes came on the hero at 0.423.0. Four things moved after it, each on his eye and each read back off the deployed page, and the state he locked is 0.425.3. His words: "that's good Claude, lets lock in all of these changes".

1. **The fore-edge could not be seen.** A version softening the banding inside it read back correctly off the live page and he could not see any difference at all, because at 13px wide there was nothing there big enough to soften. He was right and it is recorded as a wasted change rather than quietly dropped. The depth went to 9 per cent.
2. **Nine was an overcorrection**, made unmistakable rather than right. He asked whether each book needed to show quite so thick. It is 7 per cent, about 18px on the hero, and it is the first of the three he has seen that was judged against the other two rather than against nothing.
3. **The jacket was being trimmed.** Thickening the fore-edge exposed it: the shape was declared on the book's outer box, so a cover giving up width to the pages sat in a box of the wrong proportion and object-fit took the difference off the artwork, four and a half per cent from each side, clipping the ends of the Handbook's own subtitle rules. The cover carries the shape now and the book takes its height from it. Refusing to distort the book designer's work is the whole reason this component does not tilt, so cropping it to make room for the pages was the same fault by another route.
4. **The gap to the button below it** measured 8, which is smaller than every step in the ladder Kain ruled for this column at S114. It is 16, his own step for two things in one group.

**And one thing put to him and left as it is:** every book shows the same thickness, and real books do not. A fore-edge varying with a book's own page count would need that count held per record, which nothing does today.

## 4. The fold-back, per Harness Rule 14

The approved state is exported into the component's design folder, in the Component Design Prototypes folder, as `Book (ach-book)`: the prototype `achology-ach-book-proof-v1.html`, the build sheet `COMPONENT_DATA__ach-book.json`, and a README. **The prototype is exported rather than written:** its rules are lifted out of `components.css`, so the top of the precedence chain cannot drift from what he said yes to. It links no live stylesheet.

**Re-exported at the lock-in.** The first export held 0.423.1, which four of his own changes then overtook. It was deliberately left stale between the first yes and the lock-in, because a prototype is the state he approved and not the state of the file; the moment he locked, it was exported again at 0.425.3 and the build sheet rewritten to match. The two now agree with the page.

## 5. What is still owed on this commission

The baked share image per book, and its stamp, untouched. The tabbed comparison under standing rule 16 was not run: the component was put in front of Kain on the real page instead, and he ruled on it there. The three variables are properties, so a tabbed pass costs one line each if he ever wants to move it.

---

OWED BACK: DSRD 8 is owed the component as a new section, and DSRD 8 section 31's centre-crop rule is owed a note that the 2:3 normalising the S360 reply proposed to retire it with is not happening, because the fetch that would have done it is dropped. The brief itself needs rewriting around what is left of it.

*No em or en dashes in this file; checked before writing.*
