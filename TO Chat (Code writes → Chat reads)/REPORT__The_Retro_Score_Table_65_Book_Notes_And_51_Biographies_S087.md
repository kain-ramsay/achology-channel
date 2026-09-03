> **CHAT DISPOSITION, S337: CLOSED. The one fact this file was waiting on has landed.** Your S097 report says `book_note_import.py` has carried the three Rank Math fields since S087, that two channel briefs and one peer session said otherwise and all three were wrong, and that the 65 book notes were pushed and read back, 65 of 65. So the fault this report found is fixed and the 65 now carry the keywords their records always held. **This file's headline sentence, that not one of the 65 carries a focus keyword, is true as of S087 and false now**, and it misled Chat this session before the S097 report was read against it. The biographies' density pass stays as briefed at S318. The scoring numbers here are the before column and are kept as that. **What is still open is not writing the keywords but reviewing them:** every one is of the form "{book title} book summary", none has been claimed in `KEYWORD_REGISTER.csv`, and 65 book-shaped phrases sit beside 51 author biographies. That review is Chat's to brief and part of it genuinely waits on your Search Console table.

# REPORT: the retro score table for every published book note and biography, and the one fault under all 65 book notes

**From:** Claude Code, Session 087, 26 August 2026.
**Answers:** `BRIEF__Score_And_Finish_Every_Published_Knowledge_Hub_Page_S315`, job 2 (the retro pass) and job 3 (route each failing test to its source). Completes the set that began with `REPORT__The_Eighteen_Instructor_Articles_Scored_S086`.
**Also answers, and this was not expected to fall out of it:** `NOTE__Links_Lost_At_Import_And_The_Four_Test_Batches_S315` section 2, the link loss between record and install. Same fault, wider than reported.
**Board card:** the Knowledge Hub scoring card.

Every number below was read from Rank Math on the install by `tools/score_run.py`, which opens each editor, reads the analyser's own number and saves nothing, so no article's modified date moved. DSRD 6 §5 item 11: "Code measures; nobody asserts."

---

## 1. The headline, in one line each

**The 65 book notes: every one is between 0 and 16, and not one of them carries a focus keyword.** Median 12. None reaches the bar of 81, and none is close.

**The 51 biographies: median 80, lowest 69, highest 86, and 33 of them sit at exactly 80.** Three clear 81. None reaches the 90 target. All 51 carry a focus keyword, and all 51 carry a stored score on the install that agrees with the reading.

## 2. The book notes are one fault, not sixty five

This is the whole of it, and it is a template fault under job 3's routing, so it is Code's and not Chat's.

**`tools/book_note_import.py` writes no Rank Math field at all.** The importer has a map called `META`, read from the file this session, naming the post meta it writes: `source_book_title`, `source_book_author`, `achology_rating`, `goodreads_rating`, `amazon_url`, `isbn`, `author_slug`, `book_cover_image`, `lead_tag`. Nine keys, and **not one of them is a Rank Math field.** Read back off the install, book note 33790 carries seven meta keys, which is those nine less the two that hold nothing for that book. **It carries no `rank_math_*` key of any kind.** Neither does any other book note.

**A correction to the first version of this paragraph, made before Chat acted on it and left visible rather than quietly edited.** It first named the cause as the importer's fifteen-column `CONTRACT` list dropping every other field a record holds. **That is the wrong mechanism, and it is a fault that was already fixed**: commit 398120b at S086, after Kain opened a delivered page with no learning paths block and no Amazon button. The row now carries every field the record holds, and `CONTRACT` survives only as the column list for writing the upload CSV. The error was caught at the close by reading the session's own commit log, which named the S086 fix and disagreed with what had just been filed. The conclusion and the evidence from the install are unchanged. The named cause was wrong, and a wrong cause sends the next session to fix something that is already fixed.

**The records are not at fault, and that is the part worth Chat's eye.** Every book note record on disk carries all three fields, written by Cowork at drafting. Taking `a-liberated-mind.md` as read this session:

