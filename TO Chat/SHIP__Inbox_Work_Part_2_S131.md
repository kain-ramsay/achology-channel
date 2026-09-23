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
