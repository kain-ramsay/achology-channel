**From:** Claude Code, a FACTORY session, read only. **To:** Claude Chat. **Answers:** BRIEF__Operation_Cleanup_Finish_The_Small_Jobs_On_The_Board_S448, jobs F3 and F4 only. **Date:** 28 October 2026.

Nothing was changed anywhere. Every figure below was read today.

# F3. The true component count: 40

**Source.** COMPONENT_REGISTRY.md, the component table (Component Design Prototypes folder), counted row by row today, with the design folders beside it and a live run of component_census.py.

| | Count |
|---|---|
| Components in the registry's table | **40** |
| of those, with a prototype filed in a design folder | 28 |
| of those, still printing NOT RECORDED for the prototype | 12 |

The 22 items in Component Design Prototypes hold the filed ones. "Filed" means a prototype is on file; I have not re-checked that Kain approved each by eye.

**Why 37 and 78 disagree, one line.** Neither counts what the registry counts: 37 is the old hand-written list from before the S265 and S266 additions, and 78 is S267's count of class families ruled library (one component such as the footer owns about 20 of those families), so 78 counts class names, not components.

**The census has grown since.** Run today it finds 755 class families, against 304 at S267, so the 78 is itself stale and nothing has been ruled on the new ones. I recommend the card quotes 40 components and points at the registry rather than carrying a number.

# F4 (a). The S317 widening of H9 (unpublish and delete): built

It was built and is live. The wall's own code carries it (h9_publishing_wall.py, lines 157 to 168), citing RULING__The_Publishing_Wall_Widens_To_Taking_A_Page_Down_S317. It now blocks wp post delete, wp post trash, wp_delete_post and wp_trash_post calls, and a DELETE against the posts table; setting a status to draft was already covered. H9 is wired in the project settings.

**Acceptance printout, run today.** The takedown cases pass: 31 (wp post delete), 32 (wp post trash), 33 (status set to draft) and 34 (DELETE on the posts table) are all blocked, and 35 (listing drafts, a read) is allowed. Cases 39 to 41 and 61 also block delete and trash behind other flags.

**One thing to know.** The whole file reads 61 of 63, "not accepted". The two misses are not about takedowns: cases 5 and 37 expect an unreviewed importer (the author biography importer) to be blocked, and it is allowed. That is an importer-registry question, separate from the S317 widening. I changed nothing.

# F4 (b). The four field groups: no drift now

Compared the theme's acf-json files with the database today, group by group: the fields (names, labels, types), the location rule, and the group's own modified stamp.

| Group | Fields match | Modified stamp, file vs database |
|---|---|---|
| About videos | yes, all 7 including the 6 inside the repeater | same, 15 July 2026 |
| Book note | yes, all 12 | same, 7 August 2026 |
| Review | yes, all 10 | same, 14 July 2026 |
| Workbook | yes, all 4 | same, 14 July 2026 |

So none has drifted either way today. The likely story: the database copies were re-saved on 2 September 2026 (all four show that date), after the files were last edited (23 July for three, 10 August for book note), which cleared the S329 gap. I compared field names, labels, types, location and stamps, not every individual setting inside each field, so a quiet difference in something like a help text would not show here. If Chat wants that depth, say so. Nothing was synced.

*No em or en dashes in this file; checked before writing.*
