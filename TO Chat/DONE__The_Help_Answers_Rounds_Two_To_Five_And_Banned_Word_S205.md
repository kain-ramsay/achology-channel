**For Chat. What this needs from you:** two small things. A `post_excerpt` value for HELP__achology-uk-register-learning-providers, whose build site excerpt still reads "Achology holds UKRLP registration" because its record carries no excerpt to send (section 2). And a mend for achology-s-character-code-based-aristotle at 88 (section 3). Factory session, Code S205.

# DONE: the Help answers of rounds two to five and the 94 without the banned word are on the build site (Code, factory S205, a side session of S203, 1 to 2 November 2026)

Answers BRIEF__Import_The_198_Help_Answers_Lifted_For_Rank_Math_Rounds_Two_To_Five_S450, its dated paragraph included, on Kain's order of 1 November 2026. Route followed: TO Chat/DONE__The_50_Help_Answers_Lifted_For_Rank_Math_Updated_And_Rescored_S194 (`article_body_update.py --apply --with-seo`).

**The count.** Batches `rankmath_help_r2` to `r5` list 200 records. Less the two the brief leaves out (HELP__cips-when-need-them, HELP__what-is-achology), that is 198. Plus the 94 of `banned_holds_help_answers_s450`, 39 of them shared, which makes **253 distinct records, each imported once from its current record.** All 253 were already on the build site and published, so none was created.

## 1. The import checks

- **Fields complete and signed.** Each record was read against the help-answer standard's required fields (content_gate_standards.json: post_title, post_name, address, help_category, rm_seo_title, rm_seo_description, reviewed_by): 253 of 253 complete and signed by Kain. As sent: 159 carry the rounds two to five signature; 80 carry the later banned word signature; and 14 carry the signature Kain gave this morning, 2 November, for BRIEF__Update_26_Hub_Questions_And_32_Help_Answers_Lifted_For_Rank_Math_S451 (those 14 are in the banned word part of this brief, and Chat re-signed them at 09:00, before this run sent anything at 09:01). (The generic `stage5_import_checks.py` reads the article field list, which a Help answer does not carry, so its fails are not counted here.)
- **Body shape.** `body_guard.py --signed`: 1,118 records, 0 with a working note in the body.
- **Every link resolves.** 351 site addresses. 293 are published pages, read from the server's own list. 58 are not posts; read one a second from inside the host, 18 answer 200 (the Help category pictures and theme pages), 4 answer 301 (tag pages), and 36 answer 404. The 36 are pages not yet built on the build site: the course and school pages under /academy/, and /membership/, /certification/, /accreditation/, /access-all-areas/, /free-events/ and /free-coaching/. So they are pages to come, not broken links. 128 outside links: 102 answer below 400. The other 26 are sites that refuse scripts, mostly coachingfederation.org, bls.gov, open.ac.uk and open.edu (403), plus two that did not connect from here (taster.cpcab.co.uk, curriculum.maastrichtuniversity.nl). Nothing held for a link.

## 2. Landed

- **252 sent at the first pass,** `article_body_update.py --apply --with-seo`: body, excerpt where the record carries one, search title and search description. 0 refused at send, 0 failed. All stay published.
- **One held, then landed: using-achology-content-branding-materials.** The body tool refused it for having no outside link. It is an answer about Achology only, the case RULING__Two_Achology_Only_Help_Answers_Keep_No_Outside_Link_S450 rules on. So it went once the tool carried that allowance (item 6, theme commit e2a3e44f; its own line is in TO Chat/DONE__Three_Small_Rulings_Book_Note_Titles_Help_Links_Publisher_Links_S205.md).
- **Read back** with `--verify` (publish_gate.rendered_faults): 252 of 253 clean. The one is using-achology-content-branding-materials, read as having "no external link". That is the allowance above, the publish gate's own check not yet carrying it.
- **The banned word.** WordPress's own search across every published Help answer for "holds" finds one: achology-uk-register-learning-providers (post 10025). The word is in its excerpt, "Yes: Achology holds UKRLP registration, PRN 10099815, with CPD independently verified through SoMAP.", and the record carries no `post_excerpt`, so the update had nothing to replace it with. Its body's one remaining form, "someone holding a training budget", is an everyday use the plan keeps. **Needed from Chat:** the record's `post_excerpt`, then Code sends it.
- No record was changed by the run (no course link was written).

