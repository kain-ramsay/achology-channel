**For Chat. What this needs from you:** one ruling, whether the 34 pages at 88 are lifted by the importer fix in section 3 (no word changes) or by splitting sections in the records; and a word on the two Achology-only answers in section 2. Factory session, Code S194 (the session that began as S186).

# DONE: 50 of the 53 Help answers lifted for Rank Math are on the build site and rescored; the short paragraph test is answered (Code, S194 factory, 28 October 2026)

Answers NOTE__The_53_Help_Answers_Mended_For_Rank_Math_Import_With_SEO_And_Rescore_S449.

## 1. What reached the build site
- `body_guard.py --signed` exit 0 before any write (1,014 records, no working note).
- The theme's `tools/article_body_update.py --apply --with-seo` on 50 records: body, SEO title and SEO description. 50 of 50 updated in place, all still published, 0 refused.
- Read back with `--verify` (publish_gate.rendered_faults): 50 of 50 clean. One page (how-long-achology-refund-process) could not be read on the first pass; read again, clean.
- No record was changed by the run.

## 2. Not updated (3)
- **valts-achology and difference-between-monthly-annual-achology-membership:** the body tool refuses both for "no external link (DSRD 6 s5 item 11 move 6)". Both are answers about Achology only, which RULING__The_Help_Answer_Import_Section_5_Six_Rulings_S446 item 2 lets through, but your S449 gate-lines ruling names the body tool's outside link rule as a hard stop that never takes an exception. These two rulings disagree for these two pages. Ruling needed: an outside link added at source, or the Achology-only allowance carried into the body tool.
- **skilled-helper-course:** not on the build site; it lands with the 73 new answers, as your note says.

## 3. The short paragraph test: what Rank Math is reading
**The stored bodies carry no `<p>` tags.** The importer writes paragraphs separated by blank lines, and WordPress adds the `<p>` tags only when the page is shown. Rank Math's analyser in the editor reads the stored text with its line breaks collapsed, so with no `<p>` tags it treats everything between two headings (or a heading and a list) as one paragraph. Any such run over 120 words fails the test.

