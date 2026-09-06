# SCORE TABLE: eighty five article drafts, and the single point seventy seven of them are missing

**DOCUMENT TYPE:** score table and finding. Not a page spec.

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Commissioned by:** Kain, in the sitting, ahead of a publishing session he wants Chat and Cowork sitting in on.
**Stage:** The Publish Ready Pipeline stage 6, the score half. These records were imported at earlier sessions; this is the reading.
**Board cards:** the 83 rescued articles; Knowledge Hub score work.

---

## 1. What was measured, and how

Every one of the 85 article drafts on the install, read off the analyser in the WordPress editor by `tools/score_run.py`, which opens each editor under a write block and saves nothing. All 85 came back settled. One (35218) first returned a zero because its editor did not settle inside the deadline; it was re-read and is 89.

Word counts are the install's own `post_content` with its markup stripped, so they are the prose the analyser counts, not the raw field.

**Three of the 85 clear the bar of 90. Seventy seven sit on exactly 89.**

| Score | Articles |
|---|---|
| 91 | 3 |
| 89 | 77 |
| 88 | 2 |
| 86 | 1 |
| 84 | 1 |
| 73 | 1 |

## 2. Nothing is failing. That is the whole point

`tools/score_tests.py` across twenty of them: **eighteen pass all fourteen tests** and still read 89. A pass count cannot explain a missing point, and this tool's own history says so, because at S097 a promise was made from exactly that reading and moved nothing.

So the points were read instead, with `tools/score_breakdown.py`. On a typical 89:

```
summed: 76 of 85 across the tests that declare a maximum
EARNING LESS THAN THEY COULD:
  contentHasAssets    1 of 6
  lengthContent       4 of 8
```

76 of 85 is 89. **One more point is 77 of 85, which is 91.** There is no 90 available; the batch steps straight over the bar.

## 3. Where that one point is, measured rather than reasoned

`contentHasAssets` gives 1 for having pictures and wants a video for the other five. That is the same wall the book notes hit at S344 and it is not being chased here.

`lengthContent` is the other, and it is graded. Read off the pages either side of the step:

| Post | Words | lengthContent | Score |
|---|---|---|---|
| 35440 | 1,981 | 4 of 8 | 89 |
| 35424 | 2,043 | 5 of 8 | **91** |
| 35182 | 2,061 | 5 of 8 | **91** |
| 35434 | 2,394 | 5 of 8 | **91** |

**The ladder steps at 2,000 words.** Nineteen words separate 35440 from the bar. Every draft in the batch at 2,000 words or more scores 91; every draft below it scores 89 or less. There are no exceptions in 85 readings.

## 4. Why this is not padding, which is the part I checked hardest

DSRD 6 is explicit that length is graded and never padded, and no page is lengthened to please a plugin. So the question is not whether 2,000 words scores better. It is what these articles are supposed to be.

**Every one of the 161 records in the `field-authority-article` folder states the same band, in its own gate printout: `standard 1600 to 2400`. 155 of them carry the same sentence: "About 2,000 words".** The standard read from is DSRD 2 section 3.2, the six-section article template.

**The 77 articles sitting on 89 average 1,766 words.** They are inside their band and below their own stated target. Taking them to just past 2,000 is not writing to the plugin; it is writing to the number the standard already names, and the plugin agrees with the standard by coincidence rather than the other way round.

**The size of the job: 233 words on average, 17,500 across the batch.** The largest single gap is 372 words and the smallest is 19.

**One caution I want on the record.** DSRD 2 section 3.8 sets "Buyer-Intent and Field-Authority Question Articles" at about 750 words, and these carry `article_type: field-authority`. They are not that set: section 3.8 describes 63 articles, nine questions across seven schools, and these are 83 rescued legacy pages whose records were drafted to section 3.2 and gated at 1,600 to 2,400. **The type label and the drafting standard disagree, and the records won because they are what was actually built to.** If that is the wrong reading, say so before Cowork writes a word, because the whole recommendation turns on it.

## 5. The one article that is genuinely faulty

**35184, `the-seven-levels-of-human-awareness`, scored 73.** It is not a length case. It carries no internal link, no external link, and fails short paragraphs, which is 14 points in one page. That is a record fault and it goes back to source rather than into the length job.

## 6. What I am asking for

