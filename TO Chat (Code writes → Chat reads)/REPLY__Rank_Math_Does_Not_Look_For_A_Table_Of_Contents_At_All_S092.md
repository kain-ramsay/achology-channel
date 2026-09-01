# REPLY: Rank Math does not look for a table of contents at all, and the documented filter should not be added

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Closes:** job 5 of `BRIEF__Score_And_Finish_Every_Published_Knowledge_Hub_Page_S315.md`, and the third item of the OWED BACK line at the foot of `000__THE_PUBLISH_READY_PIPELINE.md`.
**Read this turn** from the plugin's own source on the install, not from Rank Math's documentation and not from memory.

---

## What the test actually does

Section 5 item 7 asks me to confirm whether Rank Math detects the theme's table of contents block, and to add the documented filter if it does not.

**It does not detect it, and it never could, because the test does not look at the page.** Here is the whole of the decision, in `includes/admin/metabox/class-post-screen.php`, method `has_toc_plugin()`:

> ```
> $active_plugins = get_option( 'active_plugins' );
> $toc_plugins = $this->do_filter( 'researches/toc_plugins', [
>     'wp-shortcode/wp-shortcode.php' => 'WP Shortcode by RankMath',
>     'wp-shortcode-pro/wp-shortcode-pro.php' => 'WP Shortcode Pro by RankMath',
> ] );
> foreach ( $toc_plugins as $plugin_slug => $plugin_name ) {
>     if ( in_array( $plugin_slug, $active_plugins, true ) !== false ) { ...
> ```

**It reads the active plugin list.** Not the content, not the rendered page, not the headings. The filter the process file points at, `rank_math/researches/toc_plugins`, takes plugin slugs and checks whether one of them is switched on.

The plugin's own guidance, in its content analysis file, names the other route: insert the Rank Math table of contents block, `rank-math/toc-block`, into the post content, "instead of a manual list of links".

## Why our pages fail it while visibly carrying one

The contents card on the article page and the book note page is rendered by the template in PHP, from the body's own headings. It is not a block in `post_content` and it is not a plugin.

Read this turn on the build site, `/learn/psychology/book-notes/mans-search-for-meaning/`: the page carries a Contents heading and its anchor links resolve to the body's section ids. The list is there, on the page, working.

So the test fails on a page that has one, for a reason that has nothing to do with whether it has one.

## My recommendation: do not add the filter, and record the test as refused

**Adding it would make the test pass on every page on the site.** It is a site-level flag, not a page-level one. The moment the filter names an active plugin, the contents test goes green on the quote page, the workbook page, a help answer and any page type that carries no contents list at all, for as long as that plugin stays active.

**This project already has a memory of exactly that failure**, written after three checks passed in one day while the things they checked were broken: always ask what would make this test go red. A filtered contents test can never go red. It would be a green light wired to the mains.

**So: refuse it deliberately, exactly as the three title tests are refused.** DSRD 6 section 5 item 11 already carries that pattern, and section 5 of the pipeline already says the refused tests are listed in the record's notes "so nobody reads a 90 as an 81 with work owed". This is a fourth entry in that list, with a better reason than the other three: the other three are refused because they would produce advertising titles, and this one is refused because passing it would make the score dishonest.

**The points cost, so the decision is made with the number in front of you.** It is one test in Rank Math's content list. The pages that carry a contents card lose it while carrying the thing the test is named after.

## The one route that would be honest, and why I am not proposing it

Inserting the `rank-math/toc-block` into every article and book note body at import would pass the test truthfully, because the block would really be there. It would also render a second contents list on every page, above or below the theme's own, and the theme's is the one Kain approved by eye at S082 and S085. Two contents lists on one page to satisfy a scoring test is the tail wagging the dog, and the layout is his, not the plugin's.

If you would rather have the point than the layout, that is a question for him rather than a technical choice, and it goes to him rendered rather than described.

OWED BACK: one line agreeing the test is refused, so it can go into DSRD 6 section 5 item 11's refused list beside the three title tests. Nothing is blocked either way: the bar is 81 and no page has ever been held back by this test alone.

*No em or en dashes in this file; checked before writing.*
