# BRIEF: adopt Amazon OneLink for international affiliate routing, and retire per-book Genius Links

**From:** Claude Chat, S231. **Date:** 2026-07-29. **Type:** approved brief (Kain approved this session). **Not a question: this is work to do.**

## Context, standalone

Every Book Note on the Knowledge Hub carries a "Get This Book" button pointing to Amazon. The catalogue is 620 books, each with a clean Amazon UK search URL already sitting in the finished master file (`Book_Note_Source_Bank_FINAL.xlsx`, S231). Achology serves a global audience, so a UK link loses commission on every non-UK visitor unless the link is localised to the visitor's own Amazon store with the right country affiliate tag.

Genius Link was the previous plan for this. It has been RETIRED this session: bulk link creation needs their $249/month Business tier, and creating 620 links by hand is not viable. Kain's decision, S231: drop per-book affiliate links entirely and use **Amazon OneLink**, Amazon's own free localisation, which routes any Amazon link on the site to the visitor's local store automatically. This makes the per-book link task disappear rather than moving it to another tool. One Genius Link exists from a test today (Psychology: The Briefer Course); it can be ignored or deleted, it is not part of anything.

## The work

1. **Confirm the Amazon Associates position first, and report it before changing anything.** Which country Associates programs is Achology enrolled in (US, UK, DE, and so on), what is the tag for each, and is OneLink already configured in the Amazon Associates dashboard or not yet. This determines whether step 2 is a fresh setup or a verification.

2. **Install OneLink site-wide** per Amazon's current instructions: the OneLink snippet/tag in the theme so every outbound Amazon link on every page is localised at click time. This is a one-time theme change, not a per-book change. It must cover the Book Note "Get This Book" button and any other Amazon link the site emits.

3. **Confirm the Book Note button uses the plain Amazon URL from the master file.** No geni.us wrapper, no per-book redirect: the plain Amazon URL, localised by OneLink at click time. If the theme currently expects a Genius Link field, report how it is wired so Chat can align the master file's column contract to it (this ties into the open Book Note upload column contract question, `QUESTION__Book_Note_Upload_Column_Contract.md`).

4. **Verify it works** on one rendered Book Note: a non-UK context reaches the correct local store with the correct tag, and report the result through the channel.

## What is NOT wanted

No per-book link creation of any kind. No third-party link tool. No custom domain. The whole point of this decision is that the plain Amazon URLs already in the file are enough once OneLink is on the site.

## What Chat will do with the reply

Align the master file's affiliate column to whatever the theme actually consumes (plain URL, confirmed), and mark the affiliate-link workstream closed. Nothing is blocked meanwhile.

*No em or en dashes in this file; checked before writing.*
