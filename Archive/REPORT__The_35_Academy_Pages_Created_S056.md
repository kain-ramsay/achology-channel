> **DISPOSITION, S270 (Chat), 12 Aug 2026.** Read and verified: 35 in, 35 out, titles character for character against DSRD 5, site 26 to 62 pages, nothing published. No board card was found carrying the S267 page creation specification by name; the completion is recorded in the S270 handover, and the two open sub-items (admin menus wait on templates, internal linking unanswered) stay with Code's live spec file. Archived.

# REPORT: the 35 school and course pages are created as drafts. Thirty five in, thirty five out.

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Answers:** `SPEC__Create_The_35_School_And_Course_Pages_As_Drafts_S267.md`, unblocked by `REPLY__Academy_Page_Title_Plus_Three_Document_Corrections_S269.md`.
**Supersedes:** `STOP__Academy_Parent_Absent_Plus_The_35_Row_Pairing_S056.md`, which reported the block. The block is cleared and this is its resolution.

**Status: done, verified against DSRD 5 character for character. Nothing is published.**

---

## 1. The count, which is the check Rule 8 asks for

| | |
|---|---|
| Pages the specification enumerates | **35** |
| Pages created | **35**, plus the `/academy/` parent Chat authorised separately |
| Total under `/academy/` | **36** |
| Published | **0** |
| Templates assigned | **0**, as instructed |
| Pages created that the specification does not name | **0** |
| Pages the specification names that do not appear | **0** |

Site page count went from 26 to 62. 26 plus 36 is 62.

## 2. The parent

Created as an empty draft, titled **The Academy of Modern Applied Psychology**, per Chat's S269 answer on Kain's ruling. Title copied from the community reference document, which states it as the canonical name; not written by me.

## 3. How the result was proved, and one false alarm worth recording

**The script's own verification was not trusted.** It printed 35 drafts and nothing published, but a script checking its own work is the weakest possible evidence. So the result was read back independently: every page on the site was enumerated fresh, filtered to those whose address begins `academy`, and compared against the specification's 35 slugs and DSRD 5's titles parsed from the document again.

**The independent check found what it should:** 36 pages, 36 drafts, zero published, 8 at depth one (the parent plus 7 schools), 28 at depth two, no missing rows, no unexpected rows.

**It also reported two title mismatches, and they were false.** `A Beginner's Guide` and `An Entrepreneurs' Guide` came back as `A Beginner&#8217;s Guide` and `An Entrepreneurs&#8217; Guide`, which looked like the apostrophe had been mangled on the way in.

It had not. **`get_the_title()` runs WordPress's `wptexturize` filter, which converts a straight apostrophe to a curly one on output.** I was comparing filtered output against raw source. Read straight from the database, both titles carry hex 27, the straight apostrophe, exactly as DSRD 5 has it. The comparison now reads the raw stored value and the mismatch count is zero.

Recorded rather than quietly fixed, because it is the same shape as the parser fault in the typography census: a check that compares a processed value against an unprocessed one will report faults that do not exist, and next time it might report a real one as noise.

## 4. The full 36 row pairing

Every title below is the raw stored value, read back from the database, and every one matched DSRD 5 exactly.

**The parent**

| Address | Title |
|---|---|
| `/academy/` | The Academy of Modern Applied Psychology |

**The 7 schools**, parent `/academy/`, no template

| Address | Title, from DSRD 5 section 2 |
|---|---|
| `/academy/neuro-linguistic-programming/` | The School of Neuro-Linguistic Programming (NLP) |
| `/academy/cognitive-behavioural-psychology/` | The School of Cognitive Behavioural Psychology (CBP) |
| `/academy/life-coaching/` | The School of Life Coaching and Professional Helping |
| `/academy/person-centred-counselling/` | The School of Person-Centred Counselling and Psychology |
| `/academy/mindfulness/` | The School of Mindfulness, Applied Insight and Wisdom (MIW) |
| `/academy/mental-health/` | The School of Mental Health, Wellness and Emotional Resilience |
| `/academy/personal-growth/` | The School of Personal Growth and Development (PGD) |

**The 28 courses**, no template

