# SESSION REPORT: S127, Tuesday 22 September 2026

**Theme session. Theme v0.583.0 to v0.620.0, thirty-seven change sets, every
one deployed and pushed. Assembled from the version control log, not recall.**

## Finished

- **The pricing page exists on the install and is published on the build site.**
  Page 36845, named from DSRD 1 section 13.1's locked row. Board card: Pricing
  page (PRD Pr1.19).
- **Its DSRD 6 record exists and carries its machine chapters.** Created from
  the template into the page's own design folder and filled by the readiness
  board's sweep. Code wrote only the machine rows.
- **Eighteen design rulings and four copy replacements folded in**, each from
  four rendered options where the change was Code's to propose, each filed in
  `RULING__Kains_Eighteen_S127_Rulings_On_The_Pricing_Page.md`. Board card:
  Pricing page.
- **The primary button's fill returned to the AA-safe orange**, site-wide. A
  regression repaired: the S096 fix had come undone and left its own hover
  token stranded. Board card: the one that holds accessibility, or the
  Pricing page card if there is none.
- **The stylesheet gate gained two checks**, spacing and stylesheet syntax.
  Board card: whichever holds the theme's gates.
- **A page-creating tool the publishing wall can admit**, entered in its
  reviewed register with its payloads quoted. Board card: as above.
- **The prototype in the Pricing Page folder is the ruled page**, exported
  after every ruling, per Rule 14's fold-back.

## Not finished, and what remains

- **The page's readiness record is four chapters red.** Metadata (no search
  title or description, which is copy and Chat's), schema (the page carries no
  JSON-LD at all, which is Code's to build), accessibility (now only the
  contrast fixed site-wide today, to be re-run), and structure (the choice card
  is not in the component registry).
- **The four pages this one links to still do not exist**: `/courses/`,
  `/academy/schools/`, `/access-all-areas/`, `/membership/`.
- **The Circle and Stripe confirmations** the build pointer asked for: currency
  and tax, whether included membership renews, refund terms per product,
  instalment terms. Not theme work.

## Hand added, with no machine record

Kain's own screenshots drove three of the day's findings: the broken vertical
divider, the pass card's failing SAVE contrast, and the school names running to
three lines. All three were measured before being reported.

## Three faults of Code's own, recorded because the lesson is general

1. **A ruling reported as shipped that never landed.** Half was folded in as a
   bare class that lost a tie and drew nothing. It was measured afterwards, the
   measurement returned the old number, and nobody compared it to the number
   the ruling asked for. Kain found it on the page.
2. **A stylesheet killed by a comment.** A paragraph added after a comment had
   closed put prose into the file as code, and every rule below it stopped
   applying. The browser says nothing. This is now check H.
3. **A measurement reported to Kain that was wrong.** He was told the word SAVE
   sat forty points from its figure; it sits eight. The forty came from
   measuring the typed figure and ignoring the drawn word.

*No em or en dashes in this file; checked before writing.*
