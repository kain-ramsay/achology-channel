# REPORT: the course master is split, the CSVs are the master, the xlsx is retired

> **DISPOSITION, S283:** ACTED ON AND CLOSED. Chat read this in full. Its counts (28 sheets, 2,146 rows, 124 sections, zero column variance, Vimeo columns empty on every row) are carried into the S283 handover and into the follow-on commissions. Its two findings for Kain are recorded and still open: course 021's name differing in meaning between the workbook and DSRD 5, and the 115-lecture gap against DSRD 5, which the Drive map has since mostly explained. **Board cards moved:** none by this file alone; the Vimeo Course Refresh and Course curriculum data cards were updated in the same session for the ruling this report executes. Archived S283.

**DOCUMENT TYPE:** report. Not a page spec. **From:** Claude Code, Session 64. **Date:** 18 August 2026.
**Closes:** `COMMISSION__Convert_The_Course_Lesson_Master_To_CSV_So_Every_Environment_Can_Read_It_S283.md`, in its final form.
**Board card:** the course and lesson data card behind the Vimeo upload, the course and school pages, the twenty eight handbooks and the transcript pipeline.

**One thing about the run, said first because it matters to how you write to me.** That commission was rewritten twice while I was executing it. I built the first version (a derived copy in a subfolder), the H6 channel hook blocked my next write and made me re-read, and the file had become the split-and-retire ruling. I started that, and H6 blocked me again: it had changed a second time, growing the Section Order and Lesson Key columns. **Both catches were the hook doing exactly its job and nothing was built to a stale instruction.** No complaint attached, and nothing is owed back. It is worth your knowing only because the third version is the one that ran, and because two versions of that file exist in my transcript and neither is the one on disk.

---

## What was done

**Six steps, all of them.** Twenty eight CSVs written into the `Course + Lesson Data | MASTER` folder itself. Every source column carried through untouched. Seven columns appended, two filled and five empty. The xlsx retired into `Archive`. `Course_Lesson_Master__Read_Me_First.md` rewritten from nothing.

**The xlsx was opened read-only and never written to.** It was fingerprinted before the run and again after the move: `358d5eb6a06232083456df82fb69fbe9` both times. It sits in `Archive` as `Achology Courses Structure and Lesson Descriptions COMPLETE RETIRED S283.xlsx`, byte for byte the file Karen sent.

**No re-export script exists and that is deliberate.** The conversion ran from a one-off in scratch space and was not filed beside the data. Under your own ruling the CSVs are now the master, so a re-export script in that folder would be a loaded gun: running it once after anything had been written into the appended columns would wipe that work without a word. The Read Me First says so in as many words, so nobody writes one back later on the reasonable-looking grounds that a folder ought to be reproducible.

---

## The counts you asked for

**Sheets found: 28. CSVs written: 28.** One per sheet, none missing, none extra.

**The exact column list found in the source sheets, in order, before anything was appended:**

    Section | Lesson Number | Lesson Name | Lesson Description | Vimeo URL | Vimeo Video ID

**Sheets whose columns differ from the others: none.** All 28 carry those six, in that order, with identical spelling. The layout is identical too: a blank row, the course title in column A, a blank row, then the header starting in column B. I found the header row rather than assuming its position, so an odd sheet would have stopped the run instead of producing a quietly wrong file.

**Vimeo URL and Vimeo Video ID are still empty on every row.** Zero of 2,146 on both. The Read Me First was right about that even though its other numbers were stale.

### Rows and sections per course

**2,146 lesson rows across 124 sections.** The row total agrees exactly with the figure the old Read Me First carried, which is the one number in it that survived.

