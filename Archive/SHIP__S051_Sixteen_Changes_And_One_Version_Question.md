# SHIP: everything that went to the build ground at S051

**From:** Claude Code, S051. **Date:** 2026-08-10.
**One brief for the session, since the changes are one body of work.**

## What shipped, in order

| Commit | What |
|---|---|
| `ebef9a0` | Policy template's routes rows collapsed |
| `fbda1cf` | Harness and gate find folders by marker, not by number |
| `865e1f1` | Harness README names the channel instead of numbering it |
| `d7e2210` | The 404's six doors collapsed |
| `27faf35` | The /help/ close panel collapsed, 249 articles and 14 category pages |
| `2feb30c` | The course block reads DSRD 1 §5.7's lead tag rule |
| `84c36a8` | `primary_recommended_course` retired |
| `e3d7ccc` | The card sheet template |
| `40d9840` | Six glyphs registered, three library keys renamed |
| `8a42816` | About's routes rows collapsed |
| `b0c3305` | The Manifesto's two blocks collapsed |
| `0241236` | The Code of Ethics closing pair collapsed |
| `8f15cb3` | The hero course reads the tags, `recommended_course` retired |
| `f854e20` | `amazon_genius_link_url` removed |
| `8b4ea0d` | The card sheet's member cards render |
| `747f924` | The card sheet loads `knowledge-hub.css` |

All deployed and cache purged as they went, per Rule 12. Nothing waits on Kain
uploading anything.

## What I need from you

**A version number, or a ruling that we have stopped using them.**

The theme has said `0.41.0` in `style.css` all session, through sixteen
commits. I did not bump it, and I flagged why at the first collapse: the
version is stamped onto every asset url by `achology_asset()`, so bumping it
changes every page's html and would have swamped the before-and-after diffs
that every one of today's changes was proved by.

That reasoning held for one change set. It does not hold for sixteen. The
number now says something untrue: the deployed theme is not `0.41.0`.

**My recommendation: `v0.42.0`, set as the first act of the next session**, so
it is a change of its own with nothing riding on it, and so the diffs it
disturbs are nobody's evidence. A minor rather than a patch, because the course
selection mechanism changed and two data fields were retired.

Say the word and I will set it. If versions have quietly stopped mattering now
that Code deploys rather than Kain uploading zips, say that instead and I will
stop raising it.

## One thing not done, and it is not mine

**27 commits are unpushed to origin.** The repo was already 11 behind when this
session opened, so this is not new, but it is now 27. Pushing is outward
facing, and I have not done it without being asked. Worth a ruling on whether
Code pushes as part of a change set, the way Rule 12 made deployment part of
one.

*No em or en dashes in this file; checked before writing.*
