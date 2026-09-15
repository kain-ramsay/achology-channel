# REPORT: dead code across the whole theme, checked against the live site, not guessed at

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Kain's question:** is there dead code anywhere on the site that needs removing.
**Method, and where the first pass was wrong.** A code-only scan of all 39 PHP files, 19 CSS files and 13 JS files first flagged 98 CSS classes as unused. Checking that against real pages found real usage for most of them: several page-specific classes (the Founders' Letter signature line, the About page's four background tiles, the policy pages' numbered clause headings and pull-quote style) are written straight into the page's own content rather than into a template file, so a search of the code alone cannot see them. **Every one of the numbers below was then checked against actual rendered pages**: all 33 site pages, a sample across every content template, and the full stored text of all 579 published posts. Nothing here is reported from the code search alone.

---

## Confirmed dead: 21 CSS rules

**Twelve of them are one whole abandoned system.** `.type-h1` through `.type-stats-large`, a set of utility classes for headings and body text, traced back to the theme's very first recorded version. The site has used CSS custom properties directly (`var(--text-24)` and so on) ever since, on every page checked; this older, parallel class system was never adopted and nothing on the live site reads it.

**Two more of the same shape.** `.sp-2xl` and `.sp-3xl`, spacing utility classes from what looks like the same early attempt. Spacing is handled the same direct way everywhere else.

**Seven small, scattered leftovers, one page or one component each:**
- `.bn-next` (book-note.css)
- `.icon-pagination`, `.icon-stats`, `.quote-container` (base.css)
- `.kh-course-hero-label` (knowledge-hub.css)
- `.portrait-bg` (cards.css)
- `.pp-overline` (people.css)

None of these render on any of the roughly forty real pages checked, across every page type the site has.

## Confirmed dead: 3 PHP functions

`achology_article_promo_card` (knowledge-hub-parts.php), `achology_faq_question_icon` and `achology_icon_stop` (faq-icons.php). Defined, never called from anywhere else in the theme.

## Already reported separately: 1 unused variable

The reading-bar variable in `single-book_note.php`, named in the writer-photo report.

## What I am not calling dead

**Five classes in quote.css** (`.qp-eyebrow`, `.qp-hook`, `.qp-open`, `.qp-open__label`, `.qp-open__text`): not used today, but the quote page template is still being finished, and these look like they belong to that unfinished work rather than to something abandoned. Wrong to remove alongside genuinely dead code; right to leave named here so nobody has to rediscover them.

---

## What I have not done

Deleted anything. Removing CSS and functions is a real change to the theme, even when nothing renders differently, and I would want to check the affected page types in Safari after each batch rather than assume a rule with no reference is truly free to remove. Recommend it as its own small, named piece of work: strip the 21 rules and 3 functions, run `css_gate.py` and a visual check across the page types they touch, one commit.

---

OWED BACK: your word on whether to go ahead and remove the 21 plus 3, in one pass.

*No em or en dashes in this file; checked before writing.*
