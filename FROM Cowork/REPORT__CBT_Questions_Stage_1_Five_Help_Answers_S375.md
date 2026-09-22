REPORT, from Cowork to Claude Chat, Session 375. Job 3 of the S374 tray. Completes Stage 1 of `BRIEF__The_CBT_Questions_The_Whole_Job_In_Three_Stages_S373.md`: five Help answers, drafted, gate-passed and filed for Kain's read. Stage 2 (the remaining seven CBT questions) does not start until Kain files his yes in this tray, per the brief.

# CBT Questions Stage 1: Five Help Answers, All Gate-Passed

## Method

For each of the five questions: read The Achology Base Voice and the frozen exemplar (`HELP__cbt-practitioner-vs-cbt-therapist.md`, approved by Kain S373) before drafting; researched live sources where a claim needed one (NHS Health Careers, the University of Oxford's PGDip admissions page, the BABCP's own accreditation page, the NHS's own CBT overview, all read live 21 to 22 September 2026); wrote to the reduced four-part Search and Citation Brief (DSRD 2's `brief_form: "reduced"` for help-answer); checked each keyword free in `KEYWORD_REGISTER.csv` before claiming it; drafted, pushed to device, and ran `content_gate.py` against the live standard, iterating on every failure until each of the five showed GATE: PASS. Appended all five claimed keywords to the canonical register once every record passed (1093 rows before, 1098 after).

## The five, gate-passed

| Question | Slug | Words | Flesch | Density | Category |
|---|---|---|---|---|---|
| Is a CBT certification worth it? | is-a-cbt-certification-worth-it | 808 | 65.1 | 1.49% | comparisons-and-alternatives |
| How do you start learning CBT? | how-to-start-learning-cbt | 675 | 68.1 | 1.48% | getting-started |
| What is the best CBT course or certification? | best-cbt-course-or-certification | 672 | 63.7 | 1.49% | comparisons-and-alternatives |
| How do you become a CBT therapist, and do you need a degree? | how-to-become-a-cbt-therapist | 845 | 68.9 | 1.42% | comparisons-and-alternatives |
| What does a CBT course cover? | what-does-a-cbt-course-cover | 820 | 68.8 | 1.46% | curriculum-and-subjects |

All five: GATE: PASS, every check green, on the live device copy in `Content Records/help-answer/`, confirmed by a fresh `content_gate.py` run against each this session (not a cached earlier pass).

## The three next questions per answer (rule 6), and where each goes

**Is a CBT certification worth it?**
1. What does the certificate actually qualify me to do? Answered in outline on the page; routed to the certification-qualifies answer.
2. How is a CBT practitioner different from a CBT therapist? Answered in outline; routed to the frozen exemplar.
3. Which of the three CBT courses should I actually pick? Answered on the page in the courses block; routed to the best-course answer for the fuller comparison.

**How do you start learning CBT?**
1. Which course should I actually pick to start? Answered on the page; routed to the first-course-for-a-beginner answer.
2. Is it worth paying for a course instead of free material? Answered in outline; routed to the worth-it answer.
3. What exactly is covered once I start? Answered in outline; routed to the course-content answer (now live as question 5, above).

**What is the best CBT course or certification?**
1. Is Achology's course actually worth the money? Answered in outline; routed to the worth-it answer.
2. What's the difference between a CBT practitioner and a CBT therapist? Answered in outline; routed to the frozen exemplar.
3. How does Achology compare to Udemy specifically? Answered in outline; routed to the Udemy comparison answer (not yet drafted; flagged below).

**How do you become a CBT therapist, and do you need a degree?**
1. What is a CBT practitioner, if not a therapist? Answered in outline; routed to the frozen exemplar.
2. Can I call myself a therapist after an Achology course? Answered in outline; routed to the call-myself-a-therapist answer.
3. Is an Achology certificate worth having if I'm not going down either route? Answered in outline; routed to the worth-it answer.

**What does a CBT course cover?**
1. Is a CBT certification actually worth the money? Answered in outline; routed to the worth-it answer.
2. How do you actually start learning CBT? Answered in outline; routed to the start-learning answer.
3. What is a CBT practitioner, if not a therapist? Answered in outline; routed to the frozen exemplar.

All fifteen route somewhere live or planned. One gap: the Udemy comparison answer that "best CBT course or certification" routes to isn't drafted yet; it's linked as a planned page, same as the frozen exemplar links to pages that came after it. Not a broken link on the page itself, since none of these route mentions are hyperlinks, only named next-questions.

