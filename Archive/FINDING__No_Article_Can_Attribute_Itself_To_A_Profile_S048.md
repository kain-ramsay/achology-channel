# FINDING: no article can attribute itself to a profile. The routing key does not exist in the data.

**From:** Claude Code, S048. **Date:** 2026-08-06.
**Found by:** the pen-name slug work, while checking what referenced the old URLs.
**Not fixed.** It is an import and data question, not a slug one, and the fix depends on a decision I do not own.

## The defect

`people-setup.php` builds each profile page's "writing and articles" list with
`achology_person_works()`, which queries posts carrying the person's slug in the
meta key **`achology_author`**. Its own docblock states the assumption:

> "Articles carry the person's slug in the 'achology_author' meta field, the routing hook confirmed against the Knowledge Hub CSV (its pen-name column maps to these slugs at import)."

Queried on the live database this session:

| Meta key | Rows |
|---|---|
| `achology_author` | **0** |
| `author` | 2, both `kain-ramsay` |

There is no `achology_author` anywhere. The key that does exist is `author`, and
it carries two rows.

## What that means on the page

Every one of the ten profile pages renders its empty state. Amelia's reads:

> "Amelia's Writing and Articles. Amelia's writing will appear here as it's published."

That is a correct, graceful empty state, which is why nobody has noticed. The
page looks finished. It will keep looking finished forever, because the query it
runs can never match anything, whatever gets imported later.

**This is the same shape as the stale-audio lesson and the stale-preview one: a
derived thing that silently never updates, wearing the appearance of working.**

## What I have not done, and why

I have not renamed the key in the theme, and I have not written meta onto posts.
Either one is a guess until two things are known, and neither is mine:

1. **Which key is canonical**, `achology_author` as the theme expects or `author`
   as the data has. The Knowledge Hub CSV's import mapping decides that, and the
   docblock's claim about the CSV is now known to be wrong in at least one
   direction.
2. **Why only two rows exist at all.** 249 help articles and the Knowledge Hub
   content are attributed to pen names in the vault voice profiles, so two rows
   of `author` is not a partial import so much as an absent one. Whether
   attribution was ever written at import, or was written and lost, changes the
   fix completely.

## What I would need to close it

The import mapping, or a ruling on which key wins. Once either exists, the work
is small: one key name in one function, or one bulk meta write, and then the
profile pages start listing real work.

**Worth knowing for the walk.** Our People and the ten profiles are the next
pages on the DSRD 6 walk after About. This finding will land in every one of
those eleven records under §5 item 4, internal links, and under §6. Better to
have it ruled before the walk reaches them than to file the same paragraph
eleven times.

*No em or en dashes in this file; checked before writing.*
