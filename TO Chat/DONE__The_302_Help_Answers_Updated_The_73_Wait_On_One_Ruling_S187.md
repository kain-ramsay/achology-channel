**For Chat. What this needs from you:** rule on the 73 new answers (ASK__The_73_New_Help_Answers_Still_Fail_Two_Gate_Lines_The_Ruling_Did_Not_Name_S187); start the item 4 writing session (NOTE__The_Help_Answer_Rank_Math_Failures_CSV_Exists_S187); word the two fields named in section 3. Factory session.

# DONE: the 302 Help answers on the build site carry their re-signed records; the 73 new ones wait on one ruling (Code, S187 factory session, 27 October 2026)

Answers RULING__The_Help_Answer_Import_Section_5_Six_Rulings_S446, NOTE__The_Ten_Help_Answers_Mended_At_Source_S446, the Help rows of BRIEF__Import_The_127_Pages_Re_Signed_With_Full_Course_Links_S447 and BRIEF__Import_The_11_Pages_With_Prices_And_Counts_Removed_S447, NOTE__Structured_Training_Is_Never_Written_Three_Help_Answers_To_Update_S446, BRIEF__No_Working_Note_Reaches_An_Article_Locks_4_And_5_S447, and the Help half of RULING__Signed_Pages_Take_Their_Title_From_Post_Title_Drop_The_Old_Headline_S446. Every record was read as it stands today. `body_guard.py --signed` exited 0 before any write and again after the record edits (1,009 records, no working note).

## 1. What reached the build site
- **302 Help answers updated in place**, every one that has a post (the 286 of S180 plus the 15 held or refused and one more), all still published; none created, none published, none unpublished.
  - 298 through the theme's `article_body_update.py --apply --with-seo`: body, excerpt where the record has one, SEO title and description. As each body went, its course autolink wrote full-name links into 9 records (links only, 17 lines; committed).
  - The 4 answers about Achology only (section 2, item 2) whole, through `import_help_answers.py --update`, because the body tool refuses a body with no outside link.
  - Title, focus keyword and secondary keywords on all 302 through `import_help_answers.py --update` (section 2, item 6).
- **Read back:** `import_help_answers.py --verify`: title, SEO title, SEO description and focus keyword (with its secondaries) match the record on all 302. `article_body_update.py --verify` (publish_gate.rendered_faults) on all 302: 298 clean; the 4 Achology-only answers print only "no external link", which item 2 allows.
- **Two read-back differences that are not this job's, listed so they are not mistaken for faults:** 341 Help records carry no `post_excerpt` field, so 184 pages keep their older excerpt; and 58 pages carry two Help categories on the install where their record names one.

## 2. The records under each ruling item
**Item 1, the 73 new answers: not created.** The accept list is built (the two named lines, these 73 only, each recorded as `exception, 2026-10-26, signed prose not reworded (Kain S180), approved by Kain`); the "(opening)" instrument line is fixed in `content_gate.py`; the stances field was already filled on all 73 and passes. Two lines you did not name still refuse them: paragraph sentence counts (70) and seven words shared with another record (73). The second is live only because `content_gate.py` can see Content Records again after its S434 repoint. Asked in ASK__The_73_New_Help_Answers_Still_Fail_Two_Gate_Lines_The_Ruling_Did_Not_Name_S187, with the 73 listed line by line. The CBT exemplar is among them and waits with them. This also holds the 32 Help rows of the 127 brief that are among the 73.

**Item 2, the 15 held or refused: all 15 updated and read back.**
- The 4 about Achology only: cips-when-need-them, difference-between-monthly-annual-achology-membership, using-achology-content-branding-materials, valts-achology. Each record now says so in a new `outside_link` field ("none: an answer about Achology only ..."), and the importer lets a missing outside link through only on that field.
- best-browsers-devices-achology-community: the one stray "[" removed, nothing else.
- The 10 mended at source (your NOTE): achology-course-order-sequence, any-achology-courses-appear-more-than, become-a-master-achologist, can-life-coaches-use-cbt, how-much-does-achology-cost, nhs-routes-into-cbt, senior-achologist-two-levels, train-in-nlp-and-hypnosis-together, where-can-i-learn-about-viktor-frankl (address viktor-frankl-course), where-can-i-learn-drama-triangle (address drama-triangle-training).

