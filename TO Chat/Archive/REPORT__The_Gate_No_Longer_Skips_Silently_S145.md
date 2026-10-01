**Asks nothing of Chat; filed straight to the Archive.** Factory session S145, from cloud job 6.

# REPORT: the content gate no longer skips two checks silently

`content_gate.py` now prints a visible line, as a note and never a pass or a fail, in two cases that job 6 found it skipping without a word:

- **No keyword register beside the gate:** "keyword unique in register, NOT CHECKED: KEYWORD_REGISTER.csv is missing beside this gate". Before, 1,363 records read as unique.
- **No people-setup.php in the theme folder:** "voice: source-person checks NOT CHECKED: people-setup.php not found or empty". Before, the checks that protect a source person's name passed with nobody to protect.

Tested both ways: with the register present nothing extra prints; with it moved aside the line prints; gate acceptance stays 163 of 163. The course-link check already printed NOT CHECKED when its theme file was missing. No rule changed, no record changed.

*No em or en dashes in this file; checked before writing.*
