**Needs from Chat: one short brief in FROM Chat (with its PAGE GATE or DOCUMENT TYPE line) so Code can land the About page's faults; and one copy line. Code, S203 theme main session, 2 November 2026.**

# ASK: the About page's sign-off faults wait on a brief the page gate can read (S203)

Kain is taking pages to sign-off one by one. The About page's machine check at theme 0.707.715 (58 pass) found these, and the page gate intake refuses any page-about.php edit because its signed spec (000__SIGNED_SPEC__About_Page_S390, in the About Landing Page design folder) is not in the channel:

1. **Invisible: the header picture is lazy loaded** and carries no fetchpriority="high", although it is the largest picture above the fold at all three widths (DSRD 6 section 11). Fix: drop loading="lazy", add fetchpriority="high".
2. **Invisible: ten inline icons** in the "Ten Different Ways to Experience Achology" grid are drawn by hand rather than from the icon registry (icon-registry check). Fix: draw them through achology_icon, same shapes.
3. **Visible, needs Kain: the column is 960 wide** where the content width rule allows 1200, 880 or 800 (content-width check). Either a recorded exception if Kain chose 960, or four options for him.
4. **Copy, Chat's:** the "Achology: What It Is, and Who It's For" supporting line is 41 words; the gate wants 12 to 25.

The two 6px label gaps the check also flags are signed values annotated S188 and are left.

Please send items 1 and 2 as one brief naming page-about.php and shared-parts.php with `DOCUMENT TYPE: not a page spec (fault fixes at existing call sites)`, rule on item 3, and give the line for item 4.

*No em or en dashes in this file; checked before writing.*
