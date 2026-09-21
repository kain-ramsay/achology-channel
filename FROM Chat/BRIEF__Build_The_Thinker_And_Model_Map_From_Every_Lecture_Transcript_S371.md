# BRIEF: Build the thinker and model map from every lecture transcript

**From:** Claude Chat, Session 371, Monday 21 September 2026. **To:** Claude Code. **Approved by Kain in session, S371.**
**Kind:** a commission, factory session. It builds one data file. It publishes nothing, imports nothing, and touches no theme file and no page.
**Order (Chat's call, Kain can overturn it):** after items 1 and 2 of the S370 push list (the gate check and the 216 help answers), because nothing publishes from this file yet and those two are waiting on you now.

## Why this exists

At S371 Kain approved a new kind of help answer: "Where can I learn about Carl Rogers?". It says briefly who the thinker was, from his own books, then names which Achology courses teach him and which to start with. The approved exemplar is in the help-answer folder inside Content Records: `HELP__where-can-i-learn-about-carl-rogers.md`. Kain ruled that shape for every thinker and every named model he teaches.

Chat sized it from lesson titles alone: about 50 thinkers and about 100 named models across the 2,146 lessons. Titles undercount, because many thinkers and models are named inside a lecture and not in its title. Chat has no tool that searches a whole folder on Kain's machine. You do. The map you build is the single source every one of those answers will be written from, and later the course pages' "thinkers and models you will meet" block, the links out of book notes, biographies and quote pages, and the index of the Achology wiki.

## What to build

One CSV, beside the lesson index in the Course and Lesson Data MASTER folder, named `THINKER_AND_MODEL_MAP__All_Transcripts_S371.csv`, with a short README line added to that folder's own README saying what it is and how it was built.

One row per thinker or model, per lesson that teaches it. Columns, in this order:

1. `entity` : the thinker's full name, or the model's usual name, one spelling per entity throughout (Viktor Frankl, never Victor Frankel; The Johari Window, never Johari's Window).
2. `entity_type` : thinker, or model.
3. `belongs_to` : for a model, the thinker it belongs to where the lecture says so (The Skilled Helper Model belongs to Gerard Egan); blank otherwise.
4. `lesson_key` : as in the lesson index.
5. `course_number`.
6. `lesson_name` : copied from the lesson index.
7. `depth` : taught, where the lesson is about the entity or gives it a sustained passage; mentioned, where it is named in passing.
8. `in_title` : yes or no.
9. `mention_count` : how many times the entity is named in that transcript.
10. `evidence` : one short line from the transcript showing the entity being taught, under 25 words, copied exactly.

Then a second, small CSV beside it, `THINKER_AND_MODEL_MAP__Summary_S371.csv`: one row per entity, with entity, entity_type, lessons_taught, lessons_mentioned, courses_taught (the course numbers, separated by a semicolon), and total_mentions, sorted by lessons_taught, highest first.

## How to find them

Source: the corrected transcripts in the transcripts folder of the Vimeo exports, one folder per course, files ending `.corrected.txt`, with the lesson index `LESSON_INDEX__Twenty_Eight_Courses_S351.csv` as the key.

Two passes, because a fixed list alone misses what nobody thought to list.

**Pass one, the seed list.** Search every transcript for these, with their common misspellings and speech-to-text variants: Carl Rogers, Albert Ellis, Gerard Egan (also Gerry Egan), Viktor Frankl, Abraham Maslow, Sigmund Freud, Carl Jung, Alfred Adler, Erik Erikson, Milton Erickson, Virginia Satir, Fritz Perls, Richard Bandler, John Grinder, Aaron Beck, B. F. Skinner, Ivan Pavlov, Jean Piaget, Lawrence Kohlberg, John Bowlby, Erich Fromm, Soren Kierkegaard, Aristotle, Plato, Socrates, Epictetus, Stephen Karpman, Eric Berne, Joseph Luft and Harry Ingham, Stephen Covey, Daniel Goleman, Daniel Kahneman, William Glasser, Elisabeth Kubler-Ross, Alfred Korzybski, Noam Chomsky, Shalom Schwartz, Hans Eysenck, Ulric Neisser, Stanley Milgram, Larry Crabb, Robert Dilts, Gregory Bateson, Bruce Bracken, Benjamin Bloom, Arnold Lazarus. Models: The Johari Window, The Drama Triangle, Maslow's Hierarchy of Needs, The Skilled Helper Model, the ABC model, the three core conditions, the nineteen propositions, the fully functioning person, The Meta Model, The Milton Model, the Iceberg Model, Choice Theory, The Pygmalion Effect, The Eisenhower Matrix, The Human Givens Framework, the GROW model, SOLER, SMART goals, the Wheel of Life, Transactional Analysis, the Cultural Iceberg, Logotherapy, the Eight Stages of Development, cognitive distortions, the Wise Mind model, the Core Identity Model, the Desired State Model, Parts Integration.

**Pass two, discovery.** Find what the seed list missed: every capitalised personal name that appears in three or more lessons, and every phrase ending Model, Theory, Triangle, Window, Hierarchy, Wheel, Cycle, Framework, Matrix, Ladder, Effect, Principle or Technique that appears in two or more lessons. Drop Kain, Karen, guests, students, the people in his stories, celebrities used as examples, and place names. Where you cannot tell whether a name is a thinker or a story, keep it and put a question mark at the end of `entity_type`; Chat will rule on those rows.

Achology's own models (the Core Identity Model and any other Kain built) stay in the map, marked with `belongs_to` Kain Ramsay.

## What done looks like

- Both CSVs exist where named, open cleanly, and every `lesson_key` in them is a real key in the lesson index.
- Every one of the 2,146 lessons was searched; the README line states the number of transcript files read, and names any lesson with no transcript file.
- Carl Rogers comes back with at least the ten lessons Chat found from titles: 001-125, 001-126, 001-128, 001-129, 001-130, 001-131, 004-073, 005-032, 014-016, 024-010. If any is missing, the search is wrong, not the list.
- One spelling per entity, checked by sorting the summary and reading it top to bottom.
- A short report in TO Chat: the two file names, the count of thinkers and of models, the twenty with the most lessons taught, the question-mark rows, and anything that surprised you.

## What this brief does not ask for

No help answers are drafted. No page, template, schema or import is touched. No DSRD is edited. Nothing is sent to Cowork. If something here cannot be built as written, stop and ask through the channel; do not fill the gap with judgement.

*No em or en dashes in this file; checked before writing.*
