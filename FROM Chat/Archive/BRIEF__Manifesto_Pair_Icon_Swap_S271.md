# BRIEF: Manifesto closing pair, Browse All card takes book-open

**DOCUMENT TYPE:** not a page spec.

**From:** Claude Chat, Session 271. **Approved:** Kain, S271, ruled on rendered options per standing rule 16.
**Amended:** Session 272, 13 August 2026, answering `REFUSAL__Manifesto_Icon_Swap_Brief_Has_No_PAGE_GATE_Line_S057.md`. The only change is the DOCUMENT TYPE declaration above: this is a one-value build change carrying a ruling Kain already made on rendered options and already recorded in DSRD 7 §5.2.3, not a page specification, so it carries no PAGE GATE foot. The manifesto page's own governing spec predates S264 and is exempt by date. Nothing else in this brief has changed.
**Size:** one icon key on one page.

## Context, standalone

At your S054 sweep the manifesto page's closing pair panel (Ready to Start Training as an Achologist?) ended up with `graduation-cap` on both cards: the ruled courses-glyph flip put the cap on Browse All of Our Courses, and Explore Our Seven Schools already wore it. You flagged the collision to Chat rather than deciding it (your comment block in policies-content/manifesto.php records this).

Kain has now ruled it, on side-by-side rendered options: **the Browse All of Our Courses card takes `book-open`.** Same distinctness ground as the 404 Courses door exception. The Seven Schools card keeps `graduation-cap`.

**Scope guard:** the Code of Ethics page's pair is untouched. Its Browse All card keeps `graduation-cap`, because its other row is `monitor-play` and no collision exists there.

## The change

In `policies-content/manifesto.php`, the closing pair panel (the second `achology_routes_grid` call):

- The Browse All of Our Courses row: `'icon' => 'graduation-cap'` becomes `'icon' => 'book-open'`.
- The Explore Our Seven Schools row: unchanged.
- Update your FLAGGED comment block above that call: the collision is resolved, Kain S271, recorded at DSRD 7 §5.2.3 (a recorded exception beside the 404 Courses door one).

## Acceptance

The live manifesto page's closing pair shows the open book on the left card and the cap on the right. DSRD 7 §5.2.3 and §5.2.4 already carry the ruling (updated S271), so the spec and the build meet when this ships.

*No em or en dashes in this file; checked before writing.*
