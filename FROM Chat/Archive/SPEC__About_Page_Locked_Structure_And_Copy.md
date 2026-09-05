# SIGNED SPEC: The About Page (/about/)

**From:** Claude Chat, S237. **Date:** 2026-08-04. **Approved by:** Kain Ramsay, S237.
**Answers:** `RECORD__Page_about.md` (your S043 walk, page 11).
**Status when this file lands in FROM Chat: signed.** This spec is the entire instruction. Build exactly this, nothing more. Where anything is unclear, stop and ask through the channel. Two visual addenda follow through the channel (section 10); do not build those two elements until they arrive.

---

## 1. The page's job

This page exists to get a visitor who is weighing up Achology to trust it enough to take one next step, whether that is a course, the free events, or reading deeper into who we are. It builds trust and routes; it does not close a sale.

## 2. The locked structure (top to bottom)

Kain reviewed the full built page and locked this order in S237. This is also the mobile order.

1. Site header
2. Breadcrumb
3. Hero: "About Achology" heading, intro paragraph, building photo, plus ONE new action (section 10, addendum A)
4. "Achology: What It Is, and Who It's For": intro plus the five questions and answers
5. "The Thinking that Drives Achology": the four document cards
6. "The Achology Story": the scrolling timeline, dark stage, thirteen milestones, statistics panel. The scroll behaviour is locked as built; nothing about its mechanics changes
7. "Five Aspects of the Achology Experience": the five member videos and the note beneath them
8. NEW: the founders block (section 5)
9. "Explore and Experience Achology for Yourself": the ten gateway cards, unchanged in number and layout
10. NEW: the closing enquiries panel (section 10, addendum B)
11. Page-updated date line (section 7)
12. Site footer

No section is removed and no section moves. The two new elements are the only structural additions.

## 3. Name corrections (canonical sources opened S237)

1. **The Diploma.** The page writes "Diploma in Modern Applied Psychology" in three places: the gateway flagship card, and the 2019 timeline milestone title and description. All three become the DSRD 5 canonical name exactly: **Diploma Course in Modern Applied Psychology (DiMAP)**. On second and later mentions within one block, DiMAP alone is fine once the full name has appeared.
2. **The Academy.** "Academy of Applied Psychology" (2014 milestone) and "Academy of Modern Psychology" (wherever it appears in the body) both become **The Academy of Modern Applied Psychology**.
3. **Circle.** The platform is written **Circle.io** consistently everywhere on the page; no second form.

The seven school names in the site header and footer are ALSO wrong against DSRD 5, but they are site-wide chrome and are excluded from this change set. They arrive as their own sweep brief.

## 4. Copy corrections (approved word for word, Kain S237)

1. **Meta description:** the student figure becomes **695,578**, matching the page body and its schema. Keep the description within its current healthy length; propose the exact revised string back through the channel with the rendered page.
2. **Abbreviations, page body only:** every abbreviation is spelled out at its first body use, then used freely after. At minimum: continuing professional development (CPD); Provider Reference Number (PRN); Information Commissioner's Office (ICO); artificial intelligence (AI); United Kingdom (UK); frequently asked questions (FAQs). Header and footer instances are chrome and wait for the sweep brief.
3. **Terms a stranger cannot decode:** at its first body use, "Achologist" is introduced in plain words (an Achologist is a member progressing through Achology's competency development pathway, or Kain's preferred phrasing when he reviews the rendered page); "membership" gets one plain first-use introduction the same way. After the first use, both terms run free.
4. **The courses gateway card** description becomes exactly: "Twenty-eight unique on-demand training courses, teaching psychology you can use in everyday life and work."
5. **The note under the five videos** becomes exactly: "To hear more members share their experiences in their own words, visit our Member Testimonials page."
6. **Era date ranges:** all six era ranges on the page (the dark stage at rest, the era chart labels, and the group headings in the track) are written in the form **2012 to 2014**. No en dash survives anywhere on the page. Chat corrects the timeline section of DSRD 9 to match; you do not touch the DSRDs.
7. **Three sentences with missing words, and one number described three different ways** (your S043 walk findings): send the exact current sentences through TO Chat; Chat returns the approved corrections. Do not fix these with your own wording.

## 5. NEW: the founders block

Sits between the five member videos and the gateway. Content, approved S237:

- **Image:** `About Achology Page - Kain and Karen Main Image.png` (already in the theme asset folder: 04. Single Page Template Assets / About Achology Page). The circular framed portrait with the Founding Partners badge. Give it a descriptive filename on upload per DSRD 6 section 11.
- **Copy, three to four short lines:** Achology was founded by Kain and Karen Ramsay in 2017, why they built it (dissatisfaction with psychology taught as information to memorise rather than wisdom to live by), and that members meet them personally in monthly mentorship sessions and community events.
- **One link:** to the Founders' Letter at /about/founders-letter/.
- The exact copy travels with addendum B's approval, since Kain approves the block's words looking at the rendered block. Layout follows the page's existing block patterns; if no existing pattern fits an image-plus-copy block here, stop and ask through the channel.

