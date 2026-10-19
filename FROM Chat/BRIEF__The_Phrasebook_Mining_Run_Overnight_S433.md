CODE DISPOSITION, S175: WAITS ON a factory session (this was a theme session; the API worker run is factory work).
**Needs from Code (factory session, the API worker): run the Phrasebook mining tonight, overnight. Mine Kain's own usable sentences, analogies, questions and teaching paragraphs out of his 2,142 lessons and his books on Haiku 5.5, keep each with its source, and leave the results in a staging folder for Chat to read. Nothing goes into the vault until Chat has read the first 100 pieces.**

# BRIEF: the Phrasebook mining run (Chat, S433, 19 October 2026; Kain: "Yes, brief the Phrasebook run to Code tonight")

## Why
Kain ruled the Phrasebook at S432 as the sixth layer of the voice standard (SCOPE__The_Newsroom_Blueprint_S430, Part 8, in The Newsroom's 99 Working Papers folder). It is his own words kept as small usable pieces, filed by the idea each teaches, so a writer never invents what he has already said. His words: "you might as well use my actual content, the stuff I've been teaching for years." This is the first real run of the Chore lane, and it measures that lane's cost.

## Model, effort and money (MAP__Models_Effort_And_Lanes_S432, section 4, row "Phrasebook mining")
- Model `claude-haiku-5-5`, effort `low`, through the Message Batches API (half price). The shared instruction block is sent with prompt caching.
- **Cost cap: $10 for the whole run.** Stop and report if the measured spend passes it. The API account never goes below $25 (Kain, S432).
- Record the measured cost per million source words in the report. Kain sets future budgets from it.

## Sources (all inside the iCloud project folders, so iMac 4 can read them)
1. The lesson transcripts: `0001. Achology Website Upgrade 2026/07. All Achology Videos | Vimeo Exports/output/transcripts/`. Each lesson has a plain `.txt` and often a `.corrected.txt`. Use the corrected one where it exists, otherwise the plain one, and never both: that is 2,142 lessons, about 6.1 million words. Skip the lessons listed in `000__LESSONS_WITH_NO_SPEECH.md` in that folder.
2. `0001. Achology Website Upgrade 2026/04. Content Production Factory + COWORK/The Newsroom/Achology Newsroom/Kain's Books/`: `Responsibility_Rebellion__Full_Text_from_print_v100.md` and the two `Mental_Health_Rebellion__Chapter_*.md` files. Not the DSM sourcing register.
3. `0009. Achology Publications | The Practitioner Handbooks 📚/01. The Ultimate Life Coaching Handbook (published)/TULCH FINAL MANUSCRIPT.txt`.

## The run
1. **Split (script, free).** Cut each source into chunks of about 2,500 words on paragraph or sentence boundaries. Each chunk carries its source: the lesson code and title from the file name (for example `003-123 The 8 Stages of Connection in Mature Relationships`), or the book and its chapter or section heading.
2. **Mine (Haiku).** For each chunk, return JSON only (structured output), one object per piece kept:
   - `kind`: one of `signature_phrase`, `quotable_sentence`, `analogy`, `question`, `teaching_paragraph`.
   - `text`: Kain's words. Spoken fillers are removed (um, uh, you know, like used as filler, all right?) and so are direct repeats. **Nothing is reworded, reordered or added.**
   - `idea`: the idea it teaches, in 2 to 6 plain words (for example "responsibility comes before confidence").
   - `subject`: one of the seven Knowledge Hub subjects: Psychology, Helping People, Mental Wellness, Motivation, Personal Growth, General Interest, Wisdom for Life.
   - `source`: the chunk's source, as given.
   Keep only Kain's own words. **Leave out:** another speaker in a discussion lesson (Karen or a guest), anything he reads aloud from another author, course admin ("in the next video", "download the worksheet"), and anything that only makes sense with the video on screen. Keep a piece only if a writer could use it on a page as it stands.
3. **Guard (script, free).** For every piece, strip fillers from both the piece and its chunk, lower-case both, and check that the piece's words appear in the chunk in the same order, allowing only the removed fillers and repeats. A piece that fails is moved to `flagged.jsonl` with the reason, never kept.
4. **Tidy (script, free).** Remove exact and near duplicates (the same piece from two lessons is kept once, listing both sources). Sort by subject, then by idea, then by kind.
5. **Pilot first.** Run steps 1 to 3 on 20 lessons spread across the courses before the full run. If more than 5 percent of the pilot's pieces fail the guard, stop and report instead of running the rest.

## Output (staging, not the vault)
`0001. Achology Website Upgrade 2026/04. Content Production Factory + COWORK/The Newsroom/99 Working Papers/phrasebook_run_S433/`:
- `pieces.jsonl` (every kept piece) and `pieces.csv` (the same, one row each).
- `flagged.jsonl` (every piece the guard refused, with its reason).
- `FIRST_100__For_Chat.md`: the first 100 kept pieces after sorting, laid out kind, text, idea, subject and source, for Chat to read.
- `COST.md`: requests, tokens in and out, cache reads, batch discount, dollars, and dollars per million source words.
Do not write anything into `Achology Newsroom/15 Phrasebook/`. Chat files the pieces there after reading the first 100 and showing Kain a sample.

## One call Chat made, which Kain may overturn
The ruling files each piece by the idea note it teaches in Achology Wikipedia, but that library is still empty. So each piece carries a plain idea label and a subject now, and is matched to the library's notes when they exist. Nothing is lost: the label is kept.

## Done when
The four output files and `COST.md` are in the staging folder, the pilot passed the guard, spend is under $10, and a DONE file in TO Chat gives, on its first line, what it needs from Chat. Then: pieces kept per kind, pieces flagged, lessons and books read, the measured cost, and any lesson that could not be read.

## Vault notes that fit this job (The Shared Rules, section 6)
`A Voice Is Measured From Its Author's Own Work Before Any Rule About It Is Written` (Operating System, Knowledge): the reason the Phrasebook exists. `A Checker Is Calibrated On Rejected Work` is the reason the guard refuses a piece rather than repairing it.

*No em or en dashes in this file; checked before writing.*