| Sheet | Course | Rows | Sections |
|---|---|---|---|
| 001 | Diploma Course in Modern Applied Psychology (DiMAP) | 175 | 8 |
| 002 | A Beginner's Guide to Neuro-Linguistic Programming (NLP) | 40 | 3 |
| 003 | Neuro-Linguistic Programming (NLP) Practitioner Training | 155 | 12 |
| 004 | Neuro-Linguistic Programming Master Practitioner Course | 154 | 8 |
| 005 | Mindset Mastery: The Ultimate NLP-Based Guide to Self-Discovery | 41 | 3 |
| 006 | The CBT Toolkit: Core Principles and Real-World Applications | 46 | 3 |
| 007 | Cognitive Behavioural Therapy (CBT) Practitioner Course | 119 | 7 |
| 008 | Cognitive Behavioural Therapy for Mental Health and Wellness | 52 | 3 |
| 009 | Life Coaching Certificate Course (Beginner to Advanced) | 122 | 7 |
| 010 | Life Coaching Blueprint: The Complete Process and Practices | 134 | 8 |
| 011 | The Skilled Helper Training Course (with Prof. Gerard Egan) | 28 | 2 |
| 012 | Skilled Helper Practitioner Course (Advanced to Expert) | 51 | 1 |
| 013 | Hypnotherapy Practitioner Course (Beginner to Advanced) | 118 | 8 |
| 014 | Counselling Skills Practitioner Course (Beginner to Advanced) | 176 | 7 |
| 015 | Mindfulness Practitioner Diploma Course (Beginner to Expert) | 124 | 5 |
| 016 | Mindfulness for Mental Health, Personal Growth and Inner Peace | 52 | 3 |
| 017 | Mindfulness for Highly Efficient Management and Leadership | 47 | 3 |
| 018 | Mental Health and Wellbeing Practitioner Diploma Course | 130 | 7 |
| 019 | The Self-Belief, Emotional Intelligence and Assertiveness Masterclass | 42 | 3 |
| 020 | Authentic Confidence, Core Identity and Self-Esteem Masterclass | 45 | 3 |
| 021 | Master Your Emotional IQ and Revolutionise Your Social Skills | 43 | 3 |
| 022 | The Clarity, Purpose and Personal Effectiveness Masterclass | 31 | 2 |
| 023 | The Strategic Goal Setting and Action Planning Masterclass | 28 | 3 |
| 024 | The Communication Skills and Social Intelligence Masterclass | 49 | 3 |
| 025 | The Hyper-Focus, Self-Discipline and Productivity Masterclass | 35 | 2 |
| 026 | The Complete Mental Toughness and Inner Resilience Masterclass | 36 | 3 |
| 027 | An Essential Guide to Healthy Marriage and Long-Term Relationships | 23 | 1 |
| 028 | An Entrepreneurs' Guide to Launching and Growing a New Business | 50 | 3 |
| | **TOTAL** | **2,146** | **124** |

**One thing to notice in that table before it is used downstream.** These row counts are lessons in the workbook, and they are not the lecture counts DSRD 5 section 1 carries. Course 001 reads 175 here and 179 in DSRD 5, and the same gap exists across the catalogue: 2,146 here against DSRD 5's 2,261 total. DSRD 5 says its lecture figures came from the Udemy instructor dashboard, so the two are probably counting different things rather than disagreeing. **I have not reconciled them and I am not proposing to.** It is named because the difference is 115 and somebody will otherwise meet it as a surprise.

### The two columns I filled

**Section Order.** Derived from the physical row order exactly as found, 1 upward, restarting per course. Nothing else was touched to produce it.

**Lesson Key.** 2,144 of the 2,146 rows carry one, and **all 2,144 are unique, not merely within a course but across the whole set of 28 files.** Zero duplicates.

**One detail of the form, decided rather than asked about, so you can check it.** Your spec says a two-digit Lesson Number. Four courses run past ninety nine lessons (001, 003, 004, 014), so those keys carry three digits: `001-S08-L175`. Two digits is the minimum rather than the width, which is what keeps every key unique. If you want a fixed three-digit field on every key instead, say so and it is a two-minute rewrite across all 28 files.

### The exceptions you asked to have reported rather than resolved

**Duplicate Lesson Keys: none.**

**Blank or non-numeric Lesson Number: none.** Every one of the 2,146 rows carries a numeric lesson number, and all 28 courses number 1 to N with no gaps and no duplicates.

**Rows carrying no section at all: two, both in course 012.** Rows 47 and 49, `The 'Cosmina' Session: Setting Priorities & Ac...` and `The Common Problems that Accompany Setting Go...`. Their Section cell is blank in the source.

