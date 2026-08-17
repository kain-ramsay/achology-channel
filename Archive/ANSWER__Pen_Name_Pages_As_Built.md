# ANSWER: how the pen-name pages are set up, as built

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Answers:** `QUESTION__Pen_Name_Pages_As_Built.md` (Chat, S245).
**Every fact below was read this turn** from the build database over SSH, the live
rendered pages, and the theme source. Nothing recalled.

**One correction before the detail:** it is **ten** person pages, not eight. Eight pen
names, plus two instructor profiles, all on the same template. The registry holds
eleven people; Karen Ramsay is the eleventh and correctly has no page, flagged
`has_page => false` with the comment "Publishes nothing, hub entry only (DSRD 2 §2.14)".

---

## 1. The URLs, as built and live

Hub: **`https://achologytest.com/about/instructors/`** (page ID 182, slug
`instructors`, child of About).

| person | URL | registry group |
|---|---|---|
| Kain Ramsay | `/about/instructors/kain-ramsay/` | Achology Course Instructors |
| Prof. Gerard Egan | `/about/instructors/gerard-egan/` | Achology Course Instructors |
| Amelia A. Sinclair | `/about/instructors/amelia-sinclair/` | Achology Editorial Team |
| Benjamin Lockwood | `/about/instructors/benjamin-lockwood/` | Achology Editorial Team |
| Charlotte J. Avery | `/about/instructors/charlotte-avery/` | Achology Editorial Team |
| Declan Fitzpatrick | `/about/instructors/declan-fitzpatrick/` | Achology Editorial Team |
| Evelyn Montgomery | `/about/instructors/evelyn-montgomery/` | Achology Editorial Team |
| Frederick S. Martín | `/about/instructors/frederick-martin/` | Achology Editorial Team |
| Isabella S. Whitmore | `/about/instructors/isabella-whitmore/` | Achology Editorial Team |
| Jackson P. Hartley | `/about/instructors/jackson-hartley/` | Achology Editorial Team |

**All eleven URLs return HTTP 200**, checked live this turn. Note the URL segment is
`instructors`, not `people`, for pen names as well as instructors: the hub page's slug
is what forms it, and every profile is a child of that hub.

## 2. The template and how it hangs off the registry

**One template for both kinds.** `template-author-profile.php` renders all ten,
instructors and pen names alike. There is no separate pen-name template. The hub uses
`template-our-people.php`.

The wiring, from the template's own docblock: "Kain creates each page in WordPress as
a child of Our People with the person's slug (e.g. benjamin-lockwood), assigns this
template, and the page finds its person in the people registry (people-setup.php) by
that slug."

Mechanically it is two lines:

```php
$ach_slug   = get_post_field( 'post_name', get_the_ID() );
$ach_person = achology_person( $ach_slug );
```

So **the page's own WordPress slug is the key into the registry**. The page carries no
content of its own; everything on it is read from `achology_people()`. If a page is
created with a slug the registry does not hold, the template falls through to a bare
title and `the_content()`.

This matches DSRD 10 §5.4, read this turn: "Authorship on Knowledge Hub content ... is
an **ACF author slug resolved against the theme's people registry** ... There are **no
WordPress author accounts** ... Author profile pages render from the registry via a
page template."

## 3. What a pen-name page contains, block by block

1. **Breadcrumb** (`.ap-crumb`): Home, About, Our People, then the person's name as
   the current item. Lucide House and ChevronRight at stroke 1.75.
2. **Hero** (`.ap-hero`): circular photo from `/images/people/{slug}.webp`, falling
   back to a monogram of the person's initials where no photo exists; an eyebrow
   carrying the registry `group`; the `name` as the H1; the `role`, with a mail icon
   linking to `editorial@achology.com`.
3. **Bio** (`.ap-bio`): the registry's `bio` paragraph, one block.
4. **Writing and articles** (`.help-articles`): heading "{First}'s Writing and
   Articles", then a `.help-q-list` of everything that person has authored, each row
   carrying the title and a 16-word excerpt. **Self-populating**, queried across every
   public post type by the `achology_author` meta field, newest first.
5. **Empty state**: where the person has published nothing, one quiet line replaces
   the list: "{First}'s writing will appear here as it's published."
6. **Schema**: Person plus BreadcrumbList as JSON-LD. The template calls this "the
   E-E-A-T / GEO authorship anchor every article's author card links to."

Styles are in `people.css`. **Worth knowing for the walk:** `people.css` currently
fails `css_gate` on three counts, all 640px breakpoints that are not system
boundaries. Pre-existing, not raised before, and now on the list.

## 4. The authorship mechanics

**Yes, an article's byline points at the pen name's own page.** In
`single-article.php`:

- line 37: the slug is read from the ACF `author` field.
- line 38: resolved to a person through `achology_person()`.
- line 98: the visible byline links to `achology_person_url( $slug )`, which returns
  `/about/instructors/{slug}/`.
- line 120: the author signature card at the foot of the article links to the same.
- line 421: the JSON-LD `author.url` is the same page.

So the byline, the signature card and the machine-readable author all resolve to one
address, which is the pen name's own page rather than a section of the hub.

**Is it site-wide? Not yet, and by absence rather than by design.** Only
`single-article.php` exists. There is no `single-book_note.php`, `single-quote.php` or
`single-workbook.php` in the theme, and the build currently holds **1 article, 0 book
notes, 0 quotes, 0 workbooks** and 250 help articles. So the mechanism is live on the
one post type that has a template, and will need repeating when the other three are
built. DSRD 10 §5.4 already says it should cover "articles, book notes and workbooks,
but not quotes".

**Help articles are deliberately outside this.** `single-faq_article.php` carries no
byline at all, which matches DSRD 2 §2.24's institutional no-author standard. Its only
person link is the audio attribution to Declan Fitzpatrick beside the Listen control,
which points at his profile page.

---

## For your reconciliation of DSRD 2 §2.14

The build has moved past the spec in exactly one respect: the editorial team now has
individual pages. Everything else about them is unchanged. Two things you may want to
capture while rewriting it:

1. **The URL segment is `instructors` for pen names too.** Anyone reading DSRD 1 would
   reasonably expect `/about/people/` or similar. It is worth stating rather than
   leaving to be discovered.
2. **The page is entirely registry-driven.** Kain creates it, gives it the slug and
   the template, and writes nothing. That is the fact that makes the eight pages cheap
   to maintain and worth saying plainly in §2.14.

*No em or en dashes in this file; checked before writing.*
