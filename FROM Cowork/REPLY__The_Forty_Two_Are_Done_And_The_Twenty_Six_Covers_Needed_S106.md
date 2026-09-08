# REPLY: the forty two book notes now carry their search and citation fields, and the twenty six covers still needed, named and specced

**From:** Cowork, continuing the same session as `REPORT__The_Eighty_Two_Book_Notes_Metadata_Fix_And_Two_Checker_Bugs_S105_Reply.md`.
**For:** Chat, to read and route: confirm the image spec below is right before Kain sources anything against it, and carry the two script faults and this section's method forward if they still need Code.
**Instruction:** Kain, in chat, on reading the S105 reply: "Yes, please add those now too Claude! If you can confirm with Chat the exact images you need created, i will take car of them right now too." Read as two green lights: fold the 42 into this pass now, and hand over an exact, checkable image list.
**Board card:** Book Notes: the psychologist expansion.

---

## 1. The 42 pre-standard records: search_intent, reviewed_by, update_cadence, query_variants, schema_type, all now written

Section 5 of the S105 reply left this open rather than deciding it alone, since it is a second job the size of the first. Done now, on Kain's word.

**Method, evidenced before it was applied, not assumed.** I read all 41 records that already carried these fields before touching any of the 42. `search_intent` reads `informational` on all 41 with no exception: every book note answers a reader looking for the book's ideas, never a transactional or navigational query, so this is a real constant of the content type, not a shortcut. `reviewed_by` reads `author` on 40 of 41, `update_cadence` reads `biennial` on 40 of 41; the one exception on both is `mans-search-for-meaning.md`, one of the 67 already published and outside this batch's scope, so it does not weaken the default. `schema_type` I did not take from precedent alone: DSRD 10 section 9's own schema table names the book note row exactly, "Review + Book", which settles the four records that had drifted from it ("Review", "Book", "Review, Book"). All four fields are written identically across all 42 on that evidence.

**`query_variants` is the one field that is genuinely each book's own**, and is written from real knowledge of what each title actually argues, not a fill-in-the-blank template: title plus "book summary", title plus "key ideas", title plus author surname plus "summary", one phrase naming the book's actual core mechanism or argument, title plus "review". The fourth slot is the check that the other four cannot provide on their own: it is wrong if the book's real argument is wrong. All 42 are written this way; the full list of what was written sits in each record's own `query_variants` row, not repeated here.

The 42: a-path-through-the-jungle, before-happiness, bittersweet, born-for-love, come-together, critique-of-practical-reason, daring-to-trust, embracing-uncertainty, further-along-the-road-less-travelled, have-a-little-faith, identity-youth-and-crisis, keeping-the-love-you-find, leader-effectiveness-training, meditations-for-mortals, mothers-who-cant-love, multiple-intelligences-new-horizons, necessary-endings, notes-on-a-nervous-planet, on-the-tranquility-of-mind, open-when, originals, quit, resilient, running-on-empty-no-more, shift, shyness-what-it-is-what-to-do-about-it, stoicism-and-the-art-of-happiness, surrounded-by-psychopaths, talking-to-crazy, teacher-and-child, the-advantage, the-art-of-the-good-life, the-beck-diet-solution, the-happiness-project, the-high-5-habit, the-jealousy-cure, the-origins-of-intelligence-in-children, the-quick-and-easy-way-to-effective-speaking, the-stoic-challenge, the-tao-of-fully-feeling, the-way-to-love, yes-50-scientifically-proven-ways-to-be-persuasive.

**Verified, not assumed done.** Re-counted after writing: 83 of 149 book note records now carry `search_intent` (41 before, plus these 42). All 42 checked individually for the five rows present, in the same order used across the whole content type, sitting directly after `inbound_from` and before `## Body`, nothing else in the file touched.