**The 77 drafts at 89 want roughly 233 words each of real material, drafted to their own target.** That is Cowork's, at source in the record, never on the install, and it re-enters at stage 3. The table below names every one with its exact gap so nobody writes to an average.

I have not touched a single body. Everything above is a reading.

## 7. Found on the way, and already fixed

**`search_gate.py` was enforcing a bar of 81 against DSRD 6's 90**, and had been since S315. DSRD 6 Version 12 moved it at S333 and the gate never followed. It is the row `publish_gate.py` refuses a FIRST publish on, so every one of these drafts at 84 and 89 would have been cleared as ready to go public. Corrected this session, with the two page types that hold measured exceptions keyed on post type rather than flattened (help answers 81 at S337, book notes 88 at S344), and proved both directions on the real path: an article at 82 that passed now fails, and a book note names its own bar of 88.

**It also means the whole score table needs re-reading against 90.** Of the 609 rows in the canonical table, only 7 are at 90 or better and 236 sit between 81 and 89. Those 236 were all reading as passes. That is a much wider piece of news than this batch and it is not mine to plan.

## 8. Still owed by me on this stage

The DSRD 6 record line per page, which stage 6 says carries the score and the keyword. 85 of them, not yet written. Say if you want them before the session or after the length work, since the numbers will move.

---

OWED BACK: your word on the section 3.8 versus section 3.2 reading in part 4, before Cowork writes anything. Then a commission to Cowork for the 233 words a page. And a view on the 236 rows in part 7.

## The table

Ordered by score, then by length. "To 2,000" is how many words short of the step.