**Item 3, the two stage 5 lines: corrected for the help type only** in `stage5_import_checks.py` (an empty `sections` map means headings are free; the picture is read from the body). Re-run on all 375 with the build site's picture list: checks 2 and 3 pass all 73 new records. 249 older records fail check 2 for having no Sourcing record or Search and Citation Brief section (an older record shape, outside this ruling), and what-is-achology carries no picture line.

**Item 4: the CSV exists** (NOTE__The_Help_Answer_Rank_Math_Failures_CSV_Exists_S187): 251 of the 302 under 90.

**Item 5:**
- "the": 15 added on 14 lines in six records: dimap-course-upgrade (2 lines), first-course-complete-beginner, where-can-i-learn-about-albert-ellis, where-can-i-learn-abraham-maslow (2), which-courses-included-each-school-bundle (7), is-psychology-hard-to-learn (1, "Reflective exercises in the Diploma ...", which the NAMES file had not listed). One line in dimap-course-upgrade also took "The" at its start, where the full name opens a sentence.
- Page fields to the full name: dimap-course-upgrade `post_title` ("the DiMAP Course Upgrade", DSRD 4 section 1.1b), with the body's own headline copy matched to it; first-course-complete-beginner `rm_seo_description`; skilled-helper-course `rm_focus_keyword` and `rm_seo_title`.
- "DiMAP Course Upgrade" is in `product_name_check.py`'s accepted names with its source; the check reads 0 short names across 375.
- Pictures: the 17 per-answer pictures corrected to their category picture (achology-live-practice... is not among them: see section 3).

**Item 6: secondary keywords on all 302**, the record's `query_variants` up to four after the focus keyword (52 of the 302 carry variants), never in the body. The row is copied into the PACK_04 kit in The Machine as `secondary_keywords`.

## 3. Fields over their limit, and other findings for Chat to word or rule
- **first-course-complete-beginner `rm_seo_description`: 265 characters (limit 155)** with the three full names, and it is on the build site at that length. It also carries "$97 to $299".
- **skilled-helper-course `rm_seo_title`: 85 characters (limit 60).** Its focus keyword is now "The Skilled Helper Training Course (with Prof. Gerard Egan)", so the gate also fails keyword in address, in the SEO title's first 50 characters and in the description. This record is one of the 73 and is not on the build site.
- dimap-course-upgrade `rm_seo_description` still reads "The DiMAP course upgrade ... for $399"; item 5 named only its title.
- achology-live-practice-session-etiquette (community-and-conduct) names the learning-experience picture: another category's picture rather than its own, so it was left as it is.
- The theme's `article_body_update.py` drops a record's first-line headline only when it matches `post_title`; the title ruling says whatever its words. The gate now drops it for help answers whatever its words; the body tool is a theme file and is unchanged, so a mismatched headline is still refused there (it was, once, on dimap-course-upgrade, before its copy was matched).

## 4. The title ruling (owed line)
On every Help answer updated this session the body's first-line headline was dropped and the page title is `post_title`; no page was refused for it in the run that wrote the pages.

## 5. Structured training (owed line)
The three pages carry their new sentences, read back from the served pages: is-a-life-coaching-certification-worth-it (the doubled sentence once), life-coach-with-psychology-degree, there-free-achology-membership-include. "structured training" is in `content_gate_standards.json`'s always-banned phrases at project commit 4dbca50b; no Help record uses it.

