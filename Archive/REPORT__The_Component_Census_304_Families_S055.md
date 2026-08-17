> **DISPOSITION, Session 267, 12 August 2026.** The census this file delivered is now fully ruled. Kain settled all 304 families in one sitting off the grouping report: 203 in five one-word rulings, the seventeen site-wide furniture families as library components, and the remainder split between page-local, section-local and library. The four families that looked page-local but are site-wide, including the author card this report found on every article and book note page, are library components. All rulings are written to Code for the registry and the Component Truth System board card carries them. Two questions remain, and neither is a classification: whether the two breadcrumbs are one thing written twice, and whether the five copies of the Where Next panel are identical. Both go to Kain's eye on rendered pages. Archived.

# REPORT: the theme's component census, Act 1. 304 families, and 262 of them are named nowhere in DSRD 8

**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Answers:** `COMMISSION__Harvest_The_Themes_True_Component_Census_S266.md`, Act 1 in full.
**Also answers, as a by-product:** `ANSWER__Check_4_Membership_Ruled_The_Component_Registry_S265.md`'s ask for the class prefixes.
**The instrument:** `component_census.py`, in the theme. Full table available as tab-separated data on request or by running `--tsv`; it is 304 rows and I have not pasted it whole into the channel.

## The headline, and it is worse than the six

You found six live class families named nowhere in DSRD 8 by reading the stylesheets. **The harvest finds 262, out of 304 families total.**

- **304 class families** across 16 stylesheets.
- **262 named nowhere in DSRD 8** (86 percent).
- **29 declared across more than one stylesheet.**
- **83 with no emitting template found**, which is the dead-CSS question from a different direction.
- The run takes 31 seconds.

Your six (`author-card`, `pp-card`, `navcard`, `nudge-card`, `cta-card`, `shared-video-lightbox`) are all in the 262, and they are not the interesting part of it. The interesting part is that reading found six and counting found 262, on the same theme, on the same day. That is the census argument proved rather than asserted.

**One honest caveat on the 262 before anyone acts on it.** The count includes families that are not ours and never were: `cmplz-*` (14 families, the Complianz consent banner), `wp-smiley`, `admin-bar`, `emoji`, `lucide`, and the WordPress `has-*` utilities. Those are plugin and platform classes the theme styles rather than owns. I have not removed them, because Act 1 says report facts and do not judge disposition, and "is this ours" is the first half of the disposition question that is Kain's. **But nobody should read 262 as 262 undocumented Achology components.** Stripping the obvious third-party prefixes takes it to roughly 244, and how many of the rest are utilities rather than components is exactly what Act 2 decides.

## How it ran, so Act 4 can reuse it rather than rewrite it

1. Every `*.css` in the theme is parsed for selector text, with comments and at-rule heads removed first, because declarations carry dots too (font sizes, decimals, urls) and counting those invents families that do not exist.
2. Every class token in every selector is rolled to family level: **the prefix before `__` or `--`**, exactly as the commission specified, so `.card__title` and `.card--mini` are one row named `card`.
3. Each family is also given a **cluster**, its first hyphen segment, reported beside the family and never instead of it. That is what makes the `gi-*`, `help-*` and `tm-*` groups visible as groups without breaking the grouping rule you set.
4. Emitting templates are found by searching every `.php` in the theme for the family's actual class names. `previews/` and `harness/` are excluded: previews is retired ground under Kain's S245 ruling, and crediting a family to a template nobody serves would be a false positive.
5. DSRD 8 presence is a plain word-boundary text search of the family name, reported as a fact.

It is a single script with no dependencies and no network, so wiring it into the birth gate at Act 4 is a matter of calling it and diffing against the registry.

## The split cases, which you asked to be flagged

Eighteen of the 29 splits are both split and absent from DSRD 8. These are the ones where "shared component or duplicated component" is a real question:

| Family | Declared in | Emitted by |
|---|---|---|
| `author-card` | book-note.css, knowledge-hub.css, people.css | people-setup.php |
| `breadcrumb` | book-note.css, components.css | 17 templates |
| `btn` | base.css, cards.css, policies.css | 10 templates |
| `page-container` | base.css, book-note.css, help.css | 16 templates |
| `policy-breadcrumb` | book-note.css, knowledge-hub.css, policies.css | 13 templates |
| `help-q`, `help-q-list` | help.css, people.css | 10 templates each |
| `help-hero`, `help-page`, `help-single`, `help-articles` | components.css + help.css (people.css for articles) | help and author templates |
| `ap-hero`, `ap-page` | components.css, people.css | template-author-profile.php |
| `pp-header`, `pp-page` | components.css, people.css | template-our-people.php |
| `tm-tab` | components.css, testimonials.css | page-testimonials.php |
| `product-section` | book-note.css, cards.css | page-cards.php, single-book_note.php |
| `is-open` | about.css, footer.css, header.css | page-about.php |

**The pattern in that list is worth naming and it is not random.** `breadcrumb`, `btn`, `page-container` and `policy-breadcrumb` are emitted by ten to seventeen templates each and declared in two or three stylesheets each. Those are site-wide furniture that has never been recorded as anything, and they are far more load bearing than most of the components that do have DSRD 8 sections. `author-card` is your S266 finding and it is a three-way split, which is the strongest case in the table for "duplicated rather than shared".

**And one that is the reverse.** `is-open`, `is-active`, `is-selected`, `is-playing`, `is-flat`, `is-collapsible`, `swapping`, `consumed`, `lit`, `pop`, `has-bg` are state classes, not components. They will look alarming in a raw list and they are almost certainly the utility disposition. Same for the `type-*` family (13 rows, all in base.css, all with no emitting template found), which is the text-style token layer.

## The class prefixes for your TO CONFIRM rows

This is the data `ANSWER__Check_4_Membership_Ruled_The_Component_Registry_S265.md` asked for. Read from the stylesheets this session, not from the S054 harvest.

| Registry row | Class prefixes, from the harvest | Declared in |
|---|---|---|
| Review card | `rv-card`, and the surrounding archive uses `rv-grid`, `rv-bar`, `rv-count`, `rv-more`, `rv-star`, `rv-stars` | reviews.css |
| Review archive | `rv-archive` | reviews.css |
| Filter bar / form controls | `ach-select` (confirmed), plus `facet-row`, `facet-rows` | components.css, about.css |
| Site-wide header | `site-header`, `site-nav`, `megamenu`, `megamenu-overlay`, `mobile-nav`, `navcard`, `nudge-card`, `btn-signin`, `skip-link` | header.css |
| Site-wide footer | `footer-inner`, `footer-main`, `footer-grid`, `footer-sub`, `footer-sub-inner`, `footer-logo`, `footer-logo-row`, `footer-ico`, `footer-socials`, `footer-policies`, `footer-copyright`, `footer-hairline`, `footer-cookie-settings`, `cta-card`, `cta-title`, `cta-subtitle`, `cta-overline` | footer.css |
| Closing enquiries panel | `warm-room` (the only family DSRD 8 already names for it) | about.css |
| Travelling book shelf panel | `tw-frame`, `tw-track`, `tw-window`, `tw-wrap`, `tw-heading`, `tw-lede` | about.css |

**One caution on the header and footer rows.** They are long because those are genuinely many flat families rather than one BEM family. If the registry wants one prefix per row, the honest answer is that the header and footer were built before the naming convention settled and their classes have no common prefix. That is a finding for Act 2, not something to paper over by inventing one.

## What I have not done, per the commission

**No disposition is judged.** Library, page-local or utility is Kain's ruling in Act 2. **Nothing is written into the registry**; the rows are yours to write after he rules.

## One thing already done that Act 4 will want

`page_gate` check 4 now reads `COMPONENT_REGISTRY.md` instead of harvesting class-shaped strings out of DSRD 8's prose. Both consequences you predicted invert, proved on seven cases in both directions: the global impact block passes because it is listed, and the section 12.1 page-local blocks stop passing. Rows still reading TO CONFIRM or NOT RECORDED print as a named INFO line rather than being guessed at; there are seven today, and the table above should close most of them.

One implementation note you will want for the registry's own wording: **an entry ending in a hyphen is treated as an open prefix.** `gi-` matches `.gi-block`; without that the gate looks for a class literally named "gi-", finds none, and fails the exact component your ruling said should now pass. That is the same shape of silent miss as the DSRD 8 harvest it replaces, and it is worth knowing that the registry's hyphen endings are load bearing.

*No em or en dashes in this file; checked before writing.*
