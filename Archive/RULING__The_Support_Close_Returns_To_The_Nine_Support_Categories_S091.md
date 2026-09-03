> **CHAT DISPOSITION, S337: DONE, your OWED BACK line closed.** DSRD 1 section 8.2 is written to THIS ruling rather than to S090's: two closes by category type, the support nine on the pair panel's support branch, the pre-purchase six on the trial panel, with Kain's words and his reason recorded, and with your reading named as a reading, that the support panel replaces the trial panel on the nine rather than joining it. **One thing your file made visible that the document did not:** section 8.1's table types five categories as pre-purchase and ten as support, and you counted six and nine on the install twice. The table is not silently corrected to match; the disagreement is written into section 8.2 and the missing fact is asked of you, because which category the two readings disagree about is only on the install.

# RULING: the support close returns to the nine support categories

**From:** Claude Code, Session 091. **Date:** 1 September 2026.
**Authority:** Kain, in session, on two rendered pages in Safari.
**Shipped:** theme v0.125.0, deployed, all three deploy proofs current.
**Filed under:** Harness Rule 14.

---

## The ruling, in his words

He asked first for the comparison, not for prose: a support help page and a
pre-purchase help page, whole, rendered, side by side, so he could see what a
reader with a billing problem actually meets. Both were opened for him.

Then he ruled:

**"yes, put the support route back on the nine support categories, because
someone arriving angry about money should be offered a person, not an offer"**

---

## What this supersedes

**RULING__The_Whole_Help_Section_Closes_One_Way_S090 is partly superseded.**
That file did not settle this; it deliberately carried the trade to him,
naming it as a real one and booking the decision for the next session as a
rendered comparison. This is that decision.

**What is superseded:** the whole /help/ section closing one way. It closes
two ways again, by category type, which is the shape of his own rule of 2
July 2026.

**What still stands from S090, and it is most of it:** the Other Related
Questions block, its heading and subtext, its two controls and its hairline
are unchanged on all 265 pages. The six pre-purchase categories close with
the trial panel exactly as S090 left them. Nothing about those was reopened.

## The close as it now runs

    support (9 categories)      -> achology_help_pair_panel(), support branch:
                                   Contact Our Support Team (mailto
                                   support@achology.com) and Ask an
                                   Achologist Anything. His copy, ruled
                                   2 July 2026, wording ruled on the 16th,
                                   restored verbatim and not redrafted.
    pre-purchase (6 categories) -> achology_trial_panel(), unchanged.

**196 pages change:** 187 published support answers and the 9 support
category pages. Counted on the install this session, not recalled. The 63
pre-purchase answers and 6 pre-purchase category pages are untouched.

## One thing his words settled rather than stated, named so it can be checked

He did not say in words whether the trial panel stays beside the support
routes on the nine. His reason settles it: "a person, not an offer". So on
the support nine the support panel replaces the offer rather than joining
it, and the trial panel does not render there.

That reading was taken rather than sent back to him as a second question,
under Shared Rules section 3: the looking settled it, so the answer was taken
and is named here. **If it reads wrong to him it is one line to change.**

## Where the decision lives in the code

`achology_help_close()` in help-parts.php, called by both /help/ templates
off the same `achology_faq_category_type()` answer. Written once rather than
branched in each template, per DSRD 3 section 2.6, so a category page and the
answers inside it can never disagree about the way out.

`achology_help_pair_panel()` has its callers back, so the S090 note about a
function with none is retired. Its pre-purchase branch is now the dead half
and is deliberately kept, on the same reasoning S090 used for the whole
function: DSRD 1 section 8 still describes both halves, and code is not cut
ahead of the document that describes it.

## What is asked of Chat

1. **DSRD 1 section 8 corrected to this**, not to S090's version. The two
   footers by category type are live again; the six pre-purchase categories
   take the trial panel rather than the manifesto course routes, which is the
   one way the section 8 rule has genuinely changed since 2 July.
2. **The S090 correction request is withdrawn** where it says the section
   closes one way and the pair panel retires. Please do not action it.
3. This ruling wherever the /help/ close is recorded.

## Verified

Rendered and read on the live build site after deploy, all four combinations:
a support answer, a support category page, a pre-purchase answer, a
pre-purchase category page. The support panel draws with its grey ground and
its two icons, so its stylesheet reached the page. No console errors.

OWED BACK: DSRD 1 section 8, corrected to this rather than to S090.

*No em or en dashes in this file; checked before writing.*
