# COMMISSION: ISBN, Amazon URL and Book Cover Collection Run

**From:** Claude Chat, Session 250
**To:** Claude Code
**Date:** 2026-08-06
**Status:** Approved by Kain in session. This is a commission, not a question. Build it.
**Board card:** Amazon OneLink Install (affiliate localisation), In Progress. This commission is that card's Step 1.

---

## 1. Why this run exists

Every Book Note page needs two things Code does not yet have for most books: a working Amazon link for the "Buy on Amazon" button, and a real book cover image. The cover is REQUIRED on the Book Note page with no fallback (ruled S250, DSRD 8 section 20), so a book without a cover cannot publish.

The affiliate question is already settled and needs no work here. The site uses **Amazon OneLink**, installed once site-wide in the theme, which localises any plain Amazon link to the visitor's own store with the correct associate tag. There are therefore **no per-book affiliate links to create**. The Geni.us plan is retired (S231) and any `genius link` column inherited from older workbooks is dead data.

That leaves a pure data job, and one fact makes it tractable: for a printed book, **Amazon's product code (ASIN) is the ISBN-10**. So the Amazon URL can be derived from the ISBN with no Amazon account and no Amazon API. The same ISBN also fetches the cover image free from Open Library. One lookup closes both jobs.

## 2. The input file

`Book_Note_Master.xlsx`

Location: `006. Content Production Factory + COWORK/Book Notes | Source Bank + Master File/`

620 rows, one per book. Read the current column schema from the file itself and from its `Book_Note_Master__Read_Me_First.md`; do not assume columns from anything written here. Title and author are the lookup keys.

Do not hand-edit `Book_Note_Upload.csv`. It regenerates from the master.

## 3. What to build

One script, run once, over every row of the master.

**Per row:**

1. **Resolve the ISBN.** Look up the book by title and author. Try Open Library first, then Google Books as fallback. Both are free and need no key (Google Books allows keyless use at low rate; throttle rather than key it). Prefer a widely held English-language print edition, since that edition is the one Amazon most reliably carries.
2. **Derive the Amazon URL** from the ISBN-10 in the plain canonical form `https://www.amazon.com/dp/{ISBN10}`. Convert a 13-digit ISBN to its 10-digit form where only the 13 is available. No affiliate tag, no wrapper, no shortener: the tag is applied at runtime by OneLink.
3. **Verify the URL resolves** to a real product page before accepting it, with a polite request rate and retries on transient failures. A dead or redirected-to-search URL counts as a miss, not a pass.
4. **Download the cover image** from Open Library's cover endpoint using the same ISBN, at the largest size available. Save to a single new folder beside the master, one file per book, filename keyed to the book's existing slug column so the row and the file are unambiguously paired.
5. **Reject an unusable cover.** A placeholder, a blank, or an image below roughly 400px on its long edge counts as a miss, not a pass. The page renders the cover large, so a thumbnail is not fit for use.

## 4. What to write back

Add four columns to `Book_Note_Master.xlsx` (or fill them if the master already carries them):

| Column | Contents |
|---|---|
| `isbn` | The ISBN-10 used, or blank on a miss |
| `amazon_url` | The verified plain Amazon product URL, or blank on a miss |
| `cover_status` | `ok`, `missing`, `low_quality`, or `no_isbn` |
| `book_cover_image` | The saved cover filename, or blank on a miss |

Preserve every existing column and row order. Version the change inside the master's own Read Me sheet, and put the superseded file in the folder's Archive, per the one-master-one-filename rule.

## 5. What to return through TO Chat

1. **A misses list** as its own file: every row where `cover_status` is not `ok`, with title, author, slug, and which step failed. This is the hand-work list for Kain and Chat, so it must be readable, not a log dump.
2. **A one-screen summary:** rows processed, ISBNs resolved, Amazon URLs verified, covers saved, and the miss count broken down by `cover_status` value.
3. **Any column-contract consequence** you can see for the Book Note upload CSV, since `book_cover_image` is now a required field.

## 6. Scope boundary

This commission is the data run only. It does **not** include installing the OneLink script in the theme; that is Step 3 of the same board card and travels separately once the Amazon Associates dashboard configuration is done by Kain or Karen.

Also still outstanding from S233 and unrelated to this run: your click-by-click Amazon Associates dashboard steps for switching OneLink on across the UK, US and Canada programmes. Kain is waiting on those to do Step 2.

## 7. Definition of done

The master carries the four new columns filled for every row it could resolve, the cover folder holds one usable image per resolved book, and the misses list plus summary are in TO Chat for Kain and Chat to work by hand.
