**Needs from Chat:** write this ruling into the owning document (DSRD 8's book note section on the author portrait, or DSRD 9 section 32 if that is where the fallback lives), replacing the illustrated-initials fallback.

# RULING: every book note author illustration becomes a real photograph of the author

**From:** Claude Code, factory session, S133, Thursday 24 September 2026. **To:** Claude Chat.
**Ruled by:** Kain, in this sitting, on the live Further Along the Road Less Travelled book note, where M. Scott Peck is drawn as the lettered panel captioned "Illustration by Achology". His words, verbatim:

> "Every Illustration in the book notes must be replaced with an actual image of the person/author - you must find a way to ensure this happens please."

## What it changes

The lettered-initials panel is no longer an accepted state for a book note's author portrait. Every book note shows a real photograph of its author.

## Where it stands today, read this session

`tools/absent_book_author_portraits.py` against the live site: 150 book notes published, 94 distinct authors with a portrait, **36 without** (so their pages draw the illustration), and one file on disk (`rick-hanson.webp`) not drawing because it has no licence row in `credits.json`. The 36: Judith S. Beck; M. Scott Peck; Susan Forward; Emily Nagoski; William B. Irvine; Mel Robbins; Ethan Kross; Jonice Webb; Susan Jeffers; Anthony de Mello; Douglas Stone and Bruce Patton; Derald Wing Sue and David Sue; Patrick Lencioni; Haim Ginott; Dr Julie Smith; Harville Hendrix; David Richo; Steve Peters; Shelle Rose Charvet; Kerry Patterson, Joseph Grenny and Ron McMillan; Mike Bayer; Kelly McGonigal; Dan Sullivan; Russ Harris; Norman Doidge; Michael Bungay Stanier; Lindsay C. Gibson; Tara Brach; Melody Beattie; Richard C. Schwartz; Edgar H. Schein; Guy Winch; William Ury; Kristin Neff; Chip Heath; Steven C. Hayes.

## How Code carries it out, and makes it hold

1. **Source each photograph** through `tools/author_photo_fetch.py` (Wikimedia Commons, free licence only, refused under 600 by 750, never choosing a face by name match alone), each one checked by eye against the author before it is kept, the licence written into `credits.json`. Downloading waits on Kain's yes in the sitting.
2. **Make it hold:** a book note whose author has no licensed portrait is refused at import and at the page gate, so the illustration cannot reach a page again.
3. **The authors with no free photograph anywhere** (likely for several living authors) are listed back to Kain by name; how each is sourced is his to decide.

## OWED BACK

The ruling written home; nothing else.

*No em or en dashes in this file; checked before writing.*
