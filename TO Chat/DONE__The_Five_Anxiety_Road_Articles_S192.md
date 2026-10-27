**For Chat. What this needs from you:** four records mended at source (the focus phrase in one subheading); then the banners. The five are drafts on the build site and none reads 90 yet.

# DONE: the five anxiety road articles are drafts on the build site, links in (Code, factory session S192, 27 October 2026)

Answers BRIEF__Import_The_Five_Signed_Anxiety_Road_Articles_S448 and ANSWER__Sourcing_Records_Added_To_The_Five_Anxiety_Road_Articles_S449. Section 3 of RULING__Gate_Lines_On_Signed_Words_The_73_Help_Answers_The_147_Book_Notes_And_The_Five_Anxiety_Articles_S449 is read and applied below.

## 1. Checks
- `body_guard.py --signed`: exit 0 (1014 records, no working note), run before the import and again after the link edits.
- Stage 5, three checks: 5 of 5 pass, now that each record carries its Search and Citation Brief.

## 2. Imported
Five new posts, created as drafts by the importer, which creates nothing else by design. Read back with `--verify`: 5 of 5 clean.

| Post | post_name | Status |
|---|---|---|
| 40858 | anxiety-is-ruining-my-life | draft |
| 40862 | why-do-i-get-anxiety-for-no-reason | draft |
| 40861 | is-it-better-to-fight-anxiety-or-give-in-to-it | draft |
| 40860 | how-do-you-deal-with-anxiety-day-to-day | draft |
| 40859 | can-you-use-anxiety-to-your-advantage | draft |

**Featured images: left empty.** The importer took all five without a picture (`--allow-missing-pictures`). Each record still names its `.webp`. When Kain's banners land as WebP in the theme's knowledge-hub articles images folder, one rerun of the importer attaches them with their alt text.

## 3. Score table
Each score was read off its editor on the build site by `score_run.py`; the failing tests come from `score_breakdown.py`.

| Post | Focus phrase | Score | Failing tests |
|---|---|---|---|
| 40858 | anxiety is ruining my life | 81 | contentHasAssets (0 of 6), keywordInSubheadings (0 of 3), keywordInImageAlt (0 of 2) |
| 40862 | anxiety for no reason | 81 | contentHasAssets, keywordInSubheadings, keywordInImageAlt |
| 40861 | fight anxiety | 85 | contentHasAssets, keywordInImageAlt |
| 40860 | deal with anxiety | 81 | contentHasAssets, keywordInSubheadings, keywordInImageAlt |
| 40859 | use anxiety to your advantage | 81 | contentHasAssets, keywordInSubheadings, keywordInImageAlt |

What each failing test means:
1. **contentHasAssets** (6 points) is the missing banner. It clears when the picture lands.
2. **keywordInImageAlt** (2 points) will still fail with the banner, because none of the five alt lines carries its focus phrase. The Standard retired keyword-in-alt (Part 10), so I read this as an accepted loss, not a fault.
3. **keywordInSubheadings** (3 points) is a record fault on four of the five. No H2 or H3 carries the focus phrase verbatim; is-it-better-to-fight-anxiety-or-give-in-to-it passes it. Part 5 rule 4 asks for exactly one teaching heading with the phrase.

**With the banners alone:** 87, 87, 91, 87, 87. **With the banners and one subheading each:** 90 on all five. So four records need one heading reworded at source, which is Chat's job, then Kain's yes, since the words are signed. Every page stays a draft until it reads 90 or more, as the brief says.

## 4. Inbound links
Each sentence was written word for word from the brief into the linking page's record first, at the end of its last teaching section, so no later re-import can wipe it. Project commit a5228e02, 13 records. Ten sentences joined that section's last paragraph, which stays at six sentences or fewer. Three became a paragraph of their own, because that paragraph already carried a link and Part 9 allows one link a paragraph: thoughts-and-emotions-connection, does-cbt-work-for-anxiety and what-habits-are-and-why-people-get-stuck. Those three are one-sentence paragraphs; the brief's own fallback, named here so the desk can judge.

**On the build site now: 10 of 13.** Each was read back off its post with the link present and the status still publish:
- 36347, 36319, 36363, 36333 and 36341 (quotes), 39306 (Help answer) and 33844 (book note), by `article_body_update.py`, each verified clean against its record.
- 39277 and 39819 (hub questions) and 36911 (instructor article), by the importer's update path; their bodies matched their records before the edit. The update also wrote each record's `signed` field, which the install did not yet carry.

**In the record, not yet on the build site: 3.** what-habits-are-and-why-people-get-stuck, a-guide-to-building-inner-resilience and resilience-and-mental-toughness each carry newer signed titles and search fields that wait on their own batch import (the S445 field authority and hub guide briefs). Pushing them here would have landed that batch's changes from this brief. Each link lands with its page's own import.

**Skipped, not on the build site: 2.** `why-your-fear-is-always-about-the-future` (quote) and `why-our-emotions-end-up-managing-us-instead` (quote). Neither carries the link in a record yet. Add it when their records are written.

One pre-existing line, not from this change: the importer's verify reads what-is-stress-management at 10 H2 headings against the type's 3 to 8. The record already had 10; the count includes its foot sections.

## 5. The two content gate lines (S449 ruling, section 3)
The seven words shared across the five and the signed line with no Standard version are taken as exceptions for these five, as ruled. The `content_gate.py` fix that lets a vault gate signature pass is not done in this session, and neither is its acceptance test. It is still owed and does not hold these drafts.

OWED BACK: the publish once the five read 90, with a re-score; the content gate signature fix with its test.

*No em or en dashes in this file; checked before writing.*
