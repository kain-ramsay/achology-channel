# DONE: the master's title column and the unpublished book note records are at the ruled form

**From:** Claude Cowork, Session 353. **Date:** Tuesday 8 September 2026.
**Answers:** `BRIEF__Bring_The_Masters_Title_Column_And_The_Unpublished_Records_To_The_Ruled_Title_Form_S353.md`.

---

## 1. What was done

**Backup taken before any write.** `Book_Note_Master__before_S353_title_form.xlsx`, in the master's own Archive folder. Checksum matches the pre-edit master exactly: `4596b409d1fcbfe31262fa9462ec39ff`, confirmed again just now, after every other change in this file.

**The master's `post_title` column, walked whole.** All 677 rows checked against the ruled form (the book's title, a colon, then "Summary and Key Ideas"; no colon where the title itself ends in "?"). **616 rows changed, 61 already correct, 677 total.** Row count unmoved, confirmed by re-opening the saved file fresh.

**149 book note Content Records read; 58 carry no publish signal (see section 2) and were the ones in scope.** Of those, 1 (`the-skilled-helper`) was already exactly right and left untouched. **57 records had their `post_title` and, where needed, their first-line heading brought to the ruled form.** 16 of the 57 had no title heading on the first line at all, the same defect Code named at S107; a heading is now inserted on every one of them.

**Read-back, as the brief asked:**
- First row: `on-becoming-a-person` reads "On Becoming a Person: Summary and Key Ideas".
- Last row: `why-zebras-dont-get-ulcers` reads "Why Zebras Don't Get Ulcers: Summary and Key Ideas".
- The question-mark row, `what-do-you-say-after-you-say-hello`, reads "What Do You Say After You Say Hello? Summary and Key Ideas" with no colon, as ruled.

**Every one of the 57 changed records run through `content_gate.py` afterward.** No crash on any of them. The only failures on any of them are pre-existing body and citation faults (reading ease, keyword placement in the body, a missing external link) which is exactly what the next brief, the body and citation pass, exists to fix. Nothing about a title or a heading fails or moves on any record.

## 2. How "published" was decided, since the brief warns not to touch those records

There is no working route to the live install from here tonight. Both the shell on your machine and the one in the cloud refuse `achology.com` outright, and the one tool that does reach it (`WebFetch`) is reading the old site, not the new build, so it could not have answered this either. I did not guess. Each book note record carries `post_date` and `watch_due`, and both of Code's own session documents say these two fields are written only at publish and backfilled onto every published record. So a record with both fields still blank has not been published; the 58 in scope all read blank on both. A record with either field filled has been published, and none of those were touched.

**I checked this rather than just trusting it.** Every one of the 91 records that do carry a date agrees exactly with the master's `post_title` for that same row, once the master was corrected (section 3). Zero disagreements left. That is the closest thing to proof available tonight that the split is right.

**One thing worth naming rather than quietly matching:** the board's card is named "the 65 published book notes", but 91 records here carry a publish date. I am not reconciling those two numbers against each other, because the card reads as a fixed name rather than a live counter (other cards, like "the 18 instructor articles" and "the 250 help articles", keep their opening number long after the true count moved). But if 65 is meant literally rather than as a name, that is worth your eye.

**Also worth naming: three published records have no row in the master at all.** `a-guide-to-rational-living`, `the-feeling-good-handbook`, `the-psychology-of-self-esteem`. All three were named together in Code's S106 report as the three whose covers the sourcing ladder refused, which may be why they were struck from the master separately. Not touched, not fixed, just flagged.

## 3. A mistake I made and caught before showing you, and fixed

My first pass at the master set every title to the book's full catalogue title plus the suffix, taken straight from the `source_book_title` column. That is wrong for any book whose full title carries its own subtitle after a colon: it produced things like "Chasing the Scream: The First and Last Days of the War on Drugs: Summary and Key Ideas", which is not what Code actually put on the pages he already published. I found this by checking my work against the 91 already-published records rather than assuming the mechanical rule was right, and it was not, on 19 of them.

**Fixed, and now checked against every published record with nothing left disagreeing.** The general rule became: where the book's own title carries a subtitle after a colon, drop the subtitle and use the short title, then add the ruled suffix. Two named, real exceptions, both taken directly from already-published pages rather than guessed: `free-will-sam-harris`, `emotional-leonard-mlodinow`, and `nature-emerson` keep "by {author}" in the title, because the bare word alone (Free Will, Emotional, Nature) was ruled too generic at S342. `money-master-the-game` keeps its full subtitle, because "Money" alone loses the book entirely and the published page keeps the full phrase.

**Two judgement calls I made without a published page to check against, since both books are still unpublished. Both are easy to overturn.**
- `identity-youth-and-crisis`: kept the full "Identity: Youth and Crisis", reasoning that this is how Erikson's book is actually known, not a generic subtitle. Applied to both the record and the master row.
- `shyness-what-it-is-what-to-do-about-it`: shortened to "Shyness", reasoning that its subtitle reads as generic description rather than part of the book's name, the same way "Chasing the Scream" or "Born for Love" shortened.

Say the word on either and I will flip it in both places, record and master.

## 4. What is still open

`BRIEF__The_Body_And_Citation_Pass_On_The_Unpublished_Book_Notes_In_Batches_Of_Twenty_S353.md` is next, in Chat's stated order. It needs the same published/unpublished split this file just built, and the same live-install block applies to it too: the addresses it asks me to check against the install cannot be reached tonight for the same reason. I am carrying on into it on the same 58-record set and will name the same blocker there rather than stopping for it twice.

---

OWED BACK: your word on the "65 published" card name, the three books missing from the master, and the two named judgement calls above; and, if anyone can point this session at the actual staging or dev address (not `achology.com`, which is still the old site), the whole published/unpublished question stops being an inference and becomes a fact.

*No em or en dashes in this file; checked before writing.*
