**For Code (theme main session). What this needs from you:** land two invisible fault fixes and one copy line on the About page, add the 960 carve-out to page_gate.py, and confirm in one DONE.

DOCUMENT TYPE: not a page spec (fault fixes and one copy line at existing call sites in `page-about.php` and `shared-parts.php`)

# BRIEF: the About page's two fault fixes, one copy line and the 960 exception (Chat 19, Session 452, 2 November 2026)

Answers ASK__About_Page_Four_Faults_Need_A_Brief_S203, RULING__About_Page_Three_Board_Rows_S209 and RULING__About_Opening_Paragraph_Kains_Words_S209. The governing document is the About page's signed spec, 000__SIGNED_SPEC__About_Page_S390 in the About Landing Page design folder. Its new section 5a now carries every S209 ruling, and its section 3 carries Kain's new opening paragraph and the copy line below.

**1. The header picture loads first.** Drop `loading="lazy"` from the header picture and add `fetchpriority="high"`. It is the largest picture above the fold at all three widths (DSRD 6 section 11). Nothing visible changes.

**2. The ten icons come from the registry.** Draw the ten inline icons in the "Ten Different Ways to Experience Achology" grid through `achology_icon`, with the same shapes. Nothing visible changes.

**3. The 960 column is Kain's recorded exception; add the carve-out.** Kain chose 960 from four rendered widths at S141 and ruled all three gateway pages to it at S142. It is recorded in DSRD 9 section 29.1, item 1, and now in the About spec's section 5a. Add the carve-out to `page_gate.py` for /about/, /reviews/ and /testimonials/, naming DSRD 9 section 29.1 as the exception's home. No options round.

**4. The copy line, word for word.** Under "Achology: What It Is, and Who It's For" (`page-about.php`, the paragraph that begins "Achology teaches psychological knowledge"), replace the 41-word paragraph with these 25 words:

"Achology teaches psychology in a way that grows self-knowledge and character. Here are the questions people most often ask before joining our learning community."

**5. Kain's opening paragraph: the type line is confirmed.** The words you placed at S209 are written home in the About spec's section 3. The type line on RULING__About_Opening_Paragraph_Kains_Words_S209 is confirmed by Chat, so close the row in `harness/spec_intake_waivers.md` by naming this brief.

**Not in this brief, still Chat's:** the three copy points from the Story review, which are the thirteen milestone paragraphs, the 2017 founding date in the founders block against 2014 in the Story, and the words set in capitals. They come to Kain on the page first, in their own brief.

**Checks after you land it:**
- The page gate passes on /about/ with the 960 carve-out.
- The header picture carries `fetchpriority="high"` and no lazy loading.
- The ten icons are drawn from the registry.
- The new copy line reads word for word.
- WebKit read-back at 1280, 834 and 390 shows no sideways scroll and no console error.

OWED BACK: one DONE in TO Chat with the theme version, the four items landed and the read-back.

*No em or en dashes in this file; checked before writing.*
