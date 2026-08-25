# SHIP BRIEF: v0.101.0, the enquiries panel repoint, the component gallery, and the help keywords

**From:** Claude Code, Session 84. **Date:** 25 August 2026.
**Deployed and proved:** local, server and zip all read 0.101.0, measured by `deploy.py`'s three proofs.

---

## 1. About and Our People are repointed. The stopgap is deleted.

**Your S308 section 3 ruling is done.** Both templates now call `achology_warm_room()` with every value carried across unchanged. The hand-written enqueue in `functions.php` that was holding those two pages correct is gone, because the renderer enqueues `warm-room.css` itself.

**The panel's markup now exists in exactly one place on this site**, for the first time since it was shared at S045.

**Verified on the rendered live pages, not in the source.** Both `/about/` and `/about/instructors/` render the panel with its frame, its tint, its side-by-side layout and its photograph. The photograph was separately confirmed to have actually loaded, `naturalWidth` 720 on both, because a panel that measures correctly and shows an empty circle is the exact failure this project keeps meeting.

`css_gate.py` passes on all stylesheets. The stale docblock in `shared-parts.php`, which still said page-about.php carried its own copy and must be changed in step with the function, is corrected.

**The `/enquiries/` address is untouched**, per your ruling: the button still points at the page that will exist.

## 2. The component gallery is built, and so is the thing it needed

**`tools/shot.py` is the project's first machine that looks at a page rather than measuring one.** The S083 close recorded "no headless browser on this machine" as the obstacle. That was wrong, and it was wrong from recall rather than from measurement: Google Chrome 150 is installed and runs headless, and Playwright 1.60 is already in the system Python. Playwright is pointed at the installed Chrome, so **no outside code was admitted to the machine** and Harness Rule 11 needs nothing from Kain.

**`tools/component_gallery.py` builds one page carrying every shared block**, and every fact on it is generated:

- the picture, shot from the real live page at 1200, 768 and 390
- which pages use it, read from the **rendered DOM** of 32 live pages rather than from the templates, so a class added by JavaScript counts and a class in a template nobody serves does not
- where its markup lives, and where its styling lives, both from `component_census.py`
- whether DSRD 8 names it

**The numbers, from tonight's run.** 286 class families in the theme. 107 shared, 164 page-local, 15 foreign (Complianz, WordPress core, Rank Math, SearchWP). **91 shared blocks are photographed. 16 are built and have no published page carrying them**, and they are named on the gallery rather than dropped.

**What is shared is decided mechanically**, so nobody has to agree with a judgement: emitted by two or more templates, or emitted by one of the theme's shared partials.

**Three faults it found in itself, each caught by looking at its own output rather than by a check passing:** it first photographed `.card__ctas`, a pair of buttons, as though it were the course card, because it took the shortest class rather than the block; it drew the three widths in equal columns, so a phone render looked larger than a desktop one; and it cropped components before their lazy images had loaded, which put holes in the pictures. All three are fixed and the reasons are written into the code.

## 3. The help article focus keywords are set, all 250

**Your S308 section 5 authorisation, done.** Every published help article's `rank_math_focus_keyword` is now the reader's question as the article's own title states it: trailing question mark dropped, first word lower-cased, every proper noun left alone. `How much does Achology cost?` gives `how much does Achology cost`, which is the worked example in the S083 recipe.

**250 of 250 written. 0 mismatch the derivation on read-back.** Nothing else moved: no copy, no title, no slug, no post content, and no modified date.

**The before state is snapshotted and it is outside the session**, at `05. Spreadsheets | Data | CSV Files/Help_Article_Focus_Keywords_Before_S084.tsv`: 250 rows carrying each article's id, title, old keyword and old score.

**Before: mean score 14.2, range 5 to 72, zero of 250 at 81 or better.**

**THE SCORE RE-RUN HAS NOT HAPPENED YET, and that is deliberate.** Rank Math computes its score in a browser, inside the editor, so `score_run.py` drives Kain's own Safari through AppleScript. He is looking at two rendered pages in Safari tonight, and a 250-article run would be fighting him for the browser. It is the first thing next session and it needs nothing from anybody.

## 4. Two things for your side

**A name collision on H7.** `BRIEF__Build_H7_The_Inbox_Wall_S309` commissions a hook called H7. **The harness already has an H7**, `h7_no_unanalysable_shell.py`, which is live and firing. The inbox wall should take the next free number, H8, or the existing one gets renumbered and every reference to it moves. Say which and I will build it. It waits on the FROM Chat tidy either way, as your brief says.

**The tidy is not done tonight and I am saying so rather than letting it look done.** `ASK__Archive_Every_FROM_Chat_File_You_Have_Finished_With_S309` arrived mid-session and grew twice while I was working. It is the next session's opening job, ahead of the H8 build that depends on it.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
