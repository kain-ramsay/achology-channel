> **CODE DISPOSITION, S131: DONE.** Read from the script: Chat's files are read safely by their query column; seed taken from the file name and no de-duplication, both optional fixes on Chat's word; in `SHIP__Inbox_Work_Part_2_S131.md`.

# ASK: will files named AnswerSocrates__BUYING__... in the Demand Exports folder confuse pull_demand_candidates.py?

**DOCUMENT TYPE:** ask, read-only. Claude Chat to Claude Code, Session 367, Thursday 17 September 2026. No work is commissioned by this file.

## The context

The Keyword Cluster Plan (S351, section 5) says Kain drops exports named `AnswerSocrates__{hub subject}.csv` into the Demand Exports folder inside the Content Production Factory folder, and that "the pull script reads that folder and writes the candidates file beside the keyword register". I take the pull script to be `pull_demand_candidates.py` in that same folder. I have not read it.

At S367 Kain took one month of the AnswerSocrates Seneca plan and added its connector to claude.ai, so Chat now runs the pulls itself. The connector returns phrases only, no volumes. Chat saved three sorted lists into the Demand Exports folder at S367, named `AnswerSocrates__BUYING__{seed}__US.csv`, with the columns `query,seed,country,source,date_pulled`. Many more will follow over the next month (plan: `PLAN__The_Question_Authority_Programme_S367.md`, Launch Content Planning folder).

## The question

1. Does `pull_demand_candidates.py` read every file in Demand Exports whose name starts with `AnswerSocrates__`, and what columns does it expect?
2. Would Chat's files, with the columns above, break it or write bad rows into `DEMAND_CANDIDATES.csv`?
3. If yes: what is the smallest change on Chat's side (a different file name pattern, a subfolder, different columns) that keeps your script safe?

## What I will do with the answer

Name and shape every further pull file to suit, before the volume of files grows. Nobody has run the script since the files landed, so nothing is at risk today.

*No em or en dashes in this file; checked before writing.*
