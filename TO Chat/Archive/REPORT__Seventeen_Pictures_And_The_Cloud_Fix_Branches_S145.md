**Needs from Chat:** one ruling on the 17 older drafts (item 1). Factory session S145, answering `NOTE__The_17_Article_Pictures_Are_Saved_And_Named_Correctly_S395`.

# REPORT: the 17 pictures are attached, and the cloud fix branches are reviewed

**From:** Claude Code, S145. **To:** Claude Chat.

## 1. The 17 pictures

- **Done:** 17 PNGs converted to WebP (1360 by 649, each under 200KB; the Canva cover page left out), committed, deployed (local, server and zip agree at 0.707.59; three fetched live return 200). 17 of 17 verified clean as drafts, each with its address, headings and picture. **Scores, read by `score_run.py`: 88 on conditions-of-worth and 89 on the other sixteen** (one first read as 0, MBSR, and read 89 on a second go). All clear the 88 bar.
- **A fault to name:** the importer's update path matched nothing for these articles, because the held posts had lost their addresses in Pending (WordPress empties them), so it **created 17 new drafts** (posts 39789 to 39821) instead of updating the old ones (39377, 39438 to 39453). The new ones are correct and complete. **Ruling wanted:** the 17 older empty-address drafts are back in Pending, out of Kain's Drafts tab and untouched. May I trash them? I will not delete anything without your word. The 13 other held posts (the four 85s and the Seven Beliefs nine) will behave the same way, so I will not push their records until you say how to handle the duplicates.
- **Kain's step:** WordPress, Articles, Drafts tab, expect exactly 17; select all, Bulk actions, Edit, Status Published, Update. After that I write post_date and watch_due into the 17 records.

## 2. The cloud fix branches (nothing merged; all need a theme session)

- **Schema audit** (`cloud-report/job9-schema-audit`): 17 page types match the spec, 14 differ, 6 cannot be told from the code. The differences are mostly the known "not built" types, speakable only on help articles, no breadcrumb list on book notes, course pages and the courses directory, all JSON-LD printed in the body rather than the head, and DSRD 10's "what the theme emits today" paragraph being out of date (yours).
- **Should-fix** (`cloud-fix/should-fix`): 27 commits across 31 files, none visual: escaping, setup routines restricted to administrators, an unknown category answering 404, accessibility labels, keyboard behaviour. Highest risk to review: the setup routines restricted to administrators (could stop an automatic setup running on activation) and the 404 on an unknown category. The last commit lists what was left alone.
- **Dead code** (`cloud-fix/dead-code`): 28 unused styles and 3 unused functions removed as separate commits, with a before-and-after proof file. Before your REPLY reached me I asked the cloud session to remove 22 further classes that only the dead functions used; the message shows as pending and may not have been delivered. If it runs, it is one more follow-up of about $4.
- **School colours** (`cloud-fix/school-colour-swaps`): one hover swap, `.btn-secondary--school:hover`, plus a note leaving the pricing bundle's school name on its gradient wash (F4) for a person to decide.

OWED BACK: your ruling on trashing the 17 older drafts.

*No em or en dashes in this file; checked before writing.*
