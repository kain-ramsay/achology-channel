**Needs from Chat: write the change home in the About signed spec, and confirm this file's type line. For the theme session. Code, S209 theme main session, 2 November 2026.**

DOCUMENT TYPE: not a page spec (Kain's ruling to reuse a signed component at an existing call site)

# RULING: About closes on the Knowledge Hub's learning block, not the enquiries panel (Kain, in the sitting, 2 November 2026)

Kain, on the closing enquiries panel ("Do you have questions about studying with Achology or about becoming an Achology member? Submit an enquiry here"): "I think that's absolutely garbage." His reasoning: someone reading About already knows what Achology is and may be close to signing up for a course, so give them the DiMAP block from the foot of the Knowledge Hub home. Asked yes or no, Code said yes; Kain: "yes".

**What was built.** The enquiries panel (`achology_warm_room` on page-about.php) is replaced by `achology_kh_front_learning_html()`, the learning block Kain signed on the Knowledge Hub home (S180 to S184) and already reused on the subject and list pages exactly as signed (S189): "Where Would You Like to Begin?", the four steps (Explore, Practise, Study, Certify) with step four the Diploma Course in Modern Applied Psychology (DiMAP), and the dark band with Daniel C.'s verified review and the 4.66 gauge. No words changed and no new copy; step one links to the Articles list. The block's stylesheets and its gauge script now also load on About.

**Shipped at theme 0.707.764 to 0.707.768.** The block's own sheet and gauge script, and knowledge-hub.css under them, now load on About; the subject pages' sheet does not, because its page-wide accent rule turned every orange Achology in About's headings from the page's own orange to the brighter one (caught by an element diff of the whole page before and after, fixed at 765). About's article rules for the subheading, h2 spacing, list spacing and quotation rule are held off the block, and from 1200 up it takes the Knowledge Hub's 1104 (its band's slope is drawn to 1104). Measured in WebKit at 1280, 834 and 390: every element of the block identical in size, type and colour to the Knowledge Hub home's (98 of 98; 914, 1399 and 1660 tall on both), the hairline above it 48 and 48 (32 and 32 on a phone), no sideways scroll, and every element of About above it unchanged.

**Why it fits.** The Story now ends on Kain's line "Could your next chapter start right here, today?", and the page closes on the way to start.

**For Chat.** (a) The About signed spec names the warm room as the page's last block (addendum B part 2, S237); it now closes on the learning block. (b) The enquiries panel is unchanged everywhere else it is used.

OWED BACK: one line in FROM Chat saying the change is written home and the type line is confirmed.

*No em or en dashes in this file; checked before writing.*
