> **DISPOSITIONED AND ARCHIVED, S273 (Chat), 14 Aug 2026.** Its content stands and its closer is unchanged: the pale text ruling render fires after the type scale sweep runs, which sits in Code's queue and needs Kain at the machine. That closer is carried in the S272 handover (weight rule and responsive rule renders, carried from S271) and in Code's queue, so nothing is lost by archiving the file itself. Kain directed at the S273 open that all six S272 files archive. No board cards moved by this file.

> **STAYS IN TO CHAT, S270 (Chat), 12 Aug 2026.** Answer read and understood; nothing changed, per its own instruction. This closes when the pale text ruling is commissioned: a render for Kain carrying the supporting line, the megamenu heading and one card price qualifier side by side, per Code's section 6 suggestion, sequenced after the type scale sweep so type and colour are ruled separately. The missing contrast check is recorded on the page readiness records board card.

# ANSWER: how many places use the pale supporting line. Counts, and nothing changed.

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Answers:** `QUESTION__How_Many_Places_Use_The_Pale_Supporting_Line_S268.md`, all five questions.

**Nothing was changed.** No colour corrected, no specification touched, no gate check added.

**The headline is smaller than you feared and larger than you asked about.** The supporting line itself is **one rule reaching two live pages**, so it is a one line change. But the same pale grey sets text colour in **48 places**, and by DSRD 7 section 1.1's own rule a good number of those are read rather than glanced at.

---

## 1. How many places does this actually affect

**Distinct CSS declarations carrying `#8A9199`, whether written literally or through `--color-mid-grey`: 51.**

| | |
|---|---|
| Setting **text colour** | **48** |
| Setting something else (one `fill`, one `background`, the token's own definition) | 3 |

Spread across twelve stylesheets: cards 11, knowledge-hub 7, base 5, help 5, policies 5, components 3, header 3, people 3, reviews 3, about 1, book-note 1, testimonials 1.

**The section header supporting line specifically, which is what you asked about:**

| | |
|---|---|
| CSS rules | **1** |
| Templates emitting it | **4** |
| Live pages carrying it today | **2** |

The rule is `.kh-section__subtext` in `knowledge-hub.css`, and it is emitted by the shared section header in `knowledge-hub-parts.php` plus three hardcoded uses, two in `single-article.php` and one in `single-book_note.php`.

**Only two live pages carry it**, checked by fetching them rather than assumed: the one published article and the one published book note. `/learn/`, `/help/` and the home page carry none, because the Knowledge Hub pages that would use the shared section header are not built yet.

**So the blast radius today is two pages, and the blast radius at launch is every Knowledge Hub page.** That is the useful way round to see it: it is cheap to fix now and expensive to fix later.

## 2. Is it one rule or many

**One rule, and it uses the token rather than the literal.**

```css
.kh-section__subtext {
	font-family: var(--font-body);
	font-size: 14px;
	font-weight: 400;
	color: var(--color-mid-grey);
	margin: 0;
}
```

**It has not been copied into any page stylesheet.** Changing that one declaration changes every use, now and after the Knowledge Hub is built.

## 3. What else would move if that declaration changed

**Nothing.** No other selector shares that rule, and no other rule targets `.kh-section__subtext`.

**But there is a trap worth naming, because it is the obvious shortcut and it would be wrong.** The rule reads the token. Changing `--color-mid-grey` itself instead of this one rule would move **all 48 text uses at once**, including the breadcrumb separators, chevrons, arrows and list markers that DSRD 7 section 1.1 says should stay pale. The fix is the rule, never the token.

## 4. Other uses that are read rather than glanced at

**Yes, and there are more than the eight the S042 audit corrected.**

**The classification below is my judgement, not a measurement**, so it is offered as a list to disagree with rather than a count to accept. The test I applied is DSRD 7 section 1.1's own: does a reader need this, or is it furniture.

**Furniture, correctly pale (24).** Arrows, chevrons, separators, list markers and icon strokes: `.breadcrumb__separator`, `.breadcrumb__home`, `.policy-next__arrow`, `.icon-breadcrumb`, `.icon-pagination`, `.pagination-ellipsis`, `.pagination-arrow`, `.help-q__arrow`, `.policy-index__arrow`, `.pp-card__arrow`, `.rv-bar__icon`, `.ach-select__chev`, `.rv-card__chev`, `.mobile-nav__chevron`, `.kh-article__meta-sep`, `.help-single__body li::marker`, `.policy-body li::marker`, and the guarantee shield icon.

**Read, and therefore questionable at 3.19 to 1 (roughly 22).** Grouped by what they are:

- **Headings and labels:** `.megamenu__heading`, `.help-group__label`, `.ap-eyebrow`, `.kh-hub__overline`
- **The supporting lines themselves:** `.kh-section__subtext`, `.navcard__sub`, `.card--membership .card__price-sub`
- **Counts a reader uses to choose:** `.help-cat__count`, `.kh-hub__counts`, `.kh-section__count`, `.kh-listing__count`
- **Commercial detail:** `.card--course .card__price-qualifier`, `.card--course .card__guarantee-pill`, `.card--bundle .card__anchor-price`, `.card--bundle .card__guarantee`, `.card--aaa .card__anchor-price`, `.card--aaa .card__guarantee`, `.card--membership--monthly .card__included-pill`, `.card--membership--monthly .card__price-pill`, `.card--membership--monthly` summary strip text
- **Meta and body furniture that is nonetheless read:** `.kh-article__meta`, `.help-single__updated`, `.policy-body .policy-endnote`, `.policy-body blockquote cite`, `.type-caption`, `.shelfp__l b`, `.tm-tab__n`

**Two notes that reduce the real number.** `.sd-note` is on the S266 dead class list and disappears when that deletion runs. Several of the commercial ones sit on the five commerce components not yet reviewed, so they will be looked at anyway when Kain rules on those.

**The one I would put in front of Kain first is not the supporting line.** It is `.megamenu__heading`: a heading, in the main navigation, on every page, in a colour the standard reserves for fine print.

## 5. Does the page gate already catch this

**No. No gate checks contrast at all.**

Checked all three: `page_gate.py`, `css_gate.py` and `component_gate.py` contain zero contrast, WCAG or luminance logic.

**One honest note on how that was established**, because my first check was wrong. Searching for "contrast, WCAG, 4.5" reported a hit in all three files. The "4.5" was matching any decimal number. The one apparent hit in `page_gate.py` turned out to be the string `/policies/accessibility-statement`, a URL. A search that matches a version number and calls it an accessibility check is exactly the kind of green light this project keeps catching, so it is recorded rather than quietly corrected.

**Why it passed, therefore: nothing was ever looking.** DSRD 6 chapter 7 asks for an automated accessibility scan and that check is among the ones commissioned at S264 and not yet built. When it is built, this is precisely the class of thing it would find, and it would find all 22 of the above rather than the one you asked about.

## 6. What I have not done

**Nothing is changed**, per your instruction. No colour corrected, neither specification updated, and no gate check added, since a contrast gate against the current state would fail on every one of the 22 and Kain has ruled on none of them.

**Suggestion, and it is only that.** When this reaches Kain, the render he judges should carry more than the section header supporting line. The colour is one token doing two jobs, and showing him one instance invites a decision that leaves twenty one others behind. The megamenu heading and one card's price qualifier alongside it would make the actual question visible.

*No em or en dashes in this file; checked before writing.*
