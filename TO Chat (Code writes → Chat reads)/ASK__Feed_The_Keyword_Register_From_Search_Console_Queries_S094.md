# ASK: feed the keyword register from Search Console's real queries, and take questions from AnswerSocrates exports

**From:** Claude Code, Session 094. **Date:** 2 September 2026.
**Why it travels:** Kain asked in the sitting whether four tools could help the SEO keyword and question sourcing work: the Detailed SEO browser extension, Screaming Frog, Google Analytics and AnswerSocrates. What feeds the keyword register is a content decision, so this is a proposal for Kain to rule on through Chat, not a change Code has made. Kain's words on being told it would travel as a proposal: "yes, file it please."

---

## What was checked before this was written

- The content factory already holds `build_keyword_register.py` and `KEYWORD_REGISTER.csv`, found by name in the Content Production Factory folder this session. What the register is currently built from was not read this session, and this file does not claim to know it.
- The Google Search Console service key came across in the machine move and is in place; it is the key the S093 URL inspection run used. Search Console's query report has not yet been read by any tool in the factory, as far as a name search of that folder shows.
- Screaming Frog is not installed on this machine. Neither browser extension can be driven by Code.
- The S329 brief on the pre-draft gate's search and citation check is unopened, on the move brief's order. If it already governs this ground, it wins and this ask folds into it.

## The assessment, one tool at a time

**Google Search Console: use it, first.** It reports the exact queries people typed before reaching each page, with impressions and clicks. That is the one source in this list that is real demand on this site rather than a guess or a third party's estimate. The key is already in hand, so the cost is one script that reads the Search Analytics report and writes the queries, per page, into the register alongside whatever it holds now.

**AnswerSocrates: use it, by hand.** It lists the questions people ask Google around a seed word, which is the question half of the sourcing job. It has no interface Code can pull from, so it works as an export Kain or Karen runs per topic, dropped into the factory folder, which the register builder then reads.

**Google Analytics: not for sourcing.** It shows what visitors do after they arrive and hides the search words. Useful later for choosing which pages to work on next; it would need a read-only key of the same kind as the Search Console one. Not proposed here.

**Screaming Frog and the Detailed SEO extension: leave both.** They audit a page's titles, headings and links, ours or a rival's. The factory's own gates already measure our pages over the server road, and reading a rival page is something Code can do directly. Neither sources keywords or questions.

## The proposal, as one decision

Add two inputs to the keyword register: Search Console's query report, read by machine, and AnswerSocrates exports, dropped in by hand. Nothing else in the list joins.

Under Harness Rule 11, reading Search Console is done through Google's own published interface with the key already in use, and no outside code enters the theme. The script lives in the factory folder beside the register builder.

## What is asked

A ruling, yes or no, on adding those two inputs. If yes, a BRIEF naming what the register's new columns are called and how a Search Console query is weighed against what the register already holds, since that is a content standard and not Code's to invent.

OWED BACK: a RULING, to FROM Chat.

*No em or en dashes in this file; checked before writing.*
