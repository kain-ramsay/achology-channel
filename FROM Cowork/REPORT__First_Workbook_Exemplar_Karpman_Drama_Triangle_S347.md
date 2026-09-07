# REPORT: the first workbook is drafted, gate-run, and waiting on your read

**DOCUMENT TYPE:** batch pointer, from Claude Cowork. **Date:** 7 September 2026.
**Answers:** `BRIEF__Draft_The_First_Workbook_To_The_Approved_Template_S347.md`.
**Read this cold.**

---

## 1. What is true now

One workbook is drafted: `DRAFT__The_Karpman_Drama_Triangle_Workbook.md`, in this same folder. Nothing else was drafted, no landing page, no second workbook, per the brief's own scope.

Before drafting, this session read, in the order the brief set: the approved template file (`06__WORKBOOK_TEMPLATE__Achology_Master_Layout.html`, Educational Publishing System folder, worked-example subfolder) and The Workbook Design Standard, both in full; the S345 ruling (already read this session); DSRD 2 section 3.4 and 3.4.1 (re-read in full this session, direct from the canonical file, to quote it exactly rather than from an earlier summary); and the `workbook-creation` skill.

Getting to the template file took a real detour worth naming: the Educational Publishing System folder was not among this session's connected folders (it was split out from the Website Upgrade project at S321, per the audit paper), and the Filesystem connector is broken in this session regardless (every call fails with the same schema-dialect error). Access was requested and granted through the device bridge instead, one prompt, covering the whole "Claude Code (Projects)" folder so the same route works for any sibling project next time.

## 2. The lecture and course

**Lecture 30, "The 'Drama' Triangle (of Unhelpful Dependencies)", course 007, the Cognitive Behavioural Therapy (CBT) Practitioner Course.** Read in full from its corrected transcript, never from a scan hit, per your brief's own instruction and the precedent it named (the S345 lesson 024-045 miscall).

Three lectures across the library teach the Drama Triangle. This session read all three in full before choosing:

- **007-030** (chosen): the whole lecture, start to finish, is the Drama Triangle. No digression.
- **018-094**, "Triangulation and Stephen Karpman's 'Drama' Triangle", Mental Health and Wellbeing Practitioner Diploma: also a clean, single-topic teaching, correctly cites Karpman's book where 007-030 does not (below).
- **001-100**: set aside. Its second half pivots to a different model entirely (the Superman complex / imposter syndrome), so it is not a clean single-topic source.

**The choice between 007-030 and 018-094 is this session's judgement, not a ruling, and it is close.** 007-030 was chosen because its course, cognitive-behavioural therapy, sits closest to what the model actually is: a way of reading a dysfunctional relational pattern. If you would rather the exemplar sit on 018-094, or on a different course pairing entirely, say the word and this session redrafts against that lecture instead; nothing else in the workbook changes.

## 3. Two corrections made to the source

The workbook-creation skill's rule: a verifiable factual slip in the lecture is corrected, not reproduced. Two were found and corrected, both named in the record's own sourcing note:

- The lecture dates the model to "maybe the early '70s." Karpman's paper, "Fairy Tales and Script Drama Analysis," was published in the Transactional Analysis Bulletin in 1968. The workbook states 1968.
- The lecture names Karpman's book two different ways in the same recording: "A Game-Free Life" early on, "A Game for Your Life" later. The actual title is *A Game Free Life* (Stephen B. Karpman, 2014). The workbook uses the correct title throughout.

## 4. Four contradictions found, as your brief expected

Your brief named three found and fixed at S345 and said a fourth would not be surprising. This session found four more, two in wording and two structural in the gate itself. Full detail, with the exact wording compared side by side, is in the drafted record's own sourcing note; the short form:

1. **Discussion-lead-in wording.** DSRD 2 section 3.4.1 and the actual template file carry genuinely different sentences for the line above the discussion questions. The template wins, per your brief's own precedence rule and the template file's own header note ("where the two disagree, this file wins"). The workbook uses the template's wording.
2. **Back-cover closing line.** DSRD 2 section 3.4.1 writes the closing line with its own embedded link. The template's actual small print carries no link at all, because the link lives on the button above it. The workbook follows the template.
3. **The gate's own required-fields list for a workbook bundles in the landing page's fields** (`landing_page_body`, `whats_inside`, `rm_focus_keyword`, `rm_seo_title`, `rm_seo_description`, `demand_evidence`), even though the standards file's own notes, and the approved worked example's own metadata file, treat those as a separate record with its own address and keyword. Drafting them here would mean drafting the landing page against your brief's explicit instruction not to.
4. **The gate's shared external-link check wants a citation link**, but the same standards entry's own notes say a workbook carries exactly two link destinations, the course page and the membership checkout, both internal, and "any third address in a workbook is a fault." An external link would itself be the defect on this content type.

None of the four was corrected at its source (DSRD 2, or the standards file) this session; that is not this session's place to do without your word.

## 5. The real gate, run twice, final printout

Run against the finished record with `content_gate.py workbook`, from the Educational Publishing System's own gate copy (the one with a "workbook" type actually entered):

```
CONTENT GATE  |  workbook  |  DRAFT__The_Karpman_Drama_Triangle_Workbook.md

  PASS  total body words                               1352 (standard 1100 to 1900)
  PASS  headed sections, counted not named             4 found (standard 4)
  PASS  paragraphs of 2 to 4 sentences                 all within
  ..    one-sentence paragraphs                        13 of 39, allowed (Kain, S299)
  PASS  no em or en dashes                             0 found
  PASS  banned brand words                             none
  PASS  machine-written tells                          none
  PASS  reading ease (Flesch, approximate)             61.5 (band 60 to 70)
  FAIL  required fields present (17)                   6 missing: landing_page_body, whats_inside,
                                                         rm_focus_keyword, rm_seo_title,
                                                         rm_seo_description, demand_evidence
  FAIL  focus keyword set                              missing
  PASS  internal link present                          1 found
  FAIL  external link to the source present             0 found
  PASS  no paragraph over 120 words                    all within
  FAIL  stage 0 demand evidence recorded
  FAIL  landing page body present                      the record carries no landing_page_body

  GATE: FAIL (5)
```

**Every one of the 5 failures traces to one of the two structural findings in section 4** (items 3 and 4): the six missing fields, the missing keyword, and the missing demand evidence are all landing-page work this session was told not to do; the missing landing-page body is the same; the missing external link is the workbook's own two-destinations rule doing its job. Nothing here is a defect in the drafted words. This is not called clean, because it is not clean against a gate config that is itself asking for out-of-scope work: named plainly rather than quietly passed off as green.

**What this means for the standalone test, the one check no machine runs:** read cold, the teaching explains the three positions in full, defines its own terms, carries one illustration, and the exercise walks a reader's own real relationship through the same three positions in the same order the teaching used. This session's own read says it stands alone; it has not had a second reader yet.

## 6. What this session did not do, by your brief's own scope

The cover image (the library does not exist yet, per the Design Standard's own section 8), the section icons and logo placeholders (named there as Chat's and Code's job, and two of the four icon paths are themselves still owed real lucide-static data), the landing page, and a second workbook.

## 7. What's next

Your read of the one workbook. On your word: whether 007-030 stands or you'd rather 018-094 or another pairing; whether the four contradictions in section 4 get corrected at their source now or wait; and, per the brief, volume only runs after this exemplar is approved.

---

OWED BACK: your read of `DRAFT__The_Karpman_Drama_Triangle_Workbook.md`, and your word on the lecture choice in section 2.

*No em or en dashes in this file; checked before writing.*
