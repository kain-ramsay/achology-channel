> CODE DISPOSITION, S187: WAITS ON a factory session's DONE showing the remaining Machine scripts repointed; content_gate.py is repointed at S187 (TO Chat/DONE__The_302_Help_Answers_Updated_The_73_Wait_On_One_Ruling_S187, section 7), and content_gate_fixtures.py still fails to start on the old path.

> CODE DISPOSITION, S176: WAITS ON a factory session's DONE showing the 26 Machine scripts repointed and the run scripts tested.

# NOTE: the rename is done; the Machine's scripts need repointing before any factory run (S434, 20 October 2026, afternoon)

**What this needs from you:** one factory session, before the Phrasebook run or any other run: repoint the scripts named below to the folders' new places, test the ones a run uses, and file a DONE. The hold from this morning's note stays until that DONE lands.

## What is on disk now

The project folder `04. Content Production Factory + COWORK` is now `04. The Achology Newsroom`. Inside it: `01. The Vault` (the Obsidian vault that was called The Newsroom, unchanged inside), `02. The Machine` (yours: `api_worker` moved whole, every script and register that lay at the old root, `pack_kits` with the five pack yaml files, `workbook_build_tool` and `build_datalabs_pack.py` from the dissolved `0002. Educational Publishing System` folder, The Publish Ready Pipeline and the Defect Register), `03. The Stock` (Content Records, Content Records Archive, Demand Exports, Launch Content Planning, Content Plan Spreadsheets, the Book Notes source bank, Kain's resource posts, the mentorship sources, the workbooks upgrade programme, the online tests, the review tagging run, the Data Labs Handover and the Workbook Cover Images), and `Archive`. The folder `0002. Educational Publishing System` no longer exists. The content type packs' instruction files are archived; their source notes are in the Vault's Working Papers (`pack_sources_S434`); the yaml kits are in `02. The Machine/pack_kits`.

## What moved out from under your scripts

Every script that lay at the old root now sits in `02. The Machine`, one level deeper, and the folders they read moved sideways into `03. The Stock`. These 26 scripts name `Content Records`, `Demand Exports`, `Launch Content Planning` or `Content Type Packs` by a path that is no longer true from where they sit:

attach_author_images.py, book_note_record_headings.py, build_datalabs_pack.py, build_keyword_register.py, content_gate.py, content_gate_acceptance.py, content_gate_fixtures.py, course_autolink.py, derive_author_lead_tags.py, evernote_inventory.py, export_help_keywords.py, fetch_author_photographs.py, import_field_authority_articles.py, import_help_answers.py, import_instructor_articles.py, import_quote_pages.py, publish_factory_copy.py, pull_demand_candidates.py, quote_headings_S407_sweep.py, report_keyword_clashes.py, retire_duplicate_quote_drafts.py, stage5_import_checks.py, stage5_import_checks_acceptance.py, update_published_records.py, workbook_build_tool/build_workbook.py, workbook_build_tool/build_workbook_acceptance.py.

Two of them also point at the dissolved folder by name: `content_gate_acceptance.py` (line 186) and `build_datalabs_pack.py` (line 45). Twelve files inside `api_worker` carry the old folder name, as this morning's note said. The theme's 28 files are not urgent.

The Build lane did not touch any of these and tested none of them, so I cannot say which still run. How you repoint them is your call; one shared root helper rather than 26 edits would be my guess, but it is yours.

## What else changed that you read

The Publish Ready Pipeline is at `02. The Machine/000__THE_PUBLISH_READY_PIPELINE.md`; your CLAUDE.md one folder above the project already says so. The Achology Content Standard and the house book are in the Vault's Working Papers (`standing_documents_S434` and `house_book`); the gate's standards file `content_gate_standards.json` is beside your scripts in The Machine. The Cowork Production Harness is retired in the Archive.

*No em or en dashes in this file; checked before writing.*
