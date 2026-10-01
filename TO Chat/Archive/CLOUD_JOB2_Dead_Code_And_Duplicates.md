
# Achology theme: dead code and duplicates audit (read-only)

Repository state audited: commit `8556d96` (main). Nothing was changed, built, run or deployed. Scope: `*.css` in the repository root (22 files), and PHP/JS outside `previews/`, `tools/`, `harness/` (70 files). Root-level `*.py` checkers were not treated as theme output.

## Summary

| Part | List | Count |
|---|---|---|
| A | Distinct class names defined in the stylesheets | 1105 |
| A | List 1: DEAD classes | 34 |
| A | List 1b: referenced only by dead functions | 22 |
| A | List 2: possibly built dynamically | 35 |
| A | List 2b: owned by WordPress core or a plugin | 16 |
| B | DEAD functions | 3 |
| B | Dead JS functions / files / hooks | 0 / 0 / 0 |
| B | Possibly-dynamic groups listed in B.2 (bullets) | 8 |
| C | Identical-block groups (3+ declarations) | 88 |
| C | Near-identical pairs | 30 |
| C | Selectors defined in more than one stylesheet | 1 |
| D.1 | Stylesheet selectors named where-next | 0 (the panel is `.policy-next`: 1 base definition, 74 blocks in 6 files) |
| D.2 | Breadcrumb styles | 2 (`.breadcrumb` x 16 templates, `.ap-crumb` x 2) |

Method (all counts below were produced by scripts run over the checked-out files):
- CSS was parsed rule by rule (comments blanked, `@media`/`@supports` nesting tracked); class selectors were taken from selector text, ignoring attribute selectors. Line numbers are the line of the rule's selector start.
- "Literal reference" = the class name appears as a whole word (hyphen and underscore count as word characters) anywhere in PHP or JS, **including comments**. Comment-only mentions were then separated out.
- "Dynamic" = a line in PHP/JS that concatenates, interpolates or echoes a variable immediately after a class prefix ending in `-`, `--` or `__`. Each entry below quotes that line.
- Limits: classes that could arrive from database content, ACF fields, the block editor or a plugin cannot be seen in the repository; those are marked "cannot tell from the code" where they matter.

# Part A. Dead CSS classes

1105 distinct class names are defined across the stylesheets. 1028 have a literal reference in PHP/JS (counting comments). 77 have none; of those, 28 are explained by a dynamic pattern, 16 belong to WordPress core or the Complianz plugin, and the rest are in List 1. A further 8 classes have literal references only in comments, and 22 are referenced only inside functions that are themselves never called (List 1b).

## A.0 `.about-grid`

`.about-grid` is in **neither list by the stated rule** (it has a literal reference), but it is **effectively unreachable in the code as it stands**. Its only non-comment reference is the default value of a parameter: `shared-parts.php:617` `'modifiers' => 'policy-next--pair policy-next--bubble about-grid'` in `achology_routes_grid()`, joined into the section class at `shared-parts.php:644`. Every caller of `achology_routes_grid()` supplies its own `modifiers`, and none of the supplied values contains `about-grid`: `404.php:132` (empty string), `help-parts.php:159`, `page-about.php:195` (`policy-next--pair policy-next--bubble`), `template-policy.php:331` (empty string). Those four are the only callers found by grep. `achology_site_gateway()` (`shared-parts.php:1113`, called at `page-about.php:521`, `page-reviews.php:532`, `page-testimonials.php:223`) does not call `achology_routes_grid()`; it writes its own `.gateway` markup. No other PHP or JS line writes the string `about-grid` outside comments. Because `about-grid--page` (`shared-parts.php:650`) is only added when the shell already contains `about-grid`, that one is unreachable too. Comments at `page-about.php:187` and `shared-parts.php:646-648` still describe `about-grid` as active; the code does not match them. Defined at 54 places: `components.css` lines 768 to 990 and `testimonials.css:118`. Whether something outside the theme files (database content, a plugin) writes `about-grid` cannot be told from the code. Consequence: every rule in List 2 that sits under `.about-grid` (`.about-grid__lead`, `.about-grid__tall`, `.bg-*`, `.ic-*`) can only match if `about-grid` is output, so those rules share this status.

## A.1 List 1: DEAD (no PHP or JS reference of any kind, no plausible dynamic construction): 34 classes

Stylesheet:line `selector` for every occurrence. (`kh-article__meta` has a mention in a comment only, `single-book_note.php:921`.)

- `.ach-listen-bar__facts-sep`: components.css:1577 `.ach-listen-bar__facts-sep`
- `.bn-hero__author-link`: book-note.css:594 `.bn-hero__author-link`; book-note.css:602 `.bn-hero__author-link:hover`
- `.bn-hero__meta`: book-note.css:554 `.bn-hero__meta`
- `.btn--full-width`: base.css:881 `.btn--full-width`
- `.btn-ghost--dark`: base.css:861 `.btn-ghost--dark`
- `.btn-secondary--school`: base.css:788 `.btn-secondary--school`; base.css:794 `.btn-secondary--school:hover`
- `.card--course--corner-fade`: cards.css:2931 `.card--course--corner-fade .card__image-area::after`
- `.card--course--corner-lift`: cards.css:2926 `.card--course--corner-lift .card__hero-image`
- `.card--course--corner-shift`: cards.css:2922 `.card--course--corner-shift .card__hero-image`
- `.card--featured`: base.css:954 `.card-grid .card--featured`; base.css:959 `.card-grid .card--featured`
- `.card--mini`: cards.css:752 `.card--mini`; cards.css:760 `.card--mini:hover`; cards.css:766 `.card--mini.card--quote`; cards.css:771 `.card--mini .card__thumbnail`; cards.css:780 `.card--mini .card__thumbnail--article`; cards.css:784 `.card--mini .card__thumbnail--article img`; cards.css:792 `.card--mini .card__thumbnail--book-note`; cards.css:811 `.card--mini .card__thumbnail--book-note .book-cover`; cards.css:821 `.card--mini .card__thumbnail--quote`; cards.css:831 `.card--mini .card__thumbnail--workbook`; cards.css:836 `.card--mini .card__content`; cards.css:846 `.card--mini .card__type-label`; cards.css:850 `.card--mini .card__title`; cards.css:860 `.card--mini .card__watermark`
- `.card-grid--mini`: cards.css:2703 `.card-grid--mini`; cards.css:2710 `.card-grid--mini`; cards.css:2716 `.card-grid--mini`
- `.card__portrait`: cards.css:385 `.card--quote .card__portrait`; cards.css:711 `.card--featured-quote .card__portrait`
- `.card__thumbnail`: cards.css:771 `.card--mini .card__thumbnail`
- `.card__thumbnail--article`: cards.css:780 `.card--mini .card__thumbnail--article`; cards.css:784 `.card--mini .card__thumbnail--article img`
- `.card__thumbnail--book-note`: cards.css:792 `.card--mini .card__thumbnail--book-note`; cards.css:811 `.card--mini .card__thumbnail--book-note .book-cover`
- `.card__thumbnail--quote`: cards.css:821 `.card--mini .card__thumbnail--quote`
- `.card__thumbnail--workbook`: cards.css:831 `.card--mini .card__thumbnail--workbook`
- `.cards-sheet__treatment`: cards.css:2948 `.cards-sheet__treatment`; cards.css:2953 `.cards-sheet__treatment span`
- `.cards-sheet__variants`: cards.css:2958 `.cards-sheet__variants > * + *`
- `.help-popular__sep`: help.css:145 `.help-popular__sep`
- `.help-single__overline`: help.css:493 `.help-single__overline`
- `.kh-article__author`: knowledge-hub.css:559 `.kh-article__author`; knowledge-hub.css:565 `.kh-article__author:hover`
- `.kh-article__meta`: knowledge-hub.css:512 `.kh-article__meta`
- `.kh-article__meta--body`: book-note.css:1706 `.bn-body > .kh-article__meta--body`; knowledge-hub.css:4311 `.kh-article__meta--body`; knowledge-hub.css:4336 `.kh-article__meta--body + p`
- `.kh-article__meta-sep`: knowledge-hub.css:550 `.kh-article__meta-sep`
- `.kh-aside__btn-name`: knowledge-hub.css:2118 `.kh-aside .kh-aside__btn-name, .kh-aside__share .kh-aside__btn-name`; knowledge-hub.css:2118 `.kh-aside .kh-aside__btn-name, .kh-aside__share .kh-aside__btn-name`
- `.kh-aside__head-mark`: knowledge-hub.css:2392 `.kh-aside .kh-aside__head-mark`; knowledge-hub.css:2401 `.kh-aside .kh-aside__head-mark svg`
- `.policy-next--image`: components.css:390 `.policy-next--image`; components.css:398 `.policy-next--image::before`; components.css:404 `.policy-next--image > *`; components.css:409 `.policy-next--image .policy-next__title`; components.css:413 `.policy-next--image .policy-next__lead`
- `.product-section`: cards.css:2650 `.product-section`
- `.product-section__heading`: cards.css:2654 `.product-section__heading`
- `.qp-cardrow__meta`: quote.css:258 `.qp-cardrow p.qp-cardrow__meta`; quote.css:266 `.qp-cardrow__meta span + span::before`
- `.tm-lb__poster-play`: testimonials.css:100 `.tm-lb__poster-play`; testimonials.css:101 `.tm-lb__poster-play svg`
- `.tm-panel`: testimonials.css:65 `.tm-panel[hidden]`

