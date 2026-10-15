> Chat: please pass this to Kain one step at a time. It answers item 4 of REPLY__Yes_To_All_Four_Audit_Questions_S426. It needs his hands because it is a setting on his own GitHub account.

# NOTE: how Kain checks that the main branch of each repository cannot be wiped (Code, factory session, S170, Thursday 15 October 2026)

**What it is for.** Several background jobs push to these repositories. Branch protection stops anyone, including a mistake, from deleting the main branch or overwriting its history by force. It does not stop the normal pushes the jobs make. **Do not tick "Require a pull request" or "Require status checks": those would block the background jobs.**

**Which repositories** (all under the account kain-ramsay, all private): the theme repository, the record repository, the component prototypes repository, and the new factory copy repository. The channel repository too, if it has its own GitHub page.

**The clicks, for each repository in turn:**
1. Open github.com in Safari, signed in, and go to the repository's page.
2. Click "Settings" in the row of tabs along the top of the repository.
3. In the left column click "Rules", then "Rulesets".
4. If a ruleset already exists and its name mentions the main branch, click it and go to step 8. If the list is empty, click the green "New ruleset" button, then "New branch ruleset".
5. In "Ruleset name" type: protect main.
6. Set "Enforcement status" to "Active".
7. Under "Target branches" click "Add target", then "Include default branch". Under "Rules" make sure these two are ticked: "Restrict deletions" and "Block force pushes". Leave everything else unticked.
8. Check there is nothing under "Bypass list" (it should say no bypass). Click the green "Create" button (or "Save changes" if one existed).
9. Tell Chat the repository is done. Repeat from step 1 for the next one.

**What Kain will see when it works:** the Rulesets page lists "protect main" with the word Active beside it.

OWED BACK: Kain's word, per repository, that it shows Active. Nothing waits on it.

*No em or en dashes in this file; checked before writing.*
