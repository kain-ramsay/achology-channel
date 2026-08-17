# REPORT: the collapse pass, and why the About preview cannot be collapsed as your brief describes

**From:** Claude Code, S230. **Date:** 2026-07-29. **Answers:** `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md`.
**Nothing was changed. Two of your three items are already closed, and the first turns out to be a different problem from the one the brief describes.**

## Item 3 first: the private copies are gone, verified

You asked me to audit what remained of the routes rows, poster tiles and circular member cards after v0.36.29 and v0.36.30. Audited across every template and every builder:

- **The routes grid, the member stories and the member voices are authored once**, in `shared-parts.php`, as `achology_routes_grid()`, `achology_member_stories()` and `achology_member_voices()`. `page-about.php` and `page-testimonials.php` call them. No template carries its own copy.
- **The preview builders call the real renderers**, not copies. `_build_testimonials.py` runs the actual `shared-parts.php` functions through `_php_render.py`, with a comment in the file saying why: "this preview cannot drift from what the page ships".
- The remaining matches for "poster" and "member-story" in `about-setup.php` and `page-testimonials.php` are **data, not markup**: ACF field names, and the testimonial JSON the page ships. Data in one place is not duplication.

**Item 3 closes.**

## Item 2: preview markup is generated, not frozen, on the pages that were promoted

Same evidence: where a block was promoted to `shared-parts.php`, its preview renders from that home through `_php_render.py`, so a copy edit reaches the preview without the builder being touched. That holds for the routes grid, member stories, member voices and the testimonial cards.

It does **not** hold for the About page, and that is the same problem as item 1.

## Item 1: the About preview is not a stale copy of the About page. It is a different page.

Your brief says: "the About preview renders a 'PROPOSED about-page CSS' copy rather than the live about.css. Collapse it: the preview renders the live stylesheet, and the blob is deleted."

I compared the two before touching anything, and the premise does not hold:

| | Selectors |
|---|---|
| Live `about.css` | 85 |
| The builder's blob | 30 |
| **In the blob, absent from the live stylesheet** | **17** |
| **In the live stylesheet, absent from the blob** | **72** |

The blob styles a story-era system: `.story-era`, `.story-era__dates`, `.story-row__stat`, `.story-dot--dashed` and the rest. **None of that exists in the theme.** The live About page is built from a different vocabulary entirely, `.cons-shell`, `.cons-stage`, `.cons-count` and 69 others, none of which the blob knows about.

So swapping the stylesheet would not collapse a duplicate. It would leave the preview's markup, which is story-era markup, entirely unstyled, and would show a page nobody has ever built.

**What this preview actually is: a prototype of a design that was proposed and not adopted.** It has been rendering a design that does not exist, in a folder Kain opens to look at what the site does.

## What I recommend, and have not done

**Retire the About preview rather than collapse it.** Previews exist because a page cannot be seen before it is built. About is built, it is live at `/about/`, and Kain can open the real page, which is the standard the harness sets anyway: show pages, never measurements. A preview that disagrees with the built page is worse than no preview, because it is a second source of truth, which is what DSRD 3 section 2.6 exists to stop.

That means deleting `previews/about.html`, `previews/about-lightweight.html` and the `STORY_CSS` and `ABOUT_CSS` blocks that build them. It is a deletion of work Kain once approved, so **I have not done it.** Your ruling, or his.

**If the story-era design is still wanted**, this is not a preview problem at all: it is an unbuilt design sitting in a builder script, and it belongs on the board as a design decision rather than in a collapse brief.

## What is left of the brief after this

Only item 1, and it is now a yes or no rather than a collapse: retire the About preview, or record why it stays. Your section 2.6 duplicate register empties either way.

*No em or en dashes in this file; checked before writing.*
