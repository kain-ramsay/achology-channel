**DISPOSITION (S284): stays. Waits on one Kain ruling asked this session: annotate the retired citations where they stand, or fix only the five references that read as live resources (recommendation: fix the five, adopt the retired-at annotation for the rest).**

# REPORT: every filesystem path in the DSRDs, checked once

**DOCUMENT TYPE:** report. Not a page spec. **From:** Claude Code, Session 063. **Date:** 18 August 2026.
**Commissioned by:** Kain, in session, on my offer after the stale library path was found. His word: "yes."
**Follows:** `CORRECTION__DSRD_7_Points_At_A_Repo_That_Was_Shut_Down_S063`.

---

## Why it was worth running

DSRD 7 pointed at a master library that had been shut down months ago, and asserted as fact that every image set existed there in both PNG and SVG. Nothing caught it, because **a path that no longer resolves looks exactly like a path nobody has needed lately.** Same shape as the dead channel: silence reads as quiet.

So every path-like reference in all sixteen DSRD documents was resolved once, mechanically.

## The headline

| | Count |
|---|---|
| Path-like references tested | 143 |
| Resolved where the document points | **82** |
| Named without a path, found elsewhere in the project | **34** |
| **Found nowhere at all** | **27** |

**Only the last group is a finding.** The middle group is the documents naming a file without claiming a location, which is normal and not a fault.

## Two corrections I made to the check before trusting it, both worth knowing

**The first run reported 115 of 129 as unresolved and was almost entirely wrong.** It was treating website addresses as filesystem paths: `/academy/`, `/policies/privacy-policy/`, `/learn/`. Those are site routes and no disk will ever have them. **A check that raises a hundred false alarms is worse than no check**, because the real fault hides in the noise and the whole report gets ignored.

**The second run was unfair to the documents.** Most references are a bare filename with no path at all, and testing those against fixed roots and calling them unresolved blames a document for something it never claimed. Hence the three-way split above: the question is not "does this path resolve" but "does this file exist at all".

## The 27 that exist nowhere

Grouped by what they appear to be, because the fix differs.

**Retired location, already corrected separately**

- DSRD 7 line 832: `~/Documents/GitHub/website-assets/website-images/`

**Prototype and preview files, named as evidence and since deleted or renamed.** These are the largest group. Most sit in DSRD 9 and DSRD 2, where a spec cites the HTML prototype it was written from.

- `category-hub-psychology-v9.html` (DSRD 2 line 125, DSRD 9 line 23)
- `category-hub-responsive-review-lightweight.html` (DSRD 9 line 345)
- `listing-page-psychology-articles-v10.html` (DSRD 9 line 488)
- `listing-page-responsive-review-lightweight.html` (DSRD 9 line 490)
- `article-page-self-awareness-v2.html` (DSRD 9 line 571)
- `RULING__Article_Source_Block_State_B_S268.html` (DSRD 9 line 745)
- `previews/about.html` (DSRD 9 line 1073)
- `previews/testimonials.html`, `previews/_build_testimonials.py` (DSRD 8 line 1222)
- `previews/_build_previews.py` (DSRD 10 line 41)
- `aaa-section-block.html` (DSRD 8 line 749)
- `footer-locked-session26.html` (DSRD 8 line 1925)
- `achology-course-card-proof-v2.html` (DSRD 8 line 482)

**Note the pattern:** the previews were retired deliberately at S245, on Kain's own ruling that a preview of a shipped page is a second copy of a truth the page already holds. **The documents that cited them were never walked afterwards.** That is not a defect in the ruling; it is the follow-through that was missed, and it is exactly what this sweep is for.

**Data and asset files**

- `Achology_Master__Books_and_Quotes.xlsx` (DSRD 1 line 161, DSRD 2 line 925), and `Achology Master Books and Quotes.xlsx` with spaces at DSRD 2 line 990
- `Achology_Video_Library_Template_V3.xlsx` (DSRD 2 line 1128)
- `Achology_Font_Como_Embedded_Base64_Complete.css` (DSRD 3 line 529)
- `bookshelf-bg.png` (DSRD 3 line 545). The theme has `bookshelf-book-notes.webp`, which may be the same asset renamed
- `Achology_Logo_for_Light_Mode__for_Website_Redevelopment_.svg` (DSRD 8 line 1317)
- `-028-icon.webp` (DSRD 7 line 862), a fragment of a range rather than a real filename

**Documents cited by name**

- `GUIDANCE__Standardising_The_Type_Across_The_Site_S269.md` (DSRD 7 line 191). It exists, in the channel, which this sweep does not walk. Not a fault
- `ANSWER__Icon_Registry_Key_List_S054.md`, `REPORT__Icon_Registry_Sweep_S054.md` (DSRD 7 lines 485, 672). Channel documents, since archived
- `SPEC__Policies_Index_Locked_Layout_And_Copy.md` (DSRD 9 line 1572)
- `Editorial Squad Voice Specification Document.md` (the DSRD folder's own README, line 15)

**Two that are not paths at all**, and are the last false positives I could not filter cleanly: `.php` and `.js` at DSRD 3 line 90, where the document names extensions rather than files.

## What I recommend, and it is not "fix all 27"

**Most of these are harmless citations of evidence that has since been retired.** A spec saying "written from this prototype" is a historical statement, and the prototype being gone does not make the spec wrong.

**The ones worth acting on are the ones a reader would go looking for and fail to find:** the retired library path, the four spreadsheet and asset files, and the logo SVG. Those look like live resources.

**The cheap structural fix, which I would rather have than a one-off tidy:** when a document cites evidence that has been retired, say so at the citation rather than deleting it. "Written from `category-hub-psychology-v9.html`, retired S245" costs six words and stops the next reader hunting.

**And this sweep should run again**, not because it will find much next time, but because the failure it catches is silent by nature. It is a small script and it runs in about a minute.

*No em or en dashes in this file; checked before writing.*
