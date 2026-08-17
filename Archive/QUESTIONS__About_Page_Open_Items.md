# QUESTIONS: the About page's open items, S044

**From:** Claude Code, S044. **Date:** 2026-08-04.
**Against:** `SPEC__About_Page_Locked_Structure_And_Copy.md` and its addenda. Everything here is either a thing the spec asks me to send you, or a thing the spec does not cover. Nothing below was decided by me.

---

## 1. Waiting on ruling: one sweep brief releases the rest of the spec

Five spec items land in `shared-parts.php`, and that file renders /testimonials/ as well as /about/. Editing it changes two pages, which is a sweep under Rule 3 and needs a brief naming them. This is the single largest gap between the spec and what shipped.

Held in `achology_site_routes()` and `achology_member_story_cards()`:

1. §3.1, the flagship gateway card's "Diploma in Modern Applied Psychology". The two timeline instances are done; this third one is shared.
2. §4.4, the courses card description.
3. §6, all three gateway rules: one destination per card, no two cards sharing a destination, consistent link behaviour. On the built set, /pricing/ is the destination of both "Review Achology's Pricing" and "Unlock Full Access for $7", which is §6 rule 2 exactly.
4. §9, the visible question label under each of the five videos. The renderer and the question strings are both shared.
5. §8.5, the five Vimeo-ID poster filenames. The files and the paths that name them are shared.

**Ask:** one sweep brief naming /about/ and /testimonials/, covering the five items above. They are one pass in one file.

## 2. §4 item 7: the sentences with missing words, exact and current

The S043 walk output is not preserved, so these are re-read from the live copy this session rather than copied from the walk, and I have found two of the three. Both are in the shared routes set, so they travel with the sweep brief above.

1. "Simple, transparent and flexible payment options for Achology full range of course and subscription options."
2. "Get 30-day trial of the Achology membership community today for less than the price two small cappuccinos."

If your copy of the S043 walk names a third, send it and I will quote it back rather than guess at which sentence was meant.

**The one number described three different ways.** The count of courses:

- the statistics panel prints the numeral: **28**, "Total Number of Courses"
- the courses gateway card spells it: **"Twenty-eight unique training courses"**
- the same card then breaks it down as **9 + 9 + 12**, which is **30**, not 28
- and the 2022 milestone says the curriculum "expands to 25 courses, including 8 in-depth practitioner-level training programmes"

The breakdown contradicting its own total is the part a reader would actually notice. All of it is either the shared card or approved timeline copy, so none of it was touched.

## 3. §4 item 1: the proposed meta description

The page's own AboutPage JSON-LD already carries the corrected figure, and the template's docblock requires the two to stay in step. So the proposal is that string exactly, which makes them identical rather than merely consistent:

> About Achology: a decade teaching applied psychology to 695,578 students in 216 countries. What we teach, what we stand for, and who it's for.

140 characters. It lives in Rank Math post meta on page 184, which is page data rather than theme code, so it is set in the editor and not by me.

## 4. §8 item 4: the proposed alt text

The S043 record says one image's alt describes a scene the photograph does not show, but does not name which. Re-reading the seven body images this session, the only alt asserting something the photograph cannot establish is the header image, which called the building "the academy's glass-fronted entrance". Achology is an online academy; the photograph shows a building with the logo on it, and nothing establishes it as Achology's premises. Changed to:

> The Achology logo on the fascia above the glass entrance of a modern building

**Confirm this is the one the walk meant.** If it named a different image, say which and I will correct that one instead and put this back.

## 5. DSRD 6 §10 verdicts needed on five values the addenda specify

Kain approved every one of these rendered by eye, so they are built exactly as approved, not collapsed. But §10 is explicit that a comment is not a resolution: "Justifying an unnamed value in a comment and leaving it in place is not one of the three." They need verdict 2, "Name it", or verdict 3, a recorded exception.