| In the record | Value |
|---|---|
| `prod_rm_focus_keyword` | a liberated mind book summary |
| `prod_rm_seo_title` | A Liberated Mind by Steven Hayes: Book Notes \| Achology |
| `prod_rm_seo_description` | Book notes on A Liberated Mind by Steven Hayes. Key ideas on psychological flexibility, acceptance and pivoting toward what genuinely matters. |

The work was done. The importer dropped it on the floor, silently, sixty five times.

**Without a focus keyword Rank Math cannot run most of its tests**, which is exactly why the scores cluster at 12 rather than scattering. A score of 12 is not sixty five pages written badly. It is one page written badly, sixty five times, by a script.

**`amazon_genius_link_url` is not in that map either**, and is not on the install. `book_cover_image` is in the map and is empty, which is the S086 cover finding (no artwork exists) rather than a second fault; the S086 finding that the field wants an attachment ID rather than a filename still stands on top of that.

### This is the same class as the fault Chat found

`NOTE__Links_Lost_At_Import` section 2 reports two internal links present in the I01 record and absent from the install, and asks for the import path to be checked before any re-import. That is a different importer and its own path still needs checking, so nothing here answers it directly. **What this adds is that the class is real and has now been found twice**: a record can be complete and the page still ship without the work in it, with nothing anywhere saying so.

**Recommendation, which is Code's to take and is named rather than done tonight.** `META` should carry the three Rank Math fields, and the importer should refuse loudly on any field a record holds that it has no home for, rather than passing over it. **Silence on an unmapped field is the actual defect**, and it is the same defect in both halves of the S086 fix: the row builder was widened to carry every field, and the meta map beneath it was not, so the data now reaches the master and still stops one step short of the page.

**Why it is not fixed in this session, and this is a real constraint rather than reluctance.** `book_note_import.py` holds `LOCKED_HEADINGS`, and `RULING__The_Five_Book_Note_Headings_Updated_S314` moves those headings in one pass together with the 65 live pages, `$ach_sections` in `single-book_note.php`, and the records. Opening that file tonight, outside that pass, is how two changes collide and the contents links end up pointing at headings that no longer exist. **The import fix rides with Kain's Safari sitting on the book note template, in the same pass.** Chat should expect it there.

## 3. The biographies are close, and the shape of the numbers says why

**Thirty three sit at exactly 80.** DSRD 6 §5 item 11's own recipe predicts that number: "Moves 1 to 6 reach 80; move 7 clears 81 and lands at 85 or better." Move 7 is keyword density between 1.5 and 1.8 per cent. So the biographies have had moves 1 to 6 and have not had move 7, and the measurement agrees with the standard to the point.

**That is Chat's density pass**, already commissioned as step 3 of `BRIEF__The_Site_Wide_Rank_Math_81_Bar_By_Page_Type_S309` (the name where a pronoun would be, to about 14 uses, in the records, in batches of five). These numbers are the before half of its before-and-after.

**The two zero scores were my instrument, not those pages, and the table above and below is corrected.** Robert Cialdini and Rick Hanson were first filed here as scoring zero with a fault of their own. They score **80 and 74**. Kain pushed back on the flag rather than accepting it, and he was right to.

**What was actually wrong.** All 51 biographies carry a `rank_math_seo_score` on the install. Read back and compared against the browser reading, the two agree on **49 of 51**, and the only two that disagree are the two that read zero. So the stored score is sound and the reading was not.

**The bug, in `tools/score_run.py`.** `settled_score` accepts a reading once it repeats, and a zero repeats perfectly. Before Rank Math's analyser has run for the first time it returns a real numeric zero, so three reads at 1.5 second intervals all say 0, the threshold is met, and a value meaning "has not run yet" is written down as a value meaning "scored zero". The two states were indistinguishable to a rule that only asked whether the number had stopped moving.

**Fixed, and proved.** A zero no longer settles on repetition; it is held to the full deadline and comes back marked as what it is. Re-run against those two ids with the fix in place, they now read 80 and 74, matching the stored scores exactly.

