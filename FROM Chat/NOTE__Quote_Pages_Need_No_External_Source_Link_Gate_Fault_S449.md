**For Code, factory session. What this needs:** one change to the content gate's quote page entry, with its acceptance test. It does not hold any import.

# NOTE (Chat, S449): the gate asks quote pages for an outside source link that their card forbids

**The fault.** The content gate fails 91 of the 104 round one quote article drafts on "external link to the source present: 0 found". The quote card in 17 Packs (The Quote Article Pack) says the source link in the Book is the book's own note, or the course named in full, as its one link, and that "no outside thinker [is] brought in to prove the idea". So a quote page that follows its card fails the gate. The signed resisting change eight pass this line only because each happens to credit a study.

**The fix.** In `content_gate_standards.json`'s quote page entry, the source link line passes when the Book carries the book's note link or the course's full name link. An outside link stays allowed, once, for a credited study. Add an acceptance case: one round one draft with no study must pass, and a page with no source link of either kind must still fail.

**Also done by Chat today, so you know.** The 104 round one quote phrases in `KEYWORD_REGISTER.csv` now sit under their new `post_name` and address (session column "S449 address move"). No row was added or removed, and no clash was found. The register line now passes on the drafts.

OWED BACK: the gate change and its test, named in your next factory report.

*No em or en dashes in this file; checked before writing.*
