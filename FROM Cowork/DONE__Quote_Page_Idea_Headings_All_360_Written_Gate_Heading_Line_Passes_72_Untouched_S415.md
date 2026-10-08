LANE B

**For Chat: item 1 of the Lane B run list is done. The idea heading is written into all 360 swept quote records. Kain said yes to the first ten. Nothing was skipped. The 72 are untouched. Code can push when you have settled the two questions in section 4.**

# DONE: the idea in every quote page's third heading (Cowork, Lane B, S415)

BOARD: Quote pages, the idea headings, Cowork's share done (360 of 360).

## 1. The counts

1. **Written: 360 of 360** (10 in the first batch, Kain's yes, then 350). Skipped: none.
2. **The change per record:** exactly one line, the old third heading replaced by "What Can We Learn From the Idea That ‘…’?". Checked by diff against a copy taken before each change: two diff lines per record (one out, one in) on all 360. No other word changed.
3. **The 72:** untouched. I compared the records still carrying "What Can We Take Away From It?" with the 72 stems in the brief: the two sets are identical.
4. **No dashes, no straight quote marks** in any idea. Every idea is two to seven words. No two pages share an idea.
5. **The fourteen S388 pages.** The ten with a keyword in the old third heading keep it inside the idea, and the gate's keyword line reads PASS (one of four headings) on all ten: Q07033, Q07035, Q07036, Q07037, Q07038, Q07039, Q07040, Q07043 (now "Every Major Breakthrough in History Required Risk", seven words, keyword intact), Q07045 ("Learning What Your Values Really Are"), Q07034. The four opening-only pages (Q07047, Q07048, Q07050, Q07054) carry an idea written like any other and do not repeat the keyword.

## 2. The gate

I ran `content_gate.py` with the quote-page key on all 360, before the change (the 350; the first ten by the first batch) and after.

- **Heading line "section headings, verbatim and in order": FAIL before, PASS after, on all 360.**
- **No new FAIL line on any record, with one exception I fixed.** Three of my ideas carried "empowerment", a banned brand word (Part 16 rule 5) that was not in those records before. I reworded them and re-ran the gate: CQ018-042-2 ("Responsibility Comes Before Personal Power"), CQ018-080-3 ("Real Control Comes Through Taking Responsibility"), CQ018-099-1 ("Taking Responsibility Builds Personal Power"). Their gate now reads none.
- **FAIL lines still on the 350 (and the same lines on the first ten), none from my edit:** empty `stances` (350), empty `signed` (350), link text over five words (333), paragraph band (256), "actually" more than once (72), "truly" (44), "the quoted person is not narrated" (9), title/description/excerpt banned word (3). These are the date-shift fails Code reported in his DONE, section 2. I have not touched them: the brief says nothing else changes.

## 3. Reading calls I made (Chat, overturn any)

- **Title case:** Standard Part 1 rule 9, so "with", "to", "of", "on", "in", "the", "a", "an", "and", "by", "for", "or", "as" stay small. Your brief's example writes "With a Goal"; I followed the rule ("with a Goal"). The gate does not check this.
- **Spelling:** UK (Part 16 rule 13), except where the same word is already in the record's own title or quote ("Fulfillment", "Labeling", "Patronizing", "Judgmentalism", "Actualizing", "Behavioral", "Behavior"), so the heading matches the page. Where the page used neither, UK: "Defence", "Favours", "Counselling".
- **Q07040:** the keyword is "most people don't dialogue" with a straight apostrophe in the record's title and focus keyword. I kept a straight apostrophe in the idea so the keyword matches exactly (Code harness Rule 8, the mechanical-correction case). The gate passes it. If you want a curly one, it is one character in one record.
- **Where the quote is its own idea** (for example "Self-pity is powerless", "Truth is rarely convenient"), the idea is the quote's core in its own words, because a shorter paraphrase would say less. Where the quote is a long sentence, the idea is its core in seven words or fewer.
- No fresh Recipe 10 check was run on the 350, for the reason given in the first-ten DONE: one heading line, read by Kain on the first ten.

## 4. For Chat's eye (not mine to decide)

- **The dating question is still open at the gate.** After my edit the gate still dates every record by its last edit, so about 250 records FAIL the paragraph band and about 330 FAIL link text. Standard Version 11 (section 15.2 item 2) says a change that touches only some lines does not redate the rest; the gate does not yet behave that way. Code cannot push these records as they stand until the gate or the dating is settled.
- **`stances` and `signed` are empty on every record I gated.** That is separate from this brief and blocks any push through the gate.

## 5. What Code needs

The records are changed on disk in `Content Records/quote-page`. Nothing was pushed. The list of every idea is in section 6.

OWED BACK: Chat settles section 4 and writes Code's push brief. The 72 need Chat's placing call (Code's DONE, section 2).

## 6. All 360 ideas

CQ001-002-1: Your Current Understanding Is Where You Start
CQ001-002-2: Nothing Happens Without a Cause
CQ001-005-1: Believing Something Does Not Make It True
CQ001-006-1: Simple Explanations Reveal True Understanding
CQ001-006-2: Contributors Do More Than Consume
CQ001-007-1: Reflection Matters More Than Cleverness
CQ001-008-1: Simple Ideas Drive Real Change
CQ001-009-1: Perspective Shapes the Questions We Ask
CQ001-009-2: Perception Is Not the Same as Reality
CQ001-011-3: Virtue Is a Trait for Flourishing
CQ001-012-1: Everyone Has Beliefs
CQ001-013-1: A Persistent Thought Can Become Reality
CQ001-015-1: We Talk Ourselves Out of Our Wishes
CQ001-016-1: An Idea Is Not Automatically True
CQ001-017-1: Despair Grows Without Peace with Yourself
CQ001-018-1: The Philosophy We Live by Matters
CQ001-019-1: Meaning Can Only Follow Experience
CQ001-021-1: We Can Only Focus on One Thing
CQ001-023-1: Growth Means Leaving the Old Way
CQ001-024-1: Flexible Thinking Keeps Us Growing
CQ001-025-1: Behavioral Norms Are Learned
CQ001-026-1: We Can Become What We Avoid
CQ001-027-1: Culture Starts at Home
CQ001-028-1: Learning Happens Whether We Notice or Not
CQ001-029-1: Media Conditions What We Want
CQ001-030-1: We Remember What Means Something
CQ001-031-1: Our Reactions Come From Past Learning
CQ001-033-1: Even Adults Can Be Influenced
CQ001-034-1: We Choose How We Treat Others
CQ001-035-1: We Are Always Choosing Connection or Disconnection
CQ001-036-1: We Cannot Grow Beyond Our Exposure
CQ001-037-1: Beliefs Are Ideas We Have Validated
CQ001-038-1: We Can Be the Person We Needed
CQ001-039-1: Core Values Underpin Every Decision
CQ001-040-1: Leading Does Not Require Being Far Ahead
CQ001-041-1: Unmet Expectations Cause Disappointment
CQ001-042-1: Acknowledge the Past Without Living There
CQ001-043-1: The Desire to Change Must Win First
CQ001-044-1: Self-Awareness Determines Our Influence
CQ001-045-1: Parts of Us Remain Unseen
CQ001-047-1: Learned Limits Can Keep Us Stuck
CQ001-048-1: Relationships Shape the Quality of Life
CQ001-049-1: Self-Awareness Starts Personal Growth
CQ001-050-1: We Teach Best What We Have Practiced
CQ001-051-1: Growth Means Choosing Life Daily
CQ001-053-1: Public and Private Selves Can Differ
CQ001-054-1: Growth Depends on Awareness
CQ001-055-1: Self-Awareness Deserves First Priority
CQ001-057-1: Identity Shapes How We Behave
CQ001-058-1: Staying Bound to the Past Stalls Us
CQ001-063-1: Understanding Others Before Being Understood
CQ001-064-1: You Decide How Deep to Dig
CQ001-065-1: Being Yourself Is a Real Risk
CQ001-066-1: Imbalance Puts Us Out of Sync
CQ001-068-1: Self-Definition Shapes How We Carry Ourselves
CQ001-069-1: Learning Is Part of Being Alive
CQ001-070-1: Reflection Fuels Personal Growth
CQ001-071-1: Insecurity Often Hides Behind Noise
CQ001-072-1: Who You Are Is Still Unfolding
CQ001-074-1: We React to Traits, Not People
CQ001-075-1: Rule Breaking Should Serve Positive Change
CQ001-076-1: The Goal Matters More Than the Role
CQ001-077-1: First Impressions Tend to Stick
CQ001-078-1: No Personality Trait Is Good or Bad
CQ001-079-1: People Are Not Broken
CQ001-080-1: Change Begins with Owning It
CQ001-082-1: Identity Is Not the Same as Personality
CQ001-082-2: Vision Gives Us a Direction to Travel
CQ001-084-1: Two People Can Read One Experience Differently
CQ001-084-2: Our Attention Favours Ourselves
CQ001-085-1: Caring Does Not Guarantee Clear Communication
CQ001-086-1: Sustaining Is Harder Than Obtaining
CQ001-089-1: Intelligence Is Not a Fixed Quantity
CQ001-089-2: No Single Teaching Method Fits Everyone
CQ001-090-1: Believing in a Cap Limits Growth
CQ001-090-2: Understanding Is Not the Same as Endorsing
CQ001-091-1: Principles Outlast Processes
CQ001-094-1: Unsolicited Advice Can Feel Patronizing
CQ001-095-1: Assumptions Harm Healthy Relationships
CQ001-096-1: We Are All Making Sense of Things
CQ001-098-1: Our Response Shapes Our Inner Experience
CQ001-100-1: Be Yourself and Do Your Best
CQ001-101-1: Forgiveness Releases Us Too
CQ001-103-1: Understanding Bias Is Understanding Yourself
CQ001-104-1: Innovators Earn More Respect Than Imitators
CQ001-105-1: Applying Knowledge Matters More Than Retaining It
CQ001-108-1: We Are Either For or Against Ourselves
CQ001-109-1: Truth Confronts Who We Really Are
CQ001-110-1: We Can See Ourselves Objectively
CQ001-111-1: Panic Is an Attempt to Control Outcomes
CQ001-113-1: We Are the Cause of Our Effects
CQ001-114-1: Growth Comes From Changing Our Interpretation
CQ001-115-1: A Theory Is Not Always Truth
CQ001-117-1: Growth Happens Outside the Comfort Zone
CQ001-118-1: A Value Drives Every Choice
CQ001-119-1: The Simplest Ideas Can Transform Lives
CQ001-120-1: Unmanaged Emotions End Up Managing Us
CQ001-121-1: We Do Not Need Outside Validation
CQ001-122-1: Excitement Is Not the Same as Motivation
CQ001-123-1: Inner Conflict Comes From an Unknown Self
CQ001-124-1: Authentic Confidence Is Not Arrogance
CQ001-125-1: Grounded People Accept Highs and Lows
CQ001-126-1: Insecurity Fuels Criticism of Others
CQ001-127-1: Rigid Defence of Beliefs Isolates Us
CQ001-128-1: Empathy Is the Glue of Relationships
CQ001-129-1: Nobody Wakes Up Intending to Hurt Others
CQ001-130-1: Confidence Makes Us Willing to Share
CQ001-131-1: Defensiveness Blocks Our Growth
CQ001-132-1: Life Is Richer When Shared
CQ001-133-1: Growth Is What Fulfills Us
CQ001-134-1: Comparison Stops Us Actualizing Ourselves
CQ001-135-1: We Do Not Have to Accept Disorder
CQ001-136-1: Life Is Greenest Where We Water It
CQ001-137-1: Humility Is Deeply Attractive
CQ001-138-1: Fear Always Looks to the Future
CQ001-139-1: We Prioritize What We Feel We Lack
CQ001-140-1: The World Pulls Us Off Course
CQ001-141-1: Good Depends on Our Values
CQ001-142-1: Advice Reflects the Person Giving It
CQ001-143-1: Rejection Can Become Direction
CQ001-144-1: Choosing Security Costs Freedom
CQ001-145-1: Connection Determines Our Peace
CQ001-147-1: Honest Requests Make Boundaries Clear
CQ001-148-1: We Can Manage Our Prejudices
CQ001-149-1: Understanding Matters More Than Labeling
CQ001-150-1: Normal Is Built From Experience
CQ001-151-1: Others Care Mostly About Their Own Preferences
CQ001-152-1: Understanding Is the Foundation of Tolerance
CQ001-153-1: Stress Is About Time and Space
CQ001-154-1: Growth Comes From Proving Ourselves Wrong
CQ001-155-1: We Can Stop Judging Others
CQ001-156-1: Putting Others on Pedestals Puts Us Down
CQ001-157-1: Judgmentalism Is a Defence Mechanism
CQ001-158-1: What Irritates Us Is Often Style
CQ001-159-1: Co-Creation Requires Letting Go of Preferences
CQ001-160-1: Distrust Makes Others Feel Threatening
CQ001-161-1: Self-Awareness Gives Us Time to Pause
CQ001-162-1: Resisting Obedience Lets Us Make Our Mark
CQ001-163-1: Authority Cannot Be Transferred
CQ001-164-1: We Never Appreciate What We Expect
CQ001-165-1: Conformity Is an Expression of Mindlessness
CQ001-166-1: Tradition Does Not Always Serve Individuals
CQ001-167-1: Common Sense Becomes Common Through Application
CQ001-168-1: We Can Only Control Our Own Behavior
CQ001-169-1: We Can Turn Hard Experiences Around
CQ001-170-1: Family Teaches Us Inner Peace or Unrest
CQ001-171-1: Inner Freedom Needs Nothing From Society
CQ001-172-1: Self-Management Begins with Realizing Choice
CQ001-173-1: Growth Is Meant to Be Shared
CQ001-175-1: Honesty Follows Trust
CQ018-002-1: Unmet Expectations Hurt More Than Outcomes
CQ018-002-2: Unfulfilled Wants Can Lead to Sadness
CQ018-002-3: Maturity Means Becoming Responsible for Ourselves
CQ018-002-4: Life Is Constant Deciding
CQ018-003-1: Without Vision We Go in Circles
CQ018-004-1: Unawareness Is a Form of Slavery
CQ018-004-2: We Can Master Our Own Destiny
CQ018-005-1: Our Self-Image Shapes Our Results
CQ018-005-2: Growth Requires Commitment to the Process
CQ018-005-3: We Behave Out of What We Believe
CQ018-006-1: Emotions Are Not Illnesses to Fix
CQ018-006-2: Fulfillment Outlasts Happiness
CQ018-007-1: Happiness Is a Weak Motivator
CQ018-007-2: The Wisest Response Is to Reflect
CQ018-008-1: Not Deciding Is Still a Decision
CQ018-008-2: Wanting More Means Letting Go
CQ018-009-1: People Can Handle Only So Much Change
CQ018-009-2: Assumptions Outweigh Good Intentions
CQ018-010-1: We Owe No One Our Time
CQ018-010-2: Who We Let In Shapes Our Lives
CQ018-011-1: Saying Yes or No Is Our Decision
CQ018-011-2: Counselling Requires Education First
CQ018-012-1: Every Action or Inaction Has Consequences
CQ018-012-2: Transformation Needs Nothing Magical or Mystical
CQ018-013-1: People Are Moved by Fear or Freedom
CQ018-013-2: Making Peace with Flaws Lets Us Connect
CQ018-013-3: Listening Is Not the Same as Hearing
CQ018-014-1: Intellect Can Grow Without Character
CQ018-014-2: Nobody Sets Out to Mess Up
CQ018-015-1: Self-Awareness Comes Before Personal Growth
CQ018-015-2: Profound Growth Happens in Private
CQ018-016-1: Digging Deeper Can Become a Trap
CQ018-017-1: Change Is One New Habit Away
CQ018-017-2: Not Every Thought Is True
CQ018-017-3: Most People Miss Their Inner Dialogue
CQ018-018-1: The Desire to Change Must Exceed Comfort
CQ018-018-2: Self-Pity Is Powerless
CQ018-019-1: We Control Only How We Respond
CQ018-019-2: Anxiety Grows From Fear of the Unknown
CQ018-020-1: Taking Too Much Responsibility Blocks Others
CQ018-021-1: All Growth Is Relational
CQ018-021-2: The Name Therapy Guarantees Nothing
CQ018-023-1: We Are Not Entitled to Anything
CQ018-023-2: An Expanded Mind Does Not Go Back
CQ018-024-1: Techniques Are No Substitute for Effort
CQ018-024-2: Our Thoughts Create Our Feelings
CQ018-025-1: Hard Times Offer Chances to Grow
CQ018-025-2: Cannot Often Means Will Not
CQ018-025-3: Congruency Means Actions Reflect Our Values
CQ018-025-4: Mistakes Show Us a Better Way
CQ018-026-1: A Choice Exists Even When Unseen
CQ018-027-1: Change Begins When Desire Outweighs Comfort
CQ018-028-1: Awareness Reveals Our Power to Choose
CQ018-029-1: Every Emotion Is Triggered by a Thought
CQ018-030-1: Interpretation Determines Our Behavior
CQ018-031-1: Thinking Patterns Determine Emotional State
CQ018-031-2: The Past Need Not Repeat Itself
CQ018-032-1: Our Decisions Determine Relationship Quality
CQ018-033-1: Our Foundations Should Rest on Facts
CQ018-034-1: Congruence Means Words Match Actions
CQ018-035-1: Two Positions Cannot Be Held at Once
CQ018-035-2: Subjectivity Limits How Relatable We Are
CQ018-036-1: Every War Begins in One Mind
CQ018-036-2: What the Mind Does It Can Undo
CQ018-037-1: We Enter the World as Clean Slates
CQ018-038-1: Thoughts Are an Ongoing Inner Dialogue
CQ018-039-1: Cannot Is Usually Just a Choice
CQ018-039-2: People Set the Rules They Live by
CQ018-040-1: Problems Remain Until Someone Owns Them
CQ018-040-2: Everything Points Back to Responsibility
CQ018-041-1: Change Often Waits Until We Are Cornered
CQ018-041-2: Honesty About Ourselves Makes Responsibility Possible
CQ018-042-1: Truth Is Rarely Convenient
CQ018-042-2: Responsibility Comes Before Personal Power
CQ018-043-1: Our Choices Determine Our Future Results
CQ018-044-1: Peace with Others Starts Within
CQ018-044-2: Self-Acceptance Should Be Our Goal
CQ018-045-1: People Are Not Labels
CQ018-045-2: Identity Can Be a Mask
CQ018-046-1: Discrimination Comes From Feeling Better Than Others
CQ018-046-2: Cutting Out Unhealthy Relationships Makes Space
CQ018-047-1: Pretending to Be Wise Makes Us Unrelatable
CQ018-047-2: Fulfillment Comes From Making a Difference
CQ018-048-1: What We Have Cannot Motivate Us
CQ018-048-2: Few People Move Beyond Self-Actualization
CQ018-049-1: Guides Cannot Go Beyond Their Own Stage
CQ018-052-1: Doing Our Best Is What Matters
CQ018-054-1: Hidden Beliefs Undermine Us Most
CQ018-054-2: The Future Need Not Repeat the Past
CQ018-054-3: Beliefs Are Built From Past Interpretations
CQ018-055-1: Freedom Lives in Our Capacity to Choose
CQ018-055-2: One Decision Can Transform a Life
CQ018-056-1: Responsibility Starts with Each of Us
CQ018-056-2: Nobody Can Make Us Feel Without Consent
CQ018-065-1: Perception Is Not Always Reality
CQ018-065-2: Emotions Reflect Our Perception
CQ018-070-1: Reflection Brings Real Insight
CQ018-073-1: Accepting Who We Are Ends Despair
CQ018-073-2: Low Self-Opinion Makes Us Easily Offended
CQ018-073-3: Peace with Ourselves Needs Peace with Flaws
CQ018-073-4: Peace with Ourselves Is One Decision Away
CQ018-075-1: Being Real Starts with Understanding Ourselves
CQ018-080-1: Not Everyone Wants You to Grow
CQ018-080-2: Two People Not Growing Together Grow Apart
CQ018-080-3: Real Control Comes Through Taking Responsibility
CQ018-081-1: Belief Shapes Our Wellbeing
CQ018-081-2: Real Influence Needs Nothing in Return
CQ018-084-2: Without Vision We Risk Going in Circles
CQ018-085-1: Every Decision Has a Cost
CQ018-086-1: Mutual Respect Sustains a Relationship
CQ018-089-1: People Confide Only in Those They Trust
CQ018-089-2: Life Hangs on Our Judgments
CQ018-089-3: Relationships Are the Cornerstone of Life
CQ018-091-1: Spotting Flaws in Others Is Easier
CQ018-091-2: Keeping the Peace Can Cost Integrity
CQ018-092-1: Discrimination Is Intolerance for Difference
CQ018-092-2: No Single Label Can Define Anyone
CQ018-093-1: Telling People They Are Wrong Backfires
CQ018-098-1: Self-Regulation Comes Before Social Awareness
CQ018-099-1: Taking Responsibility Builds Personal Power
CQ018-102-2: We Are Not What We Do
CQ018-103-2: Assume the Best of Others
CQ018-106-1: Wrestling with Ideas Is How We Grow
CQ018-107-1: We Can Never Fully Understand Anyone
CQ018-108-1: Effort Today Brings Results Tomorrow
CQ018-109-1: Commitment Makes Anything Learnable
CQ018-110-1: Vulnerability Is a Form of Strength
CQ018-112-1: Positive Focus Is the Key to Influence
CQ018-114-1: Trust Is Missing in Power Struggles
CQ018-115-1: Clarity Moves People to Act
CQ018-119-1: Understanding Each Other Dissolves Tension
CQ018-121-1: We Cannot Do Their Work for Them
CQ018-127-1: Helping Others Helps Us Understand Ourselves
CQ018-128-1: Nobody Has It All Together
CQ018-130-1: Thinking About Doing Is Not Doing
Q04251: Self-Esteem Shifts with How We See Ourselves
Q06984: Helping Is About the Person Seeking Help
Q06985: Helping Is Enabling, Not Just Fixing
Q06986: Most People Have Unused Resources
Q06987: Helping Builds More Effective Self-Helpers
Q06988: Hope Helps Clients Achieve Their Goals
Q06989: Clients Should Become Agents of Change
Q06990: Client Participation Decides the Outcome
Q06991: Respect Is the Foundation of Helping
Q06992: Respect Combines Grace with Toughness
Q06993: Empathy Includes Understanding Dissonance
Q06994: Challenge Is Part of Respecting Clients
Q06995: Life Has Its Own Rules
Q06996: Skill Is More Than Technique
Q06997: Helping Is More Than a Career
Q06998: Success Means Life-Enhancing Outcomes
Q06999: Support and Challenge Belong Together
Q07000: Blind Spots Are Part of Being Human
Q07001: Build the Relationship Before You Challenge
Q07002: Empathy Gives Substance to Every Response
Q07003: Listening Needs Empathic Responding
Q07004: Good Listening Is Focused and Unbiased
Q07005: Helpers Need Working Values
Q07006: Vague Goals Rarely Get Accomplished
Q07007: Hope Drives a Better Future
Q07008: Most Help Comes From Everyday People
Q07009: Coaching Flows From Who You Are
Q07010: A Coach Facilitates Rather Than Fixes
Q07011: We Can Accept Circumstances or Change Them
Q07012: Progress Begins by Deciding Who to Become
Q07013: We Own Our Choices and Consequences
Q07014: There Are No Magic Fixes for Life
Q07015: We Struggle Where We Were Never Educated
Q07016: Wanting Change Is Not Being Ready
Q07017: Knowing Who We Can Become Matters
Q07018: Nobody Is an Expert on Your Life
Q07019: Teaching Is Not the Same as Assisting
Q07020: Others Mature as Far as We Do
Q07021: Our Resourcefulness Limits Our Helping
Q07022: Reading for Insight Beats Reading for Information
Q07023: Healthy Coaching Starts with Wise Goals
Q07024: Communication Forges Healthy Connections
Q07025: Low Self-Esteem Breeds Self-Doubt
Q07026: No Single Right Way to Live
Q07027: A Coach Does Not Hold the Answers
Q07028: Coaching Is More Than Techniques
Q07029: Self-Awareness Unlocks the Potential to Change
Q07030: Coaching Encourages People to Live Well
Q07031: Wise Decisions Align with Priorities
Q07032: Self-Awareness Varies in Accuracy
Q07033: Every Coaching Relationship Begins with a Goal
Q07034: Trust Is the Key Ingredient
Q07035: Wisdom Is Not the Same as Intelligence
Q07036: A Good Coach Will Ask Probing Questions
Q07037: Purpose Is the Cumulative Outcome
Q07038: Vision Is Always Future Oriented
Q07039: People Listen with a Goal of Responding
Q07040: Most People Don't Dialogue
Q07041: Fear Assumes What Might Happen
Q07042: Change Rarely Happens Overnight
Q07043: Every Major Breakthrough in History Required Risk
Q07044: Responsibility Brings Greater Freedom
Q07045: Learning What Your Values Really Are
Q07046: Principles Guide Wise Decisions
Q07047: Priorities Give Life Its Direction
Q07048: A Breakthrough Means Seeing Differently
Q07049: People Seek Coaching to Solve Problems
Q07050: Coaching Combines Learning with Action
Q07051: Our Thoughts Form Our Reality
Q07052: Emotional Perception Means Naming Emotions
Q07053: Time Freedom Means Intentional Time
Q07054: A Good Listener Has No Other Agenda
Q07055: Considering Values Leads to Better Decisions
Q07056: People Resist Change Until Desire Grows
Q07057: We Often Misread Messages Unconsciously

*No em or en dashes in this file; checked before writing.*
