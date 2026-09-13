# RULING: the article template was rebuilt with Kain across S112, and every decision below is his

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 112, theme session. **Date:** Sunday 13 September 2026.
**Given by Kain live in the S112 sitting**, on the rendered page at achologytest.com, one change at a time, over a full day.
**Filed under Harness Rule 14.** Theme 0.377.0 is live on the build ground and every ruling below is in it.
**Owning documents:** DSRD 9 section 22 (the article page), DSRD 7 sections 3 and 4 (type and space), DSRD 8 section 27 (the contents card). Chat writes them.

---

## 1. What happened, in one line

**The S111 sweep was started and the article page turned into a redesign.** The sweep's first family landed, and then Kain worked the article template with me from the top of the page to the bottom. The page that exists now is not the page that existed this morning, and he said so at the close: *"This page is unique. I've never seen an article page anything like this before."*

## 2. The page's shape, which is the ruling that matters most

**One grid for the whole article.** The banner, the writing and the foot obey one set of vertical lines. The hero's words sit directly above the writing and share its width; the hero's picture sits directly above the side column and shares its width. Content area 1104, reading column 800, gutter 48, side column 256. All tokens; `--container-rail` is new in base.css and is what 1104 minus 800 minus one gutter leaves.

**The furniture left the reading column.** The contents card and the share row used to sit inside the writing. Inside it they had only two possible shapes and both were wrong: floated they cut the line beside them to 47 letters, full width they blocked the top of the page. They now sit in a column of their own beside the writing, which takes no width from it.

**The side column, top to bottom:** the article's picture (square, appearing when the banner leaves), the contents, and the Know Your Psychology mark held to the foot of the screen. Those three travel as one panel the height of the screen. Below them, at the foot of the column, six related reading links and one way out.

**The page now ends:** writing, author with the share marks on his own line, two courses drawn from the article's own tags, footer.

## 3. Every ruling, in the order he gave them

1. The two cards inside the writing stop floating. Measured: the line beside them was 47 letters against the article's 87.
2. The contents leaves the writing for a column of its own, modelled on markmanson.net, which he brought.
3. The hero joins the same grid. Widening one without the other had put the writing 152px left of the hero.
4. The background marks are switched off on the article. His own approved design; switched off in one line, not deleted.
5. The dark course card comes off the page entirely.
6. The author card loses its sentence and stacks the role under the name, on every hub page type.
7. The share row moves from the panel to beside the author, then into the author's own row, small, square, aligned on his bottom line.
8. The contents card becomes a panel: no fill, no border, no padding, heading down a step.
9. An orange line divides the writing from the panel, then becomes a grey hairline running the full height of the writing, because orange should mean one thing.
10. The Know Your Psychology mark joins the column, then becomes the generic artwork, then the full-width panel image, then pins to the foot of the screen and links to `/learn/`.
11. Related Further Reading moves into the column as a labelled shelf of six, dressed in styles the column already had.
12. The type in that column: one typeface, three sizes, one leading per size, one label treatment for both lists.
13. The standfirst takes a measure of 55 letters, and its size goes to 21, the step above the body.
14. The byline leaves the hero. The author stays in the page's structured data and at the foot.
15. The course block's heading and sentence take his new words: "Want to Take Your Interest Further?" over "Explore related courses and deepen your understanding with insights you can use in everyday life."
16. The trial panel takes his new words, given earlier the same day.

## 4. Two things Chat should carry into the DSRDs with care

**DSRD 7 section 4.1 gains a second column width.** `--container-rail`, 256px, derived rather than chosen. Its note should say so, because the day the reading column moves this has to move with it.

**A measure can be written in characters.** The standfirst is capped at 55 letters rather than a pixel width, so it holds its LENGTH when the face or the size changes. That is the first place on the site where a measure is expressed the way section 4.1 describes it, and it is worth naming as the pattern.

## 5. What is not done, and is the next session

**This page does not pass its own gate.** `page_gate.py` returns 40 passed, 12 failed. Two failures were mine today and are fixed. The rest are real and mostly content: a dead link to `/learn/mental-wellness/book-notes/resilient/`, four acronyms used before being spelled out, a keyword at 0.30 per cent against a 1.0 floor, no DSRD 6 record on file, and a recorded Rank Math score older than the page. **The template looks the way Kain wants and this page is not publishable by his own standard; those are different things.**

**The five author biography headings are not applied.** Chat's `REPLY__The_Five_Author_Biography_Headings_Reworded_By_Kain_Sweep_The_51_S357` arrived mid-sitting. Verified this session on the live install rather than from memory: **51 published `article` posts carry those headings and no other post type does**, which matches the 51 records exactly. No help answer, book note or quote page is affected.

OWED BACK: DSRD 9 section 22 and DSRD 7 sections 3 and 4 written to the above, and DSRD 8 section 27 for the contents card's new form.

*No em or en dashes in this file; checked before writing.*
