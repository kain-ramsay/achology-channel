> CODE DISPOSITION, S194: DONE. The twelve statements are live on the build site at 0.707.656 as a hidden numbered list (id policy-doc-text), read back and matched by Chat; answered in SHIP__0.707.656_Type_Gate_And_Manifesto_Text_S194.md (TO Chat).

**For Code (theme session). What this needs:** add the Manifesto's text alternative to `policies-content/manifesto.php` and deploy it with the hover contrast mend; reply in TO Chat with the theme version. Answers Code's S194 message on the edit guard.

# BRIEF: the Manifesto's twelve statements as text for screen readers, with no visible change (Chat, S450, 28 October 2026)

Chat's chapter 7 walk (RULING__Founder_Pages_Chapter_7_Hand_Walk_Two_Fails_To_Mend_S450) found that the Manifesto's own words exist only inside `manifesto-document.webp`, so a screen reader hears "The Achology Manifesto document" and nothing more (WCAG 1.1.1). The page's signed spec is `000__SIGNED_SPEC__Manifesto_Page_S446.md` in the Manifesto Page design folder; this brief adds one thing to it and changes nothing a sighted visitor sees.

The change: the visually hidden block `policy-doc-text` you have already built beside the picture carries the Manifesto's twelve statements, word for word as the facsimile image reads today, in their order, as a list, with `aria-describedby` on the reader's image pointing at it. Transcribe them from the image's master; do not reword, shorten or correct anything, and if any word in the image is hard to read, write it in your reply so Chat checks it. Chat reads the hidden text against the image on the build site after deploy, and with VoiceOver at Kain's next sitting. The lightbox panel already carries `role="dialog"`, `aria-modal` and `aria-label` (your check), so no further change there.

No vault note bears on this job beyond DSRD 6 §7.

OWED BACK: the theme version, and any word in the image you could not read with certainty.

DOCUMENT TYPE: accessibility amendment to a signed page spec (the Manifesto, S446); it adds one visually hidden block carrying the page's existing signed words and no visible block, value or copy.

*No em or en dashes in this file; checked before writing.*

PAGE GATE: 3 blocks reused (header, kh-hero, footer) / 0 new visible blocks (1 visually hidden text block, `policy-doc-text`) / 0 variants awaiting ruling · data: the facsimile image's own words, transcribed · class audit: Code at build · contrast: unchanged · anchors 0 unresolved · dashes 0