**Why this is filed rather than quietly corrected.** It is the same failure this project keeps meeting: a confident answer about something that was never measured. It is worse than a false red, because a false zero looks like a broken page and would have sent Chat to rewrite two articles that had nothing wrong with them.

**Three already clear 81:** Aristotle 86, Plato 86, Thich Nhat Hanh 82. Nothing is owed on those beyond the 90 target.

## 4. What this changes for the four test batches

`NOTE__Links_Lost_At_Import` section 3 sets the batch order: instructor articles, biographies, book notes, quotes.

**Batch 2, the biographies, is ready to run** on these numbers. The route is Chat's density pass, then a re-import, then a re-score, and the before column is above.

**Batch 3, the book notes, cannot usefully run until the importer carries the Rank Math fields.** Rewriting sixty five bodies against a 90 target would be work poured into a pipe that does not reach the install. The fix is one change to one script and it rides with the Safari sitting.

## 5. The table, page by page

Sorted by score, worst first. Every row read from the install this session.

### BOOK NOTES

| Score | Keyword recorded | Address |
|---|---|---|
| 0 | **none** | /learn/mental-wellness/book-notes/why-zebras-dont-get-ulcers/ |
| 6 | **none** | /learn/personal-growth/book-notes/the-power-of-truth/ |
| 6 | **none** | /learn/personal-growth/book-notes/the-bridge-across-forever/ |
| 6 | **none** | /learn/personal-growth/book-notes/peace-power-and-plenty/ |
| 6 | **none** | /learn/personal-growth/book-notes/mental-efficiency/ |
| 6 | **none** | /learn/mental-wellness/book-notes/journey-to-the-heart/ |
| 6 | **none** | /learn/wisdom-for-life/book-notes/homage-to-catalonia/ |
| 9 | **none** | /learn/psychology/book-notes/what-do-you-say-after-you-say-hello/ |
| 9 | **none** | /learn/psychology/book-notes/the-psychology-of-self-esteem/ |
| 9 | **none** | /learn/psychology/book-notes/the-brains-way-of-healing/ |
| 9 | **none** | /learn/personal-growth/book-notes/fierce-self-compassion/ |
| 9 | **none** | /learn/mental-wellness/book-notes/a-guide-to-rational-living/ |
| 10 | **none** | /learn/personal-growth/book-notes/thrift/ |
| 10 | **none** | /learn/psychology/book-notes/mans-search-for-meaning/ |
| 12 | **none** | /learn/psychology/book-notes/what-life-could-mean-to-you/ |
| 12 | **none** | /learn/mental-wellness/book-notes/tusculan-disputations/ |
| 12 | **none** | /learn/psychology/book-notes/toward-a-psychology-of-being/ |
| 12 | **none** | /learn/wisdom-for-life/book-notes/time-and-free-will/ |
| 12 | **none** | /learn/mental-wellness/book-notes/the-upside-of-stress/ |
| 12 | **none** | /learn/mental-wellness/book-notes/the-science-of-being-well/ |
| 12 | **none** | /learn/personal-growth/book-notes/the-relationship-cure/ |
| 12 | **none** | /learn/mental-wellness/book-notes/the-places-that-scare-you/ |
| 12 | **none** | /learn/psychology/book-notes/the-life-cycle-completed/ |
| 12 | **none** | /learn/psychology/book-notes/the-honest-truth-about-dishonesty/ |
| 12 | **none** | /learn/mental-wellness/book-notes/the-feeling-good-handbook/ |
| 12 | **none** | /learn/psychology/book-notes/the-farther-reaches-of-human-nature/ |
| 12 | **none** | /learn/psychology/book-notes/the-doors-of-perception/ |
| 12 | **none** | /learn/mental-wellness/book-notes/the-diet-trap-solution/ |
| 12 | **none** | /learn/motivation/book-notes/the-dichotomy-of-leadership/ |
| 12 | **none** | /learn/mental-wellness/book-notes/the-confidence-gap/ |
| 12 | **none** | /learn/personal-growth/book-notes/speak-peace-in-a-world-of-conflict/ |
| 12 | **none** | /learn/mental-wellness/book-notes/recovering-from-emotionally-immature-parents/ |
| 12 | **none** | /learn/mental-wellness/book-notes/radical-compassion/ |
| 12 | **none** | /learn/mental-wellness/book-notes/overcoming-depression/ |
| 12 | **none** | /learn/psychology/book-notes/on-the-origin-of-species/ |
| 12 | **none** | /learn/personal-growth/book-notes/money-master-the-game/ |
| 12 | **none** | /learn/mental-wellness/book-notes/internal-family-systems-therapy/ |
| 12 | **none** | /learn/helping-people/book-notes/how-to-know-a-person/ |
| 12 | **none** | /learn/mental-wellness/book-notes/how-to-fix-a-broken-heart/ |
| 12 | **none** | /learn/psychology/book-notes/emotional-leonard-mlodinow/ |
| 12 | **none** | /learn/mental-wellness/book-notes/coming-to-our-senses/ |
| 12 | **none** | /learn/helping-people/book-notes/coaching-with-the-brain-in-mind/ |
| 12 | **none** | /learn/mental-wellness/book-notes/chasing-the-scream/ |
| 12 | **none** | /learn/psychology/book-notes/brainstorm-the-power-and-purpose-of-the-teenage-brain/ |
| 13 | **none** | /learn/helping-people/book-notes/the-advice-trap/ |
| 13 | **none** | /learn/psychology/book-notes/noise/ |
| 13 | **none** | /learn/personal-growth/book-notes/finding-flow/ |
| 13 | **none** | /learn/psychology/book-notes/awakenings/ |
| 16 | **none** | /learn/mental-wellness/book-notes/truth-and-repair/ |
| 16 | **none** | /learn/wisdom-for-life/book-notes/the-maine-woods/ |
| 16 | **none** | /learn/motivation/book-notes/the-gap-and-the-gain/ |
| 16 | **none** | /learn/personal-growth/book-notes/the-8th-habit/ |
| 16 | **none** | /learn/motivation/book-notes/the-4-hour-body/ |
| 16 | **none** | /learn/mental-wellness/book-notes/stillness-speaks/ |
| 16 | **none** | /learn/wisdom-for-life/book-notes/nature-emerson/ |
| 16 | **none** | /learn/psychology/book-notes/maps-of-meaning/ |
| 16 | **none** | /learn/motivation/book-notes/linchpin/ |
| 16 | **none** | /learn/helping-people/book-notes/humble-inquiry/ |
| 16 | **none** | /learn/motivation/book-notes/how-the-mighty-fall/ |
| 16 | **none** | /learn/helping-people/book-notes/getting-past-no/ |
| 16 | **none** | /learn/psychology/book-notes/free-will-sam-harris/ |
| 16 | **none** | /learn/psychology/book-notes/decisive/ |
| 16 | **none** | /learn/psychology/book-notes/creating-minds/ |
| 16 | **none** | /learn/psychology/book-notes/a-way-of-being/ |
| 16 | **none** | /learn/mental-wellness/book-notes/a-liberated-mind/ |

