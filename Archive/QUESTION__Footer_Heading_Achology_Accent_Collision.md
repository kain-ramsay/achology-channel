# QUESTION: ruling 2 collides with the orange Achology rule in the dark footer (S043)

Status: ruling 2 marked waiting on this ruling. Rulings 1, 3, 4 and 9 shipped in v0.36.35. Nothing was built on a guess.

## The collision, standalone

Ruling 2 (RULINGS file, S233): "At desktop, the About, Achology Schools and Useful Links headings stop being announced as collapsed interactive buttons: render them as plain headings with no button role and no expanded/collapsed state." For a screen reader to hear a plain heading, the element must carry heading semantics, so "Achology Schools" becomes a real heading.

The moment it is a heading, DSRD 7 line 107 fires, word for word: "The orange Achology rule (Kain, standing; written in S224). Wherever the word \"Achology\" appears inside a heading, anywhere on the site, it is rendered in brand orange, wrapped in `<span class=\"policy-next__accent\">`. No exceptions, no per-page judgement."

The span's one CSS implementation (components.css line 375) is unscoped and sets `color: var(--color-orange-link)`, the quieter #C64E14, with this recorded intent: "brand orange sits at 2.9:1 on the off-white panel and fails large-text AA; #C64E14 clears it". DSRD 8 line 1077 documents the same: the accent renders #C64E14 "on the off-white panel".

The footer is the opposite context. DSRD 8 section 19.9 specifies the column heading as "Como 11px/600, uppercase, brand orange (same as desktop)", the whole heading already brand orange on the dark footer. Applying the span as implemented would turn the word Achology #C64E14 on the dark background: no longer brand orange (against DSRD 7 line 107's own required rendering), visibly darker mid-word, and a visual change ruling 2 does not authorise (its acceptance is that only the announcement changes).

## The three levers

1. Wrap the word and add one footer-scoped line so the span inherits the heading's brand orange there. This satisfies every written sentence at once: the word is wrapped, it renders brand orange, the footer heading stays visually identical. My recommendation.
2. Omit the wrap inside the dark footer. The rule says no exceptions, so this needs an explicit ruling, not my judgement.
3. Keep that one column's heading as a non-heading element. This fails ruling 2's acceptance for one column of three and I do not recommend it.

One ruling requested: lever 1, yes or no. If yes, ruling 2 ships in the next change set with the scoped line and the acceptance evidence. If another lever, say which and I build exactly that.

No em or en dashes in this file, checked before writing.
