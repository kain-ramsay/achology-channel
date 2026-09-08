# REPLY: the five S348 rulings are carried out, and two of the three lines you asked for are here

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** `RULING_AND_REPLY__Every_S105_Question_Answered_S348.md` sections 1, 2, 3, 4 and 7, and the second and third of the three lines owed on `COPY_BRIEF__Five_Our_People_Copy_Changes_And_Three_Lines_To_Send_Back_S348.md`.
**Board cards:** the 18 instructor articles; the 250 help articles; the Our People page.

---

## Section 1. The heading level, and the nine pages it was blocking

**All eighteen records changed**, 106 heading markers from four hashes to two, and the diff carries no other line: I01 five, I02 six, I03 five, I04 six, I05 five, I06 six, I07 six, I08 six, I09 six, I10 six, I11 six, I12 six, I13 six, I14 six, I15 six, I16 six, I17 seven, I18 six.

**Nine pages, not eight, and the ninth is included.** The S105 file said eight were blocked by the heading and one by the duplicate. Both blocks are gone, so all nine were corrected in one command: posts 34254, 34256, 34258, 34260, 34270, 34272, 34274, 34276 and 34280.

**Read back two ways.** The install reports no page of any Knowledge Hub type still carrying the three-hyphen paragraph, which is what the em dash was rendering from. And all nine render clean through the publish gate. The bodies were sent with `article_body_update.py --apply`, which writes `post_content` and never a status: every one of the nine was published before and is published now.

**One thing worth your eye, not a fault.** The archived I10 exemplar wrote its body sections at three hashes, not two, and the book note and author biography records are mostly three as well. The ruling said two and the eighteen now read two. If the house convention is actually three, that is a separate ruling and eighteen records would move again; I have not assumed it either way.

## Section 2. The I10 duplicate, measured

**The verdict is a measurement, not a choice.** The live page is post 34270, published, at `why-giving-advice-does-not-work`. Its body is 1,440 words normalised. `I10__why-good-advice-rarely-inspires-change.md` matches it **word for word, 1,440 of 1,440**. `I10__why-giving-advice-does-not-work__EXEMPLAR_S329.md` matches **about an eighth of it**, and is 1,507 words.

**So the first is the record and it stays.** The exemplar has moved to `Content Records Archive` with its name intact. Nothing deleted.

**Three things you should know about the file that moved.** It is not an older draft of the live article: it is a different piece of writing on a neighbouring subject, with its own Search and Citation Brief block, and it has never been imported. Its own `post_status` field reads draft, and only one post answers to that slug. If it is meant to become a page, it needs a different address and a different keyword, and that is yours.

**The archive sits beside Content Records rather than inside it, and that was not cosmetic.** Put inside, as your wording read, it was still walked by `article_body_update.py`'s record search and by `build_keyword_register.py`'s rebuild, both of which treat every folder under Content Records as a content type. The shelved file went on counting as a live record and went on blocking the very page the ruling was written to unblock. Overturn it in one word if you want it inside, but the two scripts then need a skip rule each, which is the one-rule-three-implementations shape my S105 file named as having cost a live page twice.

Its placement took it outside the tracked path, so `.gitignore` now names the archive as well. A record set aside still has no second copy.

## Section 3. `inbound_from` is a counted, named line

Done as ruled, and it fails nothing. It prints on every full-gate run, in the notes block beside the paragraph-word line, in one of four states: how many addresses the field names, that the field is present and empty, or that the field is not on the record at all.

The count reads the addresses out of the field rather than splitting on its separator, because each entry may carry the sentence the link belongs in and quoted text holds semicolons of its own.

**Six acceptance cases added, and the suite is 103 of 103.** Four prove the count and the four states. Two prove the half a counted line cannot prove about itself: that no state of the field changes the number of failures, and that the line is never a PASS or a FAIL. The count case goes red against a naive split, which reads a two-address value as four.

## Section 4. The keyword clash, and what it actually was

**The clash was not where the ruling placed it, and the ruling still resolves it.** The register held `kain ramsay` twice: on the **author biography** `kain-ramsay`, at `/learn/helping-people/articles/kain-ramsay/`, and on the help answer. That biography record's own `rm_focus_keyword` field reads `Kain Ramsay` and it keeps it, exactly as you ruled, so nothing on it moved.

