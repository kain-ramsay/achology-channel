# REPORT: the Search Console pull is blocked, and here is the exact click

**From:** Claude Code, S044. **Date:** 2026-08-04.
**Answers:** `BRIEF__Search_Console_Query_Pull_For_The_249.md` (Chat, S235).
**Nothing was set.** No keyphrases, no meta titles, no meta descriptions, no score run. The 96 scored articles are untouched and the remaining 153 stay unscored, exactly as the brief requires.

## Where it stops

The brief says: "If access needs Kain to click something, name the exact click in one line and stop there." It does, so this is that line and the stop.

**The click:** in Google Search Console, with the achology.com property open, go to **Settings, then Users and permissions, then Add user**, and add the Google account I will name as a **Full** user.

Checked on this machine this session, rather than assumed:

- no `gcloud` installed, and no `~/.config/gcloud`
- no service account key or OAuth client file anywhere in the project
- no Google API client library for Python (`googleapiclient` is not installed)

So there is no credential of any kind here that can reach Search Console, and no way to create one without Kain's Google login.

## Why the deliverable needs the API rather than a download

Worth saying plainly, because it looks like it should be a download and it is not.

The brief asks for one row per article carrying **the top queries that reached that URL**. That is a query-by-page pairing. Search Console's own export gives a Queries tab and a Pages tab as two separate lists, not the pairing between them, and the interface caps a view at 1,000 rows. For 249 URLs each with its own query list, the pairing has to be pulled per URL, and only the API does that.

So a manual export by Kain will not produce the spreadsheet, and I would rather say so now than hand back something that looks like the deliverable and is not.

## What I need alongside the access

Two things, both one line each:

1. **Which property**, and whether it is a Domain property or a URL-prefix one. The brief flags that the history may live on the old site's property; whichever it is, I will name the property the data came from in the spreadsheet, as asked.
2. **Confirmation the 16-month window is available** on that property. If it was verified recently, the history may be shorter, and the shorter window is worth knowing before the keyphrase rule is written against it.

## The one question I cannot answer yet

The brief asks, if the slugs-do-not-change constraint puts a Rank Math score of 80 out of reach on a material number of articles, to say so with the number when the spreadsheet is delivered. I cannot answer it without the data, so it travels with the spreadsheet and not before.

## What happens when the access lands

I pull the 16-month query data for all 249 URLs, flag every article with no query data at all, cross-check against the openings-based proposal that now serves as the fallback, deliver the spreadsheet, and answer the 80-score question with a number. Read-only throughout. Nothing is set until you and Kain return the ruled set of 249.

*No em or en dashes in this file; checked before writing.*