Measured with a read-only editor probe (Rank Math's own analyser, nothing saved), on two pages:
- achology-members-host-workshops-events (post 359, 88): no `<p>` tags; runs between headings of 109, 135 and 63 words; the 135 fails. Rank Math: "At least one paragraph is too long."
- achology-access-all-areas-pass (post 245, 93): no `<p>` tags; longest run 118 words. Rank Math: "You are using short paragraphs."

The words are not the cause, as you thought: each reader-visible paragraph is short. **The fix, in the importer, never in the records:** the conversion wraps each paragraph in `<p>` tags before it stores the body. That is a change to the theme's `tools/article_body_update.py`, which is outside the deploy set but is shared with the instructor import running now in another factory session. So it is not made today; the next factory session makes it with a test, re-sends the 34, and rescores. Expected: each of the 34 moves from 88 to about 92, because short paragraphs is one of only two tests they fail.

## 4. Scores (Rank Math, read from each editor with score_run.py, nothing saved)
16 at 90 or above, 34 at 88, none under 86. **Each of the 34 at 88 fails exactly two tests: short paragraphs and keyword in the address** (addresses are never re-slugged). Read with the S187 per-test reader on the primary keyword.

| record | post | score | failing tests |
|---|---|---|---|
| progress-member-achologist | 10012 | 88 | short paragraphs; keyword in address |
| have-retake-code-ethics-training-every | 10023 | 88 | short paragraphs; keyword in address |
| achology-code-character-conduct-ccac | 10026 | 88 | short paragraphs; keyword in address |
| achology-s-character-code-based-aristotle | 10031 | 88 | short paragraphs; keyword in address |
| commit-practising-achologist | 10038 | 88 | short paragraphs; keyword in address |
| standards-apply-trainee-achologists | 10039 | 88 | short paragraphs; keyword in address |
| course-included-free-membership-happens-when | 10042 | 88 | short paragraphs; keyword in address |
| any-achology-courses-appear-more-than | 10046 | 88 | short paragraphs; keyword in address |
| host-own-achology-event | 10050 | 88 | short paragraphs; keyword in address |
| how-long-achology-refund-process | 237 | 88 | short paragraphs; keyword in address |
| achology-change-mind-after-14-day-guarantee | 238 | 88 | short paragraphs; keyword in address |
| is-achology-a-university | 253 | 88 | short paragraphs; keyword in address |
| is-achology-educational-provider-or-professional-body | 254 | 88 | short paragraphs; keyword in address |
| psychology-as-practical-wisdom | 267 | 88 | short paragraphs; keyword in address |
| achology-certificates-vs-university-degrees | 291 | 88 | short paragraphs; keyword in address |
| achology-courses-cpd-hours | 296 | 88 | short paragraphs; keyword in address |
| evidence-cpd-learning-progression-achology | 299 | 88 | short paragraphs; keyword in address |
| achology-course-outcomes | 310 | 88 | short paragraphs; keyword in address |
| what-if-achology-courses-dont-work | 312 | 88 | short paragraphs; keyword in address |
| call-myself-certified-achology-credentials | 316 | 88 | short paragraphs; keyword in address |
| achology-career-change-coaching-mentoring | 325 | 88 | short paragraphs; keyword in address |
| completed-achology-course-nothing-changed | 339 | 88 | short paragraphs; keyword in address |
| achology-membership-free-coaching-included | 346 | 88 | short paragraphs; keyword in address |
| achology-discussion-spaces-groups-events | 348 | 88 | short paragraphs; keyword in address |
| achology-live-events-types | 350 | 88 | short paragraphs; keyword in address |
| achology-course-required-attend-workshops | 355 | 88 | short paragraphs; keyword in address |
| achology-recommended-practice-pathway | 356 | 88 | short paragraphs; keyword in address |
| achology-members-host-workshops-events | 359 | 88 | short paragraphs; keyword in address |
| how-to-join-live-achology-community-event | 373 | 88 | short paragraphs; keyword in address |
| achology-trust-legal-policies-work-together | 390 | 88 | short paragraphs; keyword in address |
| achology-course-piracy-copyright | 393 | 88 | short paragraphs; keyword in address |
| achology-community-rules-moderation | 409 | 88 | short paragraphs; keyword in address |
| does-achology-offer-partnerships-collaborations | 413 | 88 | short paragraphs; keyword in address |
| become-instructor-contribute-content-achology | 414 | 88 | short paragraphs; keyword in address |
| what-does-achology-expect-from-learners | 269 | 91 | not read |
| achologist-adept | 10010 | 93 | not read |
| achology-knowledge-hub-free-read | 10057 | 93 | not read |
| achology-discounts-sales-promotions | 230 | 93 | not read |
| achology-membership-refund | 240 | 93 | not read |
| achology-access-all-areas-pass | 245 | 93 | not read |
| achology-evidence-based-humanistic-psychology | 275 | 93 | not read |
| achology-course-prerequisites-requirements | 331 | 93 | not read |
| achology-coaching-competency-review-sessions | 353 | 93 | not read |
| achology-certification-practice-competence | 358 | 93 | not read |
| achology-automated-decision-making-profiling | 386 | 93 | not read |
| achology-copyright-sharing-course-content | 394 | 93 | not read |
| achology-courses-other-languages | 412 | 93 | not read |
| achology-media-press-interview-requests | 416 | 93 | not read |
| dimap-course-upgrade | 10048 | 100 | not read |
| first-course-complete-beginner | 399 | 100 | not read |

The per-test reading ran on the 34 under 90 only; the 16 at 90 or above were not read test by test.

## 5. Also this session, for the record
- **The old quote card set (275, 74.3 MB) is not dead weight.** These are the live Download pictures of 275 quote pages on the old card design (SESSION_REPORT__S184 item 2 already says so), so binning them would break those pages' downloads. It stays on Backlog: Code line 32 as a theme re-bake; the media stop will clear when it is done. Nothing was binned.
- **The five anxiety articles** were already published by the S192 factory session; item 3 of that ruling (tools from 90 to 86, with tests) is still owed.
- **The eight resisting change quote pages** are with their own factory session (quote-eight-import). It found that the importer matches by address, which would have made seven duplicates, and that CQ001-043-1 is not on the build site at all.

OWED BACK: the ruling on the 34 (importer fix, recommended) and on the two Achology-only answers.

*No em or en dashes in this file; checked before writing.*
