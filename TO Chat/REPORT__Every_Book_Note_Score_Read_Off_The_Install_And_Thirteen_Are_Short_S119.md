# REPORT: every book note on the install read one at a time. 112 at 88, thirteen short, and the reason the thirteen are short

**Filed by Claude Code, Session 119. Date:** 15 September 2026.
**Answers:** Kain's instruction at this session's open, after he caught a false claim live at S118 that all 42 book notes were at 88.

---

## What was actually read, and why it was 125 and not 42

S118 claimed all 42 book notes it touched were at 88. That was false: only the 17 drafts had been re-scored, the 25 already-published ones had never been checked, and Kain was looking at several of them sitting at 21 in the WordPress admin while the claim was being made.

So this session did not re-check a list of 42. **It read the live Rank Math score of every book note on the install, all 125, drafts and published together, one page at a time**, with `score_run.py --ids`, plain, no `--refresh`. A superset cannot hide a page a wrong list would have missed. Nothing below is taken from a file, a memory or an earlier report.

## The table

| Score | How many |
| --- | --- |
| 88 | 112 |
| 86 | 5 |
| 82 | 1 |
| 24 | 1 |
| 21 | 6 |

**112 of 125 are at 88, which is the ceiling a book note can reach** (the cover is one image, and Rank Math scores images at 1 of 6; measured and filed at S103). **Thirteen are short**, and every one of the thirteen is a published page, not a draft.

- **21:** resilient, shyness-what-it-is-what-to-do-about-it, the-beck-diet-solution, identity-youth-and-crisis, multiple-intelligences-new-horizons, the-origins-of-intelligence-in-children
- **24:** yes-50-scientifically-proven-ways-to-be-persuasive
- **82:** boundaries-cloud
- **86:** emotional-leonard-mlodinow, free-will-sam-harris, nature-emerson, the-brains-way-of-healing, why-zebras-dont-get-ulcers

## Why they are short, read off the install and off the records

The S118 fix (re-writing the three Rank Math columns from the record with `--overwrite-columns`) **did not reach any of these thirteen**, and the reason is not the column safety rule it was blamed on.

Read off the install this session, post 36206, resilient:

- focus keyword: `resilient rick hanson book summary`
- SEO title: `Resilient by Rick Hanson: Book Notes`

Its record says the focus keyword is `Resilient`, which is what Kain's S349 ruling requires (the book's title). So the install carries boilerplate the record does not.

**But the importer cannot push the record's value, because it cannot read the record at all.** A plan run over all thirteen returns: records read cleanly, 1; records that could not be read, 12. Every one of the twelve fails for the same reason: it is missing all five of the current body sections. Those twelve records are an older generation. `resilient.md` carries `The Argument at the Heart of the Book`, `The Background the Author Comes From`, `Practical Applications Beyond the Book`, `What this Might Possibly Mean for You`, `What Your Next Learning Step Could Be`, and no Search and Citation Brief at all. A current record, such as `boundaries-cloud.md`, carries the eight-part Search and Citation Brief and the five current sections: `What this Book is Actually Saying`, `Where the Author is Coming From`, `What Could this Mean for Society?`, `What You Can Take From the Book`, `What are Your Next Learning Steps?`.

**So this is a content gap, not a tooling one.** Twelve book note records were never brought up to the current record shape, the importer has therefore never been able to touch their pages, and those pages have been sitting live carrying their original metadata ever since. The thirteenth, boundaries-cloud, reads cleanly and is at 82, so it is a different and smaller problem.

This is not mine to fix. Rewriting a record's body into the current sections is drafting, and the harness puts drafting with Cowork and Chat. What I can do the moment the twelve records are rebuilt is one run, and the pages will take their correct values.

## The honest status line

Read this turn, off the install, 125 of 125: **112 at 88, thirteen short, none of the thirteen fixable by Code today.** No count in this file is repeated from anywhere else.

OWED BACK: a ruling on who rebuilds the twelve old-generation book note records, and whether boundaries-cloud at 82 is looked at with them or separately.

No em or en dashes in this file; checked before writing.
