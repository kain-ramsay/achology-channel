# SHIP: the button sweep, and the Founders' Letter's outward link

**From:** Claude Code, S046. **Date:** 2026-08-05. **Shipped:** v0.38.15, deployed.
**Closes:** `BRIEF__Button_Sweep_S245_Rulings.md`, now archived.
**Also files, under Rule 14:** Kain's ruling in session on the Founders' Letter link.

---

## 1. The button sweep

Built exactly to the brief. **Only the footer CTA button changed.** Sign In, the
nudge CTA and the Listen button were not touched, as instructed.

DSRD 8 §19.7 as amended, read from the canonical file this turn: "12px 24px padding
(joined to the DSRD 7 §5.1 standard, Kain's S245 ruling on the rendered card;
superseding the earlier 12px 28px)" and "'Start Your Trial' + Lucide `ArrowRight`,
15px, white, 6px gap".

**One decision worth recording:** the padding override was **deleted** rather than
restated as 12px 24px. The button now inherits its size from `.btn`, so it cannot
drift from the standard again without the standard itself moving. `.cta-card__btn`
keeps only what is genuinely local to the CTA card, the z-index lift above the
bubble watermark.

The typed chevron is gone and the arrow comes from `achology_icon( 'arrow-right' )`,
the same registry every other action button uses, so it carries the system's one
stroke weight automatically.

### Measured on the rendered live page

| property | measured | §19.7 as amended |
|---|---|---|
| padding | 12px 24px | 12px 24px |
| border radius | 10px | 10px |
| font | Como 14px/600 | Como 14px/600 |
| background | rgb(237, 105, 34) | #ED6922 |
| text | rgb(255, 255, 255) | white |
| arrow | 15px by 15px | 15px |
| gap | 6px | 6px |
| stroke | 1.75 | DSRD 7 §5.2's one weight |

### The three page types the brief names

| page | label | arrow | typed chevron |
|---|---|---|---|
| /about/ | Start Your Trial | present | gone |
| a help article | Start Your Trial | present | gone |
| the 404 | Start Your Trial | present | gone |

### Gate

```
=== footer.css ===
  PASS

=== components.css ===
  PASS

==================================================
GATE PASSED. Safe to ship.
```

---

## 2. RULING: one outward link in the Founders' Letter

Kain, in session, having first asked for an external link and then named the
destination himself when I said the choice was his:

> "link Diagnostic and Statistical Manual of Mental Disorders to
> https://en.wikipedia.org/wiki/Diagnostic_and_Statistical_Manual_of_Mental_Disorders"

**No copy was written.** The phrase already stood in the letter, in the sentence
"The American Psychiatric Association began publishing that list in 1952, as the
Diagnostic and Statistical Manual of Mental Disorders." Linking existing words is
what DSRD 1 §6.4 asks for, "the anchor is the words already in the sentence", and it
keeps the Rule 8 content boundary intact: I placed a link, I did not draft a word.

DSRD 3, read this turn: "All external links across the site open in a new tab
(`target="_blank"` with `rel="noopener"`)." Built to match the UKRLP link on About,
which is the site's existing outward pattern.

**Verified on the rendered page:** destination correct, `target="_blank"` present,
`rel="noopener"` present, anchor reads "Diagnostic and Statistical Manual of Mental
Disorders", and it is the only outward link in the letter's content.

**For the record:** this is now the letter's first outward citation, so DSRD 2's
citation practice may want a line about it.

---

## 3. Still owed on that page, and it is yours

The Founders' Letter still carries **no Rank Math title, description or focus
keyword**. Kain also asked this session for the focus keyword to be built into the
hero image's alt text, which currently reads "Kain and Karen Ramsay, founding
partners of Achology.com".

**Both are blocked on the same thing and neither is mine under Rule 8.** There is no
focus keyword to build into anything, and Rank Math cannot score the page at all
until one exists, so the keyword is what stands between that page and 80, not the alt
text. It is requested in `REQUEST__Founders_Letter_Metadata_Needs_Writing.md`. Send
the title, the description and the focus keyword together and I will set all three
and rewrite the alt in one pass.

*No em or en dashes in this file; checked before writing.*
