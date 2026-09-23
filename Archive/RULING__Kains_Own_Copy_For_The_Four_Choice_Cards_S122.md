# RULING: Kain's own copy for the pricing page's four choice cards, and the artwork stays off

**From:** Claude Code, S122, Wednesday 17 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Session type:** theme.

**DOCUMENT TYPE: not a page spec.** It files two rulings and specifies no page.

Read with `RULING__Kain_Rules_The_Chooser_As_The_Pricing_Page_Layout_S122.md`,
which is the layout these cards sit in.

## Ruling one: his price-tag artwork stays off the page

> "Yes, leave the picture off."

The artwork he drew at S365 and ruled into the opening band at S121 is not on
this page and does not return. The Chooser has no opening band, and the page now
opens straight onto the four choices; the artwork would push them down the first
screen, which costs most on a phone. Put to him with that reason and ruled.

## Ruling two: the four cards carry his words

He typed all four cards in the sitting. They are carried in exactly as typed,
capitals and all, and not one word of them is Code's:

| name | price | first line | second line |
|---|---|---|---|
| On-Demand Courses | From $97 | Flexible Payment Plans | Lifetime Access to Courses |
| Discounted Bundles | From $987 | Flexible Payment Plans | Lifetime Access to Courses |
| Access ALL Areas | $2,995 | Flexible Payment Plans | Lifetime Access to Courses |
| Membership Plans | $7 Trial | For Your First 30 Days | Then $34.50 Per Month |

Every card now carries the same four parts in the same order: a name, a price
and two lines. The small grey qualifier that used to hang off the figure is gone,
because his first line is what it was for.

**Every figure still matches the document that owns it**, checked against them
rather than assumed: $97 is the lowest course price (DSRD 5 section 1), $987 the
lowest bundle price (DSRD 4 section 1.2), $2,995 the pass (section 1.3), and $7
for 30 days then $34.50 a month is section 1.4's monthly product. His copy
changed the words around the numbers and none of the numbers.

## Two open things his copy settles, which Chat should record

- **"Flexible Payment Plans" answers the instalment question.** Chat's S365
  pointer left instalments open for the live Stripe setup to answer ("whether
  instalments are offered and on what terms", the same fact the course page's
  Three Ways To Buy block waits on). Kain has answered it on three of the four
  cards. It is his to answer, and the course page's block can now be closed from
  the same answer if Chat agrees the two are the same fact.
- **"Discounted Bundles" is this card's name for the school bundles.** DSRD 5's
  product name is untouched everywhere else on the site, including in the
  bundles block further down this same page, which still reads "Go deeper in one
  discipline" over the seven school panels. Chat decides whether that is a
  deliberate two-name state or something to put back to him.

## The fold-back, complete this session (Harness Rule 14)

Built, gated (`css_gate.py`: `pricing.css` PASS) and deployed at theme
**v0.464.0**; server, local and zip proved identical by `deploy.py`. Checked at
1440 and 390: the four names, the four prices and the four links each sit on one
line, all four cards are the same height, the page holds one text edge, nothing
overflows and no tap target is under 44px. The prototype in the Pricing Page
folder is re-exported at the close of the sitting rather than per card, because
the sitting is still running.

## OWED BACK

Nothing to answer. Write both rulings into the documents that own them, and
record the two open things above.

*No em or en dashes in this file; checked before writing.*
