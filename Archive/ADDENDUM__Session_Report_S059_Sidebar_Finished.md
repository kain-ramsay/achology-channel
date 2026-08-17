**DISPOSITION (S275, written at archive):** read at the S275 close. One question it carried (should admin chrome become a recorded component) was put to Kain and ruled NO; the ruling travelled to Code in RULINGS__S059_Addenda_Answered_S275.md (FROM Chat). Theme version v0.61.7 carried into the S275 handover from this file. Board cards moved: none (the four commits sit on the Schools and Courses side tabs card per Code's own note).

# ADDENDUM 2 to SESSION_REPORT__S059: the admin sidebar, finished and approved

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Extends:** `SESSION_REPORT__S059.md` and `ADDENDUM__Session_Report_S059_Three_Admin_Changes.md`, which carried the work to v0.61.3.
**Theme:** v0.61.3 to **v0.61.7**, four further commits, all pushed and deployed.
**Approved:** Kain, on his own screen, in his words: "the changes you have made work, and look great".

---

## What was added, from the log

| Commit | Version | What |
|---|---|---|
| `52b7c94` | 0.61.4 | WordPress's own three separators removed, so the group rules are the only lines |
| `0d3bc13` | 0.61.5 | The tail sorted: WordPress administration gathered and separated from the plugins, sixth hairline |
| `94609a6` | 0.61.6 | Glyph icons take brand orange, plugin logos untouched |
| `5c00377` | 0.61.7 | Icons alternate orange and white by group |

**Board:** all four sit on the Schools and Courses side tabs card.

## The two defects Kain's questions exposed, both mine

**"Are all of the hairlines we need on the dashboard menu?"** WordPress ships three separators of its own. The new order stopped naming them but never removed them, so all three fell through to the foot: one drawing a second line hard against the last rule, the other two scattering among the plugins. **My verification had passed because I tested the ordering function against a short hand-made list containing no separators and no plugins.** A test built from the same assumption as the code cannot find the assumption. Fixed at 0.61.4 by removing them outright, since the groups now carry their own.

**"Another hairline to separate WordPress from plugins?"** A hairline alone would have drawn a neat line through a jumbled list: the tail ran three plugin menus, then the five WordPress items, then four more plugin menus, because a plugin takes whatever position it asks for. Fixed at 0.61.5 by naming the five WordPress core slugs and letting every plugin fall through after, so **a plugin installed next year lands in the plugin group with no edit to this file.**

## One value measured rather than assumed

Brand orange `#ED6922` on the sidebar's `#1d2327` gives **5.03:1**, well past the 3:1 an icon needs.

**The AA-safe orange `#B8460F` gives only 2.97:1 here and would have failed.** That value exists for small text on white; the rule does not transfer to a glyph on a dark ground. Worth recording because the obvious move was to reach for the "safe" orange, and the obvious move was wrong.

## The alternation, and why it is not decoration

Kain asked for the tint to alternate group by group, his reason being that every dashboard a developer has handed him has been a jumble. **The hairline says where a group ends; the alternating tint says which rows belong together without the eye having to find the line first.** White is the base and orange is applied per group, which also means a plugin drawing a plain glyph sits quietly with the plugin block rather than borrowing the brand colour.

The tint is set as a class on the menu row keyed on the slug, not as a stylesheet of guessed element IDs: WordPress builds those IDs by sanitising the slug, which for the two academy tabs produces something nobody would predict correctly twice.

## One thing worth carrying, about verification

**I could not verify this work myself and said so each time.** WordPress only assembles that sidebar inside a logged-in browser session, and the command-line view builds only part of it. Kain checked it on his own screen and approved it there.

That is the honest shape of the two-surfaces rule for admin chrome: **the admin sidebar has no prototype and no data file, because it is not a site component**, so there is nothing to fold back under Rule 14 beyond this record. If Chat wants admin chrome to become a recorded component, that is a decision rather than an omission, and it should be taken deliberately.

*No em or en dashes in this file; checked before writing.*
