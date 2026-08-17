# RECORD: the four About rulings and the photo swap, verified on the live page. One question back.

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Closes:** `INSTRUCTION__About_Four_Rulings_From_Kains_Viewing.md` and
`INSTRUCTION__About_Image_Swap_Support_Team_Photo.md`, both S238.
**Verified against:** the rendered page at https://achologytest.com/about/, read this
turn at desktop and phone width. Not read from the source, not from memory.

## The state I found

**All four rulings and the photo swap were already built**, by S044 and S045, and are
live now at v0.38.11. I made no code change under this instruction. What follows is
verification, not a claim of new work.

| ruling | state on the rendered page |
|---|---|
| 1. Remove the visible page-updated line | **Gone.** No visible date anywhere on the page. `datePublished` and `dateModified` remain in the JSON-LD, reading from the single `ACH_ABOUT_MODIFIED` value, so page and schema cannot disagree. |
| 2. Every button on the DSRD 7 §5.1 system | **Audited in full. One question, below.** |
| 3. The hero hairline narrower at desktop | **Built.** Above 1024px the line is carried by the copy block and stops where the photograph's column begins, so it no longer runs the full width. Below that it stretches full width as Kain ruled. |
| 4. The phone hero treatment | **Built.** At 599.98px and under the photograph sits behind the text at 12 percent opacity, decorative, taking no pointer events. It shares the exact breakpoint of the header stack, which was the seam Kain caught. |
| Photo swap | **Done.** The lower instance is now `achology-customer-support-team.webp`, alt "Four members of the Achology customer support team wearing headsets at their desks". The founders block keeps the founders photograph. |

## Ruling 2, the audit, in full

Three buttons exist on the page. Every other clickable thing is a card row or an
accordion trigger, not a button.

| button | style built | Como 14/600 | radius 10px | icon | stroke |
|---|---|---|---|---|---|
| Read the Achology Story (hero) | secondary outline, #354149 border and text | yes | yes | ArrowDown | 1.75 |
| Read the Founders' Letter | secondary outline, #354149 border and text | yes | yes | ArrowRight | 1.75 |
| Submit an Enquiry Here | primary solid, #ED6922, white text | yes | yes | ArrowRight | 1.75 |

**Against §5.1 all three conform.** Type, size, weight, radius and colours match the
system; every icon is a registered Lucide icon at the one stroke weight.

**The pairing rule does not bite on this page.** I checked: no two buttons share a
parent, so there is no side-by-side pair to contrast. §5.1's pairing sentence, read
this turn: "Where two buttons sit side by side as a pair, they contrast: one primary
solid and one secondary or ghost, never two of the same style."

## The question, which is not mine to answer

Two of the three do not match the **variant the signed addenda named**, even though
both sit inside the system.

- **Addendum A** says of the hero action: "**Style:** primary solid button per DSRD 7
  section 5.1. Background #ED6922, white text." It is built **secondary outline**.
- **Addendum B part 1** says of the founders link: "**Link:** ghost style per DSRD 7
  section 5.1: 'Read the Founders' Letter' in brand orange." It is built **secondary
  outline**, dark rather than orange, and as a bordered button rather than a ghost.

Two signed instructions point different ways and neither overrides the other in
writing. The S237 addenda name specific variants. The S238 ruling says buttons are
uniform and buttons doing the same kind of job look the same, which is what the build
now does: the page's one real action, the enquiry, is the only solid button, and the
two navigational controls are outlines beneath it.

That is a defensible reading and it may well be what a later session intended, but it
is not written down anywhere, so under Rule 5 I have not decided it and have not
changed the buttons. It needs one line from Kain:

**Does the hero action go back to primary solid and the founders link to an orange
ghost, as the addenda specify? Or does the S238 uniformity ruling stand, leaving the
enquiry button as the page's only solid one?**

I recommend leaving it as built. A page with two solid orange buttons above a third
loses the hierarchy that makes the enquiry read as the thing to do. But it is his
page and his call, and the addenda are signed, so the build is currently at odds with
a signed document and that should not sit unrecorded.

## What is still outstanding on About, and why

The items assigned to `shared-parts.php` at S044 are still not built: the courses card
wording, the three gateway rules, the flagship card's Diploma name, the five video
labels and the five Vimeo-ID filenames. That file renders /testimonials/ as well as
/about/, which makes it a two-page change and a sweep under Rule 3. **One sweep brief
naming both pages releases all of it in a single pass.** It has been waiting since
S044 and it is the last thing standing between this page and its full DSRD 6 record.

*No em or en dashes in this file; checked before writing.*