| Value | Where | DSRD 7 today |
|---|---|---|
| Como 28px / 700 heading | founders block, warm room | §3 names 28px/700 only as "Stats Large, Social proof values". Every other section heading on the page renders 24px/600 |
| Source Sans 3 17px / 1.65 | founders body | §3 names no 17px body role. `.pfq-ans` already uses 17px, unnamed, one of the 27 the S043 walk counted |
| Source Sans 3 17px / 1.6 | warm room body | as above |
| 16px corner radius | warm room panel | §5 names 12px card and 10px button and input only |
| `0 4px 14px rgba(53,65,73,0.25)` and its deeper press state | back-to-top | §5.4 names shadows for cards, mini cards, dropdowns and the dark stage. None for a floating control |

My reading is that all five are verdict 2: they are a real need the system has not met yet, and naming them lets the next page reach for them. That is Kain's call and your edit, not mine.

## 6. Waiting on ruling: the upper `.tw-wrap` boundary

The S238 sweep brief assigns `.pfq` and `.tw-wrap` to this change set. Three of their four boundaries are now conformant at all three widths. The fourth cannot be fixed without a ruling.

The hairline at the top of the story block reads 48 above and 32 below at desktop, where §4.3 ruling 4 wants 48/48. The 32 below is `.tw-frame`'s own `padding-top`, and `.tw-frame` is the pinned sticky frame. §4.3's one-owner rule says that padding should move onto `.tw-wrap`; the About spec §2 says "The scroll behaviour is locked as built; nothing about its mechanics changes". Moving it changes what the frame paints as it scrolls under the header.

**Ask:** which wins. At phone the same boundary already reads 32/32 and is conformant, so this is a desktop and tablet question only.

## 7. The locked structure does not name a block that is on the page

Spec §2 lists twelve items and says "No section is removed and no section moves". The built page also carries "About Achology Related Questions", the eight-question `.help-popular` block, sitting after the gateway. It is in neither the list nor the removals. The evaluator checklist item 1 asks for "nothing present the spec does not name", so as written the page fails that line whatever I do.

I kept it, because §2 forbids removing a section. **Confirm** it belongs in the locked list, or that it goes.

## 8. Where the closing panel sits

Addendum B says the panel sits "after the gateway, before the page-updated date line". Both are true of two positions, because the Related Questions block sits between them. I placed it last, so the page's final ask is an action rather than another list of links, which is what the S043 walk found missing. **Confirm or move it**; it is a one-line change either way.

## 9. WITHDRAWN: page_gate v3 was already built and ruled

I wrote this as still open on the strength of the S043 record's "waiting on ruling" line, and your `ANSWER__S044_Items_Chat_Can_Close_Now.md` is right that it is closed. Read from the script this turn:

> `v3 (S043, Kain-authorised): the mirror replays the origin's real HTTP status`

I trusted a record over the tool it describes. Left visible rather than deleted, because the same stale line sits in `RECORD__Page_about.md`.

## 9b. NEW, and it matters more than the item it replaces: the gate cannot see a cached page

**The first page_gate run against the rebuilt About page reported 26 pass, 3 fail, and was measuring the previous build.** SiteGround's dynamic cache was serving the old HTML. The deployed file was byte-identical to mine, the version string had moved, and the page the gate read had none of the new work in it.

What gave it away was luck rather than method: the gate reported five en dashes, and I knew the six era ranges were gone from the source. Without that thread to pull, a clean-looking gate printout would have gone into the record as verification of work that was not on the page.

This is the same class of defect as the mirror's blanket 200, and it is the one DSRD 6 §11 is written against: an instrument reporting confidently on something it is not looking at. `page_gate` reads the origin, the origin serves cache, and nothing in the gate can tell fresh from stale.

**What I did:** purge the cache before every gate run (`wp sg purge` over SSH). Every number in this session's records was obtained that way, and the honest run was 35 pass, 4 fail.

**What it needs, and it is your ruling:** page_gate purges before it measures, so nobody has to remember. Small change to the script, and I will not touch it without your word.

**Worth checking on your side:** whether any record already filed was gated against a cached page. The Policies index re-gates in particular were run in the same session as a deploy.

## 10. Noted, no action needed

The founders letter and enquiries links ship pointing at pages that do not exist yet, per the spec's own acceptance. The S238 chrome brief dissolves the §1 chrome findings in the About record, and I will re-verdict that row when I refresh the record after the upload.

*No em or en dashes in this file; checked before writing.*
