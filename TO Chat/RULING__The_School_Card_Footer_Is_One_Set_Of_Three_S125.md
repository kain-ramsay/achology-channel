# RULING: the school card's footer is one set of three, at one size

**DOCUMENT TYPE: ruling record, not a page spec.** It records a ruling Kain gave in session and specifies no page.

**From:** Claude Code, S125, Monday 21 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Reads with:** `RULING__One_Footer_On_The_School_Card_With_The_Seal_In_It_S125.md`, filed earlier this session, which this one follows directly and corrects.
**OWED BACK:** two things, and the second is a change to a register. Both at the foot of this file.

## His ruling, in his words

> "We have three bits of information in this one block. A Pricing Options dropdown, which you don't even have a border around, an Enrol button, and a price ... The Pricing Options dropdown should in essence be the same size as a typical button. Please standardise this ... You have like three different font sizes going on here ... Having three different font sizes in one block is ridiculous. Lean this thing out. Please make some effort here."

He is right on every count, and the fault was Code's. The block had been built by taking width from whatever would give it: the field lost its border, the price kept the register's 24, the saving sat at 12 under it, and the result was three objects of three sizes and two heights standing in a row and calling itself one block.

## What it is now

The footer is built as **one set** rather than three things that happen to share a line. Every piece takes the same height, the same corner radius, the same type size and the same face. What separates them is fill and weight, which is **his own weight-not-size ruling from earlier in this build**, applied here.

- **The plan** is the site's own field again, at the standard it already had. DSRD 7 section 5.5, quoted: "height 44, padding 12px 16px, Mulish 14px in brand dark, 10px radius, 1px hairline border." Its border is back.
- **The price** keeps the Seal, filled with the school's own text-safe colour, white type, the saving beside the figure inside it. Same height, same corner, same size, heavier weight, because the money is what the eye should land on.
- **The action** is the button, untouched. DSRD 7 section 3's register, quoted: "| Button | 14px | 600 | ... | All buttons |".

## The register change this forces, which is the part Chat must act on

**One size across the block overrides DSRD 7 section 3's own row for the bundle price.** That register gives it 24px, quoted: "| Bundle Price | 24px | 700 | ... | Bundle/AAA card price |". A 24 beside two 14s is the third size he counted, so the row now reads 14px at weight 700 on this card.

Kain's instruction in the sitting is the higher authority under The Shared Rules section 8, and this file is how it reaches the document that owns it. **Chat's call to make:** whether the register's Bundle Price row changes outright, or gains a note that the pricing page's school card footer sets it at 14/700 because the block is a control set. The Access All Areas card shares that register row and was not in front of him, so it has not been touched.

## Shipped

Theme **v0.530.0**, deployed, with local, the server and the zip each measured and agreeing. `css_gate`: pricing.css PASS.

Checked on the rendered page at 1440, 1024, 768 and 390: one type size everywhere in the block, the three pieces the same height on every one of the seven cards, one line at the widest screen with nothing outside a card and nothing clipped, and no sideways scroll.

**One thing reported to him and not hidden:** below the widest screen the action takes the full width under the other two, because three objects of one height do not cross a card that narrow when the seven stand two abreast.

## Also owed back

Fold this and the two S125 rulings before it into DSRD 8 section 8 as the pricing page's school panel footer, replacing what the S124 rulings put there.

## Still open on this page

The two membership panels and the free tier strip, the questions block, the closing help strip, and the page's rhythm judged last. `/pricing/` is still unpublished on Chat's S365 disposition and its DSRD 6 record is not filed.

*No em or en dashes in this file; checked before writing.*
