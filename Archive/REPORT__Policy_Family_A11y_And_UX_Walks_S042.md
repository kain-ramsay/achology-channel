# REPORT: the §7 and §8 walks across the seven policy pages, with six questions needing rulings

**From:** Claude Code, S042 (Code-side numbering; the session after your S233 status note). **Date:** 2026-07-29.
**Continues:** the seven RECORD__Policy_*.md files filed yesterday, whose §7 and §8 rows were "not verified". Both walks have now run and every record is updated in place: verdict line, §7 row, §8 row, and closing list.

## What ran

DSRD 6 §7 (the accessibility walk) and §8 (the ease-of-use walk) on all seven policy pages, on the live build site, at desktop and phone widths. §8's fresh-eyes rule is satisfied: yesterday's session built and swept the copy, this is a new session and I read each page cold. Instruments: the rendered pages' accessibility trees, computed styles and geometry, measured contrast ratios, keyboard reachability of every interactive element, a 200 percent zoom equivalent, 320px reflow, and full text reads. One honesty note: the browser pane here runs unpainted, so everything was verified by measurement on the rendered DOM rather than by eyeball; Kain's §11 item 5 look remains the human eye on these pages.

## The result in one line

All seven pages pass everything that is theirs. Every finding below lives in the shared template or in copy, none is a blocker, and none was fixed, because each needs either a ruling or the copy owner.

## The six questions, each needing a ruling

**1. The sticky header hides focused content (template, site-wide, a real §7 fail).** The header is sticky and the page declares no scroll offset, so anything the browser scrolls to the top edge lands underneath the header. A keyboard user tabbing backward up the page has their focused item hidden, which §7 forbids in terms: "with the focused item always visible, never hidden under the sticky header." The fix is one CSS declaration reserving the header's height at the top of the scroll, but it touches every page at once and no DSRD names the offset value, so under Rules 3 and 5 it needs a brief naming the value. My proposal: reserve the header height plus a small breathing space, applied in base.css.

**2. The footer's column headings lie to screen readers at desktop (template, site-wide).** The About, Achology Schools and Useful Links headings are buttons carrying an announced collapsed state for the phone accordion. At desktop the lists are permanently open and the buttons do nothing, but they still announce "button, collapsed". A screen reader user hears closed sections that are open, presses, and nothing happens. At phone width the accordion behaves correctly, announced state and all. Fix: at desktop the headings should stop being announced as collapsed interactive buttons. Needs a brief; it is one footer template shared site-wide.

**3. The desktop menu's announced state trails reality (template, site-wide, lower confidence).** The top navigation opens its panels on keyboard focus, which is right and matches what the Accessibility Statement promises, but the trigger's announced state read "closed" while the panel was open when I drove it synthetically. Worth one look and, if real, the same brief as item 2.

**4. The date line's grey against DSRD 7's own rule (policy family and any dated template).** "Last updated: 1 July 2026" renders in the fine-print grey, which measures about 3.2:1 on white. DSRD 7 §1's table says that grey "fails AA for reading" and is only for "single-line text carrying no meaning a reader needs", and its rule adds: "#8A9199 is never used for anything a reader needs." DSRD 6 §6 requires the date shown on policy pages. Is a policy's last-updated date something a reader needs? If yes, the line moves to a darker text colour; if no, it stands as compliant fine print. Your call, not mine.

**5. The Cookie Policy promises a control that does not exist (one page's copy against the build).** Section 4 tells the reader they can "reopen the cookie settings via the link in the site footer". There is no cookie banner and no footer settings link anywhere on the build site. Either the consent tooling is cutover work, in which case I record it as deferred alongside the canonical, or it is a gap to close now. Which?

**6. The public accessibility bar disagrees with the standard (one page against DSRD 6).** The Accessibility Statement names WCAG 2.1 AA as the site's bar and says we monitor 2.2. DSRD 6 §7 names WCAG 2.2 AA as the bar. The two should say the same thing; which one moves is yours and Kain's.

## Copy findings from the fresh read (the copy is yours and Kain's, so listed, not touched)

The dash sweep left a colon standing where a dash or hyphen once was, and in six places the sentence now stumbles:

- Privacy Policy §9: "for example through chat functions, direct messages, or contact exchanges: you do so independently"
- Privacy Policy §10: "such as cloud hosting, software, and technical support providers: may be located outside the UK"
- Terms §1: "Achology Transactions Ltd (ATL): Scottish company number SC697126: based in Glasgow, Scotland"
- Disclaimers §2: "a therapist: client, doctor: patient, counsellor: client, or similar professional relationship" (hyphenated pairs are meant, and hyphens are permitted)
- Trust Statement §1: "Learning, especially learning that involves psychology, ethics, identity, values, or human behaviour: will inevitably provoke thought"
- Trust Statement §2: "Achology, including all staff, contributors, facilitators, and management: accepts no responsibility"

Two cosmetic title notes: the rendered browser titles of Terms and Refunds capitalise "And". The Refund Policy and Cookie Policy otherwise read clean, and the Refund Policy's at-a-glance block is the best piece of self-evident writing in the family.

## What this unblocks

When your rulings on 1 to 4 land as briefs, the fixes are small and I can run them. The seven records now show every chapter runnable from here as run; each page waits only on Kain's tablet-and-phone look, the cutover lines, and the rulings above.

*No em or en dashes in this file; checked before writing.*
