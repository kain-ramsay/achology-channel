# ANSWER: what internal linking has run across the help articles, and the counts today

**From:** Claude Code, S059. **Date:** 2026-08-14.
**Answers:** the closing question in `SPEC__Create_The_35_School_And_Course_Pages_As_Drafts_S267.md`, the section headed "And one question, which is a question and not a commission".
**Method:** every published help article's `post_content` read out of the live build database this turn and counted by script, plus an HTTP status check on every link target run from inside the server so the edge protection could not answer for it. Nothing was changed. Counts, not opinions, as asked.

**One correction to the question's premise before the numbers: there are 250 published help articles, not 249.** The 250th is the principle-based reflective discussion article you commissioned. Every figure below is out of 250.

---

## 1. What ran, and when

| When | What | Result |
|---|---|---|
| S226, 28 July | `BRIEF__Internal_Links_Across_The_249_Help_Articles.md`, the link map: 46 phrase-to-target rows, eight rules | commissioned |
| S228, 28 July | the map run across all 249 | 249 read, **187 gained links, 459 added**, filed as `REPORT__Link_Map_Pass_Across_The_249.md` |
| S230 to S046, 5 Aug | `INSTRUCTION__Verify_Help_Section_Link_Ceiling.md`, steps 1 and 2: measure the ceiling | **161 of 250 over eight**, filed as `REPORT__In_Body_Link_Ceiling_Measured.md` |
| S245, 5 Aug | Kain ruled the ceiling splits by article job, written into DSRD 1 §6.4 rule 7 | the trim was to run **after** the keyphrase score run |
| since | **steps 3 to 5, the trim, have never run** | see section 4 |

**One thing in that history matters more than the rest.** At S228 Kain overrode rule 8 of the brief, which said write a link only where the target returns 200 today. His words, on the record in that report: "yes, write every link now". So 408 of the 459 new links were written pointing at pages that did not exist. That decision is the single largest fact about the section's link graph today, and section 5 measures what it now costs.

## 2. The counts today

| | |
|---|---|
| Published help articles | 250 |
| Anchors in article bodies | **2,439** |
| of which internal | 2,433 |
| of which external | 5 |
| of which fragment or mail | 1 |
| Distinct internal targets | 298 |
| Articles carrying no links at all | **0** |
| Median links per article | 9 |
| Heaviest article | 17 |

**This is unchanged since 5 August.** The S046 measurement of the same thing, same definition, same 250 articles, was 2,438. It is 2,439 now, and the distribution below is identical to the S046 table in every band. Nothing has moved.

The 2,516 figure in the S228 report is not comparable to these and should not be read as a fall. It was taken by a different extraction; I have not re-derived it and I am not treating it as the same measurement.

**In-body only.** Breadcrumbs, the Related Questions block, the CTA block and the cross-link are rendered by the template and are in none of these numbers.

## 3. How they are distributed

**By article:**

| in-body links | articles |
|---|---|
| 0 | 0 |
| 1 to 4 | 7 |
| 5 to 8 | 82 |
| 9 to 15 | 152 |
| 16 or more | 9 |

**By target family, counted as link instances:**

| family | instances |
|---|---|
| article to article | 1,810 |
| commercial (courses, academy, membership, pricing, access, accreditation, certification) | 461 |
| policy | 84 |
| about | 39 |
| knowledge hub | 7 |
| other internal | 32 |

**The four heaviest single targets** are `/courses/` at 113, `/membership/` at 70, `/certification/` at 67 and `/academy/schools/` at 52. The heaviest article target is `/help/events-and-mentorship/achology-live-events-types/` at 43 inbound.

**Three quarters of the section's links point at itself.** 1,810 of 2,433 are article to article. That is the shape to hold in mind before any authority strategy is designed: the help section is currently a closed loop that feeds itself, and 461 links, under a fifth, point at anything commercial. **76 of the 250 articles carry no commercial link at all.**

## 4. The ceiling

DSRD 1 §6.4 rule 7, read from the canonical document this turn: "Eight in-body links to a page is the working ceiling for a support answer or a short article. A page past that reads as a link farm and each link is worth less."

**161 of 250 are over eight.** That is the same 161 measured at S046, band for band. Kain's S245 ruling split the ceiling by article job: a narrow support answer keeps eight, an orientation answer has no fixed ceiling. **The classification that ruling requires has never been applied**, so no article has been trimmed and none has been recorded as legitimately over. The work was sequenced behind the keyphrase score run and that is still where it sits.

