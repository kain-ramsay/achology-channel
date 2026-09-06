# RULING and SHIP: the flagship card takes the DiMAP artwork and Kain's new copy

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Given by:** Kain, in the sitting, looking at the closing gateway block.
**Shipped:** theme v0.167.49, deployed with its three proofs. Also in this stretch: v0.167.45 to .48, below.
**Board card:** the closing gateway panel.

---

## His words, and what shipped on them

> "can you bake the DiMAP course image into the background of the Start Learning with Achology's Flagship Course card ... to the same transparency as the background image on the Accreditation Pathway card"

Done, and the transparency is not reproduced but reused: every value in that treatment already lives in `components.css` for any card carrying `has-bg`, so this is one data key and one CSS line. Fourteen per cent, filling the card, the diagonal mask fading it to a quarter at the top left, the border dropped and a dark inset ring in its place. Read back off the rendered page: the flagship card and the Accreditation card now match on opacity, size and mask exactly.

The picture is the DiMAP course's own artwork, already in the theme for that course's card, rather than a new file cut for this block. That is why it points at `images/courses/` where the other three point at `images/about/`.

**Worth knowing:** the whole `has-bg` treatment sits inside a `min-width: 1024px` media query, so the background shows from laptop width up and not below. The Accreditation card has always behaved that way; the flagship card now matches it.

## The replacement copy, his words exactly

> "Do you fully understand yourself and your psychological make up? If your answer is no, Achology's famous Diploma in Modern Applied Psychology (DiMAP) course could be the single, most valuable investment that you make into yourself this year."

Used character for character, with the apostrophe taking the file's `&rsquo;` form.

**One discrepancy, named to him in the same turn rather than quietly corrected.** It reads "Diploma in Modern Applied Psychology (DiMAP)". DSRD 5 section 1's catalogue name is "Diploma **Course** in Modern Applied Psychology (DiMAP)", and the line this replaces carried a note recording that the wording had read "Diploma in" once before and was corrected precisely because Course is the name the whole catalogue is keyed on. His words are the higher authority under Rule 14, so they stand as written and the question is with him. **If he says restore it, one word changes and I will file his answer.**

## The rest of this stretch, all on his word in the same sitting

**v0.167.45** the card gained a label above the three learning paths and lost the "On-Demand Training Courses" line repeated beneath each one.

**v0.167.46** the label reads "Three Learning Paths", chosen after four wordings were measured against the actual space. It is also DSRD 4 section 2's own title for them. It holds one line everywhere except a phone, where it folds by three pixels; he was told before choosing.

**v0.167.47 and v0.167.48** the block's heading and lead line moved into `achology_site_gateway()` beside the cards they introduce. They had been typed separately in all three page files, three copies of the same two sentences. All three pages now pass only their own heading id, and Testimonials stops borrowing About's. Verified on the three live pages: identical rendered markup, three distinct ids.

**These last two were the edits your S344 type line unblocked.** They landed within minutes of it arriving.

---

OWED BACK: nothing, unless DSRD 9's specification of this block records the copy, in which case it wants Kain's new sentences and the two structural notes above.

*No em or en dashes in this file; checked before writing.*
