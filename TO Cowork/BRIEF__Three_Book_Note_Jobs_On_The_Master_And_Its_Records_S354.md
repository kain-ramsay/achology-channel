# BRIEF: three book note jobs, all on the master and its records

**DOCUMENT TYPE:** brief, from Claude Chat, Session 354. **Date:** Wednesday 9 September 2026. **Signed by Kain in the S354 sitting.**
**Board card:** Book Notes.
**Why all three are yours:** the Book Note master is an xlsx and Chat cannot open one; and every published word is outside Code's hands under Harness Rule 8. Nothing here is doable by either of the other two.

**Take a backup of the master before any write**, into its own Archive folder, named the way you named `Book_Note_Master__before_S353_title_form.xlsx`, and print its checksum. Same discipline as S353, which worked.

---

## Job one: restore three master rows for three live pages

**The three books:** `a-guide-to-rational-living`, `the-feeling-good-handbook`, `the-psychology-of-self-esteem`.

You flagged these yourself at S353 and you were right. **All three are live pages on the install today.** They were struck from the master at S351 when Code could not source their covers and Kain ruled them dropped. **Kain then found the covers himself in the S107 sitting**, all three clear the 900 pixel bar, and Code restored the pages the same evening. Published book notes went 89 back to 92.

**What was never restored is the master.** Until it is, any run driven from the master skips these three silently, which is the same shape of fault as the title column you fixed last night.

**What to do.** Restore one row per book, complete, to the same column contract every other row uses. Their Content Records exist and are the source for the row's values; where a value is genuinely absent from the record, name it rather than inventing it. **Set each row's `post_title` to the ruled title form** (the book's title, a colon, then "Summary and Key Ideas"), and check the value against the live page's own title rather than deriving it, since all three pages already carry the ruled form from Code's S107 pass.

**Read back:** the three rows present, the master's row count before and after, and each `post_title` quoted.

## Job two: the Handbook's missing source link

**`the-ultimate-life-coaching-handbook`.** Code tried to push this record at S107 and `article_body_update.py` refused it: no external link in the body. He then checked by hand rather than trusting the refusal, and found the record's body **contains no links at all, of any kind.**

**Chat told Code at S353 that this record and `the-skilled-helper` had both gained a source link. That was true of one of them only, and the error was Chat's.**

**What to do.** Add one external source link to the body, the same fix as the citation half of your S353 body pass. **The book is Kain Ramsay's own**, so the link points at a real listing for that book, not at an Achology.com product page. Then re-run `content_gate.py` on the record and report the result. This record is one of the two sitting below the type's bar, and the missing link is part of why.

## Job three: a new book note, A New Guide to Rational Living

**Commissioned by Kain in Code's S107 sitting, in his words:** "yes, A New Guide to Rational Living should get its own book note. Albert Ellis is one of my favourite authors who i discuss in most courses. From an honour perspective, he deserves it!"

**Why it is a separate book and not a duplicate.** The 1975 revision by Ellis and Harper is substantially rewritten, separately catalogued, and the edition most readers buy today. The existing note covers the 1961 original. The 1961 page had been carrying the 1975 cover for months; that is now fixed, which is how the gap was found.

**The four things Chat has already settled, so you do not have to ask:**

- **Slug:** `a-new-guide-to-rational-living`.
- **Focus keyword:** `a new guide to rational living`, the book's own title, per `RULING__The_Book_Note_Keyword_Is_The_Books_Title_S349`. **Claim it in the register deliberately before drafting.** It does not collide with the 1961 note's `a guide to rational living`, but the two titles compete for the same searches, so the claim is made rather than discovered at import.
- **Voice:** Benjamin Lockwood, as every book note.
- **The cross-link, ruled by Chat:** **both ways, one sentence each.** The new note names the 1961 original as the book that started it. **The 1961 note gains one sentence naming the 1975 revision as the edition most readers buy today.** Two pages this close together with no line between them is how a reader ends up on the wrong one. Write both sentences; the 1961 record is an edit to a live page's record, so name it clearly in your DONE file so Code knows to push it.

**What to produce.** The full book note record to the standard type spec, plus its master row, plus the one-sentence edit to the 1961 record. Print `GATE: PASS` on the new record before you call it done.

---

OWED BACK: one DONE file covering all three jobs, with the master backup checksum, the three restored rows read back, the Handbook's gate result, and `GATE: PASS` on the new Ellis record. Then Code builds the page.

*No em or en dashes in this file; checked before writing.*
