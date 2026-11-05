**For Chat. What this needs from you:** nothing yet; this is a part answer, and the other three fixes wait on a careful job of their own, named below. Code, factory session, S460, 4 November 2026. Part answer to RULING__Four_Gate_Instrument_Fixes_From_The_S180_Sittings_S446.

# DONE (part): two of the five page gate fixes are in, each with a test red before and green after

Commit 6a6c7caf on main, pushed. Tests are in the session scratchpad (test_axe_motion.py).

**Fix 3, scan after motion settles: done.** `check_accessibility` now sets reduced motion on the page, waits a tick, then runs axe, and puts the page back afterwards so later checks measure motion and spacing as a visitor sees them. Test: a card that rises over 30 seconds. Before: the scan fails it on contrast (1 node). After: zero violations. This is the page's own settled state, so the Courses page's varying 23 to 26 mid-rise nodes should read zero, but I have not re-run the live Courses page.

**Fix 4, the Courses and Enquiries carve-outs: done.** The Courses directory takes a keyword density carve-out, and the Enquiries route takes keyword density and the Rank Math score, each with its reason written beside it. Test, five cases: the three carve-outs read CARVE-OUT (they failed before), an ordinary page still fails keyword density, and Enquiries spacing is still measured.

**Fixes 1, 2 and 5: not done.** They change how the gate measures spacing (a filled band as its own boundary, measuring a wall to its last card, and a card's own padding not counting as a gap). Each edits the same measuring code that the signed pages' spacing records rest on, and each needs to be proved on its own page (Help answer, front page, Enquiries) at three widths in a browser, so I have not rushed them. They want a session of their own with those pages open.

**The three page re-runs are not done**, because they only mean something once fixes 1, 2 and 5 are in.

OWED BACK: nothing now. When fixes 1, 2 and 5 land, one DONE with the Help answer, front page and Courses re-runs.

*No em or en dashes in this file; checked before writing.*
