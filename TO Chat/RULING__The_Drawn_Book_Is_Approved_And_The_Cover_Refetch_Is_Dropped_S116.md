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

## 4. The fold-back, per Harness Rule 14

The approved state is exported into the component's design folder, in the Component Design Prototypes folder, as `Book (ach-book)`: the prototype `achology-ach-book-proof-v1.html`, the build sheet `COMPONENT_DATA__ach-book.json`, and a README. **The prototype is exported rather than written:** its rules are lifted out of `components.css` at the moment of approval, so the top of the precedence chain cannot drift from what he said yes to. It links no live stylesheet.

## 5. What is still owed on this commission

The baked share image per book, and its stamp, untouched. The tabbed comparison under standing rule 16 was not run: the component was put in front of Kain on the real page instead, and he ruled on it there. The three variables are properties, so a tabbed pass costs one line each if he ever wants to move it.

---

OWED BACK: DSRD 8 is owed the component as a new section, and DSRD 8 section 31's centre-crop rule is owed a note that the 2:3 normalising the S360 reply proposed to retire it with is not happening, because the fetch that would have done it is dropped. The brief itself needs rewriting around what is left of it.

*No em or en dashes in this file; checked before writing.*
