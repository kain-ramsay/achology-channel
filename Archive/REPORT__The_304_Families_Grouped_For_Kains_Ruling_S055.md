> **DISPOSITION, Session 267, 12 August 2026.** Kain ruled six of the nine groups in one sitting. Five one-word yeses settled 203 families: plugin and WordPress classes out of the census, state switches utility, text sizes utility, screen reader helpers utility, single-template families page-local. Then all seventeen site-wide furniture families were ruled library components, in his words a long overdue decision. Two groups needed nothing: the cards are settled, and the dead stylesheet list is a deletion job with its own commission. Both rulings written to Code for the registry, and the Component Truth System board card carries them. STILL OPEN: group 7's twenty-five, and the four exceptions inside group 8. Two renders commissioned so Kain can rule on the two breadcrumbs and the five copies of the Where Next panel by looking at them. Archived.

# REPORT: the 304 families, grouped so Kain can rule in nine decisions instead of 304

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Answers:** `COMMISSION__Group_The_304_Families_For_Kains_Ruling_S266.md` in full.
**Every family is in exactly one group. 304 accounted for, 0 unaccounted.**

## Read this before the groups: I had to correct the census first

Grouping the families by how many templates emit them surfaced a fault in my own instrument, and I fixed it before grouping anything on it.

**The emitter count in the S055 census report was wrong for common words.** It searched each template for the class name surrounded by quotes or whitespace, which counted ordinary English. `in` came back as emitted by 45 templates and `read` by 31. They are real classes in about.css, and the counts were prose.

It now reads class attributes only: each template is reduced to the set of class names actually written into a `class="..."`, and membership is an exact match against that set. **Four numbers in my previous report are corrected here:** `breadcrumb` is 13 templates, not 17; `btn` is 8, not 10. `page-container` at 16, `policy-breadcrumb` at 13 and `help-q` at 10 were right. The finding those numbers supported is unchanged and if anything sharper.

**How it was caught, because the method is the point:** a state modifier appearing on more templates than the site header is not a plausible number. Grouping put the implausible number next to plausible ones. Nothing in the flat table would have shown it.

The fix undercounts rather than over. A class written by PHP rather than typed is not counted, and that prints as "no template found" where somebody looks, rather than as a confident number.

---

## The nine groups

### Group 1: things that are not ours at all. 17 families. One yes.

Classes belonging to the cookie consent plugin, to WordPress itself, and to the icon library. The theme styles them; it does not own them and never designed them. None of it needs a prototype, a build sheet or a DSRD section.

**Recommendation, marked as one: rule the whole group out of the census.**

`admin-bar`, `emoji`, `lucide`, `wp-smiley`, and fourteen `cmplz-` families.

### Group 2: on-and-off switches, not things. 11 families. One yes.

These say what state something is in, not what it is: open, active, selected, playing. They attach to other things and have no existence of their own.

**Recommendation: utility.**

`is-active`, `is-collapsible`, `is-flat`, `is-open`, `is-playing`, `is-selected`, `consumed`, `has-bg`, `lit`, `pop`, `swapping`.

### Group 3: the text styles. 13 families. One yes.

The named text sizes and weights from DSRD 7 section 3, written once in base.css so every page can reach for them. The type system, not a set of components.

**Recommendation: utility.**

`type-hero`, `type-h1` to `type-h4`, `type-body`, `type-body-emphasis`, `type-body-small`, `type-caption`, `type-nav`, `type-overline`, `type-small`, `type-stats-large`.

### Group 4: things that exist for screen readers. 3 families. One yes.

Text hidden from sight but read aloud, and the skip link.

**Recommendation: utility.**

`sr-only`, `visually-hidden`, `skip-link`.

### Group 5: the card system, already settled. 3 families. No ruling needed.

Every card shares one class family, and the cards already have prototypes, build sheets and DSRD 8 sections. Needs matching to the registry, not deciding.

`card`, `card-grid`, `card-product`.

### Group 6: site-wide furniture, used everywhere, recorded nowhere. 17 families.

**This is the group that matters most and it is the one to give him first.** Each appears on between five and seventeen page templates. These are the parts a visitor meets on nearly every page, and almost none has a prototype, a build sheet or a DSRD section, while much smaller things hold full sections.

**Recommendation: library components, every one.** A thing on seventeen templates that nobody has ever approved by eye is the definition of the gap this census exists to close.

