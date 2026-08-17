# QUESTION: how many places does the pale grey supporting line actually affect?

**DOCUMENT TYPE:** not a page spec. A read-only question. Nothing here commissions any change, and nothing is to be swept.
**From:** Claude Chat, Session 268. **Date:** 2026-08-12.
**Why it is being asked:** found while building a render for Kain this session. Contrast was measured rather than assumed, and one pair failed.

## The finding

The **supporting line beneath a section heading** is specified as mid grey `#8A9199`. Measured on white, it is **3.19:1**, which is below the AA threshold of 4.5 for text at that size.

**This is not a new standard being applied to old work. It is two of our own documents disagreeing, and the pale one winning by accident.**

- The section header pattern (DSRD 9 §20.7, and every section that reuses it, including §22.8 and §22.10 on the article page) specifies the subheading in mid grey.
- DSRD 7 §1.1, the text colour roles table, says mid grey is **fine print**: breadcrumb separators, footer fine print, and single-line text carrying no meaning a reader needs. It says in its own words that the colour is never used for anything a reader needs.

A supporting line under a heading is read. So by DSRD 7 §1.1's own rule it should be soft grey `#5E6B75`, which measures **4.97:1** on white and passes.

**There is precedent and it is exactly this.** The S042 component audit walked all 46 uses of `#8A9199` across the theme and corrected the 8 that carried interactive text or a headline, to `#5E6B75`, at v0.21.7 with Kain's approval. The section-header supporting line was not among the 8. It looks like a miss rather than a decision, but that is an inference and Kain rules it, not me.

## What is being asked

**Counts, not opinions, and nothing changed.**

1. **How many places does this actually affect?** Every element on the live site rendering a section-header supporting line in `#8A9199`. Report as: how many distinct CSS rules, how many templates, and how many live pages.
2. **Is it one rule or many?** If the whole thing is one declaration in the components stylesheet, this is a one-line change. If it has been copied into page stylesheets, say how many copies and where.
3. **What else would move if that one declaration changed?** Any other element inheriting from the same selector that is genuinely fine print and should stay pale.
4. **Are there other `#8A9199` uses that are read rather than glanced at?** The S042 audit was a year of building ago. If a fresh count finds more of the same shape, name them. Do not fix them.
5. **Does the page gate already catch this?** If a contrast check exists among the machine checks, say why this passed. If it does not, say so plainly; that is useful either way.

## What happens next, so the scope is clear

**Nothing is swept.** This is a site-wide colour change, so Kain rules it by looking, not by reading a measurement. When your counts come back, he sees a real block rendered at real size in both colours, with the count under it, and says yes or no.

**Do not change the colour, do not update either specification, and do not add a gate check for it yet.** A gate against a rule Kain has not ruled on would fail on everything, which is the same mistake the typography gate was deliberately held back from.

*No em or en dashes in this file; checked before writing.*
