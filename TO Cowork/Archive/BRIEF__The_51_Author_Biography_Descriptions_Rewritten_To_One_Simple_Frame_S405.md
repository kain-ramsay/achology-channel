# BRIEF: the 51 author biography descriptions, rewritten to one simple frame (S405)

**From Chat, S405, on Kain's word in session: "commission Cowork with this right now, please".** Run it end to end, then hold.

## Why

Kain found that the author biographies' search descriptions (the `rm_seo_description` field, the line under the title in Google and on the page) tie real people to Achology. Taleb's reads "Explore his life, his major works, and his influence on Achology." Taleb has no link to Achology, and the line tells a reader he does. That is a false claim of association, and the PRD bars overclaiming at launch. Kain also found the lines hard to read. The site is not launched, so no reader has seen them.

## The frame (ruled by Kain, S405)

Two sentences. The first says plainly who the person is. The second is fixed, word for word.

> {Name} is {who they are, in plain words}. Read about {his/her/their} life, {his/her/their} big ideas and the books {he/she/they} wrote.

Kain's approved example, for Taleb:

> Nassim Nicholas Taleb is a former options trader who writes about risk and uncertainty. Read about his life, his big ideas and the books he wrote.

**How to fill the first sentence.**
- The full name exactly as `subject_name` holds it, first.
- "is" for a living person, "was" for one who has died (the fixed sentence then reads "the books he wrote" either way).
- Who they are in plain words a thirteen-year-old understands: what they did, not praise. Read it from the record's own body, never from memory. Every word must be true of that person.
- Never the word Achology, and never any line that ties the person to Achology, its courses or its teaching. This holds for Kain Ramsay and Gerard Egan too (Kain, S405: he would rather Achology was not in these lines).
- No praise words (great, leading, renowned, legendary), no dashes, UK spelling.
- The whole description at most 155 characters including spaces. If a first sentence makes it longer, shorten the first sentence, never the fixed one.
- No two descriptions alike: only the first sentence changes, so make each one about that person.

## The job

1. **The 51 biographies** in `Content Records/author-biography/` (the `_scratch_peterson.md` file is not a record; leave it). For each, replace only the `rm_seo_description` value with the new line. Change nothing else in the record.
2. **A sweep of every other record** in `Content Records` (every folder) for any line that ties a named real person to Achology: "influence on Achology", "taught at Achology", "Achology's approach owes", and anything like it, in any field or the body. **List them; do not change them.** Kain Ramsay and Gerard Egan, who do teach at Achology, are listed only where a line claims more than is true.
3. **Run the gate** on each of the 51 and paste any FAIL on the description line.

## What comes back, in one DONE file in FROM Cowork

- A table of all 51: name, the old description, the new one, its character count.
- The sweep list from step 2: file, field or paragraph, the line, why it is listed.
- Anything you could not do, and why.

Kain signs the 51 from your table. Then Code pushes the field to the build site. Code's push waits on Kain's signature.

## Boundaries

Never open the master file. Change only the one field in the 51 records. Write only into `Content Records/author-biography/` and FROM Cowork. Read the Content Standard (Version 8) Part 2 first; where it and this brief disagree, tell Chat in the DONE rather than choose.

*No em or en dashes in this file; checked before writing.*
