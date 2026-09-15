# REPORT: item D, zero of fifty pass the current gate, the same fault as I04, I14 and I18

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `REPLY__The_Book_Note_Route_Is_The_One_You_Ran_At_S106_And_S107_S361.md`.

---

Found the route: `tools/book_note_import.py`, in the theme repository, not the factory. Master, then upload CSV, then site, in that order. `--push` hardcodes `post_status=draft`, so it cannot publish on its own; the normal `publish_gate.py` clearance is still the only way anything goes live. Good, and unchanged.

**Before running it: ran `content_gate.py` fresh against every unpublished book-note record, as asked. Zero of fifty pass.**

50 records in `Content Records/book-note/` have no matching post on the install at all (filename against `wp post list --post_type=book_note --post_status=any`, 99 live posts). None of the 50 print `GATE: PASS`.

**44 of the 50 fail on exactly one thing: "paragraphs of 3 to 4 sentences."** The same check, the same shape, that just failed I04, I14 and I18 this session. 4 more fail on that plus total body word count. 1 fails on machine-written tells alone. 1 fails on outcome-or-problem tag count alone. This is not the "15 held on grounds outside that brief, plus 1 on SEO title length" you expected from Cowork's body-and-citation pass; those grounds were checked against an earlier standard. The paragraph-rhythm rule tightened after that pass, and it now blocks nearly the whole batch, not sixteen records.

**Nothing imported, nothing pushed.** Zero records printed PASS, so the instruction's own condition, "import every record that prints GATE: PASS," has nothing to act on today.

This reads as the same structural problem I04, I14 and I18 surfaced, at fifty times the scale: content drafted before the current paragraph-rhythm rule existed, now failing it wholesale. Whatever routes those three to Cowork for a paragraph-split pass is very likely the same fix this whole batch needs, not sixteen individual holds.

---

OWED BACK: whether this goes to Cowork as one paragraph-split job across the fifty, the same shape as the I04/I14/I18 fix, or whether you want the individual failing lines for all fifty first. Either way, I did not import or push anything on the strength of my own reading of "close enough."

*No em or en dashes in this file; checked before writing.*
