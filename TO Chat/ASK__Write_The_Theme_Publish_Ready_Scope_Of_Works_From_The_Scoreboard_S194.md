**For Chat. What this needs:** one scope of works, in order, that takes every theme page and template to READY under DSRD 6 §0, written as a brief a brand-new theme session can open and run. Kain's yes, S194 (28 October 2026): "Yes, send Chat the scoreboard so it writes the theme publish-ready scope of works for a new session."

# ASK: write the theme publish-ready scope of works from the readiness scoreboard (Code, theme S194, 28 October 2026)

## Why
Kain asked for one set of deliverables that brings the theme in its current state up to publish ready, instead of a mountain of small jobs in the background, to be kicked off in a fresh session. The scoreboard is the honest starting point: it derives the row set from the theme and WordPress, not from the records that exist.

## The scoreboard, run today at theme 0.707.657 (`python3 page_readiness_board.py`)
857 rows owe a record, covering 873 live pages. 28 have no record. 0 are READY. 621 carry a failing line. 7,973 chapter lines are open. Columns: closed, open, fail.

The theme's own pages and templates (32 rows), the scope this ASK is about:

```
404.php (any unknown address)        2   5   4   open: §2 §3 §4 §5 §7 §8 §9 §10 §11
/about/                              2   6   3   open: §1 §2 §3 §4 §5 §7 §9 §10 §11
/accessibility-statement/            3   6   2   open: §2 §3 §4 §5 §7 §9 §10 §11
archive-faq_article.php /help/       NOT MEASURED, no record
/cards/                              0   8   3   open: §1 to §11
/code-of-ethics/                     9   2   0   open: §10 §11
/cookie-policy/                      3   6   2   open: §2 §3 §4 §5 §7 §9 §10 §11
/courses/                            1   5   4   open: §2 §3 §4 §5 §7 §8 §9 §10 §11 (1 line unreadable)
/disclaimers/                        3   6   2   open: §2 §3 §4 §5 §7 §9 §10 §11
/founders-letter/                    9   2   0   open: §10 §11
/how-we-write/                       8   0   1   open: §11 (2 lines unreadable)
/instructors/                        2   6   3   open: §1 §3 §4 §5 §7 §8 §9 §10 §11
learn-listing.php /learn/            2   7   2   open: §1 §2 §3 §4 §5 §7 §9 §10 §11
/manifesto/                          9   2   0   open: §10 §11
/policies/                           4   6   1   open: §3 §4 §5 §7 §9 §10 §11
/pricing/                            3   5   3   open: §1 §2 §3 §5 §7 §9 §10 §11
/privacy-policy/                     3   6   2   open: §2 §3 §4 §5 §7 §9 §10 §11
/refund-policy/                      3   6   2   open: §2 §3 §4 §5 §7 §9 §10 §11
/reviews/                            6   1   4   open: §1 §2 §7 §8 §11
single-article.php                   0   7   2   open: §1 §2 §3 §4 §5 §8 §9 §10 §11 (2 unreadable)
single-book_note.php                 3   6   2   open: §2 §3 §4 §5 §7 §9 §10 §11
single-faq_article.php               3   4   4   open: §2 §3 §4 §5 §7 §9 §10 §11
single-quote.php                     3   5   1   open: §2 §3 §4 §5 §7 §9 (2 unreadable)
single-workbook.php                  0  11   0   open: §1 to §11
taxonomy-faq_category.php            3   5   3   open: §2 §3 §4 §5 §7 §9 §10 §11
taxonomy-kh_category.php             2   4   5   open: §1 §2 §3 §4 §5 §7 §9 §10 §11
taxonomy-kh_tag.php                  3   7   1   open: §2 §3 §4 §5 §8 §9 §10 §11
template-author-profile.php (17)     2   6   3   open: §1 §3 §4 §5 §7 §8 §9 §10 §11
/terms-and-conditions/               3   6   2   open: §2 §3 §4 §5 §7 §9 §10 §11
/testimonials/                       0   7   4   open: §1 to §11
/trust-statement/                    3   6   2   open: §2 §3 §4 §5 §7 §9 §10 §11
/workbook-thank-you/                 NOT MEASURED, no record (and no published page found)
```

The content rows (373 articles, 150 book notes, 302 Help answers) are left to the factory imports and are not this ASK, except where a template line fails on all of them.

## What Code knows that the plan should weigh
- Many open chapters on signed pages are records never re-swept, not faults: a sweep (`page_readiness_board.py --sweep`) closes machine halves fast, but it wipes Chat's reader halves (copy the record first, restore after; factory fault, met at S188 and S191).
- Several lines are instrument faults: the orphan crawl misses 913 pages; keyword density reads the empty editor on theme-built pages; Rank Math scores the empty editor on theme pages (the founder and policy pages carry that as Kain's exception).
- css_gate still fails 7 stylesheets on the old spacing lines (header.css alone holds 38: on-scale hand-typed values that can become tokens with no visible change, and off-scale optical values that need a ruling or an annotation). One ruling on the off-scale kind would let the new session clear them in one pass.
- Fold in, so nothing sits in the background: from NOTE S449, the sky-less re-exports, cloud jobs 18 and 19, All Tags at 320; from BRIEF__Operation_Cleanup, T6 (mail and Tag Manager), T8 (the S169 four decisions branch) and T15 (thank-you page words), with T3 to T5 as their own sessions (T7 and T9 are DONE at S194; T1, T2, T10 to T14 at S191); Page Readiness R2 to R4, R6 to R9, R11; the two renames; the 16 list search titles; site search with the 37 synonyms; the founder pages' sign-off and VoiceOver read at Kain's sitting.
- Founder pages today: chapter 7 passes on all three (SHIP__0.707.657_Founder_Pages_Hover_Contrast_S194); open are §10 and §11, plus one site-wide spacing line (author-card__role margin-top 2) and two mega menu thumbnails served at 96x96 against 768x366 files.

## What Code suggests for the order
Kain's one-page-at-a-time rule stands. Code suggests: first the sweeps and instrument fixes (no Kain needed, closes most machine halves at once); then the templates that carry the most pages (single-faq_article, single-article, single-book_note, the taxonomy pages), because each closes lines on hundreds of content pages; then the site pages; with the pages that need Kain's eye batched into one Safari sitting at his width (1268) where possible. Chat decides.

OWED BACK: one BRIEF in FROM Chat that a new theme session can open and run, with its PAGE GATE line where it builds a page.

*No em or en dashes in this file; checked before writing.*
