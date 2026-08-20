# BRIEF: the policy endnote takes the soft grey. Ruled by Kain, S296.

**From:** Claude Chat, Session 296. **Date:** 20 August 2026.
**Closes:** the contrast failure standing on chapter 7 of every policy-family record since 14 August.

PAGE GATE: all nine policy-family pages. Chapter 7's machine half re-run after the change.

---

## The change

**One declaration, in `policies.css`, in the `.policy-endnote` rule.**

`color: var(--color-mid-grey);` becomes `color: var(--color-soft-grey);`

Nothing else in that rule moves. The spacing, the hairline, the font and the size are untouched, and the link colour inside the endnote is already the accessible orange and stays as it is.

## Why, and it is not a new decision

The contrast failure the gate reports at `.policy-endnote` is a token that was applied wrongly, not a colour anybody chose.

`base.css` states the rule itself, in the text colour roles block, written at Kain's contrast audit on 13 July 2026:

- soft grey is for card stats, school-name text and all secondary supporting text, and passes at 5.5 to 1
- mid grey is for single-line captions, meta, separators and decorative icons only, at 3.2 to 1, and therefore never on links, nav or content

The endnote is a sentence carrying a link. It is content, so it was never mid grey's to hold.

Measured against white: mid grey #8A9199 gives 3.19 to 1 and fails; soft grey #5E6B75 gives 5.47 to 1 and passes.

**Kain saw both rendered, tabbed, on the real line at desktop and phone widths, and chose the soft grey.**

## What this fixes, and where else to look

The endnote renders on all nine pages using the policy template, so one declaration clears the same fault everywhere it appears: privacy, terms, cookies, refunds, trust statement, disclaimers, accessibility statement, and the two quiet About pages that carry an endnote.

**Two other rules in the same file use mid grey and were not part of this ruling.** They are named so nobody assumes they were swept in, and so nobody assumes they are safe either:

- the blockquote citation line
- the two further mid-grey declarations earlier in the file

**Do not change them under this brief.** If the gate reports contrast failures on any of them, report it through the channel and it becomes its own sitting with Kain, on the same rendered-comparison basis this one had.

## Definition of done

The endnote renders in soft grey on all nine pages. Chapter 7's machine half is re-run and the `.policy-endnote` contrast violation is gone from every policy-family record. The rendered pages come back through the channel so Kain can see the change in Safari.

*No em or en dashes in this file; checked before writing.*
