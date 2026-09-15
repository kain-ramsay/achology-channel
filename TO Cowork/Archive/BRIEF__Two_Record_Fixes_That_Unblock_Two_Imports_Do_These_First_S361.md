# BRIEF: two record fixes that unblock two imports, before anything else in your tray

**Filed by Claude Chat, Session 361. Date:** 15 September 2026.
**Kain's instruction, live:** cards are being closed. Two Code imports are refused at the front door on record faults only you can fix. Do these two before the three briefs already in your tray; both are mechanical and neither adds new content.

---

## Job 1. Strip the dead `featured_image` field from all 200 course 018 quote records

Code's S117 report: all 200 CQ018 records carry an identical `featured_image` value pointing at a file that exists nowhere, and no other quote record on the site carries the field at all. The import refuses on it. Remove the field from all 200 records, change nothing else, run each through `content_gate.py`, and confirm 200 of 200 pass. Report: 200 records corrected, gate count, path. Then Code runs `BRIEF__Import_And_Score_All_200_CQ018_Quote_Pages_Publish_On_Kains_Word_Only_S360`.

**Closes the Cowork half of:** Course quotes card.

## Job 2. Bring all 24 DSM articles up to the paragraph floor, carrying the sourcing corrections

Code's S117 report: all 24 DSM series records fail the paragraph-floor check (the floor Kain commissioned at S357, held in `content_gate_standards.json`; read the value there, never from this file). Breaches run 6 to 33 short paragraphs per record. Rewrite each record so every paragraph meets the floor, holding the article's argument, voice (Kain's own name) and course close exactly as drafted.

**While you are inside each record, apply the sourcing register.** At S358 the manuscript chapters behind this series were checked live claim by claim. Nothing is clear for use unless CONFIRMED or CONFIRMED-WITH-CORRECTION, and a corrected claim is carried only in its corrected form. The register is appended in full below. Six matter most:

- The "only 1 of 157 DSM-5 disorders has a biomarker" statistic: drop entirely, unverifiable.
- Homosexuality "not removed from the DSM until 1987": wrong; full removal is 2013 (DSM-5).
- The DID case counts: use the corrected chain, roughly 90 cases by 1970, about 200 by 1980, about 6,000 by 1986, about 40,000 by the mid-1990s.
- Autism in California: 273 per cent, 1987 to 1998, not 1987 to 1994; the "237 per cent" figure does not exist.
- The bereavement disorder: the 6 to 12 month criterion belongs to DSM-5-TR (2022, Prolonged Grief Disorder), not DSM-5; prevalence about 10 per cent with a variability caveat, not 7 to 20.
- The "Ms T" case vignette: not a citable case; do not present it as a sourced case.

Also standardise the spellings: Allen Frances, James Davies, Michel Foucault; DSM-I had 106 categories; major depression is 5 of 9 symptoms; the DSM-5 "porous boundaries" quote is page 6.

Run each rewritten record through `content_gate.py`; report 24 of 24 passing, the paragraph-floor count per record before and after, and the path. Then Code runs `BRIEF__Import_And_Score_All_24_DSM_Series_Records_As_Drafts_Publish_Nothing_S357`.

**Closes the Cowork half of:** 24 articles in Kain Ramsay's name.

## Job 3. Bring three instructor articles up to the paragraph-rhythm rule: I04, I14, I18

Code's finish pass today (DONE B, S117): I04 (blind-spots-that-keep-people-stuck) 6 paragraph breaches; I14 (busy-but-not-fulfilled) 17 breaches plus one "plainly"; I18 (persuade-someone-who-disagrees) 9 breaches. All three were drafted before the rule took its present shape. Split the over-long paragraphs at natural breaks, swap "plainly" for "simply" in I14, change no other word; Kain has already read and approved these articles, so this is rhythm only, never a rewrite. Run each through `content_gate.py`; report 3 of 3 passing with the breach count before and after. These three are the last thing holding the 18 instructor articles card, so do this one first of the three jobs.

**Closes the Cowork half of:** 18 instructor articles.

## Job 4. The same paragraph-split pass across all 50 unpublished book note records

Code ran `content_gate.py` fresh on every unpublished book-note record today (REPORT S117): zero of fifty pass, 44 on the paragraph-rhythm rule alone, 4 on that plus body word count, 1 on machine-written tells, 1 on tag count. Same cause as Job 3: drafted before the rule took its present shape. Split the over-long paragraphs at natural breaks across all fifty, no rewording; on the 4 short bodies and the 1 tag-count record, make the smallest change the gate names; on the 1 tells record, swap the flagged words per the Base Voice register. Run each through `content_gate.py`, report 50 of 50 passing, the count before and after, and the path. Then Code imports and publishes through `tools/book_note_import.py` and `publish_gate.py`.

**Closes the Cowork half of:** Book notes backlog.

**Order across the four jobs:** 3, then 1, then 4, then 2.

---

OWED BACK: one DONE report per job, to FROM Cowork, with the counts named above.

*No em or en dashes in this file above this line; checked before writing. The appended register below is reproduced as filed at S358.*

---

## Appendix: the S358 sourcing register, chapters 1 and 2

| # | Claim | Outcome | Real source found | Correction / notes |
|---|-------|---------|--------------------|---------------------|
| 1 | WHO def. of mental health | CONFIRMED | WHO Global Health Observatory, "Mental Health, Brain Health and Substance Use"; WHO "Mental health: strengthening our response" fact sheet | Exact wording match. |
| 2 | WHO def. of mental disorder | CONFIRMED-WITH-CORRECTION | Current WHO fact sheet, "Mental disorders" | Use WHO's current wording: "A mental disorder is characterized by a clinically significant disturbance in an individual's cognition, emotional regulation, or behaviour." Not the chapter's. |
| 3 | "Only 1 of 157 DSM-5 disorders" has a biomarker | NOT FOUND, DO NOT CARRY | none | Drop the statistic. The general point that psychiatric diagnoses lack biomarkers is defensible with a different citation. |
| 4 | Steven Hyman quotes and title | CONFIRMED-WITH-CORRECTION | Hyman, "The Diagnosis of Mental Disorders: The Problem of Reification," Annual Review of Clinical Psychology 6 (2010) 155 to 179 | "unintended epistemic prison" is verbatim and confirmed. "Scripture and subjectivity" not found; drop. NIMH Director 1996 to 2001 confirmed. Title him psychiatrist and neuroscientist. |
| 5 | DSM edition history | CONFIRMED-WITH-CORRECTION | Wikipedia DSM article; Vukic et al., Behavioral Sciences 6(1):5 (2016) | DSM-I was 106 categories, not 102. DSM-II 182, DSM-III 265, DSM-III-R 292, DSM-IV 297 and 886 pages all confirmed. |
| 6 | DSM-IV definition of mental disorder | CONFIRMED | APA DSM-IV (1994), quoted in Stein et al., Psychological Medicine (2010) | Verbatim match. |
| 7 | DSM-5 definition of mental disorder | CONFIRMED | APA DSM-5 (2013), Introduction | Exact match. |
| 8 | Homosexuality: 1970 protests, 1971 disruption, 1973 vote, "not removed until 1987" | CONFIRMED-WITH-CORRECTION | Wikipedia, "Homosexuality in the DSM"; AJP Residents' Journal, "Gay Is Good" (2022) | 1970, 1971, December 1973 vote and 1974 referendum all confirmed. Full removal is 2013 (DSM-5), not 1987. |
| 9 | Spitzer / Carlat "arbitrary number of five" | CONFIRMED | Carlat, Unhinged, Free Press, 2010 | Book, author and quote confirmed. |
| 10 | "Cracked" by "James Davis" | CONFIRMED-WITH-CORRECTION | James Davies, Cracked, Icon Books, 2013 | Author is James Davies. |
| 11 | DSM-5 depression: 5 of 8 symptoms | CONFIRMED-WITH-CORRECTION | DSM-5 Criterion A, Major Depressive Disorder | 5 of 9 symptoms, not 8. |
| 12 | April 2021 "state of emergency" DHSC briefing | CONFIRMED-WITH-CORRECTION | McGregor press release, June 2021 | Ayton, Virgo and the fourfold demand rise are real. The date April 2021, the phrase "state of emergency" and the BMI wording are unconfirmed; do not carry as stated facts. |
| 13 | DSM-5 Introduction "porous boundaries" quote, p.5 | CONFIRMED-WITH-CORRECTION | DSM-5 Introduction, cited in Frontiers in Psychology (2015) | Page 6, not 5. |
| 14 | 2004 subthreshold study, about 53 per cent | CONFIRMED | Lewinsohn et al., Psychological Medicine 34(4) (2004) 613 to 622 | 52.5 per cent; confirmed. |
| 15 | MPD/DID history and case counts | CONFIRMED-WITH-CORRECTION | Piper and Merskey, Canadian Journal of Psychiatry 49(9) (2004); Taylor and Martin (1944); Nathan, Sybil Exposed (2011); Thigpen and Cleckley (1957) | Both "before 1970" figures wrong. Use about 90 by 1970, about 200 by 1980, about 6,000 by 1986, about 40,000 by the mid-1990s. Sybil and Three Faces of Eve facts confirmed. |
| 16 | Autism prevalence and California DDS percentages | CONFIRMED-WITH-CORRECTION | CDC 2020; California DDS reports 1999 and 2002 | 1 in 54 (2020) confirmed. 273 per cent is 1987 to 1998, not 1987 to 1994. "237 per cent" does not exist; drop it. |
| 17 | UC Davis M.I.N.D. Institute 2002 study | CONFIRMED | California DDS report, 17 October 2002 | Confirmed including the two cohorts and the conclusion. |
| 18 | 2020 diagnostic inflation meta-analysis | CONFIRMED | Fabiano and Haslam, Clinical Psychology Review (2020) | Figures match exactly. Note autism deflated DSM-IV to DSM-5. |
| 19 | Haslam, "Concept Creep" | CONFIRMED | Haslam, Psychological Inquiry 27(1) (2016) 1 to 17 | Page-specific content not verbatim-verified. |
| 20 | DSM-IV cost 5 million vs DSM-5 cost 25 million | CONFIRMED (figures); NOT FOUND (NIMH/peer-review contrast) | Allen Frances, Psychology Today, May 2012 | Use the dollar figures. Drop or soften the NIMH and peer-review contrast. |
| 21 | "Allan Frances" | CONFIRMED-WITH-CORRECTION | Wikipedia; Medscape | Spell Allen Frances. His stated concern is overdiagnosis and lowered thresholds; treat "reliability over patient benefit" as paraphrase. |
| 22 | DSM-5 hypomania criteria | CONFIRMED | DSM-5 Hypomanic Episode criteria | Exact match. |
| 23 | Persistent complex bereavement disorder, 6 to 12 months, 7 to 20 per cent | CONFIRMED-WITH-CORRECTION | Wikipedia, "Prolonged grief disorder"; Prigerson et al., World Psychiatry (2021) | In DSM-5 it sat in Section III. The 6 to 12 month criterion and full status belong to DSM-5-TR (2022), renamed Prolonged Grief Disorder. Prevalence about 10 per cent with a variability caveat. |
| 24 | NICE stepped-care model | CONFIRMED | NICE depression guideline (NBK63757) | Confirmed. |
| 25 | "Michael Foucault" | CONFIRMED-WITH-CORRECTION | Wikipedia; Sedgwick, Psycho Politics | Michel Foucault. |
| 26 | "Ms T" case | NOT FOUND, DO NOT CARRY | none | No matching published case report. Do not present as a sourced case. |
| 27 | Doctors interrupt after about 11 seconds | CONFIRMED | Singh Ospina et al., Journal of General Internal Medicine 34 (2019) 36 to 40 | Confirmed. |
