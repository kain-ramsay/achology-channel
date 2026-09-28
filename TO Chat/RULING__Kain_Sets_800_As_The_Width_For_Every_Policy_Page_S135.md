**Needs from Chat:** write this into DSRD 9 section 27, where the table still names 880 as the reading column. Nothing to decide.

# RULING: every policy page reads at 800, settled for good

**From:** Claude Code, S135 (theme), Monday 28 September 2026.

Kain, in the sitting, after asking for one standard for all policy pages decided by eye and not revisited: "Yes, 800 for all policy pages is settled for good."

## What this settles

- DSRD 9 section 27 says reading pages, including "the seven legal policies, the policies index", sit in an 880 column. The site's token `--container-article` has been 800 since the S112 article sitting (DSRD 9 records "an 800 reading column" for the article page), and every policy page renders at 800. The document and the build disagreed; Kain ruled for the build.
- The page gate's width check (`page_gate.py`, `CONTENT_WIDTHS`) now accepts 800, so policy pages stop failing it. It still accepts 1200 and 880 for any page that uses them.

## OWED BACK

DSRD 9 section 27 amended to 800 for policy pages (and articles, per S112).

*No em or en dashes in this file; checked before writing.*
