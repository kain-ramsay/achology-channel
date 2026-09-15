# DONE: Job 2, all 24 DSM series instructor-articles now pass the paragraph floor

**Filed by Claude Cowork, Session 361. Date: 15 September 2026.**

## What was checked first

Before touching any wording, I went through the S358 sourcing register claim by claim against the 24 articles, matching each flagged fact (the DSM-I category count, the homosexuality removal date, the DID case-count chain, the autism percentages, the depression symptom count, the DSM-5-TR bereavement criteria, the hypomania criteria, the DSM cost figures, the Allen Frances spelling, the "Ms T" case, the 11-second interruption study, and the rest) to the article that actually uses it. Every single one was already correct: the series had already been drafted, or an earlier session had already corrected it, against this same register. None of the 24 needed a factual change. I have not touched a fact, a figure, a name, or a citation in any of the 24.

## What was fixed

Paragraph rhythm only, the one thing the gate was actually failing on in all 24 (confirmed: every file showed `GATE: FAIL (1)`, the rhythm check alone, nothing else). Same mechanical method used on Job 1 and the book-note batch: only sections that genuinely breach the rule are regrouped, the gate's own one-short-paragraph-per-section allowance is used before falling back to a natural-break split, and nothing is added, removed, or reordered beyond punctuation and capitalisation at a split point. Verified word-for-word identical against the originals afterward across all 24, and re-run through `content_gate.py` clean before touching the live files.

Breach count before and after, all 24 now zero:

| Article | Breaches before |
|---|---|
| a-diagnosis-actually-describing | 4 |
| a-false-epidemic-happen-without-anyone-lying | 19 |
| a-psychiatric-diagnosis-simply-wrong | 9 |
| blood-test-for-depression | 3 |
| bmi-decide-who-gets-eating-disorder-treatment | 26 |
| diagnosing-bipolar-disorder-in-children | 12 |
| diagnosis-be-scientifically-weak-but-still-useful | 28 |
| diagnostic-inflation-actually-happening | 13 |
| doctors-have-only-minutes-to-diagnose | 4 |
| does-a-diagnosis-do-to-the-person | 17 |
| everyone-agreeing-on-a-diagnosis | 3 |
| five-symptoms-mean-depression | 1 |
| homosexuality-was-a-diagnosis | 10 |
| hypomania-from-an-ordinary-mood-swing | 18 |
| is-my-grief-normal | 25 |
| mental-disorders-tripled-since-the-1950s | 5 |
| multiple-personality-diagnoses-spike-after-a-film | 7 |
| self-report-decide-a-diagnosis | 11 |
| the-definition-of-mental-disorder | 6 |
| the-dsm-5-cost-five-times-more | 6 |
| the-dsm-call-its-own-categories-porous | 11 |
| the-rise-in-autism-diagnoses-real | 12 |
| what-is-concept-creep | 9 |
| what-is-stepped-care | 28 |

**24 of 24 passing.** Path: `Content Records/instructor-article/`

OWED BACK: nothing on Job 2. Job 4's remaining 25 heading-mismatched book notes still wait on the ASK note filed earlier this session.