Known and accepted: /about/founders-letter/ does not exist yet. Kain creates pages; the link ships pointing at its planned DSRD 1 address.

## 6. The gateway rules (approved S237)

The ten cards stay. Three mechanical rules now govern them:

1. **One destination per card.** A card carries exactly one link target. The $7 trial card currently points at two different destinations from this page; it gets one, the DSRD 4 checkout URL for the trial, copied exactly from DSRD 4.
2. **No two cards share a destination.** The two differently worded links that currently lead to the same place are resolved so each destination appears once. Report the resolution through the channel if any case is ambiguous.
3. **Consistent link behaviour.** Internal links open in the same tab; external links open in a new tab with rel noopener, per DSRD 3. No link behaves differently from its twin.

The "Meet Achology's Founders" gateway card stays as built (Kain's ruling, S237), alongside the new founders block.

## 7. Machine visibility (the S237 standard, now DSRD 3 section 2.4)

1. **The five question answers ship in the delivered code, readable from first load.** The click-to-reveal selector becomes purely visual behaviour layered on top; no answer text is conditional on JavaScript or a click for its existence in the markup. On phone, the first answer starts open.
2. **A visible date line** sits at the foot of the page, above the footer: "Page updated" plus month and year, refreshed whenever the page genuinely changes. Wire datePublished and dateModified into the page's JSON-LD at the same time.
3. The accreditation answer that quotes the UK Register of Learning Providers registration number now links the register itself.

## 8. Accessibility fixes (this page's own, from your S043 record)

1. The question selector emits each answer directly after its question in source order; no more all-questions-then-all-answers.
2. The video lightbox gets a real focus trap to match its dialog role, and the page behind it becomes unreachable while it is open.
3. The selector drops the arrow-key roving-focus tablist behaviour, or adopts honest accordion semantics; it announces what it is.
4. The one wrong alt text (describing a scene the photograph does not show) is corrected; propose the new alt through the channel with the render.
5. The five body images named by bare Vimeo IDs get descriptive plain-word filenames (the DSRD 6 section 11 item your record flags as the one that cannot be fixed cheaply later).
6. The seven clipped timeline-track links your record found are made reachable or removed from tab order, whichever the built scroll mechanic supports; report which through the channel.

## 9. The five member videos

Each of the five videos gains a visible text label directly beneath it: its question, in real text, exactly as currently baked into the poster image. The posters stay as they are for now; the text label is the machine-readable and reader-visible source of truth from this build on.

## 10. Two visual addenda (do not build these elements until they arrive)

- **Addendum A, the hero action:** one action in the hero, scrolling the reader down to The Achology Story. Kain picks the wording and treatment from rendered options; the addendum carries his choice.
- **Addendum B, the closing enquiries panel:** a new closing element after the gateway, one heading, one line, one button to /enquiries/ (DSRD 1 address; page not yet created, same acceptance as the Founders' Letter link). It is being designed as a shared site-wide component with per-page message; the addendum carries the approved design and exact copy, plus the founders block copy. Also arriving with it: a back-to-top control for phone (the page runs roughly seventeen screenfuls at phone width), rendered and approved the same way.

Everything else in this spec is buildable now.

## 11. Rulings recorded (context, no build action)

- Schema: DSRD 10 governs per-page schema; the built page (AboutPage plus BreadcrumbList) is correct as it stands. Chat amends DSRD 3's table to point at DSRD 10.
- The prospectus is removed from the About page's requirements; DSRD 1 and DSRD 2 are amended on Chat's side. No prospectus element is built.
- DSRD 6 section 6's "four signals" count becomes five on Chat's side.
- The phone-tier spacing separators and the header/footer chrome (school names, abbreviations) are excluded from this change set and arrive as two separate sweep briefs.
- The six 404 destinations and the /membership/ redirect your record lists are site state, not template defects; Kain creates those pages in their turn. No change to the links in this build beyond the gateway rules in section 6.

## 12. Definition of done

The page rebuilt to this spec as its own change set under the harness, re-gated, the changed parts re-walked, the DSRD 6 record refreshed in place, the theme zip rebuilt for Kain to upload, and the rendered page returned through TO Chat for Kain to view in Safari, together with the proposed meta description string, the three defect sentences (section 4 item 7), and any channel questions this spec names. The two addenda elements are built only once their addenda land in FROM Chat.

*No em or en dashes in this file; checked before writing.*
