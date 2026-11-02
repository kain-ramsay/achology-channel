> CODE DISPOSITION, S203: DONE. The theme, project record, channel and newsroom clones point at achology-developments and fetch clean; no launchd job or hook writes a kain-ramsay address; achology-factory was not among the five moved and is left as it is.

**For Code (any session, first thing). What this needs from you:** repoint every local clone and every background job on the iMac from `kain-ramsay/<repo>` to `achology-developments/<repo>`, then say so in one line of your next session report.

# NOTE: the five repositories moved into the achology-developments organisation (Chat, Session 451, 2 November 2026)

Kain created the GitHub organisation **achology-developments** on the Team plan today and transferred all five repositories into it: achology-theme, achology-record, achology-component-prototypes, achology-newsroom and achology-channel. He did this so branch protection is enforced, which it was not on private repositories under his free personal account.

**Already done on the iMac Pro:** the clones of achology-channel and achology-newsroom point at `git@achology-github:achology-developments/<repo>.git`, and each has been fetched clean. GitHub redirects the old `kain-ramsay/...` addresses, so nothing has broken, but nothing should rely on the redirect.

**For you on the iMac:** run `git remote set-url origin git@achology-github:achology-developments/<repo>.git` in every clone (the theme, the project record, the prototypes, the channel, and any factory or cloud job that pushes), then `git fetch`. Check any script, launchd job or hook that writes a `kain-ramsay/` address, including the factory copy into achology-newsroom (see ASK__The_Newsroom_Factory_Copy_Stopped_On_22_October_S451).

**Next, Kain's hands:** one organisation-wide ruleset, "protect main" (restrict deletions, block force pushes, default branch, all repositories, no bypass). That ruleset never blocks normal pushes.

OWED BACK: one line in your next session report.

*No em or en dashes in this file; checked before writing.*
