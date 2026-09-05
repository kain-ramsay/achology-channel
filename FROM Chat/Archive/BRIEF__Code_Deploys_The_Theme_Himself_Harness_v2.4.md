# BRIEF: you deploy the theme yourself from now on. Harness v2.4, Rule 12.

**From:** Claude Chat, S242. **Date:** 2026-08-04.
**Authority:** Kain's ruling, S242, in his own words: the zip-upload step is nonsense and is corrected permanently.

## The ruling

Kain asked why he is uploading theme zips when you are connected to the server. He is right: you already write to the server over SSH (the About portraits were deployed and verified byte-identical this way, and you purge the SiteGround cache with `wp sg purge` over SSH before every gate run). The zip upload was a courier step left over from before that access existed, and it is retired.

The Harness is now Version 2.4. New Rule 12, quoted in full so you have it before H1 next serves it to you:

> **Rule 12. Code deploys; Kain never uploads.** When a change set has passed its gates and its closing commit (Rule 9), Code deploys the theme to the server himself over SSH, purges the cache, and returns the rendered live page link (Rules 6 and 7). Kain never uploads a theme zip, and a message asking him to upload anything is a harness break. Deployment is part of the change set, never a separate step waiting on a human courier. If SSH access to where the theme lives is ever missing or refused, that is a stop-and-ask through TO Chat (Rule 5), never a fallback to a Kain upload.

## Immediate action

Your `SHIP__About_Page_Rebuilt_To_Spec.md` (v0.37.0) is currently parked as "changed, not verified", waiting on a zip upload that is no longer coming. At your next session:

1. Deploy v0.37.0 to the server yourself over SSH, exactly the theme state at commit `90e0877`'s change set close.
2. Purge the cache before gating, per your own S044 finding (item 9b).
3. Run the rest of your SHIP note's "Next" list as written: re-gate the live page, re-walk the changed parts, refresh `RECORD__Page_about.md`, and return the rendered page through TO Chat for Kain to view in Safari, with the DSRD 6 record.

## The one honest check first

Before your first Rule 12 deploy, confirm end to end that the SSH access you hold can write the full theme to where the live theme runs, not only individual files or a build location. If any gap exists between what your key can reach and where the theme lives, name the exact gap in a file to TO Chat and stop there, per Rule 12's own last sentence. Do not route around a gap by asking Kain to upload; that route no longer exists.

Note also that deployment commands sit in your own proposed permissions ask-list (`ssh`, `rsync`, `scp`), so Kain approving each deploy command at your keyboard is expected and correct until his ruling on that proposal lands. That approval prompt is not a harness break; a zip request is.

*No em or en dashes in this file; checked before writing.*
