# ADDENDA A + B: The About Page Visual Elements (completes SPEC__About_Page_Locked_Structure_And_Copy.md)

**From:** Claude Chat, S237. **Date:** 2026-08-04. **Approved by:** Kain Ramsay, S237, every element judged rendered by eye.
**Status when this file lands in FROM Chat: signed.** With this file, the About page spec is complete and fully buildable. Where anything is unclear, stop and ask through the channel.

---

## ADDENDUM A: the hero action

One button in the hero, below the intro paragraph, roughly 26px beneath it.

- **Style (corrected S243, Kain's ruling on the rendered page):** secondary outline button per DSRD 7 section 5.1. Border and text #354149, Como 14px weight 600, border radius 10px. The original S237 wording named a primary solid orange button; the built page carries an outline, and Kain ruled S243 that the build stands and this addendum is corrected to match. The reason is hierarchy: the closing enquiry button is the page's one solid orange action, and the two navigational controls above it are outlines, so the thing to do stands out. Hover per the system's secondary state.
- **Label:** Read the Achology Story
- **Icon:** Lucide ArrowDown, 16px, stroke 1.75, in the button's text colour, to the right of the label, 8px gap. Chat is registering ArrowDown (and ArrowUp, below) in the DSRD 7 section 5.2 icon registry; build once that edit is confirmed in the README change register.
- **Behaviour:** smooth scroll to The Achology Story section on the same page.

## ADDENDUM B, part 1: the founders block

Sits between the five member videos and the gateway, a hairline above and below at the page's standard spacing (48 above and below, 32 on phone).

- **Layout:** portrait left, text right, 64px gap. Portrait 340px square (the circular framed image fills it). Phone: stacked and centred, portrait 260px.
- **Image:** `About Achology Page - Kain and Karen Main Image.png` from 04. Single Page Template Assets / About Achology Page. Descriptive filename on upload. Alt text: "Kain and Karen Ramsay, founding partners of Achology.com".
- **Heading:** The People Behind Achology. Como 28px weight 700, brand dark, the word Achology in brand orange, matching the page's other section headings.
- **Body, exact and approved:** two paragraphs, Source Sans 3 17px, line height 1.65, brand dark:

  "Achology was founded by Kain and Karen Ramsay in 2017, motivated by a simple frustration: psychology was often taught as academic knowledge, mainly as theoretical data to memorise rather than as practical wisdom for everyday use."

  "Today, they run Achology from the central belt of Scotland, with members meeting them in person at mentorship sessions and events held throughout the year. Kain and Karen have been married since 2013 and have a daughter named Skye."

- **Link (corrected S243, Kain's ruling on the rendered page):** secondary outline button per DSRD 7 section 5.1, border and text #354149: "Read the Founders' Letter", Como 14px weight 600, Lucide ArrowRight 16px, gap 6px growing to 9px on hover. Destination /about/founders-letter/ (accepted pending page, per the spec). The original S237 wording named an orange ghost link; the built page carries an outline button, and Kain ruled S243 that the build stands and this addendum is corrected to match, for the same hierarchy reason given in Addendum A.

## ADDENDUM B, part 2: the closing enquiries panel ("the warm room")

Sits after the gateway, before the page-updated date line.

- **Panel:** background rgba(237,105,34,0.06) (the gateway's warm tint), border radius 16px, padding 56px, overflow hidden, with one decorative soft circle (460px, rgba(237,105,34,0.05)) bleeding off the top right corner.
- **Layout:** text left, portrait right (300px, the same founders image, with drop shadow 0 10px 28px rgba(53,65,73,0.16)), 48px gap. Phone: stacked and centred, portrait 250px.
- **Heading:** Como 28px weight 700, brand dark, Achology in brand orange: "Do you have a question about joining or studying with Achology?"
- **Body, exact and approved:** Source Sans 3 17px, line height 1.6, brand dark: "Achology is run by real people. Feel welcome to ask us any questions you have regarding the courses, membership, or how to get started, and we will respond as soon as possible."
- **Button:** primary solid, "Submit an Enquiry Here", Lucide ArrowRight 16px, destination /enquiries/ (accepted pending page, per the spec).
- **Component note:** this panel is intended as a future shared site-wide closing component with a per-page message. For THIS build it ships on the About page only; the shared component decision, its DSRD 8 entry, and its relationship to the existing help-contact closing panel are Chat's to bring to a component session. Do not generalise it yet.

## ADDENDUM B, part 3: the back-to-top control (phone)

- 46px circle, background brand orange, white Lucide ArrowUp 20px stroke 1.75, shadow 0 4px 14px rgba(53,65,73,0.25), fixed 22px from the right and bottom edges.
- Appears below 768px only, once the reader has scrolled past the hero; hidden at the top of the page. One tap returns to the top of the page.
- Hover and press: background #D85A1B, lifts 2px, shadow deepens.

## Definition of done

These three elements join the main spec's change set and its single definition of done: built under the harness, re-gated, the DSRD 6 record refreshed, the theme zip rebuilt, the rendered page returned through TO Chat with everything the main spec's section 12 lists.

*No em or en dashes in this file; checked before writing.*
