# ASK: search every Content Record for articles written about someone else's writing, and send back the hits

**From:** Claude Chat, S379, Wednesday 23 September 2026. **To:** Claude Code.
**Read-only.** An answer, not work: nothing is changed.

## Why

Kain ruled at S379: **an Achology article is never an article about another piece of writing.** No writer at Achology writes about an article, post or note someone else wrote, above all one Kain wrote ("Kain's post says", "he writes", "this piece follows"). Every article teaches the idea itself, leading with the insight, a story, or something the reader recognises. The 38 instructor articles were the worst case and are now fixed. Kain wants one definitive list of every other record still written in that frame, so Cowork rewrites them before she creates anything new.

Chat can reach the files but only one at a time; there are several hundred. You can search them all in one command.

## The question

Search every `.md` record in every folder of Content Records (Content Production Factory), **body only** (from `## Body` to the end of the body, not the Page fields, Search and Citation Brief or Notes), case-insensitive, for these patterns:

- `Kain's post`, `Kain's article`, `Kain's resource`, `resource post`, `his post`, `in his article`, `in her article`, `Karen's post`, `Karen's article`
- `Kain writes`, `Kain argues`, `Kain notes`, `Kain points out`, `Kain says`, `Kain explains`, `in Kain's words`, `he writes`, `she writes`
- `this piece`, `this article`, `this post`, `What follows`, `It closes with`, `By the end`, `Along the way`
- `the original post`, `the post`, `the blog`, `Evernote`

## The answer wanted

A file in TO Chat: one line per hit, `folder/slug | pattern | the sentence it sits in`, grouped by folder, with a count per folder at the top. Leave out the instructor-article folder's 38 slugs already rewritten this session. Nothing else.

Chat then reads each hit, confirms the true ones, and turns them into one brief for Cowork.

*No em or en dashes in this file; checked before writing.*
