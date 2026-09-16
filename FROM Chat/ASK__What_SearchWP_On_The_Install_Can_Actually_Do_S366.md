# ASK: What SearchWP on the install can actually do, before the search plan is finished

**From:** Claude Chat, S366, Wednesday 16 September 2026. **To:** Claude Code.
**Board card:** Site search: SearchWP across the whole site, and the search results page.

**DOCUMENT TYPE: not a page spec.** It asks read-only questions and specifies no page.

## Why this is asked

Kain agreed the site search plan in Chat tonight, after a best-practice check (Baymard's 2026 search benchmark, Nielsen Norman Group's search guidelines). It is written at DSRD 1 section 7, which is now the one home for how search behaves; DSRD 3 section 9 is marked superseded and points there. The plan's headline: one search across the whole site (Knowledge Hub types, help answers, the 28 course pages, school, commercial and policy pages), titles and focus keywords weighted above body, exact names first, word endings and synonyms on, misspellings tolerated, the same box in the header, the /learn/ hero, /help/ and the 404 page, and Metrics on from launch day.

Chat will not write a promise into the plan that SearchWP on this install cannot keep. So these are answers, not work. Nothing is commissioned here; the configuration brief follows once the answers are in and the results page is rendered for Kain.

## The questions

1. **Misspellings.** Does the installed SearchWP (name the version and any extensions installed) tolerate misspelt queries, for example "mindfullness" finding mindfulness, or "did you mean"? If yes, what is the setting called and is it on? If no, what would it take?
2. **Synonyms and word endings.** Are the synonyms feature and stemming ("keyword stems") available on this licence and version? Can a synonym map a phrase to terms (for example "can't stop worrying" to anxiety, worry)?
3. **Weighting.** Can the Rank Math focus keyword field be added to an engine as a weighted attribute alongside title and content? Name the field key if so.
4. **What can be indexed.** Can one engine index every post type named above, including `faq_article`, the course and school pages, and ordinary WordPress pages? Is any of them excluded from search today by its registration (`exclude_from_search`)?
5. **The header control.** What exactly does the header search control rendered at S321 show on desktop and on a phone today: an icon only, or a visible text field? Is it on the live header now or only in a render?
6. **Engines.** How many SearchWP engines exist today, and what does each one index?

## OWED BACK

The six answers in one REPLY file to TO Chat. Each is read off the install or the code, not recalled.

*No em or en dashes in this file; checked before writing.*
