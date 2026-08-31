# REPORT: SearchWP is installed, licensed, configured and indexed, and search works

**From:** Claude Code, Session 089. **Date:** 31 August 2026.
**Answers:** `RULING__SearchWP_Is_Bought_And_The_Token_Is_On_The_Desktop_Install_It_S321`, all seven steps and its OWED BACK line.
**Ruled by:** Kain, in the sitting: "go ahead and install the search plugin, the token for it is on my desktop."
**Board card:** Plugins and Site Configuration.

---

## 1. The tier, which was the open question, answered from the account

The S321 ruling said to read the tier rather than ask him. Read from SearchWP's own licence server this session:

| | |
|---|---|
| tier | **Standard**, price id 0 |
| sites | **1** |
| expires | 2027-08-26 |
| bought by | Karen Ramsay, manager@achology.com |

**It matches Code's own S087 pricing check exactly**, which named Standard at 99 dollars a year covering one site, and warned in its section on what Kain should see before paying: "it covers one site, and this project has two."

**That single activation is now spent on achologytest.com**, because the vendor refuses the download until the licence is activated for the domain asking for it. It is reversible: the activation is released and re-used on achology.com at cutover. **Named for the cutover list rather than left to be discovered there.**

## 2. The seven steps

1. **Downloaded**, 4.6.1, from the vendor with the licence on the Desktop. No zip was ever on the machine and none was needed.
2. **Installed and activated** on the build install.
3. **Licence stored** in the plugin's own option.
4. **Two engines built.**
5. **ACF fields added as attributes**, on every source.
6. **Index built** across all five sources.
7. **Search results excluded** from SiteGround's dynamic caching.

## 3. The two engines, and why two

| Engine | Sources |
|---|---|
| `default` | article, book_note, quote, workbook |
| `help` | faq_article |

**DSRD 1 section 2.5 excludes the help section from Knowledge Hub search**, and an engine returns results only from the sources added to it. Two engines is the plugin's ordinary shape here rather than a workaround.

**Every source indexes custom fields on the wildcard key.** This is the whole reason the plugin was checked for it at S087: the book note page's writing lives in ACF fields, not in `post_content`, so a source indexed on title and content alone would index all 65 book notes as empty pages and nobody would see it until a search returned nothing.

## 4. Proved by searching, not by reading the config

`/?s=zebras` returns `/learn/mental-wellness/book-notes/why-zebras-dont-get-ulcers/`.

**And `/?s=Sapolsky` returns it too**, which is the test that matters: Robert Sapolsky's name is not in that page's title or slug. It exists only in an ACF field. That one result is the S087 risk closed on the real site.

## 5. Two wrong writes on the way, named rather than buried

**The first attempt wrote nothing.** The PHP payload went as one quoted shell line, every single quote inside it closed the quoting around it, `'article'` arrived as `article`, and the source filter matched nothing. The script's own refusal caught it and wrote no config.

**The second attempt ran, reported success, and was wrong.** It printed "engines written: default 4 sources, help 1 sources" and produced a config with the wildcard attribute silently stripped and the second engine missing altogether. `Utils::normalize_engine_config` keeps only an attribute carrying a `settings` key, and mine carried `name` and `weight`.

**Reported success, wrong result, which is the fault this project keeps meeting in different clothes**, and it is exactly what that file's own header had warned a hand written config would do.

**So the shape is no longer guessed at.** It is read back off the install, where the plugin itself wrote it, extended by one line, and written with a plain option update. The tool now refuses to index at all unless it reads back two engines with a custom field attribute on every source.

## 6. One thing that came back out of the harness

The scripted PHP route needed an H9 exception, and one was added under the register's own discipline: payload read line by line, hash recorded, reason written. **When the rewrite removed the need for it, the entry was taken back out of `h9_reviewed_scripts.json` rather than left standing.** An exception nobody needs is a hole waiting for a future script to be dropped into.

## 7. What is left, and it is Chat's

**The search results page itself.** It is one of the eleven Knowledge Hub templates and sits on Chat's side of the S314 split. **The index is ready before the page is**, which is the order the S311 ruling asked for: a results page built against an empty index tests an empty page.

The cache exclusion is already in place for `/?s=` and `/search/`. If the built page lands on a different address, that exclusion needs its row and Code adds it.

OWED BACK: nothing. All seven steps are done and read back.

*No em or en dashes in this file; checked before writing.*
