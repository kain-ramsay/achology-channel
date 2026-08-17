# RECORD: the About and Testimonials sweep. Four of five items were already built; one shipped.

**From:** Claude Code, S048. **Date:** 2026-08-06. **Theme:** v0.38.60, live.
**Answers:** `BRIEF__About_Testimonials_Sweep_S245.md`, all four acceptance criteria.
**Acceptance 2 is not met, and not by anything in this change set.** See the gate section.

## What I found before building anything

The brief authorises five spec items and three rulings. Read against the live
pages rather than against the code comments, **four of the five items and all
three rulings were already built**. Verified on the rendered page:

| Item | State found | Evidence from the live page |
|---|---|---|
| §3.1 flagship card course name | already done | all three instances read "Diploma Course in Modern Applied Psychology (DiMAP)" |
| §4.4 courses card description | already done | reads the approved sentence exactly |
| §6 gateway rules | already done | fourteen cards, **zero duplicate destinations**, every external carrying `target="_blank" rel="noopener"` |
| §8.5 poster filenames | already done | all five are descriptive, for example `achology-member-story-personal-benefit.webp`, no bare Vimeo IDs |
| §9 video question labels | **NOT done, shipped this session** | see below |
| Ruling 1, drop 9 + 9 + 12 | already done | the string appears nowhere on the page |
| Ruling 2, the two sentences | already done | both present |
| Ruling 3, the $7 card | already done | "Unlock Full Access for $7" points at `https://community.achology.com/checkout/community-subscription`; "Review Achology's Pricing" keeps `/pricing/` |

**One check of mine was wrong before it was right.** My first pass reported
ruling 2's first sentence missing. It was there: the brief writes "Achology's"
with a straight apostrophe and the page renders a curly one, so a literal
comparison failed on punctuation. Recorded because it is the same class of trap
as the Founders' Letter alt text, in the opposite direction.

**A punctuation divergence to note, not fixed.** Both approved sentences carry
straight apostrophes in the brief; the page renders curly ones, following the
theme's site-wide `&rsquo;` convention. The words match exactly. I have not
changed either, because silently altering an approved character is precisely
what Rule 8 forbids, and because the convention is deliberate everywhere else.
If verbatim means the character too, it is a one-line fix on your word.

## The one item that was owed: §9, the visible video labels

> "Each of the five videos gains a visible text label directly beneath it: its question, in real text, exactly as currently baked into the poster image."

It had been built and deliberately held at S044, with the reason recorded in
the code: the rule carrying it lives in components.css, and components.css did
not pass its own gate. **That blocker is gone.** The values behind it were named
into DSRD 7 in the S238 pass (your ANSWER item 5), and `css_gate` now reports
components.css PASS, checked this session.

Shipped in v0.38.60. Poster and caption are one figure; the grid spans moved
from the button to the figure, or a caption would sit outside its own poster's
column. The question now lives in three places doing three jobs: the
`figcaption` for everyone, the `img alt` for a reader who cannot see the
poster, and the button's `aria-label` so the control announces what it plays.

Caption styling takes DSRD 7 §1's Scanned role, which names soft grey #5E6B75
for "card excerpts and taglines, stats labels, timeline descriptions, image
captions". This is an image caption, which is that row word for word.

**Verified on the live page, cache purged:** five captions, all below their
posters, 14px at #5E6B75, **5.47:1** on white. Desktop spans 3,3,2,2,2 at widths
432, 432, 283, 283, 283, which is the original two-then-three composition at the
documented 282.66 card width. Phone spans 1,1,1,1,1 at 160px. No horizontal
scroll at either width.

**A mistake worth your knowing.** The first deploy shipped the markup and not
the stylesheet: assets are cache-busted by the theme version and I had not
bumped it, so the browser kept the old components.css. The captions rendered at
the wrong size and colour and every grid span fell back to `auto`, quietly
breaking the composition. Reading the rendered page caught it; reading my own
diff would not have.

## Acceptance 2: both pages FAIL their gate, and this change set did not cause it

Run after the change, cache purged before each:

```
/about/          FAIL  34 passed, 2 failed
  FAIL  hairline-present  desktop boundary 2 (policy-header | policy-body): no hairline, gap 48.0px
  FAIL  hairline-spacing  mobile  boundary 2 (policy-header | policy-body): 1.0 above, 32.0 below (want 32/32)

/testimonials/   FAIL  35 passed, 6 failed
  FAIL  hairline-present  desktop boundary 2 (policy-header | tm-answers): no hairline, gap 48.0px
  FAIL  hairline-spacing  mobile  boundary 2 (policy-header | tm-answers): 1.0 above, 32.0 below (want 32/32)
  FAIL  boundary-owner    desktop boundary 5: firstOfB_marginTop 48px, .policy-closing, .policy-related in about.css
  FAIL  boundary-owner    desktop boundary 5: firstOfB_paddingTop 48px, same rule
  FAIL  boundary-owner    desktop boundary 6: firstOfB_marginTop 48px, same rule
  FAIL  boundary-owner    desktop boundary 6: firstOfB_paddingTop 48px, same rule
```

**Proved pre-existing rather than assumed.** Every failure sits at a page-header
or closing-panel boundary; none involves the video strip. More usefully, git
settles it: the only change to `about.css` in this whole session was **three
comment lines** correcting a superseded DSRD quotation, and the
`.policy-closing, .policy-related` rule the gate names last changed on
**2026-08-04**, two days before this session. Nothing shipped today touches
these boundaries.

They are the S224 hairline rulings applied to two pages that have not yet had
their turn in the walk. **About is the very next page on that walk**, and
Testimonials is the last, so both will be fixed there under the walk
instruction, with the document line quoted for each fix. Fixing them inside
this sweep would be the "while I am in here anyway" that Rule 3 exists to stop.

So: **acceptance 1, 3 and 4 are met; acceptance 2 is not, and cannot be met by
this change set.** Reported rather than quietly re-scoped.

## Acceptance 3, dash check

Zero em and zero en dashes on both pages, from the gate above.

## Still open on the About spec, not part of this brief

`SPEC__About_Page_Locked_Structure_And_Copy.md` §8 items 1, 2, 3 and 6 (the
accessibility fixes) and §4 items 2, 3 and 6 (abbreviations, undecodable terms,
era date ranges) are not covered by this sweep brief and are not built. They
belong to About's turn in the walk. Naming them here so the gap between the two
documents is visible rather than assumed closed.

*No em or en dashes in this file; checked before writing.*
