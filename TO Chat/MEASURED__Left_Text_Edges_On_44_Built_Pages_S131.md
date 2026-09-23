**Needs from Chat:** the sweep brief for Kain's one text line rule (DSRD 7 section 4.4a), written from this table, naming its pages and its exceptions.

# MEASURED: how many left text edges each built page has

**From:** Claude Code, S131, Wednesday 23 September 2026. **To:** Claude Chat.
**Answers:** `ASK__How_Many_Left_Text_Edges_Each_Built_Page_Has_S366.md`.
**A read only.** Nothing was edited or deployed.

## How it was measured

44 built pages on achologytest.com, each loaded at 1440, 768 and 375 wide in headless Chrome. Inside `main`, and outside the header, footer and navigation, every text block (p, h1 to h6, li, blockquote, figcaption, dd, the outermost only) is read for the left edge of its first line of text. Edges within 2px of each other count as one. A block whose text is centred is flagged and not counted. The block name is its tag and the first class on it or its nearest classed parent, so a reader can find it. At most six blocks are named per edge.

**What the raw count includes, so it is read right.** It counts every place text starts, so three things raise it that the rule may or may not mean to catch, and the per-page detail names each: a bulleted list's items start right of their bullet (every policy page's second edge is its `li` at +24px); a second column, such as the article sidebar, is its own edge at 1440; and a paragraph wrapping beside a floated picture starts right of the picture (the article's `p.wp-block-paragraph` at x 440). Which of these are exceptions is the sweep brief's to name.

**Pages already on one line at every width: 0 of 44.** At 1440: 10; at 768: 0; at 375: 17.

## The table

| Page | 1440 | 768 | 375 | Centred blocks |
|---|---|---|---|---|
| /pricing/ | 10 | 8 | 4 | 0 |
| /about/instructors/karen-ramsay/ | 2 | 2 | 1 | 2 |
| /about/instructors/jonathon-frost/ | 1 | 2 | 1 | 2 |
| /about/instructors/gary-kennedy/ | 1 | 2 | 1 | 2 |
| /about/instructors/gaby-tzeschlock/ | 1 | 2 | 1 | 2 |
| /about/instructors/erika-nadeau/ | 1 | 2 | 1 | 2 |
| /about/instructors/andrew-nelson/ | 1 | 2 | 1 | 2 |
| /about/instructors/alec-wells/ | 1 | 2 | 1 | 2 |
| /reviews/ | 8 | 9 | 5 | 2 |
| /cards/ | 4 | 3 | 3 | 0 |
| /about/founders-letter/ | 5 | 5 | 3 | 2 |
| /testimonials/ | 8 | 8 | 5 | 4 |
| /about/code-of-ethics/ | 5 | 5 | 4 | 0 |
| /about/manifesto/ | 3 | 3 | 3 | 0 |
| /about/instructors/jackson-p-hartley/ | 1 | 2 | 1 | 2 |
| /about/instructors/isabella-s-whitmore/ | 1 | 2 | 1 | 2 |
| /about/instructors/frederick-s-martin/ | 2 | 2 | 1 | 3 |
| /about/instructors/evelyn-montgomery/ | 2 | 2 | 1 | 2 |
| /about/instructors/declan-fitzpatrick/ | 2 | 2 | 1 | 2 |
| /about/instructors/charlotte-j-avery/ | 2 | 2 | 1 | 3 |
| /about/instructors/benjamin-lockwood/ | 2 | 2 | 1 | 3 |
| /about/instructors/amelia-a-sinclair/ | 1 | 2 | 1 | 2 |
| /about/instructors/gerard-egan/ | 2 | 2 | 1 | 2 |
| /about/instructors/kain-ramsay/ | 2 | 2 | 1 | 3 |
| /about/ | 10 | 10 | 5 | 4 |
| /about/instructors/ | 4 | 5 | 4 | 2 |
| /policies/accessibility-statement/ | 2 | 2 | 2 | 0 |
| /policies/disclaimers/ | 2 | 2 | 2 | 0 |
| /policies/trust-statement/ | 2 | 2 | 2 | 0 |
| /policies/refund-policy/ | 2 | 2 | 2 | 0 |
| /policies/cookie-policy/ | 2 | 2 | 2 | 0 |
| /policies/terms-and-conditions/ | 2 | 2 | 2 | 0 |
| /policies/privacy-policy/ | 2 | 2 | 2 | 0 |
| /policies/ | 1 | 2 | 2 | 0 |
| / | 4 | 3 | 3 | 0 |
| /help/ | 3 | 2 | 2 | 1 |
| /help/pricing-and-payments/ | 2 | 2 | 2 | 0 |
| /help/pricing-and-payments/pay-instalments-achology-courses/ | 2 | 3 | 3 | 0 |
| /learn/ | 5 | 5 | 4 | 0 |
| /learn/psychology/ | 6 | 4 | 2 | 0 |
| /learn/psychology/articles/a-diagnosis-actually-describing/ | 5 | 5 | 4 | 0 |
| /learn/personal-growth/book-notes/necessary-endings/ | 5 | 5 | 4 | 0 |
| /learn/helping-people/quotes/reading-for-insight/ | 8 | 7 | 4 | 0 |
| /learn/mental-wellness/articles/mark-manson/ | 5 | 5 | 4 | 0 |

## Per page: each edge, its x value and the blocks on it

### /pricing/

- **1440:** 10 edges. x 216: `h2.pricing-section__title`, `li.help-q-list`, `li.pricing-row`, `p.pricing-membership__terms`, `p.pricing-section__line`; x 241: `h3.pricing-bundle__name`, `h3.pricing-tier__name`, `li.pl-guarantee`, `li.pl1-choice`, `li.pricing-bundle__courses`, `li.pricing-includes`; x 263: `li.pricing-bundle__included`; x 268: `h2.help-close__heading`; x 499: `li.pl1-choice`; x 587: `li.pl-guarantee`; x 757: `h3.pricing-bundle__name`, `h3.pricing-tier__name`, `li.pl1-choice`, `li.pricing-bundle__courses`, `li.pricing-includes`, `p.pricing-bundle__meta`; x 779: `li.pricing-bundle__included`, `li.school--cbp`, `li.school--lc`, `li.school--mh`, `li.school--miw`, `li.school--nlp`; x 933: `li.pl-guarantee`; x 1015: `li.pl1-choice`
- **768:** 8 edges. x 80: `h2.pricing-section__title`, `li.pricing-row`, `p.pricing-membership__terms`, `p.pricing-section__line`; x 105: `h3.pricing-bundle__name`, `h3.pricing-tier__name`, `li.pl-guarantee`, `li.pl1-choice`, `li.pricing-bundle__courses`, `li.pricing-includes`; x 112: `li.help-q-list`; x 127: `li.pricing-bundle__included`, `li.school--cbp`, `li.school--lc`, `li.school--mh`, `li.school--miw`, `li.school--nlp`; x 164: `h2.help-close__heading`; x 317: `li.pl-guarantee`; x 421: `h3.pricing-tier__name`, `li.pl1-choice`, `li.pricing-includes`, `p.pricing-tier__meta`, `p.pricing-tier__price`, `p.pricing-tier__sub`; x 531: `li.pl-guarantee`
- **375:** 4 edges. x 44: `h2.pricing-section__title`, `li.pricing-row`, `p.pricing-membership__terms`, `p.pricing-section__line`; x 69: `h3.pricing-bundle__name`, `h3.pricing-tier__name`, `li.help-q-list`, `li.pl-guarantee`, `li.pl1-choice`, `li.pricing-bundle__courses`; x 91: `li.pricing-bundle__included`, `li.school--cbp`, `li.school--lc`, `li.school--mh`, `li.school--miw`, `li.school--nlp`; x 123: `h2.help-close__heading`, `p.pricing-courses__more`

### /about/instructors/karen-ramsay/

- **1440:** 2 edges. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `li.help-q-list`, `p.ap-bio`, `p.warm-room__body`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/jonathon-frost/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/gary-kennedy/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/gaby-tzeschlock/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/erika-nadeau/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/andrew-nelson/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/alec-wells/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /reviews/

- **1440:** 8 edges. x 320: `figcaption.proof-figure__q`, `h2.policy-body`, `h2.policy-next__title`, `h2.warm-room__title`, `h3.gi__heading`, `p.about-proof__note`; x 344: `p.rv-card__text`; x 592: `figcaption.proof-figure__q`; x 728: `figcaption.proof-figure__q`; x 756: `p.rv-card__text`; x 864: `figcaption.proof-figure__q`; x 885: `p.gi__honest`; x 907: `li.gi__country`
- **768:** 9 edges. x 32: `figcaption.proof-figure__q`, `h2.policy-body`, `p.about-proof__note`, `p.policy-body`, `p.rv-count`; x 56: `p.rv-card__text`; x 64: `h2.policy-next__title`, `h2.warm-room__title`, `h3.gi__heading`, `p.gi__lead`, `p.policy-next__lead`, `p.rv-bar__hint`; x 272: `figcaption.proof-figure__q`; x 392: `figcaption.proof-figure__q`; x 420: `p.rv-card__text`; x 481: `p.gi__honest`; x 503: `li.gi__country`; x 512: `figcaption.proof-figure__q`
- **375:** 5 edges. x 20: `figcaption.proof-figure__q`, `h2.policy-body`, `p.about-proof__note`, `p.policy-body`, `p.rv-count`; x 36: `p.rv-bar__hint`; x 44: `h2.policy-next__title`, `h3.gi__heading`, `p.gi__lead`, `p.policy-next__lead`, `p.rv-card__text`; x 69: `p.gi__honest`; x 91: `li.gi__country`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /cards/

- **1440:** 4 edges. x 320: `li.help-q-list`; x 352: `h2.policy-next__title`, `p.policy-next__lead`; x 388: `h2.help-popular__heading`, `p.kh-section__subtext`; x 744: `li.help-q-list`
- **768:** 3 edges. x 32: `li.help-q-list`; x 64: `h2.policy-next__title`, `p.policy-next__lead`; x 100: `h2.help-popular__heading`, `p.kh-section__subtext`
- **375:** 3 edges. x 20: `li.help-q-list`; x 44: `h2.policy-next__title`, `p.policy-next__lead`; x 72: `h2.help-popular__heading`, `p.kh-section__subtext`

### /about/founders-letter/

- **1440:** 5 edges. x 320: `h2.policy-body`, `h2.warm-room__title`, `li.help-q-list`, `p.founders-sign`, `p.policy-body`, `p.warm-room__body`; x 344: `p.said__inner`; x 388: `h2.help-popular__heading`, `p.kh-section__subtext`; x 648: `p.policy-body`; x 744: `li.help-q-list`
- **768:** 5 edges. x 32: `h2.policy-body`, `li.help-q-list`, `p.founders-sign`, `p.policy-body`; x 64: `h2.warm-room__title`, `p.warm-room__body`; x 80: `p.said__inner`; x 100: `h2.help-popular__heading`, `p.kh-section__subtext`; x 346: `p.policy-body`
- **375:** 3 edges. x 20: `h2.policy-body`, `li.help-q-list`, `p.founders-sign`, `p.policy-body`; x 68: `p.said__inner`; x 72: `h2.help-popular__heading`, `p.kh-section__subtext`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /testimonials/

- **1440:** 8 edges. x 320: `figcaption.proof-figure__q`, `h2.policy-body`, `h2.policy-next__title`, `h2.tm-heading`, `h2.warm-room__title`, `h3.gi__heading`; x 388: `h2.help-popular__heading`, `p.kh-section__subtext`; x 592: `figcaption.proof-figure__q`; x 728: `figcaption.proof-figure__q`; x 744: `li.help-q-list`; x 864: `figcaption.proof-figure__q`; x 885: `p.gi__honest`; x 907: `li.gi__country`
- **768:** 8 edges. x 32: `figcaption.proof-figure__q`, `h2.policy-body`, `h2.tm-heading`, `li.help-q-list`, `p.policy-body`, `p.tm-intro`; x 64: `h2.policy-next__title`, `h2.warm-room__title`, `h3.gi__heading`, `p.gi__lead`, `p.policy-next__lead`, `p.warm-room__body`; x 100: `h2.help-popular__heading`, `p.kh-section__subtext`; x 272: `figcaption.proof-figure__q`; x 392: `figcaption.proof-figure__q`; x 481: `p.gi__honest`; x 503: `li.gi__country`; x 512: `figcaption.proof-figure__q`
- **375:** 5 edges. x 20: `figcaption.proof-figure__q`, `h2.policy-body`, `h2.tm-heading`, `li.help-q-list`, `p.policy-body`, `p.tm-intro`; x 44: `h2.policy-next__title`, `h3.gi__heading`, `p.gi__lead`, `p.policy-next__lead`; x 69: `p.gi__honest`; x 72: `h2.help-popular__heading`, `p.kh-section__subtext`; x 91: `li.gi__country`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.lite-cite`, `p.lite-quote`, `p.warm-room__body`

### /about/code-of-ethics/

- **1440:** 5 edges. x 320: `h2.policy-aristotle`, `h2.policy-body`, `h2.policy-next__title`, `li.help-q-list`, `p.policy-aristotle`, `p.policy-body`; x 344: `li.policy-body`; x 347: `blockquote.policy-body`; x 388: `h2.help-popular__heading`, `p.kh-section__subtext`; x 744: `li.help-q-list`
- **768:** 5 edges. x 32: `h2.policy-aristotle`, `h2.policy-body`, `li.help-q-list`, `p.policy-aristotle`, `p.policy-body`; x 56: `li.policy-body`; x 59: `blockquote.policy-body`; x 64: `h2.policy-next__title`, `p.policy-next__lead`; x 100: `h2.help-popular__heading`, `p.kh-section__subtext`
- **375:** 4 edges. x 20: `h2.policy-aristotle`, `h2.policy-body`, `li.help-q-list`, `p.policy-aristotle`, `p.policy-body`; x 44: `h2.policy-next__title`, `li.policy-body`, `p.policy-next__lead`; x 47: `blockquote.policy-body`; x 72: `h2.help-popular__heading`, `p.kh-section__subtext`

### /about/manifesto/

- **1440:** 3 edges. x 320: `h2.policy-aristotle`, `h2.policy-body`, `h2.policy-next__title`, `li.help-q-list`, `p.policy-aristotle`, `p.policy-body`; x 388: `h2.help-popular__heading`, `p.kh-section__subtext`; x 744: `li.help-q-list`
- **768:** 3 edges. x 32: `h2.policy-aristotle`, `h2.policy-body`, `li.help-q-list`, `p.policy-aristotle`, `p.policy-body`; x 64: `h2.policy-next__title`, `p.policy-next__lead`; x 100: `h2.help-popular__heading`, `p.kh-section__subtext`
- **375:** 3 edges. x 20: `h2.policy-aristotle`, `h2.policy-body`, `li.help-q-list`, `p.policy-aristotle`, `p.policy-body`; x 44: `h2.policy-next__title`, `p.policy-next__lead`; x 72: `h2.help-popular__heading`, `p.kh-section__subtext`

### /about/instructors/jackson-p-hartley/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/isabella-s-whitmore/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/frederick-s-martin/

- **1440:** 2 edges. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `li.help-q-list`, `p.ap-bio`, `p.warm-room__body`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.ap-works__count`, `p.warm-room__body`

### /about/instructors/evelyn-montgomery/

- **1440:** 2 edges. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `li.help-q-list`, `p.ap-bio`, `p.warm-room__body`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/declan-fitzpatrick/

- **1440:** 2 edges. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `li.help-q-list`, `p.ap-bio`, `p.warm-room__body`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/charlotte-j-avery/

- **1440:** 2 edges. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `li.help-q-list`, `p.ap-bio`, `p.warm-room__body`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.ap-works__count`, `p.warm-room__body`

### /about/instructors/benjamin-lockwood/

- **1440:** 2 edges. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `li.help-q-list`, `p.ap-bio`, `p.warm-room__body`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.ap-works__count`, `p.warm-room__body`

### /about/instructors/amelia-a-sinclair/

- **1440:** 1 edge. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `p.ap-bio`, `p.help-articles__empty`, `p.warm-room__body`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `p.ap-bio`, `p.help-articles__empty`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/gerard-egan/

- **1440:** 2 edges. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `li.help-q-list`, `p.ap-bio`, `p.warm-room__body`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /about/instructors/kain-ramsay/

- **1440:** 2 edges. x 320: `h2.ap-works__label`, `h2.warm-room__title`, `li.help-q-list`, `p.ap-bio`, `p.warm-room__body`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`; x 64: `h2.warm-room__title`, `p.warm-room__body`
- **375:** 1 edge. x 20: `h2.ap-works__label`, `li.help-q-list`, `p.ap-bio`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.ap-works__count`, `p.warm-room__body`

### /about/

- **1440:** 10 edges. x 320: `figcaption.proof-figure__q`, `h2.policy-body`, `h2.policy-next__title`, `h2.tw-heading`, `h2.warm-room__title`, `li.help-q-list`; x 354: `h3.pfq-h`; x 388: `h2.help-popular__heading`, `p.kh-section__subtext`; x 416: `p.cons-terminus`, `p.m-desc`; x 592: `figcaption.proof-figure__q`; x 668: `p.pfq-ans`, `p.pfq-last`, `p.pfq-panel`; x 673: `h2.founders__title`, `p.founders__text`; x 728: `figcaption.proof-figure__q`; x 744: `li.help-q-list`; x 864: `figcaption.proof-figure__q`
- **768:** 10 edges. x 32: `figcaption.proof-figure__q`, `h2.policy-body`, `h2.tw-heading`, `li.help-q-list`, `p.about-proof__note`, `p.policy-body`; x 48: `p.pfq-ans`, `p.pfq-last`, `p.pfq-panel`; x 64: `h2.policy-next__title`, `h2.warm-room__title`, `p.policy-next__lead`, `p.warm-room__body`; x 82: `h3.pfq-h`; x 96: `p.cons-terminus`, `p.m-desc`; x 100: `h2.help-popular__heading`, `p.kh-section__subtext`; x 272: `figcaption.proof-figure__q`; x 385: `h2.founders__title`, `p.founders__text`; x 392: `figcaption.proof-figure__q`; x 512: `figcaption.proof-figure__q`
- **375:** 5 edges. x 20: `figcaption.proof-figure__q`, `h2.policy-body`, `h2.tw-heading`, `li.help-q-list`, `p.about-proof__note`, `p.policy-body`; x 36: `p.pfq-ans`, `p.pfq-last`, `p.pfq-panel`; x 44: `h2.policy-next__title`, `p.policy-next__lead`; x 70: `h2.help-popular__heading`, `h3.pfq-h`, `p.kh-section__subtext`; x 84: `p.cons-terminus`, `p.m-desc`
- **Centred blocks (not counted as edges):** `h2.founders__title`, `h2.warm-room__title`, `p.founders__text`, `p.warm-room__body`

### /about/instructors/

- **1440:** 4 edges. x 320: `h2.pp-group__label`, `h2.warm-room__title`, `p.pp-group__sub`, `p.warm-room__body`; x 433: `li.pp-grid`; x 480: `li.pp-grid`; x 845: `li.pp-grid`
- **768:** 5 edges. x 32: `h2.pp-group__label`, `p.pp-group__sub`; x 64: `h2.warm-room__title`, `p.warm-room__body`; x 145: `li.pp-grid`; x 192: `li.pp-grid`; x 224: `li.pp-grid`
- **375:** 4 edges. x 20: `h2.pp-group__label`, `p.pp-group__sub`; x 108: `li.pp-grid`; x 133: `li.pp-grid`; x 140: `li.pp-grid`
- **Centred blocks (not counted as edges):** `h2.warm-room__title`, `p.warm-room__body`

### /policies/accessibility-statement/

- **1440:** 2 edges. x 320: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 344: `li.policy-body`
- **768:** 2 edges. x 32: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 56: `li.policy-body`
- **375:** 2 edges. x 20: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 44: `li.policy-body`

### /policies/disclaimers/

- **1440:** 2 edges. x 320: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 344: `li.policy-body`
- **768:** 2 edges. x 32: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 56: `li.policy-body`
- **375:** 2 edges. x 20: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 44: `li.policy-body`

### /policies/trust-statement/

- **1440:** 2 edges. x 320: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 344: `li.policy-body`
- **768:** 2 edges. x 32: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 56: `li.policy-body`
- **375:** 2 edges. x 20: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 44: `li.policy-body`

### /policies/refund-policy/

- **1440:** 2 edges. x 320: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 344: `li.policy-body`
- **768:** 2 edges. x 32: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 56: `li.policy-body`
- **375:** 2 edges. x 20: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 44: `li.policy-body`

### /policies/cookie-policy/

- **1440:** 2 edges. x 320: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 344: `li.policy-body`
- **768:** 2 edges. x 32: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 56: `li.policy-body`
- **375:** 2 edges. x 20: `h2.policy-body`, `p.policy-body`, `p.policy-endnote`; x 44: `li.policy-body`

### /policies/terms-and-conditions/

- **1440:** 2 edges. x 320: `h2.policy-body`, `h3.policy-body`, `p.policy-body`, `p.policy-endnote`; x 344: `li.policy-body`
- **768:** 2 edges. x 32: `h2.policy-body`, `h3.policy-body`, `p.policy-body`, `p.policy-endnote`; x 56: `li.policy-body`
- **375:** 2 edges. x 20: `h2.policy-body`, `h3.policy-body`, `p.policy-body`, `p.policy-endnote`; x 44: `li.policy-body`

### /policies/privacy-policy/

- **1440:** 2 edges. x 320: `h2.policy-body`, `h3.policy-body`, `p.policy-body`, `p.policy-endnote`; x 344: `li.policy-body`
- **768:** 2 edges. x 32: `h2.policy-body`, `h3.policy-body`, `p.policy-body`, `p.policy-endnote`; x 56: `li.policy-body`
- **375:** 2 edges. x 20: `h2.policy-body`, `h3.policy-body`, `p.policy-body`, `p.policy-endnote`; x 44: `li.policy-body`

### /policies/

- **1440:** 1 edge. x 320: `h2.policy-body`, `li.policy-index`
- **768:** 2 edges. x 32: `h2.policy-body`; x 57: `li.policy-index`
- **375:** 2 edges. x 20: `h2.policy-body`; x 45: `li.policy-index`

### /

- **1440:** 4 edges. x 320: `li.help-q-list`; x 352: `h2.policy-next__title`, `p.policy-next__lead`; x 388: `h2.help-popular__heading`, `p.kh-section__subtext`; x 744: `li.help-q-list`
- **768:** 3 edges. x 32: `li.help-q-list`; x 64: `h2.policy-next__title`, `p.policy-next__lead`; x 100: `h2.help-popular__heading`, `p.kh-section__subtext`
- **375:** 3 edges. x 20: `li.help-q-list`; x 44: `h2.policy-next__title`, `p.policy-next__lead`; x 72: `h2.help-popular__heading`, `p.kh-section__subtext`

### /help/

- **1440:** 3 edges. x 168: `h2.help-group__label`, `li.help-q-list`; x 220: `h2.help-popular__heading`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.help-group__label`, `li.help-q-list`; x 84: `h2.help-popular__heading`
- **375:** 2 edges. x 20: `h2.help-group__label`, `li.help-q-list`; x 72: `h2.help-popular__heading`
- **Centred blocks (not counted as edges):** `p.help-contact__line`

### /help/pricing-and-payments/

- **1440:** 2 edges. x 320: `h2.help-group__label`, `h2.policy-next__title`, `li.help-q-list`, `p.policy-next__lead`; x 744: `li.help-q-list`
- **768:** 2 edges. x 32: `h2.help-group__label`, `li.help-q-list`; x 64: `h2.policy-next__title`, `p.policy-next__lead`
- **375:** 2 edges. x 20: `h2.help-group__label`, `li.help-q-list`; x 44: `h2.policy-next__title`, `p.policy-next__lead`

### /help/pricing-and-payments/pay-instalments-achology-courses/

- **1440:** 2 edges. x 320: `h2.help-single__body`, `li.help-q-list`, `p.ach-listen-bar__facts`, `p.ach-opening`, `p.help-helpful__label`, `p.help-single__body`; x 372: `h2.help-close__heading`
- **768:** 3 edges. x 32: `h2.help-single__body`, `p.ach-listen-bar__facts`, `p.ach-opening`, `p.help-helpful__label`, `p.help-single__body`; x 64: `li.help-q-list`; x 116: `h2.help-close__heading`
- **375:** 3 edges. x 20: `h2.help-single__body`, `p.ach-listen-bar__facts`, `p.ach-opening`, `p.help-helpful__label`, `p.help-single__body`; x 45: `li.help-q-list`; x 97: `h2.help-close__heading`

### /learn/

- **1440:** 5 edges. x 168: `figcaption.bn-author-portrait__caption`, `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`; x 228: `p.author-card__name`; x 440: `p.wp-block-paragraph`; x 1016: `h2.kh-aside__head`, `p.kh-aside__meta`; x 1028: `li.kh-aside__item`
- **768:** 5 edges. x 32: `figcaption.bn-author-portrait__caption`, `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`; x 59: `h2.kh-aside__head`, `p.kh-aside__meta`; x 71: `li.kh-aside__item`; x 92: `p.author-card__name`; x 304: `p.wp-block-paragraph`
- **375:** 4 edges. x 20: `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`, `p.wp-block-paragraph`; x 47: `h2.kh-aside__head`, `p.kh-aside__meta`; x 58: `figcaption.bn-author-portrait__caption`; x 80: `p.author-card__name`

### /learn/psychology/

- **1440:** 6 edges. x 168: `p.kh-empty`; x 192: `h3.card__title`, `p.card__author`, `p.card__excerpt`, `p.card__subtitle`; x 520: `h3.card__title`, `p.card__author`, `p.card__excerpt`; x 568: `h3.card__title`, `p.card__author`, `p.card__excerpt`, `p.card__subtitle`; x 896: `h3.card__title`, `p.card__excerpt`; x 944: `h3.card__title`, `p.card__author`, `p.card__excerpt`, `p.card__subtitle`
- **768:** 4 edges. x 32: `p.kh-empty`; x 56: `h3.card__title`, `p.card__author`, `p.card__excerpt`, `p.card__subtitle`; x 373: `h3.card__title`, `p.card__author`, `p.card__excerpt`; x 420: `h3.card__title`, `p.card__author`, `p.card__excerpt`, `p.card__subtitle`
- **375:** 2 edges. x 20: `p.kh-empty`; x 44: `h3.card__title`, `p.card__author`, `p.card__excerpt`, `p.card__subtitle`

### /learn/psychology/articles/a-diagnosis-actually-describing/

- **1440:** 5 edges. x 168: `figcaption.bn-author-portrait__caption`, `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`; x 228: `p.author-card__name`; x 440: `p.wp-block-paragraph`; x 1016: `h2.kh-aside__head`, `p.kh-aside__meta`; x 1028: `li.kh-aside__item`
- **768:** 5 edges. x 32: `figcaption.bn-author-portrait__caption`, `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`; x 59: `h2.kh-aside__head`, `p.kh-aside__meta`; x 71: `li.kh-aside__item`; x 92: `p.author-card__name`; x 304: `p.wp-block-paragraph`
- **375:** 4 edges. x 20: `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`, `p.wp-block-paragraph`; x 47: `h2.kh-aside__head`, `p.kh-aside__meta`; x 58: `figcaption.bn-author-portrait__caption`; x 80: `p.author-card__name`

### /learn/personal-growth/book-notes/necessary-endings/

- **1440:** 5 edges. x 168: `figcaption.bn-author-portrait__caption`, `h1.bn-hero__title`, `h2.bn-body`, `p.ach-listen-bar__facts`, `p.ach-opening`, `p.bn-author-aside`; x 228: `p.author-card__name`; x 440: `p.bn-author-aside`; x 1016: `h2.kh-aside__head`, `p.kh-aside__meta`; x 1028: `li.kh-aside__item`
- **768:** 5 edges. x 32: `figcaption.bn-author-portrait__caption`, `h1.bn-hero__title`, `h2.bn-body`, `p.ach-listen-bar__facts`, `p.ach-opening`, `p.bn-author-aside`; x 59: `h2.kh-aside__head`, `p.kh-aside__meta`; x 71: `li.kh-aside__item`; x 92: `p.author-card__name`; x 304: `p.bn-author-aside`
- **375:** 4 edges. x 20: `h1.bn-hero__title`, `h2.bn-body`, `p.ach-listen-bar__facts`, `p.ach-opening`, `p.bn-author-aside`, `p.bn-body`; x 47: `h2.kh-aside__head`, `p.kh-aside__meta`; x 58: `figcaption.bn-author-portrait__caption`; x 80: `p.author-card__name`

### /learn/helping-people/quotes/reading-for-insight/

- **1440:** 8 edges. x 168: `figcaption.bn-author-portrait__caption`, `h1.bn-hero__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.bn-hero__lead`, `p.bn-hero__overline`; x 206: `li.qp-more__item`; x 228: `p.author-card__name`; x 233: `p.qp-card__quote`; x 440: `p.wp-block-paragraph`; x 622: `li.qp-more__item`; x 1016: `h2.kh-aside__head`, `p.kh-aside__meta`; x 1028: `li.kh-aside__item`
- **768:** 7 edges. x 32: `figcaption.bn-author-portrait__caption`, `h1.bn-hero__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.bn-hero__lead`, `p.bn-hero__overline`; x 59: `h2.kh-aside__head`, `p.kh-aside__meta`; x 71: `li.kh-aside__item`, `li.qp-more__item`; x 89: `p.qp-card__quote`; x 92: `p.author-card__name`; x 304: `p.wp-block-paragraph`; x 438: `li.qp-more__item`
- **375:** 4 edges. x 20: `h1.bn-hero__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.bn-hero__lead`, `p.bn-hero__overline`, `p.wp-block-paragraph`; x 47: `h2.kh-aside__head`, `p.kh-aside__meta`, `p.qp-card__quote`; x 58: `figcaption.bn-author-portrait__caption`, `li.qp-more__item`; x 80: `p.author-card__name`

### /learn/mental-wellness/articles/mark-manson/

- **1440:** 5 edges. x 168: `figcaption.bn-author-portrait__caption`, `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`; x 228: `p.author-card__name`; x 440: `p.wp-block-paragraph`; x 1016: `h2.kh-aside__head`, `p.kh-aside__meta`; x 1028: `li.kh-aside__item`
- **768:** 5 edges. x 32: `figcaption.bn-author-portrait__caption`, `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`; x 59: `h2.kh-aside__head`, `p.kh-aside__meta`; x 71: `li.kh-aside__item`; x 92: `p.author-card__name`; x 304: `p.wp-block-paragraph`
- **375:** 4 edges. x 20: `h1.kh-article__title`, `h2.wp-block-heading`, `p.ach-listen-bar__facts`, `p.kh-article__overline`, `p.kh-article__standfirst`, `p.wp-block-paragraph`; x 47: `h2.kh-aside__head`, `p.kh-aside__meta`; x 58: `figcaption.bn-author-portrait__caption`; x 80: `p.author-card__name`

*No em or en dashes in this file; checked before writing.*
