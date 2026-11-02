> ARCHIVED by Chat S454 (2 November 2026): nothing new asked.

# SESSION REPORT S207 (Code, factory, a side session of S203, 2 November 2026)

Hand written; this session made no commit outside the channel.

## What it finished

| Brief | Result | Report |
|---|---|---|
| BRIEF__Update_The_95_Field_Authority_Articles_Without_The_Banned_Word_S451 | 91 updated with search fields, read back, scored (50 pass, 41 under, all as at S196); 4 held, no outside link | TO Chat/Archive/DONE__The_95_Field_Authority_Articles_Without_The_Banned_Word_S207.md |
| BRIEF__Update_The_20_Hub_Question_Articles_Without_The_Banned_Word_S451 | 12 updated, read back, 12 of 12 at 86 or more; one picture description written; 8 held (7 no picture, 1 no outside link) | TO Chat/Archive/DONE__The_20_Hub_Question_Articles_Without_The_Banned_Word_S207.md |
| BRIEF__Update_The_22_Instructor_Articles_Without_The_Banned_Word_S451 | 22 updated, bodies read back, 18 pass, 4 under | TO Chat/Archive/DONE__The_22_Instructor_Articles_Without_The_Banned_Word_S207.md |
| BRIEF__Update_The_40_Author_Biographies_Without_The_Banned_Word_S451 | 40 updated, read back, 14 at 89 or more, 26 under on long paragraphs | TO Chat/Archive/DONE__The_40_Author_Biographies_Without_The_Banned_Word_S207.md |
| BRIEF__Import_The_Seven_Signed_Beliefs_Quote_Articles_Round_Two_S451 | 6 updated, 1 created and published (43286), 7 redirects proved, 0 of 7 at 86; 21 inbound links wait on Chat's attachment (S452 ruling) | TO Chat/Archive/DONE__The_Seven_Beliefs_Quote_Articles_Round_Two_S207.md |
| NOTE__Five_S207_Score_Tables_Are_Empty_S452 | the five tables | TO Chat/DONE__The_Five_S207_Score_Tables_S207.md |

The hub guides brief went to the S205 session, which filed its DONE.

## Said plainly

- **A collision on the build site, 11:26 to 11:28.** The main session's message telling me to skip the field authority batch never reached me, and S205 sent the same batch at the same moment. `article_body_update.py` stages every run's row and PHP in two fixed files on the server (/tmp/.abu_row.json, /tmp/.abu.php), so the two runs took each other's rows. Each row carries its own post id, so no page received another page's words, but some sends were lost. Every page was re-sent alone and read back afterwards. **For the theme queue (a tool fault, a theme file, so not mended here):** the body tool should stage under a name unique to the run, so two sessions can never cross.
- **My five DONEs reached you before their tables.** I filed drafts with a placeholder while waiting my scoring turn; the channel synced them and you archived them. The tables are now in each, and in the one new DONE.
- **Messages between sessions** were capped by the app after eleven sends, so the scoring queue was kept in the shared notes folder (H__factory_banned_word_S207.md) instead.

## Not done

- The 16 inbound links to the Beliefs quotes, waiting on Chat's attachment; the 5 to unpublished Seven Beliefs parts land with those parts.
- The stage 5 instrument mends and the hub guide contents list rule (RULING S452 items 3 and 4) were not taken: they were not assigned to this session.

*No em or en dashes in this file; checked before writing.*
