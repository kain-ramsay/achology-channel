diff --git a/README.md b/README.md
index 37afb27..7e2f79d 100644
--- a/README.md
+++ b/README.md
@@ -16,16 +16,28 @@ This repository **is** the theme. There is no page builder and no framework: cle
 |---|---|---|
 | Design system | `base.css`, `components.css`, `cards.css`, `fonts.css` + the font files | Complete. All three faces self-hosted since S103: Como, Mulish, Caveat. The site makes no request to Google |
 | Site header | `header.php`, `header.css`, `header.js`: sticky bar, 3 mega menus, mobile overlay | Complete |
-| Site footer | `footer.php`, `footer.css`, `footer.js`: link grid, socials, mobile accordions | Complete |
-| Policy pages | `template-policy.php` + `policies-content/`: all 7 legal pages, wording baked in | Complete |
+| Site footer | `footer.php`, `footer.css`: link grid, socials | Complete |
+| Policy pages | `template-policy.php`, `policies.css` + `policies-content/`: the 7 legal pages, the Code of Ethics, the Manifesto, the Founders' Letter and How We Write, wording baked in; `policies-content/policies.php` is an analyser-feed copy of the /policies/ wording and is never rendered to visitors | Complete |
 | Policies index | `template-policies-index.php`: the /policies/ overview page | Complete |
-| Help section | `archive-faq_article.php`, `taxonomy-faq_category.php`, `single-faq_article.php` + `faq-setup.php`, `faq-icons.php`, `help.css`, `help-article.js`: /help/ landing, 15 category pages, article page | Complete (article import pending) |
-| People pages | `template-our-people.php`, `template-author-profile.php` + `people-setup.php`, `people.css`, `images/people/`: the Our People hub, the ten author profile pages, and the article author signature card | Complete (Kain creates the 11 pages in WP) |
-| Knowledge Hub | `taxonomy-kh_category.php`, `learn-listing.php`, `single-article.php` + `knowledge-hub-setup.php`, `knowledge-hub-parts.php`, `knowledge-hub.css`: 7 category hubs, 32 listing URLs, the article page | Complete (awaiting Hub content; article page carries declared placeholder zones) |
-| About page | `page-about.php`, `about.css`, `about.js`: the /about/ page and "The Achology Story" timeline | Complete |
+| Help section | `archive-faq_article.php`, `taxonomy-faq_category.php`, `single-faq_article.php` + `faq-setup.php`, `faq-icons.php`, `help-parts.php`, `help.css`, `help-article.js`: /help/ landing, 15 category pages, article page | Complete (article import pending) |
+| People pages | `template-our-people.php`, `template-author-profile.php` + `people-setup.php`, `people.css`, `people.js`, `images/people/`: the Our People hub, the ten author profile pages, and the article author signature card | Complete (Kain creates the 11 pages in WP) |
+| Knowledge Hub | `taxonomy-kh_category.php`, `learn-listing.php`, `single-article.php` + `knowledge-hub-setup.php`, `knowledge-hub-parts.php`, `knowledge-hub.css`, `knowledge-hub.js`, `kh-band.css`: 7 category hubs, 32 listing URLs, the article page | Complete (awaiting Hub content; article page carries declared placeholder zones) |
+| About page | `page-about.php`, `about-setup.php`, `about.css`, `about.js`: the /about/ page and "The Achology Story" timeline | Complete |
 | 404 page | `404.php`: the wayfinding page | Complete |
 | SEO tooling | `rank-math-feed.php`: admin-only analyser feed | Complete |
-| Remaining page templates | Homepage, Academy, Schools, Courses, Membership, Pricing | Next phase |
+| Theme core | `style.css`, `functions.php`, `index.php`: the theme header, the feature-file loader and the stylesheet and script enqueues, and the fallback template | Present |
+| Shared blocks | `shared-parts.php`, `shared-parts.js`, `global-impact.php`, `global-impact.css`, `warm-room.css`, `modal.js`, `listen.js`: the site-wide block renderers, the global impact block, the closing enquiries panel, the one dialog controller and the read-aloud control | Present |
+| Courses page | `template-courses.php`, `courses-directory.css`, `courses-directory.js`, `courses-setup.php`: the /courses/ page and the 28 courses as data | Present |
+| Course pages | `template-course.php`, `course-parts.php`, `course.css`, `course.js`: one template for all 28 course pages | Present |
+| Pricing page | `page-pricing.php`, `pricing-parts.php`, `pricing.css`, `pricing.js`: the /pricing/ page | Present |
+| Commerce cards | `commerce-cards.php`: the four commerce cards as data and as components | Present |
+| Card sheets | `page-cards.php`, `card-review.php`: the card sheet, and the four-family commerce card review page | Present |
+| Reviews | `page-reviews.php`, `reviews-setup.php`, `reviews-import.php`, `reviews.css`, `reviews.js`: the /reviews/ page, the `review` post type, and the one-way loader for the Notion Review Bank | Present |
+| Testimonials | `page-testimonials.php`, `testimonials.css`, `testimonials.js`: the /testimonials/ page | Present |
+| Book Note page | `single-book_note.php`, `book-note.css`, `book-note.js`: the Book Note page | Present |
+| Quote page | `single-quote.php`, `quote.css`: the Quote page | Present |
+| Admin tools | `media-library.php`, `academy-admin.php`: folders and "Used on" for the Media Library, and the Schools and Courses side tabs in WordPress admin | Present |
+| Remaining page templates | Homepage, Academy, Schools, Membership | Next phase |
 
 ## How the policy pages work
 