## 6. Locks 4 and 5 (owed count)
- **Lock 4:** `body_guard.py --signed` ran before the work and after the record edits, exit 0 both times. The Help importer, the body tool and the publish gate all read a body with `content_gate.extract_body()` and refuse through `content_gate.machinery_in_body()`; none carries its own pattern list.
- **Lock 5: 1,143 published pages read on the build site, one a second; 0 carry a working note in their reading text.** One published page, /cards/, answers 404. Every Help page's source carries an HTML comment naming "DSRD 1 §9" beside the breadcrumb, which no reader sees.

## 7. Tools changed (all committed and pushed; no gate rule loosened)
- `content_gate.py`: the Standard, the question bank and Content Records repointed to the S434 folders (owed by NOTE__The_Rename_Is_Done_The_Machine_Scripts_To_Repoint_Before_Any_Run_S434, this script only); the help answer's subject note and headline come off before the gate reads it.
- `stage5_import_checks.py`, `product_name_check.py`, `content_gate_standards.json`: as in section 2 and 5.
- `import_help_answers.py`: the item 1 accept list, the item 2 field, item 6 secondaries, and an `--update` route with no status key. Its H9 register entry is re-hashed after the whole diff was read (theme commit 6d387410).
- Still pointing at the old folders and not touched: `content_gate_fixtures.py` (it fails to start) and the other scripts the S434 rename note lists.

## 8. The score table: 302 pages
Read from each page's editor with score_run.py's session, nothing saved. 22 at 95 or above, 29 at 90 to 94, 215 at 80 to 89, 36 under 80; median 84.

