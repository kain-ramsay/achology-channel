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

## 2. `author_website_url` is deleted, and its slot points at Achology's own author page

It was written when Achology had no author pages. **There are now 51 author biographies live**, and the template already holds `author_slug`, which guards the link to that author's Achology hub.

So the external website link is removed rather than replaced. The reader is sent to Achology's own page about that author, which is a page we own, keep current and can improve, rather than an external site nobody checks.

**`author_website_url` comes out of the contract, out of `upload_contracts.json`, and out of the template.**

## The two checks, before anything is built

Both are yours, and neither is Kain's.

**Check one: does the Goodreads ISBN route still resolve?** Open three real ISBNs read from the master and report where each one lands. Goodreads retired its API in 2020, and the evidence Chat has for this route is developer forum posts rather than a current guarantee, so it is proved on the live site or it is not used. **If it does not resolve, stop and say so**; the fallback is that the Goodreads rating prints unlinked, exactly as today, and `goodreads_rating` stays as the only Goodreads field.

**Check two: how many of the master's rows carry an ISBN?** Read the count off `Book_Note_Master.xlsx` and report it. It decides how many book notes get the link at all, and a low number would change the answer.

**Report both before building either change.** Nothing here is urgent and nothing else waits on it.

---

OWED BACK: the two check results, in one file, before the contract or the template is touched.

*No em or en dashes in this file; checked before writing.*