| Post | Slug | Score | Words | To 2,000 | Focus keyword |
|---|---|---|---|---|---|
| 35184 | `the-seven-levels-of-human-awareness` | **73** | 1898 | 102 | levels of human awareness |
| 35436 | `the-importance-of-self-awareness` | **84** | 1836 | 164 | self-awareness |
| 35276 | `stereotyping-the-unseen-threat-to-diversity-and-inclusion` | **86** | 1758 | 242 | diversity and inclusion |
| 35161 | `psychological-blind-spots` | **88** | 1253 | 747 | psychological blind spots |
| 35163 | `busy-but-not-fulfilled` | **88** | 1303 | 697 | busy but not fulfilled |
| 35290 | `the-impact-of-transference-and-counter-transference` | **89** | 1628 | 372 | transference and counter-transference |
| 35186 | `aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology` | **89** | 1631 | 369 | revolutionized cognitive psychology |
| 35228 | `finding-purpose-how-human-values-shape-your-lifes-direction` | **89** | 1633 | 367 | human values shape your life's direction |
| 35304 | `triggers-that-lead-to-relationship-breakdowns` | **89** | 1639 | 361 | triggers that lead to relationship breakdowns |
| 35198 | `books-about-person-centred-psychology` | **89** | 1646 | 354 | books about person-centred psychology |
| 35254 | `misattribution-of-arousal-study-insights-into-emotional-perception` | **89** | 1648 | 352 | misattribution of arousal |
| 35282 | `the-dynamics-of-cognitive-dissonance` | **89** | 1650 | 350 | the dynamics of cognitive dissonance |
| 35238 | `insights-from-mary-ainsworths-the-strange-situation-study` | **89** | 1652 | 348 | the strange situation study |
| 35220 | `exploration-of-the-false-memory-experiment-by-elizabeth-loftus` | **89** | 1653 | 347 | false memory experiment |
| 35250 | `mastering-the-art-of-persuasion` | **89** | 1654 | 346 | the art of persuasion |
| 35200 | `carl-rogers-person-centered-counseling` | **89** | 1654 | 346 | person-centered counseling |
| 35312 | `unraveling-behaviorism-psychology-a-historical-perspective` | **89** | 1657 | 343 | behaviorism |
| 35178 | `12-psychological-principles` | **89** | 1658 | 342 | psychological principles |
| 35272 | `skills-for-highly-effective-counseling` | **89** | 1661 | 339 | highly effective counseling |
| 35306 | `twenty-pivotal-moments-in-psychologys-history` | **89** | 1671 | 329 | psychology's history |
| 35216 | `exploration-of-dr-howard-gardners-nine-types-of-intelligence` | **89** | 1673 | 327 | howard gardner's nine types of intelligence |
| 35248 | `maslows-hierarchy-of-needs` | **89** | 1673 | 327 | Maslow's hierarchy of needs |
| 35300 | `the-smart-goal-setting-framework` | **89** | 1675 | 325 | the SMART goal-setting framework |
| 35244 | `learned-helplessness-experiment-the-psychology-of-helplessness` | **89** | 1681 | 319 | learned helplessness experiment |
| 35208 | `dynamics-of-leading-effective-diplomatic-discussions` | **89** | 1685 | 315 | effective diplomatic discussions |
| 35256 | `navigating-life-with-a-sound-mind` | **89** | 1688 | 312 | sound mind |
| 35318 | `what-habits-are-and-why-people-get-stuck` | **89** | 1694 | 306 | what habits are and why people get stuck |
| 35252 | `mimicking-aggression-insights-from-the-bobo-doll-experiment` | **89** | 1703 | 297 | bobo doll experiment |
| 35204 | `decide-with-confidence-10-timeless-principles-for-wise-decision-making` | **89** | 1707 | 293 | wise decision making |
| 35270 | `sigmund-freuds-defence-mechanisms` | **89** | 1712 | 288 | sigmund freud's defence mechanisms |
| 35242 | `learn-about-the-psychologist-dr-albert-ellis` | **89** | 1715 | 285 | albert ellis |
| 35438 | `the-origins-of-humanistic-psychology` | **89** | 1715 | 285 | origins of humanistic psychology |
| 35258 | `obedience-to-authority-stanley-milgram` | **89** | 1718 | 282 | obedience to authority |
| 35234 | `how-irresponsibility-leads-to-personal-disempowerment` | **89** | 1721 | 279 | personal disempowerment |
| 35308 | `understanding-the-layers-of-identity` | **89** | 1721 | 279 | layers of identity |
| 35230 | `gerard-egans-skilled-helper-model-using-the-3-stage-framework` | **89** | 1725 | 275 | skilled helper model |
| 35302 | `the-worlds-most-influential-psychologists` | **89** | 1725 | 275 | world's most influential psychologists |
| 35194 | `balanced-lifestyle-seven-practical-steps-to-achieve-life-balance` | **89** | 1731 | 269 | life balance |
| 35206 | `depth-perception-insights-from-the-visual-cliff-experiment` | **89** | 1731 | 269 | visual cliff experiment |
| 35246 | `lessons-from-how-to-win-friends-influence-people` | **89** | 1738 | 262 | how to win friends influence people |
| 35310 | `unraveling-apathy-insights-from-the-bystander-effect-study` | **89** | 1740 | 260 | the bystander effect |
| 35268 | `qualities-of-a-true-leader` | **89** | 1744 | 256 | qualities of a true leader |
| 35296 | `the-road-to-character-10-lessons-from-david-brooks-classic` | **89** | 1748 | 252 | the road to character |
| 35294 | `the-origins-of-positive-psychology` | **89** | 1750 | 250 | origins of positive psychology |
| 35320 | `what-is-counselling` | **89** | 1752 | 248 | what is counselling |
| 35196 | `benefits-of-practical-learning-why-experience-outweighs-academic-knowledge` | **89** | 1753 | 247 | benefits of practical learning |
| 35232 | `history-and-timeline-of-counselling-psychology` | **89** | 1771 | 229 | history and timeline of counselling psychology |
| 35286 | `the-impact-of-the-hawthorne-studies-on-workplace-dynamics` | **89** | 1771 | 229 | hawthorne studies |
| 35262 | `psychology-history-timeline` | **89** | 1771 | 229 | psychology history timeline |
| 35226 | `finding-lifes-purpose-with-viktor-frankls-mans-search-for-meaning` | **89** | 1775 | 225 | man's search for meaning |
| 35278 | `the-complete-history-of-life-coaching-and-its-predecessors` | **89** | 1782 | 218 | history of life coaching |
| 35426 | `compassions-test-insights-from-the-good-samaritan-experiment` | **89** | 1786 | 214 | good samaritan experiment |
| 35280 | `the-dark-side-of-human-behavior-the-impact-of-the-zimbardo-deindividuation-study` | **89** | 1787 | 213 | zimbardo deindividuation study |
| 35264 | `psychology-theories-for-motivation` | **89** | 1787 | 213 | psychology theories for motivation |
| 35202 | `conditioning-fear-insights-from-the-little-albert-experiment` | **89** | 1791 | 209 | little albert experiment |
| 35180 | `13-morally-dubious-psychology-experiments` | **89** | 1799 | 201 | morally dubious psychology experiments |
| 35192 | `an-exploration-of-the-pygmalion-effect-experiment-on-expectations` | **89** | 1808 | 192 | pygmalion effect experiment |
| 35260 | `perceptions-illusion-insights-from-the-halo-effect-experiment` | **89** | 1808 | 192 | halo effect experiment |
| 35214 | `examining-the-doll-test` | **89** | 1819 | 181 | the doll test |
| 35188 | `albert-banduras-social-learning-theory` | **89** | 1845 | 155 | bandura's social learning theory |
| 35314 | `unveiling-attachment-insights-from-harlows-monkey-experiments` | **89** | 1848 | 152 | harlow's monkey experiments |
| 35298 | `the-role-of-freedom-in-personal-autonomy-and-decision-making` | **89** | 1851 | 149 | personal autonomy and decision making |
| 35322 | `what-is-the-meaning-of-life-a-comprehensive-exploration` | **89** | 1855 | 145 | meaning of life |
| 35224 | `exploring-self-determination-theory-key-principles-applications` | **89** | 1859 | 141 | self-determination theory |
| 35284 | `the-foundational-principles-of-person-centred-counselling` | **89** | 1865 | 135 | principles of person-centred counselling |
| 35218 | `exploration-of-the-cognitive-maps-experiment-by-edward-tolman` | **89** | 1869 | 131 | cognitive maps experiment |
| 35274 | `social-conformity-insights-from-the-asch-conformity-experiment` | **89** | 1869 | 131 | asch conformity experiment |
| 35210 | `essential-character-traits-for-personal-growth-and-development` | **89** | 1870 | 130 | character traits for personal growth |
| 35432 | `how-immediacy-shapes-engaging-and-impactful-conversations` | **89** | 1886 | 114 | engaging and impactful conversations |
| 35176 | `10-ethically-dubious-experiments` | **89** | 1891 | 109 | ethically dubious experiments |
| 35430 | `from-roots-to-revolution` | **89** | 1894 | 106 | from roots to revolution |
| 35266 | `psychology-understanding-the-blue-eyes-brown-eyes-experiment` | **89** | 1902 | 98 | blue eyes brown eyes experiment |
| 35190 | `an-exploration-of-freuds-psychoanalytic-theory` | **89** | 1911 | 89 | freud's psychoanalytic theory |
| 35288 | `the-impact-of-the-invisible-gorilla-experiment-explained` | **89** | 1911 | 89 | invisible gorilla experiment |
| 35212 | `ethically-questionable-insights-from-the-robbers-cave-experiment` | **89** | 1924 | 76 | robbers cave experiment |
| 35428 | `delayed-gratification-insights-from-the-marshmallow-test-study` | **89** | 1932 | 68 | marshmallow test |
| 35240 | `jean-piagets-contributions-to-developmental-psychology` | **89** | 1937 | 63 | piaget's contributions to developmental psychology |
| 35236 | `how-philosophy-illuminates-our-understanding-of-psychology` | **89** | 1947 | 53 | understanding of psychology |
| 35292 | `the-lucifer-effect-10-lessons-from-philip-zimbardos-classic` | **89** | 1947 | 53 | the lucifer effect |
| 35316 | `voices-of-vulnerability-insights-from-the-monster-study-experiment` | **89** | 1977 | 23 | monster study |
| 35222 | `exploration-of-the-split-brain-experiment-by-roger-sperry` | **89** | 1978 | 22 | split brain experiment |
| 35440 | `understanding-your-core-values` | **89** | 1981 | 19 | understanding your core values |
| 35424 | `a-guide-to-breaking-bad-habits` | **91** | 2043 | over | breaking bad habits |
| 35182 | `20-common-cognitive-biases-that-influence-your-decisions` | **91** | 2061 | over | cognitive biases that influence your decisions |
| 35434 | `karpman-drama-triangle` | **91** | 2394 | over | karpman drama triangle |

*No em or en dashes in this file; checked before writing.*