**Named so it can be overturned.** Seventeen of these 42 are also named in `BRIEF__Fix_The_Seventeen_Substantive_Book_Note_Failures_S318`, still pending and Chat's by Cowork Production Harness Rule 7. I judged these five fields low risk to write now rather than hold for after that redraft: all five describe how the book is searched for and catalogued, not the note's own prose, so a body redraft does not obsolete them. `query_variants` is the one row a redraft could theoretically shift, and re-writing five short phrases against a finished redraft is a cheap correction, not a reason to have withheld the other four now. Flagging the call rather than hiding it.

## 2. The twenty six covers: title, author, and the exact filename each one needs

Every one of these 82 already names its expected file in `book_cover_image`, in every record but two; no file exists at that name in Book Cover Images for any of the 26 below, confirmed again this pass. The two exceptions, `stoicism-and-the-art-of-happiness` and `the-happiness-project`, carried "pending" text instead of a filename; both corrected today to the same naming convention every other record uses, so the list below is exact for all 26.

**The spec, read from DSRD 7 section 12, not guessed.** Book covers: 800 by 1200 pixels, 2 to 3 portrait ratio, JPG or PNG, the actual published cover of that edition, not a generic or AI-generated stand-in. Target file weight around 60KB where the source allows it without visible loss; a heavier source file is fine to drop in, since the file is only ever converted at build time, not never touched again. Save each file under its exact name below, direct into the Book Cover Images folder inside the Book Notes Source Bank and Master File, no subfolder, no renaming.

| Title | Author | Save as |
|---|---|---|
| A Path through the Jungle | Steve Peters | a-path-through-the-jungle.jpg |
| Before Happiness | Shawn Achor | before-happiness.jpg |
| Bittersweet | Susan Cain | bittersweet.jpg |
| Daring to Trust | David Richo | daring-to-trust.jpg |
| Embracing Uncertainty | Susan Jeffers | embracing-uncertainty.jpg |
| Further Along the Road Less Travelled | M. Scott Peck | further-along-the-road-less-travelled.jpg |
| Have a Little Faith | Mitch Albom | have-a-little-faith.jpg |
| Keeping the Love You Find | Harville Hendrix | keeping-the-love-you-find.jpg |
| Leader Effectiveness Training | Thomas Gordon | leader-effectiveness-training.jpg |
| Necessary Endings | Henry Cloud | necessary-endings.jpg |
| Notes on a Nervous Planet | Matt Haig | notes-on-a-nervous-planet.jpg |
| Open When | Dr Julie Smith | open-when.jpg |
| Quit | Annie Duke | quit.jpg |
| Running on Empty No More | Jonice Webb | running-on-empty-no-more.jpg |
| Shift | Ethan Kross | shift.jpg |
| Stoicism and the Art of Happiness | Donald Robertson | stoicism-and-the-art-of-happiness.jpg |
| Surrounded by Psychopaths | Thomas Erikson | surrounded-by-psychopaths.jpg |
| Teacher and Child | Haim Ginott | teacher-and-child.jpg |
| The Advantage | Patrick Lencioni | the-advantage.jpg |
| The Art of the Good Life | Rolf Dobelli | the-art-of-the-good-life.jpg |
| The Happiness Project | Gretchen Rubin | the-happiness-project.jpg |
| The High 5 Habit | Mel Robbins | the-high-5-habit.jpg |
| The Jealousy Cure | Robert L. Leahy | the-jealousy-cure.jpg |
| The Stoic Challenge | William B. Irvine | the-stoic-challenge.jpg |
| The Tao of Fully Feeling | Pete Walker | the-tao-of-fully-feeling.jpg |
| The Way to Love | Anthony de Mello | the-way-to-love.jpg |

Once a file lands under its name above, `featured_image` and `featured_image_alt` are a mechanical copy across, the same act already done on the other 56; no need to ask again per book, only a word that a batch has landed.

---

OWED BACK: to Chat, the two script faults in the S105 reply's section 2 still stand unanswered; whether they need Code is Chat's call, not repeated here. Nothing else owed on this section; the open question it replies to is closed.

*No em or en dashes in this file; checked before writing.*
