> CHAT DISPOSITION, S357: answered. Kain ruled article 1 stands as the pattern; RULING__DSM_Article_1_Stands_As_The_Pattern_Draft_2_To_24_S357 is in TO Cowork. The check 4 question goes to Code as an Ask. Archived.

RULING, from Cowork, 10 September 2026, article 1 of the DSM series, drafted to BRIEF__Draft_The_24_DSM_Articles_In_Kains_Name_Exemplar_First_S356.md.

**Context.** The brief asked for article 1 only, "Why Isn't There a Blood Test for Depression?", drafted from the approved plan and the S355 ruling, gated, reported, then stopped for Kain's read before anything else in the series moves. This is that report.

**What was drafted.** `Content Records/instructor-article/blood-test-for-depression.md`. Kain's voice, first person, the Hook-Book-Look-Took shape as four headed sections after an unheaded opening: "So What Replaces a Blood Test for Depression?", "Why That Gap Is Not the Scandal It Sounds Like", "What This Changes When It Is Your Diagnosis", "What To Do With This". The DSM's part exactly as Part B row 1 gives it, no more: no DSM diagnosis is confirmed by a blood test or brain scan, the general absence well documented rather than the dropped "157 disorders, 1 biomarker" statistic. The course's part is course 018 lesson 2, "who is actually responsible for your mental and emotional wellbeing", closing on the Mental Health and Wellbeing Practitioner Diploma Course with DiMAP named beside it, both with facts read fresh this session from DSRD 5 and DSRD 4.

**A real sourcing gap, found and closed, not skipped.** The plan's own Part D marks claim 3, the "157 disorders, 1 biomarker" statistic, as not found and drops it from article 1. What it does not do is hand article 1 a replacement citation for its actual central claim, that no laboratory test of any kind currently confirms any psychiatric diagnosis. I sourced this myself this session, the same discipline the plan used for claims 28 to 30: a live search found Lakhan, Vieira and Hamlat, "Biomarkers in psychiatry: drawbacks and potential for misuse," International Archives of Medicine, 2010, fetched and read directly, carrying the exact line the article rests on: "there are no clinical laboratory tests to date that can be used by clinicians to diagnose patients with psychiatric disorders." Recorded in the record's own Search and Citation Brief, part 5, with the source and its kind, and linked in the body where the claim is made.

**A tool fault, worked around and flagged rather than hidden.** DSRD 5 and DSRD 4 are meant to be read through the dedicated Filesystem connector. Every call on it this session, list_directory, search_files, list_allowed_directories, failed identically with an "unsupported dialect" outputSchema error, a genuine fault in that tool's own definition, not a permissions or content problem. I read both DSRDs fresh this session through the device shell instead, at their real canonical paths, and copied the course-018 and DiMAP figures from there directly rather than from memory or an older secondary citation. Worth Code's eye if the Filesystem connector is meant to be the load-bearing route and is currently broken outright.

**A process miss, named rather than buried.** The brief's own sourcing standard expects the Search and Citation Brief gated on its own, with `content_gate.py --pre-draft`, before a word of body exists. I drafted the fields, the brief and the body in one pass, which meant the pre-draft gate's check 4 ("no body yet") had already lost the order when I ran it. I tested the brief in isolation afterward, body and notes stripped, and it passes every one of the pre-draft gate's other eight checks cleanly on its own merits. Check 4 itself still refuses the isolated brief alone, on a straight word count, which reads as the check not distinguishing the Search and Citation Brief's own permitted prose (825 words, a normal size for a complete eight-part brief) from an actual body. Possibly worth an Ask-Code question on whether check 4 is meant to exclude the brief section from its count; not something I am fixing myself on the checker. The remaining 23 will be drafted brief-first, gated, then written, in the correct order, whatever check 4 makes of it.

**Full gate, real and unedited, run after every fix above:**

```
CONTENT GATE  |  instructor-article  |  blood-test-for-depression.md
standard read from: DSRD 2 section 3.7, read S299 and again S332. 1,200 to 2,200 words (band widened from 1,500 by Kain at S352, for the six AI-and-bias articles in his own name; the eighteen published instructor articles all sit inside the wider band), first person, reflective. Section 3.7's Shape line (Kain, S332): four to eight headed sections, counted rather than named.

  PASS  total body words                               1397 (standard 1200 to 2200)
  PASS  headed sections, counted not named              4 found (standard 4 to 8)
  PASS  paragraphs of 2 to 4 sentences                  all within
  ..    one-sentence paragraphs                         1 of 24, allowed (Kain, S299)
  PASS  no em or en dashes                              0 found
  PASS  banned brand words                              none
  PASS  machine-written tells                           none
  PASS  reading ease (Flesch, approximate)              63.2 (band 60 to 70)
  PASS  required fields present (24)                    all present
  ..    fields not in the contract                      hub, practice
  PASS  every tag is one of the 36 locked slugs         3 tags, all registered
  PASS  outcome or problem tags, 2 to 4                 3 found
  PASS  lead_tag is one of the record's own tags        support-mental-health
  PASS  kh_tag_order carries the same tags as kh_tag    same set
  PASS  author is a key the people registry holds       kain-ramsay
  PASS  focus keyword set                               blood test for depression
  PASS  keyword in first 50 chars of SEO title          44 chars
  PASS  SEO title length                                44 (max 60)
  PASS  keyword in first 120 chars of description       139 chars
  PASS  description length                              139 (max 155)
  PASS  keyword in address slug                         blood-test-for-depression
  PASS  keyword verbatim in first 10% of body
  PASS  keyword in a subheading                         4 headings read
  PASS  keyword density                                 1.43% (5 hits, band 1.0 to 1.5)
  PASS  keyword unique in register                      unique
  PASS  no process text in the body                     clean
  PASS  internal link present                           3 found
  PASS  external link to the source present             1 found
  PASS  no paragraph over 120 words                     all within
  PASS  keyword in image alt text                       a person wondering why there is no blood test for depression
  PASS  stage 0 demand evidence recorded                Live search (Cowork, S352, 8 September 2026)

  GATE: PASS
```

**First run failed on three lines**, real and not smoothed over: three paragraphs ran to five sentences against the four-sentence ceiling, one instance of the banned word "plainly" (used twice, both missed on the first pass), and the external link to the Lakhan source was cited in prose but never actually hyperlinked into the body. Fixed by splitting the three long paragraphs, replacing both instances of "plainly", and adding the missing markdown link. Re-run to the clean pass above.

**The two new fields, hub and practice.** Both are S355 and S356 rulings this record carries correctly; both print as "not in the contract" because `content_gate_standards.json` has not yet been updated by Code to require them on this type, the same state the practice field was in on the quote-page type before that update landed. Not a defect in the record.

**Status.** Article 1 of 24 drafted, gated, and stopped here, exactly as the brief asked. Nothing else in the series drafts until Kain's word comes back through Chat.

OWED BACK: nothing further from this side. Kain's read, then his word back through Chat on whether article 1 stands as the pattern for the remaining 23.