## A.1b List 1b: referenced only inside functions that are never called: 22 classes

These have a literal reference, so they are not in List 1, but every reference sits inside a function that Part B lists as dead (`achology_article_promo_card()` for `kh-promo*`, `achology_pricing_pass()` for `pricing-pass__*`). They are dead unless that function is called some way the code does not show.

- `.kh-promo`: book-note.css:1145 `.bn-body > .kh-promo`; book-note.css:1664 `.bn-body > .kh-promo`; knowledge-hub.css:2613 `.kh-promo`; knowledge-hub.css:2687 `.kh-article__body > .kh-aside, .kh-article__body > .kh-promo`; (+20 more)
- `.kh-promo__arrow`: knowledge-hub.css:4075 `.kh-promo__arrow`; knowledge-hub.css:4170 `.kh-promo:hover .kh-promo__arrow`; knowledge-hub.css:4179 `.kh-promo, .kh-promo__bulb, .kh-promo__arrow, .kh-promo::after`
- `.kh-promo__body`: knowledge-hub.css:4048 `.kh-promo__body`
- `.kh-promo__bulb`: knowledge-hub.css:4088 `.kh-promo__bulb`; knowledge-hub.css:4103 `.kh-promo__bulb svg`; knowledge-hub.css:4168 `.kh-promo:hover .kh-promo__bulb`; knowledge-hub.css:4179 `.kh-promo, .kh-promo__bulb, .kh-promo__arrow, .kh-promo::after`
- `.kh-promo__cta`: knowledge-hub.css:4074 `.kh-promo__cta`
- `.kh-promo__inner`: knowledge-hub.css:4003 `.kh-promo__inner`
- `.kh-promo__mark`: knowledge-hub.css:4014 `.kh-promo__mark`
- `.pricing-pass__after`: pricing.css:340 `.pricing-pass__after`
- `.pricing-pass__anchor`: pricing.css:288 `.pricing-pass__anchor`
- `.pricing-pass__buy`: pricing.css:265 `.pricing-pass__buy`
- `.pricing-pass__cta`: pricing.css:321 `.pricing-pass__cta`; pricing.css:3247 `.pl .pricing-pass__cta`
- `.pricing-pass__desc`: pricing.css:226 `.pricing-pass__desc`
- `.pricing-pass__eyebrow`: pricing.css:188 `.pricing-pass__eyebrow`
- `.pricing-pass__facts`: pricing.css:235 `.pricing-pass__facts`; pricing.css:244 `.pricing-pass__facts li`; pricing.css:253 `.pricing-pass__facts svg`
- `.pricing-pass__guarantee`: pricing.css:326 `.pricing-pass__guarantee`; pricing.css:338 `.pricing-pass__guarantee svg`
- `.pricing-pass__list`: pricing.css:348 `.pricing-pass__list`; pricing.css:365 `.pricing-pass__list:hover`; pricing.css:366 `.pricing-pass__list svg`
- `.pricing-pass__name`: pricing.css:217 `.pricing-pass__name`
- `.pricing-pass__price`: pricing.css:279 `.pricing-pass__price`
- `.pricing-pass__save`: pricing.css:303 `.pricing-pass__save`
- `.pricing-pass__title`: pricing.css:204 `.pricing-pass__title`
- `.pricing-pass__unit`: pricing.css:314 `.pricing-pass__unit`
- `.pricing-pass__was`: pricing.css:295 `.pricing-pass__was`

## A.2 List 2: POSSIBLY BUILT DYNAMICALLY: 35 classes

No literal use in code (or comments only); the name fits a pattern the code builds at runtime. The builder line is quoted.

