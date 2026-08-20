# BRIEF: the six Community Eldership biographies, approved by Kain. Do this as soon as you pick up the channel.

**From:** Claude Chat, Session 296. **Date:** 20 August 2026.
**Kain's instruction, S296: place the six biographies right away.** The earlier hold on this file is lifted. The Vimeo run still comes first if you are mid-course; this is a short job to take at the next clean break, not something to interrupt a run for.

**Closes:** the unapproved-copy warning you wrote into `people-setup.php` at S062, in your own words: "EVERY ROLE AND EVERY BIOGRAPHY BELOW IS DRAFTED BY CODE AND HAS NOT BEEN THROUGH KAIN OR CHAT."

PAGE GATE: /about/instructors/. Record: the Instructors folder. Chapter 1 re-read after the change.

---

## What happened

Chat ran the reading chapters on the Our People page at S296 and failed chapter 1 on this block. The six biographies were yours, the visible FILLER markers had been removed at Kain's S062 instruction, and the page was describing six real people in words nobody had approved.

**Kain has now written them.** Below is his copy. It replaces the `bio` field for all six.

## The six biographies

**alec-wells**
Alec is a Master Achologist and one of Achology's community elders, with thousands of hours of workshops and training behind him. He hosts events, mentors members through the practical side of their learning, and helps verify the record of practice other members build.

**andrew-nelson**
Andrew is a Master Achologist and one of Achology's community elders, having delivered thousands of hours of workshops and training. He hosts community events and works alongside new Achology members as they figure out how to put their learning into practice.

**erika-nadeau**
Erika, a Master Achologist and experienced Achology community elder, has conducted thousands of hours of workshops and training. She organises events, mentors members in their practice, and helps verify their submitted learning activities as an accreditation verifier.

**gaby-tzeschlock**
Gabriele (Gaby) is a Master Achologist and one of Achology's community elders, with thousands of hours of workshops and training to her name. She hosts community events, mentors members through their own practice, and helps verify the record of work they put forward.

**gary-kennedy**
Gary is a Master Achologist, former priest, and one of Achology's community elders, having delivered thousands of hours of workshops and training. He organises events, assists Achology members with their learning processes, and helps validate their record of practice.

**jonathon-frost**
Jonathon is a Master Achologist and one of Achology's community elders, with thousands of hours of workshops and training behind him. He hosts events, mentors members, and hosts regular weekly mentorship for Achology students who want to develop expert coaching skills.

## Two corrections Chat made to Kain's text, both mechanical

Named here rather than made silently, so he can overturn either.

1. **"organizes" became "organises"** in Gary's line. The site is UK English throughout, and Erika's line, written in the same pass, already reads "organises".
2. **"achology students" became "Achology students"** in Jonathon's line. The business name is capitalised everywhere else on the site.

Nothing else in his wording is altered. The rhythm, the length and the word choices are his.

## The name change, and what it does not touch

**Gabriele Tzeschlock is now her name on the page**, with Gaby in brackets at first mention. The community reference document has always called her Gabriele; the registry said Gaby.

**Update the `name` field to "Gabriele Tzeschlock". Leave the array key `gaby-tzeschlock` alone.** She carries `has_page` set to false, so the key builds no URL and no slug depends on it. Renaming the key would be a change with no visible effect and a real chance of breaking the photo lookup, which reads the key.

**Check the photo file resolves after the change.** `achology_person_photo()` builds its path from the key, so it should be unaffected, but confirm it rather than assume.

## The `line` field

Each person's one-sentence `line` is used by the author signature block, which these six never render because `has_page` is false. **Leave the six `line` fields as they are** unless the shorter form is showing somewhere Chat has not found. If it is, say so through the channel rather than writing new short lines yourself.

## Delete the warning

Once the six biographies are Kain's, **remove the unapproved-copy warning block from `people-setup.php`**, including the line about the FILLER markers. It has done its job. Keep the note recording that the shared role line is Kain's own wording.

## Definition of done

The six biographies on /about/instructors/ read exactly as above. The warning block is gone. Her name reads Gabriele (Gaby) and her photograph still loads. The rendered page comes back through the channel so Chat can re-read chapter 1 and Kain can see it in Safari.

## What this does not close

Chapter 1 still fails on two bare acronyms in role lines: CTO in Kain Ramsay's, and TAYA in Isabella S. Whitmore's. Both are registry strings and both are still with Kain. Do not fix either under this brief.

---

# PART TWO: WITHDRAWN S296. DO NOT BUILD THE LINKS FIELD.

**Kain ruled S296, minutes after this part was written: none of the six elders has a link to give, so the field is not built and the collection is dropped.**

Everything below this line is the withdrawn instruction, kept so nobody reinstates it from memory as a good idea that was never tried. **It was tried, briefly, and stopped for a reason: there is nothing to put in the field.**

**Build nothing from Part Two. Part One, the six biographies, stands and is the whole of this brief.**

## The withdrawn instruction, for the record only

Karen was asked to collect two links for each of the six elders, a personal website and a LinkedIn profile where they had both. The registry has no field for links, for any of the seventeen people, so one was to be added empty and filled when the values arrived.

The values are not coming. An empty field on seventeen people, serving nobody, is worse than no field: it reads as an unfinished job every time somebody opens the registry.

**If links are ever collected, this is the shape that was reasoned through**, and it can be picked up rather than re-derived: an ordered list per person, each entry carrying the label a reader sees and the address it goes to, flat rather than named slots so a third kind of page is not forced into the wrong box; and when the display is built, the addresses belong in the profile page's Person schema as `sameAs`, which is the whole reason they would be worth collecting.

*No em or en dashes in this file; checked before writing.*
