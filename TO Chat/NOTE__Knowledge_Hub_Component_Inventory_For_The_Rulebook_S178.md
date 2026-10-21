For Chat: this is the inventory Kain asked Code to write for the Knowledge Hub rulebook (RULING__A_Knowledge_Hub_Rulebook_And_Shared_Components_S178); please use it to place the rulebook and its first shared components, and rule the conflicts in section C.

# NOTE: every repeated Knowledge Hub part, where its rules live, and where the copies differ (Code, S178, theme)

Read only; nothing was changed. Line numbers are in the theme folder's files at 0.707.415. DSRD numbers are DSRD 7, 8 and 9.

## A. The parts (each: pages, where built, where ruled, shared or copied, rules found only in code)

1. **Breadcrumb trail.** Every Knowledge Hub page. Hand-written in learn-home.php 55-65, taxonomy-kh_category.php 81-95, learn-listing.php 253-273 and 479-514, learn-tags.php 83-97, taxonomy-kh_tag.php 232-260; shared only on the four single pages (achology_kh_hero, knowledge-hub-parts.php 923-939). The chevron is pasted inline six times and never comes from the icon registry; the BreadcrumbList data is copied in each template. Ruled: DSRD 9 20.3, 21.3, 34.3, 35.2, 39.4 item 2; DSRD 8 25. Drift: class names; rungs; the quote page's crumb says "Quotes" where its list says "Quote Articles". Code only: the per-book trail (learn-listing.php 496).
2. **Hero band.** Subject pages, 32 lists, All Tags, tag pages; the front page still has its older hero; single pages the Soft Light hero. rx-band copied in taxonomy-kh_category.php 79-132, learn-listing.php 251-329, learn-tags.php 81-132; the tag page forks it (tgp-ban, 222-276). Ruled: DSRD 9 20.0, 20.0d to 20.0f, 21.0, 34.11, 34.13, 35.0a, 39.9; DSRD 8 28, 12.7. Drift: the label above the title; the right-hand panel. The html element's class list is set twice (knowledge-hub-parts.php 4091-4097, kh-tag-setup.php 326-332). Code only: Book Notes lists show the subject name alone in the title (S174).
3. **Faces panels.** Subject pages, Book Notes and Quotes lists, All Tags (Faces Veil), the front banner. Copied in taxonomy-kh_category.php 108-131 and learn-listing.php 297-306; hard-coded name lists at learn-listing.php 205-237 and learn-tags.php 158. Ruled: DSRD 9 20.0, 20.0f, 21.0, 35.6. Drift: only the lists ask for the colour photo, so subject pages warm into nothing. Code only: the Quotes faces rotate one place per list (S176).
4. **Categories bar.** Subject pages, lists, All Tags, tag pages. Copied four times (taxonomy-kh_category.php 136-146, learn-listing.php 332-342, learn-tags.php 135-144, taxonomy-kh_tag.php 279-298); the subject order written twice. JS kh-subject.js 20-36 and 498-506; kh-tag.js 118-128. Ruled: DSRD 9 20.0, 20.0c, 20.0e, 34.11; DSRD 8 12.7 calls it a reuse candidate. Drift: where "All Categories" and the subject links go; aria-current. Code only: on All Tags and tag pages the label goes to /learn/.
5. **Kind buttons, filters and pills.** Every band, the subject page's grey plate, tag pages, per-book lists. Written about five ways; the kind-to-icon list four times. Ruled: DSRD 9 20.0, 20.0e, 21.4, 34.11; DSRD 8 6.10 rule 4. Drift: "Quotes" against "Quote Articles", "Book Notes" against "Book Note Articles"; only All Tags has the arrow; the book note's Explore More uses book-open, not notebook-pen.
6. **Editor's Picks and the lead row.** Subject pages and lists. Copied in taxonomy-kh_category.php 154-179 and learn-listing.php 350-431 in three versions; quill pasted twice. Ruled: DSRD 9 20.0b, 20.0c, 20.0e, 21.0; DSRD 8 12.7 says shared, the code is copied. Code only: no reading time (S174); the Quotes lead excerpt rewrite (S176); Book Notes picks show the name before the colon (S178).
7. **Mixed masonry wall and the Know Your Psychology logo card.** Subject pages and lists (wall), All Tags (logo card in its grid). Data achology_kh_subject_mixed_grid (knowledge-hub-parts.php 4151-4221), quote pool (4232-4274), grid HTML (4494-4551), cache (4619-4667); logo template copied word for word (category 201, listing 459) plus All Tags' own (learn-tags.php 170-189); two placement routines in kh-subject.js (56-247 and 406-490). CSS in three homes (.bx-brand, .qc--logo, .tt__logo) with different padding, border and shadow. Ruled: DSRD 9 20.0c items 1 to 7, 34.11, 35.6, 39.9; DSRD 8 12.7. Code only: SWAP 7, MAX_DROP 3, DROP_GAIN 24. The front page wall now reproduces it in preview (kh-front-research-s178/front.html).
8. **Quote wall (wide dark cards, papers).** Quotes lists, tag pages' Quote group and view-all. PHP shared (achology_kh_quote_wall_html, 4565-4595); JS copied (kh-subject.js 249-496, kh-tag.js 9-53) and the paint routine differs. Ruled: DSRD 9 21.0, 34.12; RULING__Quotes_List_Wall_Is_Spotlight_S176; BUILD_SHEET__Articles_Listing_S174. Code only: wide card 80 to 160 characters, four small cards between wide ones, none in the last six, never stacked within 300, grows 64 at most, four papers never touch.
9. **Card types.** Standard cards (achology_kh_card 405-502), featured cards (509-620), wall tiles (4494-4551). Ruled: DSRD 8 6.0 to 6.10; DSRD 9 20.0. Drift: three reading-time formulas and labels; standard cards still print "by {author}"; hover lift 3 against 2. Fault: the grid HTML has no workbook branch, so workbooks are labelled "Article" with the newspaper icon.
10. **Search field.** Front page (a working form), subject pages and lists (drawn only, copied). Ruled: DSRD 9 20.0c item 8, 38, 39.4 item 3, 39.9; DSRD 7 5.5.
11. **Topics band ("Explore the Achology Knowledge Hub by Topic").** Subject pages and lists; one shared function (achology_kh_hub_topics_html 4727-4756). Ruled: DSRD 9 20.0c, 20.0e; DSRD 8 12.7. Drift: its header lacks the supporting line DSRD 8 23.4 requires; names come through a display-name map, not Kain's S177 titles; the four families are cut in three places; old 31-topic CSS still present.
12. **All Tags quilt and topic tiles.** Tile is one function (achology_kh_topic_tile_html, kh-tag-setup.php 173-181); the quilt's scripts are inline in learn-tags.php 196-300; family colours held in three places. Ruled: DSRD 9 35.0a, 35.3 (numbered twice), 35.6; DSRD 8 6.10; BUILD_SHEET__All_Tags_Index_Page_S390; RULING__All_Tags_Tile_Lines_Are_Kains_Own_Words_S177. Probable fault: the tile's pattern and lift values are set only on main.kh-tags, so tag pages' Related Topics tiles may lack them (to check on the page).
13. **Learning path and course callouts.** Subject pages and lists (shared achology_kh_hub_path_html 4762-4828), tag pages (their own copy), single pages (achology_close_conversation). The course is chosen three ways. Ruled: DSRD 9 20.0c, 20.0e, 34.11, 22.15b, 40 item 6; DSRD 8 12.7 still says page-local.
14. **Section headers.** Everywhere; achology_kh_section_header exists (707-722) but only learn-home uses it, about ten places hand-write it. Ruled: DSRD 8 23, 23.3, 23.4; DSRD 7 3.3.
15. **Explore More on the single pages.** Copied four times with four headings and different thresholds. Ruled: DSRD 9 22.14, 32, 40 item 3, 37.7.
16. **Related Topics.** Tag pages (taxonomy-kh_tag.php 376-393). Dead CSS: five across overridden to three.
17. **Pagination.** One shared function (achology_kh_pagination 729-762). Gap: the first page of a list fills 23 cards, the DSRD says 24.

