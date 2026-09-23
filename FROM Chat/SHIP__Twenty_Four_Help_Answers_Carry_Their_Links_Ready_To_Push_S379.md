# SHIP: all 24 held help answers now carry a checked outside link, ready to push

**From:** Claude Chat, S379, Wednesday 23 September 2026. **To:** Claude Code.
**Answers:** `ASK__Twenty_Four_Corrected_Help_Answers_Held_For_A_Link_S130.md` (archived with this).
**Board card:** Help section reader-first correction pass.

## What was done

Each of the 24 records in the help-answer folder of Content Records now carries one outside link, placed on words already in a sentence, at a page Chat read this session and confirmed says what that sentence claims. No other word changed. The two with no internal link (achology-code-character-conduct-ccac, six-achology-cpd-statuses) each gained one internal link to a page already linked elsewhere in the live section. The free trial answer also gained an internal link to /membership/, since its body had none. Each edit was confirmed by the returned diff.

| Record | Anchor words | Outside page |
|---|---|---|
| achology-anti-gatekeeping-pricing | tuition that usually means borrowing | https://www.gov.uk/student-finance/new-fulltime-students |
| achology-code-character-conduct-ccac | Aristotle's virtue ethics (plus internal: the Code of Ethics to /about/code-of-ethics/) | https://plato.stanford.edu/entries/aristotle-ethics/ |
| achology-code-ethics | virtue ethics | https://plato.stanford.edu/entries/ethics-virtue/ |
| achology-discussion-boundary-feels-unsafe | trust that and treat it as information | https://www.mentalhealth.org.uk/explore-mental-health/articles/tips-navigating-online-communities-while-supporting-your-mental-health |
| achology-free-trial-introductory-offer | you can cancel at any time (plus internal: Achology Membership to /membership/) | https://www.citizensadvice.org.uk/debt-and-money/banking/stopping-a-future-payment-on-your-debit-or-credit-card/ |
| achology-lifetime-access-explained | stops future payments | same Citizens Advice page |
| achology-no-transformation-promises | evidence | https://www.asa.org.uk/advice-online/substantiation.html |
| achology-payment-methods | PCI-compliant system | https://docs.stripe.com/security |
| achology-pricing-versus-udemy-universities | clinical psychology | https://www.careers.nhs.scot/explore-careers/psychology/clinical-psychologist/ |
| achology-teaching-philosophy | cognitive bias | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10071311/ |
| achology-vs-linkedin-learning-comparison | LinkedIn Learning | https://www.linkedin.com/learning/ |
| cips-when-need-them | coaching session | https://coachingfederation.org/about |
| course-completion-vs-competence | many hours of practice | https://doi.org/10.1037/0033-295x.100.3.363 |
| difference-between-monthly-annual-achology-membership | billed each month until you cancel | same Citizens Advice page |
| how-to-request-achology-refund | raising a chargeback with your bank | https://www.citizensadvice.org.uk/consumer/somethings-gone-wrong-with-a-purchase/getting-your-money-back-if-you-paid-by-card-or-paypal/ |
| is-achology-worth-the-money | £27,000 in tuition | https://www.gov.uk/student-finance/new-fulltime-students |
| no-credential-inflation-achology | "internationally accredited" stamps | https://eqar.eu/?p=143 |
| post-nominal-letters-achology-certificates | a regulator can strike someone off | https://www.hcpc-uk.org/news-and-events/blog/2023/understanding-the-regulation-of-psychologists/ |
| principle-based-reflective-discussion | reflective practice | https://www.hcpc-uk.org/news-and-events/blog/2021/reflective-practice-discover-a-range-of-resources-to-support-you/ |
| six-achology-cpd-statuses | continuing professional development (plus internal: the Society of Modern Applied Psychology to /accreditation/) | https://www.cipd.org/uk/learning/cpd/about/ |
| using-achology-content-branding-materials | copyrighted | https://www.gov.uk/copyright |
| valts-achology | practice, in company, with feedback | https://journals.sagepub.com/doi/10.1177/1745691616635600 |
| what-achology-certificate-proves | licensed professional | https://www.regulated-professions.service.gov.uk/professions/practitioner-psychologist |
| who-verifies-achology-cpd-claims | a registered provider of learning | https://ukrlp.education.gov.uk/ |

## The ask

Push each of the 24 through `article_body_update.py` as you did the 192. If the tool refuses any, say which and why, and Chat fixes it at the record. Outside links follow DSRD 1 section 6.4 as your importer already applies it.

## OWED BACK

The count pushed and read back off the install, and any refusal named.

*No em or en dashes in this file; checked before writing.*
