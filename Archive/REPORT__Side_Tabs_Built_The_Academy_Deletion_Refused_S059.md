# REPORT: the two side tabs are built. The /academy/ deletion is refused, with evidence

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Answers:** `COMMISSION__Schools_And_Courses_Side_Tabs_Now_And_Delete_Academy_Draft_S273.md`, both jobs, and `BRIEF__Manifesto_Pair_Icon_Swap_S271.md`.
**Shipped:** theme v0.61.1, deployed and verified.

---

## Job 1: the two side tabs, built and verified

**Schools and Courses now appear as their own sidebar entries**, the way Book Notes and Quotes do, each opening WordPress's own Pages list filtered to that tree.

Read back from the live server after deploying:

```
academy parent found: 33498
Schools tab would list: 7 pages
Courses tab would list: 28 pages
```

**Seven and twenty eight, exactly as the acceptance asks.**

Keyed on the parent chain as you directed, and the `/academy/` parent is found **by its slug rather than by a written-in ID**, so a re-created parent does not silently empty both tabs. Two details worth recording because they are the difference between a tab that works and one that looks like it does:

- **The filter fails closed.** Where the tree cannot be resolved the list shows nothing rather than every page on the site. A filter failing open would put sixty pages under a tab labelled Schools, which is worse than an empty list because it reads as an answer.
- **The sidebar highlight and the screen title follow the tab.** Without that, both tabs light up "Pages" and the screen says "Pages", so Kain clicks Schools and lands somewhere that says Schools nowhere on it.

Nothing else changed: no URL, no content, no status, no front-end navigation, no menu.

## Job 2: I have not deleted page 33498, and this is a stop-and-ask

Your commission told me to check the parent chain first. **It does not survive the deletion, and the reason is bigger than a re-parent.**

Read from the live database this session:

```
pages parented to 33498: 7   (the seven schools)
school 33499 now: academy/neuro-linguistic-programming
courses under it: 5
course 33506 now: academy/neuro-linguistic-programming/diploma-modern-applied-psychology
draft pages whose address starts academy/: 35
```

**Page 33498 is not a stray secondary Academy page. It is the structural parent that gives all 35 pages their `/academy/...` addresses.** WordPress page URLs are hierarchical, so deleting it, or re-parenting the seven schools to 0, rewrites every one of those 35 addresses to drop the `/academy/` prefix.

Three things break with it:

1. **DSRD 1 §2.3**, which is the whole reason these are Pages using parent and child rather than a custom post type: "A school lives at `/academy/{school-name}/` and a course at `/academy/{school-name}/{course-name}/`."
2. **The 76 in-body links** in the help articles pointing at `/academy/...`, counted in my S059 linking answer.
3. **The S267 specification's own output.** These 35 drafts were created to that structure eleven days ago and reported as correctly parented.

**Kain's ruling was made on a description, not on this.** His words were "if he set up a secondary Academy page, delete it", which is the right instruction for what he was told existed: a duplicate. What exists is load-bearing. That is new information he did not have, so under Rule 5 the deletion stops here rather than being executed or worked around.

**What I recommend, and it is his call not mine.** Leave 33498 in place as the structural parent until the real `/academy/` page is built from its own signed spec, then either promote 33498 into that page or re-parent the seven schools onto the new one in the same sitting. It is a draft, so it is invisible to the public and costs nothing where it sits. The alternative, deleting it now and re-creating the whole tree later, throws away the 35 correct addresses to gain nothing.

**One thing that is genuinely wrong and worth his eye:** its title is "The Academy of Modern Applied Psychology", which is a real page title sitting on a placeholder. If the concern behind the ruling was that a half-made Academy page exists, that is the part to fix, and renaming it costs nothing.

## The manifesto icon swap, shipped

Your S272 amendment removed the reason I refused it, and I had not gone back to it. Done now.

`policies-content/manifesto.php`, the closing pair: Browse All of Our Courses takes `book-open`, Explore Our Seven Schools keeps `graduation-cap`. The FLAGGED comment block is replaced with the ruling, its DSRD 7 §5.2.3 record and the Code of Ethics scope guard.

Verified on the live page rather than in the file, by reading the rendered icon paths either side of the two card names:

```
Browse All of Our Courses -> M12 7v14, M3 18a1 1 0 0 1-1-1V4...   (Lucide BookOpen)
Explore Our Seven Schools -> M22 10v6, M6 12.5V16a6 3 0 0 0 12 0v-3.5   (Lucide GraduationCap)
```

## One thing I owed you and never sent

**`BRIEF__Course_Video_Rename_Map_S260` is blocked and has been silent.** Karen's Google Drive is not mounted on this Mac: `~/Library/CloudStorage` is empty and there is no `Achology Curriculum Videos` folder anywhere on disk, so the 28 course folders cannot be read at all.

The master workbook half is fine and present. The map needs both halves, so the job cannot start.

I found this earlier today and told Kain and not you, which left the job looking silent rather than blocked. That is the read-and-parked failure in the other direction and it is mine.

*No em or en dashes in this file; checked before writing.*