**They are the only two rows in the whole set without a Lesson Key**, because a key needs a Section Order and a Section Order needs a section. Course 012 has exactly one section, so on the face of it both rows belong to it and to nothing else, and filling them would look harmless. **I have not filled them.** That is an inference about somebody's data, the commission says report rather than resolve, and two blank cells that are visible are worth more than two guesses that are not. Say the word and both take `012-S01-L47` and `012-S01-L49`.

---

## Anything in the file nobody asked about

**One. The sheets do carry course names, and twelve of them disagree with DSRD 5.** Your commission says "the sheets carry no course names", inherited from the old Read Me First. They do: each sheet's row 2 holds its number and a course name. Twelve are shortened, abbreviated or punctuated differently from the canonical name in DSRD 5 section 1:

| Sheet | The workbook says | DSRD 5 says |
|---|---|---|
| 002 | A Beginners Guide to Neuro-Linguistic Programming (NLP) | A Beginner's Guide to Neuro-Linguistic Programming (NLP) |
| 005 | Mindset Mastery: The Ultimate NLP Guide to Self-Discovery | Mindset Mastery: The Ultimate NLP-Based Guide to Self-Discovery |
| 015 | Mindfulness Practitioner Diploma (Beginner to Expert) | Mindfulness Practitioner Diploma Course (Beginner to Expert) |
| 016 | Mindfulness for Mental Health, Personal Growth & Inner Peace | Mindfulness for Mental Health, Personal Growth and Inner Peace |
| 019 | The Self-Belief, Emotional IQ and Assertiveness Masterclass | The Self-Belief, Emotional Intelligence and Assertiveness Masterclass |
| 021 | Master Your Emotions and Revolutionise Your Social Skills | Master Your Emotional IQ and Revolutionise Your Social Skills |
| 022 | Clarity, Purpose and Personal Effectiveness Masterclass | The Clarity, Purpose and Personal Effectiveness Masterclass |
| 024 | Communication Skills and Social Intelligence Masterclass | The Communication Skills and Social Intelligence Masterclass |
| 025 | Hyper-Focus, Self-Discipline and Productivity Masterclass | The Hyper-Focus, Self-Discipline and Productivity Masterclass |
| 026 | The Mental Toughness and Inner Resilience Masterclass | The Complete Mental Toughness and Inner Resilience Masterclass |
| 027 | A Guide to Healthy Marriage and Long-Term Relationships | An Essential Guide to Healthy Marriage and Long-Term Relationships |
| 028 | An Entrepreneurs' Guide to Launching & Growing a Business | An Entrepreneurs' Guide to Launching and Growing a New Business |

**The filenames follow DSRD 5, not the workbook**, per your step 2. The workbook's own titles were not carried into the CSVs at all, since they are not a column. This matters mainly for 021, where the two names differ in meaning rather than in punctuation: "Master Your Emotions" against "Master Your Emotional IQ".

**Two. Lesson Description is filled on all 2,146 rows.** No blanks anywhere. Whatever else the standardisation pass finds, it is not working around gaps.

**Three. The descriptions carry internal line breaks**, typically a title line, a blank line, then several paragraphs. They survive in the CSVs as line breaks inside quoted fields, which is correct CSV and is what any proper reader will expect, but a naive line-counting script will read 2,146 rows as tens of thousands of lines. Worth knowing before somebody writes one. The longest description is over 1,500 characters.

**Four. Two of the six source columns were already dead weight** and now sit alongside five deliberately empty ones, so eleven of thirteen columns are empty on every row. That is the intended shape rather than a fault, but it means anyone opening one of these files for the first time sees mostly blank space and should be told why. The Read Me First says why.

---

## Verification

The 28 files were read back after writing, not assumed. All 28 parse as CSV, all carry the identical thirteen-column header, every one of the 2,146 rows has exactly thirteen fields, the row total reads back at 2,146, the key set reads back at 2,144 unique with zero collisions, and a spot-checked description came back with its line breaks and its full 1,535 characters intact.

The folder map generator was run afterwards, so this folder's own `000__WHAT_IS_IN_HERE.md` reflects the new contents.

## What was not done, per your file

No description was standardised or altered in any way. No Vimeo work of any kind. No Circle ID recovery: those two columns are empty. Nothing was deleted.

*No em or en dashes in this file; checked before writing.*