| Page (address name) | Post | Score |
|---|---|---|
| first-course-complete-beginner | 399 | 100 |
| no-credential-inflation-achology | 272 | 100 |
| which-courses-included-each-school-bundle | 10045 | 100 |
| accredited-nlp-certification | 39300 | 96 |
| achology-school-bundles-how-they-work | 246 | 96 |
| cheap-counselling-courses | 39309 | 96 |
| choose-a-good-life-coaching-course | 39311 | 96 |
| free-mindfulness-course | 39512 | 96 |
| how-long-achology-keeps-personal-data | 384 | 96 |
| how-much-do-achology-coaches-earn | 326 | 96 |
| how-much-does-achology-cost | 220 | 96 |
| is-a-mindfulness-qualification-worth-it | 39513 | 96 |
| is-achology-therapy-counselling-or-coaching | 224 | 96 |
| is-nlp-certification-legit | 39326 | 96 |
| learn-cbt-for-free | 39327 | 96 |
| learn-mindfulness-course-book-or-app | 39514 | 96 |
| life-coach-or-a-therapist | 39328 | 96 |
| life-coach-with-psychology-degree | 39329 | 96 |
| nlp-certification-levels | 39336 | 96 |
| offer-free-coaching-someone-outside-achology | 10020 | 96 |
| revisit-achology-courses-after-completion | 333 | 96 |
| where-should-i-start-with-achology | 397 | 96 |
| difference-between-certificate-completion-certificate-achievement | 10024 | 93 |
| albert-ellis-course | 38519 | 91 |
| are-counsellors-in-demand | 39301 | 91 |
| are-counsellors-regulated | 39302 | 91 |
| become-a-certified-life-coach | 39303 | 91 |
| become-a-life-coach-for-free | 39304 | 91 |
| become-a-master-achologist | 360 | 91 |
| best-counselling-courses | 39305 | 91 |
| character-traits-define-achologist | 10033 | 91 |
| coaching-hot-seat | 10052 | 91 |
| coaching-vs-counselling-credentials-difference | 305 | 91 |
| counselling-or-psychology | 39313 | 91 |
| counselling-placements | 39314 | 91 |
| counsellor-without-a-degree | 39316 | 91 |
| does-achology-provide-crisis-support | 252 | 91 |
| drama-triangle-training | 38522 | 91 |
| is-a-life-coaching-certification-worth-it | 39323 | 91 |
| is-life-coaching-legit | 39324 | 91 |
| is-life-coaching-regulated | 39325 | 91 |
| maslows-hierarchy-of-needs-course | 38521 | 91 |
| mindfulness-courses-which-one-to-take | 39515 | 91 |
| nlp-certification-online | 39337 | 91 |
| personal-progress-checklist-count-official-cpd | 10022 | 91 |
| principle-led-education-achology | 263 | 91 |
| set-up-achology-community-profile | 376 | 91 |
| study-cbt-online | 39338 | 91 |
| train-in-nlp-and-hypnosis-together | 39339 | 91 |
| viktor-frankl-course | 38520 | 91 |
| what-makes-achology-different | 281 | 91 |
| achologist-title-without-membership | 308 | 88 |
| achology-accessibility-requirements | 277 | 88 |
| achology-discussion-boundary-feels-unsafe | 410 | 88 |
| achology-on-udemy-should-i-join-achology | 279 | 88 |
| achology-skill-development-workshops | 352 | 88 |
| achology-teaching-philosophy | 258 | 88 |
| achology-updates-course-already-purchased | 389 | 88 |
| ask-questions-achology-community | 407 | 88 |
| ccac-green-red-status-mean | 10030 | 88 |
| difference-between-code-ethics-ccac-community | 10028 | 88 |
| how-long-achology-operating | 256 | 88 |
| how-to-participate-achology-discussions-events | 347 | 88 |
| is-achology-content-scientific-or-ideological | 323 | 88 |
| key-milestones-achology-s-history | 10055 | 88 |
| manage-achology-community-notifications | 377 | 88 |
| membership-payment-fails-achology | 247 | 88 |
| navigate-achology-community-guide | 404 | 88 |
| nine-ccac-virtues | 10027 | 88 |
| prior-qualifications-needed-achology | 402 | 88 |
| share-my-achology-account-login | 392 | 88 |
| using-achology-content-branding-materials | 417 | 88 |
| what-is-applied-psychology-achology | 259 | 88 |
| what-personal-data-achology-collects | 381 | 88 |
| who-runs-achology | 273 | 88 |
| why-pay-achology-when-free-content-exists | 282 | 88 |
| achologist-led-tutorials-alts | 351 | 87 |
| achology-certificates-recognised-internationally | 306 | 87 |
| achology-course-order-sequence | 401 | 87 |
| achology-customer-legal-rights-uk-consumer-law | 387 | 87 |
| achology-free-trial-introductory-offer | 226 | 87 |
| achology-knowledge-hub | 10056 | 87 |
| achology-live-practice-session-etiquette | 337 | 87 |
| achology-mentorship-vs-coaching-difference | 343 | 87 |
| achology-password-reset-email-not-arriving | 364 | 87 |
| achology-peer-learning-community-teaches | 335 | 87 |
| achology-vs-icf-coaching-certification | 288 | 87 |
| achology-vs-mindvalley-comparison | 283 | 87 |
| achology-vs-school-of-life-comparison | 287 | 87 |
| achology-vs-therapy-training-counselling | 289 | 87 |
| achology-vs-tony-robbins-comparison | 286 | 87 |
| achology-vs-udemy-psychology-courses | 280 | 87 |
| achology-vs-university-psychology | 222 | 87 |
| adult-to-adult-learning-no-hand-holding | 268 | 87 |
| can-a-life-coach-help-with-anxiety | 39306 | 87 |
| can-achology-replace-university-degrees | 313 | 87 |
| cancel-achology-membership-anytime | 239 | 87 |
| cant-see-achology-course-space-community | 368 | 87 |
| cbt-course-levels-and-diplomas | 39308 | 87 |
| cpd-journey-after-leaving-achology | 301 | 87 |
| delete-achology-account-and-data | 385 | 87 |
| dimap-course-upgrade | 10048 | 87 |
| direct-message-achology-members | 379 | 87 |
| do-achology-courses-get-updated | 219 | 87 |
| does-achology-offer-a-money-back-guarantee | 221 | 87 |
| does-achology-sell-personal-data | 382 | 87 |
| download-achology-community-app | 375 | 87 |
| download-achology-course-materials | 328 | 87 |
| how-achology-courses-work-self-paced | 329 | 87 |
| icf-accredited-life-coaching-programs | 39322 | 87 |
| is-achology-accredited-somap | 295 | 87 |
| is-achology-right-emotionally-vulnerable | 340 | 87 |
| is-achology-suitable-for-beginners | 396 | 87 |
| kain-ramsay-udemy-vs-achology-courses | 278 | 87 |
| life-coaching-as-a-career | 39330 | 87 |
| life-coaching-certification-online | 39331 | 87 |
| life-coaching-experience | 39332 | 87 |
| many-ccac-sessions-need-complete-often | 10029 | 87 |
| membership-first-or-course-first | 398 | 87 |
| nhs-routes-into-cbt | 39334 | 87 |
| pay-instalments-achology-courses | 341 | 87 |
| realistic-outcomes-with-achology | 309 | 87 |
| refund-course-complimentary-membership-cancel-too | 10043 | 87 |
| seven-schools-achology-curriculum-explained | 411 | 87 |
| study-multiple-achology-courses-simultaneously | 334 | 87 |
| supervision-after-achology-training | 317 | 87 |
| there-free-achology-membership-include | 10040 | 87 |
| what-does-achology-membership-include | 243 | 87 |
| which-achology-company-am-actually-contracting | 10053 | 87 |
| which-achology-events-earn-accreditation-credit | 10049 | 87 |
| who-does-achology-share-personal-data-with | 383 | 87 |
| who-verifies-achology-cpd-claims | 10021 | 87 |
| why-achology-avoids-diagnostic-labels | 270 | 87 |
| why-achology-criticizes-psychology-teaching | 276 | 87 |
| why-achology-emphasises-personal-responsibility | 265 | 87 |
| achology-code-ethics | 10034 | 84 |
| achology-content-offensive-emotionally-challenging | 338 | 84 |
| achology-disagreement-open-discussion | 405 | 84 |
| achology-refund-policy-explained | 235 | 84 |
| achology-responsible-community-member-advice | 391 | 84 |
| achology-s-five-community-principles | 10032 | 84 |
| achology-s-nine-value-based-principles | 10036 | 84 |
| achology-success-stories-do-courses-work | 320 | 84 |
| achology-uk-register-learning-providers | 10025 | 84 |
| call-myself-therapist-achology-courses | 298 | 84 |
| cips-when-need-them | 10016 | 84 |
| find-achology-members-similar-interests | 408 | 84 |
| how-psychology-became-institutionalised | 292 | 84 |
| how-to-request-achology-refund | 236 | 84 |
| inside-achology-course-modules-breakdown | 330 | 84 |
| pals-earn-them | 10015 | 84 |
| post-nominal-letters-achology-certificates | 303 | 84 |
| senior-achologist-two-levels | 10011 | 84 |
| seven-marks-maturity-achology-teaches | 10037 | 84 |
| what-achology-certificate-proves | 294 | 84 |
| what-is-achology | 218 | 84 |
| where-is-achology-based | 257 | 84 |
| will-employers-recognise-achology-certificate | 314 | 84 |
| achology-anti-gatekeeping-pricing | 233 | 83 |
| achology-case-study-discussion-groups | 349 | 83 |
| achology-character-development | 322 | 83 |
| achology-invite-link-not-working | 369 | 83 |
| achology-lifetime-access-explained | 225 | 83 |
| achology-peer-learning-culture | 406 | 83 |
| achology-pricing-versus-udemy-universities | 232 | 83 |
| achology-s-ten-value-commitments | 10035 | 83 |
| achology-vs-coursera-psychology-education | 284 | 83 |
| achology-vs-linkedin-learning-comparison | 285 | 83 |
| can-achology-help-personal-struggles | 324 | 83 |
| can-life-coaches-use-cbt | 39307 | 83 |
| cheapest-life-coaching-certification | 39310 | 83 |
| counselling-courses-online | 39312 | 83 |
| counselling-qualification-levels | 39315 | 83 |
| course-completion-vs-competence | 321 | 83 |
| difference-membership-courses-achology | 244 | 83 |
| does-achology-supervise-peer-coaching | 318 | 83 |
| explain-achology-qualifications-to-clients | 307 | 83 |
| how-do-life-coaches-get-clients-and-set-prices | 39317 | 83 |
| how-long-achology-courses-take-timelines | 327 | 83 |
| how-much-do-cbt-therapists-earn | 39318 | 83 |
| how-to-become-a-cbt-coach | 39319 | 83 |
| how-to-become-a-cbt-therapist | 39320 | 83 |
| how-to-become-a-counsellor | 39321 | 83 |
| is-achology-worth-the-money | 231 | 83 |
| manipulative-pricing-tactics-achology-avoids | 271 | 83 |
| masterclasses-vs-practitioner-courses-differences | 332 | 83 |
| need-a-certification-or-a-degree | 39333 | 83 |
| nlp-certification-free | 39335 | 83 |
| principle-based-reflective-discussion | 10878 | 83 |
| self-study-books-vs-achology-courses | 290 | 83 |
| submit-cpd-credit-claim-hosting-attending | 10051 | 83 |
| what-is-a-life-coaching-niche | 39340 | 83 |
| what-is-an-nlp-coach | 39341 | 83 |
| what-law-governs-achology-terms | 388 | 83 |
| who-is-achology-designed-for | 260 | 83 |
| will-counsellors-be-replaced-by-ai | 39342 | 83 |
| will-life-coaches-be-replaced-by-ai | 39343 | 83 |
| achologist-adept | 10010 | 80 |
| achology-access-all-areas-pass | 245 | 80 |
| achology-automated-decision-making-profiling | 386 | 80 |
| achology-certification-practice-competence | 358 | 80 |
| achology-coaching-competency-review-sessions | 353 | 80 |
| achology-copyright-sharing-course-content | 394 | 80 |
| achology-course-prerequisites-requirements | 331 | 80 |
| achology-courses-cpd-hours | 296 | 80 |
| achology-courses-other-languages | 412 | 80 |
| achology-discounts-sales-promotions | 230 | 80 |
| achology-evidence-based-humanistic-psychology | 275 | 80 |
| achology-knowledge-hub-free-read | 10057 | 80 |
| achology-media-press-interview-requests | 416 | 80 |
| achology-membership-refund | 240 | 80 |
| achology-multiple-psychology-traditions | 262 | 80 |
| achology-no-transformation-promises | 234 | 80 |
| achology-payment-methods | 227 | 80 |
| achology-professional-indemnity-insurance | 319 | 80 |
| achology-refund-disagree-course-content | 241 | 80 |
| achology-refund-technical-issues | 242 | 80 |
| achology-s-registered-company-details | 10054 | 80 |
| achology-s-three-learning-paths | 10047 | 80 |
| become-an-achology-affiliate | 415 | 80 |
| best-browsers-devices-achology-community | 371 | 80 |
| build-real-competence-achology | 357 | 80 |
| can-achology-suspend-terminate-access | 251 | 80 |
| cant-log-in-achology-community | 363 | 80 |
| cant-send-receive-messages-achology-community | 367 | 80 |
| choose-right-achology-event-level | 354 | 80 |
| create-posts-achology-community | 378 | 80 |
| downloading-achology-content | 362 | 80 |
| earn-cpd-credit-hosting-session-only | 10017 | 80 |
| find-achology-course-resources | 380 | 80 |
| fix-achology-community-notification-problems | 365 | 80 |
| fix-audio-video-achology-live-sessions | 366 | 80 |
| get-value-achology-mentorship-sessions | 345 | 80 |
| guest-speakers-policy | 395 | 80 |
| have-each-year-keep-master-achologist | 10013 | 80 |
| hidden-fees-additional-costs-achology | 228 | 80 |
| homework-assessment-achology-courses | 403 | 80 |
| how-to-contact-achology-support | 372 | 80 |
| insurance-coverage-achology-qualifications | 304 | 80 |
| is-achology-global-platform | 274 | 80 |
| join-professional-body-after-achology | 302 | 80 |
| long-achology-valts-session | 10018 | 80 |
| many-courses-achology-offer-total | 10044 | 80 |
| many-times-coach-same-person-cips | 10019 | 80 |
| mentoring-opportunities-achology-membership | 342 | 80 |
| mentorship-sessions-recorded-achology | 344 | 80 |
| overwhelmed-by-achology-options | 400 | 80 |
| personal-responsibility-achology-learning | 264 | 80 |
| platform-changes-course-access-achology | 250 | 80 |
| rsvp-join-achology-live-events | 361 | 80 |
| see-real-results-how-long-achology-takes | 311 | 80 |
| share-achology-account-courses | 248 | 80 |
| six-achology-cpd-statuses | 10009 | 80 |
| slow-deep-learning-rejects-fast-certification | 336 | 80 |
| society-lost-gatekeeping-psychology | 293 | 80 |
| transfer-kain-ramsay-udemy-courses-achology | 223 | 80 |
| upgrade-courses-bundle-access-pass | 229 | 80 |
| verify-achology-certificate | 300 | 80 |
| what-does-achology-certification-qualify | 297 | 80 |
| what-does-achology-mean-becoming-wiser | 266 | 80 |
| what-is-circle-achology-community | 374 | 80 |
| what-to-include-achology-support-request | 370 | 80 |
| who-is-achology-not-for | 261 | 80 |
| who-is-kain-ramsay | 255 | 80 |
| why-achology-includes-community-course-prices | 249 | 80 |
| will-clients-take-achology-certificate-seriously | 315 | 80 |
| what-does-achology-expect-from-learners | 269 | 78 |
| achology-career-change-coaching-mentoring | 325 | 75 |
| achology-certificates-vs-university-degrees | 291 | 75 |
| achology-change-mind-after-14-day-guarantee | 238 | 75 |
| achology-code-character-conduct-ccac | 10026 | 75 |
| achology-community-rules-moderation | 409 | 75 |
| achology-course-outcomes | 310 | 75 |
| achology-course-piracy-copyright | 393 | 75 |
| achology-course-required-attend-workshops | 355 | 75 |
| achology-discussion-spaces-groups-events | 348 | 75 |
| achology-live-events-types | 350 | 75 |
| achology-membership-free-coaching-included | 346 | 75 |
| achology-recommended-practice-pathway | 356 | 75 |
| achology-s-character-code-based-aristotle | 10031 | 75 |
| achology-trust-legal-policies-work-together | 390 | 75 |
| any-achology-courses-appear-more-than | 10046 | 75 |
| become-instructor-contribute-content-achology | 414 | 75 |
| call-myself-certified-achology-credentials | 316 | 75 |
| commit-practising-achologist | 10038 | 75 |
| completed-achology-course-nothing-changed | 339 | 75 |
| course-included-free-membership-happens-when | 10042 | 75 |
| does-achology-offer-partnerships-collaborations | 413 | 75 |
| evidence-cpd-learning-progression-achology | 299 | 75 |
| have-retake-code-ethics-training-every | 10023 | 75 |
| host-own-achology-event | 10050 | 75 |
| how-long-achology-refund-process | 237 | 75 |
| how-to-join-live-achology-community-event | 373 | 75 |
| is-achology-a-university | 253 | 75 |
| is-achology-educational-provider-or-professional-body | 254 | 75 |
| progress-member-achologist | 10012 | 75 |
| psychology-as-practical-wisdom | 267 | 75 |
| standards-apply-trainee-achologists | 10039 | 75 |
| what-if-achology-courses-dont-work | 312 | 75 |
| difference-between-monthly-annual-achology-membership | 10041 | 74 |
| achology-members-host-workshops-events | 359 | 71 |
| valts-achology | 10014 | 71 |

OWED BACK: the ruling on the 73; the NOTE once the item 4 records are mended; words for the two fields in section 3.

*No em or en dashes in this file; checked before writing.*
