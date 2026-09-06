# REFUSAL: the S344 ruling cannot unblock a page edit, because it carries no DOCUMENT TYPE line

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Refused document:** `RULING_AND_REPLY__Book_Notes_Take_88_And_Every_S103_File_Answered_S344.md`
**Missing:** a PAGE GATE line at its foot, or a `**DOCUMENT TYPE:** ... Not a page spec.` line at its head.
**Board card:** the Codex theme audit.

---

## What happened, measured rather than predicted

Your S344 reply ruled that the two accessibility fixes are mine to make: `role="group"` with `aria-pressed` on the testimonial filter buttons in `page-testimonials.php`, and `inert` on the policy document reader in `template-policy.php`.

I declared the work with your ruling named in the SPEC field, as the wall asks, and attempted a one-line edit to `page-testimonials.php`. **H2 refused it**, in its own words:

> H2 PAGE GATE INTAKE: blocked. The spec governing this page carries no PAGE GATE line at its foot. (A document with no DOCUMENT TYPE line is treated as a page spec, ruled by Kain S266: forgetting to declare gets you refused, never waved through.)

So the ruling written to unblock page edits cannot unblock one, because the tripwire reads the document it points at and finds neither of the two things that would let it pass. It is exactly the S266 case that made you add type lines to your own documents, and this file simply has not got one.

**The fix is one line in your file, at its head, and then all of this moves.** Something like the one on `NOTE__Prepare_Reviews_Page_Two_Rulings_For_Safari_Sitting_S278.md`: `**DOCUMENT TYPE:** ruling and reply. Not a page spec.`

This is not mine to fix. The wall says so directly, and so does Rule 8: I never edit your documents.

## What is waiting on that one line

**The two accessibility fixes you ruled mine.** Both are page-template edits and both are refused for this reason.

**A third, which Kain asked for in the sitting tonight and which I could not start.** He asked whether the "Explore and Experience Achology for Yourself" block is genuinely one shared thing across About, Reviews and Testimonials. Measured on the three live pages: the block, its ten cards and their wording all come from one function and one list, and the rendered HTML is identical character for character except for the heading's internal id. But **the heading and the lead line are typed out separately in each of the three page files**, three copies of the same two sentences, so a change to one would silently diverge from the other two. He asked for them to come from the one place, and for the Testimonials block's id, which currently reads `about-grid-title`, to be corrected to its own page. Both are page-file edits.

## The wider question your ruling raised, and my answer to it

You asked me to write your rule into my harness on Rule 8's terms, and named the test yourself: the rendered page's text content and its screenshot at the three widths are byte-identical before and after, and only attributes, roles or focus behaviour changed.

**That test is good and I would widen it by one word.** As written it says "an accessibility correction". The heading refactor above changes no wording, no appearance, and not even an attribute; it changes only where a string is read from, and it passes your test more cleanly than the cases you had in mind, yet it is not an accessibility correction and so is not covered. I suggest the rule keys on the test rather than on the motive: **a change that alters no wording and no appearance needs no signed spec, whatever it was made for.**

I have not written anything into the harness. The harness is yours (Rule 8), and the growth governor asks what leaves as this enters, which is your call and Kain's, not mine.

---

OWED BACK: the DOCUMENT TYPE line on the S344 file, which unblocks three pieces of work at once. And your word on whether the rule keys on the test or on the motive.

*No em or en dashes in this file; checked before writing.*
