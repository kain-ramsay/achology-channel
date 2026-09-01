# RULING: the seven legal pages take the 880 column, and the 620 one is deleted

**From:** Claude Code, Session 091. **Date:** 1 September 2026.
**Authority:** Kain, in session, on the rendered comparison.
**Shipped:** theme v0.130.0 then v0.131.0, deployed, all three deploy proofs
current.
**Closes:** the one Code item in `RULING__The_880_Width_Is_Written_Into_DSRD_9_
And_DSRD_7_S312`.
**Filed under:** Harness Rule 14.

---

## The ruling, in his words

**"Shall the seven legal pages move to the wide column, yes please"**

## He was shown it before he ruled, which was his own S085 instruction

My S085 ruling said one policy page is shown to him at 880 on the rendered page
before all seven move. That ran: Privacy came out of the prose list for one
sitting and rendered at 880, the other six stayed at 620, and both were opened
in Safari beside the Manifesto, which was already at 880 on writing he had
approved.

**He asked what the wide column actually was**, in those words, and was given
it plainly: it is the width the rest of the site already uses, the narrow one
is about two thirds of it and exists only on these seven, and what changes is
how far the eye travels before dropping to the next line.

**The cost was measured on the rendered pages and put to him, not hidden.**

    880 column   87 characters to a line
    620 column   67 characters to a line
    comfortable  45 to 75

So the seven legal pages now read slightly harder than they did, and match
every other page on the site. **He took that trade with the number in front of
him**, which is the point of showing rather than describing.

**One thing worth recording:** the 880 column measured 96 characters when he
rejected it at S062. It measures 87 now, because the body face moved to Mulish
since. The trade he accepted is a smaller one than the trade he refused, and he
was told so.

## What was deleted, and it is all of it

The slug list in `template-policy.php`, the class it applied, the 620
`max-width` and the 1.75 line height in `policies.css`. **`policy-page--prose`
does not exist anywhere on the site now.** Deleted rather than left unused: an
orphan rule is a thing somebody re-applies.

**Two comments were corrected rather than left pointing at deleted code.** The
S062 record in `policies.css` keeps its reasoning, because it is a real
measurement and the reason this is a genuine trade rather than a tidy-up, and
now says the rules it describes are gone. `knowledge-hub.css` cited that
selector as the pattern it copied; it no longer does. The Hub's own 1.75 is
Kain's S081 ruling on the rendered article and is untouched.

## The S062 lesson is kept, and it is not about this class

That slug list existed because the first build applied the narrow column to
every page on the template, sweeping in the Code of Ethics, the Manifesto and
the Founders' Letter: three finished pages he had already approved, changed
without being asked and shipped before he could refuse.

**The rule that came out of it outlives the class and is written into both
files as surviving this deletion:** a ruling covers what it names, and a
template that happens to serve other pages is never a reason to widen it.

**Those three pages were verified unchanged after this deploy**, because
sweeping them by accident is the exact fault the list was built to prevent.
They never carried the class, so they were already at 880.

## Verified

All ten rendered pages read after deploy: the seven legal pages carry
`policy-page` and no prose class; Terms measures 880 with 87 characters to a
line, where it measured 620 and 67 before; the Manifesto, Code of Ethics and
Founders' Letter are unchanged. Every theme asset served 200 at ver=0.131.0.

## What is asked of Chat

1. Nothing owed. DSRD 7 section 4 and DSRD 9 sections 25 and 27 already say
   880, so the build has caught up with the documents rather than the other
   way round.
2. **Worth noting in the record:** the 620 column is now gone from the code as
   well as from the documents, so the superseded rows kept beneath those
   tables describe nothing that still exists anywhere.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
