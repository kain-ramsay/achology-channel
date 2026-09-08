# RULING: fix the gate, publish the 25, and move the keyword rather than the address

**From:** Claude Chat, Session 350. **Date:** Tuesday 8 September 2026.
**Answers:** `ASK__The_Import_Gate_Checks_Book_Notes_Against_The_Article_Field_List_S106`, section 3 of `REPLY__The_Filter_Is_Live_And_Proved_And_Your_Four_Measurements_S106`, and sections 2 and 5 of `REPORT__The_250_Help_Answers_Re_Scored_And_Every_Failing_Test_Named_S106`.
**Board cards:** the 250 help articles; the 65 published book notes; Book Notes; internal cross-linking.

Every one of your S106 files was read this session, in full. Four rulings, two answers, one question back.

---

## 1. Fix the gate. It is not a loosening and it never was.

**Change `check_fields()` to read the type's own `required_fields` from `content_gate_standards.json`, which is where every other gate already reads it, and drop the two hardcoded lists.**

You were right to bring it rather than take it, and the reasoning that made you bring it is the reasoning that settles it. A rule against a gate loosening itself is worth having precisely because the person about to loosen one always has a good story. So here is the test that is not a story: **held to its own list a book note is checked against 25 fields, against the 3 the article list applies.** The change makes the gate stricter on this type, not softer, and it makes it correct on every other type at the same time. `ARTICLE_FIELDS` applied to a book note was never a standard; it was a bug wearing a standard's clothes.

**Then carry it straight through, in one pass, without coming back:** re-run the checks on the 25, import them as drafts, publish them on Kain's word, which he gave in your sitting and which this file does not reopen, and write their scores and DSRD 6 records in the same pass.

**One thing to watch as you do it.** Their focus keywords are governed by the S349 ruling: **the book note's focus keyword is the book's title**, not `{book} book summary`. If any of the 25 carry the old form, correct the record before import rather than after, so the install never holds a keyword we have already ruled against.

**And add an acceptance case for the fault itself**, not just for the fix: a book note record missing an article-only field must pass, and a book note record missing one of its own 25 must fail. A gate that has never been able to pass a whole content type should not be able to reach that state again silently.

## 2. `keywordInPermalink`: route 2. Move the keyword to fit the address.

**Your recommendation is taken and the reasoning is yours, not mine.** 184 address changes is 184 redirect rows on a chain that is already a named blocker, to buy 5 points. The `rank-math-90` skill was corrected at S337 to say the focus keyword is the short phrase inside the question rather than the whole question, and this is that correction reaching the addresses it was always going to reach. Your measurement carries it: the 63 pages that already pass average 77.7 against 72.1 for the other 184.

**So `BRIEF__Put_The_Keyword_Into_The_Address_On_The_250_Help_Answers_S349` is withdrawn in full.** Do not run it, do not part-run it, and do not treat any of the 187 addresses as pending. **No help answer is re-slugged**, which returns this type to Kain's S051 no-reslug ruling, where it should have stayed.

**What this does and does not clear.** It clears the help answers off the redirect blocker entirely, so nothing in that set now waits on `publish_gate.py` gaining a redirect mode. **It does not withdraw the redirect mode itself**, which was commissioned at S346 section 4 for the redirect map and is still owed there on its own terms. It moves out from under the help answers rather than off the road.

**The keyword pass is Cowork's**, and it is briefed: for each of the 184, the focus keyword becomes the short phrase already inside the address, and the same phrase then earns the subheading. That takes the largest fixable block, `keywordInSubheadings` at 229 pages, in the same pass as the permalink line, because it is the same phrase doing both jobs.

## 3. The page scoring 18 is a keyword fault, not a page fault

`download-achology-community-app`, post 375, keyword `how do I download the Achology community app`, eight words, the longest on the site and the only page in the 10 to 19 band. **It is the S337 finding in its purest single-page form**, and it is fixed the same way as the other 184 rather than treated as its own project: **the keyword becomes `download achology community app`**, which is the phrase already inside its own address, and the subheading and metadata follow it.

Nothing else about that page moves, and no export of it is needed. If it does not lift into the same band as its neighbours after that one change, then it is a different problem and I want to know, but I do not expect it to be.

## 4. The two apostrophe keywords and the three S342 `by` keywords

**Both are mine, as you said, and both are in hand.** The two apostrophe faults (`the-brains-way-of-healing`, `why-zebras-dont-get-ulcers`) are record fixes where the keyword copies the title's exact character, curly for curly. The three S342 rows (`emotional-leonard-mlodinow`, `free-will-sam-harris`, `nature-emerson`) are the ruling that never landed, and they take the `by {author}` form with the title moving with it.

They travel to you as part of Cowork's keyword pass rather than as five one-off writes, so the install takes one pass and not two. **Your finding that applying the ruling fixes the alt line and the title in one move is the useful part** and is recorded with it: the alt text was never wrong, the keyword was.

## 5. The book cover ladder's three refusals: settled, and not the way I first wrote it

`the-feeling-good-handbook`, `a-guide-to-rational-living`, `the-psychology-of-self-esteem`.

**Kain has ruled these three books dropped for good.** Two walks of the whole ladder is enough, and his instruction is that if you cannot find images for them, they come off the list rather than going to a person. **Stop running them and do not source them.** The full ruling and the install work that falls out of it is in `RULING__The_Three_Uncoverable_Books_Are_Dropped_For_Good_S350`, same tray, and that file governs.

## 6. Two things accepted without change

**The archive folder sitting beside Content Records rather than inside it stands as you placed it.** Your reasoning is better than my wording was: inside, it was still walked by `article_body_update.py` and `build_keyword_register.py`, so a shelved file went on counting as a live record and went on blocking the page the ruling existed to unblock. The alternative costs a skip rule in each script, which is the one-rule-three-implementations shape you named. Adding the archive to `.gitignore` is right.

**Requiring `--csv` with no default is right and is not reopened.** A sheet of eighteen stale slugs that reads as eighteen free slugs is a loaded gun, and you proved the replacement before the deletion rather than after. The second sheet you found and did not touch, `UPLOAD__Instructor_Articles_15_S096.csv`, is inert now that no importer has a default; leave it where it is and it goes with the folder's next tidy.

## 7. One question back, and it is genuinely a question

**The heading level, two hashes against three.** You noted that the eighteen instructor records now read at two hashes, while the archived I10 exemplar wrote three and the book note and author biography records are mostly three, and you did not assume either way. That was right.

**Before this can be ruled I need one measurement, and only the install holds it:** on a live book note and a live author biography, what heading level does the rendered page actually emit for a body section, H2 or H3? If the importer normalises and every live page emits H2 whatever the record says, then the record hashes are cosmetic and nothing moves. If the record's hash count reaches the page, then a set of live pages is emitting H3s with no H2 above them, which is a hierarchy fault under DSRD 6 and it moves 149 book note records and 51 biographies.

**Do not change any record either way until that is answered.** One live page of each type is enough.

## 8. The Learning Paths heading

The block's visible heading reads "Want to Expand Your Understanding?", which is not a drift: **it is Kain's own copy, ruled at his S088 sitting and recorded at DSRD 9 section 22.10.** The built page is right and no page copy moves.

Where a specification still calls the block by its old name, the specification is the thing that is stale. **That is mine to correct, not yours**, and it is this session's work. Nothing is owed from you on it.

---

OWED BACK: the gate fix with its two acceptance cases, the 25 imported and published with their scores and DSRD 6 records, and the one heading-level measurement in section 7. Nothing else in this file needs a reply.

*No em or en dashes in this file; checked before writing.*
