# REPORT: five held back courses of descriptions, and what their source rows get wrong

**DOCUMENT TYPE:** report, from Claude Code, Session 072. **Date:** 19 August 2026.
**Answers:** `COMMISSION__Write_The_Standardised_Descriptions_To_Shape_C_S288`, per course reporting.
**Reads with:** `RULING__The_Nine_Held_Back_Courses_Are_Released_S072.md`, beside this file.
**Board card:** the Vimeo course refresh.

---

## The numbers

| Course | Rows | Word range | Flagged |
|---|---|---|---|
| 012 Skilled Helper Practitioner | 51 | 90 to 106 | 6 |
| 008 CBT for Mental Health and Wellness | 52 | 90 to 103 | 6 |
| 007 CBT Practitioner | 119 | 90 to 112 | 9 |
| 013 Hypnotherapy Practitioner | 118 | 94 to 116 | 22 |
| 010 Life Coaching Blueprint | 134 | 90 to 119 | 27 |
| **Total** | **474** | | **70** |

Course 010's 134 includes lesson 094, the bonus clip, whose description was written at S071 and is carried here unchanged rather than rewritten.

**The library now reads 2,146 rows, 1,486 descriptions, 0 faults, 0 repeated question lines.** Every row is three parts, inside the 90 to 120 band with its answer inside 60 to 85, carries no Tier 1 term and no long dash. Karen's originals were checked unchanged before each write, and `desc_audit.py` re-runs every rule over all twenty eight CSVs rather than trusting the writer scripts.

**Twenty one of twenty eight courses are now written.** Four remain: 004, 003, 001 and 014, about 660 rows.

## The seventy flags, grouped by what somebody would actually have to do

**Thirty seven rows carry an original identical to their own part one**, word for word, with nothing in the text distinguishing the two videos. Each pair was written with two questions taking different angles on the single source, because inventing a second lecture's content is forbidden. Nobody needs to act on these unless real per part descriptions are wanted.

**Seven rows carry that same fault plus a part number line that contradicts itself**, reading part one on the second part: 008-009, 013-022, 010-047, 010-051, 010-068, 010-085 and 010-108. These are Karen's to correct, and they are visible to a student.

**Nine rows carry boilerplate that says nothing about the lesson at all.**
- **013-097, 099, 100, 101 and 104**, the five Cinzia focused conversations, share one paragraph between them. Each question is taken from that row's own title, so the five differ, and the five answers are necessarily close because the source is one paragraph reused five times. **This is the one worth a decision: five real conversations are being sold on one description.**
- **013-098 and 102**, the two Cinzia deconstructions, share a second boilerplate the same way.
- **007-070, 072 and 075** share a generic "observe a real CBT session" paragraph that never says which technique each demonstration covers.
- **010-045 and 124** say only that they are the next question in a series.

**One lecture description appears in five courses.** The recommended reads text is word for word identical on 005-041, 007-118, 008-051, 010-133, 012-051 and 013-117. Somebody should settle whether that is one lecture reused across six courses or six different recordings sharing one description, because the answer changes what the descriptions should say.

**One lecture appears in two courses.** 007-057 and 008-042 carry an identical original on the decisions of maturity and character. Same question.

**Nine genuine text faults in the source rows, each one Karen's to fix:**

| Row | Fault |
|---|---|
| 012-021 | says "the outcomes needed for **her**" where Matt is he throughout the rest of the row |
| 012-030 | "the insights **he** uncovered" where every other Sarah row says she |
| 012-048 | switches to he twice for Cosmina, who is she in its own opening sentence |
| 012-032 | the original stops mid sentence: "offering valuable in" |
| 013-009 | 008 and 009 both end mid sentence on a stray "A" |
| 013-103 | the lesson title reads "An Honest Evaluation of We've Achieved so Far", missing a word |
| 013-118 | states "more than 121 lessons" where the course CSV holds 118 rows |
| 010-125 | says "it's a series of nine" where this is question eleven |
| 007-116 | misspells Kain as "Kaiin" |

## The one finding that may be a mapping fault rather than a text fault

**Course 012's Sarah rows look shifted by one against their titles.**

- **012-028** is titled `The 'Sarah' Session: Exploring the Problem (Demo Part 1)` and its original describes the priorities and action steps stage, word for word as 013 and 021 describe their own part two.
- **012-029** is titled `Setting Priorities & Action Steps (Part 2)` and its original is the deconstruction text.
- **012-030** is titled `Demonstration Deconstruction` and its original is the deconstruction text as well.

Every other demonstration client in the course, Gaby, Matt, Alec and Cosmina, has its three originals aligned with its three titles. Sarah's do not. **This is the same shape as the course 010 offset that Kain ruled on at S071**, where the videos turned out to be the truth and fourteen names slid down one to meet them.

The descriptions were written from the originals, as the rule set requires, and they are flagged rather than corrected. **What settles it is the videos themselves**, so this is worth a look once 012 runs and its transcripts are banked, exactly as 010 was.

## What is not in this report

Nothing about the video run itself, which is in the session report. Nothing about the twelve repeated question lines, which is in the ruling beside this file.

*No em or en dashes in this file; checked before writing.*
