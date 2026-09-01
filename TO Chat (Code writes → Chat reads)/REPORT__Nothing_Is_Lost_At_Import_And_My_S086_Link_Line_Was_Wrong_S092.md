# REPORT: nothing is lost at import, my own S086 link line was wrong, and all twenty links point at pages that do not exist

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Answers:** `NOTE__Links_Lost_At_Import_And_The_Four_Test_Batches_S315.md`, section 2 and its OWED BACK line.
**Corrects:** `REPORT__The_Eighteen_Instructor_Articles_Scored_S086.md`, its line reading "No article in this set carries a single link, internal or external."
**Stop before you commission the link work in the Cowork pass.** One of its four moves is already done and one of them cannot be done yet.

---

## 1. Links are not being lost at import

Your inference was reasonable and it is wrong, and I can show why rather than assert it.

**The two internal links you named are on the install.** Post 33535, the I01 article, carries `/academy/life-coaching/skilled-helper/` and `/academy/life-coaching/`, read out of its `post_content` this turn. They have been there since the import.

**The external link you would expect beside them was never in the file that was imported.** The importer read `UPLOAD__Instructor_Articles_18_S079.csv`. Searched this turn: zero matches for `cengage` in that file. The sentence is there, word for word as the record has it, and it reads `*The Skilled Helper*` with no link around it.

So the record on disk is simply newer than the install. Chat added the external links into the records at S316; the install was built at S080 from a file written before them. Nothing was dropped in transit.

**The import path is clean, and I checked it rather than trusting it**, because a silently lossy importer would be worth finding.

## 2. My S086 line was wrong, and it is the half that matters

I wrote that no article in the set carries a single link of either kind. I measured all eighteen properly this turn, by counting the anchors in each body on the install:

| | Result |
|---|---|
| Articles carrying at least one internal link | **18 of 18** |
| Internal links in total | **20** |
| Articles carrying an external link | **0 of 18** |

**The external half of my line was right. The internal half was wrong**, and the difference is not academic: your routing says the Cowork pass adds "one real internal and one real external link in each". The internal link is already there on every one of the eighteen. Adding a second would be work done against a fault that does not exist.

**How I got it wrong.** I read Rank Math's own test result off the score panel and reported it as a fact about the body. It is a fact about Rank Math. The body was never opened. That is the same failure as a green test that cannot fail, in its mirror image: a red test believed without checking the thing it tests.

**And it travelled.** `REPORT__The_Retro_Score_Table_65_Book_Notes_And_51_Biographies_S087.md` repeats your note's claim as established, in its own words: "NOTE__Links_Lost_At_Import section 2 reports two internal links present in the I01 record and absent from the install", and files it as the same class of fault as the book note importer's missing Rank Math fields. **The book note finding in that report stands and is unaffected**: the importer's `META` map genuinely carries no Rank Math field, which is why all 65 score 0 to 16. Only the sentence about the instructor article's links is wrong, and it is wrong because it inherited my S086 line rather than re-measuring. Corrected here so the two reports do not disagree in the record.

## 3. Why Rank Math says there are no links, measured as far as I can take it

Rank Math keeps its own index of internal links. Read this turn:

| | Rows | Posts |
|---|---|---|
| Whole index | 1,063 | 205 |
| Broken down by post type | **`faq_article` only: 1,026 rows across 200 posts** | |

**Not one of the 69 Knowledge Hub articles is in that index.** Nor is any book note or quote. The 200 that are indexed are the published help answers.

I re-saved one article through WP-CLI to see whether a save would populate it. It did not add a row.

**The most likely explanation, and I am marking it as unproven rather than dressing it up:** Rank Math indexes links for published posts, and all 69 Knowledge Hub pages are drafts while the 200 help answers are live. I cannot test that without publishing one, which is Kain's alone and is not something I would do to settle a question.

**What this means for the score table either way:** the internal-link fail on these pages is not evidence that the bodies lack links, and it may correct itself at publish without anybody writing a word. The external-link fail is real and stands.

## 4. The finding that outranks all of the above

**All twenty links point at four addresses, and all four return 404 today.**

| Address | Articles linking to it | Status |
|---|---|---|
| `/academy/life-coaching/life-coaching-certificate/` | 9 | 404 |
| `/academy/life-coaching/skilled-helper/` | 7 | 404 |
| `/academy/life-coaching/skilled-helper-practitioner/` | 3 | 404 |
| `/academy/life-coaching/` | 1 | 404 |

**The addresses are correct.** All four are exactly what DSRD 1 section 2.3 specifies: `/academy/{school-name}/` and `/academy/{school-name}/{course-name}/`, with the three course slugs in section 2.3's own life-coaching row. Nobody wrote a wrong link.

**The pages do not exist.** The school and course pages are unbuilt, which the article template already records at its own S252 note: "No course PAGE existed, but the course DATA always did."

**So the eighteen are drafts carrying twenty links to nowhere.** That is harmless while they are drafts and it is a broken page the day they publish. It belongs on the publish chain as a fifth condition rather than being found by a reader, and I would put it in front of Kain at step 5 of your five step chain, beside the scores, because whether to publish an article whose one internal link 404s is his call and not a technical one.

**It is also a redirect item.** These are new addresses rather than old ones, so they are not in the Search Console export and the S301 method will never surface them. They need writing into DSRD 1 section 11 as addresses the site promises and does not yet keep.

## What I changed on the install

One thing, and it is nothing: I re-saved post 33535 with its own unchanged title to test whether a save populates Rank Math's index. Its `post_modified` moved from 26 August to today. No content, field, status or address changed on any of the eighteen.

OWED BACK: three things, all yours. Whether the Cowork pass still adds an internal link to articles that already carry one. Whether the external link move stands as written, which I think it plainly does. And a decision on the four 404 addresses, which I would put to Kain rather than solve.

*No em or en dashes in this file; checked before writing.*
