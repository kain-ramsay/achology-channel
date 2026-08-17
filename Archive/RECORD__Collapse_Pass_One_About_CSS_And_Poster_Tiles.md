# RECORD: collapse pass one. The About CSS and the poster tiles, and a question the pass exposed

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Against:** `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md`, items 1 and 3.
**Commit:** `76b228e`. The brief asks for the block family, its one home, and the
evidence, filed here per pass. All three follow.

---

## The families collapsed, and their one home

| block family | one home |
|---|---|
| The About page's CSS | `about.css` in the theme, loaded after the shared sheets in the production enqueue order |
| The five member poster tiles | `achology_member_stories()` in `shared-parts.php` |

## What was removed

**Three hand-authored "PROPOSED about-page CSS" blobs**, 553 lines of CSS and markup
across eight constants, duplicating a live `about.css` of 1,028 lines. Your brief
called this "the largest remaining lie in the preview system" and that was accurate.

**Two of the three were also dead.** They wrote `about.html` and were overwritten by
the third before anything read the file. I checked for any read between the writes
before removing them rather than assuming.

**A private copy of the five poster tiles**, built from a hardcoded list of Vimeo ids
and image filenames, and never read by anything. Directly beside it, `ABOUT_PROOF`
already renders the real `achology_member_stories()` through `_php_render.py`, with a
comment claiming the preview "cannot drift from the page". The copy was the drift.

## Two pre-existing breakages found, both proved before the change

This is the part worth your attention, because it is the rule's own argument made
concrete.

1. **The dead poster copy still asked for the five images by their old Vimeo-id
   filenames.** They were renamed to descriptive names during the About build,
   `SPEC__About_Page_Locked_Structure_And_Copy.md` §8 item 5. The builder had been
   crashing there ever since.
2. **`achology_asset()` began stamping the theme version onto asset URLs at v0.38.9**,
   which put `wp_get_theme()` on the path of every renderer that emits an image. The
   preview render harness stubs five WordPress functions and had no stub for that one,
   so every `php_render()` call died with an uncaught Error.

I verified both were present before my edit by stashing my change and running the
unmodified builder: it crashed identically.

**Net effect: the About preview could not be produced at all since v0.38.9, and nobody
noticed.** Both breakages are fixed and the builder runs to completion again.

## Verification, on the rendered preview

- No `PROPOSED about-page CSS` blob anywhere in `about.html`.
- `base.css`, `components.css`, `policies.css` and `about.css` all present and marked
  "(live theme file)", injected by `_refresh_previews.py`.
- The H1 computes as **Como 32px/700** from the live sheet, which is DSRD 7's value.
- **Five** poster tiles present, from the real renderer.
- Builder compiles and runs clean; 61 previews refreshed against the live theme.

---

## The question this pass exposed, and it is item 2

**Item 2, frozen preview content, cannot honestly be closed by re-authoring markup.**

The About preview's markup is still a hand-authored snapshot. It has no hero action,
no founders block, no closing enquiries panel and no back-to-top control, because all
four shipped after it was frozen. So the CSS now tells the truth and the markup still
does not.

I could generate the markup from `page-about.php` as well. Before I spend a session on
that, the prior question deserves an answer, because I think it changes the work:

**Should a preview of a shipped page exist at all now?**

Harness Rule 12 says Code deploys and Kain views the rendered live page. The About page
is live. A local preview of it can never be more truthful than the page itself, is a
second copy by definition, and this pass has just shown it was silently broken for
days without consequence, because nobody needed it.

**My recommendation:** retire the previews of pages that have shipped, and keep the
preview system only for what it is genuinely for, which is showing Kain something that
does not exist yet. That would close item 2 by deletion rather than by building a
second renderer, and it would empty most of §2.6's duplicate register at a stroke.

**What I have not done:** deleted anything of the sort. The `about-fiveacts-*` previews
are superseded design explorations and the constants they use are the ones I left in
place. Whether they should exist is the same question and it is not mine to answer.

## What remains on the register

- **Item 2**, frozen preview markup, waiting on the question above.
- **Item 3's remainder**: the routes rows and circular member cards in
  `help-parts.php`, `template-policy.php` and `404.php` are not yet audited. Next pass,
  one family at a time, unless the answer above makes some of it moot.

*No em or en dashes in this file; checked before writing.*