- `.about-grid__lead`: components.css:908 `.about-grid .about-grid__lead, .about-grid .about-grid__tall`; components.css:912 `.about-grid .about-grid__lead .policy-next__arrow, .about-grid .about-`; components.css:915 `.about-grid .about-grid__lead .policy-next__name, .about-grid .about-g`; (+9 more). Builder: `shared-parts.php:659`  `if ( $row['size'] ) { $class .= ' about-grid__' . $row['size']; }`. Evidence: value 'lead' is passed at shared-parts.php:1211.
- `.about-grid__tall`: components.css:908 `.about-grid .about-grid__lead, .about-grid .about-grid__tall`; components.css:912 `.about-grid .about-grid__lead .policy-next__arrow, .about-grid .about-`; components.css:915 `.about-grid .about-grid__lead .policy-next__name, .about-grid .about-g`; (+13 more). Builder: `shared-parts.php:659`  `if ( $row['size'] ) { $class .= ' about-grid__' . $row['size']; }`. Evidence: value 'tall' is passed at shared-parts.php:1272.
- `.bg-accred`: components.css:808 `.about-grid .bg-accred::after`. Builder: `shared-parts.php:669`  `if ( $row['bg'] ) { $class .= ' has-bg bg-' . $row['bg']; }`. Evidence: value 'accred' is passed at shared-parts.php:1315.
- `.bg-dimap`: components.css:816 `.about-grid .bg-dimap::after`. Builder: `shared-parts.php:669`  `if ( $row['bg'] ) { $class .= ' has-bg bg-' . $row['bg']; }`. Evidence: value 'dimap' is passed at shared-parts.php:1210.
- `.bg-hub`: components.css:809 `.about-grid .bg-hub::after`. Builder: `shared-parts.php:669`  `if ( $row['bg'] ) { $class .= ' has-bg bg-' . $row['bg']; }`. Evidence: value 'hub' is passed at shared-parts.php:1375.
- `.bg-schools`: components.css:807 `.about-grid .bg-schools::after`. Builder: `shared-parts.php:669`  `if ( $row['bg'] ) { $class .= ' has-bg bg-' . $row['bg']; }`. Evidence: value 'schools' is passed at shared-parts.php:1323.
- `.card--membership--annual`: cards.css:2293 `.card--membership--annual .card__header`; cards.css:2297 `.card--membership--annual .card__header::before`; cards.css:2311 `.card--membership--annual .card__header-title`; (+6 more). Builder: `commerce-cards.php:509`  `card--membership--<?php echo esc_attr( $tier ); ?>`. Evidence: $tier is 'monthly' or 'annual' (commerce-cards.php:474, 484, 493); the full class appears in PHP only in comments, never as a string literal in code.
- `.card--membership--monthly`: cards.css:2237 `.card--membership--monthly .card__header`; cards.css:2241 `.card--membership--monthly .card__header::before`; cards.css:2257 `.card--membership--monthly .card__header-title`; (+6 more). Builder: `commerce-cards.php:509`  `card--membership--<?php echo esc_attr( $tier ); ?>`. Evidence: $tier is 'monthly' or 'annual' (commerce-cards.php:474, 484, 493); the full class appears in PHP only in comments, never as a string literal in code.
- `.ic-tint`: components.css:858 `.about-grid .ic-tint .policy-next__icon`. Builder: `shared-parts.php:668`  `$class .= ' ic-' . $row['tone'];`. Evidence: 'tint' is the default tone (shared-parts.php:657).
- `.ic-orange`: components.css:859 `.about-grid .ic-orange .policy-next__icon`. Builder: `shared-parts.php:668`  `$class .= ' ic-' . $row['tone'];`. Evidence: 'tone' defaults to 'tint'; 'dark' is passed at shared-parts.php:1200; whether 'orange' and 'slate' are ever passed: cannot tell from the code.
- `.ic-slate`: components.css:860 `.about-grid .ic-slate .policy-next__icon`. Builder: `shared-parts.php:668`  `$class .= ' ic-' . $row['tone'];`. Evidence: 'tone' defaults to 'tint'; 'dark' is passed at shared-parts.php:1200; whether 'orange' and 'slate' are ever passed: cannot tell from the code.
- `.ic-dark`: components.css:861 `.about-grid .ic-dark .policy-next__icon`. Builder: `shared-parts.php:668`  `$class .= ' ic-' . $row['tone'];`. Evidence: 'tone' defaults to 'tint'; 'dark' is passed at shared-parts.php:1200; whether 'orange' and 'slate' are ever passed: cannot tell from the code.
- `.course-hero--1`: course.css:222 `.course-hero--1 .course-hero__inner`; course.css:231 `.course-hero--1 .course-hero__text`; course.css:235 `.course-hero--1 .course-hero__buy`; (+1 more). Builder: `course-parts.php:382`  `course-hero--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-hero--2`: course.css:248 `.course-hero--2 .course-hero__inner`; course.css:256 `.course-hero--2 .course-hero__art`; course.css:262 `.course-hero--2 .course-hero__art img`; (+11 more). Builder: `course-parts.php:382`  `course-hero--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-hero--3`: course.css:301 `.course-hero--3 .course-hero__buy`; course.css:309 `.course-hero--3 .course-hero__inner`; course.css:319 `.course-hero--3 .course-hero__text`; (+2 more). Builder: `course-parts.php:382`  `course-hero--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-optin--1`: course.css:393 `.course-optin--1 .course-optin__inner`. Builder: `course-parts.php:509`  `course-optin--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-optin--2`: course.css:402 `.course-optin--2 .course-optin__inner`. Builder: `course-parts.php:509`  `course-optin--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-optin--3`: course.css:412 `.course-optin--3 .course-optin__inner`. Builder: `course-parts.php:509`  `course-optin--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-curriculum--1`: course.css:549 `.course-curriculum--1 .course-curriculum__section:not(.is-open) .cours`. Builder: `course-parts.php:643`  `course-curriculum--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-curriculum--2`: course.css:561 `.course-curriculum--2 .course-curriculum__body`. Builder: `course-parts.php:643`  `course-curriculum--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-curriculum--3`: course.css:603 `.course-curriculum--3 .course-curriculum__section:not(.is-open)`; course.css:611 `.course-curriculum--3 .course-curriculum__heading`. Builder: `course-parts.php:643`  `course-curriculum--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-buybox--1`: course.css:881 `.course-buybox--1`; course.css:889 `.course-buybox--1 .course-buybox__inner`. Builder: `course-parts.php:975`  `course-buybox--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.course-buybox--2`: course.css:897 `.course-buybox--2`; course.css:907 `.course-buybox--2`; course.css:912 `.course-buybox--2 .course-buybox__inner`. Builder: `course-parts.php:975`  `course-buybox--<?php echo esc_attr( $option ); ?>`. Evidence: $option comes from achology_course_option() (course-parts.php:185), which returns a key of that decision's options array.
- `.gi__label--down`: global-impact.css:309 `.gi__label--down`; global-impact.css:484 `.gi__label, .gi__label--left, .gi__label--up, .gi__label--down`. Builder: `global-impact.php:216`  `gi__label--<?php echo esc_attr( $ach_gi_c[4] ); ?>`. Evidence: direction 'down' appears in the country rows of global-impact.php (lines 192-196 region).
- `.gi__label--left`: global-impact.css:301 `.gi__label--left`; global-impact.css:484 `.gi__label, .gi__label--left, .gi__label--up, .gi__label--down`. Builder: `global-impact.php:216`  `gi__label--<?php echo esc_attr( $ach_gi_c[4] ); ?>`. Evidence: direction 'left' appears in the country rows of global-impact.php (lines 192-196 region).
- `.gi__label--up`: global-impact.css:305 `.gi__label--up`; global-impact.css:484 `.gi__label, .gi__label--left, .gi__label--up, .gi__label--down`. Builder: `global-impact.php:216`  `gi__label--<?php echo esc_attr( $ach_gi_c[4] ); ?>`. Evidence: direction 'up' appears in the country rows of global-impact.php (lines 192-196 region).
- `.kh-aside__portrait--cover`: knowledge-hub.css:3418 `:is(.kh-article__body, .bn-body) > .kh-aside.is-past-hero .kh-aside__p`; knowledge-hub.css:3810 `.bn-body > .kh-aside .kh-aside__portrait--cover`; knowledge-hub.css:3815 `.bn-body > .kh-aside.is-past-hero .kh-aside__portrait--cover`. Builder: `knowledge-hub-parts.php:1125`  `' kh-aside__portrait--' . esc_attr( $ach_pic_kind )`. Evidence: $ach_pic_kind comes from $picture['kind']; 'kind' => 'cover' is set at single-quote.php:503.
- `.school--cbp`: components.css:24 `.school--cbp`. Builder: `commerce-cards.php:254`, `courses-setup.php:513`, `pricing-parts.php:912`, `commerce-cards.php:401`  `school--<?php echo esc_attr( $code ); ?>`. Evidence: code 'cbp' is a school code in commerce-cards.php:100-148 and courses-setup.php:48-66.
- `.school--lc`: components.css:25 `.school--lc`. Builder: `commerce-cards.php:254`, `courses-setup.php:513`, `pricing-parts.php:912`, `commerce-cards.php:401`  `school--<?php echo esc_attr( $code ); ?>`. Evidence: code 'lc' is a school code in commerce-cards.php:100-148 and courses-setup.php:48-66.
- `.school--mh`: components.css:28 `.school--mh`. Builder: `commerce-cards.php:254`, `courses-setup.php:513`, `pricing-parts.php:912`, `commerce-cards.php:401`  `school--<?php echo esc_attr( $code ); ?>`. Evidence: code 'mh' is a school code in commerce-cards.php:100-148 and courses-setup.php:48-66.
- `.school--miw`: components.css:27 `.school--miw`. Builder: `commerce-cards.php:254`, `courses-setup.php:513`, `pricing-parts.php:912`, `commerce-cards.php:401`  `school--<?php echo esc_attr( $code ); ?>`. Evidence: code 'miw' is a school code in commerce-cards.php:100-148 and courses-setup.php:48-66.
- `.school--nlp`: components.css:23 `.school--nlp`. Builder: `commerce-cards.php:254`, `courses-setup.php:513`, `pricing-parts.php:912`, `commerce-cards.php:401`  `school--<?php echo esc_attr( $code ); ?>`. Evidence: code 'nlp' is a school code in commerce-cards.php:100-148 and courses-setup.php:48-66.
- `.school--pc`: components.css:26 `.school--pc`. Builder: `commerce-cards.php:254`, `courses-setup.php:513`, `pricing-parts.php:912`, `commerce-cards.php:401`  `school--<?php echo esc_attr( $code ); ?>`. Evidence: code 'pc' is a school code in commerce-cards.php:100-148 and courses-setup.php:48-66.
- `.school--pgd`: components.css:29 `.school--pgd`. Builder: `commerce-cards.php:254`, `courses-setup.php:513`, `pricing-parts.php:912`, `commerce-cards.php:401`  `school--<?php echo esc_attr( $code ); ?>`. Evidence: code 'pgd' is a school code in commerce-cards.php:100-148 and courses-setup.php:48-66.
- `.single-quote`: quote.css:1241 `.single-quote .bn-hero > .page-container`; quote.css:1245 `.single-quote .bn-hero > .page-container > .breadcrumb-bar`; quote.css:1250 `.single-quote .bn-hero .bn-hero__grid`; (+5 more). Builder: `header.php:37`  `<body <?php body_class(); ?>>`. Evidence: WordPress adds the post-type class `single-quote` through body_class(); the theme never writes it as a string in code.

## A.2b List 2b: no literal reference, not built by theme code, owned by WordPress core or a plugin: 16 classes

The theme styles markup it does not emit. Whether the plugin still outputs these names cannot be told from the repository. `footer.php:136` emits a different Complianz class (`cmplz-manage-consent`), which is not in this list.

