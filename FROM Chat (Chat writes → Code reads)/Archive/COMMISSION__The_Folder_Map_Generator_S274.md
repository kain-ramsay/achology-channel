# COMMISSION: build the folder map generator

**DOCUMENT TYPE:** approved brief, not a page spec. No PAGE GATE line applies.
**From:** Claude Chat, Session 274, 15 August 2026.
**Approved by:** Kain, in session, S274.
**Governing specification:** `SPEC__Folder_Navigation_And_Map_Currency_S274.md`, in the Project Delivery System folder. Read it whole before writing any code. This brief does not restate it.
**Why now:** the S274 filesystem walk found standing rule 24 resting on maps that were never built, and the one map at the top of the estate stale and contradicting the live project map.

---

## What you are being asked to build

One script, living in the theme's tools folder beside `page_readiness_board.py` and `component_census.py`.

Its behaviour is specified in section 4 of the specification. In summary, so this brief stands alone if you read it first:

1. It walks the project folder from its root.
2. At folder levels one and two only, as the specification defines them, it finds each folder's map file by a marker line rather than by filename.
3. It regenerates everything below that marker: subfolders one line each with their loose file counts, the loose files at that level, and any file breaking the folder's stated rule.
4. It never writes above a marker. The hand-written purpose is not yours or the script's to touch.
5. Where a folder at those levels has no map, it reports `MAP MISSING` and creates nothing.
6. It prints a summary line: maps updated, maps missing, and every folder whose contents changed since the previous run.

The marker line is:

```
<!-- FOLDER MAP: EVERYTHING BELOW THIS LINE IS GENERATED. DO NOT EDIT BY HAND. -->
```

**The changed-folder line is the load-bearing output.** Without it the script is a tidying tool. With it, it is the check that catches the tree moving while the maps stand still, which is the exact failure that produced the stale root map.

---

## Three things Chat decided, named so Kain or you can overturn them

1. **Find the map by marker, not by filename.** Three naming conventions are already live across the estate and renaming them would break references in the Project Instructions and the DSRDs. This is the same lesson as the harness finding its own anchors.
2. **The generator reports the tree rather than Code reporting his touched files.** Kain's first instinct was that you would tell Chat each session which files you had touched. A walk cannot forget and a person can, so the walk is the stronger mechanism and it removes a manual relay.
3. **It runs as a hook at the end of every Code session**, with its summary going into your session report. If a hook is the wrong instrument here, say so in your reply rather than working around it.

---

## Three questions only you can answer

1. **Can the run be a genuine hook**, one that refuses a session ending without it having run, in the way the existing enforcement hooks do? Or is an end-of-session step in your harness the honest limit?
2. **Where should the previous-run state live** so the changed-folder comparison has something to compare against, given the folder is iCloud-synced and files can be evicted to stubs?
3. **Does anything in the theme, the hooks or `CLAUDE.md` already read a folder's contents in a way this script would duplicate or break?** Chat cannot search file contents on your machine and cannot see the hooks.

---

## What is not being asked for

- Do not create any map file. A map's hand-written half states a purpose, and a purpose is Kain's to decide, never a script's to invent.
- Do not move or refile anything. The S274 walk found misfiled and duplicated documents and they are a separate pass.
- Do not touch the stale root folder map. Its retirement wording is going to Kain for approval and will travel separately.

## What comes back

Your reply through TO Chat, carrying the three answers above and the script's first run output against the real tree, including its `MAP MISSING` list. That list is what tells Chat and Kain how many maps have to be written and where.

*No em or en dashes in this file; checked before writing.*
