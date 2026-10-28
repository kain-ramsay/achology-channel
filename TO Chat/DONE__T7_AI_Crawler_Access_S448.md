**For Chat. What this needs from you:** nothing to decide. Mark T7 of BRIEF__Operation_Cleanup_Finish_The_Small_Jobs_On_The_Board_S448 as built, waiting on the main theme session to review, commit and deploy, and add the cutover checks in section 3 to the cutover list.

# DONE: T7, the site opened to AI crawlers, switching on only at cutover (Code side session, 28 October 2026)

Built to DSRD 3 section 6.6. All three pieces are in one new theme file. Nothing is committed or deployed: the main theme session reviews, commits and deploys it.

## 1. Files touched

- `ai-crawler-access.php`, new, in the theme folder. Holds all three pieces and the one switch.
- `functions.php`, one require line for the new file, with a four-line comment, placed after the Media Library require. Nothing else in the file is changed.
- `ai_crawler_access_acceptance.py`, new, in the theme folder. The test.
- This note.

None of the files the main theme session is editing were touched (`knowledge-hub.css`, `header.css`, `components.css`, `template-policy.php`, `policies-content/`).

## 2. How each piece switches on at cutover

There is one switch for all three pieces, `achology_ai_access_on()`. It is on only when both of these are true:
- the site's own address is not the build site. It uses the theme's existing `achology_is_build_ground()`, which reads the address from the database, so the cutover clone onto achology.com turns it on with nobody having to remember anything;
- WordPress's "Discourage search engines" box is unticked (blog_public 1). Cutover already has to untick it.

If either one is false, all three pieces stay off. On achologytest.com today both are false.

1. **Allow rules for each AI crawler.** robots.txt gets its own `Allow: /` group for each of the eleven crawlers DSRD 3 names: OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, GPTBot, ClaudeBot, Google-Extended, Applebot-Extended and CCBot. Each group also repeats WordPress's own two admin lines, so naming a crawler never opens /wp-admin/ to it. A crawler that already has its own group, for example one added by hand in Rank Math's robots editor, does not get a second one. While the switch is off, robots.txt stays exactly as WordPress writes it today ("Disallow: /").
2. **/llms.txt.** When the switch is on, /llms.txt answers in plain text in the llmstxt.org shape: the site name, the site tagline (Settings, General), then four sections. Knowledge Hub: /learn/, articles, workbooks, topics and every Hub category. Help: /help/ and every Help category. Courses: /courses/ and all 28 courses by their full DSRD 5 names. About: the reviews page. Every entry is built from data the site already holds, so the list cannot drift. While the switch is off, the address falls through to WordPress's own 404, as it does today.
3. **No snippet limits on Knowledge Hub and Help pages.** When the switch is on, every Hub and Help page loses `nosnippet`, and any max-snippet, max-image-preview or max-video-preview is opened to its widest value. That covers single pages, categories, tags, listings and anything under /learn/ or /help/. Both writers of the robots tag are handled: WordPress core and Rank Math. noindex and index are never touched, so this cannot reveal the build site. No other page is changed.

## 3. Three checks for the cutover list

- **No physical robots.txt or llms.txt in achology.com's web root after the clone.** A real file on disk is served before WordPress runs, so it would hide pieces 1 and 2. The build site has neither (checked on the server today). The old achology.com may have a robots.txt of its own, and that one must go.
- **The CDN must let them in (DSRD 3 section 6.6, "The CDN must agree").** After cutover, check in the server logs, or with a crawl test, that the named crawlers actually get 200 responses. SiteGround's security plugin could block them even though robots.txt allows them.
- **cutover_gate.py could carry three more facts**, for the main theme session to add if it wants them: robots.txt names GPTBot, /llms.txt answers 200, and one Hub page's robots tag has no nosnippet. I left that gate alone because it is the main session's file.

## 4. Proof

`python3 ai_crawler_access_acceptance.py`: **71 of 71 passed.** This Mac has no PHP, so the test sends the real include, wrapped in stand-ins for WordPress, to the build server's own PHP through standard input. Nothing is written on the server.

What the test covers:
- the switch stays off on the build site even with blog_public 1;
- the switch stays off on achology.com with blog_public 0;
- with the switch on, each of the eleven crawlers is named once with Allow: /;
- a crawler group already in the file is not repeated;
- the robots tags of Hub, Help and single pages are opened in both the WordPress core and Rank Math shapes, with noindex left exactly as it was;
- every other page is left untouched;
- /llms.txt is matched only at the site root, and its body has the right headings, links and full course names.

The cases with the switch off are the red half: they run the same functions on the same input and require no change at all.

Not yet checked in a browser, because nothing is deployed and the switch is off on the build site by design. The real check comes at cutover, using the three checks in section 3.

*No em or en dashes in this file; checked before writing.*
