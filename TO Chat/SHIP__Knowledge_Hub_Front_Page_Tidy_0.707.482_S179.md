For Chat: please note the front page tidy (stage 6) in DSRD 9 section 39.10; and put one site-wide line on Backlog: Code (below).

# SHIP: the Knowledge Hub front page tidy, 0.707.482 (Code, S179, theme)

Kain: "yeah, I'd like you to do the front page tidy up"; the five parts were named to him first.

What changed: kh-front.css loses every rule that matched nothing (the round 25 dark bar variants, the round 19 book panel, the panel's old heading strip, the hidden kind line, four unused keyframes and three unused registered properties); the panel's working names (z, z9, zf, y-az, zz) are one family, kfm, across kh-front.css, kh-front-setup.php, kh-front.js and learn-home.php; the old front page's subject cards and category pill strip (achology_kh_subject_card, achology_kh_category_pills, nothing called either) leave knowledge-hub-parts.php, and their rules (kh-home__*, kh-subject-grid, kh-subject-card) leave knowledge-hub.css; the .kh-pill rules stay (the lists' sort pills use them) and the .kh-search rules stay.

Proof: every element on /learn/ outside the wall (623) recorded before and after at 1280, 834 and 390 (position, size and sixteen computed properties): zero differences at every width. The alphabet lights its topics and the Spotlight rule holds under the new names. css_gate passed on kh-front.css. Local, server and zip agree.

Not done, and why: the front page loads policies.css, help.css and people.css because every page loads them as a chain (knowledge-hub.css depends on people.css, which depends on help.css, which depends on policies.css). The front page uses one rule from policies.css (the breadcrumb bar) and one from people.css (the learning path heading), and none from help.css. Unchaining them is a site-wide change, so it is a line for Backlog: Code, not a front page edit.

Reach: none; these were the front page's own leftovers.

OWED BACK: the Backlog line for the stylesheet chain.
