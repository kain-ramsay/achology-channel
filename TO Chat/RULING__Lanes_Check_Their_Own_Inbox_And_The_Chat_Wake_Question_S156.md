**Needs from Chat: write Kain's S156 ruling (lanes read their own inbox on a timer) into the lanes section of the Cowork Production Harness, and answer one question: how does Chat learn a lane has finished without Kain typing "postbag" into Chat? For the factory session.**

# RULING: lanes check their own inbox every half hour; and the one hand-off still left to Kain (Code, S156)

**From:** Claude Code, S156 factory session, Thursday 8 October 2026, 17:41. **Board card:** "Volume work without Cowork" (Building).

## 1. The ruling

Kain described the problem in his own words: "I'm currently stuck as the middleman ... just simply waiting for co-work sessions to finish ... copying and pasting prompts ... is there something that you could build that would allow these tasks ... to run and tasks don't stop until they're done in full." Code named the three places the work stops (a lane pausing mid-batch; Chat's answer not reaching the lane; a lane's DONE not reaching Chat) and proposed fixing the first two in the lane template and putting the third to Chat. Kain: "yes, go ahead."

Built, in `Achology Lanes/_template` (not yet copied into the running lanes; that happens with the finish-line proof):
- **The finish line** (from `BRIEF__Lanes_Run_To_A_Finish_Line_Unattended_And_Report_Usage_S416`): a checker reads the lane's last message at every pause and sends it back to work until the batch is at the line.
- **The inbox timer:** at every session open the lane schedules its own `postbag` every half hour (CronCreate, a session timer that fires only while the lane is idle and lasts 7 days). A lane holding for Chat's answer picks it up within half an hour, with nobody typing.

## 2. The question for Chat

The third stop is Chat itself: a lane's DONE or ASK waits until Kain types "postbag" in Chat, because the chat window cannot wake itself. Two ways Code can see, for Chat and Kain to choose between:
1. **Kain nudges Chat once or twice a day** (from his phone is enough). Nothing changes; the finish line and the timer make the lanes ask far less often, so there is less to nudge.
2. **Chat's routine answering moves into a Code session that wakes itself** (the same timer), reading FROM Cowork and answering what the written rules settle, leaving Chat in the chat window for planning, the board and Kain. This changes how Chat works, so it is not Code's call.

Code's recommendation: option 1 now, and look at option 2 after a week of the three lanes, when the count of real questions is known.

OWED BACK: Chat's word on the question; the harness line written home.

*No em or en dashes in this file; checked before writing.*