## B. Most worth making one shared component first (most copies, most drift)
1 Breadcrumb; 2 Know Your Psychology logo card; 3 Categories bar; 4 Band header; 5 Kind names, icons and buttons; 6 Editor's Picks and lead row; 7 Explore More block; 8 Section header (the function exists, unused); 9 Reading time and meta line; 10 Topic data (families, colours, names); 11 Faces panel; 12 Quote wall script. The masonry wall Kain named is already one function in PHP; its logo card and its two scripts are the parts to unify.

## C. Rules that disagree between two places (each needs one ruling)
1. Logo cards per wall: DSRD 9 20.0c item 6 and DSRD 8 12.7 say at most one; kh-subject.js allows three (S174/S175).
2. Workbooks lists: DSRD 9 21.0 says the old design until Kain sees them; the code draws the twin design.
3. Book Notes picks: DSRD 20.0b and 21.0 say chosen by hand, four covers; the code shows the newest, names only (S178).
4. Quotes picks: 20.0b says chosen by hand; the code shows the Quote Article Anatomy panel.
5. Faces count: 20.0 says eight; the code shows seven.
6. Old tag descriptions: retired in 34.11 and 35.3, still sent by rank-math-feed.php 879-887 (overridden at a later priority).
7. The purpose line's wording differs between 20.0a and 20.0e.
8. Count label under list titles: DSRD 7 17.1 requires it; the twin lists dropped it (S174).
9. DSRD 7 17.2 still says five items per hub section, from before the redesign.
10. Card byline: DSRD 9 20.0 says never a pen name; achology_kh_card prints "by {author}".
11. "Quotes" against "Quote Articles" in breadcrumbs and lists.
12. Course callout heading: three wordings across lists, single pages and DSRD 9 40 item 6.
13. "Deep Exploration Articles" (topics band) against "Deep Dive Articles" (Kain's S177 title).
14. Hover values: DSRD 8 6.10 says lift 2 over 0.3s; tiles lift 3 over 0.2s; the All Tags pointer card timing differs.
15. Supporting line: DSRD 8 23.4 requires it; the topics band has none.
16. Front page: learn-home.php still has the three latest rows, the trust line and the old top line, all removed by DSRD 9 39.9.
17. Tile layout: DSRD 9 35.0a says four across, 35.6 three (the code does three).
18. DSRD 7 4.3 says four recorded exceptions and lists five.
19. Class clash: .kh-tags names both the front page's pill row and the All Tags page's main element.
Also: DSRD 9 has no section 41; 35.3 is numbered twice; 39.7 and 39.8 are missing.

OWED BACK: Chat names the rulebook's home, decides which parts become shared components first, and rules each conflict in section C (or puts the ones that are Kain's to him).
