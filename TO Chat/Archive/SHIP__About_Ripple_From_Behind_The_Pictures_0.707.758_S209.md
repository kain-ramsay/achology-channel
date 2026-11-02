> ARCHIVED by Chat S454 (2 November 2026): a fault fix on the signed About page, for the record; nothing asked.

**Needs from Chat: nothing to decide; a fault fix on the signed About page, for your record. Code, S209 theme side session, 2 November 2026.**

# SHIP: the About ripple now spreads from behind the pictures (theme 0.707.757 and 0.707.758)

**What changed.** About's three round pictures (the header picture, the founders portrait and the closing panel portrait) ripple once each as they come into view (Kain, S209 polish board row 2). The ring was drawn on top of each picture, so it crossed the photograph; everywhere else on the site, the Help category band's ring is drawn behind its picture. Two lines in the About ripple block in help.css: the picture is raised above the ring (0.707.757), and the ring now starts on each photograph's own circle, measured at 2.8 to 3.1 percent in on all three image files, instead of 9 percent in, which was inside the photograph (0.707.758). With the ring behind but still starting at 9 percent, almost all of it was hidden, which is why the second line was needed.

**Why.** Kain asked why the founders picture's ripple drew over the picture when every other ripple comes from behind. It was a fault, not a design: the same animation, the same colour and timing, now in the same place as the Help band's.

**Checked in Playwright WebKit** on the build site at 1070, 1268 and 390 wide, with the ring held mid-spread: on all three pictures the ring shows only past the photograph's edge, through the aura and beneath its orange marks and the name label, and never over a face. On a phone the header picture still has no ring, as before. With reduced motion asked for, no ring shows at any width. css_gate PASS. Deployed from a clean copy of the commit; local, server and zip all report 0.707.758.

**Nothing else changed.** Timing, colour, spread and when each ring fires are as signed.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
