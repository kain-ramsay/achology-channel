# THE COURSE TAGGING MECHANISM, in full. And my S252 ruling is withdrawn.

**Written S252 by Claude Chat. Date: 2026-08-07.**
**Supersedes `RULING__Article_Shows_Its_Category_School_Courses_S252.md` in full. That ruling was wrong. Do not build to it.**
**Replaces the stand-in in `achology_course_companions()` in `courses-setup.php`.**

## Read this first

You could not find a tag rule for courses and built a stand-in that picks the nearest course by school, and you flagged it. **That was the right thing to do and the gap was real from where you were standing.**

It was not real, though. **The full tag-to-course mapping has been in DSRD 1 §5 since the taxonomy was written**, and neither of us went and read it. I then compounded it: I ruled an article should show its category's school courses, which is a different mechanism, invented on the spot, while the settled one sat in the canonical file. Two of us derived an answer the system had already given.

That is the same fault as the settings.json miss and the same fault as a green test that could not fail. It is the vault principle *A Question The System Has Already Answered Is Retrieved, Never Re-Derived*, and today it cost a live page a wrong mechanism.

**My ruling is withdrawn. Build to what follows.**

## The mechanism, whole

### 1. What the tags are

**36 tags at launch, in four groups.** They are visitor-facing language, not curriculum language: what a reader searches for, not what a syllabus promises. That was the deliberate design decision, so tag pages rank and read naturally while still driving the recommendation engine underneath.

| Group | Count | Maps to courses? |
|---|---|---|
| Outcome | 16 | **Yes** |
| Problem | 9 | **Yes** |
| Modality | 6 | **Yes** |
| Content attribute | 5 | **No** |

**Content attribute tags never map to courses.** Research-Based, Practical Exercise, Deep Dive, Beginner-Friendly, Professional Practice describe the piece, not the reader's goal. They are ignored entirely by the recommendation.

### 2. Where they live

**DSRD 1 §5, the canonical file.** Read it there rather than from this note.

- §5.1 governance rules
- §5.2 the 16 outcome tags, each with its mapped courses
- §5.3 the 9 problem tags, each with its mapped courses
- §5.4 the 5 content attribute tags, descriptions only, no course column
- §5.5 the 6 modality tags, each with its mapped courses
- §5.6 the 36 slugs, locked S247, the addresses the tag pages are built at

**One thing that will trip you if you parse those tables literally.** §5.2, §5.3 and §5.5 use abbreviated course names for readability, and DSRD 1 says so explicitly at the head of §5: "DiMAP" for the full Diploma Course in Modern Applied Psychology, "CBT for Mental Health" for the full title, and so on. **This is a named exemption from the product-name rule, applying only to these mapping tables. DSRD 5 is the source of truth for full canonical names.** So the mapping resolves through DSRD 5, never by treating the abbreviation as the name.

### 3. How a course carries them

**It does not.** This is the part the stand-in got backwards, and it is worth stating plainly.

**The tag maps to courses. The content carries tags. A course carries nothing.** There is no tag field on a course. The relationship lives in the tag, in one table, in DSRD 1 §5, and is read from there.

That is why no amount of looking at a course told you anything: courses are the destination, not the origin.

### 4. How a piece of content carries them

Each piece gets **two to four outcome or problem tags maximum**. Content attribute and modality tags are additional and not counted in that limit.

**Tags are assigned at production and travel in the upload CSV**, never applied afterwards by hand. With 620 book notes and thousands of quotes, retro-tagging is not a plan.

### 5. How a page picks its courses

```
the page's tags
  -> drop every content attribute tag
  -> for each remaining tag, take its mapped courses from DSRD 1 section 5
  -> resolve each abbreviated name to its canonical course via DSRD 5
  -> the courses that appear most often across the page's tags rank highest
  -> show the top N
```

**N is not the same everywhere:**

| Block | Where | How many |
|---|---|---|
| Explore Related Learning Paths | Every Knowledge Hub content type | **2 courses** |
| Mapped Courses Callout | Tag landing pages | **up to 3 courses** |

Both are named in DSRD 1's own block table, and DSRD 2 names the two-course block at §1.5 item 10 and §1.6 item 11.

**On the Book Note page specifically:** DSRD 9 §32.1 item 6 was amended this session to three cards at desktop and two below. That is the tier rule for how many cards are *displayed*; this is the rule for *which courses* fill them. Where the two disagree on count, DSRD 9 §32.1 governs the Book Note page and DSRD 1 governs everywhere else, and I will reconcile them once you tell me what the resolved mapping actually yields.

### 6. What to do about the ties

The rank rule above will produce ties, often. **Do not invent a tiebreak.** Report what you find: how many pages resolve to a clean top two, how many tie, and what the tie looks like. Kain rules the tiebreak once, on real numbers, rather than either of us guessing at it now.

## What I need back from you

**Explain the mechanism back to me in your own words before you build it**, including what a course carries (nothing) and what happens to a content attribute tag (nothing). If any part of it does not land, say which part.

Then, before writing code, **report three things:**

1. Whether the 36 tags exist as real terms in WordPress, or only as a table in DSRD 1
2. Whether the content actually carries tags yet, and if so on how many rows of the Book Note master
3. What the mapping yields on the one live book note, so the first render can be checked against the table by hand

**If the tags are not in the database yet, the mechanism cannot run and the correct answer is to say so and stop**, not to build a second stand-in. That is what you did the first time and it was right.

## Do not ask Kain any of this

The mechanism is settled and written down. Anything that reads as missing comes to me, and I go and find it in the record, as I should have done tonight.

*No em or en dashes in this file; checked before writing.*
