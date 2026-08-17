# BRIEF: one copy change on the Policies index Code of Ethics card

**From:** Claude Chat, S251. **Date:** 2026-08-06.
**Closes:** the one open copy fail in `RECORD__Policies_index.md`, DSRD 6 section 1.
**Authority:** Kain, in session, S251. He chose the wording himself.
**Page:** https://achologytest.com/policies/

## The change

On the Policies index, the Code of Ethics card description.

**From:**

```
The expected level of character and behaviour that every practising Achologist pledges to uphold.
```

**To:**

```
The expected level of character and behaviour that every practising Achology member pledges to uphold.
```

One word replaced: `Achologist` becomes `Achology member`. Nothing else on the card,
the sentence or the page changes.

## Why

DSRD 6 section 1 names "Achologist" among the terms that must be identified at first
use. The card never identifies it, so a reader arriving cold from a search result is
left holding a word they cannot fill in. That is precisely what the front-door rule
exists to stop. The replacement carries the same meaning and needs no explaining,
which removes the need to identify the term rather than adding an explanation the
card has no room for.

## Acceptance

1. The sentence on the rendered live page reads exactly as written above, verified by
   character comparison against this brief rather than by reading it back.
2. `page_gate` re-run on /policies/ and the DSRD 6 section 1 row moves from FAIL to
   PASS in that page's record.
3. Dash check clean.

## Scope note

Check whether the same sentence is authored anywhere else before changing it. The
Code of Ethics card may share a renderer with the policy family, and the collapse
pass found several block families with more copies than expected. If the string
appears in more than one place, change every instance and say so; if it appears in a
shared renderer, change it once there. Do not change the word "Achologist" anywhere
else on the site in this pass: other pages may identify it properly, and each is its
own turn on the walk.

*No em or en dashes in this file; checked before writing.*
