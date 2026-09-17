# RULING: web access today, and whether Firecrawl would close the research gaps

**From:** Claude Cowork, the session following S360. Date: Monday 14 September 2026.
**Answering:** ASK__What_Web_Access_Do_You_Have_And_Would_Firecrawl_Close_The_Research_Gaps_S357.md

**Acknowledged first: the paragraph floor ruling.** Read in full. Every body drafted by this session from this point holds the floor: at least three sentences or at least fifty words per paragraph, one short paragraph allowed per section. The quote corpus already drafted this session (CQ001-050-1, CQ001-051-1) is not reopened here; it waits on Code's count and Chat's worst-first brief, as the ruling directs.

## Question 1: what can you read on the web today

Two separate layers, not one. WebSearch and WebFetch read static pages: a plain fetch and convert to text, no script execution, no login, no cookies. They cannot open a page that renders its content with JavaScript after load, cannot get behind any authentication wall, and cannot open Search Console at all, because Search Console is not a page on the open web; it is private dashboard data gated to Kain's own Google login. Separately, when the desktop link is up, this session also has real browser automation, either Claude in Chrome or the built in browser pane, driving an actual Chrome browser that executes JavaScript and can use a signed in session's own cookies. The buying questions gap was a data access limit, not a rendering limit: no fetch tool, Firecrawl included, reads private account data, because it was never published on any page a crawler could reach.

## Question 2: would Firecrawl have closed either gap

No, on the evidence. The Search Console page level data problem is an authentication problem, and Firecrawl fetches and crawls public pages the same way WebFetch does; it does not hold a Google login. The one tool already in this session that could plausibly reach Search Console is the real browser, driven through Kain's own signed in Chrome, not a new crawler. The AnswerSocrates export gap is not a web access problem at all: I checked the Demand Exports folder directly this session and it is still empty. That file is Kain's own export, owed from his side, and no crawling tool retrieves a file that was never generated.

## Question 3: the DSM sourcing register

Read the register in full before answering rather than guessing. Of the three items marked not found, two look like content that does not exist as cited at all: the "157 disorders" statistic and the "Ms T" case report, neither of which any tool found after a real search, because a fabricated or composite detail has no source for any tool to find. The third, the April 2021 DHSC briefing's exact date and phrasing, sits in primary government records, Hansard or a DHSC submission, which is a search depth and indexing question more than a rendering one; Firecrawl's crawl and search combination could plausibly do better here than a single fetch call, but that is not proven, only plausible. One further item, the Haslam paper's pages 11 and 13, reads like the paper was found but not read in full depth; that looks fixable with the tools already available, by fetching the actual PDF, without a new tool. Net: Firecrawl's realistic value is narrow, mainly primary source archive material, not the two gaps named in the ask.

OWED BACK: nothing further. This closes the ask.

*No em or en dashes in this file; checked before writing.*
