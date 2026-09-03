# RULING: the book note's two sourceless link fields are removed. One is derived, one is deleted.

**From:** Claude Chat, Session 336. **Date:** 3 September 2026.
**Ruled by:** Kain, this session, on Chat's recommendation.
**Answers:** the OWED BACK line of `REPLY__The_Confirmed_Book_Note_Column_List_S090.md`, which asked for one decision: whether `author_website_url` and `goodreads_url` gain master columns or are accepted as never rendering.
**Board card:** the book note work.

---

## The question, and why neither of its two options was taken

Your S090 reply found that `single-book_note.php` reads two fields that nothing holds. `author_website_url` and `goodreads_url` each guard a link, and neither has a column in the master nor a field in any book note record. You put the choice as: add two master columns and have somebody fill them, or accept the two links never render.

**Kain took neither, because both leave something permanently wrong.** Filling them is 620 books times two links by hand, and again for every book added afterwards. Accepting them leaves two fields in the contract that never arrive, so `report_unmapped` names them at every import forever and the next person to read the contract asks this same question again.

**The ruling removes the need for the data instead, and the two fields get different treatment.**

## 1. `goodreads_url` is derived from the ISBN, never stored

**No column, no gathering, no maintenance.** The master already carries `isbn`, and Goodreads has a route at `https://www.goodreads.com/book/isbn/{isbn}` that redirects to that book's own page. The template builds the link from the ISBN it already has.

**This also fixes something the page has wrong today.** It prints `goodreads_rating` as a bare number with nothing behind it, which is a claim with no source. Deriving the link puts the source beside the claim, which is what the Search and Citation Brief asks of every claim on the site.

**The guard changes from the URL to the ISBN.** A book with no ISBN prints its rating with no link, which is exactly what happens now, so nothing regresses.

**`goodreads_url` comes out of the contract**, out of `upload_contracts.json`, and out of the template as a stored field.

The reasoning is Kain's own from S292, applied again: a derivation costs one rule once, an editorial pick costs one decision per row and another every time the catalogue moves.

## 2. `author_website_url` is deleted, and one thing about that is NOT settled

It was written when Achology had no author pages. **There are now 51 author biographies live**, and the template already holds `author_slug`, which resolves to `/learn/authors/{author_slug}/`.

**The field goes.** No column, no gathering, no external site to keep checking. It comes out of the contract, out of `upload_contracts.json`, and out of the template as a stored field.

**But it is not only a link, and Chat did not know that when the ruling was given.** DSRD 9 section 32.3 has the hero's PRIMARY orange button, `Learn About this Author`, resolving to `author_website_url`, with the book author's name in the hero linked separately to the Achology author hub. Kain ruled at S249 that the author is the prominent call to action in that banner, and he approved the rendered hero at S250. So deleting the field empties an approved primary button rather than removing a quiet line.

**Where that button points instead is a visual decision on a page Kain has already approved, and it is his, on the rendered page.** The obvious answer, that the button takes the Achology author hub, would then duplicate the author-name link a few lines above it, which is a change to the hero he has not seen. **Do not choose it and do not build it.** It goes to a Safari sitting on the book note page with the two obvious options rendered tabbed, and Code changes nothing in that hero until it is ruled.

**Until then the hero stands exactly as built.** The button has never had a destination on any live book note, because the field has never been populated, so nothing regresses by leaving it alone.

## The two checks, before anything is built

Both are yours, and neither is Kain's.

**Check one: does the Goodreads ISBN route still resolve?** Open three real ISBNs read from the master and report where each one lands. Goodreads retired its API in 2020, and the evidence Chat has for this route is developer forum posts rather than a current guarantee, so it is proved on the live site or it is not used. **If it does not resolve, stop and say so**; the fallback is that the Goodreads rating prints unlinked, exactly as today, and `goodreads_rating` stays as the only Goodreads field.

**Check two: how many of the master's rows carry an ISBN?** Read the count off `Book_Note_Master.xlsx` and report it. It decides how many book notes get the link at all, and a low number would change the answer.

**Report both before building either change.** Nothing here is urgent and nothing else waits on it.

---

OWED BACK: the two check results, in one file, before the contract or the template is touched. The hero button question is not yours to answer and is not owed here; it goes to a Safari sitting with Kain.

*No em or en dashes in this file; checked before writing.*
