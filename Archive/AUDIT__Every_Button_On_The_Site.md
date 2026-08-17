# AUDIT: every button on the site, measured. The code is not the problem. The documents are.

**From:** Claude Code, S046. **Date:** 2026-08-05.
**REWRITTEN the same session**, after I read the component specs. My first version of
this file called six things "drift" and recommended fixing them in code. **That was
wrong and I have corrected it below.** Every one of those values is specified in
DSRD 8, and the code matches its spec exactly. Changing the code would have put it at
odds with the documents.

**Why this exists:** Kain raised it in session, unprompted, from his own eye: the hero
buttons are right, but the button in the closing enquiries block and the one in the
footer "are completely different, they do completely different things, which is
inconsistency". He asked for a site-wide button sweep and called it a priority.

**Status: STOPPED, per Rule 8.** "Where a spec is wrong or contradicts another, report
it and stop." No code has been changed. What Kain is seeing is real, but it cannot be
fixed in the theme without contradicting DSRD 8.

**How it was measured:** computed styles read off the rendered live pages this turn, at
achologytest.com, across five page types: About, Testimonials, the help landing, a help
article and the 404. Then checked, one by one, against the specification that governs
each component.

---

## 1. What is live, and what its own spec says

| control | measured live | its spec | verdict |
|---|---|---|---|
| `.btn` base (hero actions, enquiry) | Como 14/600, 10px radius, 12px 24px | DSRD 7 §5.1 font and radius; padding is in `base.css` only | **conforms** |
| `.btn-signin` header and mobile nav | Como **13px**/600, 10px radius, **9px 22px** | DSRD 8 §18.6: "Font Como 13px/600 ... Padding 9px 22px ... Border-radius 10px" | **conforms exactly** |
| `.nudge__cta` promo card | Como 14/600, **8px radius**, **8px 16px** | DSRD 8 §18.12: "CTA button Como 14px/600, white text, 1.5px rgba(255,255,255,0.55) border, 8px radius, 8px 16px padding" | **conforms exactly** |
| `.cta-card__btn` footer, every page | Como 14/600, 10px radius, **12px 28px**, label ends "›" | DSRD 8 §19.7: "Button Como 14px/600, white text on brand orange #ED6922, 1.5px orange border, 10px border-radius, 12px 28px padding" and content "Start Your Trial ›" | **conforms exactly, chevron included** |
| `.help-listen__btn` | Como 14/600, 10px radius, **9px 16px** | DSRD 7 §5.2 registers the icon only. **No padding specified anywhere.** | unspecified |
| `.help-helpful__btn` | Como 15/600, **999px pill** | Ruled a registered exception by Kain, S046 | exception, filed separately |

**Five of six conform to their own specification. One is unspecified. Zero are drift.**

## 2. So where does the inconsistency actually live

In the documents. They specify different values for the same kind of control, and
nothing arbitrates between them.

1. **DSRD 7 §5.1 never states a padding.** It gives font, radius and colours and stops.
   So it cannot settle any disagreement about size, and every component spec has
   filled the gap on its own.
2. **Four different paddings are specified across the documents:** 12px 24px (the code
   base), 9px 22px (§18.6), 8px 16px (§18.12), 12px 28px (§19.7).
3. **Two different radii are specified:** 10px in §5.1, §18.6 and §19.7, but **8px** in
   §18.12. §5.1 says "Button border-radius: 10px" with no exception noted, so §18.12
   contradicts it outright.
4. **Two font sizes are specified:** 14px in §5.1, 13px in §18.6. Same, no exception
   noted.
5. **§19.7 puts a typographic chevron inside the button label**, "Start Your Trial ›",
   while DSRD 7 §5.2 says "All icon slots in the design system use named Lucide icons
   from this registry. Improvised freehand SVG icons are prohibited." A text chevron is
   not a Lucide icon and not a registered slot. These two documents disagree about the
   most-seen button on the site.

**This is why Kain can see it and no gate has ever caught it.** Every gate checks a
component against its own spec, and every component passes. Nothing checks the specs
against each other.

## 3. What I recommend, and what I have not done

**I have changed nothing and I am not proposing a code sweep.** A sweep now would make
five conforming components non-conforming.

The fix is one ruling and then one pass, in that order:

1. **§5.1 gains a padding line and becomes the authority.** One standard button size,
   and a small number of explicitly named variants (a compact one for chrome, whatever
   the footer card needs) with the reason each exists written beside it.
2. **The four component specs are reconciled to it.** Either each keeps its value as a
   registered exception with a stated reason, or it moves to the standard. Both are
   fine; what is not fine is four values and no statement of which governs.
3. **The chevron question gets settled** between §19.7 and §5.2. My view: the registered
   Lucide `ArrowRight`, because it is the same arrow every other action button on the
   site uses and the typed chevron is a different shape and weight at the same size.
   But §19.7 is a signed component spec and I will not overrule it.
4. **The listen button gets a specified padding**, since it currently has none and is
   the one control on the site genuinely deciding for itself.
5. **Then, and only then, one code pass** brings anything that moved into line.

**My recommendation on the standard itself:** one button size at 12px 24px, because it
is what §5.1's own base already produces and what the two most recently approved pages
use; one named compact for buttons inside fixed-height chrome; and the footer card
keeps 28px only if there is a reason worth writing down, otherwise it joins the
standard.

## 4. What Kain should be told, in his terms

He was right that it looks inconsistent, and he was right that it matters. He was
looking at four different specifications, faithfully built. The fix belongs in the
documents first, or the same drift returns the next time a page is built to a spec that
disagrees with §5.1.

*No em or en dashes in this file; checked before writing.*
