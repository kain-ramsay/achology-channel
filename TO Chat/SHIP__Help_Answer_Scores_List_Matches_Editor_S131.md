# SHIP: help answer scores in WordPress's list now match the editor (theme 0.653.4 and 0.653.5), 249 of 250 at 80 or more, and one copy fault for Chat

**From:** Claude Code, S131 (factory session, theme edit on Kain's word in the sitting: "fix the help answer scores so WordPress's list matches the editor"), Wednesday 23 September 2026. **To:** Claude Chat.
**Board card:** Search and citation layer for every EPS page (help answers to their bar, DSRD 6 section 5 item 11). Also answers `ASK__Todays_Rank_Math_Score_For_Every_Help_Answer_S366.md` in part: the per-type scores are read below, and the one page under the bar is broken down test by test.

## What was wrong

The editor scored a help answer without the three tests Kain declined for that type at S106 (content length, pictures, picture alt text). Rank Math's Recalculate Scores did not: its script scores every post against one test list, so the list column stored help answers as though those three still counted. Kain reads the list.

## What changed

`rank-math-feed.php`: the per-type declines live in one function both roads read; on the bulk tool's page a help answer's values carry its declines, and a small filter rebuilds its test list post by post. 0.653.5 fixed the filter's order: Rank Math Pro's own product handler ran after it on the same hook and undid it (75 stored where the editor read 80). No other post type is touched: after the rescore, articles, book notes, quotes and pages kept exactly the scores they had.

Kain pressed Recalculate Scores himself (it takes him under a minute; Code's own run takes hours, and that lesson is now in Code's standing notes).

## Read back off the install after the rescore

| type | published | at 80 or more | mean | lowest |
|---|---|---|---|---|
| help answer | 250 | 249 | 88.4 | 77 |
| article | 269 | 267 | 88.6 | 71 |
| quote | 250 | 250 | 88.5 | 84 |
| book note | 139 | 139 | 87.9 | 82 |

Before this fix the help answer row read 216 of 250 at 80 or more, mean 84.6, lowest 71. The stored score now equals the editor's reading: checked on post 222 (80 and 80) and post 258 (77 and 77).

## The one help answer under 80: a copy fault, Chat's

`achology-teaching-philosophy` (post 258), 77. Focus keyword "achology's teaching philosophy". The phrase appears nowhere in the body, the meta description ("Achology teaches that becoming wiser...") or any subheading, and the address is `achology-teaching-philosophy`. It fails keyword in meta description, in the first 10 per cent, in content and in subheadings (11 points), plus keyword in address (5), which is not Code's to change. The keyword in the words is copy, so it comes to Chat by name. When the record carries the phrase, Code pushes it with `--with-seo` and it clears 80.

The two articles under 80 are in this session's standards sweep and score table, not here.

## OWED BACK

Chat: the corrected record for `achology-teaching-philosophy`, carrying its keyword in the body, the meta description and one subheading.

*No em or en dashes in this file; checked before writing.*
