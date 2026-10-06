> CODE DISPOSITION, S151: WAITS ON a factory session opening: it names no page or component, so it is factory work, and the theme session S151 leaves it untouched (Harness Rule 1, two sessions).

> **CHAT, S409: this brief is brought to the signed plan. The plan is now `PLAN__The_YouTube_Channel_Programme_S409.md` in the same folder (the S408 draft is archived beside it). Three changes below, each marked S409: step 3 also reads the channel's status; a new step 6 sends Google the two applications; step 5's limits are already verified by Chat and only need Code's check of (f). Everything else stands.**

**For Code: connect Claude to the Achology YouTube channel and read every video, writing nothing to the channel. Chat's commission, signed by Kain's word in Chat at S408 and re-signed on the S409 plan. This is Product 1 (P1) and the start of P2 of PLAN__The_YouTube_Channel_Programme_S409.**

# BRIEF: Connect Claude to YouTube and read every video

Written by Chat, S408. Read the plan first; it lives in the project folder "All Achology Videos | Vimeo Exports", inside the folder "YouTube Channel Programme". The plan holds the whole programme. This brief is its first job only.

## Why

Kain wants the same control over the Achology YouTube channel (@AchologyAcademy, channel ID UCfu-Mf885W4SVN05RLJxIzg) that he had over Vimeo, where Code updated and upgraded 2,146 videos in four days. The channel holds about 150 videos by his count, and could hold over 1,000 in twelve months. Before any change is made, Claude has to be able to read the channel, from a chat and from a script.

## What to do, in this order

1. **Set up the access.** A Google Cloud project with the YouTube Data API v3 and the YouTube Analytics API enabled, and an OAuth sign-in as the channel owner. The sign-in is Kain's act: walk him through it step by step in plain words, one thing at a time, and do nothing that needs his password yourself. Store the credentials the way the Vimeo credentials are stored, never in the channel, never in git.
2. **Build the bulk script**, in Python on Google's official client library (`github.com/googleapis/google-api-python-client`), in the Vimeo run's own pattern: target every video by ID, a ledger of old and new values so every change can be reversed, one pilot before any batch, each batch committed as it completes. **Writing to the channel is switched off in this brief.** The script reads only.
3. **Read the channel into one ledger**, as a CSV in the YouTube Channel Programme folder: for every video, its ID, title, description, tags, category, language, publish date, length, privacy status, views, impressions, click rate, average view duration, traffic sources, top search terms, playlists, thumbnail address, caption status. Add a column for the course or lesson it belongs to where the title or description makes that clear, and leave it blank where it does not. Count the videos and report the real number. **Added S409: also read and report the channel's status: subscriber count; whether it is in the YouTube Partner Program (monetised); whether Advanced Features is on; the channel keywords and the About text as they stand; and the daily upload limit the channel shows in Studio's Feature eligibility, if it shows one.** Pull one clean still frame of Kain from each of the ten most-viewed videos into the folder, for Chat's thumbnail renders (P3).
4. **Evaluate and install one in-chat server**, so Chat can read and later edit single videos from a conversation. Candidates: `github.com/mrchevyceleb/youtube-mcp` (22 tools, runs locally for Claude Code and Desktop) and `github.com/sankalpaacharya/youtube-mcp` (20 tools, can be deployed to Cloudflare Workers so claude.ai chat can use it). **Read each one's code before running it** and report what you found, including anything that sends data anywhere. Install the one you judge sound, with its write tools disabled until Kain's go. If neither is sound, say so and stop; the bulk script alone still carries the programme.
5. **Verify these limits against Google's own documentation**, and report each as confirmed, wrong, or not found. **S409: Chat has since read Google's quota page itself (`RESEARCH__How_A_Channel_Like_Ours_Is_Grown_Live_Checked_S409.md` in the plan folder, section 1): (a) confirmed, 10,000 units; (b) confirmed, 50; (c) wrong, uploads now sit in their own bucket of 100 a day at 1 each; (d) confirmed from the videos.insert reference; (e) confirmed by three developer sources. Only (f) is still owed: the Audit and Quota Extension form's address, what it asks for, and how long Google says it takes.**
6. **Send Google the two applications (added S409, Kain's yes).** On the same day the access is set up, submit the YouTube API Services compliance audit for the project and the quota extension request, describing the use honestly: a channel owner's own tooling to read, package and publish the owner's own videos, in the Vimeo run's pattern. Record the submission dates and any reference numbers in the report. Both gate the plan's P6 and both take weeks, which is why they go in first.

## What not to do

No title, description, tag, thumbnail, playlist, caption or privacy setting on the channel is changed by this brief. No video is uploaded. No comment is posted. If a step seems to need a write, stop and ask through the channel.

## Done when

The ledger exists with the real video count and every column filled where YouTube holds the data; the channel's status is reported (S409); the ten still frames are in the folder (S409); the two applications are sent and their dates recorded (S409); Chat can read the channel from a chat (shown by Chat listing five video titles back); the in-chat server decision is reported with what the code review found; limit (f) is reported; and the whole report is filed to TO Chat. The report names the one thing that stopped any step, if anything did.

## Standing

Under The Harness, with its status line. Nothing here is a design decision, so Kain's eye is not needed for the code; his sign-in in step 1 is the only point where he is needed.

OWED BACK: the report in TO Chat, the ledger in the YouTube Channel Programme folder.

*No em or en dashes in this file; checked before writing.*
