**DISPOSITION (Chat, S276, 17 August 2026): acted on and archived.** The five admin chrome commits and the v0.61.8 to v0.61.12 theme move were written onto the board card "Build WordPress Back End in theme", verified by read-back; no admin chrome card exists and that card owns the back end. The one decision this file named for Chat, whether admin chrome becomes a recorded component, was already ruled by Kain at S275: it does not, and that ruling sits in RULINGS__S059_Addenda_Answered_S275.md in FROM Chat. Cards moved: 1.

---

# ADDENDUM 3 to SESSION_REPORT__S059: the top bar, the dashboard, and the close

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Extends:** `SESSION_REPORT__S059.md` and its two earlier addenda, which carried the work to v0.61.7.
**Theme:** v0.61.7 to **v0.61.12**. Final state: local, server and zip all agree, all three repositories clean and pushed.

---

## What was added, from the log

| Commit | Version | What |
|---|---|---|
| `a6755e0` | 0.61.8 | Top bar: comments bubble and WordPress logo menu removed, "+ New" trimmed to what is made by hand |
| `26f39a0` | 0.61.9 | Dashboard: welcome panel and Quick Draft removed, Rank Math's blog feed unhooked |
| `18c782c` | 0.61.10 | The Achology community panel, top of the dashboard side column |
| `e3876e3` | 0.61.11 | Community link set; Activity and WordPress Events and News removed |
| `1c4a35f` | 0.61.12 | Community shortcut points at the community feed |

**Board:** all five sit on the Schools and Courses side tabs card, or wherever Chat prefers to keep admin chrome.

## The principle applied, since it will be asked

Four boxes were removed and one added, and the difference is not taste. **The test was whether Kain would act on it.** WordPress selling block themes, Rank Math selling its blog, an Activity list of posts and comments that do not exist, and WordPress meetup news all failed it. A door to the Circle community he works in daily passes it.

Rank Math's feed was removed **at its own hook rather than hidden with CSS**, which keeps the widget's real numbers and stops the dashboard making an HTTP request to rankmath.com in order to draw.

## The cutover finding, filed separately

`CUTOVER__Dormant_Capability_To_Switch_On_At_Launch_S059.md`. The short version: **nothing needs buying.** Image compression, WebP and lazy loading are installed and unset; security is running; Rank Math already holds the live Analytics property with the module off.

**That last one is a hazard, not a gap.** The build ground is configured with `G-HJ29S4Z0R8`, stream `achology.com`. The only thing keeping test traffic out of live analytics is that the module is off. It belongs beside the noindex carve-out as a build-ground rule.

## Two things that came out of Kain's questions rather than my checks

**"Are all of the hairlines we need there?"** exposed three WordPress separators falling through unplaced. **"Another hairline between WordPress and plugins?"** exposed the tail being interleaved rather than merely unseparated. Both are in addendum 2.

**And at the close, "confirm what the next session needs to be" exposed a wrong statement in a report I had already filed.** See `CORRECTION__The_Cards_Workbench_Is_Not_A_404_S059.md`. The sweep is startable; the specimen page works and always did.

## One decision named for Chat rather than taken

Admin chrome now carries real design decisions: an order, six rules, a colour scheme and a panel. **It has no prototype and no data file, because it is not a site component.** Whether it should become one is a decision, not an omission. If it stays unrecorded, the next person to touch this menu has these commit messages and nothing else.

## The state at close

| | |
|---|---|
| Theme | v0.61.12, deployed, zip rebuilt, all three proofs current |
| Repositories | theme, written record and component prototypes: all clean, all pushed |
| FROM Chat | 12 live |
| Placeholders left in the project | 320, draining since the iCloud fix |

*No em or en dashes in this file; checked before writing.*
