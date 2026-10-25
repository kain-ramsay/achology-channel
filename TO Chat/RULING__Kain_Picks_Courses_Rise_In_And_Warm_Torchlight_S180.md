NEEDS FROM CHAT: write Kain's S180 Courses pick into the Courses page's signed spec as an amendment; the build sheet is already updated and the prototype follows the deploy.

# RULING: Kain picks Courses Rise In and Warm Torchlight for the Courses page (S180)

**Kain's words**, in the S180 theme sitting, on four options shown to him on the real page at /courses/?courses-option=1 to 4 (relayed to this side session by the S180 main session): "I would like, both the courses rise in, I would like that, and the warm torchlight. Is that possible?" The main session answered yes. The options came from his S180 ask to "suggest if there's any improvements you would make to it to make it look even more, from a design perspective, even more visually spectacular".

**What is now built** (courses-directory.css section 7, courses-directory.js; not yet deployed, the main session deploys):
1. **Courses Rise In.** Whenever the list of courses changes (at load, a tick, a sort, Explore More), the cards on show rise 32 into place and fade in over 0.6s, one after another, 90 apart. The Knowledge Hub walls' Rise (DSRD 8 section 41) in spirit, here on the course grid.
2. **Warm Torchlight.** A soft light in the band's light orange (`--color-orange-footer`) follows the pointer across the fifteen answers, lighting the faces and the edges of the tiles near it; on a phone it sits where a finger touched. With no pointer every tile is exactly its signed ground and edge.
3. Both are off for anyone who asks their device for reduced motion.
4. Options 1 (Glowing Choices) and 3 (Slow Drift) are not taken, and the ?courses-option switch is removed whole.

**Checked** in WebKit at 1280, 834 and 390: the rise plays at load and on a tick at every width, the light follows the pointer (and a touch on a phone), and reduced motion stops both. With everything settled and no pointer, the page matches the page as it was, apart from a rounding step of one shade in 255 on the chosen tiles, which no eye can see. css_gate passes on courses-directory.css.

**Fold-back (Harness Rule 14).**
- **Build sheet updated:** BUILD_SHEET__Courses_Directory_Page.md in the Courses Directory Page design folder carries a Warm Torchlight row (section 2) and a Courses Rise In row (section 3). It also now carries the answer tiles as Kain chose them at S143, the fold-back the S393 amendment said would come at the next sitting.
- **Prototype:** the prototype is exported from the deployed page (export_page.py copies the page's own markup), so `PROTOTYPE__Courses_Directory_Page_S138.html`'s next version is written into the same folder as soon as the main session deploys this build. It will be named in a one-line note when it lands.

**For the spec:** an amendment to 000__SIGNED_SPEC__Courses_Directory_Page_S362.md recording the two picks, in Chat's words.

*No em or en dashes in this file; checked before writing.*