| Address | Title, from DSRD 5 section 1 |
|---|---|
| `/academy/neuro-linguistic-programming/diploma-modern-applied-psychology/` | Diploma Course in Modern Applied Psychology (DiMAP) |
| `/academy/neuro-linguistic-programming/beginners-guide-nlp/` | A Beginner's Guide to Neuro-Linguistic Programming (NLP) |
| `/academy/neuro-linguistic-programming/nlp-practitioner/` | Neuro-Linguistic Programming (NLP) Practitioner Training |
| `/academy/neuro-linguistic-programming/nlp-master-practitioner/` | Neuro-Linguistic Programming Master Practitioner Course |
| `/academy/neuro-linguistic-programming/mindset-mastery-self-discovery/` | Mindset Mastery: The Ultimate NLP-Based Guide to Self-Discovery |
| `/academy/cognitive-behavioural-psychology/cbt-toolkit/` | The CBT Toolkit: Core Principles and Real-World Applications |
| `/academy/cognitive-behavioural-psychology/cbt-practitioner/` | Cognitive Behavioural Therapy (CBT) Practitioner Course |
| `/academy/cognitive-behavioural-psychology/cbt-mental-health/` | Cognitive Behavioural Therapy for Mental Health and Wellness |
| `/academy/life-coaching/life-coaching-certificate/` | Life Coaching Certificate Course (Beginner to Advanced) |
| `/academy/life-coaching/life-coaching-blueprint/` | Life Coaching Blueprint: The Complete Process and Practices |
| `/academy/life-coaching/skilled-helper/` | The Skilled Helper Training Course (with Prof. Gerard Egan) |
| `/academy/life-coaching/skilled-helper-practitioner/` | Skilled Helper Practitioner Course (Advanced to Expert) |
| `/academy/person-centred-counselling/hypnotherapy-practitioner/` | Hypnotherapy Practitioner Course (Beginner to Advanced) |
| `/academy/person-centred-counselling/counselling-skills-practitioner/` | Counselling Skills Practitioner Course (Beginner to Advanced) |
| `/academy/mindfulness/mindfulness-practitioner-diploma/` | Mindfulness Practitioner Diploma Course (Beginner to Expert) |
| `/academy/mindfulness/mindfulness-mental-health/` | Mindfulness for Mental Health, Personal Growth and Inner Peace |
| `/academy/mindfulness/mindfulness-leadership/` | Mindfulness for Highly Efficient Management and Leadership |
| `/academy/mental-health/mental-health-practitioner-diploma/` | Mental Health and Wellbeing Practitioner Diploma Course |
| `/academy/personal-growth/self-belief-emotional-intelligence/` | The Self-Belief, Emotional Intelligence and Assertiveness Masterclass |
| `/academy/personal-growth/authentic-confidence/` | Authentic Confidence, Core Identity and Self-Esteem Masterclass |
| `/academy/personal-growth/emotional-iq-social-skills/` | Master Your Emotional IQ and Revolutionise Your Social Skills |
| `/academy/personal-growth/clarity-purpose-effectiveness/` | The Clarity, Purpose and Personal Effectiveness Masterclass |
| `/academy/personal-growth/goal-setting-action-planning/` | The Strategic Goal Setting and Action Planning Masterclass |
| `/academy/personal-growth/communication-social-intelligence/` | The Communication Skills and Social Intelligence Masterclass |
| `/academy/personal-growth/hyper-focus-productivity/` | The Hyper-Focus, Self-Discipline and Productivity Masterclass |
| `/academy/personal-growth/mental-toughness-resilience/` | The Complete Mental Toughness and Inner Resilience Masterclass |
| `/academy/personal-growth/healthy-marriage-relationships/` | An Essential Guide to Healthy Marriage and Long-Term Relationships |
| `/academy/personal-growth/entrepreneurship-business/` | An Entrepreneurs' Guide to Launching and Growing a New Business |

## 5. What was not touched, per the specification's four rules

**Draft only.** Nothing published, confirmed by an independent count of published pages under `academy`, which is zero.

**Nothing else changed.** No menu, no navigation, no redirects, no copy, no settings.

**Only what is listed.** Zero unexpected pages.

**`/academy/schools/` untouched and still absent**, per Chat's confirmation that it is specified but unbuilt, is not one of the 35, and gets its own spec.

## 6. Still not started, deliberately

**The two admin menu entries**, Courses and Schools, which filter the Pages list by template. There is still no template to filter on. The specification itself says to build it when the templates exist, and that has not changed.

**The internal linking answer** across the 249 help articles, which that commission also asks for. It needs a real count off the live database and travels separately so it does not ride on a page creation report.

*No em or en dashes in this file; checked before writing.*
