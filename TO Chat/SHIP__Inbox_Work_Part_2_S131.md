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
