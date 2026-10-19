**Needs from Code (factory session): add one gate check. A page body carrying a lecture number or code fails, on every kind of page. Then list the records that fail it now.**

# RULING: no lecture number on any page, checked by the gate (Kain, S433, 20 October 2026)

Kain found a quote page whose body said "This line comes from lecture 001-056". His ruling, given more than once and restated tonight: a page never carries a lecture number or code. On quote pages the words lecture, lesson and recording already stay out of the body (Kain, S420; house book Part J and Part 17.5). The house book now carries the number rule for every page in Part P (Version 3, S433).

## The check
- **Fail** any page body (the record's `## Body` section, and every field that prints on the page) that matches a lecture code: three digits, a hyphen, three digits, for example `\b\d{3}-\d{3}\b`. A quote ID such as `CQ001-121-1` is never in the body, so it is not caught. If a real year range or phone number ever trips the check, list it rather than exempting it silently.
- Keep the existing quote page line for the words lecture, lesson and recording as it is.
- Add a test for each: one record that passes and one that fails.

## The count
Chat counted 71 records whose body carries a lecture code on 20 October 2026: 54 instructor articles, 7 workbooks, 6 quote pages and 4 hub question articles. Change nothing in them. They are rewritten through the newsroom, not patched. Report the gate's own count, so the two can be compared.

OWED BACK: one line when the check and its tests are in, with the gate's count.

*No em or en dashes in this file; checked before writing.*
