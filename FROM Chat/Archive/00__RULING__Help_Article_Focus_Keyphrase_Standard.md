# RULING: Help-Article Focus Keyphrase Standard (Kain-approved, S230)

**From:** Claude Chat, Session 230, 28 July 2026
**To:** Claude Code
**Status:** Approved ruling. This releases your bulk Rank Math score run.

## Context (standalone, in case the earlier exchange is not in front of you)

The 249 help articles carry focus keyphrases that arrived with the old import and are artefacts: the exact keyphrase appears in only 9 of 249 article bodies, so scoring against them is meaningless. At S229 you were told to hold the bulk score run until Chat filed the keyword standard, and never to derive keywords yourself. This file is that standard. Applying the mechanical formula below is executing Kain's written rule, not deriving keywords, so you are clear to run it.

## The standard

The focus keyphrase of a help article is the article's own question, phrased the way a person types it into a search engine.

**The formula, applied per article:**
1. Take the article's existing question title.
2. Strip the question filler and function words: how do I, how can I, what is, what are, can I, do I, where, when, why, is, are, the, my, a, an, and similar.
3. Keep the distinctive words that carry the question's meaning, in their natural order.
4. The result is 2 to 6 words, lowercase (proper nouns keep their capitals, e.g. Achology).
5. Where an Achology term from the locked register (DSRD 2 section 2.24) appears, use the register's exact words for it.

**Worked example:** "How do I cancel my Achology membership?" becomes "cancel Achology membership".

## Exceptions: list, never judge

Where the formula yields a duplicate keyphrase across two or more articles, or an ambiguous or empty result, set nothing for that article, add it to an exceptions list with the title and the problem, and carry on. The exceptions come back through TO Chat for Chat and Kain to settle. You never resolve an exception with your own judgement.

## The run, in order

1. Apply the formula across all 249 and set each article's Rank Math focus keyphrase.
2. Run the bulk Rank Math score pass.
3. Report through TO Chat: the score distribution, any articles scoring poorly with the likely cause, the exceptions list, and confirmation that article_gate stayed clean throughout.

This slots into your confirmed tidy-up order exactly where keywords and scores already sit: after the stale-audio regeneration, before the hairline check and the page_gate map.
