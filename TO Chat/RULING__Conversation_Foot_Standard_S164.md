First line of need: Chat, write Kain's S164 rulings on the close of the three content pages into DSRD 9 section 22.15 (it replaces the two paths at the foot of every article, book note and quote page; the workbook thank-you page keeps the two paths).

# RULING: the close is "Keep the Conversation Going", Side by Side (theme session, S164, the page sweep)

**From:** Claude Code, theme session S164, 13 October 2026. **Ruled by:** Kain, in the sitting, over five rounds in `previews/conversation-s164`. **Session:** theme. **Board card:** the four content page templates. **Follows:** RULING__Contents_Lines_And_Foot_Conversation_S163 section 3, which this settles.

## 1. What Kain chose
- **Twin bubbles, Side by Side** ("very clean, that's brilliant"): a cream course bubble with an orange line and a dark community bubble, side by side and level, tails down and outward.
- **His own two pictures, no text** ("Enrol on the Course No Text", "Join the Community No Text"), faded in at the top of each bubble behind the book, half drained toward the brand's tones, at the **Quiet** strength ("somewhere in between option one and option three ... a bit more subtle"; "option three is good").
- **The text given more weight** ("a little bit hard to read"): the descriptions take the dark long-form colour that base.css names for long-form text.
- **Matched pictures:** the course cover in the site's 3D book, and a community cover drawn for the same book. Kain ruled a 3D book beside a flat tile "completely inappropriate".

## 2. The standard, as built (0.707.241)
- **Fixed words:** the heading "Keep the Conversation Going"; the subtitle "You've finished this {type}. Choose how you'd like to carry it on: on your own, or alongside others who are learning too."; the labels "Study it on your own" and "Talk it through with others"; the community name "Live Learning in the Achology Community", its description, its facts (Live every day, Mentorship, Free coaching), and its button "Explore Membership".
- **Read from the page:** the course is the page's best-matched course, the same one as the side panel. Its name, its approved description (data/courses.json hero_description), its cover, its lesson count and its ratings are read, never typed. The button reads "Explore This Course".
- **Varies by type:** one word, "article", "book note" or "quote".
- **The mirror:** both bubbles share one grid of six rows, so each row starts level on both sides. The community words are written to the course words' lengths: course names run 51 to 69 characters and descriptions 167 to 190.
- **No course matched:** the community bubble stands alone, centred, as the two paths did. Kain's open choice from S163 (a DiMAP fallback) is still his. It was not raised in the sitting, so nothing was changed.
- **Lesson count and ratings:** shown. Kain ruled "the facts are really good, really like the facts on one line".

## 2a. Later the same sitting: Video and Live, and Kain's own words (0.707.242 and 0.707.243)
- **Kain's words, one line each on desktop:** the heading is "Ready to Further Your Learning?" and the line beneath is "You've finished this {type}. Choose how you'd like to continue: on your own or with like-minded others?"
- **No more books.** Kain: "a diploma course ... is a course. And the community is a membership subscription ... these images would suggest that both are books." His choice of four: **Video and Live** ("that's totally the one we want").
  - The course is a lesson ready to play: its own course-card artwork (images/courses/course-NNN-540.webp) in a player, with a play button, a progress line and the lesson count.
  - The community is a session happening now: Kain's group picture (no text), a Live tag and three participant tiles.
  - Both use the same frame. The background wash and the drawn community cover are retired.
- **Also from Code's critique, accepted by Kain:** the words read from the left; the tails turn in toward each other; more room above the footer.

## 3. Where it lives
`achology_close_conversation()` in knowledge-hub-parts.php; section 7 of kh-band.css; images/close-community-bg.webp (close-course-bg.webp retired at 0.707.243).

OWED BACK: DSRD 9 section 22.15 records section 2 as the close's standard; RULING__Contents_Lines_And_Foot_Conversation_S163 section 3 is answered by it.

*No em or en dashes in this file; checked before writing.*
