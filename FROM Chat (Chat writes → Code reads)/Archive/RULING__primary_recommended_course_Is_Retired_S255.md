# RULING: `primary_recommended_course` is retired, plus one question only you can answer

**From:** Claude Chat, S255. **Date:** 2026-08-10.
**Companion to:** `ANSWERS__Everything_You_Were_Waiting_On_S255.md`, written the same session.
**Correction, said plainly:** that file's section 7 told you two S255 files were already waiting for you here. They were not. The rulings had been made and written into the DSRDs, but the channel note carrying them to you was never written. This is that note, and it carries both items. Nothing else was missing.

## 1. The ruling: the field is retired

Kain ruled at S255, in his words, kill the field and let the tags choose. `primary_recommended_course` is retired outright.

**Why it goes rather than gets fixed.** It was never populated on a single one of the 620 Book Note Master rows, so nothing has ever depended on it. DSRD 1 section 5.7 now fills every course card on a book note from the row's own tags, which is the job the field was invented for and predates. Two mechanisms for one outcome is the drift the source-of-truth rule exists to stop, and this one had no data behind it to defend.

**Where it is now recorded**, all read back after writing:

- DSRD 2 section 1.6: the dual-course paragraph replaced. All three cards fill from section 5.7, no course is hand-picked for a book note.
- DSRD 2 section 3.1, the fifth body section: names the course section 5.7 puts in card one, derived from the row's tags at draft time rather than chosen.
- DSRD 2 section 6.1: the field line removed from the import mapping.
- DSRD 2 section 6.4: the retirement recorded with its reason, so it is not reinvented.
- DSRD 9 section 32.9 item 4: marked superseded, since it recorded card one as editorially chosen.
- DSRD 10 section 8, the Book Notes ACF table: marked **Retired S255**.

**What that means on your side, and it is small.** Remove the field from the ACF Local JSON, and remove any template line that reads it. Nothing renders from it today, so nothing should change on any page: if something does change, that is a finding worth a note back rather than a fix.

The column also comes out of the Book Note Master before import and is mapped nowhere. That half is Chat's, not yours.

## 2. The question, and it is read only

**What is the real ACF field name behind the Amazon link on a book note?**

DSRD 3 section 2.3 still names it `amazon_genius_link_url`, which is a name from the Geni.us plan retired at S231 and replaced by Amazon OneLink. DSRD 2 section 5.1 is clear that the field now holds the plain Amazon product URL with no wrapper, but the field's actual name in the theme is a fact only you hold.

Tell me the name as it exists in the field group, and whether any template still refers to it by the geni.us name. Chat corrects DSRD 3 to match the build, since the build is the authority. No change to the theme is being asked for here.

## 3. One thing that closed itself

The article-page course card count is no longer a question. DSRD 2 section 1.6 said two cards at desktop and DSRD 1 section 3.4 said three; the built page carries three, so DSRD 2 was the stale one and has been corrected to three. Nothing needed from you.

*No em or en dashes in this file; checked before writing.*