- `.admin-bar`: header.css:59 `body.admin-bar .site-header`; header.css:60 `body.admin-bar .megamenu`
- `.wp-smiley`: base.css:503 `img.emoji, img.wp-smiley`
- `.emoji`: base.css:503 `img.emoji, img.wp-smiley`
- `.achology-consent-bar`: footer.css:135 `.cmplz-cookiebanner.achology-consent-bar`; footer.css:162 `.cmplz-cookiebanner.achology-consent-bar::before`; footer.css:189 `.cmplz-cookiebanner.achology-consent-bar:hover::before`; (+29 more)
- `.cmplz-body`: footer.css:381 `.cmplz-cookiebanner.achology-consent-bar .cmplz-body, .cmplz-cookieban`; footer.css:398 `.cmplz-cookiebanner.achology-consent-bar .cmplz-body::before`
- `.cmplz-btn`: footer.css:441 `.cmplz-cookiebanner.achology-consent-bar .cmplz-btn`; footer.css:466 `.cmplz-cookiebanner.achology-consent-bar .cmplz-btn:hover, .cmplz-cook`; footer.css:466 `.cmplz-cookiebanner.achology-consent-bar .cmplz-btn:hover, .cmplz-cook`; (+1 more)
- `.cmplz-buttons`: footer.css:426 `.cmplz-cookiebanner.achology-consent-bar .cmplz-buttons`; footer.css:497 `.cmplz-cookiebanner.achology-consent-bar .cmplz-buttons`
- `.cmplz-cookiebanner`: footer.css:135 `.cmplz-cookiebanner.achology-consent-bar`; footer.css:162 `.cmplz-cookiebanner.achology-consent-bar::before`; footer.css:189 `.cmplz-cookiebanner.achology-consent-bar:hover::before`; (+29 more)
- `.cmplz-divider`: footer.css:421 `.cmplz-cookiebanner.achology-consent-bar .cmplz-divider, .cmplz-cookie`
- `.cmplz-documents`: footer.css:421 `.cmplz-cookiebanner.achology-consent-bar .cmplz-divider, .cmplz-cookie`
- `.cmplz-header`: footer.css:271 `.cmplz-cookiebanner.achology-consent-bar .cmplz-header`
- `.cmplz-link`: footer.css:477 `.cmplz-cookiebanner.achology-consent-bar .cmplz-links a, .cmplz-cookie`
- `.cmplz-links`: footer.css:421 `.cmplz-cookiebanner.achology-consent-bar .cmplz-divider, .cmplz-cookie`; footer.css:477 `.cmplz-cookiebanner.achology-consent-bar .cmplz-links a, .cmplz-cookie`; footer.css:484 `.cmplz-cookiebanner.achology-consent-bar .cmplz-links a:hover`
- `.cmplz-logo`: footer.css:278 `.cmplz-cookiebanner.achology-consent-bar .cmplz-logo`
- `.cmplz-message`: footer.css:381 `.cmplz-cookiebanner.achology-consent-bar .cmplz-body, .cmplz-cookieban`; footer.css:408 `.cmplz-cookiebanner.achology-consent-bar .cmplz-message`
- `.cmplz-title`: footer.css:261 `.cmplz-cookiebanner.achology-consent-bar .cmplz-title, .cmplz-cookieba`; footer.css:261 `.cmplz-cookiebanner.achology-consent-bar .cmplz-title, .cmplz-cookieba`; footer.css:280 `.cmplz-cookiebanner.achology-consent-bar .cmplz-title`; (+1 more)

# Part B. Dead PHP and JavaScript

411 function definitions were found (PHP `function`, JS `function` and arrow/function assigned to `const`/`let`/`var`). For each, every whole-word occurrence outside its own definition line was counted across all PHP and JS. 91 `add_action`/`add_filter` lines exist in the theme PHP; 87 register a named string callback, and 0 of those name a function that is not defined in the theme (none).

## B.1 DEAD (defined, never called, included or registered)

| Function | Defined | Evidence |
|---|---|---|
| `achology_article_promo_card()` | `knowledge-hub-parts.php:2227` | No occurrence anywhere else in PHP, JS, README or the root checker scripts (searched with grep). Its output carries the `kh-promo*` classes (List 1b). |
| `achology_pricing_pass()` | `pricing-parts.php:258` | No occurrence anywhere else. Its output carries the `pricing-pass__*` classes (List 1b). |
| `achology_heading_dividers()` | `knowledge-hub-parts.php:873` | Only mentioned in comments: `single-book_note.php:208`, `single-book_note.php:1044`, `single-faq_article.php:479`. No call. |

No JavaScript function, template part, PHP file, stylesheet or script file is dead: every JS function has at least one non-definition reference in its file (call or listener registration), every root `*.css` and `*.js` is enqueued (`functions.php:599-895`, or via `achology_enqueue_component_style()` for `global-impact`, `warm-room`, `help`, `knowledge-hub`), and every `require` in `functions.php` points at an existing file. Functions whose only callers are other dead functions were not chased through a full call graph: cannot tell from the code beyond the three above.

## B.2 POSSIBLY USED DYNAMICALLY (not dead)

- WordPress template files, used by filename or `Template Name` header, never dead: `404.php`, `archive-faq_article.php`, `footer.php`, `header.php`, `index.php`, `page-about.php`, `page-cards.php`, `page-pricing.php`, `page-reviews.php`, `page-testimonials.php`, `single-article.php`, `single-book_note.php`, `single-faq_article.php`, `single-quote.php`, `taxonomy-faq_category.php`, `taxonomy-kh_category.php`, `template-author-profile.php`, `template-course.php`, `template-courses.php`, `template-our-people.php`, `template-policies-index.php`, `template-policy.php`. `template-course.php` has no `Template Name` header; it is loaded by `locate_template()` at `functions.php:540`. Which pages are assigned to the `Template Name` templates is stored in the database: cannot tell from the code.
- `learn-listing.php`: loaded by `locate_template( 'learn-listing.php' )` at `knowledge-hub-setup.php:640`.
- `card-review.php`: `require`d at `page-cards.php:63` (only for `/cards/?view=review`).
- `reviews-import.php`: `require`d at `functions.php:144` only when `is_admin()`.
- `policies-content/*.php` (12 files): included by a variable path built from the page slug (`template-policy.php:138-141`, `include $ach_partial;`). `policies-content/policies.php` says in its own header it is read only by `rank-math-feed.php`, not rendered.
- `data/reviews.csv.php`: path built at `reviews-import.php:103-109`. `data/courses.json`: `course-parts.php:351`. `data/lectures/{slug}.json`: path built at `course-parts.php:85` from a slug; all 28 lecture files match a slug in `courses-setup.php` or `data/courses.json`. `data/student-countries.json`: no literal reference found in PHP or JS; cannot tell from the code whether something outside the theme reads it.
- `acf-json/*.json` (6 files): ACF reads this folder by convention; no PHP reference to it. Cannot tell from the code.
- All 87 string-named hook callbacks are used by WordPress through their hook names (for example `achology_enqueue_assets` on `wp_enqueue_scripts`); they are not dead. Four hooks use closures (`media-library.php:522, 526, 1040, 1044`).

# Part C. Duplicated rule blocks

2598 rule blocks were parsed (those with `@font-face`/`@keyframes` skipped). Declarations were lower-cased, whitespace-normalised and compared as sets, within the same `@media`/`@supports` context. Groups below need at least 3 declarations. Size = declarations per block multiplied by number of blocks.

Totals: 88 groups of identical blocks (3+ declarations); 30 near-identical pairs (80% or more shared declarations, 5+ declarations, same context); 1 selector defined in more than one stylesheet.

## C.1 Ten largest identical groups

**C.1.1** 3 declarations x 12 blocks = 36; files: about.css, cards.css, components.css, help.css, people.css, policies.css, reviews.css, testimonials.css, warm-room.css

Declarations: `border-top: 1px solid var(--color-hairline); margin-top: var(--sp-2xl); padding-top: var(--sp-2xl)`

- `about.css:822` `.policy-related`
- `cards.css:3028` `.cards-sheet__family + .cards-sheet__family`
- `cards.css:3160` `.card-review__open`
- `components.css:1159` `.policy-body--ruled + .policy-body--ruled`
- `components.css:1172` `.policy-body--ruled .about-proof__note + h2`
- `help.css:154` `.page-container > .help-popular`
- `people.css:638` `.pp-group`
- `policies.css:413` `.policy-body--ruled p + h2, .policy-body--ruled ul + h2, .policy-body--ruled ol + h2, .pol`
- `policies.css:1126` `.policy-body--ruled .policy-aristotle`
- `reviews.css:74` `.rv-archive + .policy-body--ruled`
- `testimonials.css:126` `.tm-about-proof`
- `warm-room.css:48` `.policy-closing`

