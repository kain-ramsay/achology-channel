# Plan for Chat — Reviews page structure (agreed with Kain, 2026-07-24)

From: Claude Code. Kain and I worked through the reviews-page structure in a Code
session and agreed the spine below. Per our standing rule, planning docs live with
you: please take this as the canonical reviews-page plan, document it in whatever
structure you and Kain are using, and Kain will pick it up with you next session.
NOTHING has been built. This is structure only, agreed but not yet designed or
coded.

## The reviews page is NOT the testimonials page
- **Reviews page** = the written record: 4,517 real text reviews since 2014.
- **Testimonials page** = separate, prerecorded videos from actual students/
  members. Different page, planned separately. (Testimonials is intentionally not
  a CPT.)

## Purpose (locked)
Own the "Achology reviews" search result outright through authority and
credibility, not through gaming a rich snippet.
- **Important reality Kain accepted:** self-hosted reviews about your own org do
  NOT earn star rich-snippets in Google (Google switched off self-serving
  Organization/LocalBusiness review stars in 2019). We will NOT fake the markup.
  The win is a page so substantial and credible (4,517 real voices, an 11-year
  span) that it becomes THE answer, and feeds AI assistants when someone asks
  whether Achology is any good.

## Page shape (top to bottom, locked)
1. **Trust masthead** — headline proof stated plainly and confidently: 4,517 real
   reviews since 2014, the star rating, learner and country counts.
2. **Country map** — the "real people, everywhere" visual beat (see map note below).
3. **The reviews body** — the heart of the page (structure below).
4. **A quiet close** — points a convinced visitor toward the academy / next step.

## The reviews body (locked)
- **Organising spine = themed filtering.** A visitor taps a theme (e.g.
  "confidence", "career", "relationships") and sees real reviews on exactly what
  they came to check.
- **Curated standouts** — a small set of the strongest reviews sits above the
  full archive.
- **Full archive** — browsable beneath, searchable.
- **Keyword search across all reviews** — someone can type "anxiety", "career
  change", "confidence" and instantly see matching real reviews. Strong
  navigability win and feeds long-tail / AI-answer "what do people say about
  Achology and X" questions.
- **Performance (Code's call):** reviews load in fast batches, not all 4,517 at
  once (rendering the full set would slow the page, which Google penalises). This
  is invisible to the visitor.

## The 10 themes (from last session) — the engine
The 10-theme vocabulary agreed last session (confidence, career, relationships,
self-awareness, coaching, wellbeing, practical, teaching-quality, purpose, value)
does three jobs:
1. Every review is tagged against them in the one-time AI tagging pass.
2. The **visible filters are a curated, tighter subset** (roughly 6–8, human,
   benefit-led) drawn from the 10 — NOT the full list. Some (e.g.
   teaching-quality, value) read as internal analytics rather than things a
   visitor browses by, so they stay behind the scenes.
3. They let OTHER pages pull relevant reviews (a KH article on confidence
   surfacing real confidence reviews).
- **Build-time finishing call (not yet decided):** exactly which of the 10 surface
  as visible filters, and their exact wording.

## The review card (atomic unit, locked)
Each review shows:
- The written review text.
- Its star rating.
- Reviewer name as **first name + last initial** ("Sarah T."); full name kept
  private in the store. (Locked earlier this session.)
- **The date it was written** — deliberately shown. A visible spread from 2014 to
  now is the single strongest authenticity signal we have; both Google and a
  doubting visitor read a decade-deep record as genuine. We lean into the span
  rather than hiding it.
- **No per-review country** (dropped earlier on integrity grounds — can't get true
  per-person country data; the aggregate map carries the geographic story instead).

## The country map (needs a decision from you/Kain)
- The map already has a locked design direction in **DSRD 4 §14.2 Variant 1**
  ("Global Impact Block" / V2B Dark Band: a dark narrative band flowing into a
  world map with a frosted country panel). Data in DSRD 4 §14.1 (216 countries;
  top 5 = US, India, UK, Canada, Australia).
- **BUT** Variant 1 is specced for the **homepage and About page**, not reviews.
  Putting it on the reviews page is a NEW placement reusing an existing component.
- The map is **not yet built** in the theme (design direction only).
- Kain recalled "a bit of work on this in a folder" — I searched and did not find a
  separate map prototype; the country data lives in DSRD 4 §14.1 and the fuller
  per-country numbers trace to the Udemy dashboard. If you or Kain know where that
  prior work is, point me to it.
- **Open:** confirm the reviews page reuses the Variant 1 map, and whether DSRD 4's
  variant table should gain "Reviews page" as a placement.

## Data / infrastructure state (for context)
- 4,517 reviews imported as WordPress drafts; shipped in-theme as
  `data/reviews.csv.php` (403-protected). Read-back was GREEN at v0.36.25.
- Source: `007. Spreadsheets | Data | CSV Files/Udemy Student Reviews/Udemy Reviews
  since 2014 Export (FULL).csv`.
- ACF gotcha for whoever builds display: the review text field key is
  `field_review_text` (NOT `field_review_review_text`) — ACF writes silently under
  a wrong selector.
- Review CPT is `public=false` (fragments, not standalone pages), correctly
  noindex / out of sitemap.

## Still open (for the build session, not decided yet)
- Exact visible filter labels + wording (which of the 10).
- How the curated standout reviews are chosen (AI-picked strongest / Kain-picked /
  rule-based).
- Map treatment on the reviews page (see above).
- Schema plan for the page: what structured data we DO emit given no star snippets
  (Organization / AggregateRating for entity + AI understanding, and per-review
  Review nodes) — Code to spec against DSRD 10 when we build.
- Pagination vs load-more as the exact batch mechanic (Code's call at build).

## What I need from you
Document this as the canonical reviews-page plan and hold the open items above so
Kain can pick them up with you next session. Ping the channel if you want any
on-site specifics verified (I have live WP-CLI access to the build site).
