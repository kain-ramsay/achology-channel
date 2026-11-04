> WITHDRAWN by Chat, S458, before any work: not a fault. Kain: "Are you not aware that the website is still getting built?" The home page and the course pages are not built yet; the course page is in design now.
> CODE DISPOSITION, S210: WAITS ON the theme main session; read in full by the course page block 3 design sitting, which works only its preview (Kain's one session, one job).
**For Code (theme main session). What this needs from you:** find why the home page and the academy pages answer Page Not Found on the build site, fix it, and prove it. A fault fix; no design change. Chat, Session 458, 4 November 2026.

# BRIEF (fault): the home page and every course and school page are Page Not Found

**What Chat measured, 4 November 2026, from outside (curl, no login):**

| Address | Status | What shows |
|---|---|---|
| / | 200 | the 404 template: "Page not found", "Oops! You're on a page that no longer exists." |
| /academy/ | 404 | Page Not Found |
| /academy/neuro-linguistic-programming/diploma-modern-applied-psychology/ | 404 | Page Not Found |
| /courses/ | 200 | fine |
| /learn/ | 200 | fine |

Two of your own sessions saw it in passing (SESSION_REPORT__S203_Buttons; DONE__Button_Family_Audit_Remnants_Cleared_0707791_S208: "home and course pages are not found on the build site") and left it as not their job. It is now this brief's job.

**Why it matters now.** Published pages link into the academy: every quote article's "View this Course on Achology" and its course card point at a course page, so every published quote page carries a broken link today. The course page design session is also building block 2 and block 3 against pages the build site cannot serve.

**What done looks like.**
1. The cause named in one sentence (a rewrite rule, a missing page or post, a template condition, a deploy, or something else), and when it began if the log shows it.
2. Fixed. `/` serves the home page; `/academy/`, each of the seven school pages and all 28 course pages answer 200 with their own templates, at the addresses DSRD 1 section 2.3 sets.
3. Proof read from outside: a status table for `/`, `/academy/`, the seven schools and the 28 courses, every one 200, none showing the 404 template. One quote page's course link clicked through and landing.
4. Nothing visible changes on any page beyond the pages returning.

OWED BACK: TO Chat/DONE__Fault_Home_Page_And_Every_Course_Page_Not_Found with the cause, the theme version if any, and the status table.

*No em or en dashes in this file; checked before writing.*

DOCUMENT TYPE: not a page spec (a fault fix on pages already built and signed). Added by Chat, Session 458.
