# COMMISSION: Harvest the theme's true component census (Act 1 of the five-part component-truth fix)

**From:** Claude Chat, Session 266, on Kain's approval of the whole solution. **Date:** 2026-08-12.
**Fires under:** standing rule 10, problem-interrupt. Kain named the problem this session; this is the first act of the agreed fix.

## The problem, so this message stands alone

Nothing in this project can answer the question "what exists that has no record?" DSRD 8 is prose about components. The theme is code that implements them. No component's record carries the class family that identifies it in the code, so no comparison is possible in either direction. Every list either environment produces is a list of what somebody remembered to write down, and a forgotten component is invisible by definition. Sampling cannot find it, because sampling draws from the list and the list is the broken part.

Evidence, found by Chat this session by reading the theme stylesheets directly. Six class families are live in the theme and named nowhere in DSRD 8:

| Class family | File | Where it renders |
|---|---|---|
| `.author-card` | people.css | Knowledge Hub article pages and Book Note pages. This is the pen-name signature card. Never designed with Kain, never ruled |
| `.pp-card` | people.css | Our People page profile cards |
| `.navcard` | header.css | The header dropdown design boxes. DSRD 8 s18.8 describes the format in prose but never names the class |
| `.nudge-card` | header.css | The header dropdown nudge box. DSRD 8 s18.12 describes it in prose, class never named |
| `.cta-card` | footer.css | The footer CTA box. DSRD 8 s19.7 describes it in prose, class never named |
| `.shared-video-lightbox` | components.css | The panel testimonial videos open into |

Also: `.card--course` is used in book-note.css, so the course card is being reused outside the commerce pages and no document records that.

The Component Registry created at S265 was meant to be the join between record and code. It was populated from DSRD 8's prose, which is the incomplete thing, so it inherited the same blind spot: thirteen rows against a theme carrying at least six unrecorded families.

## The agreed solution, all five parts

Kain approved the whole solution at S266. Recorded here in full so both environments hold the same picture.

1. **The census flips direction.** The code counts itself. Every class family in the theme's stylesheets is harvested mechanically, and that harvest is the census. A component that exists has classes, and classes cannot hide.
2. **Every family gets one of three dispositions:** library component, page-local block (the DSRD 8 s12 category, which already exists), or utility. Nothing sits unfiled. This is what separates furniture from components, and it needs a human ruling, not a rule.
3. **Every component row carries four artefacts, and a missing one prints:** class prefix, approved prototype, build sheet, DSRD 8 decision section. A gap prints as a visible NOT RECORDED line, never as a blank. Same blind-spot direction Kain ruled at S265 for the DSRD 6 scoreboard.
4. **The birth gate.** A new class family cannot enter the theme without its registry row; the hook machinery fails the build. This is what makes the fix permanent rather than a one-off tidy.
5. **DSRD 8 stops being read as the census.** S257 demoted it to decision history but nothing took over its inventory job, so both environments kept reading it as one. The registry becomes the named census and DSRD 8's opening line says so, so a Claude reading it cold cannot repeat the error.

Once proven on components, the same mechanism points at pages (templates against signed specs and DSRD 6 records) unchanged. Built once, not twice.

## Act 1: your work in this commission

This is the harvest only. Parts 2 to 5 follow once the true size is known, and part 2 needs Kain, not you.

1. **Harvest every class family from every stylesheet in the theme.** All of them, not the ones you expect: base.css, cards.css, components.css, header.css, footer.css, about.css, people.css, help.css, policies.css, reviews.css, testimonials.css, book-note.css, knowledge-hub.css, global-impact.css, fonts.css, style.css, and any file that arrives after this is written. Group to family level (the prefix before `__` or `--`), not to individual selector, so `.card__title` and `.card--mini` roll up to `card`.
2. **For each family, report as data:** the family prefix, the file or files declaring it, the selector count, the template or partial files that emit it, and whether the family appears anywhere in DSRD 8 (a plain text search is enough; you are reporting the fact, not judging it).
3. **Flag the split cases.** Where one family is declared across more than one stylesheet, say so, because that is either a shared component or a duplicated one and the difference matters.
4. **Do not judge disposition.** Library, page-local or utility is Kain's ruling in part 2, not yours. Report the facts and stop.
5. **Say what the harvest cost and how it ran,** so the same script can become the gate's census in part 4 rather than being written twice.

## Definition of done

A report in TO Chat carrying the full family table, the DSRD 8 presence column, the split-case flags, and the method. Nothing is written into the registry by you: Chat maintains it, and the rows land after Kain rules the dispositions.

## Sequencing

This runs ahead of the two commissions already in FROM Chat that touch components (the five commerce components for Safari ruling, and the shared blocks widening if it lands), because the harvest may reveal that those lists are themselves short. Take it before them.

*No em or en dashes in this file; checked before writing.*
