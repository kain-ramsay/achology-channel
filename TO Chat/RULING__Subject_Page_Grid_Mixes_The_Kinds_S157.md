**Needs from Chat: write this ruling into DSRD 9 section 20.0 (the grid, item 4) and its card sheet; the build sheet already carries it. For the theme session's record.**

# RULING: the subject page grid mixes the two kinds (Kain, Code's S157 theme sitting)

**Kain's words, on the built Psychology page in Safari:** "the different types of posts, they're not jumbled up particularly well ... on the top row there is like just four articles, second row four articles, third row four articles, fourth row four articles, so some sort of jumbling system where on each row you would have at least one ... different types of article type ... having a book note next to an article with an article underneath the book note that gives us the masonry effect."

**What was built at 0.707.160 (commit on main):**
- Each kind keeps its own newest-first order. The two are interleaved.
- The kind a subject holds fewer of takes at least one place per row of four, where it has enough pieces; otherwise every piece it has. Those places are spread evenly down the 48, and move along the row in a fixed rotation (third, first, fourth, second place) so the book notes do not stand in one column.
- It is fixed, not random: the page is the same on every load.
- This replaces "newest first across the rows" in the grid rule only for the mix between kinds; inside a kind, newest first still holds.

**Measured on the build site, all seven categories:** Psychology, Helping People, Personal Growth and Wisdom for Life: a book note in 11 of the 12 rows each, the last row being the masonry's levelled foot, which falls on four articles. Motivation (9 book notes), General Interest (5) and Mental Wellness (9 articles against 36 book notes) cannot give every row a mix and use all they have, spread evenly. Column feet level to within 1 pixel on every page.

**Prototype:** not re-exported. The frozen prototype still shows the old newest-first order; the build sheet's new "Decided in S157" row is the record (Harness Rule 14 fold-back owed: the prototype's next version).

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
