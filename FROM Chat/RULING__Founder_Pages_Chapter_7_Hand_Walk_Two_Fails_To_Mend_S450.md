> CODE DISPOSITION, S194: WAITS ON a theme session (read in full by the S194 factory session, which edits no theme file).

**For Code (theme session). What this needs:** mend the two faults below, then rerun chapter 7's machine half on the three founder pages and write these lines into the three DSRD 6 records; reply in TO Chat with the theme version. Answers ASK__Founder_Pages_Rescore_And_Final_Reread_S188 (chapter 7 half).

# RULING: the founder pages' chapter 7 hand walk is done; two faults to mend, both settled by existing rulings (Chat, S450, 28 October 2026)

Walked by Chat on the build site, theme 0.707.655, against DSRD 6 §7 and §7.1's WCAG 2.2 checks, on the Founders' Letter, the Manifesto and the Code of Ethics, at 1440 wide and at 320 wide (the 400 per cent reflow width). No vault note bears on this job beyond DSRD 6 §7 and DSRD 7 §1.

## What passes on all three

- **Keyboard:** every control reachable by Tab in reading order; no positive tabindex; the focus ring is the site's `:focus-visible` rule, 2px brand orange, 3.16:1 on white and 6.64:1 on the dark footer, above the 3:1 bar; walked with real Tab presses and seen on screen.
- **Focus not hidden (2.4.11):** the header is sticky at 72px and the page carries `scroll-padding-top: 80px`, so a focused item never sits under it.
- **Contrast at rest:** no text on the three pages below 4.5:1 (3:1 for large text).
- **Names:** no link or button without an accessible name; skip link present; `lang="en-GB"`.
- **Images:** the Letter's two photographs and the signature carry true descriptions; the menu's course thumbnails are correctly decorative beside their names.
- **Reflow:** at 320 wide, no sideways scroll and nothing wider than the screen on any of the three.
- **Target size (2.5.8):** the menu and footer links under 24px tall all clear the spacing exception; the only clashes found were with the closed mega menu, which is hidden.
- **Moving things:** the only animation is the cookie button's single half-second slide.
- **Code of Ethics handbook:** the 42 page images are a named dialog ("The Achology Code of Ethics Handbook", each image "Page N of 42"), and the page offers the PDF, which is tagged, carries real text, `en-GB` and a title. That PDF is the text alternative, so this passes.

## Fail 1, all three pages (a site template, so fixed once): hover states put small text in brand orange

DSRD 6 §7 requires every hover and focus state's contrast checked by hand. DSRD 7 §1 already rules that brand orange #ED6922 (3.16:1 on white) is for large text, borders, fills and icons only; small orange text takes `--color-orange-link` #B8460F; and no button carries a white label on brand orange. These hover rules break it:

| Rule | What it does on hover | Size | Measured |
|---|---|---|---|
| `.site-nav__link:hover, :focus-visible` | header link text to brand orange on white | 12px 500 | 3.16:1 |
| `.btn-signin:hover, :focus-visible` | white label on a brand orange fill | 12px 600 | 3.16:1 |
| `.nudge__cta:hover, :focus-visible` | brand orange label on white | 14px 600 | 3.16:1 |
| `.policy-next__row:hover .policy-next__name` (and its arrow) | name to brand orange on white | 18px 600 (not large) | 3.16:1 |
| `.navcard:hover .navcard__name` | name to brand orange on off-white #F3F4F4 | 14px 600 | about 2.9:1 |
| `.mobile-nav__list a`, `.mobile-nav__sublist a`, `.mobile-nav__toggle` hover | to brand orange; measure on their ground | small | check |
| `.site-search__toggle:hover` | icon to brand orange on off-white | icon, 3:1 bar | about 2.9:1 |

**The mend, settled by DSRD 7 §1, not a new design:** each small-text hover above takes `--color-orange-link` #B8460F (5.35:1 on white, 4.86:1 on off-white); `.btn-signin`'s hover fill takes `--color-orange-action` #C85015 with its white label (4.55:1), as every primary button already does; the search icon takes #B8460F or keeps brand orange on a white ground. The hover still reads as orange, one step deeper. Because it is a visible change, show Kain the before and after on one header in Safari when you next sit together; it needs no four options, as it applies a ruling he already made.

## Fail 2, the Manifesto: the Manifesto's own words exist only as a picture

The page explains the Manifesto, but the Manifesto itself, the words members read aloud, is only inside `manifesto-document.webp`, in the thumbnail and in the lightbox, both described as "The Achology Manifesto document". A screen reader user never hears it (WCAG 1.1.1 and 1.4.5). The outer `.policy-doc-lightbox` also carries no role; check the panel inside it carries `role="dialog"` and a name, as the Code of Ethics panel does.

**The mend, no visible change:** carry the Manifesto's full text with the image, either as a visually hidden transcript inside the figure and the lightbox panel, or as `aria-describedby` pointing at it, taken word for word from the master image's current wording (the three "empower" words Kain replaced at S433 are already out of the designed image only if Kain has remade it; use the wording the image shows today, and the Backlog: Chat line on the remake stands). A Manifesto PDF like the handbook's would also do.

## The three chapter 7 lines for the records (write them in once both mends are live and the machine half reads zero)

- **Founders' Letter:** §7 hand walk 28 October 2026, Chat: keyboard, focus visible and not hidden, contrast at rest, names, images, 320 reflow, target size, motion all pass; hover contrast failed (template, Fail 1), passes once mended at theme <version>.
- **Manifesto:** as the Letter, plus the Manifesto image's text alternative (Fail 2), passes once mended at theme <version>.
- **Code of Ethics:** as the Letter; the handbook passes through its tagged PDF; hover contrast (Fail 1) passes once mended at theme <version>.

Not walked here, and still owed at Kain's sitting by §7.1: the VoiceOver read on the Mac and on the iPhone.

OWED BACK: the theme version carrying both mends, the machine half rerun on the three pages, and the three lines written into the records.

*No em or en dashes in this file; checked before writing.*
