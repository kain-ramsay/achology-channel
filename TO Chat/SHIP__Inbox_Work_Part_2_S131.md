> **CHAT DISPOSITION, S382: STAYS, read in full.** All the DONE/REPLY/ASK-answered items read and taken as read-back-clean; nothing further needed on them. Both Kain-facing items are closed: the softening pass turned out to be a new gate line on the 641 pass already running, so it went to Cowork as `ADDENDUM__A_New_Contraction_Check_Joins_The_641_Pass_On_Help_Answers_S382` rather than to Kain; `CQ001-061-1` is answered (import as a draft) in `REPLY__CQ001_061_1_Import_As_Draft_S382` in this tray. One thing still open: Chat's own classification pass on the thinker/model question-mark rows (about 139 entries, the S371 map), not run this session, named as Chat's next item, not blocking. Archive once that is settled.

**Needs from Chat (updated at the S131 close; everything below your S382 line is new since you read it):** (1) rule the six folded redirect rows whose S087 addresses are not in the workbook; (2) rule the 20 keyword register clashes, each a published quote and its old Handbook draft sharing one quote ID; (3) decide whether author biographies and quote pages get score bars of their own (203 pages fail only the site-wide 90); (4) brief Cowork on three copy jobs Code measured: the 33 help answers at 80 (keyword not in the body), the 132 CQ001 practice blocks under 40 words, and the 11 book notes held on the S381 'actually' line; (5) sign or reword one policy line ("We trade plainly and honestly.") in `REPLY__Plainly_Sweep_S131.md`; (6) fold `RECORD__The_Book_Note_Column_Rulings_0_401_To_0_414_S131.md` into DSRD 8 section 31; (7) the Achology Project Instructions file reads DRIFTED against its marker, yours to restamp when finished. Everything else here is done and read back.

# SHIP, part 2: Code's inbox worked through, newest first (Kain, S131)

**From:** Claude Code, S131 (factory session), Wednesday 23 September 2026. **To:** Claude Chat. Part 1 (`SHIP__Inbox_Work_S131.md`) was acted on by Chat's S380 reply; this carries on from it.

### BRIEF__A_Contraction_Check_In_The_Help_Answer_Gate_And_A_Count_Of_The_Live_Help_Bodies_S373: DONE

**Part two, the check, built.** `content_gate.py` with its settings in the help-answer entry of `content_gate_standards.json`: a body with no contraction **fails**; an H2 section with none, and a body whose uncontracted forms (it is, you will, is not, do not, does not, cannot, you are, that is, there is, will not) outnumber its contractions, are **flagged, never failed**. Excluded: link text, quoted titles, canonical course names, the UKRLP line, the Related questions block. privacy-and-legal, refunds-and-billing and pricing-and-payments take the fail line only. A possessive ("Achology's") is not a contraction. Acceptance 135 of 135, 10 new. Proved on the two records named:

```
HELP__cbt-practitioner-vs-cbt-therapist.md
  PASS  contractions: at least one in the body         32 contractions, 0 uncontracted forms
  ..    contractions: sections with none, flagged not gated 0 of 6
  ..    contractions: stiff forms outnumber them, flagged not gated no, 0 to 32
HELP__what-is-achology.md
  FAIL  contractions: at least one in the body         0 contractions, 5 uncontracted forms
  ..    contractions: sections with none, flagged not gated 5 of 5
  ..    contractions: stiff forms outnumber them, flagged not gated yes, 5 to 0
```

**Found and closed on the way:** 29 of Cowork's help records written since S373 carry two working-notes sections of the help-answer skill ("The three next questions a first-time visitor would ask (rule 6)" and "Open before this record is called ready") above their Sourcing record, so the gate and the push tool read them as body. None has reached the install (searched); both headings now end the body.

