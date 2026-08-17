# FINDING: two more OG alt texts carry the em dash, outside the eight your brief named

**From:** Claude Code, S047. **Date:** 2026-08-05.
**Relates to:** `ANSWER__S047_Walk_Batch_All_Items_S245.md` item 3, which authorised the sweep across eight named pages. Those eight are done and proved.
**Needs:** one line extending the brief to two more attachments, or a decision to leave them.

## What happened

Your item 3 named eight pages, which was exactly right against the evidence I gave you: I had found the defect by reading the eight live pages that emit an `og:image`. When I went to apply the fix I checked the media library itself rather than the pages, and the same string sits on **ten** attachments, not eight.

The two extra are the artwork for the Manifesto and the Code of Ethics:

| Attachment | Alt text as it stands |
|---|---|
| 911 | The Achology Manifesto [EM DASH] an ancient handwritten scroll lit in amber against a dark background |
| 908 | The Achology Code of Ethics [EM DASH] an ancient handwritten scroll lit in amber against a dark background |

The dash character is written out in words above so this file does not itself breach the ban.

They did not show up in my page-level reading for a simple reason: **/manifesto/ and /code-of-ethics/ emit no `og:image` at all**, which I reported to you as an observation under the site-wide OG imagery item. So the images exist, carry alt text, carry the banned character, and are currently attached to nothing that renders them.

## What I did, and why I stopped there

I applied the fix to exactly the eight your brief names, and no further. Rule 3 is explicit that a sweep runs only over the pages a signed brief names, and "while I am in here anyway" is the failure it exists to stop, even when the extra work is two lines of the same command. So the eight are done and the two are reported.

## What would close it

One line extending the brief to attachments 911 and 908. The transformation is identical: the em dash becomes a colon. It is two more WP-CLI updates, and I will fold them into the Manifesto and Code of Ethics passes, which are pages 8 and 9 of this walk and are coming shortly.

Worth noting for whoever writes the OG imagery item up: fixing these two only matters once those two pages actually emit their image. If the site-wide OG work wires them up later, the alt text will already be clean; if it is done in the other order, the dash ships.

*No em or en dashes in this file; checked before writing.*
