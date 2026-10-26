Needs nothing from its reader: a ship record, filed straight into the Archive.

# NOTE: ship 0.707.554, Knowledge Hub walls stop freezing as their pictures arrive (Code S183, theme main session, 26 October 2026)

**What changed.** kh-subject.js, the one wall's layout (section 4): a wall remembers its last laying, keyed on its column count, column width, logo height and every card's span and height; when a picture arrives and no card's size has changed, it puts that laying back instead of running the thirty tries again. Rise in turn and every wall rule are unchanged. Commit 2868d7f3; it also carries the Manifesto side session's 20343b4f (its 0.707.553). Server, local and zip agree.

**Why.** Kain, S183, on the front page: the cards "drop in", "clunky", "slow", where last week they faded in smoothly. Measured in WebKit, logged out: the page froze as it scrolled (front page 12 freezes up to about a second; Personal Growth 22; Psychology 15), because every picture that arrived set off a fresh laying, and on a mixed wall that runs all thirty tries (rule 4 seldom reaches zero). The Articles wall, one kind, finished in one try and never froze. The regression came with the one wall (0.707.498, S180), which re-lays on each picture's arrival.

**Proof.** In the test browser, live against the fixed copy: front page at 1280, 12 freezes to 0; Personal Growth 22 to 0; Psychology 15 to 0; Wisdom for Life 24 to 0; Articles, Quotes and a topic page unchanged at 0. Cards in the same places at 1280 on every page; at 834 and 390 a few foot cards differ, as the live wall already differs from itself between visits (Personal Growth, live against live). Every foot level within 1 px once the rise has played. Live after the deploy: 0 freezes and no card told to arrive late on the front page and Personal Growth.

**Reach.** Every Knowledge Hub wall (the shared layout script).

**What Chat needs to do.** Nothing.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