## 3. Scores (bar 90 for Help answers), read by `score_run.py`; failing tests by the per-test reader; nothing saved

**252 pass, 1 under.** 104 read 100, 41 read 96, 106 read 93, 1 reads 91. The one under: achology-s-character-code-based-aristotle (post 10031) at 88, failing keywordIn10Percent and keywordInPermalink. Its phrase, "character code based on Aristotle", is not in the opening tenth, and it is not in the address (addresses are not moved without a ruling).

| Page (address name) | Post | Focus phrase | Signature | Score | Against 90 | Failing tests |
|---|---|---|---|---|---|---|
| achologist-led-tutorials-alts | 351 | achologist-led tutorials (alts) | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-anti-gatekeeping-pricing | 233 | Achology anti-gatekeeping pricing | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-case-study-discussion-groups | 349 | case study discussion group | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-certificates-recognised-internationally | 306 | achology certificates recognised internationally | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-character-development | 322 | achology character development | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-course-order-sequence | 401 | achology course order | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-customer-legal-rights-uk-consumer-law | 387 | Achology customer legal rights | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-free-trial-introductory-offer | 226 | Achology free trial introductory offer | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-invite-link-not-working | 369 | achology invite link not working | banned word (94) | 100 | pass | not read (at or over the bar) |
| achology-knowledge-hub | 10056 | achology knowledge hub | banned word (94) | 100 | pass | not read (at or over the bar) |
| achology-live-practice-session-etiquette | 337 | achology live practice session etiquette | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-mentorship-vs-coaching-difference | 343 | mentorship vs coaching | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-password-reset-email-not-arriving | 364 | achology password reset email not arriving | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-peer-learning-community-teaches | 335 | achology peer learning community | banned word (94) | 100 | pass | not read (at or over the bar) |
| achology-peer-learning-culture | 406 | achology peer learning culture | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-s-ten-value-commitments | 10035 | ten value commitments | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-vs-coursera-psychology-education | 284 | achology vs coursera | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-vs-linkedin-learning-comparison | 285 | achology vs linkedin learning | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-vs-mindvalley-comparison | 283 | achology vs mindvalley | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-vs-school-of-life-comparison | 287 | achology vs school of life | banned word (94) | 100 | pass | not read (at or over the bar) |
| achology-vs-therapy-training-counselling | 289 | achology vs therapy | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-vs-tony-robbins-comparison | 286 | achology vs tony robbins | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-vs-university-psychology | 222 | Achology vs university psychology | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| best-online-psychology-course | 41435 | best online psychology course | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| can-a-life-coach-help-with-anxiety | 39306 | life coach help with anxiety | banned word (94) | 100 | pass | not read (at or over the bar) |
| can-achology-help-personal-struggles | 324 | help personal struggles | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| can-achology-replace-university-degrees | 313 | achology replace university | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| can-life-coaches-use-cbt | 39307 | can life coaches use cbt | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| cancel-achology-membership-anytime | 239 | cancel Achology membership anytime | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| cant-see-achology-course-space-community | 368 | see achology course | banned word (94) | 100 | pass | not read (at or over the bar) |
| cbt-course-levels-and-diplomas | 39308 | cbt course levels and diplomas | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| cbt-practitioner-vs-cbt-therapist | 41437 | cbt practitioner | banned word (94) | 100 | pass | not read (at or over the bar) |
| cheapest-life-coaching-certification | 39310 | cheapest life coaching certification | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| counselling-courses-online | 39312 | counselling courses online | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| counselling-qualification-levels | 39315 | counselling qualification levels | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| course-completion-vs-competence | 321 | course completion vs competence | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| cpd-journey-after-leaving-achology | 301 | after leaving achology | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| delete-achology-account-and-data | 385 | Achology account and data | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| direct-message-achology-members | 379 | message achology members | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| do-achology-courses-get-updated | 219 | achology courses get updated | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| does-achology-offer-a-money-back-guarantee | 221 | achology offer a money-back guarantee | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| does-achology-sell-personal-data | 382 | Achology sell personal data | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| does-achology-supervise-peer-coaching | 318 | achology supervise peer coaching | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| download-achology-course-materials | 328 | download achology course materials | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| explain-achology-qualifications-to-clients | 307 | explain achology qualifications to clients | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| how-achology-courses-work-self-paced | 329 | how achology courses work | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| how-do-life-coaches-get-clients-and-set-prices | 39317 | life coaches get clients | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| how-long-achology-courses-take-timelines | 327 | how long achology courses take | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| how-much-do-cbt-therapists-earn | 39318 | how much do cbt therapists earn | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| how-to-become-a-cbt-coach | 39319 | how to become a cbt coach | banned word (94) | 100 | pass | not read (at or over the bar) |
| how-to-become-a-cbt-therapist | 39320 | how to become a cbt therapist | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| how-to-become-a-counsellor | 39321 | how to become a counsellor | banned word (94) | 100 | pass | not read (at or over the bar) |
| how-to-start-learning-cbt | 41448 | how to start learning cbt | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| icf-accredited-life-coaching-programs | 39322 | icf accredited life coaching | banned word (94) | 100 | pass | not read (at or over the bar) |
| is-a-mindfulness-qualification-worth-it | 39513 | mindfulness qualification | banned word (94) | 100 | pass | not read (at or over the bar) |
| is-achology-accredited-somap | 295 | achology accredited | banned word (94) | 100 | pass | not read (at or over the bar) |
| is-achology-right-emotionally-vulnerable | 340 | emotionally vulnerable | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| is-achology-suitable-for-beginners | 396 | Achology suitable for beginners | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| is-achology-worth-the-money | 231 | achology worth the money | banned word (94) | 100 | pass | not read (at or over the bar) |
| learn-hypnotherapy-online-or-free | 41459 | learn hypnotherapy online | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| learn-psychology-for-free-online | 41460 | learn psychology for free | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| learn-psychology-on-your-own | 41461 | learn psychology on your own | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| life-coach-with-psychology-degree | 39329 | psychology degree | banned word (94) | 100 | pass | not read (at or over the bar) |
| life-coaching-as-a-career | 39330 | life coaching as a career | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| life-coaching-certification-online | 39331 | life coaching certification online | banned word (94) | 100 | pass | not read (at or over the bar) |
| life-coaching-experience | 39332 | life coaching experience | banned word (94) | 100 | pass | not read (at or over the bar) |
| manipulative-pricing-tactics-achology-avoids | 271 | manipulative pricing tactics achology avoids | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| many-ccac-sessions-need-complete-often | 10029 | CCaC sessions | banned word (94) | 100 | pass | not read (at or over the bar) |
| membership-first-or-course-first | 398 | membership first or course first | banned word (94) | 100 | pass | not read (at or over the bar) |
| need-a-certification-or-a-degree | 39333 | certification or a degree | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| nhs-routes-into-cbt | 39334 | nhs routes into cbt | banned word (94) | 100 | pass | not read (at or over the bar) |
| nlp-certification-free | 39335 | nlp certification free | banned word (94) | 100 | pass | not read (at or over the bar) |
| principle-based-reflective-discussion | 10878 | principle-based reflective discussion | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| realistic-outcomes-with-achology | 309 | realistic outcomes with achology | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| refund-course-complimentary-membership-cancel-too | 10043 | course complimentary membership | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| self-study-books-vs-achology-courses | 290 | books vs achology courses | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| seven-schools-achology-curriculum-explained | 411 | seven schools Achology | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| should-you-become-a-hypnotherapist | 41469 | should you become a hypnotherapist | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| study-mental-health-online-is-it-worth-it | 41470 | study mental health online | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| study-multiple-achology-courses-simultaneously | 334 | study multiple achology courses | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| study-psychology-by-distance-learning-uk | 41471 | psychology by distance learning | banned word (94) | 100 | pass | not read (at or over the bar) |
| supervision-after-achology-training | 317 | supervision after achology training | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| there-free-achology-membership-include | 10040 | free achology membership | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| train-as-a-mental-health-practitioner-online | 41472 | mental health practitioner online | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| train-as-a-wellbeing-coach-or-practitioner-online | 41473 | train as a wellbeing coach | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| what-can-you-do-with-a-mental-health-certificate | 41476 | mental health certificate | banned word (94) | 100 | pass | not read (at or over the bar) |
| what-do-you-learn-in-behavioural-psychology | 41478 | learn in behavioural psychology | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| what-do-you-learn-in-developmental-psychology | 41480 | learn in developmental psychology | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| what-do-you-learn-in-social-psychology | 41481 | learn in social psychology | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| what-does-achology-membership-include | 243 | achology membership include | banned word (94) | 100 | pass | not read (at or over the bar) |
| what-is-a-life-coaching-niche | 39340 | life coaching niche | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| what-is-an-nlp-coach | 39341 | what is an nlp coach | banned word (94) | 100 | pass | not read (at or over the bar) |
| where-can-you-study-developmental-psychology-online | 41494 | study developmental psychology | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| where-can-you-study-psychoanalysis-online | 41495 | study psychoanalysis | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| where-is-achology-based | 257 | achology based | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| which-achology-company-am-actually-contracting | 10053 | which achology company | banned word (94) | 100 | pass | not read (at or over the bar) |
| which-achology-events-earn-accreditation-credit | 10049 | achology events earn accreditation credit | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| which-courses-included-each-school-bundle | 10045 | each school bundle | banned word (94) | 100 | pass | not read (at or over the bar) |
| who-does-achology-share-personal-data-with | 383 | share personal data | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| who-is-kain-ramsay | 255 | who is kain ramsay | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| who-verifies-achology-cpd-claims | 10021 | who verifies Achology CPD claims | banned word (94) | 100 | pass | not read (at or over the bar) |
| why-achology-criticizes-psychology-teaching | 276 | achology criticizes psychology teaching | banned word (94) | 100 | pass | not read (at or over the bar) |
| will-counsellors-be-replaced-by-ai | 39342 | will counsellors be replaced by ai | banned word (94) | 100 | pass | not read (at or over the bar) |
| will-life-coaches-be-replaced-by-ai | 39343 | will life coaches be replaced by ai | rounds 2 to 5 | 100 | pass | not read (at or over the bar) |
| achology-lifetime-access-explained | 225 | Achology lifetime access explained | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| achology-pricing-versus-udemy-universities | 232 | Achology pricing versus Udemy universities | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| achology-vs-icf-coaching-certification | 288 | achology vs icf coaching certification | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| achology-vs-udemy-psychology-courses | 280 | achology vs udemy psychology courses | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| adult-to-adult-learning-no-hand-holding | 268 | no hand-holding | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| albert-ellis-course | 38519 | albert ellis course | banned word (94) | 96 | pass | not read (at or over the bar) |
| become-a-certified-life-coach | 39303 | become a certified life coach | banned word (94) | 96 | pass | not read (at or over the bar) |
| become-a-life-coach | 41430 | become a life coach | banned word (94) | 96 | pass | not read (at or over the bar) |
| become-a-mental-health-practitioner | 41431 | become a mental health practitioner | banned word (94) | 96 | pass | not read (at or over the bar) |
| cheap-counselling-courses | 39309 | cheap counselling courses | banned word (94) | 96 | pass | not read (at or over the bar) |
| cheapest-hypnotherapy-course | 41438 | cheapest hypnotherapy course | banned word (94) | 96 | pass | not read (at or over the bar) |
| difference-membership-courses-achology | 244 | difference membership courses achology | banned word (94) | 96 | pass | not read (at or over the bar) |
| download-achology-community-app | 375 | download achology community app | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| drama-triangle-training | 38522 | drama triangle training | banned word (94) | 96 | pass | not read (at or over the bar) |
| how-long-does-a-mental-health-course-take | 41443 | mental health course take | banned word (94) | 96 | pass | not read (at or over the bar) |
| how-much-does-achology-cost | 220 | achology cost | banned word (94) | 96 | pass | not read (at or over the bar) |
| how-to-study-psychology-online | 41449 | study psychology online | banned word (94) | 96 | pass | not read (at or over the bar) |
| introduction-to-psychology-course-online | 41452 | introduction to psychology course | banned word (94) | 96 | pass | not read (at or over the bar) |
| is-a-life-coaching-certification-worth-it | 39323 | life coaching certification worth it | banned word (94) | 96 | pass | not read (at or over the bar) |
| is-nlp-certification-legit | 39326 | nlp certification legit | banned word (94) | 96 | pass | not read (at or over the bar) |
| is-psychology-hard-to-learn | 41457 | is psychology hard to learn | banned word (94) | 96 | pass | not read (at or over the bar) |
| kain-ramsay-udemy-vs-achology-courses | 278 | kain ramsay udemy vs achology | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| masterclasses-vs-practitioner-courses-differences | 332 | masterclasses vs practitioner courses | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| nlp-certification-levels | 39336 | nlp certification levels | banned word (94) | 96 | pass | not read (at or over the bar) |
| pay-instalments-achology-courses | 341 | instalments achology courses | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| personal-progress-checklist-count-official-cpd | 10022 | personal progress checklist | banned word (94) | 96 | pass | not read (at or over the bar) |
| principle-led-education-achology | 263 | principle-led education | banned word (94) | 96 | pass | not read (at or over the bar) |
| psychology-course-accreditation-online | 41468 | psychology course accreditation | banned word (94) | 96 | pass | not read (at or over the bar) |
| submit-cpd-credit-claim-hosting-attending | 10051 | cpd credit claim | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| train-in-nlp-and-hypnosis-together | 39339 | nlp and hypnosis | banned word (94) | 96 | pass | not read (at or over the bar) |
| viktor-frankl-course | 38520 | viktor frankl course | banned word (94) | 96 | pass | not read (at or over the bar) |
| want-to-learn-psychology-where-to-start | 41475 | want to learn psychology | banned word (94) | 96 | pass | not read (at or over the bar) |
| what-does-achology-expect-from-learners | 269 | expect from learners | banned word (94) | 96 | pass | not read (at or over the bar) |
| what-does-an-nlp-course-cover | 41486 | what does an nlp course cover | banned word (94) | 96 | pass | not read (at or over the bar) |
| what-is-a-mental-wellbeing-course-who-is-it-for | 41487 | mental wellbeing course | banned word (94) | 96 | pass | not read (at or over the bar) |
| what-law-governs-achology-terms | 388 | achology terms | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| what-you-learn-on-a-mental-health-course | 41489 | on a mental health course | banned word (94) | 96 | pass | not read (at or over the bar) |
| where-can-you-study-social-psychology-online | 41496 | study social psychology | banned word (94) | 96 | pass | not read (at or over the bar) |
| who-is-achology-designed-for | 260 | achology designed for | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| why-achology-avoids-diagnostic-labels | 270 | diagnostic labels | rounds 2 to 5 | 96 | pass | not read (at or over the bar) |
| why-achology-emphasises-personal-responsibility | 265 | personal responsibility | banned word (94) | 96 | pass | not read (at or over the bar) |
| achologist-title-without-membership | 308 | call yourself an achologist | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-accessibility-requirements | 277 | what accessibility support does achology offer | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-code-character-conduct-ccac | 10026 | Achology's CCaC | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-code-ethics | 10034 | Achology Code of Ethics | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-community-rules-moderation | 409 | achology community moderation rules | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-content-offensive-emotionally-challenging | 338 | find achology content offensive | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-course-piracy-copyright | 393 | content on a torrent site | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-disagreement-open-discussion | 405 | achology's approach to open discussion | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-discussion-boundary-feels-unsafe | 410 | achology discussion feels unsafe | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-membership-free-coaching-included | 346 | achology membership include free coaching | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-membership-refund | 240 | Achology membership refund policy | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-multiple-psychology-traditions | 262 | multiple psychology traditions at achology | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-no-transformation-promises | 234 | does Achology promise transformation results | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-on-udemy-should-i-join-achology | 279 | achology course on udemy | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-payment-methods | 227 | what payment methods does achology accept | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-professional-indemnity-insurance | 319 | need achologist indemnity insurance | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-refund-disagree-course-content | 241 | refund for course content | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-refund-policy-explained | 235 | achology's refund policy | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-refund-technical-issues | 242 | refund for technical issues | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-responsible-community-member-advice | 391 | advice from other Achology members | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-s-five-community-principles | 10032 | five principles | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-s-nine-value-based-principles | 10036 | achology's nine value-based principles | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-s-registered-company-details | 10054 | achology's registered company details | banned word (94) | 93 | pass | not read (at or over the bar) |
| achology-s-three-learning-paths | 10047 | achology's three learning paths | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-skill-development-workshops | 352 | skill development workshops at achology | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-success-stories-do-courses-work | 320 | do achology courses work | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-teaching-philosophy | 258 | achology's teaching philosophy | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-uk-register-learning-providers | 10025 | UK Register of Learning Providers | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| achology-updates-course-already-purchased | 389 | Achology updates a course | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| ask-questions-achology-community | 407 | ask a question in achology | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| become-an-achology-affiliate | 415 | join the achology affiliate programme | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| best-browsers-devices-achology-community | 371 | browsers and devices work best | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| build-real-competence-achology | 357 | real competence with Achology | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| call-myself-therapist-achology-courses | 298 | call yourself a therapist | banned word (94) | 93 | pass | not read (at or over the bar) |
| can-achology-suspend-terminate-access | 251 | achology suspend or terminate access | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| cant-log-in-achology-community | 363 | log in to Achology community | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| cant-send-receive-messages-achology-community | 367 | send or receive messages | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| ccac-green-red-status-mean | 10030 | green or red CCaC status | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| choose-right-achology-event-level | 354 | choose the right event | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| create-posts-achology-community | 378 | post in the Achology community | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| difference-between-code-ethics-ccac-community | 10028 | three conduct codes | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| does-achology-offer-partnerships-collaborations | 413 | achology partnerships and collaborations | banned word (94) | 93 | pass | not read (at or over the bar) |
| downloading-achology-content | 362 | download Achology course content | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| earn-cpd-credit-hosting-session-only | 10017 | credit for hosting a session | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| evidence-cpd-learning-progression-achology | 299 | cpd and learning progression | banned word (94) | 93 | pass | not read (at or over the bar) |
| find-achology-course-resources | 380 | resources for your Achology course | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| find-achology-members-similar-interests | 408 | achology members with similar interests | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| fix-achology-community-notification-problems | 365 | fix Achology notification problems | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| fix-audio-video-achology-live-sessions | 366 | audio or camera problems | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| get-value-achology-mentorship-sessions | 345 | most value from mentorship sessions | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| guest-speakers-policy | 395 | achology invite guest speakers | banned word (94) | 93 | pass | not read (at or over the bar) |
| have-each-year-keep-master-achologist | 10013 | maintain master achologist status | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| hidden-fees-additional-costs-achology | 228 | hidden fees or additional costs | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| homework-assessment-achology-courses | 403 | homework in achology courses | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| how-long-achology-operating | 256 | long has achology been operating | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| how-psychology-became-institutionalised | 292 | psychology became institutionalised and gatekept | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| how-to-contact-achology-support | 372 | contact the Achology support | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| how-to-participate-achology-discussions-events | 347 | achology discussions and events | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| how-to-request-achology-refund | 236 | request an Achology refund | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| inside-achology-course-modules-breakdown | 330 | inside an achology course module | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| insurance-coverage-achology-qualifications | 304 | insurance cover for achology qualifications | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| is-achology-content-scientific-or-ideological | 323 | achology scientific or ideology-based | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| is-achology-global-platform | 274 | achology a global learning platform | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| join-professional-body-after-achology | 302 | join a professional body | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| key-milestones-achology-s-history | 10055 | milestones in achology's history | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| long-achology-valts-session | 10018 | VALTS session length | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| manage-achology-community-notifications | 377 | manage your Achology community notifications | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| many-courses-achology-offer-total | 10044 | how many achology courses | banned word (94) | 93 | pass | not read (at or over the bar) |
| many-times-coach-same-person-cips | 10019 | coach the same person for CIPS | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| membership-payment-fails-achology | 247 | Achology membership payment failed | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| mentoring-opportunities-achology-membership | 342 | achology membership mentorship groups | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| mentorship-sessions-recorded-achology | 344 | achology mentorship sessions recorded | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| navigate-achology-community-guide | 404 | navigate the achology community | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| nine-ccac-virtues | 10027 | nine virtues | banned word (94) | 93 | pass | not read (at or over the bar) |
| overwhelmed-by-achology-options | 400 | choosing an achology course | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| pals-earn-them | 10015 | PALS credit | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| personal-responsibility-achology-learning | 264 | achology personal responsibility | banned word (94) | 93 | pass | not read (at or over the bar) |
| platform-changes-course-access-achology | 250 | courses if achology platform changes | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| post-nominal-letters-achology-certificates | 303 | letters after your name | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| prior-qualifications-needed-achology | 402 | qualifications to study at achology | banned word (94) | 93 | pass | not read (at or over the bar) |
| rsvp-join-achology-live-events | 361 | RSVP to Achology events | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| see-real-results-how-long-achology-takes | 311 | honest achology results timeline | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| senior-achologist-two-levels | 10011 | the two senior achologist levels | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| seven-marks-maturity-achology-teaches | 10037 | marks of maturity | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| share-achology-account-courses | 248 | share your Achology account | banned word (94) | 93 | pass | not read (at or over the bar) |
| share-my-achology-account-login | 392 | your Achology account or login | banned word (94) | 93 | pass | not read (at or over the bar) |
| six-achology-cpd-statuses | 10009 | achology cpd member levels | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| slow-deep-learning-rejects-fast-certification | 336 | deep learning over fast certification | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| society-lost-gatekeeping-psychology | 293 | gatekeeping of psychological knowledge | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| transfer-kain-ramsay-udemy-courses-achology | 223 | transfer Udemy course to Achology | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| upgrade-courses-bundle-access-pass | 229 | upgrade to Achology bundle | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| using-achology-content-branding-materials | 417 | achology content or branding | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| verify-achology-certificate | 300 | verify an achology certificate | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| what-achology-certificate-proves | 294 | achology certificate actually prove | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| what-does-achology-certification-qualify | 297 | certification qualify me | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| what-does-achology-mean-becoming-wiser | 266 | becoming wiser at achology | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| what-is-applied-psychology-achology | 259 | applied psychology at achology | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| what-is-circle-achology-community | 374 | what is Circle and why | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| what-personal-data-achology-collects | 381 | personal data does Achology collect | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| what-to-include-achology-support-request | 370 | your Achology support request | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| who-is-achology-not-for | 261 | not designed for | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| who-runs-achology | 273 | who runs achology day-to-day | banned word (94) | 93 | pass | not read (at or over the bar) |
| why-achology-includes-community-course-prices | 249 | why achology includes community access | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| why-pay-achology-when-free-content-exists | 282 | why pay for achology | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| will-clients-take-achology-certificate-seriously | 315 | take your achology certificate seriously | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| will-employers-recognise-achology-certificate | 314 | employers recognise achology certificates | rounds 2 to 5 | 93 | pass | not read (at or over the bar) |
| does-achology-provide-crisis-support | 252 | crisis support | banned word (94) | 91 | pass | not read (at or over the bar) |
| achology-s-character-code-based-aristotle | 10031 | character code based on Aristotle | banned word (94) | 88 | **under** | keywordIn10Percent, keywordInPermalink |

## 4. Shared with the S451 brief

Fourteen of these are also in BRIEF__Update_26_Hub_Questions_And_32_Help_Answers_Lifted_For_Rank_Math_S451. They went from the records as they stood at 09:01 on 2 November, which already carry that brief's signature, so its body, excerpt and search title and description changes for these 14 are on the build site now and scored in the table above. What that brief still owes for them is only its own DONE line. Nothing was sent from an earlier copy.

## Commits

Theme: e2a3e44f (the body tool and its H9 hash, item 6). Project: none. Channel: this DONE and the brief's disposition line.

OWED BACK: the excerpt for achology-uk-register-learning-providers, and a mend for achology-s-character-code-based-aristotle.

*No em or en dashes in this file; checked before writing.*
