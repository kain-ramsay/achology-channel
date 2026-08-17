# QUESTION: people.css has three 640px stack points, and DSRD 7 §4.5 names only two exceptions site-wide

**From:** Claude Code, S049. **Date:** 2026-08-06. **Status: waiting on ruling. Nothing changed.**
**Blocks:** `css_gate` on `people.css`, and therefore a clean CSS gate on the Our People record and the ten profile records after it.

## What the document says

DSRD 7 §4.5, read from the canonical file this session:

> "Breakpoints are §4.1's boundaries only (768 and 1024, plus their max-width forms 767, 767.98, 1023 and 1023.98), plus one named mechanism boundary: 1040px, the inset-panel outdent point (§4.4). Any other media-query width is a defect unless annotated as an approved stack-point exception. Two such exceptions exist as of S223 and are to be annotated in place: the policies.css table stack at 640px and the about.css phone header stack at 599.98px."

Two exist. `people.css` has three more, and they are not among them.

## What they are

All three are stack points of exactly the kind §4.5 contemplates, not drift:

```
line  84  @media (max-width: 640px)   .ap-hero              the profile hero stacks and centres
line 177  @media (max-width: 640px)   .pp-card              the people card wraps
line 219  @media (max-width: 640px)   .author-card__line    the author line stops truncating
```

It is the same 640 the policies table stack already uses and which Kain has already approved once.

## Why I have not annotated them

Because annotating one is the act of approving it. §4.5's own words are "annotated as an **approved** stack-point exception", and the approval is Kain's, not mine. Writing that comment myself would manufacture the approval and leave three lines reading as though he had ruled on something he has never seen. Under Rule 5 this stops here.

Moving them to 767.98 is not a neutral alternative either: it changes where three layouts stack, which is visible on the profile pages, and visible changes are his.

## The question, in one line

**Do these three join §4.5's named exceptions, or do they move to 767.98?**

My reading, offered and not acted on: they join. 640 is already an approved stack point in this system, all three uses are genuine stack behaviour rather than arbitrary numbers, and moving them would change three rendered layouts to satisfy a rule whose own mechanism exists to accommodate this case. If that is right, §4.5's sentence needs its count changed from two to five with the three lines named, and I will write the in-place annotations quoting the amended sentence.

## What it is holding up

`people.css` fails `css_gate` on these three lines and nothing else. It failed on them before this session and before any change of mine; I found it while walking About, which loads this stylesheet. Until it is ruled, the Our People record and the ten profile records each have to carry a CSS gate that fails on lines nobody has ruled on, which makes every one of those records read worse than the pages are.

*No em or en dashes in this file; checked before writing.*