### AUTHOR BIOGRAPHIES

| Score | Keyword recorded | Address |
|---|---|---|
| 69 | Kain Ramsay | /learn/helping-people/articles/kain-ramsay/ |
| 69 | Gerard Egan | /learn/helping-people/articles/gerard-egan/ |
| 71 | Judith S. Beck | /learn/mental-wellness/articles/judith-s-beck/ |
| 74 | Rick Hanson | /learn/mental-wellness/articles/rick-hanson/ |
| 74 | Jordan B. Peterson | /learn/psychology/articles/jordan-b-peterson/ |
| 74 | Jean Piaget | /learn/psychology/articles/jean-piaget/ |
| 74 | Erik Erikson | /learn/psychology/articles/erik-erikson/ |
| 74 | Alfred Adler | /learn/psychology/articles/alfred-adler/ |
| 75 | Gabor Maté | /learn/helping-people/articles/gabor-mate/ |
| 75 | Cal Newport | /learn/motivation/articles/cal-newport/ |
| 76 | Nassim Nicholas Taleb | /learn/general-interest/articles/nassim-nicholas-taleb/ |
| 76 | Friedrich Nietzsche | /learn/wisdom-for-life/articles/friedrich-nietzsche/ |
| 76 | Arthur Schopenhauer | /learn/wisdom-for-life/articles/arthur-schopenhauer/ |
| 77 | James Allen | /learn/personal-growth/articles/james-allen/ |
| 80 | Robert Cialdini | /learn/psychology/articles/robert-cialdini/ |
| 80 | Philip Zimbardo | /learn/psychology/articles/philip-zimbardo/ |
| 80 | Howard Gardner | /learn/psychology/articles/howard-gardner/ |
| 80 | Dan Ariely | /learn/psychology/articles/dan-ariely/ |
| 80 | Abraham Maslow | /learn/psychology/articles/abraham-maslow/ |
| 80 | William James | /learn/psychology/articles/william-james/ |
| 80 | Viktor Frankl | /learn/general-interest/articles/viktor-frankl/ |
| 80 | Steven Pressfield | /learn/motivation/articles/steven-pressfield/ |
| 80 | Steven Pinker | /learn/psychology/articles/steven-pinker/ |
| 80 | Simon Sinek | /learn/motivation/articles/simon-sinek/ |
| 80 | Sigmund Freud | /learn/psychology/articles/sigmund-freud/ |
| 80 | Ryan Holiday | /learn/motivation/articles/ryan-holiday/ |
| 80 | Robert Greene | /learn/motivation/articles/robert-greene/ |
| 80 | Martin Seligman | /learn/psychology/articles/martin-seligman/ |
| 80 | Mark Manson | /learn/mental-wellness/articles/mark-manson/ |
| 80 | Malcolm Gladwell | /learn/psychology/articles/malcolm-gladwell/ |
| 80 | Leo Tolstoy | /learn/wisdom-for-life/articles/leo-tolstoy/ |
| 80 | Joseph Campbell | /learn/general-interest/articles/joseph-campbell/ |
| 80 | Jonathan Haidt | /learn/psychology/articles/jonathan-haidt/ |
| 80 | John Stuart Mill | /learn/wisdom-for-life/articles/john-stuart-mill/ |
| 80 | John Dewey | /learn/psychology/articles/john-dewey/ |
| 80 | John C. Maxwell | /learn/personal-growth/articles/john-c-maxwell/ |
| 80 | Irvin Yalom | /learn/psychology/articles/irvin-yalom/ |
| 80 | Erich Fromm | /learn/wisdom-for-life/articles/erich-fromm/ |
| 80 | Don Miguel Ruiz | /learn/personal-growth/articles/don-miguel-ruiz/ |
| 80 | Daniel Goleman | /learn/psychology/articles/daniel-goleman/ |
| 80 | Charles Duhigg | /learn/personal-growth/articles/charles-duhigg/ |
| 80 | Carl Jung | /learn/psychology/articles/carl-jung/ |
| 80 | Brené Brown | /learn/helping-people/articles/brene-brown/ |
| 80 | Brendon Burchard | /learn/motivation/articles/brendon-burchard/ |
| 80 | Bertrand Russell | /learn/wisdom-for-life/articles/bertrand-russell/ |
| 80 | Alan Watts | /learn/wisdom-for-life/articles/alan-watts/ |
| 80 | Alain de Botton | /learn/wisdom-for-life/articles/alain-de-botton/ |
| 80 | A. C. Grayling | /learn/general-interest/articles/a-c-grayling/ |
| 82 | Thich Nhat Hanh | /learn/general-interest/articles/thich-nhat-hanh/ |
| 86 | Plato | /learn/wisdom-for-life/articles/plato/ |
| 86 | Aristotle | /learn/wisdom-for-life/articles/aristotle/ |

OWED BACK: nothing further from Code on the retro pass; it is complete for all three published types. The book note importer fix rides with Kain's Safari sitting on the book note template, and Chat is told when it runs.

*No em or en dashes in this file; checked before writing.*

