**DISPOSITION (S280, Chat):** read and answered at S279 via REPLY__The_Four_S062_Files_Answered_S279 in the new FROM Chat. Carried in the S279 handover: DSRD 7 sections 3.1 and 3.2 still hold pre-ship sizes for the nine rows this ruling moved, and the Knowledge Hub article body at 880 shares the line-length fault and has not been put to Kain. Archived.

# RULING: Kain approved the Knowledge Hub article and book note pages on the type scale

**DOCUMENT TYPE:** ruling, filed under Harness Rule 14. It doubles as the ship brief for v0.64.1, because the ship is nothing but the execution of the ruling and a second file would say the same thing twice.
**From:** Claude Code, Session 062. **Date:** 17 August 2026.
**Executes:** `BRIEF__Type_Scale_Sweep_S270.md`, sitting two of the representative page route.
**Board card:** the typography card.

---

## 1. The ruling, in Kain's words

> "the right one reads better on both"

Given in Safari, on the two column comparison: the Knowledge Hub article page and the book note page, each rendered twice, left as the live site serves it and right with every type size on the nine approved steps. One page design on screen at a time, tabbed, per standing rule 16.

**This is a Safari ruling on rendered pages**, which is the standard this project requires for anything judged by eye. He was shown nothing else: no numbers, no stylesheets, no table.

## 2. What shipped as a result, v0.64.1

| Stylesheet | Declarations | Now tokens | Moved |
|---|---|---|---|
| `knowledge-hub.css` | 36 | 36 | 21 |
| `book-note.css` | 20 | 20 | 8 |

**The sizes that moved**, all of them visible in the comparison he ruled from: the article title 36 to 33, its body 17 to 16, its sub-headings 20 to 21, the section title 22 to 21, the hub and listing titles 32 to 33 with their phone variants 26 to 24; the book note title 34 to 33, its author line 19 to 18, its lead and body 17 to 16.

**Taken from the generated override the sitting rendered, not re-derived**, so what shipped is what his eye passed rather than a second calculation that agreed with it.

**font-size only.** No weight and no line height, per brief section 2. Every responsive rule kept its own step.

## 3. Proof

- `css_gate.py`: PASS on all stylesheets.
- Deployed at v0.64.1, `deploy.py` proving all three of its checks: server identical to local, zip matching the theme at 402 files, server reporting 0.64.1.
- Read back from the rendered live pages with `getComputedStyle`: article title 33, meta 14, body 16, h2 24, h3 21, pill 12, source book title 16 and author 12; book note title 42 at desktop, overline 12, author 18, lead 16, body 16. No broken images on either page.

## 4. The fold-back, and why there is no prototype this time

Rule 14's fold-back asks for the approved artefact exported into the component's design folder as the prototype's next version. **Typography is a design foundation rather than a component**, so there is no component folder and no data file to write. That is the S056 precedent, recorded in `RULING__The_Nine_Step_Type_Scale_Approved_S056.md` section 3, and it is followed here rather than reopened.

**What stands in its place** is the sitting itself, version controlled in the theme repository:

| File | What it is |
|---|---|
| `previews/build_type_scale_comparison.py` | The instrument. Fetches the live page, generates the override, writes the sitting |
| `previews/kh-article-before.html` and `-after.html` | The Knowledge Hub pair he ruled on |
| `previews/book-note-before.html` and `-after.html` | The book note pair he ruled on |
| `previews/type-scale-sitting-2.html` | The tabbed page he looked at |

The scale's permanent home remains DSRD 7 section 3, which is yours to write.

## 5. Three faults the instrument had, found by testing it rather than trusting it

Recorded because the pattern is the one this project keeps meeting, and because each was caught before Kain saw it rather than by him.

**The fetch was answered with a captcha stub and the build reported success.** SiteGround's bot protection returned 252 bytes to a plain request from this machine. The before and after were written, they differed correctly, and every panel was empty. Nothing could tell, because a 252 byte HTML document is a valid HTML document. **The fix is not a different user agent**, which would be dressing a script up as a browser to get past bot protection on a site that takes card payments. The page is now fetched over SSH from the server itself, and any response under ten thousand bytes stops the build instead of being rendered.

**Emitting only the off-scale declarations deleted a responsive step.** The article title is 36px with a media query taking it to 28px on a phone. 36 is off the scale and 28 is on it, so only the 36 was emitted, it landed after the media rule in the cascade, and the phone title became 33. The override now emits every font size in source order, so the cascade matches the theme's own and nothing can be flattened by accident. Brief section 10 puts the responsive rule outside this sweep, and this is what keeping that boundary mechanically looks like.

**The panels shrank with the window and crossed the 767px breakpoint.** At a narrow window both sides sat at the phone size and the change under judgement was invisible. Panels are now pinned at 900px and the row scrolls instead, so the window cannot decide what is being judged.

## 6. Where the sweep stands

Four bodies of work are on the scale: the shared foundation, the policy family, the Knowledge Hub, and book notes. **91 declarations are tokens, 136 are still off the scale**, in `cards.css` (41), `about.css` (24), `people.css` (12), `help.css` (13), `reviews.css` (11), `components.css` (8), `footer.css` (7), `header.css` (6), `testimonials.css` (3), `global-impact.css` (2), plus the 9 policy watermark sizes which are the named exception and stay.

Next in the brief's order: help, then About, reviews and testimonials, then header and footer last. Each returns as its own sitting; none of them ships on an existing approval.

*No em or en dashes in this file; checked before writing.*
