# Brief for Chat — how I propose to store and display the student reviews

From: Claude Code · 2026-07-23 · Kain asked me to brief you before I build.
Card: "Confirm Reviews & Testimonials Content-Type ACF + Reconcile the Full
Content-Type Inventory."

## The data, verified today (not from memory)

Kain zipped the two CSVs in `007 …/Udemy Student Reviews/` so I could read them
(the originals are iCloud placeholder stubs). Actual figures:

| File | Rows | What it is |
|---|---|---|
| Udemy Reviews since 2014 Export (FULL) | **181,989** | the raw firehose, 5 columns |
| Distilled Notion Reviews File (IN NOTION) | **4,517** | the curated set, 13 columns |

The distilled file is the working set and appears to be the Notion Review Bank
in CSV form. It carries: Review Text, Course #, Course Name, Primary School,
All Schools, Star Rating, Student Name, Review Date, Word Count, Tier,
Featured, Website Published, Notes.

Its state: **all 28 courses and all 7 schools covered**; pre-filtered to 3
stars and up; Tier splits **4,060 Displayable / 457 Insight**; word counts 10
to 752, median 36.

**Both "Featured" and "Website Published" are blank on all 4,517 rows** — the
filtering was done, the final publish selection never was.

## What is already specced (so we don't reinvent it)

- **DSRD 1** defines two separate pages: `/reviews/` (verified student reviews
  library) and `/testimonials/` (video testimonials). They are not the same page.
- **DSRD 4 §14.2** already defines the Social Proof Component System: six
  variants across eleven page types, including course-specific proof on all 28
  course pages.
- **DSRD 4 §14 and DSRD 5** both name the **Notion Review Bank as the single
  source of truth** for review text and social proof data.
- **DSRD 4 §14** rule: star ratings use Udemy's displayed recency-weighted
  figures, never raw CSV averages, and social proof uses cumulative totals only.

## The distinction that makes this simple

**Numbers and text are two different problems.** The star ratings, review
counts and student counts are product facts already held in DSRD 5 and must
keep coming from there. They are not computed from this CSV. Only the **review
text we display** needs a home. That is all this build decides.

## What I propose to build

A `review` custom post type with an ACF group in Local JSON, exactly the same
pattern as `faq_article` and the four Knowledge Hub types:

- Fields: reviewer name, star rating, review date, review text, source course
  (post object), primary school, tier, featured flag.
- Imported once from the distilled CSV, each review linked to its course.
- `/reviews/` becomes an archive query; the course-page and school-page blocks
  are the same query filtered by course or school.
- No runtime dependency on Notion, editable by Kain in WP admin, ACF
  version-controlled in the theme.

**Kain's decision today on selection:** publish all 4,060 Displayable, let each
course page surface its own best few automatically (by rating and length), and
reserve "Featured" for the handful he hand-picks for the homepage or the
`/reviews/` hero. He does not want to hand-curate 4,000 rows.

## What I need from you

1. **Does the Notion Review Bank match this 4,517-row distilled file?** You may
   have sight of the bank and its history; I only have the CSV export dated
   23 March. If the bank has moved on, the CSV is stale and I should import
   from the current bank instead.
2. **Any prior decisions from earlier sessions I should honour?** Kain recalls
   discussing reviews "a long time ago" and is unsure what was settled. If
   there are agreed rules on display counts, attribution format (full name vs
   first name and initial), or anything about GDPR on publishing student names,
   they should govern this build.
3. **One data flag for the page work:** "Mindset Mastery: The Ultimate
   NLP-Based Guide to Self-Discovery" has only **3** reviews; a few others sit
   at 40 to 73, while the largest are capped at 250. That one course's block
   will look sparse whatever we do, so the component needs a graceful low-count
   state.

Nothing here ships until Kain approves. I am speccing the CPT and ACF now; the
display components are page work and stay with the page-template card.