**The help answer took its own title.** Post 255 now carries `who is kain ramsay`, read back off the install, and `HELP_SECTION__CLAIMS.csv` carries the same. The register rebuilt: **661 rows, no clashes.**

**One row you may want to look at, untouched.** The `/about/instructors/kain-ramsay/` page is a third thing again, and its claim reads `kain ramsay achology`, dated S097. It clashes with nothing, so I have left it.

## Section 7. The stale sheet, and the gun is unloaded

**The claim was proved, not taken.** The sheet's eighteen `post_name` values are the pre-S309 filename slugs, and not one of them is a live slug, so every one reads as free and a plain run creates eighteen duplicates. That is measured off the file, not remembered.

**And the replacement was proved before the deletion.** `build_upload_csv.py` rebuilt the type from the records: 28 rows carrying the live slugs. So the sheet was generated output and not a source, which is why deleting an untracked file was safe.

`--csv` is now required, with no default. A named sheet that does not exist is refused with the build command printed rather than a traceback. The sheet itself is deleted.

**Three records refused by the rebuild, on their own faults, and they are yours because they are body faults:** `I01__why-people-seek-help.md` and `I09__the-quiet-aim-of-good-helping.md` both fail "outcome or problem tags, 2 to 4" with one found. `KAREN_SOURCE_LESSONS_S344.md` is not a record and refuses on having no page-fields table, which is correct.

**One more sheet sits in the same folder, `UPLOAD__Instructor_Articles_15_S096.csv`.** It is not named in your ruling and I have not touched it. It is inert now that no importer has a default, but it is the same shape of thing.

---

## The two lines you asked for, verbatim

**The About page's lead, under "Achology: What It Is, and Who It's For".** Read from `page-about.php` this turn, 45 words:

> Achology teaches psychology in a way that makes you wiser, not just smarter. Below are the questions people most often ask before studying with us and joining the private learning community at community.achology.com, where members collaborate to practise the skills taught in their courses.

**Evelyn Montgomery's first two bio paragraphs**, read off the rendered page at `/about/instructors/evelyn-montgomery/` this turn, in the order a reader meets them:

> Evelyn Montgomery writes the most approachable articles for the Achology Knowledge Hub, designed for readers who may be encountering psychological concepts for the first time in their lives. She presumes no prior knowledge and always treats her readers with respect, never condescending.

> Evelyn starts with a moment, or a common experience a reader is likely to recognise from their own week, explains it in plain words, and then pulls back to show how it connects to something much larger about people. She treats her reader as a mature, responsible adult throughout, which means she explains the bigger ideas and 'harder parts' rather than quietly skipping over or ignoring them. Nothing is ever simplified to the point where it stops being true, and nothing at all is dressed up to sound cleverer than it really is in practice.

**Your premise for that edit does not survive the read, so read it before you draft.** Only the first paragraph says she writes the most accessible articles. The second does not repeat it. The line that does repeat it is her one-line card summary, "Evelyn writes Achology's most accessible articles, for readers meeting an idea in psychology for the first time", which sits on the hub card and on her page above these two paragraphs. If that is the repeat Kain saw, the cut belongs somewhere different from where the brief puts it.

The first of the three lines, the trial panel's 36 words, went to you at S105 and is not repeated here.

---

## Two of your files are a theme sitting's, and they are queued rather than done

`COPY_BRIEF__Five_Our_People_Copy_Changes_And_Three_Lines_To_Send_Back_S348.md` and `RULING__The_Trial_Panel_Heading_And_Body_Are_Kains_Final_Words_S348.md` both name pages and both want theme edits. Kain gave no ruling on either in this sitting, so neither was picked up: both are named in `000__THE_THEME_QUEUE.md` and both stay live in FROM Chat with their head lines. The trial panel ruling is understood and its words are not being questioned; it needs a sitting that deploys.

---

OWED BACK: nothing on the five rulings. On the two theme files, the theme version carrying their changes, read back off the page, which waits on a theme session.

*No em or en dashes in this file; checked before writing.*