Reading: Different files, different components with the same values. The selectors differ and do not overlap, so these are not overrides of one another: the same values are written independently in several places. Whether that is deliberate or accidental cannot be told from the code.

**C.1.2** 4 declarations x 8 blocks = 32; files: cards.css, components.css, knowledge-hub.css, people.css

Declarations: `display: block; height: 100%; object-fit: cover; width: 100%`

- `cards.css:239` `.card--article .card__banner img`
- `cards.css:570` `.card--featured-article .card__image-area img, .card--featured-workbook .card__image-area `
- `cards.css:784` `.card--mini .card__thumbnail--article img`
- `components.css:682` `.proof-card img`
- `knowledge-hub.css:1195` `.kh-source-book__cover img`
- `people.css:72` `.ap-avatar img`
- `people.css:672` `.pp-card__avatar img`
- `people.css:1011` `.author-card__avatar img`

Reading: Different files, different components with the same values. The selectors differ and do not overlap, so these are not overrides of one another: the same values are written independently in several places. Whether that is deliberate or accidental cannot be told from the code.

**C.1.3** 3 declarations x 8 blocks = 24; files: about.css, global-impact.css, knowledge-hub.css, people.css, policies.css, reviews.css

Declarations: `display: block; height: auto; width: 100%`

- `about.css:91` `.st-svg`
- `about.css:157` `.about-header__art`
- `about.css:632` `.policy-header--portrait .policy-doc img`
- `global-impact.css:261` `.gi__map-img`
- `knowledge-hub.css:4493` `.kh-foot__kyp .kh-aside__course-mark`
- `people.css:465` `.pp-header__art`
- `policies.css:899` `.policy-doc__thumb`
- `reviews.css:40` `.reviews-header__art`

Reading: Different files, different components with the same values. The selectors differ and do not overlap, so these are not overrides of one another: the same values are written independently in several places. Whether that is deliberate or accidental cannot be told from the code.

**C.1.4** 6 declarations x 4 blocks = 24; files: global-impact.css, help.css, knowledge-hub.css, pricing.css

Declarations: `color: var(--color-dark); font-family: var(--font-heading); font-size: var(--text-24); font-weight: 600; line-height: 1.25; margin: 0`

- `global-impact.css:115` `.gi-intro__title`
- `help.css:178` `.help-popular__heading`
- `knowledge-hub.css:1033` `.kh-section__title`
- `pricing.css:122` `.pricing-section__title`

Reading: Different files, different components with the same values. The selectors differ and do not overlap, so these are not overrides of one another: the same values are written independently in several places. Whether that is deliberate or accidental cannot be told from the code.

**C.1.5** 7 declarations x 3 blocks = 21; files: cards.css, reviews.css

Declarations: `background: var(--color-white); border-radius: var(--radius-card); box-shadow: var(--shadow-card); display: flex; flex-direction: column; overflow: hidden; transition: box-shadow 0.2s ease, transform 0.2s ease`

- `cards.css:12` `.card`
- `cards.css:873` `.card-product`
- `reviews.css:725` `.rv-card`

Reading: Different files, different components with the same values. The selectors differ and do not overlap, so these are not overrides of one another: the same values are written independently in several places. Whether that is deliberate or accidental cannot be told from the code.

**C.1.6** 7 declarations x 3 blocks = 21; files: cards.css

Declarations: `align-items: center; color: var(--color-soft-grey); display: flex; font-family: var(--font-body); font-size: var(--text-12); font-weight: 400; gap: 5px`

- `cards.css:1603` `.card--bundle .card__stat`
- `cards.css:1994` `.card--aaa .card__stat`
- `cards.css:2400` `.card--membership .card__stat`

Reading: Parallel per-variant rules (bundle/aaa/membership/course) inside one file. Looks like deliberate per-variant repetition; whether it is intended or merely never consolidated cannot be told from the code.

**C.1.7** 10 declarations x 2 blocks = 20; files: about.css, people.css; context `@media (max-width: 599.98px)`

Declarations: `align-items: center; display: flex; inset: 0; justify-content: center; margin: 0; max-width: none; pointer-events: none; position: absolute; width: 100%; z-index: 0`

- `about.css:368` `.policy-page--about .policy-header--doc .policy-doc, .policy-header--portrait .policy-doc`
- `people.css:440` `.pp-header__doc`

Reading: Different files, different components with the same values. The selectors differ and do not overlap, so these are not overrides of one another: the same values are written independently in several places. Whether that is deliberate or accidental cannot be told from the code.

**C.1.8** 10 declarations x 2 blocks = 20; files: cards.css

Declarations: `-webkit-box-orient: vertical; -webkit-line-clamp: 3; color: var(--color-soft-grey); display: -webkit-box; font-family: var(--font-body); font-size: var(--text-14); font-weight: 400; overflow: hidden; position: relative; z-index: 2`

- `cards.css:119` `.card__excerpt`
- `cards.css:138` `.card__subtitle`

Reading: Same file, different selectors. Looks like repeated typography/layout values; deliberate or accidental cannot be told from the code.

**C.1.9** 10 declarations x 2 blocks = 20; files: cards.css

Declarations: `height: 100%; object-fit: cover; object-position: top right; opacity: 0.12; pointer-events: none; position: absolute; right: 0; top: 0; width: auto; z-index: 1`

- `cards.css:385` `.card--quote .card__portrait`
- `cards.css:711` `.card--featured-quote .card__portrait`

Reading: Parallel per-variant rules (bundle/aaa/membership/course) inside one file. Looks like deliberate per-variant repetition; whether it is intended or merely never consolidated cannot be told from the code.

**C.1.10** 10 declarations x 2 blocks = 20; files: cards.css

Declarations: `align-items: center; background: var(--school-accent, var(--color-orange)); border-radius: 50%; display: flex; flex-shrink: 0; height: 16px; justify-content: center; margin-top: 1px; opacity: 0.12; width: 16px`

- `cards.css:1644` `.card--bundle .card__tick-circle`
- `cards.css:2036` `.card--aaa .card__tick-circle`

Reading: Parallel per-variant rules (bundle/aaa/membership/course) inside one file. Looks like deliberate per-variant repetition; whether it is intended or merely never consolidated cannot be told from the code.

## C.2 Other identical groups (11 onward), one line each

