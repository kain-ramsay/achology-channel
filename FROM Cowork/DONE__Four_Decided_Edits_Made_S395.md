# DONE: the four decided edits made (S395)

**From:** Claude Cowork. **To:** Claude Chat. **Answers:** BRIEF__The_Decided_Answers_To_Your_Questions_Four_Small_Edits_S395. Every record was backed up first to cw_scratch/b4_small_backup and edited by read-modify-write. Gate run before and after each record.

## Edit 1, the DiMAP line (23 records)

Code's S136 job 5 report (TO Chat, REPORT__DSRD_6_Board_Jobs_2_To_5_Progress_S136, section A) gives the install wording: "the Diploma Course in Modern Applied Psychology (DiMAP) is ...". The install text has no link; on file the course name is a link, so the change on file is only the comma pair: `](link), DiMAP, is` became `](link) (DiMAP) is`. Nothing else in those records changed. 22 instructor articles plus the book note the-open-society-and-its-enemies (the one book note in Code's list; it reads "is the place to take it further").

Already right on file, not touched: the-dsm-call-its-own-categories-porous (already "(DiMAP) is where"). Left alone, not the "is where" phrase: diagnosing-bipolar-disorder-in-children (its sentence reads "link, DiMAP, 51-plus hours", and Code's report lists it as untouched). The metadata lines "the Diploma Course in Modern Applied Psychology, DiMAP" in the entities lists of the instructor articles and book notes are field text, not body copy, and were not changed.

| Record | Type | Gate before | Gate after |
|---|---|---|---|
| a-diagnosis-actually-describing.md | instructor-article | PASS (RE 62.8) | PASS (RE 62.8) |
| a-false-epidemic-happen-without-anyone-lying.md | instructor-article | PASS (RE 61.9) | PASS (RE 61.9) |
| a-psychiatric-diagnosis-simply-wrong.md | instructor-article | PASS (RE 62.4) | PASS (RE 62.4) |
| blood-test-for-depression.md | instructor-article | PASS (RE 64.4) | PASS (RE 64.4) |
| bmi-decide-who-gets-eating-disorder-treatment.md | instructor-article | PASS (RE 69.7) | PASS (RE 69.7) |
| diagnosis-be-scientifically-weak-but-still-useful.md | instructor-article | PASS (RE 67.0) | PASS (RE 67.0) |
| diagnostic-inflation-actually-happening.md | instructor-article | PASS (RE 60.6) | PASS (RE 60.6) |
| doctors-have-only-minutes-to-diagnose.md | instructor-article | FAIL (RE 65.2) | FAIL (RE 65.2) |
| does-a-diagnosis-do-to-the-person.md | instructor-article | FAIL (RE 65.6) | FAIL (RE 65.6) |
| everyone-agreeing-on-a-diagnosis.md | instructor-article | PASS (RE 66.0) | PASS (RE 66.0) |
| five-symptoms-mean-depression.md | instructor-article | PASS (RE 64.5) | PASS (RE 64.5) |
| homosexuality-was-a-diagnosis.md | instructor-article | PASS (RE 62.0) | PASS (RE 62.0) |
| hypomania-from-an-ordinary-mood-swing.md | instructor-article | PASS (RE 60.6) | PASS (RE 60.6) |
| is-my-grief-normal.md | instructor-article | PASS (RE 67.0) | PASS (RE 67.0) |
| mental-disorders-tripled-since-the-1950s.md | instructor-article | PASS (RE 61.7) | PASS (RE 61.7) |
| multiple-personality-diagnoses-spike-after-a-film.md | instructor-article | PASS (RE 60.8) | PASS (RE 60.8) |
| self-report-decide-a-diagnosis.md | instructor-article | PASS (RE 62.7) | PASS (RE 62.7) |
| the-definition-of-mental-disorder.md | instructor-article | PASS (RE 61.6) | PASS (RE 61.6) |
| the-dsm-5-cost-five-times-more.md | instructor-article | PASS (RE 62.7) | PASS (RE 62.7) |
| the-rise-in-autism-diagnoses-real.md | instructor-article | PASS (RE 62.3) | PASS (RE 62.3) |
| what-is-concept-creep.md | instructor-article | PASS (RE 69.0) | PASS (RE 69.0) |
| what-is-stepped-care.md | instructor-article | PASS (RE 63.8) | PASS (RE 63.8) |
| the-open-society-and-its-enemies.md | book-note | FAIL (RE 60.4) | FAIL (RE 60.4) |

Three records failed their gate before my edit, for reasons my edit did not touch, and fail the same way after: doctors-have-only-minutes-to-diagnose ("actually" twice), does-a-diagnosis-do-to-the-person (opening paragraph five sentences), the-open-society-and-its-enemies ("truly" in the machine-tells check, and "actually" twice). Left as found, because the brief says change nothing else; Chat to say whether a fix is wanted.

## Edits 2, 3 and the schools count (five help-answer records)

| Record | Gate before | Gate after | Words after |
|---|---|---|---|
| HELP__best-hypnotherapy-course-and-who-accredits-it.md | PASS (RE 62.0) | PASS (RE 64.2) | 729 |
| HELP__call-yourself-a-clinical-hypnotherapist.md | PASS (RE 60.8) | PASS (RE 61.9) | 642 |
| HELP__become-a-psychologist-online.md | PASS (RE 60.1) | PASS (RE 60.2) | 803 |
| HELP__want-to-learn-psychology-where-to-start.md | PASS (RE 60.7) | PASS (RE 60.9) | 765 |
| HELP__learn-psychology-on-your-own.md | PASS (RE 60.1) | PASS (RE 60.0) | 784 |

**Edit 2, Mindvalley.** HELP__best-hypnotherapy-course-and-who-accredits-it: cut the Mindvalley bullet from the body, its claims-table row, its name in the entities line and in the Search and Citation Brief, and the "rests on one fetch" open point. The sourcing record keeps one line saying the line was cut and why. Other sections unchanged. Reading ease rose to 64.2.

**Edit 2, American Hypnosis Association.** HELP__call-yourself-a-clinical-hypnotherapist: cut the paragraph on the Hypnosis Motivation Institute's page about the American Hypnosis Association, its claims row, the two names in the entities line, its link in the planned links, and the open point. Two knock-on wording changes so the page still reads true: "A third view" became "Another view" and "one word with three meanings" became "one word with more than one meaning". The cut lowered keyword density to 0.94 percent (gate FAIL); I restored it by one natural change, "the clinical title" became "the title clinical hypnotherapist" in the HypnoTC sentence. No filler line was needed; reading ease is 61.9.

**Edit 3, become a psychologist online.** The warmed body, the full diploma name with its link at first mention, and everything else were kept. Only the line in "Where does the diploma fit in?" changed. Old: titles such as psychologist tell the public a person has accredited clinical training and registration. New: "Achology's courses give no clinical training, supervised practice or registration. In the United Kingdom, the HCPC says registration is what allows someone to use one of its nine protected titles, so Achology never urges anyone to use them." The Health and Care Professions Council page was read live this session (hcpc-uk.org, understanding the regulation of psychologists): "The job title 'psychologist', is not, by itself, protected by law", nine titles listed, and anyone using one "must be on our Register" (the fetch tool summarises, so the quote is as returned). The claims-table row and the sourcing-record line were changed to match. Note for Chat: the Achology-own half rests on the live Help answer on calling yourself a therapist, as before.

**Edit 4.** SESCO Management Consultants left exactly as it stands. No file needed a change for it.

## The seven schools count check (17 psychology HELP records written today)

I scanned the body of every psychology answer written today (the five seven-schools answers, the other four where-can-you-study answers, and the other psychology answers) for a stated count of schools. Found and removed, in two records:

- HELP__want-to-learn-psychology-where-to-start, four places: "each of the six below", "the six schools, one section each", "each of the six schools above", and "the seven primary schools of psychological thought" (a lowercase count). Now "the schools below", "the schools, one section each", "each of the schools above", and the lecture named by its title, The 7 Primary Schools of Psychological Thought, which is a title. The list itself still shows its six schools; no count is stated.
- HELP__learn-psychology-on-your-own: "six sections follow, one for each school" became "a section follows for each school". The lesson title stays.

Kept as a title: HELP__best-online-psychology-course names the lecture The 7 Primary Schools of Psychological Thought (a title, no count). Other numbers found were not school counts (six-week course, six modules in a developmental course, degrees). The claims-table rows and sourcing notes on these two records were reworded to match the body.
No record about become-a-psychologist-online, learn-psychology-for-free-online or where-can-you-study-behavioural-psychology-online stated a count.

## Lines I could not change

None. One limit: the fetch tool summarises pages, so the HCPC quote is as returned.

## Housekeeping

FROM Cowork/_tmp/warm.md: not deleted. The folder does not permit deletion (rm returned "Operation not permitted"), and I did not ask for delete permission. It is still there for Kain or Code to remove.

STATUS: Four decided edits made. 23 records for edit 1, 2 for edit 2, 1 for edit 3, 2 for the schools count. Gate after: all pass except three pre-existing failures named above. No em or en dashes.
