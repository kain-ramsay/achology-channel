# BRIEF: raise the Reviews control bar to a proper search and filter bar (S258)

**From:** Claude Chat, Session 258. **To:** Claude Code.
**Commissioned by:** Kain, directly, S258. He has looked at what is live and says there is room to improve it.
**Surface:** yours. The theme already holds this control bar, so under the S258 two-surface rule you render, Kain judges live in Safari, and the fold-back is yours (harness Rule 14).

---

## 1. What Kain asked for

He wants the /reviews/ control bar to be excellent rather than functional: the search field itself, and the dropdowns, including the spacing inside the dropdown options, the option font size and weight, and everything else that decides whether the bar reads as designed or assembled.

This is a design commission, not a bug report. What is live works; it has not yet been designed by eye.

## 2. What the specifications already fix, and must not be re-invented

Read these from source before you render anything. They are not restated in full here on purpose.

- **DSRD 7 section 5.3:** input border radius is 10px. Cards 12px, buttons 10px.
- **DSRD 7 section 5.2:** the Search icon is already registered for exactly this field: Lucide `Search`, 17px, mid grey #8A9199, inside the Reviews page control bar search input. Registered ahead of build at S239. Do not substitute another icon or size without a ruling.
- **DSRD 7 section 5.4:** `--shadow-dropdown` exists and is the site's dropdown shadow. An open select panel is a dropdown; it takes this token, not a new value.
- **DSRD 7 section 1:** hairline #EEEDED is named for dropdown borders. Mid grey #8A9199 is fine print only and never carries meaning a reader needs; a placeholder that a reader must read to know what the field does is a judgement call worth putting to Kain rather than defaulting.
- **DSRD 7 section 1.1:** an option label in a dropdown is a scanned label, not read prose, so #5E6B75 is its natural colour and #354149 is the safe default where it is doing more work than that.
- **DSRD 7 sections 3.1 and 3.2:** the type scale. Nav is Como 13px/500 uppercase; Button is Como 14px/600; Overline is Como 11px/600; Body Small is Source Sans 3 14px/400. A control label and an option row are almost certainly one of these, not a new size.
- **DSRD 7 section 4:** the 8px spacing scale. Every gap inside this bar is a multiple of it or it is a defect under section 4.5.
- **DSRD 7 section 5.1:** button paddings, including the 9px 22px compact chrome variant, which is the closest existing precedent to a control-bar control.

## 3. What no specification fixes, and what that means

Nothing anywhere in DSRD 7, 8 or 9 specifies a form field's height, its internal padding, its focus ring, an option row's height or padding, the gap between the trigger and its open panel, or the maximum height of a scrolling option list. This is a genuine gap, not an oversight you should route around: it means these are Kain's to rule by eye, and yours to render as options.

Under Harness Rule 5 you do not fill this by judgement, and under the S258 render standard you do not put it to him in prose. You render.

## 4. Claude Chat's proposal, offered as a starting point, not a decision

Marked plainly as a proposal so Kain can rule on it. Derived from the tokens above, not invented from taste:

- **Field height 44px** at desktop, which is the accessible minimum touch target and sits on the 8px scale as 40 plus a hair; 48px if the bar reads too slight beside the cards.
- **Field padding 12px 16px**, with the search icon inset 16px from the left edge and 10px of clear space before the text starts.
- **Field text Source Sans 3 15px/400 in #354149**, placeholder in #5E6B75 rather than #8A9199, because the placeholder is the only thing telling a reader what the field searches.
- **Control gap 16px** between the search field and the dropdowns, 12px between dropdowns.
- **Option row: 10px 16px padding, 15px/400, #354149, hover background #F3F4F4**, selected row in #B8460F with weight 600. A row under about 36px tall starts to feel cramped on a long list.
- **Panel: 10px radius, 1px #EEEDED border, `--shadow-dropdown`, 4px gap below the trigger, 6px inner padding top and bottom**, max height around 320px before it scrolls.
- **Focus: a visible 2px brand orange ring** on both field and trigger, since keyboard focus on a filter bar is exactly where WCAG 2.2 bites and DSRD 7 has no focus-ring standard at all (its only focus values are two annotated one-offs in cards.css).

Treat every number above as a candidate. Where your eye says a value is wrong on the real page, render yours beside it rather than adopting it silently.

## 5. How to put it to Kain

Render the whole bar in place on the live page, above the real 4,517-review grid, at desktop, tablet and phone, with a dropdown open in the shot so the option rows are judged rather than imagined. One question at a time: do not change the bar's shape and its type and its option spacing in one render and ask him which he prefers.

Where you offer a choice, both options carry the same real filters and the same real page, with one variable changed, behind temporary switches as you did for the card heights.

Then the fold-back: once he rules, export the approved state into the component's design folder as its prototype version, update the build sheet, file the RULING naming both, and Chat records it in DSRD 8 and writes the settled values into DSRD 7 as the site's first form-control standard, which is what this bar becomes for every filter and search field built after it.

## 6. One thing not to solve here

The Theme dropdown still cannot be built: its data does not exist until the review bank tagging pass runs. Kain has commissioned that pass. Design the bar for three dropdowns plus search, and leave the Theme slot ready.

*No em or en dashes in this file; checked before writing.*
