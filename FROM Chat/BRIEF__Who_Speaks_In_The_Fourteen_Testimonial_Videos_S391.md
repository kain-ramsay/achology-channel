**Needs from Code:** one read-only job on Vimeo, approved by Kain at S391. Return a list of who speaks in each of the fourteen banked testimonial videos, and each video's transcript. Build nothing on the site.

# BRIEF: who speaks in the fourteen testimonial videos, and what they say

**From:** Claude Chat, S391, Tuesday 29 September 2026. **To:** Claude Code.
**Kain's yes, S391:** "Yes, please do." Once this data exists, Kain and Chat decide how the videos are built into /testimonials/, and whether any belong elsewhere on the site too.
**Card:** "Finish Member Testimonials Page" (steps 3 and 4 of its Definition of Done).

## What these videos are

The fourteen videos in Vimeo folder 20119371 (user 71102328; shown in Kain's account as "2024 Testimonials (long)" under Member Testimonials). IDs, titles and lengths are in your own `DELIVERY__The_Fourteen_Testimonial_Videos_S084` (channel Archive). All fourteen already have achologytest.com on their embed whitelist (your S090 pass).

**What Kain told Chat at S391:** each video is not one member. It is several members, each answering that video's one question in turn. **Each speaker's name is shown on screen as a lower third.** Vimeo stores no speaker names; the description field is empty on all fourteen.

## The job

1. **Transcript.** For each video, read its text tracks through the Vimeo API. Use Kain's own caption track if one exists, otherwise Vimeo's automatic one. Where a video has none, make one from the audio. Keep timestamps.
2. **Speaker changes.** From the transcript's timing (and pauses or cuts, however you find them most reliably), find the moment each new member starts.
3. **Names.** At each change, take a still frame through Vimeo's API (thumbnails at a chosen time, or the smallest rendition you can reach) without downloading the multi-gigabyte files, and read the name from the lower third.
4. **Check against what the site already holds.** Compare each name with the nine members on /testimonials/ (`achology_member_voice_cards()`) and with the people registry (`people-setup.php`). Note where a name differs: for example, the testimonials page says "Jon Frost", and Kain confirmed at S391 he is **Dr Jonathan Frost**.

## What comes back, through TO Chat

One file, per video: the ID, the question, then each speaker in order with start time, end time, the name exactly as the lower third shows it, and that speaker's part of the transcript. Mark anything you could not read as unread, never guessed. Say which transcripts are Vimeo's automatic ones, since those need a read for errors before any page uses them.

Also say, in one line each: the total number of different members across all fourteen, and how many appear who are not among the nine on the page.

## Limits

Read only. Change nothing on Vimeo (no captions added, no settings changed). Build nothing on the site. Transcripts are verbatim speech and are not edited for style.

*No em or en dashes in this file; checked before writing.*