## Per-H2 contraction count, each answer

**Is a CBT certification worth it?** Opening 2. "What does 'worth it' actually mean here?" 5. "What do you actually get for your money?" 4. "Will a CBT certificate get you a job?" 2. "Is it worth it compared to free content online?" 4. "So, Is a CBT Certification Worth It in the End?" 1. "Where can you start?" 0.

**How do you start learning CBT?** Opening 1. "Is CBT Hard to Learn?" 2. "Can you really learn it on your own?" 1. "How to Start Learning CBT, Step by Step" 3. "What does the first stage actually involve?" 3. "How long before you're using it in your own life?" 4. "Where can you start?" 0.

**What is the best CBT course or certification?** Opening 4. "What's the Best CBT Course If You're Already a Clinician?" 5. "...If You Just Want a Cheap Taste of the Ideas?" 7. "...If You Want to Actually Use CBT Yourself?" 5. "So, What Is the Best CBT Course or Certification, Really?" 5. "Where Can You Start With Achology?" 0.

**How do you become a CBT therapist?** Opening 2. "What's the NHS Route..." 5. "What's the University Route?" 2. "Do You Need a Degree?" 3. "...Is There a Shorter Route?" 6. "Where Can You Learn CBT With Achology?" 2.

**What does a CBT course cover?** Opening 1. "What Are the Six Areas..." 3. "How Long Does It Take..." 2. "Do You Need Any Background in Psychology First?" 3. "Is It Just Theory, or Real Practice Too?" 4. "What Does the NHS Say CBT Actually Involves?" 4. "What Does a CBT Course Cover, in Practice?" 1. "Where Can You Learn CBT With Achology?" 0.

Gap: the course-list section ("Where can you start?" / "Where Can You Start With Achology?" / "Where Can You Learn CBT With Achology?") reads at 0 contractions in three of the five answers. It's short, factual, list-led text, and reads naturally without one, but it's a genuine gap against "contractions throughout" as a standing rule and I'm flagging it rather than quietly deciding it doesn't count.

## Voice check

Not machine-run. Cowork's `content_gate.py` checks structure, SEO mechanics and machine-written tells, not voice. Whether these five actually sound like Achology, and like a kind person talking, is Kain's own read to make, not a gate result to report.

## Gaps and findings logged this batch

1. **The full gate enforces `shared.locked_tags` on every content type, help-answer included, even though help-answer's own type entry in `content_gate_standards.json` never declares `locked_tags`, `kh_tag`, `lead_tag` or `kh_tag_order`.** It runs via `main()`'s std-merge (`std = dict(cfg["shared"]); std.update(cfg["types"][ctype])`), which pulls the shared block in regardless. The frozen exemplar predates this and was never run against it. All five new records carry real, evidenced `kh_tag`/`lead_tag`/`kh_tag_order` values from DSRD 1 section 5.6's locked register; not yet checked by Kain.
2. **`content_gate.py`'s `BODY_TRAILER_HEADINGS` whitelist, which decides where body-word and paragraph scanning stops, doesn't include "the three next questions a first-time visitor would ask (rule 6)".** Left in its usual place (after the body, before Sourcing record), that heading's numbered list gets scanned as body content, inflating the word count and occasionally tripping the paragraph cap on numbered-list items. Worked around, in all five records, by placing that section after Sourcing record and Open items, so it falls after a heading the code does recognise. Not a fix to Code's file; a fix to my own records' section order.
3. **Consecutive bullet-list items with no blank line between them count as one merged paragraph block** in `content_gate.py`'s `paragraphs()`, contradicting the written standard's stated intent that list items aren't counted as paragraphs. Every bulleted block in all five records (course lists, Related Questions) carries a blank line between each item to avoid this.
4. **The three zero-contraction H2 sections**, named above under "Per-H2 contraction count".
5. Nothing in the stances or standards could not be squared with a question this batch; no scope drift from the brief.

## Definition of done

All five records written to their live locations in `Content Records/help-answer/`, each confirmed GATE: PASS on a fresh device run this session. `KEYWORD_REGISTER.csv` updated with all five keywords, 1098 rows confirmed. This report filed to FROM Cowork.

Per the brief: Stage 1 stops here. Kain reads all five in full. Nothing in Stage 2 starts until Chat files his yes in this tray.

COWORK | Batch: 5 | Drafted: 5 of 5 | Gate and evaluator: PASS (5 of 5) | Skipped: none | Outside brief: none
