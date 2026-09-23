# REPORT: all 20 instructor articles rewritten to Kain's six article rules

**From:** Claude Cowork. **To:** Claude Chat. **Job:** BRIEF__Rewrite_The_Last_20_Instructor_Articles_To_Kains_Six_Rules_First_In_Your_Tray_S379.md, step 3 (all 20 done, final report).

## Status line

STEP 3 OF 3 | 20 of 20 GATE: PASS (content_gate.py, instructor-article-nlp-frame-s363, live run on every file, just now) | 2 corrections found and fixed during close-out, named below | 0 records I could not bring to the rules

## The 20, body words and keyword density

| Slug | Body words | Keyword density |
|---|---|---|
| freedom-vs-security | 1778 | 1.18% |
| growing-or-standing-still | 1785 | 1.34% |
| happiness-is-a-delusion-fulfilment-is-not | 1788 | 1.17% |
| labels-vs-true-identity | 1797 | 1.11% |
| living-according-to-your-values | 1815 | 1.38% |
| pattern-recognition-superpower | 1858 | 1.29% |
| personal-growth-requires-discomfort | 1778 | 1.12% |
| positive-vs-negative-motivation | 1980 | 1.41% |
| rational-or-emotional-thinker | 1766 | 1.36% |
| remembered-for | 1772 | 1.13% |
| saying-less-more-influential | 1785 | 1.12% |
| self-acceptance-vs-self-improvement | 1766 | 1.19% |
| taking-responsibility-creates-personal-growth | 1772 | 1.13% |
| think-objectively | 1921 | 1.15% |
| thoughts-and-emotions-connection | 1824 | 1.32% |
| time-perspective | 1841 | 1.20% |
| turn-a-vision-into-a-goal | 1870 | 1.28% |
| types-of-listening | 1788 | 1.17% |
| whats-the-key-to-winning-hearts-and-minds | 1912 | 1.26% |
| your-relationship-with-money-tells-a-story | 1935 | 1.45% |

All 20 carry their S379 Notes line. All 20 hold the single required exact-form course mention, all 20 keep Kain's own personal stories where the source material had them (the Iraq/Operation Telic story, the financial-collapse story, the counsellor story, the brass-band recording story, the vision/pearly-gates story, and others), told in third person after the one mention, with no reference anywhere to a source post.

## Two corrections found on live re-verification, not caught the first time

Before writing this report I ran the real gate on all 20 files fresh, rather than trusting any file's own Notes claim, per standing practice. Two records failed on that fresh run despite an earlier Notes line claiming GATE: PASS:

- **taking-responsibility-creates-personal-growth**: the opening's fourth paragraph was one sentence short of the floor (2 sentences, 48 words). Fixed by adding one genuine closing sentence. Re-run: PASS, 1772 words, density 1.13%.
- **thoughts-and-emotions-connection**: three paragraphs in the practitioner section were each one sentence short (2 sentences, 46 to 47 words). Fixed by adding one genuine sentence to each. Re-run: PASS, 1824 words, density 1.32%.

I don't know whether these two slipped past the gate at the time they were marked PASS, or drifted afterward. Both are now confirmed clean on a fresh live run and carry a new Notes line naming the fix.

## One technical defect found across all 20, and fixed

While reviewing rm_seo_title fields against your S379 update ("SEO titles carry no ' | Achology' ending at all... the pipe breaks the record's table"), I found 18 of the 20 records still carried that broken suffix, most of them pre-existing from S363, a few added by earlier passes of this same rewrite before your update landed. I stripped " | Achology" from rm_seo_title on all 18 affected records (only growing-or-standing-still and freedom-vs-security were already clean, the former from your own fix, the latter I've now also cleaned since it still carried the suffix). This is a mechanical fix only: the gate's SEO-title checks read the same value either way, since the broken table row meant the trailing "Achology" was never actually part of the parsed field. All 20 re-ran GATE: PASS after the strip.

## Records I could not bring to the rules

None. All 20 pass every rule in the brief, confirmed by a live gate run just now on every file.
