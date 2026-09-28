# DONE: The Seven Beliefs series, Parts 1 and 2

**From:** Claude Cowork, S386, Monday 28 September 2026 (session continued from Chat's brief the same day).
**Answers:** `BRIEF__The_Seven_Beliefs_Series_Parts_1_And_2_Then_Stop_S386.md`, TO Cowork.
**Delivered to:** Content Records/seven-beliefs-series/PART_01__the-seven-beliefs-achology-is-built-on.md and .../PART_02__every-human-being-can-grow-and-mature.md, each carrying its sourcing record beneath it.

Per the brief: Parts 1 and 2 only, then stop. Part 3 has not been started.

## Word counts (brief's band: 2,500 to 3,500 words, checked by hand)

- Part 1, article body only (excluding its sourcing record): 2,552 words.
- Part 2, article body only (excluding its sourcing record): 2,552 words.

Both sit inside the band. No type key exists yet for this series in `content_gate_standards.json` (confirmed against `python3 content_gate.py --types`, which lists no `seven-beliefs-series` entry), matching what the brief itself said to expect. The gate script therefore cannot run its type-specific pass on either file; every check below was run by hand instead, against the same shared bar the gate enforces on every other content type (dashes, banned words, paragraph floor, reading ease), per the brief's own instruction.

## Gate results (by hand)

Both articles, checked with a small Python script against the Base Voice and house-copy-standards rules:

- Em or en dashes: zero in both files.
- "Truly": zero in Part 1. One in Part 2, and it sits inside the Kierkegaard quote itself ("to will to be that self which one truly is"), a real person's own words, which the Base Voice rule does not edit.
- "Plainly": zero in both files.
- "Actually": one in each file, at the cap.
- Approximate Flesch reading ease (the same heuristic used elsewhere in this project, since `textstat` could not be installed offline): Part 1 about 61, Part 2 about 61. Both inside the 60 to 70 band, though not by a wide margin; I flag this rather than call it comfortably clear.
- Paragraph floor (at least three sentences or 50 words, one shorter line allowed per section): both pass; the check found no section carrying more than its one allowed short line.
- Both banned word lists (brand/marketing hype words, and the Base Voice's machine-written tells such as delve, tapestry, realm, seamless): clear in both files.
- Series panel: both headed "Part N of 9" and both close by naming the next part.
- Links: both link to `/about/what-achology-believes/`, Part 1 links forward to Part 2, and Part 2 links back to Part 1.

## The full UNVERIFIED list

Every quotation used is checked against a primary or near-primary source, but not every one against a physical book with a confirmed page number. Flagged rather than guessed, per the brief:

**Part 1:**
- Bernard of Chartres's "dwarfs on the shoulders of giants" saying (via John of Salisbury, *Metalogicon*, 1159): the specific book/chapter location within the *Metalogicon* was not confirmed. The saying and its attribution are well established, but I could not pin a page.
- Korzybski's "the map is not the territory" (*Science and Sanity*, 1933): a page 58 citation turned up in background research, from a secondary source rather than the physical book, so no page number is claimed in the article.

**Part 2:**
- Kierkegaard's "to will to be that self which one truly is" (*The Sickness Unto Death*, 1849): wording verified against an online reproduction of the English text and cross-checked, chapter and section location confirmed (Chapter 1, Section C), but the translator and print page number were not confirmed. Different English translations may paginate differently.
- William James's "Habit is thus the enormous fly-wheel of society, its most precious conserving agent" (*The Principles of Psychology*, 1890): wording verified against a primary-text reproduction and cross-checked, chapter confirmed (Chapter IV, "Habit"), but the print page number in any specific edition was not confirmed.
- Carl Rogers's "The good life is a process, not a state of being. It is a direction not a destination." (the essay "The Good Life and the Fully Functioning Person," in *On Becoming a Person*, 1961): wording verified against an online reproduction carrying the full surrounding paragraph, and cross-checked, but the print page number was not confirmed.

Nothing was used as a direct quotation without at least this level of check. Where I could not get further than "wording confirmed, page not," I said so on the record rather than inventing a number.

**One trap deliberately avoided, in both parts:** "We are what we repeatedly do. Excellence, then, is not an act, but a habit" was considered and rejected as an Aristotle quote. It is Will Durant's own paraphrase of Aristotle, from *The Story of Philosophy* (1926), confirmed via Snopes and cross-checked. Neither article attributes it to Aristotle.

## What I was unsure of, beyond sourcing

- **"Achology.com" versus "Achology" in running prose.** Project standing rule 2 says the business name is written in full as Achology.com. The approved exemplar this brief points to, `APPROVED__What_Achology_Believes_Page_Copy_S386.md`, never once writes "Achology.com" in its own body copy; it writes "Achology" throughout, speaking as the brand. I matched the exemplar's actual pattern rather than rule 2, on the judgement that rule 2 governs formal identification rather than every mention inside a page written in Achology's own speaking voice. I have not resolved this against rule 2 myself; it may need your ruling, and if you want "Achology.com" used in running prose, both articles need a pass to apply it.
- **Kierkegaard's translator.** I used the wording common to the English translations I could check online, but did not settle which named translation edition (Lowrie, Hannay, or the Hongs) Achology should cite if a page number is ever added. Flagged above as UNVERIFIED for that reason.
- **Reading ease margin.** Both articles measure just above 60 rather than comfortably mid-band. This is the same approximate heuristic, and the same tight-margin pattern noted earlier this session on the CBT hub guide fix. If a stricter reading-ease measurement is run later and disagrees, both may need another pass.

## Not done, on purpose

Part 3 has not been started, per the brief's explicit instruction to stop after Parts 1 and 2. Everything past this report waits on your read and your yes.