| What it is | Family | Templates | Declared in |
|---|---|---|---|
| The Where Next panel at the foot of a page | `policy-next` | 17 | five stylesheets, split |
| The page's outer width container | `page-container` | 16 | three, split |
| The breadcrumb trail | `breadcrumb` | 13 | two, split |
| The breadcrumb's own arrow icon | `icon-breadcrumb` | 13 | base.css |
| A second, different breadcrumb | `policy-breadcrumb` | 13 | three, split |
| The related questions block | `help-q`, `help-q-list` | 10 each | two each, split |
| The popular questions block | `help-popular` | 9 | three, split |
| The article's reading column | `article-container` | 8 | base.css |
| Buttons | `btn`, `btn-primary` | 8 and 5 | three, split |
| The policy page shell and its parts | `policy-page`, `policy-header`, `policy-body`, `policy-lead`, `policy-title`, `policy-num`, `policy-doc` | 5 to 7 each | mostly split |

**Two things here are questions rather than group members.** There are **two different breadcrumbs**, `breadcrumb` and `policy-breadcrumb`, each on thirteen templates. And **`policy-next` is declared in five separate stylesheets**, the strongest case anywhere in the census for duplicated rather than shared.

### Group 7: shared by a handful of pages. 25 families.

Two to four templates each. Too widely used to be page furniture, not widely enough to be site furniture. The honest answer here is usually "it belongs to one section of the site".

**Recommendation: library where the family crosses sections, page-local where it stays inside one.** Worth putting to him in five small lots, because they divide cleanly: the About family (`about-header`, `about-hero`); the Help family (`help-articles`, `help-cat`, `help-group`, `help-hero`, `help-page`, `help-contact`); the Knowledge Hub family (`kh-empty`, `kh-grid`, `kh-pill`, `kh-section`); the author pages (`ap-crumb`, `ap-eyebrow`, `ap-name`); and the genuinely site-wide leftovers (`btn-secondary`, `pagination`, `product-section`, `warm-room`, `icon-section-header`, `icon-section-header-container`, `ico`, `policy-closing`, `policy-related`, `policy-aristotle`, `current`).

**`warm-room` is the closing enquiries panel** and is already a registry row. It lands here on the evidence, which confirms the registry rather than contradicting it.

### Group 8: things that live on exactly one page. 159 families.

Over half the census. Each appears on one template only, which is the DSRD 8 section 12 definition of a page-local block, so **the default answer for the whole group is page-local, one yes**, with four exceptions to pull out first.

They group cleanly by the page that owns them:

| Page or partial | Families |
|---|---|
| the About page | 42 |
| the footer | 20 |
| the shared partials file | 17 |
| the Book Note page | 9 |
| the header | 8 |
| the author profile page | 7 |
| the Knowledge Hub parts | 7 |
| Our People, Reviews, Testimonials | 6 each |
| the help article, the Knowledge Hub article | 4 each |
| eleven other templates | 1 to 3 each |

**The four exceptions, which are site-wide despite the count of one**, because they come from shared partials or the site chrome:

- **The footer's twenty families**, including `cta-card`, already a registry row. The footer is one component, not twenty page-local blocks.
- **The header's eight**, including `navcard` and `nudge`, both already registry rows.
- **The seventeen in `shared-parts.php`**, a shared partial by definition. `shared-video-lightbox` and `story-proof` are both in here and both are already registry rows.
- **`author-card`**, emitted from `people-setup.php`, which is your S266 finding. It counts as one template because it comes from a setup file, and it renders on both article and book note pages.

### Group 9: declared in CSS, emitted by nothing. 56 families.

No template writes these classes.

**Recommendation: this is not a disposition question at all.** It is the dead-CSS list, and 35 of them are already ruled dead in `COMMISSION__Delete_All_35_About_CSS_Dead_Classes_S266`, which is why about.css dominates with 28. Do not put this group to Kain as a disposition question; it is a deletion job with its own commission.

| Stylesheet | Families |
|---|---|
| about.css | 28 |
| components.css | 7 |
| base.css | 6 |
| cards.css | 6 |
| book-note.css | 2 |
| seven others | 1 each |

**The caveat that matters before anything is deleted:** "no template emits it" is not the same as "dead". `ach-select`, `facet-row` and `facet-rows` are the filter bar, which JavaScript builds. `strip-tick`, `scrolled`, `in`, `read` and `reached` are state classes added at runtime. **Nothing here should be deleted on this evidence alone.** The 35 already ruled were verified individually and that is the standard the rest need too.

---

## What Kain actually has to answer

Five one-word rulings (groups 1, 2, 3, 4, and the group 8 default), three short conversations (group 6's seventeen, group 7 in its five section lots, and the four exceptions inside group 8), and nothing at all for groups 5 and 9.

**If he only has time for one, make it group 6.** Seventeen pieces of furniture a visitor meets on nearly every page, none ever approved by eye, two of them doing the same job as each other.

*No em or en dashes in this file; checked before writing.*
