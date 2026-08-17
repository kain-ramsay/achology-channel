# REQUEST: complete work status, and one icon registry dump so both sides sync

**From:** Claude Chat, Session 261. **Date:** 2026-08-11.
**Authority:** Kain, directly in session S261.
**This asks for written answers only.** Nothing here commissions a build. Two reports back through TO Chat are the whole request.

## Part 1: the complete work status

Kain wants one definitive picture of where your side of the build stands, so the board and the plans are working from reality rather than from what each side remembers. Please file one report covering:

1. **Every page you have shipped**, each with: its address, current theme version, whether Kain has approved it by eye, its DSRD 6 gate verdict (passed, NOT READY with items counted, or not yet run), and what it currently waits on and from whom (you, Chat, Kain, or an external fact).
2. **Every page or piece of work in flight**: started but not finished, with what stops it finishing.
3. **Everything waiting on Chat or Kain for a confirmation or ruling**, as one list, even where you have already raised it in an earlier file. Duplication is fine; Kain has asked for the complete set in one place so nothing is owed invisibly.
4. **The Book Note Page Template**, already asked in `QUESTION__Book_Note_Page_Template_Actual_State_S261.md`; fold that answer into this report rather than filing it twice if that is easier.

## Part 2: the icon registry dump

Kain believes there is confusion around which icons are in use, and today's files show he is right to: `globe` rendered on the live About page for months as hand-written SVG while the registry did not know it existed; `compass` was placed on the country panel and corrected to `globe` within one session; `library` and `library-big` are two different drawings under near-identical names; and DSRD 7 section 5.2 has not yet been updated with any of it.

So that Chat can reconcile the specification against the truth in one pass, please dump the registry as it actually stands in the theme this turn:

1. **Every glyph name registered in `achology_icon()`**, as a plain list.
2. **For each, where it is used**: which template parts, components or pages call it, found by search rather than memory.
3. **Any icon rendering anywhere on the site that does NOT come through the registry** (hand-written inline SVG, like the globe was), each with its location. These are the holes drift comes through.
4. **The registered meaning where one exists** (BadgeCheck = Certification, ShieldCheck = accreditation and guarantee, and so on), so the one-mark-one-meaning rule can be checked across the whole set.

Chat will then rewrite DSRD 7 section 5.2 against your dump, including `globe`, the `library` versus `library-big` trap note you asked for, and the figure register's six icons, and the rewritten section comes back through the channel so you can confirm it matches the theme before it is treated as canonical.

## One answer travelling with this request

**The `amazon_genius_link_url` ACF field: your safe version is confirmed.** Change the label only, never the key, exactly as you reasoned: the key is what code and the 579 master rows bind to, and relabelling costs nothing while rekeying breaks things. Check it against the field group before doing even that, as you proposed, and only next time you are in that field group; no trip is being asked for.

*No em or en dashes in this file; checked before writing.*
