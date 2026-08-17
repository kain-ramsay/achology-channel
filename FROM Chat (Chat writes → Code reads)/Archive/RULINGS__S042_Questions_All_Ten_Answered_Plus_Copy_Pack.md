# RULINGS: all ten S042 questions answered, with the copy pack and briefs (S233, 29 July 2026)

Context for Code: your five S042 files (the policy-family §7/§8 report, the Manifesto and Ethics records and walk report, and the NOTE on Kain's standard ruling) were read in full in Chat S233. Kain ruled on every open question this session. All ten rulings below carry his explicit approval, given S233. Nothing here is provisional. Your NOTE is banked: his minimum-standard ruling confirms DSRD 6 as written, so no spec change follows from it.

## The ten rulings

**1. Sticky header focus (site-wide, approved fix).** Reserve the header's height plus a small gap at the top of the scroll, in base.css, applied once site-wide (scroll padding on the document root, value: the measured header height plus 8px; you hold the true measured height). Acceptance: tabbing backward up any page keeps the focused element fully visible below the header at desktop, tablet and phone.

**2. Footer column headings (site-wide, approved fix).** At desktop, the About, Achology Schools and Useful Links headings stop being announced as collapsed interactive buttons: render them as plain headings with no button role and no expanded/collapsed state. The phone accordion keeps its current, correct behaviour. Acceptance: a screen reader at desktop hears plain headings; at phone it hears buttons with true state.

**3. Desktop menu announced state (verify first).** Run a real check on whether the trigger's announced state trails the open panel. If confirmed, sync the announced state to reality in the same change set as ruling 2. If not confirmed, say so and close the line. Report either way.

**4. The date line grey (approved fix).** A policy's last-updated or adoption date is something a reader needs, so it leaves the #8A9199 fine-print grey. Move it to the darkest existing DSRD 7 text token that passes AA for reading; no new colour is created. Applies to the policy family and any dated template.

**5. The Cookie Policy's promised settings link (deferred, recorded).** The consent tooling is cutover work. Record the promise as deferred on the Cookie Policy's record, alongside the canonical. Chat has written the requirement onto the Plugins and Site Configuration card so the banner build must deliver the footer cookie-settings link the copy promises; the copy stays as written.

**6. WCAG 2.1 versus 2.2 (both stand, deliberately).** The public Accessibility Statement keeps its 2.1 AA commitment with 2.2 monitored; DSRD 6 keeps 2.2 AA as the internal bar. We promise the lower and hold ourselves to the higher, never the reverse. Chat adds one clarifying line to DSRD 6 §7 at this session's close so no future audit re-flags the pair. No page change.

**7. The §12 row for the Manifesto and the Code of Ethics (ruled).** Both pages belong to the policy-page row. Their adoption dates satisfy §6's visible-date line as the honest equivalent for a standards document; a last-updated line is added only if and when either document is ever revised. Update both records accordingly.

**8. page_gate measurement (approved instrument amendment).** Amend the gate to measure hairline spacing from the geometrically last visible child, not the last child in code order. This is an instrument change under the harness rules: version the amendment in the script's header, state it in your next status line report, and re-run the gate on the Manifesto and Ethics pages; the two spacing rows should then pass.

**9. Reading order (approved fix).** Reorder the document-header variant so the H1 precedes the document figure and its buttons in code order, with the rendered appearance pixel-identical at all three widths (CSS ordering carries the visual). Acceptance: a screen reader meets the page title first; the gate still passes; nothing moves visually. If anything shifts visually at any width, stop and return a preview instead of shipping.

**10. The copy pack (exact replacements, apply verbatim).**

Code of Ethics page:
- First mention: replace "issued by SoMAP" with "issued by the Society of Modern Applied Psychology (SoMAP)". If any earlier occurrence of SoMAP exists on the page, the first occurrence takes the full form instead and later mentions stay short.
- Replace "Our code of ethics - also referred to as our ethical framework - asks two things" with "Our code of ethics, also referred to as our ethical framework, asks two things".
- Replace "was adopted 28 July 2022" with "was adopted on 28 July 2022".

Manifesto page:
- Replace the H2 "Our Commitment to the SOMAP Code of Ethical Practice" with "Our Commitment to the SoMAP Code of Ethical Practice".
- Replace "was adopted on 17 Aug 2019" with "was adopted on 17 August 2019" (full month names on both pages, matching).

Privacy Policy:
- Replace "for example through chat functions, direct messages, or contact exchanges: you do so independently" with "for example through chat functions, direct messages, or contact exchanges, you do so independently".
- Replace "such as cloud hosting, software, and technical support providers: may be located outside the UK" with "such as cloud hosting, software, and technical support providers, may be located outside the UK".

Terms and Conditions:
- Replace "Achology Transactions Ltd (ATL): Scottish company number SC697126: based in Glasgow, Scotland" with "Achology Transactions Ltd (ATL), Scottish company number SC697126, based in Glasgow, Scotland".

Disclaimers:
- Replace "a therapist: client, doctor: patient, counsellor: client, or similar professional relationship" with "a therapist-client, doctor-patient, counsellor-client, or similar professional relationship".

Trust Statement:
- Replace "Learning, especially learning that involves psychology, ethics, identity, values, or human behaviour: will inevitably provoke thought" with "Learning, especially learning that involves psychology, ethics, identity, values, or human behaviour, will inevitably provoke thought".
- Replace "Achology, including all staff, contributors, facilitators, and management: accepts no responsibility" with "Achology, including all staff, contributors, facilitators, and management, accepts no responsibility".

Browser titles (four pages): connecting words render lowercase mid-title: "And" in the Terms and Refunds titles, "Of" and "For" in the Code of Ethics title, and any equivalent in the Manifesto title. Subject-first structure unchanged.

- The page-01.webp filename stands as flagged: rename only when the image is next touched, exactly as you recorded.

## Sequencing

Run these as your next session's change set(s) under the harness, each page re-gated after its fixes, records updated in place. Rulings 1, 2, 3, 4 and 9 are template work and may share a change set; ruling 8 is the instrument; ruling 10 is copy. Nothing else is owed from Chat on these; the DSRD 6 §7 clarifying line (ruling 6) lands on our side tonight.

*No em or en dashes in this file; checked before writing.*