## 5. Where the links actually go, checked rather than assumed

Of the 623 links pointing outside the help section:

| | distinct targets | link instances |
|---|---|---|
| Resolve to a live page today | 15 | 132 |
| Do not resolve: 404 | 33 | **421** |
| Resolve, but to the wrong place | 1 | **70** |

**421 in-body links currently return a 404.** They are the commercial half: `/courses/` 113, `/certification/` 67, `/academy/schools/` 52, `/access-all-areas/` 29, `/pricing/` 27, `/accreditation/` 27, `/enquiries/` 20, `/free-events/` 7, `/free-coaching/` 3, and 76 across `/academy/` and the school and course pages. The 35 school and course pages I created at S058 are drafts, so they count as 404 here and will resolve the day they publish.

**The one that is worse than a 404, and is new information.** `/membership/` does not 404. It **301 redirects to `/help/getting-started/membership-first-or-course-first/`**, a help article. So 70 links written to reach the membership sales page currently deliver the reader back into the help section. In link-graph terms those 70 are not commercial links at all; they are article-to-article links wearing a commercial address, and the real commercial figure is 391 rather than 461. I have changed nothing about it and am not proposing to; it belongs with the redirect map work, and it is the kind of thing a linking strategy would be built on top of without noticing.

The knowledge hub routes do resolve: `/learn/articles/`, `/learn/workbooks/`, `/learn/book-notes/` and `/learn/quotes/` all return 200, and `/learn/` 302s to `/learn/articles/`. A database check alone reports those as missing, because they are theme routes and not pages, which is why the status check was run from inside the server.

## 6. The mirror rule

**I could not find a mirror rule, and I am reporting that rather than assuming what it means.** I read DSRD 1 §6.4 in full and searched all ten DSRDs and the whole channel for it. The only mirror rules written anywhere are breadcrumbs mirroring the URL hierarchy (DSRD 1) and the image-set mirrors in DSRD 7. Neither is about linking. The S226 brief's eight rules contain nothing reciprocal, and its rule 1 is first-mention-only, which does not imply a return link. The nearest thing that exists is the Related Questions block, four per article, and that is template-driven rather than in-body.

So that it is answered rather than deferred, I measured reciprocity anyway across the article-to-article graph:

| | |
|---|---|
| Directed article-to-article edges | 1,569 |
| Directions with a return link | **782** |
| Directions with none | **787** |
| Mutual pairs | 391 |
| Median inbound article links per article | 5 |
| Most linked article | 43 inbound |
| Articles with no inbound article link at all | **1** |

**It holds both ways just under half the time**, which is what you would expect from a pass that was never asked to make it hold. The single orphan is `/help/curriculum-and-subjects/dimap-course-upgrade/`: nothing in the section links to it.

**If a mirror rule does exist somewhere I cannot see, tell me where and I will measure against it rather than against my own reading.**

## 7. Two defects found while counting

Both small, both left alone because you said answer and do not act.

1. **One self-link.** `/help/curriculum-and-subjects/seven-schools-achology-curriculum-explained/` contains a link to its own address. That breaks S226 rule 3 and DSRD 1 §6.4 rule 3. It is the only one in 2,439.
2. **The 301 in section 5.** 70 links reaching a help article instead of the membership page.

Clean: no link sits inside a heading anywhere in the 250, no anchor is unterminated, no anchor is empty, and no article carries zero links. Rules 1, 2 and 4 of the brief hold across the corpus.

## 8. What is worth knowing before a strategy is designed

Stated as facts, not as a recommendation, since the strategy is Kain's and not mine.

- The section links to itself 1,810 times and to anything commercial 391 times once the redirect is discounted. Any plan to build the authority of specific pages starts from a graph that currently concentrates it inside the help section.
- 421 links are already written and waiting on pages that do not exist. They become live authority the day those pages publish, with no editing pass needed. The 35 drafts are most of that.
- 161 articles sit over the ceiling and none has been classified under the ruling that governs them. A relinking pass and the trim touch the same 161 articles, so running them separately means editing those articles twice.
- The corpus has not moved since 5 August, so every measurement in this file can be treated as current rather than as a snapshot that is drifting.

*No em or en dashes in this file; checked before writing.*
