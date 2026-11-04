DONE: the button family's last audit list is cleared and on the build site as 0.707.793. Nothing needed from Chat.

Theme commit fca21549, pushed; deployed by deploy.py from a clean worktree of HEAD (server, zip and version all agree at 0.707.793). Net figures: 14 files, 20 lines in, 57 out, 37 fewer.

What changed, against DSRD 7 section 5.1 (picks 7, 8, 19):

1. Tags index kinds row now takes the pills, as the search page does: the white 12 corner tiles, cream wash, orange edge, lift and rising pattern are gone (kh-subject.css), the pattern layer is out of learn-tags.php, and buttons.js no longer skips the row. Each kind keeps its arrow at the end, still.
2. Contents links on articles, book notes and quotes: the words keep their own grey on hover (the kh-band.css hover colour removed); the fire line draws on hover and stays on the current item on all three, measured. The audit's "no line on articles" did not reproduce on six articles at 1280 or 390; the line was drawing already.
3. Comments in buttons.css and base.css now name the picks and DSRD 7 section 5.1, not preview folders.
4. Focus rings: About era names and Testimonials tabs lose their 3px rings (the family's 2px ring was already winning); the duplicate on the pricing reveal is removed; About's back to top button and the workbook path pictures now draw the family ring (2px brand orange, 3 out).
5. Dead paint proved and removed: the search clear button's hover and focus, the search A to Z hover, the Testimonials tab washes, the About era Soft Ring outline (live, and off family: it drew a second ring over the pill), and the kh-front A to Z letters' hover and pressed paint. Kept because it is live and not a family control: the search best match card's hover (kh-search.css line 81, a card). buttons.js now also follows a pill row's class changes, so the About era being read is the pill that shows chosen (it was stuck on the first era).

Proof: css_gate equals the baseline exactly (kh-subject 75, cards 47, kh-tag 39, header 33, people 25, warm-room 1; every other file passes). Playwright WebKit, ten pages (tags, article, book note, quote, about, testimonials, pricing, search, workbook, Knowledge Hub front) at 1280 and 390: every element measured Before and After, nothing moved by more than half a pixel. On the build site after the deploy: rest, hover and keyboard focus measured at both widths on every control above, each matching its pick.

Left for whoever owns it: the contents panel's current item still turns dark and bolder as the reader scrolls (a state, not a hover; the brief said hover only, so it stands).
