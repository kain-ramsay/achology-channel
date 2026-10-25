DONE, Chat S445 (25 October 2026): enquiries@achology.com written into DSRD 4 section 5.3 (support@ replaced, and the no-SMTP route named as open against DSRD 3), DSRD 2 section 2.9, and the Enquiries signed spec's Added S441 block as item 4a; board cards moved: none (Backlog: Code's Enquiries line stays until the test send and the seventh topic's words).

**For Chat (theme). What this needs from you:** write into DSRD 4 section 5.3 and DSRD 2 section 2.9 that the Enquiries page sends every topic to enquiries@achology.com, replacing support@achology.com, and into the Enquiries signed spec that the editorial inbox is the same address.

# RULING: every enquiry goes to enquiries@achology.com (Kain, theme session S180, 25 October 2026)

## Kain's words
Asked to name the inbox for the Enquiries page, Kain asked Code to read the live site's enquiries page for the addresses in use. Code found five on achology.com/achology/achology-inquiries/: enquiries@achology.com (the main one, beside the phone number), support@, business-partnerships@, media-inquiries@, and manager@ (only in the page's hidden search data). Code recommended enquiries@achology.com. Kain: "yes".

## What it changes
DSRD 4 section 5.3 says the form is "a message to support@achology.com". The page built at 0.707.501 sends every topic, the mistake topic included, to enquiries@achology.com, set once on the server (ACHOLOGY_ENQUIRIES_INBOX in enquiries-setup.php). Routing by topic to other inboxes is one line each there, if the team ever wants it.

## Also in this build, for the record
The two orange "pending" reply window lines and the confirmation's reference row are not on the page (the spec's acceptance 5 allows removing them until Karen's window is written). The mail goes out through WordPress's own mail on the host; no SMTP plugin is installed on the build site, so delivery is proved by a test send, which waits on Kain's yes.

OWED BACK: the three document lines.

*No em or en dashes in this file; checked before writing.*
