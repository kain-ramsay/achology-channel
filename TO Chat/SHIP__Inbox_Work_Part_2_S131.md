**Needs from Chat:** Kain's decision on a softening pass for the help section, from the contraction count below; everything else here is done and read back.

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
