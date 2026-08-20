# BRIEF: the six Community Eldership biographies, approved by Kain. HOLD until the Vimeo run is finished.

**From:** Claude Chat, Session 296. **Date:** 20 August 2026.
**Do not start this until the course description and Vimeo work is done.** Kain's instruction, S296. This sits in the queue behind it.

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

*No em or en dashes in this file; checked before writing.*
