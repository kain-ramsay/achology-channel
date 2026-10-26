Needs nothing from its reader: a ship record, filed straight into the Archive.

# NOTE: ship 0.707.548, a quicker card arrival on every Knowledge Hub wall, behind a switch (Code S183, theme main session, 26 October 2026)

**What changed.** kh-subject.js section 5 and kh-subject.css (Rise in turn): with `?arrive=quick` on the address, a wall's cards start the moment they touch the screen (rootMargin 0, threshold 0, was -8% and 0.12), the stagger stops after the fourth card (0.05 s steps, was 0.07 s with no cap), and the fade and rise take 0.35 s (was 0.6 s). Without the switch nothing changes. Checked in WebKit on /learn/: the quick wall carries bx-arrive--quick and a waiting card's fade reads 0.35 s. Commit 10cba60c; server, local and zip agree.

**Why.** Kain, S183, signing off the front page's look: "a lot of the cards are really quite slow in loading." The kh-front-page session measured it in WebKit: every picture had downloaded 1 to 10 s before its card came into view; the wait is the arrival effect (a typical card fully there 1.2 s after reaching the screen, the slowest 2.5 s).

**What Chat needs to do.** Nothing yet. Kain compares the two in one Safari page; his pick becomes the default on every Hub wall and the switch is removed, with a RULING then (it amends BRIEF__Rise_In_Turn_On_Every_Knowledge_Hub_Wall_S440's timings).

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
