**For Chat. What this needs from you:** new alt text in three records, and one ruling on the bar these five are published against. Answers NOTE__Four_Anxiety_Headings_Carry_Their_Phrase_Update_The_Drafts_S449.

# ASK: three anxiety banners need new alt text, and the 90 bar (Code, factory session S192, 27 October 2026)

**Done.** The four new headings are on the drafts. Kain's five banners arrived as a zip in Article Page Assets. All five are the right shape (2722 by 1299). I converted them to WebP at 1980 by 945, each under 60KB. The importer updated all five drafts from their records and verified 5 of 5 clean. All five are still drafts.

## 1. Two banners attached, three held on their alt text
I looked at each picture beside its record's `featured_image_alt`.
- **Attached:** 40858 anxiety-is-ruining-my-life (a man by a window at dusk, phone in hand, city below) and 40861 is-it-better-to-fight-anxiety-or-give-in-to-it (a woman at a glass door, hand on the handle). Both match their alt text.
- **Held, because the alt text describes a different picture.** The image map says the alt text is changed to match before import:

| Post | Record's alt text says | The banner shows |
|---|---|---|
| 40862 why-do-i-get-anxiety-for-no-reason | a kettle on a quiet kitchen worktop in soft morning light, a mug beside it | an orange kettle steaming against streaks of orange light; no mug, no kitchen |
| 40860 how-do-you-deal-with-anxiety-day-to-day | an open notebook with a handwritten list beside a cup of tea | a worried man, hand at his mouth, city lights streaking behind him at night |
| 40859 can-you-use-anxiety-to-your-advantage | a person in a parked car smiling after a difficult call | a worried man crouched with a tablet, streaks of light behind him at night |

When the three records carry alt text that matches, one importer rerun attaches them. The WebP files are made and waiting.

## 2. The scores, and why 90 is out of reach on this page shape

| Post | Score | Tests earning less than their maximum |
|---|---|---|
| 40858 (banner) | 86 | contentHasAssets 1 of 6, lengthContent 3 of 8, keywordInImageAlt 0 of 2 |
| 40861 (banner) | 86 | the same three |
| 40862 | 85 | contentHasAssets 0 of 6, lengthContent, keywordInImageAlt |
| 40860 | 85 | the same three |
| 40859 | 85 | the same three |

keywordInSubheadings now passes on all five.

My S192 DONE projected 90 or more with the banners. That was wrong, and I correct it here. I had added the points the failing tests showed. But Rank Math gives a single featured picture only 1 of the test's 6 points: the rest comes from more pictures or video in the body. It also scores a page of about 1,100 words at 3 of 8 for length, where 2,500 words earns full marks. With all three banners in, the five will read 86.

**The comparison.** I sampled 60 published articles on the build site: the lowest reads 86, the middle 86 and the highest 89. None reaches 90. So 86 is where a one-picture article of this length sits on this site, and these five are level with their peers.

**The question.** The S449 note says the pages stay drafts until each reads 90. Neither of the two levers is mine to pull: a second picture in each body, or roughly 1,400 more words. My recommendation: Chat rules contentHasAssets and lengthContent as a named page-type shortfall for the article family, which the rank-math-90 skill's own success test allows. Then the five publish at 86 once the three banners are attached.

## 3. Later the same sitting: Kain closes section 1
Kain, in Code, word for word: "the images I've given you are just the images that we're going to need you to use." So the alt text follows the pictures. Code wrote the three `featured_image_alt` lines to describe each banner as made, and changed nothing else (project commit b6520aab):
- why-do-i-get-anxiety-for-no-reason: "An orange kettle letting off steam on a counter, with streaks of warm light sweeping around it"
- how-do-you-deal-with-anxiety-day-to-day: "A worried man with his hand at his mouth, city lights streaking past behind him at night"
- can-you-use-anxiety-to-your-advantage: "A worried man crouching with a tablet in his hands, streaks of city light behind him at night"

`body_guard.py --signed` exits 0. All five banners are attached, verified 5 of 5 clean. **Final scores, all banners in: 86 on all five** (40858 to 40862). All five are still drafts. Section 2, the bar, is put to Kain in Code in the same turn.

## 4. Kain rules the bar, and the five are published
Kain, in Code, word for word: "Yes, publish the five at 86. Articles like these are accepted at 86." Chat, please write this home where the bar lives (DSRD 6 section 5 item 11), as the rule for this article family.

- **Clearance.** `publish_gate.py --clear` with `--override` quoting Kain's words, clearance fb9e44ec6e70fabd. As every first publish does, it refused the five on the draft 404 (assets-load, block-heading, breadcrumb-hierarchy, dsrd6-record and the rest of the nine), and each refusal is written on the clearance by name.
- **Published.** Posts 40858 to 40862, status publish, 27 October 2026 at 19:10.
- **Re-gated at the live addresses** with `--update`, after a cache purge: every check that blocks a live page passes, clearance 4a5bdda46a40a575 (minted by the re-gate and not spent).
- **Carried on the pages, not blocking:** dsrd6-record, because no DSRD 6 record exists for these five, as for the other articles; image-budget; image-responsive; keyword-density, which reads the keyword as thin, the move 7 band the Standard retired as a fail; orphan; rank-math, because the gate's own score table does not hold these five yet: the scores live in this file; spacing-scale.
- **Final scores:** 86 on all five.

**One fault for a theme session, found here.** `publish_gate.py` still imports the content gate from the old factory folder name, `04. Content Production Factory + COWORK`, renamed at S434. So a `--clear` on any Knowledge Hub page stops with `No module named 'content_gate'`. This session ran it with the Machine folder put on Python's path for the run, and changed no theme file. The fix is that folder name, in the FACTORY line near line 378. Its `record_for` reads the same stale root, which is why it finds no content record.

OWED BACK: nothing more on the five. The content gate signature fix with its test is still owed from the S449 ruling.

*No em or en dashes in this file; checked before writing.*
