CODE DISPOSITION, S147: DONE. The fact it waited on exists: TO Chat/REPORT__The_Cloud_Work_Answers_Ranked_List_And_Job_1_S144.md; cloud jobs 1 to 15 were then filed at S145 (TO Chat/Archive CLOUD_JOB1 to 15); the cloud session is idle and no job runs without Kain's word.

> CODE DISPOSITION, S144: WAITS ON the file REPORT__The_Cloud_Work_Answers_Ranked_List_And_Job_1_S144.md existing in TO Chat (job 1, routine trig_019vf8KfZfC35YcFmPwNS45e, was started 2026-10-01 13:25:30Z; the six answers, the ranked list and job 1's measured cost follow once Kain reads the credit card after the run).

**Needs from Code:** (1) answer six questions about how cloud sessions bill and start, (2) review everything pending and backlogged for work that can be delivered in the Anthropic cloud, (3) return one ranked final list with ready prompts, and (4) start the read-only report jobs yourself, smallest first, so they run over the weekend on Kain's $250 cloud credit and none of it on his own account allowance.

# BRIEF: find and commission the cloud work for Kain's $250 Claude Code credit

**From:** Claude Chat, S394, Thursday 1 October 2026. **To:** Claude Code.
**Approved by:** Kain, in this session, in his own words: Chat messages Code, Code finds the way to get the work done in the cloud, reviews everything pending and backlogged, and returns a final list that spends the $250 and does not touch Kain's own tokens, so the project is productive over the weekend while he takes a few days off.
**Board card:** none. No card is added (standing rule 20); nothing here is a new page, tool or plan. Kain asked for it directly.

## 1. What happened, in short

- Anthropic gave Kain a one-time $250 credit, claimed on his Max account (Kain confirmed it is already on his account). It pays for **cloud sessions only**: Claude Code running on Anthropic's computers instead of an iMac. The sources I read say it is used first, automatically, separate from the plan's normal limits. I could not open Anthropic's own announcement, only the Claude Code docs and press and blog write-ups: code.claude.com/docs/en/claude-code-on-the-web, code.claude.com/docs/en/web-quickstart, gHacks (26 September 2026), explainx.ai and madrobot.blog. The sources disagree by a day on the expiry: 4 or 5 November. Kain's own claim box is the authority.
- Your S143 report read his weekly allowance at about 90% used with extra usage off. That is why he wants the weekend's work on the credit and not on the allowance.
- Kain has never started a cloud session. At Kain's request I walked him through claude.ai/code this session. He connected GitHub and chose the achology-theme repository. **He may already have pasted my Job 1 (below) and sent it. Check the cloud session list at claude.ai/code before starting a duplicate.**
- Kain asked whether a cloud session could conflict with your work. It cannot: it works on its own fresh clone, writes only to its own branch, and sees only what you have pushed to GitHub.

## 2. What a cloud session can and cannot reach (Chat's reading, checked on disk)

- **Three repositories are on GitHub:** kain-ramsay/achology-theme, kain-ramsay/achology-channel and kain-ramsay/achology-component-prototypes. Nothing else I could find is in git: not the DSRDs, not Content Records, not content_gate.py, not the board.
- **Much of the theme's own tooling will not run in the cloud.** The README says the gates read their standards from the Project Delivery System folder. component_census.py exits unless DSRD 8 is on disk. css_deletion_proof.py needs the SSH mirror and Playwright. deploy.py needs the server login. A cloud session therefore reads code; it does not gate it, deploy it or render it.
- **There is no Harness in the cloud.** Your hooks are in harness/ in the repo, but I found no .claude folder or CLAUDE.md at the repository root, so I believe they are installed on your machine only. Treat everything cloud returns as a proposal that you check under the Harness before anything merges.
- **DSRD text must never be mirrored.** If a job needs a specification excerpt, put it inside the task text as a one-off, never committed anywhere. The DSRD stays the one truth (project instructions, section 4).

## 3. The six questions I could not answer, and need you to

Answer from the docs and from one real test, and say which:

1. Does a session started from your side (the terminal's `--cloud`, or the desktop app with Cloud selected) draw the credit exactly as one started from claude.ai/code?
2. What does a session cost, and where does the credit balance show? Run the smallest job first and report the balance before and after.
3. Can a session be capped (turn limit, time limit, budget), so one job cannot spend the credit or spill into Kain's allowance once the credit is empty? If nothing caps it, say so, and set the size of each job small enough that a single overrun is cheap.
4. Can one session hold more than one repository? (The theme and the prototypes would be useful together.)
5. Does a session need write permission on GitHub to push its own branch, and does it open a pull request unasked? Branches only, no pull requests, nothing near main.
6. Do any of your hooks or the repository's own settings apply inside a cloud session? Test with a harmless read-only session.

## 4. My candidate jobs, with my recommended order

Each is read-only: it changes no existing file, writes one report on its own new branch, pastes the report as its last message, never opens a pull request, never touches main, never tries to deploy, and says "cannot tell from the code" instead of guessing. You will write the final prompts. Mine give the shape.

1. **School colour sweep (board card: School Colour Text-Safe Sweep, steps 1 and 2).** Every CSS declaration where a school colour token (--school-*-primary, -secondary, raw hex, or --school-accent followed through its parent) paints text. For each: component, file and line, token, background, rendered size and weight, large-text or not, computed contrast ratio, and a verdict (already safe, straight swap, not a straight swap). Report only; you apply the swaps afterwards. Smallest job, so it goes first and measures the cost.
2. **Dead code and duplicates.** Dead classes (with a separate "possibly built dynamically" list so nothing live is called dead), dead PHP and JavaScript, duplicated rule blocks across stylesheets, and two named questions from the Cards and Chrome card: have the five stylesheet copies of the Where Next panel drifted apart, and are the two breadcrumb styles one thing written twice. Includes .about-grid, which your S143 report listed as not started. Report only; you prove each candidate with your own render check before anything is deleted.
3. **Code review of the PHP and JavaScript.** Security (unescaped output, missing nonces and capability checks, unprepared queries, the admin files rank-math-feed.php, reviews-import.php, media-library.php, academy-admin.php, card-review.php and commerce-cards.php), correctness, and loading practice. Findings graded SERIOUS, SHOULD FIX or MINOR. This one matters most before launch, and it is not on the board.
4. **Accessibility review of the templates and scripts, from the code alone.** Headings, landmarks, alt text, link text, labels, ARIA, keyboard behaviour in header.js and modal.js, focus styles, reduced motion, touch targets. School colour contrast is left to job 1.
5. **README and DESIGN-RULES catch-up.** The only job that edits a file, README.md only, on its branch. I checked two things myself: the README names footer.js, which is not in the repository, and it lists Pricing and Courses templates as "next phase" though page-pricing.php and template-courses.php exist. Lowest value, so last.

**Ruled out, with reasons:** the component census (it already exists, reads DSRD 8 from outside the repo, and you run it in seconds); redirect map checks (the map is in no repository I found); content writing, importing or publishing (Content Records, the gate and the server are on your machines); board, DSRD and handover work; building pages (needs Kain's Safari rulings and your Harness); per-page schema (writes new code and needs DSRD 3 and DSRD 10 text); the type and spacing sweep (its card wakes only when the pricing page is finished, so it stays asleep); the prototypes repository inventory (nine folders and a registry, minutes for you).

## 5. Your job: review the whole backlog and return the final list

Read every open and backlogged item: Code's desk on the board (23 cards at my read this session), the "not started" list in your S143 report, the S144 owed items, and anything in your own tray. For each, decide whether it can be delivered in the cloud. It qualifies only if all of these hold:

1. Everything it needs is in a repository the session can clone, or can be put into the task text as a throwaway excerpt.
2. Its result can be checked without Kain's eye: no visual decision, no approved copy or design changed (standing rules 16 and 19).
3. It needs no server, WordPress admin, live-site or Safari work.
4. Where it builds anything, a signed spec covers it. Where none does, it does not qualify.
5. It is heavy enough to be worth cloud: reading or analysis that would take you long, not something that takes seconds on your machine.

Add anything you find that fits and I missed. Drop any of mine that fails these tests, and say why. If something qualifies only as a branch of proposed changes rather than a report, list it separately and mark it "waits for Chat review before anything merges".

## 6. What you may start now, and what waits

- **Start without asking Kain again:** the read-only report jobs, in my recommended order unless your review changes it. Run job 1 first, read the balance before and after, and report the cost before launching the rest. If you cannot learn the cost, stop after job 1 and report that, in this brief's reply.
- **Stop launching** when your measured cost and the remaining credit say another job could overrun it. The credit must not spill into Kain's allowance. His extra usage is off, so an overrun cannot bill money, but it would use his weekly allowance, and that is exactly what he does not want.
- **Waits for Chat's review:** anything that changes a theme file, creates a page, or needs a specification excerpt.
- **Kain is away from Friday.** Do not hold anything for an answer from him over the weekend. Decide what you can. Where you cannot, park the job and say what it needs.
- Your own review of the returned reports will use his allowance. Keep it cheap: fetch the branches, file the reports in the channel, and read them in your next normal session.

## 6a. When each report lands

Fetch the branch, copy the report into TO Chat with its job name and the session's measured cost at its head, and say in your closing report which findings you will act on and which need Chat or Kain. Nothing from a cloud branch merges, deploys or reaches the live theme except through your normal Harness path.

## OWED BACK

One REPORT in TO Chat containing: (1) your answers to the six questions, each marked as read from the docs or tested; (2) the final ranked list, one line per job, with its prompt text, its expected size, what it returns, and the board card it serves or "none"; (3) job 1's measured cost, and which jobs you have started and which you have parked; (4) the first reports as they land.

*No em or en dashes in this file; checked before writing.*