**Part one, the count,** across the 246 help-answer records on disk (the live 250 less the 33 with no record, plus Cowork's newer records not yet live). No body edited.

    records read: 246
    bodies with no contraction: 156
    bodies where uncontracted forms outnumber contractions: 200
    
    by category (records, with none, contractions, uncontracted forms):
      membership-and-access               11 records,  10 with none,    1 contractions,   52 uncontracted
      achology-basics-and-identity        32 records,  28 with none,    4 contractions,  162 uncontracted
      refunds-and-billing                 10 records,   8 with none,    9 contractions,   54 uncontracted
      privacy-and-legal                   17 records,  13 with none,    7 contractions,   77 uncontracted
      outcomes-and-expectations           17 records,  13 with none,   20 contractions,   82 uncontracted
      community-and-conduct               10 records,   7 with none,    7 contractions,   62 uncontracted
      learning-experience                 13 records,   9 with none,    5 contractions,   51 uncontracted
      partnerships-and-press               3 records,   2 with none,   12 contractions,   14 uncontracted
      technical-help                      14 records,   9 with none,    7 contractions,   90 uncontracted
      events-and-mentorship               28 records,  17 with none,   19 contractions,  146 uncontracted
      certificates-cpd-accreditation      22 records,  13 with none,   52 contractions,   87 uncontracted
      getting-started                     11 records,   5 with none,   46 contractions,   39 uncontracted
      curriculum-and-subjects             17 records,   7 with none,   81 contractions,   34 uncontracted
      comparisons-and-alternatives        28 records,  11 with none,  197 contractions,   72 uncontracted
      pricing-and-payments                13 records,   4 with none,   21 contractions,   40 uncontracted
    
    every body, worst first (contractions, uncontracted forms):
      achology-knowledge-hub-free-read                           achology-basics-and-identity   0  13
      direct-message-achology-members                            technical-help                 0  11
      seven-marks-maturity-achology-teaches                      achology-basics-and-identity   0  11
      there-free-achology-membership-include                     membership-and-access          0  11
      achology-knowledge-hub                                     achology-basics-and-identity   0  10
      course-included-free-membership-happens-when               membership-and-access          0  10
      dimap-course-upgrade                                       curriculum-and-subjects        0  10
      achology-success-stories-do-courses-work                   outcomes-and-expectations      0   9
      ccac-green-red-status-mean                                 community-and-conduct          0   9
      difference-between-certificate-completion-certificate-achievement certificates-cpd-accreditation   0   9
      downloading-achology-content                               technical-help                 0   9
      mentorship-sessions-recorded-achology                      events-and-mentorship          0   9
      set-up-achology-community-profile                          technical-help                 0   9
      share-my-achology-account-login                            privacy-and-legal              0   9
      achology-certification-practice-competence                 events-and-mentorship          0   8
      achology-course-piracy-copyright                           privacy-and-legal              0   8
      achology-course-required-attend-workshops                  events-and-mentorship          0   8
      achology-mentorship-vs-coaching-difference                 events-and-mentorship          0   8
      achology-teaching-philosophy                               achology-basics-and-identity   0   8
      achology-vs-therapy-training-counselling                   comparisons-and-alternatives   0   8
      adult-to-adult-learning-no-hand-holding                    achology-basics-and-identity   0   8
      coaching-vs-counselling-credentials-difference             certificates-cpd-accreditation   0   8
      does-achology-offer-a-money-back-guarantee                 refunds-and-billing            0   8
      have-retake-code-ethics-training-every                     certificates-cpd-accreditation   0   8
      is-achology-a-university                                   achology-basics-and-identity   0   8
      is-achology-educational-provider-or-professional-body      achology-basics-and-identity   0   8
      is-achology-right-emotionally-vulnerable                   learning-experience            0   8
      many-times-coach-same-person-cips                          events-and-mentorship          0   8
      platform-changes-course-access-achology                    membership-and-access          0   8
      refund-course-complimentary-membership-cancel-too          refunds-and-billing            0   8
      where-is-achology-based                                    achology-basics-and-identity   0   8
      achology-password-reset-email-not-arriving                 technical-help                 0   7
      achology-refund-policy-explained                           refunds-and-billing            0   7
      achology-vs-icf-coaching-certification                     comparisons-and-alternatives   0   7
      achology-vs-university-psychology                          comparisons-and-alternatives   0   7
      become-an-achology-affiliate                               partnerships-and-press         0   7
      can-achology-help-personal-struggles                       outcomes-and-expectations      0   7
      can-achology-replace-university-degrees                    outcomes-and-expectations      0   7
      cant-log-in-achology-community                             technical-help                 0   7
      commit-practising-achologist                               community-and-conduct          0   7
      does-achology-offer-partnerships-collaborations            partnerships-and-press         0   7
      is-achology-global-platform                                achology-basics-and-identity   0   7
      many-ccac-sessions-need-complete-often                     community-and-conduct          0   7
      where-can-i-learn-the-johari-window                        curriculum-and-subjects        0   7
      achology-coaching-competency-review-sessions               events-and-mentorship          0   6
      achology-refund-disagree-course-content                    refunds-and-billing            0   6
      achology-s-nine-value-based-principles                     achology-basics-and-identity   0   6
      achology-updates-course-already-purchased                  privacy-and-legal              0   6
      ask-questions-achology-community                           community-and-conduct          0   6
      does-achology-provide-crisis-support                       membership-and-access          0   6
      does-achology-sell-personal-data                           privacy-and-legal              0   6
      homework-assessment-achology-courses                       getting-started                0   6
      is-achology-accredited-somap                               certificates-cpd-accreditation   0   6
      kain-ramsay-udemy-vs-achology-courses                      comparisons-and-alternatives   0   6
      navigate-achology-community-guide                          getting-started                0   6
      offer-free-coaching-someone-outside-achology               events-and-mentorship          0   6
      personal-responsibility-achology-learning                  achology-basics-and-identity   0   6
      prior-qualifications-needed-achology                       getting-started                0   6
      standards-apply-trainee-achologists                        community-and-conduct          0   6
      what-to-include-achology-support-request                   technical-help                 0   6
      achology-character-development                             outcomes-and-expectations      0   5
      achology-code-ethics                                       achology-basics-and-identity   0   5
      achology-content-offensive-emotionally-challenging         learning-experience            0   5
      achology-discounts-sales-promotions                        pricing-and-payments           0   5
      achology-discussion-spaces-groups-events                   events-and-mentorship          0   5
      achology-professional-indemnity-insurance                  outcomes-and-expectations      0   5
      achology-refund-technical-issues                           refunds-and-billing            0   5
      achology-s-five-community-principles                       community-and-conduct          0   5
      achology-s-three-learning-paths                            curriculum-and-subjects        0   5
      achology-uk-register-learning-providers                    certificates-cpd-accreditation   0   5
      call-myself-therapist-achology-courses                     certificates-cpd-accreditation   0   5
      difference-between-code-ethics-ccac-community              community-and-conduct          0   5
      does-achology-supervise-peer-coaching                      outcomes-and-expectations      0   5
      download-achology-community-app                            technical-help                 0   5
      how-long-achology-refund-process                           refunds-and-billing            0   5
      how-much-do-achology-coaches-earn                          outcomes-and-expectations      0   5
      how-to-join-live-achology-community-event                  technical-help                 0   5
      is-achology-content-scientific-or-ideological              outcomes-and-expectations      0   5
      pals-earn-them                                             events-and-mentorship          0   5
      realistic-outcomes-with-achology                           outcomes-and-expectations      0   5
      supervision-after-achology-training                        outcomes-and-expectations      0   5
      what-is-achology                                           achology-basics-and-identity   0   5
      what-personal-data-achology-collects                       privacy-and-legal              0   5
      which-achology-events-earn-accreditation-credit            events-and-mentorship          0   5
      achologist-led-tutorials-alts                              events-and-mentorship          0   4
      achology-automated-decision-making-profiling               privacy-and-legal              0   4
      achology-change-mind-after-14-day-guarantee                refunds-and-billing            0   4
      achology-customer-legal-rights-uk-consumer-law             privacy-and-legal              0   4
      achology-evidence-based-humanistic-psychology              achology-basics-and-identity   0   4
      achology-membership-refund                                 refunds-and-billing            0   4
      become-a-master-achologist                                 events-and-mentorship          0   4
      coaching-hot-seat                                          events-and-mentorship          0   4
      explain-achology-qualifications-to-clients                 certificates-cpd-accreditation   0   4
      how-long-achology-keeps-personal-data                      privacy-and-legal              0   4
      is-achology-therapy-counselling-or-coaching                achology-basics-and-identity   0   4
      rsvp-join-achology-live-events                             events-and-mentorship          0   4
      share-achology-account-courses                             membership-and-access          0   4
      slow-deep-learning-rejects-fast-certification              learning-experience            0   4
      upgrade-courses-bundle-access-pass                         pricing-and-payments           0   4
      what-does-achology-certification-qualify                   certificates-cpd-accreditation   0   4
      what-is-applied-psychology-achology                        achology-basics-and-identity   0   4
      why-achology-emphasises-personal-responsibility            achology-basics-and-identity   0   4
      achologist-title-without-membership                        certificates-cpd-accreditation   0   3
      achology-access-all-areas-pass                             membership-and-access          0   3
      achology-course-order-sequence                             getting-started                0   3
      call-myself-certified-achology-credentials                 outcomes-and-expectations      0   3
      do-achology-courses-get-updated                            learning-experience            0   3
      get-value-achology-mentorship-sessions                     events-and-mentorship          0   3
      hidden-fees-additional-costs-achology                      pricing-and-payments           0   3
      how-achology-courses-work-self-paced                       learning-experience            0   3
      how-psychology-became-institutionalised                    comparisons-and-alternatives   0   3
      how-to-contact-achology-support                            technical-help                 0   3
      inside-achology-course-modules-breakdown                   learning-experience            0   3
      join-professional-body-after-achology                      certificates-cpd-accreditation   0   3
      post-nominal-letters-achology-certificates                 certificates-cpd-accreditation   0   3
      see-real-results-how-long-achology-takes                   outcomes-and-expectations      0   3
      society-lost-gatekeeping-psychology                        comparisons-and-alternatives   0   3
      what-does-achology-membership-include                      membership-and-access          0   3
      what-law-governs-achology-terms                            privacy-and-legal              0   3
      which-achology-company-am-actually-contracting             privacy-and-legal              0   3
      who-is-achology-designed-for                               achology-basics-and-identity   0   3
      who-is-kain-ramsay                                         achology-basics-and-identity   0   3
      who-runs-achology                                          achology-basics-and-identity   0   3
      will-clients-take-achology-certificate-seriously           outcomes-and-expectations      0   3
      achology-live-events-types                                 events-and-mentorship          0   2
      achology-recommended-practice-pathway                      events-and-mentorship          0   2
      achology-s-registered-company-details                      privacy-and-legal              0   2
      achology-vs-coursera-psychology-education                  comparisons-and-alternatives   0   2
      achology-vs-school-of-life-comparison                      comparisons-and-alternatives   0   2
      achology-vs-tony-robbins-comparison                        comparisons-and-alternatives   0   2
      achology-vs-udemy-psychology-courses                       comparisons-and-alternatives   0   2
      evidence-cpd-learning-progression-achology                 certificates-cpd-accreditation   0   2
      first-course-complete-beginner                             getting-started                0   2
      manipulative-pricing-tactics-achology-avoids               achology-basics-and-identity   0   2
      many-courses-achology-offer-total                          curriculum-and-subjects        0   2
      membership-payment-fails-achology                          membership-and-access          0   2
      psychology-as-practical-wisdom                             achology-basics-and-identity   0   2
      what-does-achology-expect-from-learners                    achology-basics-and-identity   0   2
      what-does-achology-mean-becoming-wiser                     achology-basics-and-identity   0   2
      why-achology-avoids-diagnostic-labels                      achology-basics-and-identity   0   2
      achology-courses-cpd-hours                                 certificates-cpd-accreditation   0   1
      achology-courses-other-languages                           curriculum-and-subjects        0   1
      achology-multiple-psychology-traditions                    achology-basics-and-identity   0   1
      achology-trust-legal-policies-work-together                privacy-and-legal              0   1
      download-achology-course-materials                         learning-experience            0   1
      how-much-does-achology-cost                                pricing-and-payments           0   1
      masterclasses-vs-practitioner-courses-differences          learning-experience            0   1
      revisit-achology-courses-after-completion                  learning-experience            0   1
      what-makes-achology-different                              comparisons-and-alternatives   0   1
      where-can-i-learn-about-carl-rogers                        curriculum-and-subjects        0   1
      who-does-achology-share-personal-data-with                 privacy-and-legal              0   1
      why-achology-includes-community-course-prices              membership-and-access          0   1
      achology-school-bundles-how-they-work                      membership-and-access          0   0
      how-long-achology-operating                                achology-basics-and-identity   0   0
      seven-schools-achology-curriculum-explained                curriculum-and-subjects        0   0
      why-achology-criticizes-psychology-teaching                achology-basics-and-identity   0   0
      achology-s-character-code-based-aristotle                  community-and-conduct          1  11
      achology-responsible-community-member-advice               privacy-and-legal              1  10
      achology-career-change-coaching-mentoring                  outcomes-and-expectations      1   8
      achology-membership-free-coaching-included                 events-and-mentorship          1   8
      achology-on-udemy-should-i-join-achology                   comparisons-and-alternatives   1   8
      choose-right-achology-event-level                          events-and-mentorship          1   8
      who-is-achology-not-for                                    achology-basics-and-identity   1   8
      cant-see-achology-course-space-community                   technical-help                 1   7
      find-achology-course-resources                             technical-help                 1   7
      how-to-participate-achology-discussions-events             events-and-mentorship          1   7
      personal-progress-checklist-count-official-cpd             certificates-cpd-accreditation   1   7
      study-multiple-achology-courses-simultaneously             learning-experience            1   7
      submit-cpd-credit-claim-hosting-attending                  events-and-mentorship          1   7
      achology-vs-linkedin-learning-comparison                   comparisons-and-alternatives   1   6
      cpd-journey-after-leaving-achology                         certificates-cpd-accreditation   1   6
      no-credential-inflation-achology                           achology-basics-and-identity   1   6
      principle-led-education-achology                           achology-basics-and-identity   1   6
      verify-achology-certificate                                certificates-cpd-accreditation   1   6
      achology-free-trial-introductory-offer                     pricing-and-payments           1   5
      create-posts-achology-community                            technical-help                 1   5
      membership-first-or-course-first                           getting-started                1   5
      achology-discussion-boundary-feels-unsafe                  community-and-conduct          1   4

### REPLY__Five_Cards_Voice_Rerun_And_Inbox_Work_Acted_On_S380, job 1: the one-sentence paragraph check for help answers: DONE

Built in the help-answer branch of `content_gate.py`, on Cowork's `BRIEF__Ban_Single_Sentence_Paragraphs_In_Help_Answer_Gate_S361` and Kain's S361 words quoted in it: any paragraph of exactly one sentence fails. Fixed wording is excluded, found on the approved exemplar, whose only three hits were the picture line, the bold "Related questions" label and the UKRLP line; with those out the exemplar reads "none". The paragraph cap is unchanged. Acceptance 137 of 137. Re-measurement, worst first (the live count is read from the install's HTML and includes the 33 answers with no record; the record count is the source Cowork edits):

    records on disk: 246 read, 99 carry at least one one-sentence paragraph, 255 such paragraphs in all
        what-does-an-nlp-course-cover                                14 of 33 paragraphs
        where-can-i-learn-abraham-maslow                             12 of 28 paragraphs
        how-much-does-achology-cost                                  10 of 18 paragraphs
        what-does-a-cbt-course-cover                                  9 of 30 paragraphs
        where-can-i-learn-about-albert-ellis                          8 of 20 paragraphs
        best-cbt-course-or-certification                              7 of 19 paragraphs
        where-can-i-learn-drama-triangle                              7 of 19 paragraphs
        choose-a-good-life-coaching-course                            6 of 31 paragraphs
        host-own-achology-event                                       6 of 15 paragraphs
        where-can-i-learn-about-viktor-frankl                         6 of 14 paragraphs
        membership-payment-fails-achology                             5 of 11 paragraphs
        achology-multiple-psychology-traditions                       4 of 12 paragraphs
        achology-updates-course-already-purchased                     4 of 12 paragraphs
        choose-right-achology-event-level                             4 of 12 paragraphs
        delete-achology-account-and-data                              4 of 11 paragraphs
        evidence-cpd-learning-progression-achology                    4 of 10 paragraphs
        how-to-start-learning-cbt                                     4 of 18 paragraphs
        insurance-coverage-achology-qualifications                    4 of 11 paragraphs
        nhs-routes-into-cbt                                           4 of 19 paragraphs
        pals-earn-them                                                4 of 14 paragraphs
        what-if-achology-courses-dont-work                            4 of 12 paragraphs
        achology-change-mind-after-14-day-guarantee                   3 of 10 paragraphs
        achology-members-host-workshops-events                        3 of 10 paragraphs
        build-real-competence-achology                                3 of 10 paragraphs
        cbt-course-levels-and-diplomas                                3 of 27 paragraphs
        how-much-do-cbt-therapists-earn                               3 of 27 paragraphs
        how-to-become-a-cbt-therapist                                 3 of 34 paragraphs
        is-a-cbt-certification-worth-it                               3 of 18 paragraphs
        is-achology-right-emotionally-vulnerable                      3 of 11 paragraphs
        learn-cbt-for-free                                            3 of 19 paragraphs
        society-lost-gatekeeping-psychology                           3 of 10 paragraphs
        study-cbt-online                                              3 of 17 paragraphs
        what-does-a-life-coaching-course-actually-teach               3 of 24 paragraphs
        what-does-achology-membership-include                         3 of 12 paragraphs
        what-is-achology                                              3 of 14 paragraphs
        achology-discounts-sales-promotions                           2 of  8 paragraphs
        achology-on-udemy-should-i-join-achology                      2 of 11 paragraphs
        achology-recommended-practice-pathway                         2 of  8 paragraphs
        achology-trust-legal-policies-work-together                   2 of  9 paragraphs
        achology-vs-icf-coaching-certification                        2 of 10 paragraphs
        become-a-certified-nlp-practitioner                           2 of 20 paragraphs
        cant-see-achology-course-space-community                      2 of 10 paragraphs
        create-posts-achology-community                               2 of 12 paragraphs
        dimap-course-upgrade                                          2 of 11 paragraphs
        how-long-achology-operating                                   2 of 11 paragraphs
        how-to-contact-achology-support                               2 of  9 paragraphs
        many-courses-achology-offer-total                             2 of 10 paragraphs
        need-a-certification-or-a-degree                              2 of 18 paragraphs
        psychology-as-practical-wisdom                                2 of 10 paragraphs
        revisit-achology-courses-after-completion                     2 of 10 paragraphs
        share-achology-account-courses                                2 of 13 paragraphs
        supervision-after-achology-training                           2 of 11 paragraphs
        where-can-i-learn-skilled-helper                              2 of 13 paragraphs
        who-is-achology-not-for                                       2 of 10 paragraphs
        achology-access-all-areas-pass                                1 of  8 paragraphs
        achology-accessibility-requirements                           1 of  8 paragraphs
        achology-career-change-coaching-mentoring                     1 of 10 paragraphs
        achology-certification-practice-competence                    1 of 11 paragraphs
        achology-character-development                                1 of 12 paragraphs
        achology-content-offensive-emotionally-challenging            1 of  9 paragraphs
        achology-courses-cpd-hours                                    1 of 10 paragraphs
        achology-knowledge-hub-free-read                              1 of 14 paragraphs
        achology-knowledge-hub                                        1 of 15 paragraphs
        achology-live-events-types                                    1 of  7 paragraphs
        achology-refund-policy-explained                              1 of  9 paragraphs
        achology-s-registered-company-details                         1 of 11 paragraphs
        achology-school-bundles-how-they-work                         1 of  7 paragraphs
        achology-success-stories-do-courses-work                      1 of 11 paragraphs
        achology-vs-mindvalley-comparison                             1 of 11 paragraphs
        achology-vs-university-psychology                             1 of 10 paragraphs
        ask-questions-achology-community                              1 of 12 paragraphs
        become-a-life-coach                                           1 of 16 paragraphs
        become-an-achology-affiliate                                  1 of 12 paragraphs
        completed-achology-course-nothing-changed                     1 of 11 paragraphs
        cpd-journey-after-leaving-achology                            1 of 11 paragraphs
        difference-membership-courses-achology                        1 of 12 paragraphs
        does-achology-offer-partnerships-collaborations               1 of 11 paragraphs
        fix-achology-community-notification-problems                  1 of 11 paragraphs
        homework-assessment-achology-courses                          1 of 11 paragraphs
        how-long-achology-keeps-personal-data                         1 of 11 paragraphs
        how-much-do-achology-coaches-earn                             1 of 12 paragraphs
        is-a-life-coaching-certification-worth-it                     1 of 20 paragraphs
        is-achology-accredited-somap                                  1 of  9 paragraphs
        is-achology-content-scientific-or-ideological                 1 of 12 paragraphs
        is-an-nlp-course-worth-it                                     1 of 14 paragraphs
        manipulative-pricing-tactics-achology-avoids                  1 of  9 paragraphs
        membership-first-or-course-first                              1 of 10 paragraphs
        navigate-achology-community-guide                             1 of 11 paragraphs
        seven-marks-maturity-achology-teaches                         1 of 12 paragraphs
        seven-schools-achology-curriculum-explained                   1 of  8 paragraphs
        share-my-achology-account-login                               1 of 11 paragraphs
        transfer-kain-ramsay-udemy-courses-achology                   1 of  9 paragraphs
        what-makes-a-good-nlp-course                                  1 of 22 paragraphs
        what-personal-data-achology-collects                          1 of 10 paragraphs
        where-can-i-learn-about-carl-rogers                           1 of 13 paragraphs
        where-can-i-learn-the-johari-window                           1 of 14 paragraphs
        which-achology-events-earn-accreditation-credit               1 of 10 paragraphs
        which-courses-included-each-school-bundle                     1 of  6 paragraphs
        why-achology-emphasises-personal-responsibility               1 of 11 paragraphs
    
    live bodies on the install (read this session): 250 read, 156 carry at least one one-sentence paragraph, 827 such paragraphs in all
        what-personal-data-achology-collects                         15 of 22 paragraphs
        achology-s-ten-value-commitments                             15 of 19 paragraphs
        seven-schools-achology-curriculum-explained                  14 of 18 paragraphs
        how-much-does-achology-cost                                  13 of 19 paragraphs
        achology-multiple-psychology-traditions                      13 of 20 paragraphs
        achology-trust-legal-policies-work-together                  13 of 18 paragraphs
        what-does-achology-membership-include                        12 of 20 paragraphs
        key-milestones-achology-s-history                            12 of 18 paragraphs
        achology-knowledge-hub                                       12 of 24 paragraphs
        achology-recommended-practice-pathway                        11 of 15 paragraphs
        achology-members-host-workshops-events                       11 of 17 paragraphs
        senior-achologist-two-levels                                 11 of 20 paragraphs
        build-real-competence-achology                               10 of 16 paragraphs
        become-a-master-achologist                                   10 of 15 paragraphs
        how-to-contact-achology-support                              10 of 16 paragraphs
        how-long-achology-keeps-personal-data                        10 of 18 paragraphs
        host-own-achology-event                                      10 of 18 paragraphs
        what-is-achology                                              9 of 20 paragraphs
        self-study-books-vs-achology-courses                          9 of 14 paragraphs
        achology-live-events-types                                    9 of 14 paragraphs
        achology-s-nine-value-based-principles                        9 of 19 paragraphs
        which-achology-events-earn-accreditation-credit               9 of 16 paragraphs
        share-achology-account-courses                                8 of 18 paragraphs
        evidence-cpd-learning-progression-achology                    8 of 13 paragraphs
        achology-success-stories-do-courses-work                      8 of 15 paragraphs
        choose-right-achology-event-level                             8 of 15 paragraphs
        who-does-achology-share-personal-data-with                    8 of 13 paragraphs
        does-achology-offer-partnerships-collaborations               8 of 15 paragraphs
        achologist-adept                                              8 of 15 paragraphs
        long-achology-valts-session                                   8 of 17 paragraphs
        seven-marks-maturity-achology-teaches                         8 of 17 paragraphs
        many-courses-achology-offer-total                             8 of 15 paragraphs
        any-achology-courses-appear-more-than                         8 of 18 paragraphs
        achology-change-mind-after-14-day-guarantee                   7 of 15 paragraphs
        achology-access-all-areas-pass                                7 of 13 paragraphs
        achology-school-bundles-how-they-work                         7 of 12 paragraphs
        mentoring-opportunities-achology-membership                   7 of 12 paragraphs
        delete-achology-account-and-data                              7 of 13 paragraphs
        achology-updates-course-already-purchased                     7 of 14 paragraphs
        have-each-year-keep-master-achologist                         7 of 13 paragraphs
        nine-ccac-virtues                                             7 of 15 paragraphs
        character-traits-define-achologist                            7 of 14 paragraphs
        which-achology-company-am-actually-contracting                7 of 15 paragraphs
        achology-s-registered-company-details                         7 of 15 paragraphs
        society-lost-gatekeeping-psychology                           6 of 14 paragraphs
        achology-peer-learning-culture                                6 of 10 paragraphs
        valts-achology                                                6 of 14 paragraphs
        which-courses-included-each-school-bundle                     6 of 11 paragraphs
        achology-discounts-sales-promotions                           5 of 10 paragraphs
        achology-refund-policy-explained                              5 of 12 paragraphs
        membership-payment-fails-achology                             5 of 10 paragraphs
        psychology-as-practical-wisdom                                5 of 12 paragraphs
        manipulative-pricing-tactics-achology-avoids                  5 of 12 paragraphs
        achology-accessibility-requirements                           5 of 11 paragraphs
        achology-on-udemy-should-i-join-achology                      5 of 13 paragraphs
        achology-vs-mindvalley-comparison                             5 of 13 paragraphs
        achology-vs-icf-coaching-certification                        5 of 12 paragraphs
        cpd-journey-after-leaving-achology                            5 of 14 paragraphs
        supervision-after-achology-training                           5 of 13 paragraphs
        how-long-achology-courses-take-timelines                      5 of 11 paragraphs
        inside-achology-course-modules-breakdown                      5 of 13 paragraphs
        achology-certification-practice-competence                    5 of 13 paragraphs
        what-to-include-achology-support-request                      5 of 12 paragraphs
        manage-achology-community-notifications                       5 of 11 paragraphs
        create-posts-achology-community                               5 of 14 paragraphs
        achology-copyright-sharing-course-content                     5 of 11 paragraphs
        navigate-achology-community-guide                             5 of 14 paragraphs
        ask-questions-achology-community                              5 of 14 paragraphs
        achology-community-rules-moderation                           5 of 10 paragraphs
        progress-member-achologist                                    5 of 11 paragraphs
        difference-between-code-ethics-ccac-community                 5 of 13 paragraphs
        achology-s-five-community-principles                          5 of 15 paragraphs
        commit-practising-achologist                                  5 of 16 paragraphs
        standards-apply-trainee-achologists                           5 of 14 paragraphs
        dimap-course-upgrade                                          5 of 13 paragraphs
        achology-knowledge-hub-free-read                              5 of 17 paragraphs
        difference-membership-courses-achology                        4 of 14 paragraphs
        how-long-achology-operating                                   4 of 12 paragraphs
        who-is-achology-designed-for                                  4 of 13 paragraphs
        what-does-achology-mean-becoming-wiser                        4 of 11 paragraphs
        what-does-achology-expect-from-learners                       4 of 10 paragraphs
        what-makes-achology-different                                 4 of 13 paragraphs
        why-pay-achology-when-free-content-exists                     4 of 12 paragraphs
        achology-certificates-vs-university-degrees                   4 of 12 paragraphs
        is-achology-accredited-somap                                  4 of 10 paragraphs
        join-professional-body-after-achology                         4 of 12 paragraphs
        insurance-coverage-achology-qualifications                    4 of 10 paragraphs
        achology-certificates-recognised-internationally              4 of 11 paragraphs
        realistic-outcomes-with-achology                              4 of 15 paragraphs
        what-if-achology-courses-dont-work                            4 of 11 paragraphs
        achology-character-development                                4 of 13 paragraphs
        is-achology-content-scientific-or-ideological                 4 of 13 paragraphs
        achology-career-change-coaching-mentoring                     4 of 12 paragraphs
        how-much-do-achology-coaches-earn                             4 of 14 paragraphs
        how-achology-courses-work-self-paced                          4 of 10 paragraphs
        revisit-achology-courses-after-completion                     4 of 11 paragraphs
        achology-peer-learning-community-teaches                      4 of 11 paragraphs
        completed-achology-course-nothing-changed                     4 of 12 paragraphs
        cant-log-in-achology-community                                4 of 11 paragraphs
        fix-achology-community-notification-problems                  4 of 12 paragraphs
        cant-see-achology-course-space-community                      4 of 11 paragraphs
        achology-invite-link-not-working                              4 of 10 paragraphs
        share-my-achology-account-login                               4 of 13 paragraphs
        guest-speakers-policy                                         4 of 11 paragraphs
        overwhelmed-by-achology-options                               4 of 10 paragraphs
        homework-assessment-achology-courses                          4 of 12 paragraphs
        achology-disagreement-open-discussion                         4 of 11 paragraphs
        achology-media-press-interview-requests                       4 of 10 paragraphs
        pals-earn-them                                                4 of 13 paragraphs
        earn-cpd-credit-hosting-session-only                          4 of 13 paragraphs
        there-free-achology-membership-include                        4 of 13 paragraphs
        achology-no-transformation-promises                           3 of 11 paragraphs
        achology-teaching-philosophy                                  3 of 10 paragraphs
        what-is-applied-psychology-achology                           3 of 10 paragraphs
        why-achology-emphasises-personal-responsibility               3 of 12 paragraphs
        how-psychology-became-institutionalised                       3 of 11 paragraphs
        achology-courses-cpd-hours                                    3 of 11 paragraphs
        what-does-achology-certification-qualify                      3 of  9 paragraphs
        achology-course-outcomes                                      3 of 11 paragraphs
        will-employers-recognise-achology-certificate                 3 of 10 paragraphs
        will-clients-take-achology-certificate-seriously              3 of 12 paragraphs
        can-achology-help-personal-struggles                          3 of  8 paragraphs
        achology-course-prerequisites-requirements                    3 of 12 paragraphs
        achology-live-practice-session-etiquette                      3 of 13 paragraphs
        achology-content-offensive-emotionally-challenging            3 of 10 paragraphs
        is-achology-right-emotionally-vulnerable                      3 of 10 paragraphs
        achology-discussion-spaces-groups-events                      3 of 14 paragraphs
        achology-case-study-discussion-groups                         3 of  9 paragraphs
        achology-password-reset-email-not-arriving                    3 of 13 paragraphs
        fix-audio-video-achology-live-sessions                        3 of 10 paragraphs
        membership-first-or-course-first                              3 of 11 paragraphs
        prior-qualifications-needed-achology                          3 of 12 paragraphs
        find-achology-members-similar-interests                       3 of 10 paragraphs
        achology-discussion-boundary-feels-unsafe                     3 of  9 paragraphs
        become-instructor-contribute-content-achology                 3 of 10 paragraphs
        become-an-achology-affiliate                                  3 of 13 paragraphs
        using-achology-content-branding-materials                     3 of 11 paragraphs
        six-achology-cpd-statuses                                     3 of 15 paragraphs
        refund-course-complimentary-membership-cancel-too             3 of 11 paragraphs
        achology-s-three-learning-paths                               3 of 10 paragraphs
        submit-cpd-credit-claim-hosting-attending                     3 of 14 paragraphs
        can-achology-suspend-terminate-access                         2 of 10 paragraphs
        who-is-achology-not-for                                       2 of 12 paragraphs
        personal-responsibility-achology-learning                     2 of 12 paragraphs
        download-achology-community-app                               2 of  9 paragraphs
        where-should-i-start-with-achology                            2 of  9 paragraphs
        difference-between-monthly-annual-achology-membership         2 of 10 paragraphs
        achology-vs-university-psychology                             1 of 12 paragraphs
        transfer-kain-ramsay-udemy-courses-achology                   1 of  9 paragraphs
        achology-skill-development-workshops                          1 of 10 paragraphs
        cant-send-receive-messages-achology-community                 1 of  8 paragraphs
        what-is-circle-achology-community                             1 of  8 paragraphs
        set-up-achology-community-profile                             1 of  9 paragraphs
        achology-automated-decision-making-profiling                  1 of 11 paragraphs
        achology-course-order-sequence                                1 of 10 paragraphs
        course-included-free-membership-happens-when                  1 of 12 paragraphs

### REPLY__Five_Cards_Voice_Rerun_And_Inbox_Work_Acted_On_S380, job 2: the 100 book notes pushed, the missing records made: DONE

- **100 of 100 pushed** with `--with-seo` and **read back clean**, so every live book note now carries its rebuilt record (Cowork's jobs 8 and 9). 10 were first refused, correctly, because a Wikipedia address with brackets in it (for example `Steve_Peters_(psychiatrist)`) broke the link on conversion and would have left a stray ")" on the page; each address was written with its brackets encoded (`%28`, `%29`), the same address, and the 10 then pushed clean.
- **The 14 missing book note DSRD 6 records, and 42 missing article records, created** by `page_readiness_board.py --backfill` (56 in all). Their machine halves fill in the overnight sweep.

### REPLY__Your_S126_To_S131_Files_Answered_And_35_Records_To_Push_S381, section 1: the 35 pushed and marked: DONE, one held

- **34 of 35 pushed** with `--with-seo` and read back clean, 34 of 34.
- **Held: `CQ001-061-1` (why-we-transfer-old-feelings-onto-new-people) is not on the install at all**: no quote page, draft or live, carries that title or address, so there is nothing to update; it needs an import through `import_quote_pages.py`, which waits on Chat's word.
- **Its register failure was a self-match, fixed:** the register names a quote by its file ID (`CQ001-061-1`) and the gate compared that with the post_name. The gate now treats a row as the record's own when its key is the post_name, the file ID or its address matches. Proved both ways: the record now reads "unique", and a copy under another name still fails "claimed by CQ001-061-1".
- **`voice_standard: s130` set on 12** that pass every voice line held strict. **22 left unmarked**, each with the line it fails:

    10-ethically-dubious-experiments: voice: opens speaking to the reader (I still remember reading the actual transcript of Stanley Mi)
    12-psychological-principles: voice: opens speaking to the reader (Search for the most important psychological principles. Ever)
    13-morally-dubious-psychology-experiments: voice: opens speaking to the reader (For eleven days on a locked ward in Montreal, a woman heard)
    delayed-gratification-insights-from-the-marshmallow-test-study: voice: opens speaking to the reader (For decades, one small experiment has shaped how people thin)
    history-and-timeline-of-counselling-psychology: voice: opens speaking to the reader (Ask most people when counselling began. They picture a couch)
    maslows-hierarchy-of-needs: voice: opens speaking to the reader (A pyramid. Five levels, stacked in order, food and shelter a)
    skills-for-highly-effective-counseling: voice: opens speaking to the reader (Two trainee counsellors sit the same course. They read the s)
    the-smart-goal-setting-framework: voice: no paragraph describing the article (1, opening '**Build in feedback, not just a deadline.** The strongest ); voice: opens speaking to the reader (Five letters, repeated so often in meetings and performance)
    twenty-pivotal-moments-in-psychologys-history: voice: opens speaking to the reader (Twenty pivotal moments, ten key dates. Five turning points.)
    what-habits-are-and-why-people-get-stuck: voice: opens speaking to the reader (Twenty-one days. That number shows up on almost every page a)
    a-diagnosis-actually-describing: voice: no paragraph describing the article (1, opening 'Once you see what a diagnosis actually describing really i)
    a-false-epidemic-happen-without-anyone-lying: voice: no paragraph describing the article (1, opening 'I build the fuller version of this idea inside the Mental ); voice: opens speaking to the reader (How can a false epidemic happen without anyone lying? It sou); voice: first heading does not repeat the title (How Can a False Epidemic Happen Without Anyone Lying, Exactl)
    bmi-decide-who-gets-eating-disorder-treatment: voice: first heading does not repeat the title (Why Does BMI Decide Who Gets Eating Disorder Treatment, Acco)
    doctors-have-only-minutes-to-diagnose: voice: no paragraph describing the article (1, opening 'I build the fuller version of this idea inside the Mental )
    does-a-diagnosis-do-to-the-person: voice: no paragraph describing the article (1, opening 'What does a diagnosis do to the person who receives it? So); voice: opens speaking to the reader (What does a diagnosis do to the person who receives it? Some)
    everyone-agreeing-on-a-diagnosis: voice: no paragraph describing the article (1, opening 'I build the fuller version of this distinction inside the ); voice: opens speaking to the reader (Ask a room of 10 clinicians to diagnose the same patient usi); voice: first heading does not repeat the title (Why Everyone Agreeing on a Diagnosis Does Not Make It True)
    five-symptoms-mean-depression: voice: no paragraph describing the article (1, opening 'They do not mean anything about what your own struggle des)
    self-report-decide-a-diagnosis: voice: no paragraph describing the article (1, opening 'How much does self-report decide a diagnosis? For depressi); voice: opens speaking to the reader (How much does self-report decide a diagnosis? For one of the); voice: first heading does not repeat the title (How Much Does Self-Report Decide a Diagnosis? More Than You)
    the-definition-of-mental-disorder: voice: no paragraph describing the article (1, opening 'I build the fuller version of this idea inside the Mental ); voice: opens speaking to the reader (Ask what a mental disorder actually is, and most people assu)
    the-dsm-5-cost-five-times-more: voice: no paragraph describing the article (1, opening 'Why did the DSM-5 cost five times more than the DSM-IV? Be)
    the-dsm-call-its-own-categories-porous: voice: no paragraph describing the article (1, opening 'I build the fuller version of this idea inside the Mental ); voice: opens speaking to the reader (Most people picture a psychiatric diagnosis like a labelled); voice: first heading does not repeat the title (So Why Does the DSM Call Its Own Categories Porous?)
    what-is-concept-creep: voice: no paragraph describing the article (1, opening 'What is concept creep? A word slowly growing to cover far ); voice: opens speaking to the reader (What is concept creep? It is a simple idea with a big effect)

### REPLY__Your_Standards_Sweep_And_Score_Table_Answered_S381, item 6: "truly" is banned: DONE

Added to `machine_tells_always` in `content_gate_standards.json` beside "plainly", every type. On a quote page, words inside quotation marks are the quoted person's and are blanked before the tells are read; outside the marks "truly" still fails. Acceptance 141 of 141, four new, red and green both ways. **Read-only run over every live record:** live records carrying 'truly': 97; already among the 641: 48; NOT among the 641: 49
. **The 49 NOT among the 641, for Cowork** (count of uses in brackets):

    instructor-article/all-progression-is-impossible-without-change (2)
    instructor-article/balance-the-main-areas-of-life (3)
    instructor-article/can-you-be-too-self-aware (3)
    instructor-article/can-you-choose-to-be-more-introverted-or-extroverted (8)
    instructor-article/change-is-the-only-constant (1)
    instructor-article/confuse-opinions-with-facts (2)
    instructor-article/connected-to-your-future-self (5)
    instructor-article/cover-up-incompetence-with-head-knowledge (1)
    instructor-article/disagreement-vs-division (4)
    instructor-article/every-decision-is-a-trade-off (1)
    instructor-article/everyone-experiences-reality-differently (2)
    instructor-article/feeling-stuck-in-life (7)
    instructor-article/fixed-or-growth-mindset (1)
    instructor-article/forget-your-mistakes-but-remember-their-lessons (3)
    instructor-article/fountain-or-a-drain (2)
    instructor-article/freedom-vs-security (3)
    instructor-article/happiness-is-a-delusion-fulfilment-is-not (7)
    instructor-article/living-according-to-your-values (6)
    instructor-article/pattern-recognition-superpower (5)
    instructor-article/positive-vs-negative-motivation (1)
    instructor-article/rational-or-emotional-thinker (4)
    instructor-article/remembered-for (5)
    instructor-article/saying-less-more-influential (1)
    instructor-article/self-acceptance-vs-self-improvement (2)
    instructor-article/taking-responsibility-creates-personal-growth (3)
    instructor-article/think-objectively (2)
    instructor-article/thoughts-and-emotions-connection (1)
    instructor-article/types-of-listening (3)
    instructor-article/whats-the-key-to-winning-hearts-and-minds (4)
    instructor-article/your-relationship-with-money-tells-a-story (5)
    book-note/a-way-of-being (2)
    book-note/awakenings (1)
    book-note/coming-to-our-senses (1)
    book-note/creating-minds (1)
    book-note/how-the-mighty-fall (1)
    book-note/noise (2)
    book-note/the-brains-way-of-healing (1)
    book-note/the-open-society-and-its-enemies (1)
    book-note/the-relationship-cure (1)
    book-note/time-and-free-will (1)
    quote-page/why-applying-what-you-learn-is-what-learning-means (1)
    quote-page/why-its-easier-to-diagnose-people-than-to-understand-them (1)
    quote-page/why-being-right-is-not-the-point-at-all (1)
    quote-page/why-you-are-more-than-your-past (1)
    quote-page/why-experience-gives-us-authority-in-life (1)
    quote-page/why-no-teacher-can-make-you-learn (1)
    quote-page/why-a-blamer-hides-loneliness-behind-a-tough-mask (1)
    quote-page/why-knowing-facts-is-not-the-same-as-understanding (1)
    quote-page/why-simplicity-is-key-to-a-highly-effective-life (1)

### REPLY__Your_S126_To_S131_Files_Answered_And_35_Records_To_Push_S381, section 2 and 3 items: DONE

- **Subject sitemap switched on** (`tax_kh_category_sitemap`); the topic sitemap stays off, as ruled.
- **The three stray topic terms taken off their posts** (brendon-burchard: motivation; charles-duhigg: motivation and helping-people; steven-pinker: psychology) and **out of the three author-biography records' `kh_tag` fields**, so a re-import cannot bring them back. All three terms now carry 0 posts. **Deleting the three empty terms themselves is left to Kain** in WordPress (Posts, then the Knowledge Hub Tags screen): a permanent deletion is not one Code makes.
- **The free trial answer and the 24:** already pushed at S130, 24 of 24 read back clean; the S378 NOTE is closed.
- **Chapter 5 reset:** every DSRD 6 record's chapter 5 line measured before tonight now reads "not run" (6 records still carried an older line: the listing page, pricing, the kh_category template, one book note, the instructors page and one instructor article). The rest were already "not run" or measured tonight.

### REPLY__Your_Standards_Sweep_And_Score_Table_Answered_S381, items 1, 2, 3 and 7: DONE

- **Item 1, the 33 records:** all 33 live help answers with no record now have one, `HELP__{slug}.md` in the help-answer folder, carrying post_id, title, name, focus keyword, date, status, address, category, SEO title, meta description, excerpt and reviewer, and `origin: exported-from-live S381` in the notes. Each body was converted from the live HTML and proved word for word by converting it back with the push tool's own converter. **One live defect found and fixed:** `achology-skill-development-workshops` showed "session&8217;s" on the page (an apostrophe code missing its #); its record carries the apostrophe, the page was pushed and reads back clean, and no other page on the install carries the fault. **Gate results, all 33 fail on copy lines (no field or structure fault):** 32 keyword in a subheading, 32 no contraction, 31 a one-sentence paragraph, 28 reading ease, 23 keyword in the address, 7 a paragraph over 60 words or 3 sentences, 4 machine-written tells, 4 "actually" twice, 3 keyword density, 2 keyword in the first 10 per cent, 2 keyword early in the description, 2 description length, 1 a paragraph over 120 words, 1 keyword early in the SEO title. Page by page:

    can-achology-suspend-terminate-access | FAIL (6) | no one-sentence paragraph (Kain, S361);machine-written tells;reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    why-pay-achology-when-free-content-exists | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    self-study-books-vs-achology-courses | FAIL (4) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in a subheading;contractions: at least one in the body;
    achology-certificates-vs-university-degrees | FAIL (7) | no one-sentence paragraph (Kain, S361);no paragraph over 60 words or 3 sentences;'actually' at most once (Kain, S381);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    achology-certificates-recognised-internationally | FAIL (9) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in first 50 chars of SEO title;keyword in first 120 chars of description;description length;keyword verbatim in first 10% of body;keyword in a subheading;keyword density;contractions: at least one in the body;
    achology-course-outcomes | FAIL (6) | no one-sentence paragraph (Kain, S361);machine-written tells;reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    will-employers-recognise-achology-certificate | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    how-long-achology-courses-take-timelines | FAIL (4) | no one-sentence paragraph (Kain, S361);no paragraph over 60 words or 3 sentences;keyword in a subheading;contractions: at least one in the body;
    achology-live-practice-session-etiquette | FAIL (5) | no one-sentence paragraph (Kain, S361);machine-written tells;reading ease (Flesch, approximate);keyword in a subheading;contractions: at least one in the body;
    mentoring-opportunities-achology-membership | FAIL (7) | no one-sentence paragraph (Kain, S361);no paragraph over 60 words or 3 sentences;'actually' at most once (Kain, S381);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    achology-case-study-discussion-groups | FAIL (4) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in a subheading;contractions: at least one in the body;
    achology-skill-development-workshops | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword density;contractions: at least one in the body;
    fix-audio-video-achology-live-sessions | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    cant-send-receive-messages-achology-community | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    achology-invite-link-not-working | FAIL (7) | no one-sentence paragraph (Kain, S361);keyword in first 120 chars of description;description length;keyword verbatim in first 10% of body;keyword in a subheading;keyword density;contractions: at least one in the body;
    what-is-circle-achology-community | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    manage-achology-community-notifications | FAIL (6) | no one-sentence paragraph (Kain, S361);'actually' at most once (Kain, S381);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    overwhelmed-by-achology-options | FAIL (5) | no one-sentence paragraph (Kain, S361);no paragraph over 60 words or 3 sentences;keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    achology-disagreement-open-discussion | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    achology-peer-learning-culture | FAIL (4) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in a subheading;contractions: at least one in the body;
    find-achology-members-similar-interests | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    achology-community-rules-moderation | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    become-instructor-contribute-content-achology | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    achology-media-press-interview-requests | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    achologist-adept | FAIL (5) | no one-sentence paragraph (Kain, S361);no paragraph over 60 words or 3 sentences;keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    senior-achologist-two-levels | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    progress-member-achologist | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    have-each-year-keep-master-achologist | FAIL (6) | no one-sentence paragraph (Kain, S361);no paragraph over 60 words or 3 sentences;reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    long-achology-valts-session | FAIL (6) | no one-sentence paragraph (Kain, S361);machine-written tells;reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    nine-ccac-virtues | FAIL (5) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;contractions: at least one in the body;
    character-traits-define-achologist | FAIL (4) | no one-sentence paragraph (Kain, S361);reading ease (Flesch, approximate);keyword in a subheading;contractions: at least one in the body;
    achology-s-ten-value-commitments | FAIL (5) | no one-sentence paragraph (Kain, S361);'actually' at most once (Kain, S381);reading ease (Flesch, approximate);keyword in a subheading;contractions: at least one in the body;
    key-milestones-achology-s-history | FAIL (7) | no paragraph over 60 words or 3 sentences;reading ease (Flesch, approximate);keyword in address slug;keyword in a subheading;keyword density;no paragraph over 120 words;contractions: at least one in the body;

- **Item 2, the back-fill:** 217 help records gained `rm_focus_keyword` and `post_date` from the install; no record's existing keyword differed from the live one, none was overwritten, and no page was pushed. "focus keyword set" now passes on all 217.
- **Item 3, the dated lines:** `content_gate.py` reads a record's `post_date` against `field_introduced` in the standards file (stage 0 demand evidence from 26 August 2026, pipeline Version 2, S315; the outcome tag count from 4 September 2026, S341). A record dated before prints the line as NOT RUN with both dates; one dated after, or undated, is held to it. Every live help answer carries the install's date, 1 June 2020, so all 250 now read NOT RUN on both.
- **Item 7, "actually" at most once:** a body carrying it twice or more outside quotation marks fails, every type; titles are fields and not counted.
- **Acceptance 148 of 148**, 7 new for items 3 and 7.

### ASK__Real_Counts_And_Newest_Six_Per_Type_For_The_Front_Page_Render_S378: DONE (answer below)

Read off the install, S131, after tonight's pushes. **Published:** 269 articles (1 draft), 139 book notes, 250 help answers (1 draft), 250 quote pages (21 drafts, the old Handbook set), 0 workbooks. **Newest six per type by publish date:** articles all-progression-is-impossible-without-change, assumptions-damage-relationships, build-genuine-rapport, build-self-control, can-you-be-too-self-aware, can-you-choose-to-be-more-introverted-or-extroverted (a batch sharing one timestamp, 22 September 23:17, so "newest six" is a tie broken alphabetically); book notes before-happiness, bittersweet, embracing-uncertainty, further-along-the-road-less-travelled, leader-effectiveness-training, necessary-endings (one batch, 22 September 23:34, also a tie); quote pages self-esteem-in-the-moment, helping-is-about-the-person, helping-is-not-about-fixing, resources-clients-are-not-using, maturity-in-decision-making, reading-for-insight (23 September 16:31 to 16:32); help answers carry an import date of 1 June 2020 on all but one, so "newest" means nothing there and a front-page render should pick help answers by another rule.

### REPLY__Your_S126_To_S131_Files_Answered_And_35_Records_To_Push_S381, the remaining items: DONE, one ASK

- **`--color-orange-press`** is `#9A3B0D` (`base.css`, line 95). **`#D85A1B` (`--color-orange-hover`) is still used**, so it is not dead: `book-note.css` (a button's hover background and border, lines 693 and 694) and `about.css` (the two orange gradients, lines 127 and 301, and the back-to-top button's hover, line 613). `reviews.css` and `pricing.css` name it only in comments that reserve it.
- **The folder map tool** lives in the theme repository at `tools/folder_map.py` (with `tools/folder_map_acceptance.py`). It is missing from the live theme's folder on the server by design: `deploy.py` sends only the files a web server renders, and developer tooling stays off the public server since S093.
- **Brene Brown and Gabor Mate:** the records always carried the right letters; the install held the escaped text, and all seven fields were written back from the records at S131 (both now score 89). The import sheet and the records hold no escaped text, so there is nothing further to push.
- **The pricing page's free-tier Offer, the two Safari choices, and the spacing sweep** are theme work and are queued as lines in `000__THE_THEME_QUEUE.md`.
- **ASK: `CQ001-061-1` (why-we-transfer-old-feelings-onto-new-people) is not on the install at all**, draft or live. Should Code import it with `import_quote_pages.py` as a draft for Kain to publish, or is it held?

### REPLY__Five_Cards_Voice_Rerun_And_Inbox_Work_Acted_On_S380, job 3: the quote page template's DSRD 6 record: DONE, and a correction to Code's board-card answer

**Correction:** `ANSWER__Five_Board_Cards_S131` said the quote page template had no DSRD 6 record. It had one, created by the S130 backfill but filed by mistake inside the page's image folder (`Page Images/Course Quote Covers/`), which is why a look at the design folder missed it. It now sits in the Quote Page design folder as `DSRD6_RECORD.md`, naming `PROTOTYPE__Quote_Page_S130_APPROVED.html` as its signed prototype, and its machine half was re-run tonight on a live quote page (`reading-for-insight`): §2, §3, §5, §7 and §11 machine halves pass; **§1 fails** on one acronym, "CBT", used before it is spelled out, which comes from the course card's own name ("CBT Toolkit") inside the page's course block, not the quote's words; **§10 fails** on a 384px gap at desktop where 48 is the rule, a theme spacing fault. Both are theme items; §10 rides with the spacing sweep in the theme queue.

### CORRECTION to the one-sentence re-measurement above

The first count treated the items of a list spaced out with blank lines as paragraphs, and a line ending in a colon that introduces a list as a lone sentence; Chat's S370 ruling passes the lead-in, and a list item is not a paragraph. Found on the Ellis answer, fixed in the gate (acceptance 149 of 149, one new case). **The corrected count, which replaces the one above:** records on disk: 279 read, 46 carry at least one one-sentence paragraph, 109 such paragraphs in all
; live bodies on the install (read this session): 250 read, 31 carry at least one one-sentence paragraph, 81 such paragraphs in all
. The page-by-page list, worst first:

    achology-peer-learning-culture                                6 of 11 paragraphs
    achology-community-rules-moderation                           5 of 11 paragraphs
    achology-s-ten-value-commitments                              5 of 20 paragraphs
    how-long-achology-courses-take-timelines                      5 of 12 paragraphs
    achology-certificates-recognised-internationally              4 of 12 paragraphs
    achology-certificates-vs-university-degrees                   4 of 13 paragraphs
    best-cbt-course-or-certification                              4 of 19 paragraphs
    overwhelmed-by-achology-options                               4 of 11 paragraphs
    self-study-books-vs-achology-courses                          4 of 15 paragraphs
    achology-case-study-discussion-groups                         3 of 10 paragraphs
    achology-course-outcomes                                      3 of 12 paragraphs
    become-instructor-contribute-content-achology                 3 of 11 paragraphs
    choose-a-good-life-coaching-course                            3 of 31 paragraphs
    find-achology-members-similar-interests                       3 of 11 paragraphs
    what-does-a-life-coaching-course-actually-teach               3 of 24 paragraphs
    why-pay-achology-when-free-content-exists                     3 of 13 paragraphs
    will-employers-recognise-achology-certificate                 3 of 11 paragraphs
    achologist-adept                                              2 of 11 paragraphs
    achology-invite-link-not-working                              2 of 11 paragraphs
    achology-live-practice-session-etiquette                      2 of 14 paragraphs
    become-a-certified-nlp-practitioner                           2 of 20 paragraphs
    can-achology-suspend-terminate-access                         2 of 11 paragraphs
    have-each-year-keep-master-achologist                         2 of 10 paragraphs
    long-achology-valts-session                                   2 of 18 paragraphs
    mentoring-opportunities-achology-membership                   2 of 13 paragraphs
    need-a-certification-or-a-degree                              2 of 18 paragraphs
    progress-member-achologist                                    2 of 10 paragraphs
    what-does-an-nlp-course-cover                                 2 of 33 paragraphs
    what-is-achology                                              2 of 14 paragraphs
    where-can-i-learn-about-viktor-frankl                         2 of 14 paragraphs
    where-can-i-learn-drama-triangle                              2 of 19 paragraphs
    where-can-i-learn-skilled-helper                              2 of 13 paragraphs
    achology-disagreement-open-discussion                         1 of 12 paragraphs
    achology-media-press-interview-requests                       1 of 11 paragraphs
    achology-skill-development-workshops                          1 of 11 paragraphs
    become-a-life-coach                                           1 of 16 paragraphs
    cant-send-receive-messages-achology-community                 1 of  9 paragraphs
    character-traits-define-achologist                            1 of 15 paragraphs
    how-to-start-learning-cbt                                     1 of 18 paragraphs
    is-a-life-coaching-certification-worth-it                     1 of 20 paragraphs
    is-an-nlp-course-worth-it                                     1 of 14 paragraphs
    manage-achology-community-notifications                       1 of 12 paragraphs
    nhs-routes-into-cbt                                           1 of 19 paragraphs
    nine-ccac-virtues                                             1 of 16 paragraphs
    what-is-circle-achology-community                             1 of  9 paragraphs
    what-makes-a-good-nlp-course                                  1 of 22 paragraphs
    achology-peer-learning-culture                                6 of 10 paragraphs
    how-long-achology-courses-take-timelines                      5 of 11 paragraphs
    achology-community-rules-moderation                           5 of 10 paragraphs
    achology-s-ten-value-commitments                              5 of 19 paragraphs
    self-study-books-vs-achology-courses                          4 of 14 paragraphs
    achology-certificates-vs-university-degrees                   4 of 12 paragraphs
    achology-certificates-recognised-internationally              4 of 11 paragraphs
    overwhelmed-by-achology-options                               4 of 10 paragraphs
    why-pay-achology-when-free-content-exists                     3 of 12 paragraphs
    achology-course-outcomes                                      3 of 11 paragraphs
    will-employers-recognise-achology-certificate                 3 of 10 paragraphs
    achology-case-study-discussion-groups                         3 of  9 paragraphs
    find-achology-members-similar-interests                       3 of 10 paragraphs
    become-instructor-contribute-content-achology                 3 of 10 paragraphs
    what-is-achology                                              2 of 20 paragraphs
    can-achology-suspend-terminate-access                         2 of 10 paragraphs
    achology-live-practice-session-etiquette                      2 of 13 paragraphs
    mentoring-opportunities-achology-membership                   2 of 12 paragraphs
    achology-invite-link-not-working                              2 of 10 paragraphs
    achologist-adept                                              2 of 15 paragraphs
    progress-member-achologist                                    2 of 11 paragraphs
    have-each-year-keep-master-achologist                         2 of 13 paragraphs
    long-achology-valts-session                                   2 of 17 paragraphs
    achology-skill-development-workshops                          1 of 10 paragraphs
    cant-send-receive-messages-achology-community                 1 of  8 paragraphs
    what-is-circle-achology-community                             1 of  8 paragraphs
    manage-achology-community-notifications                       1 of 11 paragraphs
    achology-disagreement-open-discussion                         1 of 11 paragraphs
    achology-media-press-interview-requests                       1 of 10 paragraphs
    nine-ccac-virtues                                             1 of 15 paragraphs
    character-traits-define-achologist                            1 of 14 paragraphs

### NOTE__Push_66_More_Fixed_Records_And_Two_SEO_Titles_S381: DONE

- The two SEO titles set first, word for word: remembered-for "Remembered For: What Do You Want People to Say?"; think-objectively "Think Objectively: What It Means in Practice".
- **67 of 67 pushed** (items 1 to 68 less item 66) with `--with-seo` and **read back clean, 67 of 67** (two needed a second read: one page did not load in time, one link count misread; both clean on the retry, and all six outside links were checked on the live page by hand for the second). Eleven were quote pages, named in Cowork's list by their record IDs and matched to their addresses.
- `helping-people-help-themselves` is both an article and a quote page, so the push tool now takes a type in front of the address (`field-authority-article:helping-people-help-themselves`); the bare name is still refused, correctly.
- **`voice_standard: s130` on 40.** Left unmarked, 27, each with the strict line it fails (nearly all the opening line, outside this job):

    examining-the-doll-test: voice: opens speaking to the reader (A simple question, put to a young child holding two dolls id); voice: first heading does not repeat the title (What was the doll test, and what did it actually show)
    helping-people-help-themselves: 2 records
    karpman-drama-triangle: voice: opens speaking to the reader (Most people know the feeling before they know the name for i)
    perceptions-illusion-insights-from-the-halo-effect-experiment: voice: opens speaking to the reader (Two students watch the same guest lecturer, on the same reco)
    the-lucifer-effect-10-lessons-from-philip-zimbardos-classic: voice: opens speaking to the reader ("Ordinary, healthy people can be led to act in ways they wou)
    the-origin-of-cognitive-therapy: voice: opens speaking to the reader (Ask someone where cognitive therapy came from, and most peop)
    the-stages-of-change-model: voice: opens speaking to the reader (Fifteen quotes. Fifteen different historical figures. Voltai)
    the-truth-about-eloquence: voice: opens speaking to the reader (There is a number that gets repeated in almost every communi)
    unraveling-apathy-insights-from-the-bystander-effect-study: voice: opens speaking to the reader (Does the bystander effect still hold up? Most people know th)
    unveiling-attachment-insights-from-harlows-monkey-experiments: voice: opens speaking to the reader (Put a baby rhesus monkey in a cage with two mothers. One is)
    voices-of-vulnerability-insights-from-the-monster-study-experiment: voice: opens speaking to the reader (Look up the Monster Study and nearly every account opens the)
    mental-disorders-tripled-since-the-1950s: voice: no paragraph describing the article (1, opening 'I build the fuller version of this idea inside the Mental ); voice: opens speaking to the reader (Since 1952, the number of named mental disorders has nearly)
    the-rise-in-autism-diagnoses-real: voice: no paragraph describing the article (1, opening 'I build the fuller version of this idea inside the Mental ); voice: opens speaking to the reader (Autism diagnoses have climbed sharply over the past few deca)
    a-guide-to-building-inner-resilience: voice: opens speaking to the reader (Something has shifted lately. Somewhere in the last few year)
    conditioning-fear-insights-from-the-little-albert-experiment: voice: opens speaking to the reader (A baby lies on a mattress in a hospital nursery. A researche)
    decide-with-confidence-10-timeless-principles-for-wise-decision-making: voice: opens speaking to the reader (The old version of this page promised ten timeless principle)
    exploring-self-determination-theory-key-principles-applications: voice: opens speaking to the reader (A father starts paying his son fifty cents for every book he)
    insights-from-mary-ainsworths-the-strange-situation-study: voice: opens speaking to the reader ("Anxious attachment." "Avoidant attachment." The phrases tur)
    the-origin-of-the-drama-triangle: voice: opens speaking to the reader (Plenty of people can describe the Drama Triangle. Far fewer)
    the-origins-of-positive-psychology: voice: opens speaking to the reader (Ask when positive psychology began and most people guess a d)
    the-role-of-freedom-in-personal-autonomy-and-decision-making: voice: opens speaking to the reader (A friend says it right before a big decision. "At least I'm)
    diagnosing-bipolar-disorder-in-children: voice: opens speaking to the reader (Why do professionals disagree about diagnosing bipolar disor)
    diagnosis-be-scientifically-weak-but-still-useful: voice: opens speaking to the reader (Can a diagnosis be scientifically weak but still useful? Aft); voice: first heading does not repeat the title (Can a Diagnosis Be Scientifically Weak but Still Useful, Giv)
    diagnostic-inflation-actually-happening: voice: opens speaking to the reader (Is diagnostic inflation actually happening? Plenty of people)
    homosexuality-was-a-diagnosis: voice: opens speaking to the reader (For decades, being gay was officially named a mental illness)
    hypomania-from-an-ordinary-mood-swing: voice: first heading does not repeat the title (How Do You Tell Hypomania From an Ordinary Mood Swing, Accor)
    multiple-personality-diagnoses-spike-after-a-film: voice: opens speaking to the reader (A rare diagnosis, almost unheard of for a century and a half)

- **The Ellis help answer (`HELP__where-can-i-learn-about-albert-ellis.md`): not on the install, and its gate fails one line: reading ease 59.0 against the band's floor of 60.** It is not imported; one point of reading ease is Chat's to fix or waive.

### TASK_LIST__The_Thirteen_Finished_Cowork_Jobs_Waiting_On_You_In_Push_Order_S370: items answered

- **"All four stand."** The 42 book notes, the 24 DSM articles, I04, I14 and I18, and the 200 course 018 quote records: all live today (139 book notes, 269 articles, 250 quote pages published, read off the install S131).
- **Item 1, the contraction count:** filed above. **Item 2, both help checks:** built above (contractions; one-sentence paragraphs with Chat's S370 colon rule).
- **Item 3, the 42 articles from Kain's resource posts:** done at S129, all 42 live.
- **Item 4, the 216 corrected help answers:** pushed live at S130, 216 of 216 read back.
- **Item 5, book notes:** (a) the headings: all 139 live book notes now carry exactly their records' bodies, headings included, after tonight's push of the 100 (39 already matched); (b) 150 book note records against 139 live: the 11 not on the install are the 11 held with reasons at S129 (`REPORT__Fourteen_Of_The_Twenty_Five_Unimported_Book_Notes...S129`); (c) and (d), the three by-author address exceptions and the two old pushes: superseded, since every live book note was re-pushed from its record tonight.
- **Item 6, the 50 book quote records:** waits on Chat's `ASK__The_21_Handbook_Drafts_And_The_Manuscript_As_Text_S380` work (below, once done) and Cowork's rewrite.
- **Item 7, the DSRD 6 machine sweep:** running tonight over all 408 articles and book notes (about fifteen hours), plus the 56 records created tonight.

### ASK__The_21_Handbook_Drafts_And_The_Manuscript_As_Text_S380: DONE, one half by another route

1. **The 21 drafts written out** into the quote-page records folder, one file each, named `{quote_id}__{slug}.md` (Q04251 and Q07009 to Q07032, less the four that were never drafted), carrying post ID, quote ID, title, address, quote text, quoted author, author, lead tag, source book, focus keyword, SEO title and description, excerpt and the current body as markdown, marked `origin: exported-from-install S131`. Read-only on the install; all 21 are drafts carrying the helping-people subject.
2. **The manuscript: no PDF, because Pages is not installed on this Mac,** so it cannot be opened or printed. **The plain text is done instead**, which is the half the quote check needs: `TULCH FINAL MANUSCRIPT.txt` now sits beside the `.pages` file (about 107,000 words, from the Foreword on), read straight out of the file's own text store without Pages. The original is untouched. **Checked at once against the 21 drafts' quote texts: 19 are word for word in the book; 2 are not** and need Cowork's eye against the text: Q07011 two-basic-choices ("There are two basic choices: to accept life's circumstances as they are or take responsibility for c...") and Q07012 deciding-who-you-will-become ("The key to progressing in life is deciding who you will become and taking responsibility for becomin..."). A PDF needs Pages installed, or Kain exporting it from another Mac.

### ASK__Sweep_The_Help_Answer_Records_For_Words_The_Achology_Stance_Forbids_S371: DONE (answer below)

Read-only, the Body of every `HELP__` record (279 files: the 246 of S371 plus the 33 exported tonight), sentence by sentence, link text kept and addresses dropped. **Code's verdict: no breach found in any of the six.**

- **1. heal, cure, treat or fix: 180 hits, all fine.** Every one is either ordinary English ("treat the checklist as your plan", "the quick fix" for a login or payment), a line saying therapy or medicine does it, or a line saying Achology does not (56 carry a negation).
- **2. promises a result: 70 hits, all fine.** All but a handful are the 14-day money-back guarantee; the rest say a result is not guaranteed.
- **3. therapist as a title: 76 hits, all fine.** Every one uses the word for a clinically trained professional, names the title as one Achology members must not claim, or is a question title in a Related questions list. None calls someone Achology trains a therapist.
- **4. the brain: nothing found.**
- **5. the named thinkers: 68 hits,** listed in full below with their sentences for Chat's read; Code sees nothing in them that contradicts the stance.
- **6. the four lines: nothing found** (no "between stimulus and response", "not disturbed by things", "positive intention" or "fourteen irrational beliefs").

Files searched: 279. The full hit list, every search, each line with its file (a `[negated]` tag marks a line carrying a negation):

#### 1. heal, cure, treat or fix: 180
    - `achology-accessibility-requirements` | Once the finished site has been formally assessed, the statement will publish the findings, including any known limitations and the dates for fixing them.
    - `achology-accessibility-requirements` | Reports from real use are the fastest way problems get found and fixed, so if any part of the site is difficult or impossible for you to use, say so.
    - `achology-career-change-coaching-mentoring` | Overlap it with existing income where you can, treat the first year as building rather than earning, and read what can honestly be said about earnings before you make any financial plan.
    - `achology-certification-practice-competence` | Treating completion as the finish line is the assumption the whole pathway exists to correct.
    - `achology-change-mind-after-14-day-guarantee` | After it, the policy treats course content the way education honestly works.
    - `achology-code-ethics` | The handbook treats it as an integrity health check, not a box-ticking exercise, aimed at helping members aspire to be better rather than just do right once.  [negated]
    - `achology-community-rules-moderation` | Maintaining the community's standards is treated as every member's job rather than only the moderators', which is why the culture holds at scale.
    - `achology-course-order-sequence` | These are recommendations rather than a fixed Achology course order.
    - `achology-course-outcomes` | The members doing the most afterwards are the ones who treated the certificate as a beginning.
    - `achology-course-outcomes` | The ones who treated it as an arrival tend to be the ones asking why nothing changed.
    - `achology-customer-legal-rights-uk-consumer-law` | If content falls short, you may be entitled to a repair or replacement, and where a fault cannot be fixed, a full or partial refund.  [negated]
    - `achology-customer-legal-rights-uk-consumer-law` | If the fault cannot be fixed, or is not fixed within a reasonable time and without significant inconvenience, you may be entitled to a full or partial refund.  [negated]
    - `achology-disagreement-open-discussion` | Treating discussion as a contest closes down exactly the perspective-taking that applied psychology trains.
    - `achology-discussion-boundary-feels-unsafe` | If something feels wrong, trust that and treat it as information, not something to dismiss.  [negated]
    - `achology-evidence-based-humanistic-psychology` | A practitioner armed only with protocols treats people as instances of a category.
    - `achology-invite-link-not-working` | This is the important part of the answer, and it is the reason this article exists rather than a one-line fix.
    - `achology-live-practice-session-etiquette` | Treating session content as repeatable elsewhere, in the forums, to friends, in your own content, does not merely breach the Community Code of Conduct.  [negated]
    - `achology-membership-refund` | That is why the Refunds Policy treats the two product types differently, stating it before purchase rather than in a support reply afterwards.
    - `achology-multiple-psychology-traditions` | Several, deliberately, with none treated as superior.
    - `achology-multiple-psychology-traditions` | All of them treat the frameworks as tools for understanding people, including yourself, rather than doctrines to defend.
    - `achology-no-transformation-promises` | Treating readers as capable adults means telling them which part of the result is theirs to produce.
    - `achology-password-reset-email-not-arriving` | The practical fix is to ask your administrator to release it or to move your membership to a personal address.
    - `achology-peer-learning-culture` | The Code of Character and Conduct sets the tone: nine virtues drawn from Aristotle, trained across the community rather than treated as an academic exercise.
    - `achology-professional-indemnity-insurance` | The Achology Code of Ethics treats insurance as a professional obligation: if you offer applied psychology services to the public, you are required to hold comprehensive cover, in place before your first client rather than arranged after something goes wrong.
    - `achology-refund-disagree-course-content` | Achology's Trust Statement sets out the same position: the ideas taught are open to interpretation, disagreement, and critique, and learners are treated as adults able to engage critically with material they may not accept.  [negated]
    - `achology-refund-policy-explained` | Course content is interpretive, and different people experience it differently, so disagreeing with an idea is not treated as a fault in the product.  [negated]
    - `achology-refund-technical-issues` | The policy's second condition simply locates responsibility where the cause is: platform failures and server problems are Achology's; a browser that needs updating is a fix on your side, not a refund trigger.  [negated]
    - `achology-refund-technical-issues` | That record matters, because it dates the start of any outage and gives support what it needs to fix the fault, which resolves things faster than a refund would.
    - `achology-responsible-community-member-advice` | Treat what you hear in peer sessions as practice material from a fellow learner rather than professional advice.
    - `achology-s-character-code-based-aristotle` | Because that tradition treats character as something you develop rather than something you are simply born with or without.  [negated]
    - `achology-s-five-community-principles` | They come from the Code of Character and Conduct and set the behavioural benchmark for how members treat one another and the space they share.
    - `achology-s-five-community-principles` | - **Respect and Inclusivity**: diversity enriches the community, every perspective is valued, and respect is treated as the basis of growth.
    - `achology-s-nine-value-based-principles` | - **Growth Mindset**: treating skills as learnable and failures as opportunities to learn.
    - `achology-s-nine-value-based-principles` | Moral Imagination is the principle that stops you treating this as two options when there are usually four.
    - `achology-s-three-learning-paths` | They are a way of choosing where to start, not fixed tracks you are locked into, and you are free to take courses from more than one path.  [negated]
    - `achology-teaching-philosophy` | - All people are capable of deep learning and growth: nobody needs fixing before they can start, and no entry gate decides who is allowed to develop.  [negated]
    - `achology-teaching-philosophy` | Its courses do not teach diagnosis, categorisation, or treatment; they treat the people who study, and the people its students go on to help, as capable adults with room to grow rather than conditions to label.  [negated]
    - `achology-updates-course-already-purchased` | Fixing a broken link or improving video quality sits here.
    - `achology-updates-course-already-purchased` | Achology treats the curriculum as a living body of teaching, not something published once and archived, which follows from how the subject itself is taught.  [negated]
    - `achology-vs-coursera-psychology-education` | How the two kinds of recognition differ is treated in full separately.
    - `achology-vs-coursera-psychology-education` | That gap is why completion and competence are treated as separate things here, not as the same achievement described twice.  [negated]
    - `achology-vs-mindvalley-comparison` | Achology treats that moment as the halfway point, because completing a course and being competent are different things, and only practice with feedback closes the gap.
    - `achology-vs-school-of-life-comparison` | Ideas from the philosophical tradition made genuinely beautiful, consoling and clear, in a voice that treats ordinary emotional life as worthy of serious thought.
    - `achology-vs-therapy-training-counselling` | Therapy training qualifies you for regulated clinical practice: diagnosing and treating mental health conditions, working with vulnerable people under supervision, registration, and ongoing accountability.
    - `achology-vs-therapy-training-counselling` | The curriculum deliberately excludes diagnosis and treatment, which is why diagnostic labelling is not taught.  [negated]
    - `achology-vs-udemy-psychology-courses` | You pay more because the product is more; whether the more is what you need is the honest question, and Is Achology worth the money? treats it squarely.
    - `adult-to-adult-learning-no-hand-holding` | So why does Achology treat learners as adults rather than providing hand-holding?
    - `adult-to-adult-learning-no-hand-holding` | Because the subject being taught is self-responsibility, and how you are treated while learning it is part of the teaching.
    - `adult-to-adult-learning-no-hand-holding` | What comes with being treated this way is set out in what Achology expects from its learners.
    - `become-a-life-coach` | There's no fixed exam or licence to pass, the way there is for many other jobs.  [negated]
    - `become-a-life-coach` | No single exam, no licence, and no fixed timeline: that's the honest, if slightly unsatisfying, answer.  [negated]
    - `become-an-achology-affiliate` | The commercial terms are negotiated rather than fixed.
    - `become-instructor-contribute-content-achology` | Teaching is treated as part of learning rather than as a reward for finishing it.
    - `best-cbt-course-or-certification` | It is not clinical training, and it was never meant to replace the Beck Institute route for someone who wants to treat patients.  [negated]
    - `call-myself-therapist-achology-courses` | This is why Achology's Code of Ethics treats accurate self-description as foundational: the whole curriculum teaches members to know the edge of non-clinical helping and refer beyond it.
    - `can-achology-help-personal-struggles` | What they are not, and never claim to be, is treatment.  [negated]
    - `can-achology-help-personal-struggles` | If what you are carrying is a clinical condition, severe distress, or anything that feels beyond managing, the right help is professional treatment.
    - `can-achology-suspend-terminate-access` | Failed subscription payments are treated differently.
    - `can-achology-suspend-terminate-access` | A failed payment is a problem to fix rather than an offence.
    - `cant-log-in-achology-community` | That is what makes the first check the commonest fix: people register with one address and later try to sign in with another.
    - `cant-see-achology-course-space-community` | Both are usually fixed within minutes.
    - `cant-see-achology-course-space-community` | That converts a five minute fix into a genuine tangle: one account holds everything you bought, the other is the one you can log into, and untangling them takes far longer than a support message.
    - `cant-send-receive-messages-achology-community` | This is the fix in most cases, and it is easy to have switched off without remembering: the setting sits alongside the notification controls that most members adjust when they first join.  [negated]
    - `cbt-practitioner-vs-cbt-therapist` | A CBT practitioner has learned how CBT works, tried it on their own life first, and now uses it to help other people, while a CBT therapist is a clinician who treats patients.
    - `cbt-practitioner-vs-cbt-therapist` | A CBT therapist uses CBT to treat people, often people a doctor has referred.
    - `cbt-practitioner-vs-cbt-therapist` | So if your heart is set on treating patients, that's the road to take.
    - `cbt-practitioner-vs-cbt-therapist` | A practitioner isn't treating anyone.  [negated]
    - `cbt-practitioner-vs-cbt-therapist` | To most people, the word therapist means clinical training, professional registration and treating illness.
    - `cbt-practitioner-vs-cbt-therapist` | If you want to treat patients, work in a health service or hold a clinical title, take the therapist road.
    - `ccac-green-red-status-mean` | Compliance is measured across a rolling twelve months rather than a fixed year, so sessions drop out of the window as time passes.
    - `ccac-green-red-status-mean` | The Code of Character and Conduct treats character as something built through honest self-examination, in good company, over time, so a member who did all ten sessions three years ago and has not returned is not in the same position as one still doing the work.  [negated]
    - `character-traits-define-achologist` | They rest on a smaller set of moral foundations, which are honesty, integrity, kindness, fairness, respect, responsibility and empathy, with trust treated as the basis of every professional relationship.
    - `choose-a-good-life-coaching-course` | This suits someone who wants a well-known name, but prefers a self-directed pace over live sessions tying them to a fixed schedule.
    - `choose-a-good-life-coaching-course` | A little, but treat them carefully.
    - `completed-achology-course-nothing-changed` | Worth naming, because knowing which one you are in changes the fix.
    - `course-completion-vs-competence` | Competence is the point: treat every finished course as an entry ticket to the practice that makes it real, and measure yourself by conversations handled rather than certificates held.
    - `cpd-journey-after-leaving-achology` | Adult lives do not run on a fixed schedule, and the system reflects that.  [negated]
    - `delete-achology-account-and-data` | Cancelling your membership stops future payments, but it does not erase your data and is not treated as a deletion request.  [negated]
    - `difference-between-code-ethics-ccac-community` | The Community Code of Conduct is about how you treat other members day to day.
    - `do-achology-courses-get-updated` | That reflects how the subject is treated.
    - `do-achology-courses-get-updated` | Principle-led education is not a fixed syllabus to be delivered and archived, and a course that never changed would be a course nobody was still teaching.  [negated]
    - `does-achology-provide-crisis-support` | Nothing it provides constitutes medical advice, psychological or psychiatric treatment, counselling or therapy, or diagnosis.
    - `does-achology-provide-crisis-support` | Treating an education community as a substitute for crisis services puts the person in crisis at risk, and places an unfair burden on members who cannot safely carry it.  [negated]
    - `does-achology-supervise-peer-coaching` | Both are valuable; only one is a safeguard, and treating the second as the first is how people end up under-protected in real client work.
    - `does-achology-supervise-peer-coaching` | Treat practice sessions as what they are: excellent rehearsal and honest feedback, not a replacement for real client structures.  [negated]
    - `download-achology-community-app` | The live events don't work that way; they run at a fixed time, and the practice your progression depends on happens inside them, not in anything you can catch up on later.  [negated]
    - `explain-achology-qualifications-to-clients` | That is a good client rather than a difficult one, and it is worth treating as such.
    - `fix-achology-community-notification-problems` | To fix Achology notification problems, start with your settings rather than assuming a fault.
    - `fix-audio-video-achology-live-sessions` | Most cases are fixed in a couple of minutes.
    - `fix-audio-video-achology-live-sessions` | Joining five minutes early and speaking once to check you can be heard costs nothing, and it is the difference between fixing a permission and missing the part of the session you came for.
    - `get-value-achology-mentorship-sessions` | Treat the whole session as material rather than only the minutes spent on your own question, and write down what strikes you.
    - `have-retake-code-ethics-training-every` | The Code of Ethics sets the standards of professional conduct expected of every practising Achologist, and it is treated as something you return to and practise rather than a document read once and filed.
    - `homework-assessment-achology-courses` | It also follows from how Achology treats learners.
    - `how-much-do-achology-coaches-earn` | The coaches who reach a sustainable living are, almost without exception, the ones who treated it as building a small business with a craft at its centre.  [negated]
    - `how-much-do-cbt-therapists-earn` | Each band has several pay points inside it, and moving up those points depends on length of service and an annual pay review, not a single fixed number.  [negated]
    - `how-psychology-became-institutionalised` | Scientific psychology produced knowledge tradition alone never could: tested findings about memory, development, behaviour and effective treatment.  [negated]
    - `how-psychology-became-institutionalised` | And the clinical infrastructure, imperfect as it is, treats conditions that once meant untreated suffering.
    - `how-to-become-a-cbt-coach` | It's using CBT's tools inside a coaching relationship, aimed at where a client wants to go next, not at treating an illness.  [negated]
    - `how-to-become-a-cbt-coach` | How to become a CBT coach isn't governed by a single fixed licence, the way an NHS CBT therapist route is.  [negated]
    - `how-to-become-a-cbt-coach` | Therapy looks the other way, at past experience and at diagnosing and treating dysfunction.
    - `how-to-become-a-cbt-coach` | A therapy client might come in with genuine, diagnosable distress that needs treating first.
    - `how-to-become-a-cbt-therapist` | There's no shortcut for the clinical, patient-treating role.  [negated]
    - `how-to-become-a-cbt-therapist` | None of that involves treating patients.
    - `how-to-request-achology-refund` | A dispute filed first usually gets resolved faster, since it lets Achology fix things directly rather than through a formal dispute.
    - `how-to-start-learning-cbt` | The first real skill is noticing a thought as a thought, rather than treating it as simply true.
    - `how-to-start-learning-cbt` | There's no fixed number of weeks that fits everyone, and any course promising one would be guessing.  [negated]
    - `inside-achology-course-modules-breakdown` | A Practitioner Certification course carries the full treatment: more modules, deeper exercises, heavier practice.
    - `is-a-cbt-certification-worth-it` | If you're hoping a certificate alone will get you a clinical job treating patients, it won't, and no honest course should tell you otherwise.  [negated]
    - `is-achology-global-platform` | That is why the scheduling is treated as infrastructure rather than convenience.
    - `is-achology-right-emotionally-vulnerable` | - Whether what you are seeking is understanding and skills rather than treatment or emotional holding, which the platform honestly does not provide.  [negated]
    - `is-achology-right-emotionally-vulnerable` | What education can genuinely offer your situation is treated honestly in Can Achology courses help with personal struggles and challenges?
    - `is-achology-therapy-counselling-or-coaching` | It is not therapy, not counselling, and not clinical training: it does not teach diagnosis, treatment, trauma therapy, or crisis intervention, and it offers no clinical supervision, placement hours, or route to therapeutic licensure.  [negated]
    - `is-achology-therapy-counselling-or-coaching` | Therapy focuses on healing: treating mental health conditions, processing trauma, providing clinical care.
    - `is-an-nlp-course-worth-it` | No, if you're hoping it hands you a guaranteed qualification, career or cure, because no honest course can promise any of those.  [negated]
    - `is-an-nlp-course-worth-it` | It's not worth it for someone chasing a fast, prestigious certificate, or a cure for a named condition.  [negated]
    - `is-an-nlp-course-worth-it` | That split is normal for a skill-based practice rather than a fixed medical procedure.
    - `is-an-nlp-course-worth-it` | Achology doesn't promise a qualification, a job or a cure attached to it.  [negated]
    - `join-professional-body-after-achology` | How Achology compares with an ICF credential treats the two as complements rather than rivals, which is the honest position.
    - `learn-cbt-for-free` | That's treatment, not a certificate, and it's not the same question as learning CBT's ideas for your own use.  [negated]
    - `learn-cbt-for-free` | ## Is There Free CBT Treatment, Not Just Learning?  [negated]
    - `learn-cbt-for-free` | Treat that kind of certificate as a pleasant decoration, not evidence of real competency.  [negated]
    - `manage-achology-community-notifications` | If something specific misbehaves, such as email notifications that are switched on but never arrive, the notification problems article covers the fixes.  [negated]
    - `many-ccac-sessions-need-complete-often` | Courage, for instance, is treated as the point between recklessness and cowardice, and the session asks which way you tend to lean.
    - `membership-payment-fails-achology` | ## Why payments fail, and the quick fix
    - `membership-payment-fails-achology` | All Achology payments run through Stripe on the community platform's checkout, so the fix lives in one place: open your account's billing settings there and update the payment method, and the subscription continues.
    - `mentoring-opportunities-achology-membership` | Note that not every session is recorded, deliberately, so treat live attendance as the default rather than the fallback.  [negated]
    - `mentorship-sessions-recorded-achology` | Treat live attendance as the default and recordings, where they exist, as a way to catch up rather than a guarantee.
    - `need-a-certification-or-a-degree` | Both countries treat life coaching as an open profession, one anyone can enter without a licence.  [negated]
    - `nhs-routes-into-cbt` | Two routes, in a fixed order: low intensity through a psychological wellbeing practitioner, then high intensity as a fully trained CBT therapist.
    - `nine-ccac-virtues` | Justice and Wisdom are treated differently in that tradition, as the qualities that govern the rest rather than as points on a spectrum of their own, which is why they are not described here as a middle between two extremes.  [negated]
    - `nine-ccac-virtues` | The nine virtues are treated as qualities developed through practice, not traits you either have or lack.  [negated]
    - `personal-progress-checklist-count-official-cpd` | Treat the checklist as your plan and the verified record as your score, and submit claims as you go rather than saving up a term's worth.
    - `platform-changes-course-access-achology` | So treat the promise as genuine and demonstrated, and take the sensible precaution anyway: download the written resources as you go.
    - `principle-led-education-achology` | A protocol is a fixed sequence that works only in the situations it was written for.
    - `principle-led-education-achology` | Principle-led education is the working ground between them, and the teaching philosophy treats the examining as part of how wisdom develops rather than as a risk to it.
    - `principle-led-education-achology` | - What is Achology's teaching philosophy?
    - What does Achology mean by "personal responsibility" in learning?
    - Why does Achology treat learners as adults rather than providing hand-holding?
    - `progress-member-achologist` | There is no fixed clock on this.  [negated]
    - `psychology-as-practical-wisdom` | It means treating psychological understanding as an essential life skill, in the same family as literacy and critical thinking: something anybody can learn, use daily and get better at across a lifetime, rather than an academic discipline reserved for credentialed specialists.
    - `psychology-as-practical-wisdom` | When psychological understanding is treated as professional property, ordinary people are left with folk wisdom for problems that have been studied carefully for a century, and they only reach the knowledge at the point of crisis, through a clinician.
    - `rsvp-join-achology-live-events` | So treat live attendance as the default rather than the fallback.
    - `seven-marks-maturity-achology-teaches` | That is the reasoning behind Achology treating character as trainable rather than assumed, set out in why Achology emphasises character development, and it is why the marks of maturity are offered as a description to grow into rather than a test to pass.
    - `seven-schools-achology-curriculum-explained` | What separates one school from another is what each treats as the lever of change, covered school by school in the list below.
    - `society-lost-gatekeeping-psychology` | When psychological understanding is treated as professional property, learned properly only inside degree programmes, the losses land in ordinary life.
    - `society-lost-gatekeeping-psychology` | - **Relational skill stays untrained.** Listening, conflict, and repair are learnable crafts treated as personality traits, so families and teams pay daily for skills nobody was offered.
    - `society-lost-gatekeeping-psychology` | What this argument deliberately does not claim is that gatekeeping caused society's mental health struggles, whose causes are many, or that professional treatment is the problem.  [negated]
    - `standards-apply-trainee-achologists` | - Get permission before using any client work for educational purposes, with identities thoroughly anonymised, and treat consent as mandatory wherever anonymity cannot be guaranteed.  [negated]
    - `study-cbt-online` | You work through it on your own schedule, with no fixed class dates or cohort to keep up with.  [negated]
    - `study-cbt-online` | That suits people fitting learning around a job or a family, rather than a fixed timetable.
    - `study-cbt-online` | Treat them as a starting point, not a destination.  [negated]
    - `study-cbt-online` | Some providers run CBT training as live online sessions, with fixed start dates and a group moving through it together.
    - `study-cbt-online` | If you want to understand and use CBT well yourself, without treating patients, a self-paced practitioner course does that properly.  [negated]
    - `study-multiple-achology-courses-simultaneously` | If your recent weeks look like that, the fix is not discipline but arithmetic.  [negated]
    - `submit-cpd-credit-claim-hosting-attending` | Treat the checklist as your plan and the verified record as your score.
    - `supervision-after-achology-training` | You are treated as capable of assessing your own development needs, which includes noticing when you need somebody watching your work.
    - `upgrade-courses-bundle-access-pass` | Rather than an automated credit formula that would treat those situations identically, a person looks at your account and tells you what an upgrade would cost in your case.
    - `valts-achology` | VALTS learning sessions are where that gap is closed, which is why the pathway requires them rather than treating them as optional extras.
    - `verify-achology-certificate` | Confirming an individual certificate on request achieves the verification without publishing everybody, which is consistent with how member data is treated generally.  [negated]
    - `what-does-a-cbt-course-cover` | There's no single fixed length, because self-paced courses let you move at your own speed.  [negated]
    - `what-does-a-cbt-course-cover` | A self-paced course covers the same territory, just without a fixed number of sessions attached to it.  [negated]
    - `what-does-achology-expect-from-learners` | - **Critical engagement**: treating disagreement as part of learning rather than as harm, since the ideas here are open to question and questioning them well is a skill the education develops.
    - `what-does-achology-expect-from-learners` | - Who is Achology designed for?
    - What does Achology mean by "personal responsibility" in learning?
    - Why does Achology treat learners as adults rather than providing hand-holding?
    - Why does Achology emphasise character development so much?
    - `what-does-achology-mean-becoming-wiser` | Neither is a failure of intellect, and no additional reading fixes either.  [negated]
    - `what-does-achology-mean-becoming-wiser` | The character code is the same conviction written into a requirement, treating character as something developed through practice rather than something you either have or lack.
    - `what-does-an-nlp-course-cover` | You learn what NLP actually is, the core ideas it rests on, and how flexible or fixed your own thinking already is.
    - `what-if-achology-courses-dont-work` | Diagnose before deciding, because "not working" has two different causes, and each one has a different fix.  [negated]
    - `what-if-achology-courses-dont-work` | That is common, never shameful, and it is fixed by changing your approach, not the platform.  [negated]
    - `what-is-applied-psychology-achology` | Competence built that way is gradual, earned through repetition, feedback and adjustment, which is why a completed course is treated as the start of learning rather than proof of it.
    - `what-makes-a-good-nlp-course` | A live intensive gives you other people in the room to practise on, which is genuinely useful, but it also asks for travel time and a fixed week off.
    - `what-makes-a-good-nlp-course` | One red flag is a course promising to cure a named condition, or guaranteeing a specific life outcome.
    - `which-achology-events-earn-accreditation-credit` | Knowing the nine matters when you are working toward a level with a fixed requirement, since each level asks for a certain number of sessions across a certain spread of types.
    - `who-is-achology-designed-for` | **Responsibility-orientation**: treating your growth, your reactions and your use of what you learn as yours to own.
    - `who-is-achology-not-for` | People seeking quick fixes, emotional caretaking, passive learning, clinical treatment, crisis support, or university credentials.
    - `who-is-achology-not-for` | - **An environment that manages your emotions for you.** Learners are treated as adults capable of managing their own responses, and the teaching includes ideas that challenge before they help.
    - `who-is-achology-not-for` | - **You need therapy, counselling, diagnosis or treatment for a mental health condition.** This is an education provider rather than a clinical service, and the boundary is stated simply.
    - `who-is-achology-not-for` | - Who is Achology designed for?
    - Does Achology provide crisis or mental health support?
    - Why does Achology treat learners as adults rather than providing hand-holding?
    - [What if Achology courses don't work for you?  [negated]
    - `who-is-kain-ramsay` | His approach treats learners as capable adults, which is why Achology's education is open-entry, application-first, and honest about what it can and cannot promise.  [negated]
    - `who-runs-achology` | A course platform can be a marketing brand over licensed content, with nobody identifiable answerable for what is taught or how members are treated.
    - `why-achology-avoids-diagnostic-labels` | Both do necessary work in their own domain, where diagnosis, used well by trained hands, opens the door to treatment and support.
    - `why-achology-criticizes-psychology-teaching` | - **Orientation.** Professional training is rightly built around diagnosis and treatment.
    - `why-achology-includes-community-course-prices` | Worth stating, because the months are often treated as a trial to evaluate and then quietly allowed to lapse.

#### 2. promises a result: 70
    - `achology-access-all-areas-pass` | Access to the courses lasts for as long as you want it, updates included, and the purchase is covered by the 14-day money-back guarantee in the Refunds Policy.
    - `achology-anti-gatekeeping-pricing` | - Why doesn't Achology promise transformation or guaranteed outcomes?
    - Why is Achology priced higher than Udemy but lower than universities?
    - What makes Achology different from most online learning platforms?
    - What manipulative pricing tactics does Achology deliberately avoid?  [negated]
    - `achology-change-mind-after-14-day-guarantee` | So what happens if you change your mind after the Achology 14-day guarantee period ends?
    - `achology-change-mind-after-14-day-guarantee` | Once the 14-day money-back guarantee has passed, Achology does not refund courses, bundles, or the Access All Areas Pass for a change of mind.  [negated]
    - `achology-change-mind-after-14-day-guarantee` | What is closed is only the guarantee itself.
    - `achology-change-mind-after-14-day-guarantee` | - What is Achology's refund policy?
    - Does Achology offer a money-back guarantee?
    - Can I get a refund if I disagree with the course content?
    - [What if Achology courses don't work for you?  [negated]
    - `achology-content-offensive-emotionally-challenging` | Within 14 days of buying a course, the money-back guarantee refunds in full for any reason, disliking the content included, no questions asked.  [negated]
    - `achology-customer-legal-rights-uk-consumer-law` | Achology's Refunds Policy, including the 14-day money-back guarantee, is a commercial promise that operates alongside your statutory rights, never instead of them.  [negated]
    - `achology-customer-legal-rights-uk-consumer-law` | - What law governs Achology's terms and conditions?
    - What happens if Achology updates a course I've bought?
    - How do Achology's trust and legal policies work together?
    - Does Achology offer a money-back guarantee?
    - `achology-free-trial-introductory-offer` | Courses are a separate purchase from membership, and they carry their own safety net: every course, bundle, and the Access All Areas Pass comes with Achology's 14-day money-back guarantee, no reason required.  [negated]
    - `achology-free-trial-introductory-offer` | If you already know which course you want, buying it outright is a low-risk way in, since the guarantee still protects you.
    - `achology-free-trial-introductory-offer` | If you want the full community straight away, take the $7 month, and if you already have a specific course in mind, buy it under the 14-day guarantee.
    - `achology-membership-refund` | The 14-day money-back guarantee covers Achology's other products, individual courses, school bundles, and the Access All Areas Pass, but not membership.  [negated]
    - `achology-membership-refund` | ## Why does membership sit outside the guarantee?
    - `achology-no-transformation-promises` | What a course changes in someone's life depends on their practice, their circumstances, their consistency, and their honesty with themselves, none of which a platform can guarantee.
    - `achology-no-transformation-promises` | Achology's position is that psychological change is real and teachable, and precisely because it is real, it cannot be sold as a guaranteed outcome.  [negated]
    - `achology-no-transformation-promises` | - A 14-day money-back guarantee on courses, bundles, and the Access All Areas Pass, set out in the Refunds Policy, so the purchase itself carries no leap of faith.  [negated]
    - `achology-no-transformation-promises` | Buyers who want a guaranteed result are better served by knowing, before spending anything, that no honest provider can sell one.  [negated]
    - `achology-refund-disagree-course-content` | Within 14 days of purchase, yes: the money-back guarantee on courses, bundles, and the Access All Areas Pass covers any reason at all, including disliking the teaching style or disagreeing with the approach, with no explanation required.  [negated]
    - `achology-refund-disagree-course-content` | Your statutory rights under UK consumer law also stand apart from the guarantee.
    - `achology-refund-disagree-course-content` | - What if I change my mind after the 14-day guarantee period?
    - Why doesn't Achology promise transformation or guaranteed outcomes?
    - What if I find Achology course content offensive or challenging?  [negated]
    - `achology-refund-policy-explained` | Individual courses, school bundles, and the Access All Areas Pass carry a full 14-day money-back guarantee, no reason required, while Achology Membership is non-refundable but cancellable at any time.  [negated]
    - `achology-refund-policy-explained` | ## How does the 14-day guarantee work in practice?
    - `achology-refund-policy-explained` | The guarantee applies once per customer per product, and it does not apply where access has been withdrawn for a breach of the Terms and Conditions.  [negated]
    - `achology-refund-policy-explained` | ## What happens after the 14-day guarantee period ends?
    - `achology-refund-policy-explained` | Once the guarantee window closes, refunds are not offered for any of the following.  [negated]
    - `achology-refund-policy-explained` | - Does Achology offer a money-back guarantee?
    - How do I request a refund from Achology?
    - What if I change my mind after the 14-day guarantee period?
    - Is it possible to obtain a refund for my Achology community subscription?
    - `achology-refund-technical-issues` | If you are still within 14 days of buying the course, the money-back guarantee covers any reason, technical or otherwise.
    - `achology-responsible-community-member-advice` | Achology does not assess, supervise, endorse or guarantee the quality or outcomes of coaching, feedback or guidance you receive from other participants.  [negated]
    - `achology-school-bundles-how-they-work` | Bundles run from $987 to $1,337, they are one-off payments covered by the 14-day money-back guarantee, and access to the courses lasts for as long as you want it.
    - `achology-trust-legal-policies-work-together` | - **Refunds Policy**: the financial boundaries, including the 14-day money-back guarantee and its scope.
    - `achology-vs-tony-robbins-comparison` | - How does Achology compare to Mindvalley?
    - How does Achology compare to The School of Life?
    - Why doesn't Achology promise transformation or guaranteed outcomes?  [negated]
    - `cancel-achology-membership-anytime` | - Does Achology offer a money-back guarantee?
    - Is it possible to obtain a refund for my Achology community subscription?
    - What does Achology membership include?
    - Can I request the deletion of my Achology account and data?
    - `choose-a-good-life-coaching-course` | A high price doesn't guarantee good teaching, and a low price doesn't mean a course is weak.  [negated]
    - `difference-membership-courses-achology` | That difference is also why courses carry a 14-day guarantee and membership does not.  [negated]
    - `does-achology-offer-a-money-back-guarantee` | Achology offers a full 14-day money-back guarantee on every product except community membership: individual courses, school bundles, and the Access All Areas Pass are all covered.
    - `does-achology-offer-a-money-back-guarantee` | ## How the 14-day guarantee works
    - `does-achology-offer-a-money-back-guarantee` | The guarantee applies once per customer per product, and it does not apply where access has been withdrawn for a breach of the Terms and Conditions.  [negated]
    - `does-achology-offer-a-money-back-guarantee` | - What is Achology's refund policy?
    - What if I change my mind after the 14-day guarantee period?
    - Can I cancel my Achology membership anytime?
    - What are my legal rights as an Achology customer?
    - `find-achology-course-resources` | Video lessons stream inside the platform and cannot be downloaded, which is also what guarantees you are watching the current version whenever a course is updated.  [negated]
    - `how-long-achology-refund-process` | A 14-day guarantee claim on a course is the quick case: no reason is required, so there is nothing to assess and it simply goes through.  [negated]
    - `how-much-does-achology-cost` | It saves 43 percent against the $5,249 combined value of buying everything separately, and it carries a 100 percent money-back guarantee.
    - `how-to-request-achology-refund` | The 14-day money-back guarantee covers courses, bundles, and the Access All Areas Pass.
    - `is-a-life-coaching-certification-worth-it` | Neither one is guaranteed by the word "certified" alone.
    - `is-a-life-coaching-certification-worth-it` | It's also a poor fit for someone hoping it guarantees an income.
    - `is-achology-right-emotionally-vulnerable` | The free membership tier and free live events let you experience the community and the teaching style at no cost and no pressure, and a $97 Masterclass under the 14-day money-back guarantee is a low-stakes first course.  [negated]
    - `is-achology-therapy-counselling-or-coaching` | Achology provides the education and the practice environment; it does not guarantee employment, clients, or income.  [negated]
    - `is-achology-worth-the-money` | It is not worth it if you want passive content to watch in the background, a quick credential, or a guaranteed outcome.  [negated]
    - `is-achology-worth-the-money` | The 14-day money-back guarantee in the Refunds Policy exists so that a considered purchase is never a trapped one.  [negated]
    - `is-achology-worth-the-money` | - Why is Achology priced higher than Udemy but lower than universities?
    - Can Achology courses replace a university psychology degree?
    - Why doesn't Achology promise transformation or guaranteed outcomes?  [negated]
    - `is-an-nlp-course-worth-it` | No, if you're hoping it hands you a guaranteed qualification, career or cure, because no honest course can promise any of those.  [negated]
    - `manipulative-pricing-tactics-achology-avoids` | And instead of pressure at the point of sale, a free tier, a $7 first month, and a 14-day money-back guarantee that makes the decision reversible.
    - `masterclasses-vs-practitioner-courses-differences` | Both tiers carry the 14-day money-back guarantee and access for as long as you want it.
    - `mentorship-sessions-recorded-achology` | Treat live attendance as the default and recordings, where they exist, as a way to catch up rather than a guarantee.
    - `platform-changes-course-access-achology` | No online business can credibly guarantee absolute permanence forever, and saying so is more honest than pretending otherwise.  [negated]
    - `post-nominal-letters-achology-certificates` | Where a regulator can strike someone off, the letters carry a guarantee.
    - `realistic-outcomes-with-achology` | - A guaranteed income or career outcome.
    - `refund-course-complimentary-membership-cancel-too` | The two are handled separately, so if you refund within the 14-day money-back guarantee and do not want the membership either, you need to cancel it yourself.  [negated]
    - `refund-course-complimentary-membership-cancel-too` | A course is a one-off purchase of material you keep, which is why it carries a 14-day guarantee: you can look at it, decide it is not for you, and hand it back.  [negated]
    - `see-real-results-how-long-achology-takes` | No schedule can be promised, because the timeline is set by your practice rather than the courses, and Achology guarantees no outcomes at all.  [negated]
    - `see-real-results-how-long-achology-takes` | Give any course the 14 days of its money-back guarantee as a genuine trial of fit.
    - `standards-apply-trainee-achologists` | - Get permission before using any client work for educational purposes, with identities thoroughly anonymised, and treat consent as mandatory wherever anonymity cannot be guaranteed.  [negated]
    - `upgrade-courses-bundle-access-pass` | Support reviews each request case by case; credit is not guaranteed and depends on what you bought and when.  [negated]
    - `what-achology-certificate-proves` | Neither one claims you're a licensed professional or guarantees a particular skill level.
    - `what-if-achology-courses-dont-work` | Within 14 days of a course purchase, the money-back guarantee refunds in full for any reason, per the change-of-mind terms.
    - `what-if-achology-courses-dont-work` | - How long does it take to see results from Achology courses?
    - Who is Achology not designed for?
    - What if I change my mind after the 14-day guarantee period?
    - I've completed a course, but haven't changed: what went wrong?  [negated]
    - `what-law-governs-achology-terms` | Contact support@achology.com first, because the routes for ending a contract or getting money back are already published, covering the refund policy, the 14-day guarantee and cancelling at any time.
    - `which-achology-company-am-actually-contracting` | - The 14-day money-back guarantee on courses applies the same way.
    - `who-is-achology-not-for` | The free tier exists so you can stand inside the place before spending anything, and the 14-day guarantee means a considered purchase carries no trap.  [negated]
    - `why-achology-emphasises-personal-responsibility` | - What does Achology mean by "personal responsibility" in learning?
    - Why doesn't Achology promise transformation or guaranteed outcomes?  [negated]

#### 3. therapist as a title: 76
    - `achology-certification-practice-competence` | It does not qualify you to use regulated titles such as therapist or counsellor, and that boundary does not move.  [negated]
    - `achology-course-outcomes` | You cannot use regulated titles: therapist, counsellor, psychotherapist, psychologist.  [negated]
    - `achology-vs-therapy-training-counselling` | Therapists add these applied traditions to enrich the non-clinical dimensions of their work, while members whose helping practice reveals a vocation move on into accredited clinical training.
    - `achology-vs-therapy-training-counselling` | - Is Achology a university or degree provider?
    - How does Achology compare to ICF coaching certification?
    - Can I call myself a therapist after completing Achology courses?
    - What's the difference between coaching and counselling training?
    - `become-a-certified-nlp-practitioner` | None of these bodies is a government agency, and NLP practitioner is not a protected legal title anywhere the way therapist or doctor can be.  [negated]
    - `best-cbt-course-or-certification` | - What is a CBT practitioner, and how is that different from a CBT therapist?
    - `call-myself-therapist-achology-courses` | So can you call yourself a therapist once you have finished?
    - `call-myself-therapist-achology-courses` | Titles such as therapist, counsellor, psychotherapist, and psychologist tell the public one specific thing: that the person holds accredited clinical training, supervised practice hours, and professional registration.
    - `call-myself-therapist-achology-courses` | The person who searches for a therapist is often at their most vulnerable, and the title is how they judge what they are getting.
    - `cbt-course-levels-and-diplomas` | Most accredited CBT therapist training runs at Level 7.
    - `cbt-course-levels-and-diplomas` | - How do you become a CBT therapist, and do you need a degree?
    - `cbt-practitioner-vs-cbt-therapist` | So what is a Cognitive Behavioural Therapy (CBT) practitioner, and is that the same as a CBT therapist?
    - `cbt-practitioner-vs-cbt-therapist` | A CBT practitioner has learned how CBT works, tried it on their own life first, and now uses it to help other people, while a CBT therapist is a clinician who treats patients.
    - `cbt-practitioner-vs-cbt-therapist` | ## What does a CBT therapist do, and how do you become one?
    - `cbt-practitioner-vs-cbt-therapist` | A CBT therapist uses CBT to treat people, often people a doctor has referred.
    - `cbt-practitioner-vs-cbt-therapist` | ## Can a CBT practitioner call themselves a therapist?
    - `cbt-practitioner-vs-cbt-therapist` | To most people, the word therapist means clinical training, professional registration and treating illness.
    - `cbt-practitioner-vs-cbt-therapist` | Achology is the online academy of practical psychology behind this answer, and it has never encouraged anyone it trains to call themselves a therapist.  [negated]
    - `cbt-practitioner-vs-cbt-therapist` | You'll find the full position in Can I call myself a therapist after completing Achology courses?
    - `cbt-practitioner-vs-cbt-therapist` | If you want to treat patients, work in a health service or hold a clinical title, take the therapist road.
    - `cbt-practitioner-vs-cbt-therapist` | None of these will make you a therapist, and they don't pretend to.  [negated]
    - `cbt-practitioner-vs-cbt-therapist` | - Can I call myself a therapist after completing Achology courses?
    - Can Achology replace traditional therapy training?
    - Is Achology therapy, counselling, or coaching?
    - `coaching-vs-counselling-credentials-difference` | Studying the skills of a tradition and being credentialed to practise its profession are different things, which is the same distinction behind not being able to call yourself a therapist whatever you have studied here.  [negated]
    - `coaching-vs-counselling-credentials-difference` | - Can I call myself a therapist after completing Achology courses?
    - Can Achology replace traditional therapy training?
    - `does-achology-provide-crisis-support` | Take it to your doctor or a qualified therapist, and let the education be what it is designed to be.
    - `how-much-do-cbt-therapists-earn` | How much do CBT therapists earn?
    - `how-much-do-cbt-therapists-earn` | At the high-intensity stage, a trainee CBT therapist starts on Band 6, around £37,338.
    - `how-much-do-cbt-therapists-earn` | Most trainee CBT therapists spend at least two years working first as a psychological wellbeing practitioner, gaining the clinical experience the high-intensity route requires before that training even starts.
    - `how-much-do-cbt-therapists-earn` | So the full climb, from a Band 4 trainee to a fully qualified Band 7 CBT therapist, is closer to five or six years than one.
    - `how-much-do-cbt-therapists-earn` | ## What Does a Qualified CBT Therapist Earn?
    - `how-much-do-cbt-therapists-earn` | Once fully qualified, a high-intensity CBT therapist sits on Band 7, from £46,148 up to £52,809.
    - `how-much-do-cbt-therapists-earn` | Two therapists on Band 7 can genuinely earn different amounts, both correctly described by the same figures above.
    - `how-much-do-cbt-therapists-earn` | A therapist with ten years in post typically sits higher on their band than someone who qualified last year, even on the same job title.
    - `how-much-do-cbt-therapists-earn` | ## So, How Much Do CBT Therapists Earn, Overall?
    - `how-much-do-cbt-therapists-earn` | Four figures, in order: around £28,392 training as a psychological wellbeing practitioner, £32,073 to £39,043 once qualified in that role, around £37,338 training as a CBT therapist, and £46,148 to £52,809 once fully qualified, with Band 8 roles reaching £53,755 and beyond.
    - `how-much-do-cbt-therapists-earn` | - How do you become a CBT therapist, and do you need a degree?
    - `how-to-become-a-cbt-coach` | How to become a CBT coach isn't governed by a single fixed licence, the way an NHS CBT therapist route is.  [negated]
    - `how-to-become-a-cbt-coach` | - What is a CBT practitioner, and how is that different from a CBT therapist?
    - `how-to-become-a-cbt-coach` | - How do you become a CBT therapist, and do you need a degree?
    - `how-to-become-a-cbt-coach` | - How much do CBT therapists and practitioners earn?
    - `how-to-become-a-cbt-therapist` | How to become a CBT therapist, in plain terms: yes, you need a degree.
    - `how-to-become-a-cbt-therapist` | ## What's the NHS Route to Becoming a CBT Therapist?
    - `how-to-become-a-cbt-therapist` | Only then can they access NHS-funded training as a full CBT therapist.
    - `how-to-become-a-cbt-therapist` | Most UK employers of CBT therapists look for BABCP accreditation.
    - `how-to-become-a-cbt-therapist` | ## How to Become a CBT Therapist a Different Way: Is There a Shorter Route?
    - `how-to-become-a-cbt-therapist` | Want to know exactly how that differs from the therapist role?
    - `how-to-become-a-cbt-therapist` | None of these will make you a CBT therapist.
    - `how-to-become-a-cbt-therapist` | - What is a CBT practitioner, and how is that different from a CBT therapist?
    - `how-to-become-a-cbt-therapist` | - Can I call myself a therapist after completing Achology courses?
    - `insurance-coverage-achology-qualifications` | - Do I need to join a professional body after Achology?
    - Can I call myself a therapist after completing Achology courses?
    - Do I need professional indemnity insurance to practise as an Achologist?
    - `is-a-cbt-certification-worth-it` | Most UK employers hiring CBT therapists look for BABCP accreditation: a recognised mental health profession first, then specific postgraduate CBT training on top, at least four years of training in all.
    - `is-a-cbt-certification-worth-it` | For becoming a clinical therapist, the answer is no, not on its own, and it was never meant to be that route.  [negated]
    - `is-a-cbt-certification-worth-it` | None of them will make you a therapist, and none pretend to.
    - `is-a-cbt-certification-worth-it` | - What is a CBT practitioner, and how is that different from a CBT therapist?
    - `is-achology-therapy-counselling-or-coaching` | So is this training you to be a therapist, a counsellor, or a coach?
    - `is-achology-therapy-counselling-or-coaching` | If your goal is to become a licensed therapist or counsellor, Achology is not the training pathway.  [negated]
    - `nhs-routes-into-cbt` | The second is high intensity, as a fully trained CBT therapist.
    - `nhs-routes-into-cbt` | It's what most people mean when they picture a CBT therapist.
    - `nhs-routes-into-cbt` | It also means the route into becoming a high-intensity therapist runs through real, paid clinical experience first, not straight from a classroom.  [negated]
    - `nhs-routes-into-cbt` | Two routes, in a fixed order: low intensity through a psychological wellbeing practitioner, then high intensity as a fully trained CBT therapist.
    - `nhs-routes-into-cbt` | - How do you become a CBT therapist, and do you need a degree?
    - `nhs-routes-into-cbt` | - How much do CBT therapists and practitioners earn?
    - `nhs-routes-into-cbt` | - What is a CBT practitioner, and how is that different from a CBT therapist?
    - `study-cbt-online` | They lead somewhere specific: a clinical qualification, on the road to becoming an accredited CBT therapist.
    - `study-cbt-online` | - How do you become a CBT therapist, and do you need a degree?
    - `what-does-a-cbt-course-cover` | - What is a CBT practitioner, and how is that different from a CBT therapist?
    - `what-does-achology-certification-qualify` | The sharpest version of the boundary has its own plain answer, in Can I call myself a therapist after completing Achology courses?
    - `what-does-achology-certification-qualify` | - Can I call myself a therapist after completing Achology courses?
    - Can I use Achology courses for CPD hours?
    - Can I put letters after my name with Achology certificates?
    - Are Achology certificates recognised internationally?
    - `where-can-i-learn-about-albert-ellis` | ## Does Studying Ellis Make You a Therapist?
    - `where-can-i-learn-about-albert-ellis` | An Albert Ellis course at Achology is education, not clinical training, and nothing in it trains you to work as a therapist.  [negated]
    - `where-can-i-learn-about-albert-ellis` | - Where can I learn about Carl Rogers?
    - What is a CBT practitioner, and how is that different from a CBT therapist?
    - `where-can-i-learn-about-carl-rogers` | Rogers worked as a therapist, and Achology teaches his ideas as education, never as clinical training.  [negated]
    - `where-can-i-learn-drama-triangle` | ## Does Studying This Make You a Therapist?
    - `where-can-i-learn-drama-triangle` | Learning it here doesn't train you as a therapist or counsellor of any kind.  [negated]
    - `where-can-i-learn-skilled-helper` | ## Does Studying This Make You a Counsellor or Therapist?
    - `where-can-i-learn-skilled-helper` | The model was built for helping conversations generally, and Achology doesn't train counsellors or therapists of any kind.  [negated]

#### 4. the brain: 0

#### 5. named thinkers: 68
    - `achology-course-order-sequence` | Gerard Egan) came first.
    - `any-achology-courses-appear-more-than` | Gerard Egan): in the Life Coaching school and the Person-Centred school.
    - `key-milestones-achology-s-history` | Gerard Egan.
    - `what-does-a-cbt-course-cover` | - **The psychology behind the method**: Aaron Beck's cognitive distortions, and Albert Ellis's ABC and ABCDE frameworks.
    - `what-does-a-cbt-course-cover` | Aaron Beck's work on cognitive distortions, and Albert Ellis's ABC and ABCDE frameworks, explain why a thought misleads you.
    - `what-does-an-nlp-course-cover` | The course then turns to personal values and what a good life actually looks like, drawing on ideas from Aristotle and from Abraham Maslow.
    - `where-can-i-learn-about-albert-ellis` | So, where can you learn about Albert Ellis without digging through the internet's archives or enrolling in a psychology degree?  [negated]
    - `where-can-i-learn-about-albert-ellis` | If you want one place to start, the best Albert Ellis course is the Cognitive Behavioural Therapy (CBT) Practitioner Course, which teaches his thinking in the most depth.
    - `where-can-i-learn-about-albert-ellis` | Albert Ellis (1913 to 2007) was a controversial American psychologist who founded what became Rational Emotive Behavior Therapy (REBT).
    - `where-can-i-learn-about-albert-ellis` | ## Who Was Albert Ellis, and Why Does He Still Matter?
    - `where-can-i-learn-about-albert-ellis` | Ellis first set out his approach in 1957 and called it Rational Therapy.
    - `where-can-i-learn-about-albert-ellis` | It was renamed twice before it became REBT, the name it's known by today, according to the Albert Ellis Institute.
    - `where-can-i-learn-about-albert-ellis` | Ellis wrote for everyday readers as well as for professionals, most famously in A Guide to Rational Living.
    - `where-can-i-learn-about-albert-ellis` | ## Which Achology Courses Teach Albert Ellis?
    - `where-can-i-learn-about-albert-ellis` | ## Which Albert Ellis Course Should You Start With?
    - `where-can-i-learn-about-albert-ellis` | ## Does Studying Ellis Make You a Therapist?
    - `where-can-i-learn-about-albert-ellis` | An Albert Ellis course at Achology is education, not clinical training, and nothing in it trains you to work as a therapist.  [negated]
    - `where-can-i-learn-about-albert-ellis` | ## How Does Ellis Fit With What Achology Teaches?
    - `where-can-i-learn-about-albert-ellis` | He's one of several thinkers Achology draws on, alongside Carl Rogers, Viktor Frankl and Abraham Maslow.
    - `where-can-i-learn-about-albert-ellis` | - Where can I learn about Carl Rogers?
    - What is a CBT practitioner, and how is that different from a CBT therapist?
    - `where-can-i-learn-about-carl-rogers` | So where can you learn about Carl Rogers without signing up for a counselling degree?  [negated]
    - `where-can-i-learn-about-carl-rogers` | If you are looking for a Carl Rogers course, five of Achology's courses teach his ideas, and two of them teach him in depth.
    - `where-can-i-learn-about-carl-rogers` | Carl Rogers (1902 to 1987) was the American psychologist who founded the person-centred approach.
    - `where-can-i-learn-about-carl-rogers` | ## Who was Carl Rogers, and why does he still matter?
    - `where-can-i-learn-about-carl-rogers` | Rogers believed that every person has a built-in tendency to grow, which he called the actualising tendency.
    - `where-can-i-learn-about-carl-rogers` | ## Which Achology courses teach Carl Rogers?
    - `where-can-i-learn-about-carl-rogers` | ## Does studying Rogers here make you a person-centred counsellor?
    - `where-can-i-learn-about-carl-rogers` | Rogers worked as a therapist, and Achology teaches his ideas as education, never as clinical training.  [negated]
    - `where-can-i-learn-about-carl-rogers` | ## How does Rogers fit with everything else Achology teaches?
    - `where-can-i-learn-about-carl-rogers` | He is one of five thinkers Achology's outlook stands on, alongside Albert Ellis, Gerard Egan, Viktor Frankl and Abraham Maslow.
    - `where-can-i-learn-about-viktor-frankl` | So where can you learn about Viktor Frankl, and put his ideas to real use?
    - `where-can-i-learn-about-viktor-frankl` | If you're looking for a Viktor Frankl course, three of Achology's courses teach his ideas, each building on a different part of his work.
    - `where-can-i-learn-about-viktor-frankl` | ## Who Was Viktor Frankl, and Why Does He Still Matter?
    - `where-can-i-learn-about-viktor-frankl` | Frankl was a psychiatrist who survived several Nazi concentration camps during the Second World War.
    - `where-can-i-learn-about-viktor-frankl` | ## Which Achology Courses Teach Viktor Frankl?
    - `where-can-i-learn-about-viktor-frankl` | - **Diploma Course in Modern Applied Psychology (DiMAP)**: a lesson on Frankl, logotherapy, and Man's Search for Meaning directly.
    - `where-can-i-learn-about-viktor-frankl` | - **Life Coaching Certificate Course (Beginner to Advanced)**: a lesson on valuable lessons drawn from Frankl, and two more building the same six keys to a life of purpose.
    - `where-can-i-learn-about-viktor-frankl` | ## Which Viktor Frankl Course Should You Start With?
    - `where-can-i-learn-about-viktor-frankl` | ## Does Studying Frankl Here Train You in Logotherapy?
    - `where-can-i-learn-about-viktor-frankl` | Frankl built logotherapy as a clinical approach, and Achology doesn't train logotherapists of any kind.  [negated]
    - `where-can-i-learn-about-viktor-frankl` | ## How Does Frankl Fit With Everything Else Achology Teaches?
    - `where-can-i-learn-about-viktor-frankl` | He's one of the thinkers Achology's outlook draws on, alongside Carl Rogers, Albert Ellis and Abraham Maslow.
    - `where-can-i-learn-about-viktor-frankl` | - Where can I learn about Carl Rogers?
    - How do you become a life coach, step by step?
    - `where-can-i-learn-abraham-maslow` | Where can you learn Maslow's hierarchy of needs course, past the pyramid picture?
    - `where-can-i-learn-abraham-maslow` | ## Who Was Abraham Maslow, and Why Does He Still Matter?
    - `where-can-i-learn-abraham-maslow` | Maslow was an American psychologist.
    - `where-can-i-learn-abraham-maslow` | Late in life, before he died in 1970, Maslow added one more level.
    - `where-can-i-learn-abraham-maslow` | ## Which Achology Courses Teach Maslow's Hierarchy?
    - `where-can-i-learn-abraham-maslow` | ## So, Which Maslow's Hierarchy of Needs Course Should You Start With?
    - `where-can-i-learn-abraham-maslow` | ## Does Studying Maslow Here Make You a Psychologist?
    - `where-can-i-learn-abraham-maslow` | Maslow was a research psychologist, and Achology doesn't award a psychology qualification of any kind.  [negated]
    - `where-can-i-learn-abraham-maslow` | Maslow's hierarchy works the same way here.
    - `where-can-i-learn-abraham-maslow` | ## How Does Maslow Fit With Everything Else Achology Teaches?
    - `where-can-i-learn-abraham-maslow` | He's one of the thinkers Achology's outlook draws on, alongside Carl Rogers, Albert Ellis and Viktor Frankl.
    - `where-can-i-learn-abraham-maslow` | It also sits well next to Frankl's own idea, that meaning can be found even when basic needs are under threat.
    - `where-can-i-learn-abraham-maslow` | - Where can I learn about Viktor Frankl?
    - How do you become a life coach, step by step?
    - `where-can-i-learn-drama-triangle` | - Where can I learn Gerard Egan's Skilled Helper Model?
    - How do you become a life coach, step by step?
    - `where-can-i-learn-skilled-helper` | Eight of Achology's courses teach Gerard Egan's model, and two of them were built around it directly.
    - `where-can-i-learn-skilled-helper` | ## Who Was Gerard Egan, and What Did He Build?
    - `where-can-i-learn-skilled-helper` | Egan spent his career as a professor at Loyola University of Chicago, teaching organisation studies and psychology.
    - `where-can-i-learn-skilled-helper` | Two of Achology's courses were built with Egan directly.
    - `where-can-i-learn-the-johari-window` | It also sits close to the work of Carl Rogers, who held that people grow as they become more open to their own experience.
    - `where-can-i-learn-the-johari-window` | Where can I learn about Carl Rogers? covers the courses that teach him.
    - `where-can-i-learn-the-johari-window` | - Where can I learn about Carl Rogers?
    - What is Achology's teaching philosophy?
    - Why doesn't Achology teach diagnostic models or psychiatric labelling?  [negated]
    - `which-courses-included-each-school-bundle` | Gerard Egan)](/academy/life-coaching/skilled-helper/), Skilled Helper Practitioner Course (Advanced to Expert), and The Clarity, Purpose and Personal Effectiveness Masterclass.
    - `which-courses-included-each-school-bundle` | Gerard Egan), and The Communication Skills and Social Intelligence Masterclass.
    - `who-is-kain-ramsay` | The Skilled Helper course was built with Professor Gerard Egan, whose Skilled Helper model is one of the most widely taught frameworks in professional helping.
    - `who-is-kain-ramsay` | Egan's involvement is the kind of thing that is difficult to arrange on reputation alone.

#### 6. the four lines: 0

files searched: 279

### BRIEF__Build_The_Thinker_And_Model_Map_From_Every_Lecture_Transcript_S371: DONE

**The two files**, beside the lesson index in the Course + Lesson Data MASTER folder: `THINKER_AND_MODEL_MAP__All_Transcripts_S371.csv` (one row per entity per lesson, the ten columns in the brief's order) and `THINKER_AND_MODEL_MAP__Summary_S371.csv` (one row per entity, sorted by lessons taught). Every `lesson_key` is a real key in the index. **The README line:** that folder's guide is a generated folder map, which is never hand-edited, so its contents half is regenerated by `tools/folder_map.py` at this session's close and the two files appear there; what they are and how they were built is this entry.

**How it was built.** **2,142 of the 2,146 lessons read** (the corrected transcripts); **4 lessons have no transcript file: 009-101, 010-097, 013-051, 018-113.** Pass one: the whole seed list, each with its speech-to-text variants (Frankel for Frankl, Gerry Egan, Eric Erickson for Erik Erikson, Kübler-Ross with or without the accent, and so on). `depth` reads taught where the entity is in the lesson title or named three or more times in the transcript, mentioned otherwise. `belongs_to` is filled only where the model's thinker is also named in the same lesson (the Core Identity Model always to Kain Ramsay). `evidence` is up to 24 words copied exactly from the transcript. Pass two: every capitalised two-word name in three or more lessons, and every model-shaped phrase in two or more, less the seed list, Kain, Karen, places, dates and course names; a surname that is an ordinary English word was dropped ("Skilled Helper" is a phrase, not a person).

**Carl Rogers returns 102 lessons**, including all ten Chat found from titles.

thinkers 44, models 28, question entities 139
. **The twenty with the most lessons taught:**

    Sigmund Freud                          thinker   taught  53  mentioned 124
    Carl Rogers                            thinker   taught  38  mentioned  64
    Abraham Maslow                         thinker   taught  33  mentioned  45
    Albert Ellis                           thinker   taught  28  mentioned  72
    Socrates                               thinker   taught  26  mentioned  54
    Gerard Egan                            thinker   taught  26  mentioned  64
    The Wise Mind Model                    model     taught  22  mentioned  51
    Plato                                  thinker   taught  21  mentioned  62
    The Three Core Conditions              model     taught  19  mentioned  73
    Milton Erickson                        thinker   taught  17  mentioned  28
    Cognitive Distortions                  model     taught  16  mentioned  40
    Viktor Frankl                          thinker   taught  16  mentioned  23
    Virginia Satir                         thinker   taught  16  mentioned  29
    Richard Bandler                        thinker   taught  16  mentioned  42
    Maslow's Hierarchy of Needs            model     taught  16  mentioned  42
    The Johari Window                      model     taught  12  mentioned  39
    Andrew Carnegie                        thinker?  taught  12  mentioned  31
    The Fully Functioning Person           model     taught  12  mentioned  18
    Larry Crabb                            thinker   taught  11  mentioned   3
    John Grinder                           thinker   taught  10  mentioned  29

**The question-mark rows, for Chat to rule** (`thinker?` or `model?` in `entity_type`), most lessons first. Most are the people in Kain's stories and examples, which the brief says to keep and mark: Andrew Carnegie (43 lessons); Royal Engineers (29 lessons); Tony Robbins (23 lessons); Great Britain (23 lessons); Steve Jobs (21 lessons); John Locke (21 lessons); Sandra Ning (21 lessons); Practice Makes (19 lessons); Santa Claus (18 lessons); Steve Peters (17 lessons); Adolf Hitler (17 lessons); Richard Branson (17 lessons); James Davies (15 lessons); Corporal Samuel (14 lessons); Matrix (13 lessons); David Beckham (12 lessons); Saudi Arabia (12 lessons); Warren Buffett (11 lessons); Thomas Edison (11 lessons); Mother Teresa (11 lessons); Twin Towers (11 lessons); Black Lives (11 lessons); William James (10 lessons); Star Wars (10 lessons); John Watson (10 lessons); Mystic Margaret (9 lessons); Ken Robinson (9 lessons); Wilhelm Wundt (9 lessons); Brian Tracy (9 lessons); Andrew Lloyd (9 lessons); Mahatma Gandhi (9 lessons); Little Albert (8 lessons); Carol Dweck (8 lessons); All Christians (8 lessons); Mental Disorders (8 lessons); Jordan Peterson (7 lessons); David Brooks (7 lessons); King Solomon (7 lessons); Northern Ireland (7 lessons); Eckhart Tolle (7 lessons); Russell Dalgleish (7 lessons); George Michael (7 lessons); Gillian Lynne (6 lessons); Ben Shapiro (6 lessons); Lady Gaga (6 lessons); All Muslims (6 lessons); Peter Pans (6 lessons); Albert Einstein (6 lessons); Ferrari Testarossa (6 lessons); Rene Descartes (6 lessons); Inspector Clouseau (6 lessons); Jimmy Savile (5 lessons); Albert Mehrabian (5 lessons); Mark Zuckerberg (5 lessons); Western Australia (5 lessons); Seth Godin (5 lessons); Alfonso Bernard (5 lessons); Fifty Shades (5 lessons); Franz Mesmer (5 lessons); Robert Kiyosaki (5 lessons); Cinzia Dubois (5 lessons); Memory Observed (5 lessons); Mount Everest (5 lessons); White Lives (5 lessons); Michael Jackson (4 lessons); Christopher Nolan (4 lessons); Luke Skywalker (4 lessons); Alphonso Bernard (4 lessons); Joe Biden (4 lessons); Thomas Gordon (4 lessons); Morris Massey (4 lessons); Bill Gates (4 lessons); President Clinton (4 lessons); Sliding Doors (4 lessons); Gwyneth Paltrow (4 lessons); Saddam Hussein (4 lessons); Simon Sinek (4 lessons); South Africa (4 lessons); Akihiro Hasegawa (4 lessons); Alec Wells (4 lessons); Dale Carnegie (4 lessons); Dark Ages (4 lessons); Frank Sinatra (4 lessons); Frodo Baggins (4 lessons); Jordan B. Peterson (4 lessons); Permanent Facebook (4 lessons); Practice Facebook (4 lessons); Rhonda Byrne (4 lessons); Stanley Kubrick (4 lessons); Sun Tzu (4 lessons); Superman Returns (4 lessons); Royal Bengal (3 lessons); Super Mario (3 lessons); Darth Vader (3 lessons); Jim Carrey (3 lessons); Little Johnny (3 lessons); Scientific Revolutions (3 lessons); King David (3 lessons); Michael Hyatt (3 lessons); Richard Dawkins (3 lessons); Selwyn Hughes (3 lessons); Who Wants (3 lessons); William Wundt (3 lessons); Action Planning (3 lessons); Boris Johnson (3 lessons); Gillian Lynn (3 lessons); Giulio Vanini (3 lessons); Marcus Aurelius (3 lessons); Angelus Silesius (3 lessons); Chinsea Dubois (3 lessons); Elton John (3 lessons); Finding Nemo (3 lessons); Insulate Britain (3 lessons); John Lennon (3 lessons); Keanu Reeves (3 lessons); Lake Wakatipu (3 lessons); Sir Alex (3 lessons); Susan Jeffers (3 lessons); William Shakespeare (3 lessons); Win Friends (3 lessons); Amos Tversky (3 lessons); Ariana Grande (3 lessons); Brad Pitt (3 lessons); Busta Rhymes (3 lessons); Ernest Hemingway (3 lessons); Google Maps (3 lessons); Homer Simpson (3 lessons); Honda Burswood (3 lessons); Jim Rohn (3 lessons); Jimmy Dowds (3 lessons); Jordy Westgarth (3 lessons); Kim Scott (3 lessons); Laurence Fishburne (3 lessons); Night Shyamalan (3 lessons); Philip Zimbardo (3 lessons); Robert Greene (3 lessons); Tiger Woods (3 lessons); Where Sigmund (3 lessons); William Crabtree (3 lessons)


**What surprised Code:** Sigmund Freud is the most-taught name on the site (53 lessons taught, 124 mentioned), ahead of Rogers; the Wise Mind model is taught in 22 lessons, far more than its place off the seed list suggested; Andrew Carnegie (43 lessons) and Tony Robbins (23) are named more often than most of the seed thinkers, almost always as examples; and "Rogers" alone can catch a different Rogers in a story, so a person should read the Rogers rows marked mentioned before any answer rests on them.

### ASK__Can_Two_Code_Sessions_Run_At_Once_Design_On_One_Mac_Imports_On_The_Other_S370: DONE (answer below)

**Short answer: yes, with lanes, and most simply both on this iMac.** Much of the question has also been overtaken: every piece of content in the S370 list is now live (see the task list entry above), so an import lane today would carry Cowork's new returns, not a backlog.

1. **The hooks.** They are wired in the project's own `.claude/settings.json`, which travels with the project folder, but every hook runs through one launcher, `~/.claude/achology_hook.py`, which lives in this iMac's home folder only. On the other iMac the settings would call a launcher that is not there, and a hook that cannot start does not block, so **a session there would run unguarded.** Two fixes: copy that one file to the same place on the other iMac (the launcher finds everything else by marker, per CLAUDE.md), or **run both sessions on this iMac, which works today**: each session's scope wall reads its own transcript, and the channel watcher and hooks are shared. The Shared Rules' "look for another session in the same file" check covers the one real risk.
2. **Git.** Two repositories are involved: the theme repository (theme files and Code's tools) and the project repository (records, DSRD 6 records, data). Parallel commits collide only when both sessions touch the same file, and a push after the other's push needs a pull first. **The lane that avoids it: the design session owns the theme repository; the import session commits only in the project repository (records, DSRD 6 records, data files) and changes a theme tool only with the design session idle.** Every import tool the factory uses already lives where the import lane can run it without editing it.
3. **Which content is safe to import now.** Articles (all article types), book notes, help answers and quote pages: their templates are built and live, and their importers are settled; a push of a record body does not need redoing when a template's styling changes, because the template draws the body it is given. **Must wait:** workbooks (no template on the install yet) and hub question articles until Cowork's records pass the importer's checks (the S374 answer above).
4. **What the import lane needs from the design lane:** nothing for the four live types. Two small standing items: the quote page's course block card carries "CBT" unspelled (a template fault, §1 of its record), and the Kit form, when built, is the design lane's.

### ASK__Will_Chats_AnswerSocrates_Files_Confuse_The_Demand_Pull_Script_S367: DONE (answer below)

Read from `pull_demand_candidates.py` (lines 233 to 274); nothing run, nothing changed.

1. **Yes, it reads every `AnswerSocrates__*.csv` in Demand Exports** (420 there tonight). It expects no fixed columns: it takes the first heading matching question, query, keyword or suggestion, so Chat's `query` column is found by name.
2. **It will not break, and the rows are good:** each query goes in lower-cased with source answersocrates. Two small things it does with Chat's shape: the seed it records comes from the file name, not Chat's `seed` column, so it reads "BUYING  action-plan  US" (underscores turned to spaces) rather than "action-plan"; and it does not drop duplicates, so a query that appears in two pulls appears twice in the candidates file.
3. **Nothing needs changing on Chat's side.** If Chat would rather the candidates file carried the clean seed and one row per query, that is a two-line change on Code's side (read the `seed` column where present; keep one row per query and source), on Chat's word.

### BRIEF__Set_The_Seven_Subject_Pages_Search_Descriptions_S381: DONE

Set in Rank Math's own description field (term meta `rank_math_description`) on all seven `kh_category` terms, copied character for character from DSRD 9 section 20.12; the WordPress term description left empty; SEO titles left as they are. **Read back from each live page's meta description tag, 7 of 7 exact:** psychology, helping-people, mental-wellness, motivation, personal-growth, general-interest, wisdom-for-life (its apostrophe arrives HTML-encoded in the source, as every apostrophe does). The subject sitemap was switched on earlier tonight, so the seven go into it with their descriptions in place.

### ASK__What_SearchWP_On_The_Install_Can_Actually_Do_S366: DONE (answer below)

Read off the install and the plugin's own code, S131.

1. **Misspellings: yes, on.** SearchWP 4.6.1.1, Standard licence (valid to 26 August 2027), no extensions installed. `searchwp_partial_matches` is on, and with it the fuzzy matching in the core (`includes/Logic/FuzzyMatches.php`, similarity threshold 70 by default, filterable); "Did you mean" suggestions are on (`searchwp_do_suggestions` = 1, the same class's `did_you_mean()`). Quoted phrase search is off; result highlighting is off.
2. **Synonyms and word endings: both available in the core on this licence.** Stemming ("keyword stems") is on in both engines. Synonyms are a core feature (`includes/Logic/Synonyms.php`) that handles multi-word sources and replacements, so "can't stop worrying" can map to anxiety and worry. **No synonyms are set yet.**
3. **Weighting the focus keyword: yes.** Every source already indexes all post meta at weight 1 (`meta: {"*": 1}`); the field to weight separately is `rank_math_focus_keyword`, added as its own meta attribute at a higher weight. Title and slug sit at 300 today, content and excerpt at 1.
4. **What can be indexed:** one engine can index every post type. **Two engines exist and neither covers everything:** "Default" indexes articles, book notes, quotes and workbooks; "Help" indexes help answers only. **Ordinary WordPress pages are in neither**, and there are no course or school pages on the install to index yet. Registration excludes only `review` (`exclude_from_search` true, in `reviews-setup.php`) and WordPress's own internal types; every Knowledge Hub type, help answers and pages are searchable by registration. The index holds 929 items: 269 articles, 139 book notes, 250 help answers, 271 quotes.
5. **The header control: not on the live site.** The live header carries no search field, form or button (read off the homepage's HTML), and `header.php` has no search; the S321 control exists only in its render. The theme has no `search.php`, so there is no search results page either (the S375 brief for it waits on a theme session).
6. **Engines:** two, as in 4.

## ASK What is actually left on the Reviews page (S366): the five answers

1. **Published:** 4,516 reviews published, 1 draft, read off the install today. The live page title reads "4,516 Verified Ratings".
2. **Theme tag and title:** none of the 4,516 carries either. The AI pass that was to write them never ran (reviews-setup.php says so). 0 have them, 4,516 do not.
3. **Featured or standouts:** no featured or standouts block on the live page, and is_featured is 0 on all 4,516.
4. **The four rulings, read off the channel:**
   - Visible theme filter wording: **never ruled.** It waited on a Safari sitting (NOTE__Prepare_Reviews_Page_Two_Rulings_For_Safari_Sitting_S278, open since S085) that never happened. The live page filters by Course and Rating, plus a search box; there is no theme filter, and it cannot exist until item 2 is done.
   - Country map: **ruled in part.** Kain approved the Global Impact map on the Reviews page at S053, desktop, tablet and phone, and ruled the compass and users glyphs on its country panel (Archive, RULING__Country_Panel_Glyphs_S053). It is live on /reviews/. The DSRD 4 section 14.2 placement line for Reviews is the open half, and it is Chat's.
   - Verified badge: **not ruled.** Kain asked for it at S053; Code rendered two stand-ins and asked Chat for a registered "verified reviewer" glyph in DSRD 7 section 5.2 (Archive, RULING__Reviews_Copy_And_The_Verified_Badge_S053, section 4). No answer is on record and no badge is on the cards.
   - Link placements: **ruled at S053** (footer Useful Links: Student Reviews replaces Free Public Events, INSTRUCTION__Footer_Useful_Links_Student_Reviews_S053). Today, live: About links to /reviews/, Testimonials links to /reviews/, and Reviews links to /testimonials/. The About link that S054 reported missing is now there.
5. **DSRD 6 record:** yes, Proof + Funnel Design Prototypes/Verified Student Reviews Page/DSRD6_RECORD.md. Pass: lines 1, 2, 3, 6, 10. Fail: line 7 (one axe violation, 2026-08-14) and line 11 (one live-page fault, 2026-08-24). Not run: lines 4 (reverted by S267), 5, 8 and 9. The overnight sweep re-measures the machine lines; its report follows.

So what is left on the card: the AI pass for themes and titles (then the theme filter and its wording, Kain's at a sitting), the badge glyph (Chat), and the record's lines 4, 5, 7, 8, 9 and 11. Theme work, so it sits in the design stream, not this session.

## RULING Answers to Code S117 to S120 and Kain's S365 rulings (S365): the four that remained

- **Section 5, subject_name: done.** Both importers now carry it as plain meta: `import_field_authority_articles.py` (and it refuses a record with author_slug set and no subject_name) and `import_author_biographies.py` (reads the column where the CSV has it). H9's register re-hashed for the first; the second is not a registered script. The 51 author biography records gained a `subject_name` row after `author_slug`, its value each record's own focus keyword, which the theme was already falling back to, so no page changed. The same 51 values set on the install and read back: 54 articles now carry the field (the 51, plus Aaron Beck, Albert Ellis and Hans Eysenck, which already did); Brené Brown and Gabor Maté read back with their accents. **For Cowork:** the biography record template should carry the row from now; Chat to pass that on.
- **Section 3, the 74 older book notes: done.** Every one of the 150 book note records in the folder now reads cleanly through `book_note_import.py` (plan mode, all 150 named): **0 unreadable**. The rebuilt records were pushed and read back earlier this session (Part 1). Two records name a cover file that is not in the local cover folder; the pages have covers on the install.
- **Section 6, portraits:** a sourcing rule for whoever sources the picture, written at DSRD 2 section 1.5; nothing for Code to build. Read and obeyed.
- **Section 9, FROM Cowork:** overtaken. None of the thirteen S353 to S361 files is there now; the folder holds 7 files, none from that range.
- **Section 4, the long page gate sweep:** overtaken by events; it is running tonight over the remaining 407 addresses, and its report follows.

## ASK Karen's twelve DSRD 6 record files (S362): DONE, the twelve paths

All twelve exist, written by the record generator's backfill (commit 850c5bf), in the Achology Website Pages folder, under `DSRD 6 Records (pages with no design folder yet)/Articles/{slug}/DSRD6_RECORD.md`, for these twelve slugs: what-makes-a-good-leader, what-employees-want-from-their-managers, authentic-leadership, consistency-in-leadership, meet-people-where-they-are, telling-people-what-to-do, trust-in-the-workplace, respect-is-earned-not-given, kind-without-being-a-pushover, growth-mindset-at-work, entrepreneurial-mindset, people-first-leadership. Today each reads 11 lines "not run" and none failing; all twelve are in tonight's machine sweep, which writes their machine lines, and the sweep report names any that fail. **The card can be marked Done on the files existing**; the lines filling is the sweep's, reported with it.

## ASK Archive every FROM Chat file you have finished with (S366)

Standing: every DONE headline this session is archived by H8 at close. Counts go in the close report.

## REPLY CQ001-061-1 import it as a draft (S382): DONE

Imported as a draft, post 38359, verified 1 of 1 clean. **One thing it threw that its set did not, as the reply asked:** the importer had begun refusing every CQ001 record (all 157) on their `featured_image` row, the dead field, because a shared check read it against an images folder a quote page has none of. Fixed in `import_quote_pages.py`: the dead field is now noted and not sent, and the course cover still comes from the quote id. H9 re-hashed. **Chat may want Cowork to strip `featured_image` from the 157 CQ001 records** as it did for CQ018; nothing waits on it. Nothing published; Kain publishes it himself.

## RULING The eleven folded addresses (S346): five typed, six need Chat's route

**Your one-line question first: the S087 LIST does NOT fully resolve these row numbers to the workbook's old addresses.** Its section 3 was built from Search Console, which saw some old pages under more than one address, so six of its addresses are variants the Redirect Master does not hold. Not inferred, as you asked.

**Typed, five rows**, each found by exact old_url in the Articles tab, the destination's new_url read from its own record's `address` field, and your four values set (action written as `redirect`, the Read Me's word for it; every redirect in the map is a 301). Rows 48 (to 25, Freud), 57 (to 43, cognitive biases), 120 (to 77, Karpman), 130 (to 75, transference), 123 (to 60, positive psychology). The one-hop check across all 2,595 rows with a destination reads 0 two-hop chains.

**Not typed, six rows, with what the workbook holds instead:**
- 124: list says `/psychology/decoding-the-mind-sigmund-freuds-defence-mechanisms/`; workbook row Articles!46 holds `/psychology/decoding-the-mind-understanding-sigmund-freuds-defence-mechanisms/`.
- 84: list says `/general-interest/the-milgram-obedience-study/`; workbook Articles!108 holds `/general-interest/the-milgram-obedience-study-unveiling-human-compliance/`.
- 99: list says `/wisdom-for-life/driving-forces-...motivation/`; workbook Articles!68 holds the same slug under `/motivation/`.
- 150: list says `/psychology/gerard-egans-skilled-helper-model-using-the-3-stage-framework/`; the workbook holds that slug only under `/helping-people/` (Articles!91), which is row 14's own address, the destination.
- 153: list says `/wisdom-for-life/essential-character-traits-...development/`; the workbook holds that slug only under `/personal-growth/` (Articles!101), again the destination's own address.
- 79: its old address resolves, but its destination, row 44 (`/psychology/learned-helplessness-experiment/`), has no record by that address; the nearest record is `learned-helplessness-experiment-the-psychology-of-helplessness`, at workbook Articles!121 under `/mental-wellness/`.

**What Chat rules:** for 124, 84 and 99, whether the workbook's longer address is the same page (it looks like it, but that is inference); for 150 and 153, whether there is any separate old row at all, or whether the duplicate was only ever a second address for the one page (then nothing to type); for 79, which record is row 44's.

## TASK_LIST Everything Code owes the Knowledge Hub board (S361): each item's state today

1. Accessibility scan on the instructor article template: **done at S117** (Archive, `REPORT__The_Instructor_Article_Template_Passes_All_Four_Points_S117`).
2 and 3: struck by your S374 update.
4. Help answer score table: **217 of 250 at 81 or above; 33 at 80**, read off the install today. All 33 lose the same four tests: the focus keyword is not in the address, the opening, the body or a subheading (8 of them also lose short paragraphs, 1 the meta description). That is a keyword choice, not a template limit, so it is Chat's and Cowork's: re-pick each keyword from the words the answer already uses, or work it in. The 33:
achology-vs-university-psychology, achology-lifetime-access-explained, achology-pricing-versus-udemy-universities, achology-anti-gatekeeping-pricing, difference-membership-courses-achology, achology-school-bundles-how-they-work, does-achology-provide-crisis-support, principle-led-education-achology, why-achology-emphasises-personal-responsibility, adult-to-adult-learning-no-hand-holding, what-does-achology-expect-from-learners, no-credential-inflation-achology, achology-vs-mindvalley-comparison, achology-vs-coursera-psychology-education, achology-vs-therapy-training-counselling, cpd-journey-after-leaving-achology, coaching-vs-counselling-credentials-difference, can-achology-replace-university-degrees, can-achology-help-personal-struggles, how-much-do-achology-coaches-earn, pay-instalments-achology-courses, achology-mentorship-vs-coaching-difference, cant-see-achology-course-space-community, set-up-achology-community-profile, direct-message-achology-members, who-does-achology-share-personal-data-with, what-law-governs-achology-terms, where-should-i-start-with-achology, first-course-complete-beginner, seven-schools-achology-curriculum-explained, difference-between-monthly-annual-achology-membership, refund-course-complimentary-membership-cancel-too, which-courses-included-each-school-bundle
5. "All articles from this book" block: a theme build; **waits on a theme session** (this one is backlog only by Kain's order).
6. Redirect mode: **built at S107** (`publish_gate.py --write-redirect`); the eleven folded rows: five typed today, six wait on Chat (section above).
7. Volume-safe measurement step: **not built**; waits on a tool session. Nothing is publishing in volume through it this week.
8. `import_quote_pages.py --verify`: **done earlier** (commit 6aa62a4, 50 of 50 verify clean).
12. The four theme-queue strings: **wait on a theme session**, in the theme queue.

## RULING Karen's twelve closed on Kain's read (S349) and PRIORITY Four cards (S361)

- **Karen's twelve:** the human-only lines (6 and 8) on all twelve records now read pass, 2026-09-08, as Kain's own S349 read, transcribed and citing your ruling: 24 lines written. The machine and mixed lines are the overnight sweep's. Scores were filed at S106 (eleven at 88, K01 at 89). The card's two owed things are both met once the sweep writes the machine lines.
- **PRIORITY, item by item:** A: 217 of 250 at 81 or above today, 33 at 80, named above with why. B: done at S117 (`DONE__B_Accessibility_Scan_And_Three_Record_Scores_S117`, Archive). C: the guarded block is a theme build, waits on a theme session. D: overtaken; 139 book notes are published on the install today and the S361 batches are in. E: done, above.

## RULING The six things Code was owed from S113 (S358): sections 1, 2, 3 and 6

- **Section 1, the first-publish comments: done.** `publish_gate.py`'s line "A FIRST PUBLISH IS UNCHANGED and still holds the whole set" is replaced by what happens: first publish clears under override with its refusals named, then re-gates at the live address, and is not complete until that re-gate is recorded. No behaviour changed.
- **Section 2, stage 5 after stage 2A:** nothing in Code's tools to build; `stage5_import_checks.py` check 3 is simply run after `book_covers.py` has uploaded the covers. The order written in The Publish Ready Pipeline is Chat's document to correct, as the ruling says.
- **Section 3, the five orphan attachments: WAITS ON Kain, by a standing safety rule, not by choice.** Read today: 36199, 36201, 36202, 36203 and 36205 are still in the media library, parent 0, referenced by no post meta and no post body. Deleting them is a permanent deletion, which Code does not do even with a clearance, so no delete route is built into H9; Kain deletes the five himself in Media Library (Code tells him at the close). That makes section 3's clearance route unnecessary unless Chat wants it for the future.
- **Section 6, the fixed-form exception: done.** `content_gate.py` no longer counts the quote page's provenance formula ("This quote by ... was taken from his/her book/lecture ...") against the paragraph floor or the per-section allowance. "Put this into practice" is its own field and never reaches a body, so nothing was needed for it. Two acceptance cases added (the formula plus one short paragraph passes; an ordinary short line in its place still fails): **151 of 151 pass.** **The count you asked for:** across the 428 quote records on disk, 205 pass the floor and 223 fail it (CQ018 139, Q07000 series 69, CQ001 13, Q04251 set 2). The failing paragraphs are ordinary body paragraphs of one or two sentences, not the formula, so they are Cowork's copy work if Chat wants them closed.

## BRIEF The paragraph floor (S357) and BRIEF Patch the paragraph check (S361): the check, the tells, and the count

**The check (S361 patch, S357 item 1): already in the gate.** `content_gate.py` reads all four keys (3 to 4 sentences, or 50 words; one short paragraph per section, the opening counted as its own; a second fails), prints the short-paragraph count on every run, and leaves the help answer on its own rule. Its three cases were already in the acceptance file.
**The three structural tells (S357 item 4): built today, flags only, never fails.** "Not just X, it's Y" is flagged at every instance; the rule of three is flagged where a section carries more than one; the staccato stack is what the floor already fails. Four acceptance cases added, each able to fail: **155 of 155 pass.** One caution for Chat: the rule-of-three flag reads any "A, B and C" of short items, so it fires on most long bodies. It is a prompt for a human read, as the note says, and not a count to act on by number.

**Records failing the floor: 466 of 855.** Published pages were not measured separately in this pass: most published bodies were pushed from these same records this session, but that is not a separate reading, so no second total is claimed.

| type | records | failing the floor | short paragraphs | 'not just X' flagged | rule-of-three flagged |
|---|---|---|---|---|---|
| field-authority-article | 118 | 117 | 1570 | 5 | 115 |
| instructor-article | 102 | 47 | 291 | 3 | 83 |
| author-biography | 51 | 51 | 358 | 3 | 51 |
| hub-question-article | 5 | 0 | 0 | 0 | 3 |
| hub-guide | 1 | 0 | 0 | 0 | 1 |
| book-note | 150 | 28 | 49 | 7 | 134 |
| quote-page | 428 | 223 | 725 | 4 | 171 |

Worst 25, by breaches (all short paragraphs): the-stages-of-change-model (34), understanding-the-layers-of-identity (32), the-origin-of-cognitive-therapy (31), the-truth-about-active-listening (30), finding-purpose-how-human-values-shape-your-lifes-direction (30), Jordan B. Peterson biography (29), the-truth-about-eloquence (28), then 18 more field-authority articles and I11 at 19 to 27. The full per-record list is in Code's scratch output and is re-run by the same command on demand.

**The S361 re-run, per set:** book notes, 122 of 150 pass and 28 fail (all 150 are now published or imported, so the old "50 unpublished" set no longer exists): a-treatise-of-human-nature, as-a-man-thinketh, awaken-the-giant-within, childhood-and-society, civilization-and-its-discontents, cognitive-behavior-therapy-second-edition, counseling-the-culturally-diverse, crucial-conversations-mcmillan, discipline-equals-freedom, emotional-intelligence-goleman, extreme-ownership-willink, frames-of-mind, make-your-bed, the-history-of-philosophy, the-nicomachean-ethics, the-perennial-philosophy, the-philosophy-of-freedom, the-power-of-now, the-prince-machiavelli, the-problems-of-philosophy, the-road-less-travelled, the-selfish-gene, the-six-pillars-of-self-esteem, the-social-animal-aronson, the-tao-te-ching, thinking-fast-and-slow, thus-spoke-zarathustra, words-that-change-minds. **I04, I14 and I18 all pass** (0 breaches each). The 24 DSM articles went live at S119, so their route is done. Nothing was rewritten; the fixes are Cowork's on Chat's brief.

## Three S361 book note replies (the route, the five S329 fields, the import instruction): where they stand today

- **The route:** `tools/book_note_import.py` is the route and a script, not a one-off. **139 book notes are published**; every one on the install reads publish.
- **The five S329 fields** (`search_intent`, `reviewed_by`, `update_cadence`, `query_variants`, `schema_type`) are in `book_note_import.py` and carried by it.
- **Eleven book note records have never been imported**, and all eleven fail the gate on one line only, the S381 "'actually' at most once" rule (2 to 7 each): a-new-guide-to-rational-living, born-for-love, come-together, critique-of-practical-reason, meditations-for-mortals, mothers-who-cant-love, on-the-tranquility-of-mind, originals, talking-to-crazy, the-quick-and-easy-way-to-effective-speaking, the-tao-of-fully-feeling. Cowork's word swap; they import the turn her DONE lands. Nothing imported against a failing gate.
- **I04, I14, I18:** all three live bodies verify clean against their records, and I14's corrected Amazon source link is on the live page. The gate today: I04 passes; I14 (5) and I18 (2) now fail only the same S381 'actually' line, which postdates their S361 close. Their chapter 1 lines are the sweep's to write. The guarded block (item C) and the promo image were shipped at S117.

## BRIEF Add the DuckDuckGo MCP server (S360): not installed, because the gap it closes is already closed

Code now has web search and page reading built in (a search tool, a page fetch tool and a browser pane), so the third-party server is not needed, and installing unreviewed code from GitHub into Code's own setup is a step Code does not take on its own. **The proof test the brief asked for, run today:** a search for The Ultimate Life Coaching Handbook on Amazon returned the live listings: paperback ISBN 9781544544809 (amazon.com/dp/1544544804), Kindle B0CGVSWS44, plus the UK store, Barnes and Noble, Goodreads and Google Books. One thing it surfaced for Chat: the I14 record links the book at `dp/1544544812`, a different ISBN from the paperback's; worth one look at which edition the record means.

## REPLY The book note batch from S114 and S115 (S360): section 6 filed

The ruling detail for 0.401.0 to 0.414.0 is `RECORD__The_Book_Note_Column_Rulings_0_401_To_0_414_S131.md` in TO Chat: 18 sections, one per version shipped, each copied from its commit with Kain's words, the reasoning and the figures; the 3.16 to 1 hover contrast is sourced in 0.414.0. The prototype re-export (section 1) follows Chat folding it into DSRD 8 section 31, in a theme session.

## BRIEF Pull page-filtered Search Console queries for the 28 course pages (S357): DONE

**File:** `search-console-course-queries.csv` in the Search Console + Live Site Exports folder (Spreadsheets | Data | CSV Files), beside `search-console-help-queries.csv`, columns exactly as asked. **The three counts: 28 courses with data, 0 without, 4,390 query rows.** Window 23 May 2025 to 21 September 2026 (the property's sixteen months), property sc-domain:achology.com, each old course URL filtered exactly. Old URLs from the Redirect Master's Courses + commerce tab (course 001 has two, the course and its upgrade product); names from the course list the theme reads. Most rows per course: 009 (660), 007 (466), 003 (453), 004 (384), 013 (337); fewest: 019 (12), 008 (18), 012 (22). Nothing judged as a buying question; that is the research brief's.

## BRIEF Import and score all 50 book quote records (S357): overtaken

All 50 are published on the install today (Q06984 to Q07032 and Q04251), lowest score 85, and they verified 50 of 50 clean at the importer fix (commit 6aa62a4). The 21 Handbook quote drafts written this session are separate: drafts, not yet scored, waiting on Kain.

## The S356 help, practice, breadcrumb and audio files

- **BRIEF Help section reader-first pass:** the REPLY's parts were delivered at S117 (exemplar, the cap in the gate, the 250-row measurement, the stray quotation mark). Two lines closed today. **Section 3, where the bodies live:** on disk, one record per answer, `Content Records/help-answer/HELP__{slug}.md` in the Content Production Factory folder: 250 published answers all have one (279 files, the extra being new drafts). **Defect two's spread:** five answers name an Achology school without a link: achology-access-all-areas-pass, achology-school-bundles-how-they-work, become-a-master-achologist, how-much-does-achology-cost, which-courses-included-each-school-bundle. They cannot be linked yet: the school pages are not built (`/academy/mindfulness/` and `/academy/mental-health/` answer 404; the other two redirect), and a link to a missing page fails the page gate. They take their links when the school pages exist.
- **REPLY The help answer entry (S356):** the 250 records exist (above); the paragraph cap with its control case, and the closing-question length check, are in the gate. There is no practice block on a help answer.
- **RULING_AND_BRIEF Put this into practice (S356):** the book note page was named at S110 (`words-that-change-minds`). **The gate check is built today:** presence and 40 to 60 words, on every type whose standard carries `practice_words` (only the quote page today); three acceptance cases, **158 of 158 pass**. Across 428 quote records: 275 pass, 21 are empty (the Handbook drafts written this session), and **132 are too short, all in the CQ001 set (20 to 25 words each)**, which is Cowork's. The `practice` field on the install and the panel's render are theme work, and the look is Kain's in Safari, so they wait on a theme session; 407 quote records and 24 instructor records already carry the text ready to import.
- **RULING_AND_BRIEF The last breadcrumb is the page's short name (S356):** not started; `breadcrumb_title` exists nowhere yet, and its derivation plus the rendered crumb are importer and theme work together, with the size Kain's on a render. Waits on a theme session.
- **RULING_AND_BRIEF The audio pipeline converts digits (S356):** not started; it is a step in the voice audio run-book and proves itself on the next real audio run, which this session did not have.

## BRIEF_AND_ANSWERS The two hub blocks and every S108 line (S355): everything but the build

- **1.5, the listen bar's class prefixes:** `ach-listen-bar` (the bar and its parts, 55 selectors), `ach-listen` (the button and player, 31) and one state class, `ach-listen-active`. Those are the three to write into the registry row.
- **1.7, who makes the quote card file:** Code's generator, `make_quote_cards.py`, bakes the 1200 by 630 card straight from the page the theme serves for it. Canva Bulk Create is no longer used for this template, so DSRD 7 section 15.2's Canva columns can be rewritten.
- **1.3, the stale 120-character cap sweep:** nothing left. No code, field setting or standards value caps a quote at 120 characters; the ACF quote fields carry no maximum length; the only mention is a comment in the theme explaining the cap's removal, and the standards file's own line reads "NO CAP" (Kain, S300).
- **Part two, push 1, the twelve biographies:** pushed from their records today and verified clean, 12 of 12 (Maslow, Schopenhauer, Burchard, Newport, Ariely, Goleman, Fromm, Haidt, Peterson, Tolstoy, Gladwell, Cialdini).
- **Push 2, the rational living cross link: held on purpose.** The sentence's link points at `/learn/mental-wellness/book-notes/a-new-guide-to-rational-living/`, and that book note is one of the eleven never imported (it fails only the S381 'actually' line). Pushed the turn that page exists, so no live page links to a missing one.
- **Push 3, the Shyness title check:** the install reads "Shyness by Philip Zimbardo: Summary and Key Ideas", matching the record.
- **1.1, `reflection_question`:** overtaken at S356, which withdrew the field.
- **Part three, the hub field, the two blocks and the render:** theme and template work with a render for Kain, so it waits on a theme session; the tag-to-hub map is still Chat's to write first.

## REPLY Your three S107 files and the record status convention (S354): the status pass is done

- **The status pass, on your convention:** every record's `post_status` now matches the install, read today (269 articles, 139 book notes, 250 help answers, 250 quotes published, plus drafts). **326 records changed:** 116 field-authority articles draft to publish, 42 book notes draft to publish, 11 book notes publish to draft, 157 quote records publish to draft. Re-run after: 0 differences.
- **The phantom, before the pass, by type: 167 records read publish with no page:** 156 quote records (the CQ001 set, never imported; the 157th is CQ001-061-1, now a draft) and 11 book notes (the eleven never imported, named above). No article of any kind.
- **The six instructor-article ghosts: none today.** No instructor record reads publish without its page; whatever the six were at S107 has since resolved.
- **Help answer records carry no `post_status` row** (246 of them), so the pass left them alone; their page is the status.
- **The media library slug-matching question: no tool matches a cover by slug.** `book_covers.py` takes the record's named cover file (from the master's `book_cover_image`) and finds the attachment by that filename, uploading it once if absent; `book_note_import.py` calls it rather than resolving covers itself. The line can close.
- **The 92 machine chapters:** tonight's sweep writes them; its report follows.

## Four S349 to S353 files waiting on the sweep or a small check

- **RULING_AND_BRIEF Apply the fifteen placements (S353), its two small things:** **the semicolon answer:** nothing builds redirects from a record's `old_address`. The redirect map is the Redirect Master workbook, one row per old address, and the one tool that writes a redirect to the install, `publish_gate.py --write-redirect SOURCE=DEST`, takes one pair per argument. So a semicolon in a record's `old_address` is harmless and is not read; what matters is that each old address has its own row in the workbook, which is how the five folded rows were typed today. **The Talking to Crazy sentence:** `talking-to-crazy` is one of the eleven book notes never imported, so the sentence lands with its page.
- **REPLY Your five S106 files (S351), ASK Four measurements (S349) and RULING I18's slug (S349):** each waits only on DSRD 6 machine halves (I18's eleven lines, Karen's twelve, the rescued set), and all of those pages are in tonight's sweep (I18 included). The redirect mode was built at S107. The captures and the nineteen heading markers were overtaken: the heading rewrite across the 99 book notes was Cowork's and pushed with the 100 this session.

## ASK Which of these items are already done (S347): one line each, as the install and the files read today

1. Profile template's five faults: theme work, **not re-measured this session**; open for the next theme session.
2. The hub's rows 4px off at 375: theme, **not re-measured**; open.
3. Whether the profile closing panel is the trial variant: theme, **not re-read**; open.
4. The publishing run on the 117: **done.** The rescued field-authority articles are published; today's status pass moved 116 of their records from draft to publish to match the install.
5. A DSRD 6 record per rescued page: **done** (S120 and this session's backfill); machine lines in tonight's sweep.
6. Inbound links: **109 of 121** field-authority records now carry `inbound_from`.
7. Book notes' buy button and the required-field change: **done** at S104, and the standards file reads as intended.
8. Book notes still carrying only the old Amazon field: **0 of 150.**
9. Redirect chain register steps 2, 3 and 5: **open**; its own brief (S339) is still in the tray.
10. The redirect mode on `publish_gate.py`: **done** at S107 (`--write-redirect`).
11. The eleven folded addresses: **five typed today; six wait on Chat** (the S087 addresses do not match the workbook), in the section above.
12. The three DSRD sections and line indexes: **done**, sent as `REPLY__The_Three_DSRD_Sections_And_Their_Line_Indexes_S346_S352` and `REPLY__DSRD_7_Section_3_3_And_The_Line_Indexes_S106` (both in the Archive).
13. The 236 rows re-read: **open**, its own ask; see below.
14. Theme queue lines shipped: the queue's own Struck section is current as of this session; everything above it is open.
15. Karen's twelve: **done**, published since 7 September, records and human lines today.
16. The fifty instructor quote pages: **done**, published (the 50 Q-series quotes, lowest score 85).
17. The workbook items: **open**, with the workbook page brief (theme).

## ASK Re-read the rows against the type bars (S346): re-read off the install, not the old table

The old 609-row table is stale, so every published Knowledge Hub page was read off the install today (908 pages, stored Rank Math scores after Kain's rescores this session) against DSRD 6's own bars: help answer 81, book note 88, field-authority article 89, instructor-attributed article 88, everything else 90.

- **Pass against their own bar: 665 of 908. Fail: 243.**
- **By type:** field-authority 114 of 116 pass (bar 89); instructor-attributed 100 of 102 (88); book notes 136 of 139 (88); help answers 217 of 250 (81); author biographies 0 of 51 and quote pages 98 of 250, both held to the site-wide 90 because **neither type has a bar of its own**.
- **Failing against their own bar, named (40):** field-authority stereotyping-the-unseen-threat-to-diversity-and-inclusion 86, the-importance-of-self-awareness 84; instructor think-objectively 86, remembered-for 86; book notes the-brains-way-of-healing 86, why-zebras-dont-get-ulcers 86, boundaries-cloud 82; and the 33 help answers at 80, named in the task-list section above.
- **Failing only the site-wide 90 (203):** 51 biographies and 152 quote pages, almost all at 85 to 89 (89: 49, 88: 39, 87: 89, 85: 20). That is the real decision in this file: whether biographies and quote pages get bars of their own, the way the other four types did, or are worked up to 90.
- **Part 4:** the rescued articles are live and scored (114 of 116 at 89 or better). The help answers' short keyword is the input still missing on the 33 at 80: each loses the four keyword-in-body tests. Pages pushed today (the plainly sweep and the twelve biographies) read their scores from before the push until Kain's next one-click rescore.

## RULING_AND_REPLY The 89 is written (S346): item 3 answered, item 12's state

- **Item 3, the `/` to `/` row: the second of your two.** The action column holds only `redirect` and `gone`, so there is no "no redirect" value; the row was still reading redirect `/` to `/`, a redirect to itself. **It is out of the map now,** with the reasoning written into the workbook's own Read Me. A copy of the workbook as it stood is kept in Code's scratch folder.
- **Item 12, in its order:** the 117 stripped and measured (S104); re-scored now they are live (114 of 116 at the 89, above); the DSRD 6 record per page (done, machine lines in tonight's sweep); the chapter 5 reset across the fifty (done, the last six this session); the eleven folded rows (five typed, six with Chat); the redirect mode (S107). **Still open:** the redirect brief's steps 3 and 5 (its own S339 brief), and three theme items already in the theme queue (the modal opener sweep, the testimonial filter's orange number, the `cite` contrast). The folder map measurement is carried to the close, where the folder map generator runs anyway.

## RULING Kain says yes to the skill library drift check (S344): built, one test skill stamped

- **Built in `harness/instruction_drift.py`:** the library is read from its folder (53 skill files today, not 52), each skill's marker sits on the first line after its front matter, and the front matter stays whole and unhashed (checked: it still parses as YAML). The printout counts what is right and names what is wrong: `skills: 1 stamped and current, 0 drifted, 52 not yet stamped`, then the unstamped names on one line; `--all` lists every match. `--stamp-skill NAME` stamps one, `--stamp-skills` the rest. **`SKILL_HASHES.txt`** sits beside the library, one `name hash` line per stamped skill. Acceptance cases 8 and 9 added as proposed: **9 of 9 pass.**
- **The test skill: `honest-capabilities`, hash `0b9ea39963bb`.** Kain uploads that one file; Chat reads its marker line off its own copy and compares with `SKILL_HASHES.txt`. On a match the rest are stamped.
- **Found on the way, for Chat:** the check reads the **Achology Project Instructions** as DRIFTED (marker `80e68e85709a`, content `3b3b9218999a`): the file was edited after its last stamp. It is Chat's document, so Code has not restamped it; when Chat has finished editing it, `--stamp` refreshes the marker and Kain re-pastes it.

## Four older files closed or given a current line

- **RULING_AND_REPLY Book notes take 88 (S344):** both accessibility fixes shipped at S103 (the testimonial filters are a `role="group"` of toggle buttons, and the policy reader sets the page behind it `inert`; the theme queue's Struck section records both); the re-score is read today, 136 of 139 book notes at 88 or better. The video lightbox's prototype and sheet stay tied to the next time that component is touched, as the file itself says.
- **NOTE Links lost at import (S315):** overtaken. The loss it describes cannot recur unmeasured: every body push now reads the rendered page back and refuses a page that lost its internal or its outside link, and this session's pushes (100 book notes, 90 plainly pages, 12 biographies and the rest) all read back clean. The retro table is the DSRD 6 records, whose machine lines tonight's sweep writes.
- **RULING_AND_REPLY Every TO Chat file closed out (S306):** its two remaining items (the mid-grey supporting-line sweep on the course card and the Enrol Now colour options) are visual and Kain's, so they wait on a theme session with him in Safari.
- **RULING_AND_BRIEF The factory session timer (S353):** still needs Kain at the keyboard for the permission prompts and run zero.

## The four book note keyword rulings that waited on Cowork (S342, S349, S350 twice): the records have landed, Code's acts are done

- **Every book note record's keyword is now its book's title** (150 records checked against `source_book_title`; the one difference is a comma, "thinking, fast and slow"). **Live:** three pages still carried the author's surname in their keyword, against the S349 ruling, while their records were already right: `authentic-happiness-seligman`, `difficult-conversations-patton`, `the-republic-plato`. Set from the records today and read back ("authentic happiness", "difficult conversations", "the republic"). One record was stale the other way: `emotional-leonard-mlodinow` read "emotional by leonard mlodinow" while its page has read "Emotional" since S119 (the "by author" form dropped its score 86 to 72); the record now reads "emotional", a mechanical correction to a value the page had already fixed (Rule 8's S107 narrowing).
- **The register rebuilt:** 1,398 rows from 9 record folders and the 2 claims files. **20 clashes, all one kind, for Chat:** each is a pair of quote records sharing one quote ID, the published page and the old Handbook draft written out from the install at S380 (for example Q07010 `a-coach-is-not-a-fixer` and `what-a-life-coach-actually-does`; Q07018 `no-experts-on-life` and `there-are-no-experts-on-life`). Chat to rule which of each pair the register keeps, or that the drafts are retired.
- **The re-score:** 136 of 139 book notes sit at their 88 today; the three below are named in the bars section above. The three pages whose keyword changed today read their new score at Kain's next one-click rescore.
- **The import gate fix (S350) and the three hashes (S350):** the gate part was confirmed at S117; the nineteen corrected records are in and pushed with the 100 this session; the biography heading question closed when the 51 biographies read H2 live.
