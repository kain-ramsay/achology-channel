> **CHAT DISPOSITION, S336: READ IN FULL AND CLOSED.** Nothing was owed and nothing is open. Written onto the Member Testimonials Page card: step 1 marked done with the folder, the fourteen IDs, the read-back method and the committed tool; the misspelled kaintamsay.com recorded as deliberately left and on the cutover list; and step 5's playback question noted as half answered already, since the build domain is now whitelisted on all fourteen. The next move on that card is Chat's, writing the fourteen-video block into the page's signed spec. Archived.

# REPORT: all fourteen testimonial videos now embed on the build site, read back off the API

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Answers:** `RULING__Add_The_Build_Site_To_The_Fourteen_Video_Whitelist_S311`, its OWED BACK line.
**Board card:** Video Testimonials page.

## The pass

One run, folder `20119371` on user `71102328`, over the Vimeo API. **Fourteen videos found, fourteen written, none refused.** `privacy.embed` was already `whitelist` on all fourteen, so nothing was written to it; only the domain was added.

## The read-back, one row per video, read off the API after the write

Every row below is the API's own answer to a fresh GET after the change, not this run's own counter.

| Video | Question, as titled | embed | Whitelisted domains, after |
|---|---|---|---|
| 889569815 | 1 What are the top personal benefits of regu... | whitelist | achology.circle.so, achology.com, **achologytest.com**, bettermode.io, cdn.iframe.ly, kaintamsay.com |
| 889575310 | 2 What value have you found in regular VALTS... | whitelist | as above |
| 889577533 | 3 What have you learned from regularly engag... | whitelist | as above |
| 889579778 | 4 What are your key lessons that you've lear... | whitelist | as above |
| 889581973 | 5 What role does self-awareness play in pers... | whitelist | as above |
| 889584468 | 6 What impact does self-discipline have on c... | whitelist | as above |
| 889586499 | 7 What is the one lesson that stands out as ... | whitelist | as above |
| 889588879 | 8 What is your favourite Achology course & w... | whitelist | as above |
| 889591164 | 9 What are your top 3 tips for brand new Ach... | whitelist | as above |
| 889594475 | 10 What happens if you disagree with somethi... | whitelist | as above |
| 889617801 | 11 What role does 'getting over yourself' pl... | whitelist | as above |
| 889619981 | 12 What key factors would hinder a persons c... | whitelist | as above |
| 889623105 | 13 What are the main benefits of understandi... | whitelist | as above |
| 889625291 | 14 What decision have you made this year tha... | whitelist | as above |

All fourteen carry the identical six-domain list. Nothing else on the account was touched: no `privacy.view`, no titles, and the two copy faults in the titles are left exactly as they were, as ruled.

**`kaintamsay.com` is still there and was deliberately not removed.** It is the misspelling, it is doing nothing, and it stays on the cutover list.

## The tool, and why it is committed

`tools/vimeo_embed_whitelist.py` in the theme. It runs read-only by default and writes only on `--write`. Three things are built into it rather than remembered:

- **The domain write is additive.** It adds one domain and removes none, so a domain somebody added for a reason survives any future run.
- **`privacy.embed` is written only where it is not already right**, so a needless write is never a needless chance to break something.
- **The verdict on every row is a fresh read off the API**, never this run's own counter.

It is committed rather than left in a scratchpad, which is the S089 lesson: the book cover ladder had to be recovered out of old session transcripts because its script was never committed.

## What this unblocks and what it does not

The block can now be built without showing fourteen dead players. **It is not built**, and correctly so: it waits on the signed spec you are writing, with one question per video and the count at 45 answers from nine members.

OWED BACK: nothing. The printout above is the whole of what was owed.

*No em or en dashes in this file; checked before writing.*
