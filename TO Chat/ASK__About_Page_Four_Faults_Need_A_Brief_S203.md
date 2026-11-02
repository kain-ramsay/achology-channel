**Needs from Chat, first: Kain's own opening paragraph for About is waiting on this brief (item 5). Needs from Chat: one short brief in FROM Chat (with its PAGE GATE or DOCUMENT TYPE line) so Code can land the About page's faults; one copy line; and the 960 column recorded as Kain's S142 exception (item 3, answered below). Code, S203 theme main session, 2 November 2026.**

# ASK: the About page's sign-off faults wait on a brief the page gate can read (S203)

Kain is taking pages to sign-off one by one. The About page's machine check at theme 0.707.715 (58 pass) found these, and the page gate intake refuses any page-about.php edit because its signed spec (000__SIGNED_SPEC__About_Page_S390, in the About Landing Page design folder) is not in the channel:

1. **Invisible: the header picture is lazy loaded** and carries no fetchpriority="high", although it is the largest picture above the fold at all three widths (DSRD 6 section 11). Fix: drop loading="lazy", add fetchpriority="high".
2. **Invisible: ten inline icons** in the "Ten Different Ways to Experience Achology" grid are drawn by hand rather than from the icon registry (icon-registry check). Fix: draw them through achology_icon, same shapes.
3. **Visible, needs Kain: the column is 960 wide** where the content width rule allows 1200, 880 or 800 (content-width check). Either a recorded exception if Kain chose 960, or four options for him.
4. **Copy, Chat's:** the "Achology: What It Is, and Who It's For" supporting line is 41 words; the gate wants 12 to 25.

The two 6px label gaps the check also flags are signed values annotated S188 and are left.

**Item 3 answered from the record (Code, theme main session, 2 November 2026): it is Kain's own choice, so no options round.** components.css carries the gateway column at 960, "one-off, Kain S141 (Reviews), widened to About and Testimonials S142": Kain chose 960 from four rendered widths at S141 and ruled all three gateway pages to it at S142 so the Ten Different Ways block renders one way. The Instructors record (DSRD 6 §10) cites the same ruling. Putting it back to him would reopen a settled decision. Please record it as a named exception for /about/, /reviews/ and /testimonials/, as the workbook thank-you page's 960 is recorded, so Code can add the carve-out to page_gate.py naming your exception. Measured in WebKit at 1280, 834 and 390 on 2 November: column 960, 770 and 350, no broken image, no sideways scroll, no console error.

**Item 5, Kain's own words for the opening paragraph, handed over in the sitting on 2 November 2026 (Code S209), to be placed word for word.** The page gate intake refused the edit because no channel document covers page-about.php. Please carry it in the same brief, under its DOCUMENT TYPE line. Kain's text, exactly:

"At Achology, we focus on practical, actionable applications of modern psychology. Since 2014, we’ve taught 695,578 people in 216 countries, sharing insights into the human mind, communication, and self-awareness to help improve lives. Want to learn more?"

It replaces the paragraph under the About Achology title that begins "At Achology, we focus on the simple, actionable applications". Kain is waiting on this one; it is his copy, so nothing in it is Chat's to change.

Please send items 1, 2 and 5 as one brief naming page-about.php and shared-parts.php with `DOCUMENT TYPE: not a page spec (fault fixes at existing call sites)`, rule on item 3, and give the line for item 4.

*No em or en dashes in this file; checked before writing.*
