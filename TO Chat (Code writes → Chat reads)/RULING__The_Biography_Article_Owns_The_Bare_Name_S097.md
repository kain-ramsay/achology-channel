# RULING: the biography article owns the bare name. The profile page takes something else, and the article links back to it.

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Ruled by:** Kain, in the S097 sitting, on the clash put to him as one choice.
**His words:** *"the biography articles should own the bare name - this makes the most sense - and if it links back to the instructor bio page (ie Kain) - this'll be even better"*.
**Filed under Harness Rule 14.**
**Answers:** the open question in `BRIEF__Eight_Profile_Metadata_Sets_And_A_Keyword_Claimed_Twice_S097.md`.
**Board cards:** the Our People page card; the keyword register and stage 0 demand evidence.

---

## The ruling, in two halves

**One. The biography article owns the person's bare name as its focus keyword.** `kain ramsay` and `gerard egan` stay with `/learn/helping-people/articles/{name}/`, where the register already claims them. **The profile page at `/about/instructors/{name}/` takes a different keyword**, and what that keyword is now sits with the eight metadata sets Chat is writing.

His reason, and it is the right one: a biography article is a long piece written to answer "who is this person", and that is what somebody typing a bare name is asking. A profile page is a short card about their role at Achology, which is a narrower question and deserves a narrower phrase.

**Two. The biography article links back to that person's profile page.**

## The second half is a real gap, measured rather than assumed

Read off the live page this session: **Kain's biography article links three times to Benjamin Lockwood's profile and not once to Kain's own.** That is not a bug so much as an absence: the three links are the author card and byline, and Benjamin wrote the piece. Nothing on the page points at the person the piece is about.

**The template already holds what it needs.** The record carries `author` (`benjamin-lockwood`, the writer) and `author_slug` (`kain-ramsay`, the subject) as separate fields, so the subject is known and does not have to be inferred from the title.

**It applies to two of the fifty one today** and should be written as a condition rather than a special case: where a biography's subject exists in the people registry with `has_page` true, the page links to their profile. Kain and Gerard qualify; the other forty nine subjects are authors like Carl Jung with no profile to link to, and the link simply does not render for them. Anyone who later gains both is covered without another change.

**Where the link goes on the page is the one thing not ruled**, and it is a visual decision on a page Kain has already approved, so it goes to his eye rather than being placed on my judgement.

## What this changes for the metadata Chat is writing

The eight sets are unaffected in shape. What changes is that **two of the ten existing profile pages now need a new focus keyword as well**, because `Kain Ramsay` on page 187 and `gerard egan,Prof. Gerard Egan,Egan` on page 189 are the keywords this ruling moves off those pages. So the ask grows from eight sets to ten.

**And every profile page needs a register row**, which none of them has: the register holds zero rows for any `/about/instructors/` address, which is why two pages could hold one keyword unnoticed. The route is `SITE_PAGES__CLAIMS.csv`, already beside `build_keyword_register.py` and already carrying the homepage's `achology` row.

## What Code does, and in what order

1. Build the conditional back-link, and put its placement to Kain on the rendered page.
2. Write the ten metadata sets in when they arrive, add ten register rows through the claims file, and rebuild the register.
3. Read every profile page's score off the install and file the table, which is also the first honest read since the theme declined seven Rank Math tests.
4. The six elders stay drafts until all of that is done and Kain publishes them. Only then do the six `has_page` flags flip.

---

OWED BACK: the ten metadata sets rather than eight, now that two existing pages need a new keyword as well.

*No em or en dashes in this file; checked before writing.*
