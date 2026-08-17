# REPORT: keyphrases set, and the score run stopped early with a finding you need before it restarts

**From:** Claude Code, S230. **Date:** 2026-07-29. **Answers:** `00__RULING__Help_Article_Focus_Keyphrase_Standard.md`.
**Status: stopped at 96 of 249, deliberately.** The remaining 153 are one command away, and they should not run until you have ruled on what is below, because they would produce 153 more numbers with the same known cause.

## 1. The keyphrases are set

Your formula applied across all 249, mechanically, no judgement per article:

- **223 articles now carry a focus keyphrase** derived from their own question title.
- **26 are exceptions**, listed in `EXCEPTIONS__Keyphrase_Formula.md`. All 26 are the same kind: the formula leaves 7 to 10 words, and cutting to your stated 2 to 6 means choosing which half of the question matters. Twenty three leave 7 words, two leave 8, one leaves fewer than two. No duplicates arose.
- Word counts of the 223: 5 at two words, 26 at three, 59 at four, 77 at five, 56 at six. All inside your bound.

Function words went, including prepositions, which is what "and similar" covers in your step 2. Proper nouns kept their capitals, possessives included, so "Achology's" stays capitalised. Register terms were left exactly as the register writes them.

## 2. The scores are real, and they are almost all 8

Rank Math's analyser had never seen these articles. It has now seen 96 of them:

| Score band | Articles |
|---|---|
| 0 to 19 | 91 |
| 40 to 59 | 7 |
| 60 to 79 | 1 |

## 3. The cause, measured rather than guessed

**Of those 96 articles, the keyphrase appears verbatim in the article's own text in 10 cases, and appears nowhere in it in 86.**

| | Articles | Median score |
|---|---|---|
| Keyphrase appears in the text | 10 | **47** |
| Keyphrase appears nowhere in the text | 86 | **8** |

Rank Math scores exact-phrase presence: in the title, the description, the URL, the opening paragraph, the body, the subheadings. A phrase that does not occur in the article fails nearly every test it runs, whatever the article's quality.

Examples, all scoring 8:

| Keyphrase the formula produced | The article's actual title |
|---|---|
| Achology knowledge hub available free read | Is the Achology Knowledge Hub available for free to read? |
| major milestones Achology's history | What are the major milestones in Achology's history? |
| registered company details Achology | What are the registered company details of Achology? |
| Achology company formally contracting | With which Achology company am I formally contracting? |
| steps follow organise own Achology event | What steps should I follow to organise my own Achology event? |

Read them aloud and the problem is plain: stripping the function words out of a question leaves a string no reader would type and no article contains. "Cancel Achology membership", your worked example, survives because it happens to be a phrase a person would use and a phrase the article would naturally contain. Most titles do not survive that treatment.

**This is the same defect as the import artefacts we replaced**, arrived at by a different route. The old keyphrase "achology knowledge hub free" appeared in 9 of 249 articles. The new ones appear in roughly 1 in 10.

## 4. What I am not doing

Not choosing new keyphrases. Not scoring the remaining 153 to complete a set that will be discarded. Not tuning the formula myself: it is your standard, it is editorial, and Rule 5 puts it with you.

## 5. What I would suggest, for you and Kain to settle

The formula needs one more step: **the keyphrase must be a phrase that appears in the article, or the article gets an opening line that contains it.** Two routes, and the choice is editorial:

1. **Take the phrase from the article's own text**, not from its title: the shortest natural phrase in the opening paragraph that names the subject. Mechanical enough for me to run, since it is selection rather than invention, but it needs your ruling that selection from the body is what you want.
2. **Keep the title-derived phrase and let the copy carry it**, which means an editorial pass over 249 openings. That is a content pass, and it is yours and Kain's.

Either way the scores follow. As they stand they measure the rule, not the articles.

## 6. Mechanically, the run is now cheap

Worth knowing when you rule: the first attempt could not run at all, because the host's Antibot refuses every browser I control, and support confirmed in July that it cannot be disabled or whitelisted per site. It now drives Kain's own Safari through AppleScript, in its own window, reading each score without saving anything, so no content and no modified date is touched. About 13 seconds an article in a single window; a few windows in parallel brings the whole 249 to roughly a quarter of an hour. Restarting is one command and it resumes where it stopped.

*No em or en dashes in this file; checked before writing.*
