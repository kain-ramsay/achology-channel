# RULING: the figure register. Every published number gets one label and one icon

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.58.0, live and verified.
**Authority:** Kain, S053, ruled on two rendered pages in Safari. Written by me under the Rule 14 fold-back, because the approval happened on what I rendered.
**Supersedes:** the labels and glyphs previously live on the About and Reviews figure bars.

## What Kain saw, and named himself

He put the two figure bars side by side and asked whether I could see the same inconsistencies he could. He could, and they were real:

- **Countries** was a globe on About and a compass on Reviews.
- **The rating** was a star on About and a rosette on Reviews.
- **The quote glyph** meant "Total Student Ratings" on About and "Verified Reviews" on Reviews. One symbol, two meanings, on two pages a reader moves between.
- **The labels drifted the same way**: "Average Course Rating" against "Average Rating", "Countries With Students" against "Countries".

His instruction was not to reconcile the two bars but to record a standard, which is the right call: reconciling them by hand would have lasted until the homepage got its copy.

## The cause was in the code, not in anybody's care

DSRD 4 §14.2 says the global impact block is built once and shared by three pages. It was not. **About hand-wrote its four items as inline SVG. Reviews built its four with `achology_icon()`.** Two hand-built copies of one component will always drift, and these had already drifted in three glyphs and two labels before either page was finished.

## What is now built

**`achology_figures()` in shared-parts.php is the register.** Every published figure named once, with its value, its label and its icon:

| Key | Value | Label | Icon |
|---|---|---|---|
| rating | 4.66 | Average Course Rating | star |
| ratings | 175,162 | Total Student Ratings | award |
| reviews | 4,517 | Verified Reviews | quote |
| students | 695,578 | Number of Students | users |
| countries | 216 | Countries With Students | globe |
| courses | 28 | Total Number of Courses | library-big |

**`achology_figure_bar( array $keys )` renders it.** Both pages now call it and pass the figures they show, in their existing order. About: rating, ratings, countries, courses. Reviews: reviews, rating, students, countries. **A page has no wording or glyph left to choose**, which is the point.

The Reviews country panel follows the register too, so the compass I put there earlier this session is now a globe. That change was right locally and wrong across the site, which is a decent illustration of why the register had to exist.

**`globe` is now registered** in the icon set. It had been rendering on the live About page as hand-written inline SVG for months while the registry did not know about it, which is exactly the hole the drift came through.

**The values are frozen and stay frozen.** Kain's standing S052 ruling is untouched. The register is simply where the update will happen when he calls for it, in one place instead of four.

## One defect I introduced and caught before reporting

Swapping About to the register silently changed the courses glyph, because the register named `library` and the drawing Kain approved lives under `library-big`. The two keys hold different pictures. Caught by reading the rendered glyph back off the live page rather than trusting the deploy, and corrected before this note was written. Verified since: both pages now serve identical path data for every shared figure.

## What I need from you

1. **DSRD 4 §14.2 to carry the register**, since it owns the global impact block. This is the natural home for it.
2. **DSRD 7 §5.2 to add `globe`**, and to note that `library` and `library-big` are two different drawings, which is a trap the next person will fall into.
3. **A ruling on where a figure's register entry lives long term** once the block is carried across under S257. My reading: the register belongs to the component's build sheet, not to a page spec, because six pages will eventually read from it. That is a reading, not a decision.

**One thing worth saying plainly.** This is the second time today that the same underlying gap has surfaced: the global impact block is shared by three pages and is named by no DSRD 8 section. The gate run flagged it as a boundary-owner failure this morning and Kain found it by eye this afternoon. It is worth doing before the homepage build rather than after.

*No em or en dashes in this file; checked before writing.*
