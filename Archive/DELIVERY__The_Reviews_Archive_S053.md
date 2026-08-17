# DELIVERY: the Reviews page archive, block 6

**From:** Claude Code, Session 053. **Date:** 2026-08-10.
**Theme:** v0.45.1, deployed to achologytest.com, repo level with origin.
**Built to:** `PLAN__Reviews_Page.md` section 7, `INSTRUCTION__Reviews_Page_Build_With_Kain.md` sections 2 and 3, DSRD 8 section 14 (LOCKED), DSRD 9 section 29.6 decisions 1 to 4 and 8.
**Live:** https://achologytest.com/reviews/

Kain asked for the reviews list this session and it is built: the control bar, the live count, the full grid of 4,517 in the locked review card, and the batching. Block 5, the standouts, is deliberately not built and the reason is in section 5 below.

---

## 1. The batching mechanic, which was Code's call

**Batches appended in place, on a real link.**

The control is an ordinary link to the next batch of 24, carrying the current filter state. Follow it with scripting off and the page loads at that batch, so every one of the 4,517 reviews is reachable by following links, which the page's second job needs (DSRD 9 section 29.1: "to be the page that answers 'is Achology any good' for search engines and AI assistants"). With scripting on, the same link fetches its batch through a REST route and the cards are added under the ones already read, so a reader never leaves the page and never meets a row of page numbers. One query, one card renderer, two behaviours.

The alternative, everything in one document, was never available: 4,517 whole reviews is roughly 180,000 words.

## 2. What the control bar carries, and the one control missing

Search, Course, Rating. All three work, separately and together, and the count above the grid is the real found count from the query that just ran. Verified live: `?rv_q=anxiety&rv_c=cbt-practitioner&rv_r=3` returns "Showing 1 of 1 reviews" and that review mentions anxiety, is 3 stars and is on that course. `?rv_r=4.5` returns 542, which is exactly the 4.5-star count in the export.

**Theme is missing, and it is a data gap rather than a design choice.** DSRD 9 section 29.6 decision 8 asks for it. No review carries a theme tag: the plan's section 7 names the source, "One AI pass over the displayable reviews writes two columns in the Notion bank: the theme tag and the review title", and that pass has not run. The control drops in beside the other two the day the column exists. Not improvised around.

## 3. The review title is also missing, same cause

DSRD 8 section 14.2 item 2 makes the title the card's second element. It is the second column that same Notion pass writes, and section 14.5 says it is "drawn from that reviewer's own words, lightly trimmed, never invented", so Code does not write it (Harness Rule 8 too). The slot is built and the element renders the moment the field exists. Until then the card opens on the review's words.

**This is the one thing that would most improve the archive, and it is not blocked on anything Code owns.** If that Notion pass can be commissioned, it closes this and the Theme control together.

## 4. Two corrections to the importer, both to standards it predates

**Reviewer surnames were in WordPress.** The importer wrote the export's full names into the reviewer field and the post title, and its own header called the naming question unsettled. It was settled in writing before that file ever ran. DSRD 2 section 2.24: "Reviewer names display as first name plus surname initial ("Sarah T."), applied as a transform at import; the full surname never enters WordPress (UK GDPR data minimisation; Kain's ruling)." DSRD 4 section 14.4 and DSRD 8 section 14.5 say the same. The transform now runs at import and the bank was rebuilt through it.

Proof rather than assurance: every multi-word name in the bank now ends in a single initial, queried directly, and that query reads zero exceptions. It read three before, and those three are worth recording because they are how the rule got tight: a name typed as "Norman Arthur Russell 1953" made the plain last-word rule treat "1953" as the surname and leave "Russell" standing. Trailing tokens carrying no letter are now dropped before the surname is taken.

**Nothing was published.** All 4,517 sat as drafts, so an archive would have rendered empty. The draft default existed to hold the names back and it predates DSRD 9 section 29.6 decision 2 (Kain, S221): "All 4,517 reviews are shown, including the 3.0-3.5 star band." They are published now. The post type is still `public => false`: no review has an address of its own, and publishing only lets this page query them.

## 5. Why block 5, the standouts, is not built

Its source is the hand-picked **Featured** flag in the live Notion bank (plan section 6). The export shipped in the theme, `data/reviews.csv.php`, carries the Featured column **empty on all 4,517 rows**, and so does the Website Published column. There is nothing to render. Either a fresh export carrying the flags travels to Code, or the featured set arrives another way. The block will be inserted above the archive, not appended after it, so the plan's order holds.

## 6. One question for Kain, rendered both ways

DSRD 8 section 6.0: "Card Heights: Equal heights per row via CSS grid stretch." DSRD 8 section 14.2 item 3: "Full text, no clamp: the archive's credibility depends on whole reviews." Every other card family the first rule was written for clamps its text to three lines. A review does not, so on this data the first six rows measure 969, 1046, 896, 483, 1024 and 409 pixels, and a 256px review sits inside a 1046px card with the rest of it empty.

Both rules are right on their own. Rendered both ways on the same reviews, per the S258 render standard:

- as built, stretched: https://achologytest.com/reviews/
- each card at its own height: https://achologytest.com/reviews/?rv_fit=1

The switch is temporary and annotated as such in reviews.css. The loser is deleted the moment Kain picks and the winner folds back per Rule 14.

**A second thing his eye should settle at the same time**, because it is the same 277px column: at three across, a name like "Cathy K." wraps to two lines in the attribution row. Two across would give the reviews more room. The plan's "three across at desktop" is what is built.

## 7. Also for Kain, and deliberately not decided here

Part of the export is typed in capitals, so some cards read "OLEKSANDR D." No written standard covers case, so under Rule 5 it is not Code's to settle. It is left exactly as the student typed it and it goes to his eye on the rendered page.

## 8. Still open from the plan, untouched this session

The schema question (plan section 9, DSRD 9 O4). The eight theme labels' wording. The three copy slots now standing on the page: the archive's heading, its supporting line, and the hint line that teaches by example. All three are marked slots, not draft copy, the same device the map block used at S052.

## 9. What was registered

`Star` and `Search` joined the theme's icon registry in `shared-parts.php`. Both were already registered in DSRD 7 section 5.2 ahead of this build, at the rows quoted in the code. Star is held once as the ordinary Lucide drawing and filled by the card's own CSS, so the site keeps one Star path rather than two.

## 10. Gate

`css_gate` passes on reviews.css. Three items are annotated one-offs rather than silenced: the 599.98px phone breakpoint (the exception DSRD 7 section 4.5 already names), the empty-star warm grey #E4DED9 (named in place by DSRD 8 section 14.3), and the 8px artwork radius (DSRD 8 section 14.4's own value). PHP lints clean on the server.

Verified in the browser: 24 cards on load, count real, load-more appends to 48 and updates the count, filters combine, the 4.5-star half star renders as a clipped orange copy over the grey base, the no-results state reads honestly, and the course artwork loads.

*No em or en dashes in this file; checked before writing.*
