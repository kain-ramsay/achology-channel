import sys, shutil
p = sys.argv[1]
shutil.copy(p, sys.argv[2])  # backup
s = open(p, encoding="utf-8").read()

def insert_before(s, anchor, text):
    assert s.count(anchor) == 1, anchor
    return s.replace(anchor, text + anchor)

def insert_after(s, anchor, text):
    assert s.count(anchor) == 1, anchor
    return s.replace(anchor, anchor + text)

S22 = """### 22.15 The Soft Light hero and its page changes (Kain with Code, theme sessions S162 and S163, 13 October 2026; built 0.707.234 and 0.707.235; written S423 from RULING__Hero_Direction_Soft_Light_Picked_S162, RULING__Hero_And_Section_Title_Simplifications_S162, RULING__Tablet_And_Phone_Hero_S163 and SHIP__Hero_Soft_Light_S163)

**This subsection governs the article, book note and quote page.** Where §22.4, §32.3 or §40 say otherwise, this wins; their older text stays as the record. The workbook takes the same family with its own differences (§37.6). It replaces the S161 hero standard's dark band and speech bubble (RULING__One_Hero_Standard_For_The_Four_Content_Types_S161 section 2); that ruling's lengths (title 50 to 60 characters, subtitle 150 to 170) and its 984 frame stand. Kain's words: "A. Soft light. We found it ... It brings them all together ... One hundred percent."

**1. One hero, direction A, Soft Light (`achology_kh_hero()`).**
- The band is warm cream (`--color-warm-cream`) with a hairline foot. Title in Como, brand dark, its ending one weight lighter; subtitle in brand dark; facts in orange link colour.
- The article's picture and the quote page's portrait dissolve into the band with no frame and no speech bubble, laid in with multiply, at about half strength, faded in from the right and from below, drawn far enough right that nothing dark sits behind the subtitle (worst-case contrast behind the subtitle 6.1 to 8.6 from 1024 up; 4.5 is the minimum).
- The book note stands its cover (the book component, straight, never tilted) on a faint bookshelf that fades into the cream from the right.
- **The quote page's hero is the article's** (Kain: "just lose the quote completely. And just let the banner be the banner. Same as the article."): the faded portrait, with no quote, slip or card in the band. The quote appears once, in the card under the band.
- **What lives in a hero:** breadcrumb, title, subtitle and the date line. Article: the faded picture. Book note: the cover, and "View on Goodreads" in the date line. Quote: the faded portrait. Nothing else: no author line, no audio player, no share buttons, no type label, and no buttons at any width.

**2. The date line ends on the word count (`achology_facts_line()`, shared with the Help answer's reading bar).** Article: "1 October 2026 · 7 Min Read · 1,294 words". Book note: the same, with "View on Goodreads" before the count. Quote: "24 September 2026 · 4 Min Read · 700 words". The count is the contents panel's own number, read and never typed. "Articles at Achology", "Book Notes at Achology" and "Wise Quotes at Achology" leave the line; the breadcrumb still links to each type's list.

**3. The frame (Kain approved, S162: "I 100 per cent approve the container width").** The content frame is 984: the reading column 680 at 18, a 48 gap, and the floating side panel 256, which stays. The page container is 1080 (984 plus two 48 gutters). See §27's S423 amendment.

**4. Section titles and the contents panel.**
- No numbers anywhere: the small orange numbers above section titles on book notes and quote pages are removed, and so are the contents list's 01, 02 numbers.
- A faint Achology bubble mark (about 12 per cent strength, 60 by 46) stands behind the first word of every section title, centred on it and reaching a little out past the writing's left edge, on all three types. Built as a server-side wrap of each title's first word; a title that opens with a tag is left as it is.
- The contents panel loses its "8 sections · 1,294 words" line, its bottom hairline, its rail and its watermark. The entry being read carries a small faint bubble (about 30 wide) behind its first word, kept inside the panel, in place of the orange bar (option "Behind", chosen by Kain from four rendered).

**5. The foot runs full width with no side panel (Kain, S162).** The side panel ends where the reading ends, its last item (the Amazon button on book notes and quote pages) at the reading's foot. The author row, "Explore More ..." and "Ready to Take Your Learning Further?" with its course cards then run the whole 984. This reverses Kain's S146 ruling that the quote page's panel floats down to the closing hairline; the small number above "Explore More ..." goes too.

**6. Tablet and phone (Kain, S163: "yes").**
- 1024 to 1099: the desktop hero with its object column narrowed from 312 to 260, so the words keep about 640.
- Below 1024, one column: the breadcrumb; then the picture in its own row (200 tall on a tablet, 168 on a phone), dissolving into the cream on every side, or on a book note the cover on its faint shelf; then the title, subtitle and date line. Nothing is drawn behind the words below 1024 (contrast 10.1).
- Phone: title 28, subtitle 18, gutter 20. Tablet: gutter 32, and the band's top space 48 (§26).
- Below 1200 the book note's Amazon and author-site buttons, and the quote page's Amazon or course button, sit in the side panel's strip under the contents, where from 1200 up they already sat.

**7. The listen bar is off every quote page** (Kain, decision K10, S422), measured gone at five widths at 0.707.234. Help answers still carry it until Code's backlog line 26 is done.

**8. Two page gate lines, settled by Chat at S423 (reversible; Kain may overturn).** breadcrumb-below: a recorded exception for these three heroes (§26). content-width: 1080 is added to the gate's widths as a standard, because it is Kain's own S161 and S162 frame (§27).

**Open, for Kain's next step (Code's S163 note):** from 1024 to 1199 the hero's words start at the page gutter while the writing starts further in; the first item of his alignment audit of the other components on these pages.

"""

