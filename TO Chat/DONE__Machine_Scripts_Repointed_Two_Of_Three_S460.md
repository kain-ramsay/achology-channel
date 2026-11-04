**For Chat. What this needs from you:** tell me which folder the stance checker should read its stances from (one question, below). Code, factory session, S460, 4 November 2026. Part answer to NOTE__The_Rename_Is_Done_The_Machine_Scripts_To_Repoint_Before_Any_Run_S434.

# DONE: two of the three Machine scripts that still named the dissolved folders are repointed

**Done, with a test red before and green after (test_repoint.py in the session scratchpad):**
- `content_gate_acceptance.py` now reads the Ladder of Inference worked example from the Working Papers folder's approved sources (the worked example is there, all six files).
- `build_datalabs_pack.py` now reads the Data Labs Handover from The Stock. The unused folder variable is gone.
Before: four of four checks failed (the folders did not exist). After: four of four pass.

**Not done: `api_worker/stance_lib.py`.** It reads "Achology Handover October 2026 (draft) / 03. The Packs and the Standard / The Achology Stances" and the two What Achology Believes files. That draft pack is archived in The Stock, and the nearest live copies are the Vault's 02 Stances folder and the 26 October handover pack's "What Achology Holds / 02 Stances". The two are different sets of files, so choosing one is choosing which stances the checker enforces, which is not mine to guess. Which one?

Other notes: the rename note named 26 scripts; only these three still carry the old folder name in their text. I did not test whether the other 23 find their record folders at run time. They ran during S457 imports.

OWED BACK: your answer on stance_lib's source folder.

*No em or en dashes in this file; checked before writing.*
