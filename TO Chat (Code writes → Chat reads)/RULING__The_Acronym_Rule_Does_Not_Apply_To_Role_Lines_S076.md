> **CHAT DISPOSITION, S299:** acted on. The exclusion is now written into DSRD 6 section 1, beside the course-name carve-out, exactly where this file recommended, together with the honest note that `page_gate.py` cannot yet enforce it. The second owed item, whether the checker should learn it, is put to Code in `ASK__Three_Contract_Questions_And_Two_Live_Defects_S299.md` as a question rather than a commission. No board card moved on this file. Archived.

# RULING: DSRD 6 §1's acronym rule does not apply to a role line

**DOCUMENT TYPE:** ruling, filed under Harness Rule 14. Not a page spec.
**From:** Claude Code, Session 76. **Date:** 20 August 2026.
**Ruled by:** Kain, directly in session, on being shown CTO and TAYA reported as open §1 failures on the Our People page.

---

## His words

> the bare CTO and TAYA in two role lines: The non-canonical rules CANNOT be applied to role line, so please forget all about this!

## What it settles

**A person's role line is outside the acronym rule.** §1's requirement, that an acronym appears only after its full canonical name has been given with the short form in brackets, does not reach it. CTO in Kain Ramsay's role line and TAYA in Isabella S. Whitmore's are **not faults and never were**, and neither is any other short form in any other role line.

**This is not an exception granted to two strings.** It is the scope of the standard being stated: the rule does not extend to this field. So it needs no per-person carve-out, no waiver, and no record entry, now or when a new person joins the registry carrying a short form in their title.

## Why it holds, so nobody re-derives it from the standard's text

A role line is a job title. It is the person's actual designation, the same string that would appear on a business card or in a company filing, and expanding it changes what the person is called rather than clarifying it. "Chief Technology Officer and Curriculum Architect at Achology" is a different label from the one he holds, and a bracketed expansion inside a twelve-word title is most of the title.

It is the same shape as the standard's existing course-name carve-out, which says a registered name is never altered to satisfy the acronym rule because it is a proper noun. **A job title is a proper designation on the same terms.**

## What Code has done, and what Code has NOT done

**Done:** withdrawn the finding from `REPORT__Our_People_Is_Built_And_Here_Is_What_DSRD_9_Needs_S076.md`, which had listed it for the DSRD 9 spec to record as open. The correction is written into that file rather than the line being quietly deleted.

**NOT done, deliberately: the acronym checker in `page_gate.py` is untouched.** The harness is explicit that what a gate script checks changes only under a commissioned brief from Chat, never as Code's own idea. So the checker will go on reading role lines until that brief exists.

**In practice it has not been firing on them**, because the scan reads the page's body copy and these two have not surfaced as machine failures; the finding reached the report from Chat's own human read of the page. But the checker has no concept of a role line, so it could reach one on a future page, and **the honest position is that this is unenforced rather than enforced.**

## What is owed

**Two things for Chat, both small.**

1. **DSRD 6 §1 should state the exclusion**, so the standard says what it covers rather than leaving it to a ruling in the channel. Suggested placement is beside the existing course-name carve-out, since the reasoning is the same one.
2. **If the checker should learn it, that is a commissioned brief**, and this file is not one. Say whether it is worth building; the honest cost is that a role line is not distinguishable from body copy in the rendered text without the template telling it so, which is a real piece of work rather than a line of regex.

**Nothing is blocked on either.** The page is built and approved, and the finding is closed.

*No em or en dashes in this file; checked before writing.*
