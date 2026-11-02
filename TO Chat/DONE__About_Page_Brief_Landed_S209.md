**Needs from Chat: nothing to decide; strike BRIEF__About_Page_Two_Fault_Fixes_One_Copy_Line_And_The_960_Exception_S452 and the S203 About ask. Code, S209 theme main session, 2 November 2026.**

# DONE: the About brief landed (theme 0.707.728 and 0.707.729)

1. **Header picture loads first.** `loading="lazy"` gone, `fetchpriority="high"` on. Page gate: image-lcp-candidate PASS at desktop, tablet and phone.
2. **Icons from the registry.** The ten hand-drawn ones were the tile arrows (`$ach_arrow` in shared-parts.php), now `achology_icon( 'arrow-right' )` at 18, with the old 2px stroke kept by one rule beside `.gateway__arrow` in components.css (reaches Reviews and Testimonials too, same arrow). The tile icons were already registry-drawn. Page gate: icon-registry PASS, 97 registry icons.
3. **960 carve-out** in page_gate.py PAGE_EXCEPTIONS for /about/, /reviews/ and /testimonials/, naming DSRD 9 section 29.1 item 1. Page gate prints it as a CARVE-OUT.
4. **Copy line** placed word for word; read back from the build site: "Achology teaches psychology in a way that grows self-knowledge and character. Here are the questions people most often ask before joining our learning community."
5. **Intake row closed** in harness/spec_intake_waivers.md, naming this brief.

**One more, found by the gate after item 4 and Kain's shorter opening words:** the header text became shorter than the 320 artwork, so the first block sat 64 below the header line instead of 48. Fixed at 0.707.729 by the rule Kain set on the Founders' Letter at S188 (Smaller Photo: the picture ends level with the line): About's artwork is 304 on desktop. Every hairline boundary on /about/ now reads 48/48 (32/32 on a phone). A visible change of about 5 percent in the picture's size, made on that ruling; Kain is told.

**Read-back in WebKit** at 1280 by 800, 1280 by 640, 834 by 1050 and 390 by 760: no sideways scroll, no script error, the Story pins at every size from 640 tall on 768 wide and up.

**Page gate on /about/ at 0.707.729:** 7 FAIL lines left, none from this brief: story-proof__label 6px at three widths (a signed value annotated S188, left as the S203 ask said); dsrd6-record (the record's open chapters); orphan and keyword-density (the crawl's 913 missed pages, and a template page with no post body, both tool limits).

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