- C.2.11: 5 decls x 4: `components.css:495`; `help.css:115`; `help.css:328`; `help.css:1357` first selector `.policy-next__desc`
- C.2.12: 6 decls x 3: `cards.css:1585`; `cards.css:1974`; `cards.css:2379` first selector `.card--bundle .card__school-name`
- C.2.13: 9 decls x 2: `cards.css:1948`; `cards.css:2352` first selector `.card--aaa .card__academy-line`
- C.2.14: 6 decls x 3: `people.css:559`; `testimonials.css:40`; `testimonials.css:119` first selector `.pp-group__label`
- C.2.15: 6 decls x 3: `policies.css:305`; `policies.css:353`; `policies.css:478` first selector `.policy-body a`
- C.2.16: 4 decls x 4: `cards.css:1337`; `cards.css:1622`; `cards.css:2004`; `cards.css:2410` first selector `.card--course .card__stat .icon-stat`
- C.2.17: 8 decls x 2: `cards.css:1804`; `cards.css:2165` first selector `.card--bundle .card__save-badge`
- C.2.18: 8 decls x 2: `cards.css:2110`; `cards.css:2503` first selector `.card--aaa .card__summary-strip .strip-tick`
- C.2.19: 3 decls x 5: `book-note.css:761`; `cards.css:3135`; `components.css:1053`; `course.css:592`; `pricing.css:771` first selector `.kh-aside__offer .bn-btn--fill`
- C.2.20: 5 decls x 3: `cards.css:1595`; `cards.css:1983`; `cards.css:2389` first selector `.card--bundle .card__stats`
- C.2.21: 5 decls x 3: `cards.css:1630`; `cards.css:2012`; `cards.css:2418` first selector `.card--bundle .card__checklist`
- C.2.22: 5 decls x 3: `cards.css:1665`; `cards.css:2056`; `cards.css:2455` first selector `.card--bundle .card__course-name`
- C.2.23: 5 decls x 3: `components.css:707`; `course.css:347`; `testimonials.css:98` first selector `.about-video-lightbox__panel iframe, .shared-video`
- C.2.24: 7 decls x 2: `book-note.css:411`; `knowledge-hub.css:307` first selector `.bn-hero__overline`
- C.2.25: 7 decls x 2: `cards.css:1831`; `cards.css:2188` first selector `.card--bundle .card__guarantee-pill`
- C.2.26: 7 decls x 2: `cards.css:1960`; `cards.css:2364` first selector `.card--aaa .card__academy-line .icon-school`
- C.2.27: 7 decls x 2: `help.css:674`; `policies.css:259` first selector `.help-single__body h3`
- C.2.28: 7 decls x 2: `knowledge-hub.css:1327`; `knowledge-hub.css:1452` first selector `.kh-hub__intro`
- C.2.29: 4 decls x 3: `cards.css:1526`; `cards.css:1930`; `cards.css:2338` first selector `.card--bundle .card__info`
- C.2.30: 4 decls x 3: `cards.css:1768`; `cards.css:2147`; `cards.css:2578` first selector `.card--bundle .card__price`
- C.2.31: 6 decls x 2: `components.css:1039`; `global-impact.css:333` first selector `.gateway .gateway__title`
- C.2.32: 3 decls x 4: `header.css:299`; `help.css:321`; `help.css:1344`; `knowledge-hub.css:1023` first selector `.navcard__text`
- C.2.33: 6 decls x 2: `help.css:322`; `help.css:1346` first selector `.help-q__title`
- C.2.34: 6 decls x 2: `people.css:79`; `people.css:530` first selector `.ap-name`
- C.2.35: 5 decls x 2: `about.css:303`; `about.css:489` first selector `.story-proof__label`
- C.2.36: 5 decls x 2: `book-note.css:645`; `knowledge-hub.css:356` first selector `.bn-hero__lead`
- C.2.37: 5 decls x 2: `cards.css:1101`; `cards.css:1510` first selector `.card--course .card__hero-image`
- C.2.38: 5 decls x 2: `cards.css:1795`; `cards.css:2156` first selector `.card--bundle .card__anchor-price`
- C.2.39: 5 decls x 2: `components.css:504`; `policies.css:662` first selector `.policy-next__arrow`
- C.2.40: 5 decls x 2: `course.css:402`; `pricing.css:2118` first selector `.course-optin--2 .course-optin__inner`
- C.2.41: 5 decls x 2: `help.css:747`; `knowledge-hub.css:773` first selector `.help-single__body a`
- C.2.42: 5 decls x 2: `people.css:329`; `policies.css:153` first selector `.pp-header`
- C.2.43: 5 decls x 2: `pricing.css:2608`; `pricing.css:2825` first selector `.pl-guarantees`
- C.2.44: 3 decls x 3: `about.css:385`; `cards.css:3004`; `knowledge-hub.css:1359` first selector `.tw-wrap`
- C.2.45: 3 decls x 3: `base.css:935`; `course.css:644`; `knowledge-hub.css:1375` first selector `.card-grid`
- C.2.46: 3 decls x 3: `book-note.css:1229`; `help.css:666`; `knowledge-hub.css:620` first selector `.bn-body > h2`
- C.2.47: 3 decls x 3: `cards.css:187`; `cards.css:207`; `global-impact.css:147` first selector `a.card__footer-cta:focus-visible`
- C.2.48: 3 decls x 3: `cards.css:1638`; `cards.css:2020`; `cards.css:2426` first selector `.card--bundle .card__checklist-item`
- C.2.49: 3 decls x 3: `cards.css:1762`; `cards.css:2141`; `cards.css:2572` first selector `.card--bundle .card__price-row`
- C.2.50: 3 decls x 3: `cards.css:1850`; `cards.css:2207`; `cards.css:2637` first selector `.card--bundle .card__ctas`
- C.2.51: 3 decls x 3: `cards.css:2121`; `cards.css:2449`; `cards.css:2514` first selector `.card--aaa .card__summary-strip .strip-tick svg`
- C.2.52: 3 decls x 3: `knowledge-hub.css:146`; `people.css:40`; `people.css:323` first selector `.kh-article__band > .page-container > *`
- C.2.53: 4 decls x 2: `about.css:372`; `people.css:452` first selector `.policy-page--about .policy-header--doc .policy-do`
- C.2.54: 4 decls x 2: `cards.css:1061`; `cards.css:1482` first selector `.card--course .card__image-gradient`
- C.2.55: 4 decls x 2: `cards.css:1658`; `cards.css:2049` first selector `.card--bundle .card__tick-circle svg`
- C.2.56: 4 decls x 2: `help.css:87`; `people.css:211` first selector `.help-group__label::after`
- C.2.57: 4 decls x 2: `help.css:384`; `help.css:390` first selector `.help-articles__empty`
- C.2.58: 4 decls x 2: `knowledge-hub.css:4844`; `quote.css:1208` first selector `.bn-author-portrait__credit a`
- C.2.59: 4 decls x 2: `people.css:24`; `people.css:266` first selector `.ap-page`
- C.2.60: 4 decls x 2: `pricing.css:932`; `pricing.css:971` first selector `.pricing-bundle__courses a`
- C.2.61: 3 decls x 2: `about.css:45`; `about.css:46` first selector `.xr`
- C.2.62: 3 decls x 2: `about.css:367`; `people.css:439` first selector `.policy-page--about .policy-header--doc .policy-he`
- C.2.63: 3 decls x 2: `base.css:917`; `help.css:177` first selector `.icon-section-header`
- C.2.64: 3 decls x 2: `base.css:1073`; `knowledge-hub.css:1347` first selector `.pagination-pill--active`
- C.2.65: 3 decls x 2: `book-note.css:1664`; `knowledge-hub.css:3951` first selector `.bn-body > .kh-promo`
- C.2.66: 3 decls x 2: `book-note.css:1771`; `knowledge-hub.css:2784` first selector `.bn-page > .page-container > .kh-foot__signature, `
- C.2.67: 3 decls x 2: `cards.css:233`; `cards.css:469` first selector `.card--article .card__banner`
- C.2.68: 3 decls x 2: `cards.css:366`; `cards.css:579` first selector `.card--book-note--horizontal .card__right`
- C.2.69: 3 decls x 2: `cards.css:522`; `cards.css:661` first selector `.card--workbook .card__footer-cta`
- C.2.70: 3 decls x 2: `cards.css:528`; `cards.css:667` first selector `.card--workbook .card__footer-cta svg`
- C.2.71: 3 decls x 2: `cards.css:1110`; `cards.css:1519` first selector `.card--course .card__accent-bar`
- C.2.72: 3 decls x 2: `cards.css:1886`; `cards.css:2230` first selector `.card--aaa .card__header-content`
- C.2.73: 3 decls x 2: `cards.css:2703`; `components.css:1021` first selector `.card-grid--mini`
- C.2.74: 3 decls x 2: `components.css:455`; `policies.css:539` first selector `.policy-next__row:hover`
- C.2.75: 3 decls x 2: `components.css:1567`; `pricing.css:1190` first selector `.ach-listen-bar__facts > * + *::before`
- C.2.76: 3 decls x 2: `components.css:1692`; `pricing.css:4302` first selector `.ach-listen__btn:hover, .ach-listen__btn:focus-vis`
- C.2.77: 3 decls x 2: `course.css:188`; `course.css:385` first selector `.course-hero__reassure`
- C.2.78: 3 decls x 2: `courses-directory.css:167`; `reviews.css:699` first selector `.cd-more-wrap`
- C.2.79: 3 decls x 2: `footer.css:39`; `quote.css:1112` first selector `.footer-invite__arrow svg`
- C.2.80: 3 decls x 2: `footer.css:516`; `knowledge-hub.css:4272` first selector `.footer-brand`
- C.2.81: 3 decls x 2: `help.css:738`; `policies.css:284` first selector `.help-single__body ul, .help-single__body ol`
- C.2.82: 3 decls x 2: `help.css:744`; `policies.css:291` first selector `.help-single__body li`
- C.2.83: 3 decls x 2: `knowledge-hub.css:1392`; `knowledge-hub.css:1465` first selector `.kh-tags`
- C.2.84: 3 decls x 2: `knowledge-hub.css:4256`; `reviews.css:1258` first selector `.kh-foot-way:focus-visible`
- C.2.85: 3 decls x 2: `policies.css:642`; `policies.css:645` first selector `.policy-index__row[data-word="terms"]::before`
- C.2.86: 3 decls x 2: `policies.css:646`; `policies.css:649` first selector `.policy-index__row[data-word="disclaimers"]::befor`
- C.2.87: 3 decls x 2: `policies.css:1224`; `policies.css:1252` first selector `.policy-body .help-popular`
- C.2.88: 3 decls x 2: `pricing.css:1945`; `pricing.css:2078` first selector `.pricing-bundle__headlink:hover .pricing-bundle__n`

