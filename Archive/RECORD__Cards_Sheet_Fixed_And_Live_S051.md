# RECORD: both faults fixed, all four acceptance items pass, and the sheet is live

**From:** Claude Code, S051. **Date:** 2026-08-10.
**Answers:** `FIX__Cards_Sheet_Grid_And_Member_Row_S256.md`.
**Completes:** `COMMISSION__Build_The_Card_Sheet_For_Review_S255.md`.

**The sheet: https://achologytest.com/cards/**

## Acceptance, measured on the rendered page

| # | Required | Measured |
|---|---|---|
| 1 | Standard cards at their real 3-column width, not full width | at 1280px, `.kh-grid` is `display: grid`, `352px 352px 352px`, card **352px** |
| 2 | Featured cards span 2 of the 3 columns | **728px**, which is 352 + 352 + the 24px gap |
| 3 | 768 to 1023px is 2 columns | at 900px, `406px 406px`, card **406px** |
| 3 | Below 768px is 1 column | at 390px, `350px`, card **350px** |
| 4 | The §13A row shows the member cards | **9 cards**, at both 1280px and 390px |

No horizontal overflow at 900px or 390px.

## Fault 1, and it was my error rather than a gap

`knowledge-hub.css` never enqueued on the sheet's page, so `.kh-grid` carried
its class and none of its rules. Fixed by adding the page to the same enqueue
condition the Knowledge Hub templates use, which is one clause rather than a
second stylesheet or a copied rule.

**The part worth recording is how I came to report it as right.** My delivery
said "Grids are the real ones". The class was real; the rules never reached the
page. I could not measure the widths because my own headless browser would not
lay the page out, and instead of writing "unverified, and here is why", I wrote
round the gap. Kain then found it in ten seconds by looking at it.

That is the difference between reading a template and measuring a render, and
it is the same failure this project has a rule about. The rule caught it,
because Kain looked at the page. I should not have needed him to.

The browser did lay it out on a second attempt, which is how the numbers above
exist. Nothing about the page had changed; the pane had simply not sized
itself the first time. Worth knowing for next time: a measurement of zero from
that tool is a tool failure, never a page fact, and it should stop the report
rather than be worked around.

## Fault 2, already fixed before your brief arrived

The member row was empty because I passed `achology_member_voices()` a title
and a lead, which are not its arguments. It takes a cards array. It rendered
the heading and an empty grid, which reads as a finished section until you
count what is under it.

Now called exactly as `page-testimonials.php` calls it, with
`achology_member_voice_cards()`. Nine cards, confirmed at two widths above.

## One correction to my own delivery note, so the record is straight

That note listed eighteen broken images on the sheet. **They are not broken.**
Every one returns 200 with real bytes, checked directly, theme images and
uploads alike. They read as broken because the same unlaid-out browser reported
every image as failed. Nothing needs looking at.

## What the review can now proceed on

The section 6 cards and the member row are ready to review at all three tiers.
The course cards were already reviewable and are unchanged by any of this.

Commits: `747f924` for the grid, and the member row fix immediately before it.

*No em or en dashes in this file; checked before writing.*
