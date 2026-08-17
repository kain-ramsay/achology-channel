# REPORT: the 80-point count, and the number is not the finding

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `RULINGS__Previews_Link_Ceiling_Keyphrases_S245.md` §3 and DSRD 2
§2.24: "Before any keyphrase is set, Code reports how many articles would miss
the 80 score on the URL check alone, so the slug question is decided on a real
count."
**Nothing has been set. No slug and no keyphrase has been touched.**

## 1. The count you asked for

The rule applied on paper to all 250 built help articles, with Rank Math's URL
test run the way Rank Math runs it, slugified both sides:

```
articles                                          250
  keyphrase from real query data                  142
  keyphrase derived from the opening line         108

would FAIL the keyphrase-in-URL test              179   (71.6%)
  of those, keyphrase from query data              73
  of those, keyphrase from the opening line       106
```

**That is the answer to the question as asked. It is also the least useful
number in this file**, and I would rather say so than let a slug decision rest
on it.

## 2. Why the count cannot carry the decision: one query is the top query for 64 articles

Testing the data rather than the rule, on the 158 articles the export holds
queries for:

```
distinct top queries                                57
top queries shared by more than one article         10
articles affected                                  111 of 158  (70%)
```

**"achology" is the top query for 64 different articles.** Not similar
articles: `who-is-achology-not-for`, `how-long-achology-operating`,
`achology-courses-cpd-hours`, `who-manages-achology`, `download-achology-community-app`,
and sixty more.

Applied literally, "the top real query's phrasing governs" gives 64 pages the
identical focus keyphrase. That is not a keyphrase, it is one word spread
across a quarter of the section, and Rank Math would mark every one of them as
competing with the others.

The other shared ones are the same shape: "achology meaning" leads 4 articles,
"achology certified" 4, "achology curriculum" 3, "udemy kain ramsay" 3.

**This is the finding.** The rule is sound where an article has its own
distinct query. On 70% of the rows with data, the article does not have one:
it has the brand name, because that is what people typed before they landed
anywhere.

## 3. Two smaller data problems, both real

**Six top queries are not queries at all.** They are strings that reached the
export from somewhere else, and they would become focus keyphrases if the rule
ran unattended:

```
achology-invite-link-not-working      "[client message]: no message provided. [server message]: invalid link ..."
fix-audio-video-achology-live-sessions "please grant camera permission refresh this page to start the liveness ..."
cant-send-receive-messages-achology    "[client message]: timeout of 30000ms exceeded ..."
achology-vs-coursera-psychology        "evaluate the online education company coursera on online masters in pyschology"
```

**Forty of the 158 rest on two impressions or fewer.** A top query with one
impression is one person, once, in sixteen months. §2.24 already says the data
is "good evidence of phrasing and thin evidence for ranking strategy"; this is
what that looks like per row.

## 4. What the 106 opening-line failures actually mean

They are the larger half of the failure count and they are the softest number
in it. My derivation takes the article's first sentence mechanically, so it
produces things like "what will this actually cost you" and "should you wait
for a sale". Those are the reader's question in the reader's words, which is
exactly what §2.24 asks the keyphrase to come from, but turning that sentence
into a keyphrase is a writing act, and Rule 8 puts writing with Chat and Kain.

**So treat 106 as an upper bound, not a count.** A human derivation would put
many of those keyphrases inside the existing slug, because the slugs were
written from the same questions.

The 73 failures on the query-data side are the firm number.

## 5. What I recommend, one decision

**Do not re-slug anything on this evidence.**

The URL test is one Rank Math check among many. Trading 249 stable addresses,
and every redirect that hangs off them, for one check on a section whose whole
16 months of data is 10,666 impressions is a bad trade, and the 64-article
brand-query result says the check would not even be measuring what it looks
like it measures.

**What I would do instead, if you want a proposal rather than just a stop:**
set keyphrases only where an article has a distinct query of its own, which is
47 of 158, leave the rest to the opening-line route, and let the URL check fail
where it fails. That keeps every address stable and every keyphrase honest.

That is a recommendation, not a decision. The slug question is Kain's, and it
now has a real count under it.

## 6. What this does not answer, and cannot yet

The ruling's second half, "what each scores without it", needs Rank Math to
have scored these articles, and it has not: the 249 imported articles never
triggered the scorer, which is its own open item and is older than this one.
Until that runs there is no per-article score to report, with or without the
URL check. Saying so rather than estimating it.

*No em or en dashes in this file; checked before writing.*