S22_4 = "\n\n**Superseded at S162 and S163 by §22.15 (the Soft Light hero).** Everything below in this subsection is kept as the record of what stood before."

S32 = """### 32.10 The hero from S162 and S163

The book note takes the Soft Light hero and its page changes in §22.15 whole. Its own differences: the cover (the book component, straight, never tilted) stands on a faint bookshelf fading into the cream; "View on Goodreads" sits in the date line before the word count; below 1200 the Amazon and author-site buttons sit in the side panel's strip under the contents. Where §32.3 says otherwise, §22.15 wins.

"""

S37 = """### 37.6 The hero from S162 (Kain with Code, theme session S162)

The workbook is part of the Soft Light family (§22.15): warm cream band, its cover standing straight on a faint bookshelf fading into the cream, and the email box (white field, burnt-orange button) and privacy line in the hero. **Its banner has no date line for now** (Kain: "take it out for now, then we'll figure out where we're going to place that once we get back to designing this actual page"): no date, reading time or "Practical Workbooks". Where that line lives is open, for the workbook page's design. The workbook has no theme template yet; the rest of §22.15 applies when it is built, unless Kain's workbook sitting rules otherwise.

"""

S40 = """

### 40.1 The hero from S162 and S163

The quote page takes the Soft Light hero and its page changes in §22.15 whole. **Its hero is the article's:** the faded portrait, with no quote, slip or card in the band; the quote appears once, in the card under the band. The listen bar is off this page (Kain, K10, S422; built 0.707.234). The foot runs full width with no side panel, reversing Kain's S146 ruling on this page's panel. Below 1200 the Amazon or course button sits in the side panel's strip under the contents. Where anything above in §40 says otherwise, §22.15 wins.
"""

S26 = """**Recorded exception, S423 (Chat, from Code's S163 page gate run; Kain may overturn): the Soft Light hero on the article, book note and quote page (§22.15).** The gate's breadcrumb-below line (48 to the next thing) does not apply to these heroes. On the desktop the picture or cover's top meets the breadcrumb's foot (the roof Kain locked at S161), and the gap from the breadcrumb to the title is 48. On a tablet and phone the picture row sits between the breadcrumb and the title. The top space above the breadcrumb is still 48 on desktop and tablet. The workbook thank-you page carries the same kind of carve-out (Kain, S160).

"""

S27 = """

**AMENDED S423: a third page container, 1080, for the Knowledge Hub reading pages.** Kain approved the 984 content frame at Code's S161 and S162 sittings ("I 100 per cent approve the container width"): the article, book note and quote page sit in a 984 frame (reading column 680 at 18, a 48 gap, side panel 256), inside a 1080 page container (984 plus two 48 gutters). This is his ruling on rendered pages, which is the only way this section allows a new width. It governs those three page types and the workbook page when built; every other reading page keeps 800. The page gate's `CONTENT_WIDTHS` takes 1080 (Code, from FROM Chat at S423). See §22.15."""

s = insert_before(s, "## 23. About Page Timeline", S22)
s = insert_after(s, "### 22.4 Hero", S22_4)
s = insert_before(s, "## 33. Our People Page Layout", S32)
s = insert_before(s, "## 38. Site Search Results Page Layout", S37)
s = insert_before(s, "---\n\n## 27. Page Width Rule", S26)
anchor27 = "The page gate (`page_gate.py`, `CONTENT_WIDTHS`) accepts 800."
s = insert_after(s, anchor27, S27)
s = s.rstrip("\n") + S40 + "\n"
assert "—" not in S22 + S26 + S27 + S32 + S37 + S40 and "–" not in S22 + S26 + S27 + S32 + S37 + S40
open(p, "w", encoding="utf-8").write(s)
print("ok")