## C.3 Near-identical pairs (80% or more declarations shared)

| A | B | only in A | only in B |
|---|---|---|---|
| `about.css:124` `.cons-count__num` | `about.css:298` `.story-proof__num` | font-size: var(--text-42) | font-size: var(--text-33) |
| `base.css:648` `.kh-section__subtext, .help-popular__head .kh` | `reviews.css:1291` `.rv-card__translation-text` | none | overflow-wrap: anywhere |
| `base.css:1017` `.visually-hidden` | `components.css:1731` `.sr-only` | clip: rect(0, 0, 0, 0) | clip: rect(0 0 0 0) |
| `book-note.css:1235` `.bn-body h2` | `knowledge-hub.css:589` `.kh-article__body h2` | scroll-margin-top: calc(72px + var(--sp-lg)) | none |
| `cards.css:199` `a.card__footer-info` | `components.css:102` `.breadcrumb__link` | none | transition: color 0.15s ease |
| `cards.css:1326` `.card--course .card__stat` | `cards.css:1603` `.card--bundle .card__stat` | white-space: nowrap | none |
| `cards.css:1326` `.card--course .card__stat` | `cards.css:1994` `.card--aaa .card__stat` | white-space: nowrap | none |
| `cards.css:1326` `.card--course .card__stat` | `cards.css:2400` `.card--membership .card__stat` | white-space: nowrap | none |
| `cards.css:1367` `.card--course .card__price-qualifier` | `reviews.css:921` `.rv-card__date` | margin-left: 5px | none |
| `cards.css:1862` `.card--aaa .card__header` | `cards.css:2220` `.card--membership .card__header` | background: linear-gradient(to top, var(--color-dark), #5a6d78) | none |
| `cards.css:1905` `.card--aaa .card__header-title` | `cards.css:2311` `.card--membership--annual .card__header-title` | letter-spacing: 0.02em | none |
| `cards.css:2097` `.card--aaa .card__summary-strip` | `cards.css:2491` `.card--membership .card__summary-strip` | background: rgba(53, 65, 73, 0.08) | none |
| `components.css:443` `.policy-next__row` | `policies.css:527` `.policy-index__row` | padding: var(--sp-md) var(--sp-lg) | padding: var(--sp-lg) |
| `components.css:495` `.policy-next__desc` | `quote.css:258` `.qp-cardrow p.qp-cardrow__meta` | none | margin: 0 |
| `course.css:51` `.course-block__title` | `help.css:62` `.help-hero__title` | none | font-weight: 700 |
| `courses-directory.css:89` `.cd-ticks input` | `reviews.css:388` `.ach-select__native` | margin: 0 | none |
| `help.css:82` `.help-group__label` | `people.css:206` `.ap-works__label` | color: var(--color-soft-grey) | color: var(--color-mid-grey) |
| `help.css:110` `.help-cat__name` | `people.css:679` `.pp-card__name` | none | display: block |
| `help.css:115` `.help-cat__desc` | `quote.css:258` `.qp-cardrow p.qp-cardrow__meta` | none | margin: 0 |
| `help.css:303` `.help-q-list` | `people.css:647` `.pp-grid` | none | row-gap: 8px |
| `help.css:328` `.help-q__excerpt` | `quote.css:258` `.qp-cardrow p.qp-cardrow__meta` | none | margin: 0 |
| `help.css:747` `.help-single__body a` | `policies.css:305` `.policy-body a` | none | transition: text-decoration-color 0.15s ease |
| `help.css:747` `.help-single__body a` | `policies.css:353` `.policy-header__copy a` | none | transition: text-decoration-color 0.15s ease |
| `help.css:747` `.help-single__body a` | `policies.css:478` `.policy-endnote a` | none | transition: text-decoration-color 0.15s ease |
| `help.css:1357` `.help-close__route-desc` | `quote.css:258` `.qp-cardrow p.qp-cardrow__meta` | none | margin: 0 |
| `knowledge-hub.css:773` `.kh-article__body a` | `policies.css:305` `.policy-body a` | none | transition: text-decoration-color 0.15s ease |
| `knowledge-hub.css:773` `.kh-article__body a` | `policies.css:353` `.policy-header__copy a` | none | transition: text-decoration-color 0.15s ease |
| `knowledge-hub.css:773` `.kh-article__body a` | `policies.css:478` `.policy-endnote a` | none | transition: text-decoration-color 0.15s ease |
| `knowledge-hub.css:4573` `.bn-author-portrait img` | `quote.css:1135` `.qp-hero-face img` | none | object-position: center 30% |
| `pricing.css:753` `.pricing-tab` | `pricing.css:1767` `.pricing-plan` | gap: var(--sp-xs) | justify-content: center |

Reading: the `.visually-hidden` (base.css:1017) and `.sr-only` (components.css:1731) pair differ only in `clip: rect(0, 0, 0, 0)` against `clip: rect(0 0 0 0)`, which are the same value written two ways; that one looks like an accidental copy. The `.card--*  .card__stat` / `.header` / `.summary-strip` pairs inside `cards.css` are per-variant rules. The `transition: text-decoration-color` and `margin: 0` single-declaration differences are small enough that whether they are deliberate cannot be told from the code.

## C.4 Same selector in more than one stylesheet, differing declarations

Exactly one selector (same text, same media context) is defined in two stylesheets: `.policy-body--ruled + .policy-body--ruled`.

| File:line | Context | Declarations |
|---|---|---|
| `components.css:1159` | none | `border-top: 1px solid var(--color-hairline); margin-top: var(--sp-2xl); padding-top: var(--sp-2xl)` |
| `components.css:1167` | @media (max-width: 767px) | `margin-top: var(--sp-xl); padding-top: var(--sp-xl)` |
| `testimonials.css:127` | none | `margin-top: var(--sp-2xl); padding-top: var(--sp-2xl)` |

Reading: `components.css:1159` carries `border-top`; `testimonials.css:127` repeats the same selector with only `margin-top` and `padding-top` (the same values as components.css). Their `@media (max-width: 767px)` forms are `components.css:1167` and `testimonials.css:128-131`. Because the comment at `components.css:1155-1158` says the shared separator serves Policies index, About and Testimonials, and the testimonials copy adds nothing, it looks like an accidental copy; the code does not say why it was repeated.

# Part D. Two named questions

## D.1 The Where Next panel

**Finding: the premise of "about five copies" does not hold in the code.** No stylesheet selector contains `where-next` or `wherenext`. The panel is the `.policy-next` component. It has exactly one base definition, `components.css` section 4 (`components.css:355` heading, rules at 368 to 621), described there as moved verbatim from `policies.css` section 9 (S219). The only text left in `policies.css` is a comment (`policies.css:1239`). The other places are overrides or variants of that one definition, not copies. They are listed here, then the nearest thing to a true copy (the `.policy-index` rows) is compared line by line.

### D.1.1 Every place `.policy-next` is styled

| File | Rule blocks | Lines | Role |
|---|---|---|---|
| `about.css` | 1 | 197 | one margin override |
| `book-note.css` | 1 | 1469 | one margin override |
| `components.css` | 64 | 368, 390, 398, 404, 409, 413, 418, 427, 435, 443, 455, 462, 474, 479, 486, 495, 504, 512, 517, 531, 535, 546, 552, 556, 560, 568, 572, 578, 583, 587, 597, 602, 609, 621, 768, 770, 771, 772, 773, 774, 775, 787, 792, 806, 840, 854, 858, 859, 860, 861, 903, 905, 912, 915, 917, 924, 926, 930, 939, 941, 990, 991, 1041, 1170 | base definition (368-621), `about-grid` variant (768-990), page overrides (1041, 1170) |
| `footer.css` | 1 | 63 | accent-word colour only |
| `help.css` | 6 | 418, 433, 438, 452, 460, 462 | `--bubble` / `--no-mark` variant (watermark) |
| `knowledge-hub.css` | 1 | 885 | one margin override |

### D.1.2 Declaration by declaration: base against every override outside `components.css`

Base `.policy-next` (`components.css:368`): `margin-top: var(--sp-3xl); padding: var(--sp-xl); background: var(--color-off-white); border-radius: var(--radius-card)`

| Location | Selector | Declarations | Relation to base |
|---|---|---|---|
| `components.css:583` | `.policy-next` (@media (max-width: 767px)) | `padding: var(--sp-lg)` | overrides `padding` under 768px |
| `components.css:621` | `.policy-page--404 .policy-next`  | `margin-top: 0` | overrides `margin-top` to 0 on the 404 page |
| `components.css:854` | `.about-grid.policy-next` (@media (min-width: 768px)) | `padding-top: var(--sp-2xl)` | overrides `padding-top` (about-grid, 768+) |
| `book-note.css:1469` | `.bn-page .policy-next`  | `margin-top: 0` | overrides `margin-top` to 0 |
| `about.css:197` | `.pfq + .policy-next--pair`  | `margin-top: 0` | `margin-top: 0` on the pair variant |
| `knowledge-hub.css:885` | `.kh-foot__sep > .policy-next`  | `margin-bottom: 0` | `margin-bottom: 0`, a property the base does not set |
| `help.css:418` | `.policy-next--bubble`  | `position: relative; isolation: isolate` | adds `position`, `isolation`; no base property touched |
| `help.css:433` | `.policy-next--bubble` (@media (min-width: 1040px)) | `margin-left: calc(-1 * var(--sp-xl)); margin-right: calc(-1 * var(--sp-xl))` | adds negative side margins at 1040+; base sets none |
| `help.css:438` | `.policy-next--bubble::after`  | `content: ''; position: absolute; top: 20px; bottom: 20px; right: 0; aspect-ratio: 534 / 600; background: url('images/achology-bubble-mark.webp') no-repeat left center; background-size: auto 100%; opacity: 0.06; pointer-events: non` | adds `::after` watermark |
| `help.css:452` | `.policy-next--bubble > *`  | `position: relative; z-index: 1` | child stacking |
| `help.css:460` | `.policy-next--no-mark::after`  | `display: none` | hides the watermark |
| `help.css:462` | `.policy-next--bubble::after` (@media (max-width: 1023px)) | `display: none` | hides the watermark under 1024 |

Verdict for the panel itself: not five drifted copies. One definition plus 12 override or variant blocks that each set properties the base does not, or deliberately zero a margin. None repeats the base's four declarations. Whether the user's "five copies" refers to something outside the stylesheets (for example the `previews/` mock-ups, which were not examined) cannot be told from the code.

### D.1.3 The nearest real duplicate: `.policy-index__row` family (`policies.css`) against `.policy-next__row` family (`components.css`)

`components.css:361-362` says the row anatomy "mirrors the policy-index rows". The two families do drift. Compared selector by selector:

| `.policy-next` (components.css) | `.policy-index` (policies.css) | Same? | Only in `.policy-next` | Only in `.policy-index` |
|---|---|---|---|---|
| `.policy-next__row` (`:443`) | `.policy-index__row` (`:527`) | DIFFERS | padding: var(--sp-md) var(--sp-lg) | padding: var(--sp-lg) |
| `.policy-next__row:hover` (`:455`) | `.policy-index__row:hover` (`:539`) | identical | - | - |
| `.policy-next__text` (`:479`) | `.policy-index__text` (`:573`) | DIFFERS | display: flex; flex-direction: column; gap: 2px | - |
| `.policy-next__name` (`:486`) | `.policy-index__name` (`:577`) | DIFFERS | font-size: var(--text-18) | display: block; font-size: var(--text-16); margin-bottom: 3px |
| `.policy-next__desc` (`:495`) | `.policy-index__desc` (`:594`) | DIFFERS | color: var(--color-soft-grey) | color: var(--color-dark); display: block |
| `.policy-next__arrow` (`:504`) | `.policy-index__arrow` (`:662`) | identical | - | - |
| `.policy-next__arrow svg` (`:512`) | `.policy-index__arrow svg` (`:670`) | identical | - | - |
| `.policy-next__row:hover .policy-next__name` (`:517`) | `.policy-index__row:hover .policy-index__name` (`:675`) | identical | - | - |
| `.policy-next__row:hover .policy-next__arrow` (`:535`) | `.policy-index__row:hover .policy-index__arrow` (`:679`) | identical | - | - |

`.policy-next__icon` (`components.css:462`) has no `.policy-index__icon` counterpart in `policies.css`. Shared unchanged: `:hover` on the row, arrow, arrow svg and both hover-name/arrow rules. Differing: row padding (`var(--sp-md) var(--sp-lg)` against `var(--sp-lg)`), text layout (flex column, gap 2px against none), name size (18px token against 16px token plus `display: block` and a 3px margin), description colour (`--color-soft-grey` against `--color-dark`) and `display: block`. Intent cannot be told from the code; the `policies.css` file also carries a separate large block (`policies.css:622-679`) for a data-word watermark on `.policy-index__row` that has no `.policy-next` equivalent.

## D.2 The breadcrumb

**Finding: two breadcrumb styles exist: `.breadcrumb` (with `.breadcrumb-bar`) and `.ap-crumb`. They are the same idea written twice, with different markup, and they are nearly the same visually but not identical.**

| | `.breadcrumb` family | `.ap-crumb` |
|---|---|---|
| Defined | `components.css:58-124` (rules), `policies.css:122` (`.breadcrumb-bar`), dark-ground variants `components.css:2116-2138`, `courses-directory.css:22-32`, `book-note.css`, `quote.css`, `knowledge-hub.css` spacing | `people.css:49-54` |
| Markup | `<nav class="breadcrumb-bar"><ol class="breadcrumb"><li class="breadcrumb__item">` with `breadcrumb__link`, `breadcrumb__home`, `breadcrumb__separator`, `breadcrumb__current` | `<nav class="ap-crumb">` with bare `<a>`, `<span>` separators, `<span class="current">` (no list) |
| Container layout | `display:flex; align-items:center; gap: var(--sp-xs) [4px]; flex-wrap: wrap; list-style:none; padding:0; margin:0` | `display:flex; align-items:center; flex-wrap:wrap; gap:6px` |
| Spacing | `.breadcrumb-bar { margin-bottom: var(--sp-2xl) }` (48px); top margin supplied by the page band | `margin: var(--sp-2xl) 0 48px`; `margin-top: var(--sp-xl)` under 768px |
| Text size / weight | `font-size: var(--text-12)`, link and current both `font-weight: 400` | `font-size: var(--text-12)`; link inherits; current `font-weight: 600` |
| Link colour / hover | `--color-soft-grey`, hover `--color-dark`; transition `color 0.15s ease` | `--color-soft-grey`, hover `--color-dark`; no transition |
| Current page colour | `--color-orange-link` | `--color-orange-link` |
| Separator | `.breadcrumb__separator` colour `--color-mid-grey`; svg `.icon-breadcrumb` 13px, `--color-mid-grey` | bare `<span>`; svg `.ico` 13px; colour inherits `--color-soft-grey` |
| Home link | `.breadcrumb__home` mid-grey, hover dark | plain `<a>` in `--color-soft-grey` |
| Dark-ground variants | yes (`.kh-hero`, `.cd-band`, `.bn-hero`) | none |

Plain verdict: **nearly the same.** Same size, same link and current-page colours, same hover, same 13px icons, same 48px rhythm. Different in markup (list versus bare links), in the 600 weight on the current page, in separator and home-icon colour (mid-grey against soft-grey), in the gap (4px against 6px), and in having no dark-ground variant. `people.css:47-48` says it "matches .breadcrumb", and `template-our-people.php:31-33` records a ruling that breadcrumb separators were deliberately kept out of the icon registry, so the exclusion of the registry is deliberate; whether the separate `.ap-crumb` stylesheet is deliberate cannot be told from the code.

Templates using `.breadcrumb` (literal `class="breadcrumb"` markup, one nav each, 16 files): `404.php`, `archive-faq_article.php`, `learn-listing.php`, `page-about.php`, `page-reviews.php`, `page-testimonials.php`, `single-article.php`, `single-book_note.php`, `single-faq_article.php`, `single-quote.php`, `taxonomy-faq_category.php`, `taxonomy-kh_category.php`, `template-course.php`, `template-courses.php`, `template-policies-index.php`, `template-policy.php`.

Templates using `.ap-crumb`: `template-our-people.php:81`, `template-author-profile.php:50`.

`page-pricing.php` has a `BreadcrumbList` JSON-LD block (`page-pricing.php:244-253`) but no visible `.breadcrumb` or `.ap-crumb` markup in that file; whether a shared function draws one cannot be told without tracing `achology_pricing_blocks()`.
