# Goals Setting Workflow

Disclosed reference for `tony/SKILL.md`, reached only when the user triggers goals setting/review (see the pointer in SKILL.md for the trigger list).

**Output template:** `GOALS-TEMPLATE.HTML`
**For PDF/docx feedback input:** use `pdf` or `docx` skill to read first

## Phase 1 — Goals Creation (v1)

### Step 1: Collect Metadata

| Field | Template Variable | Example |
|---|---|---|
| Full name | `{{PERSON_NAME}}` | "Phat Ho" |
| Role | `{{ROLE}}` | "Software Developer" |
| Level | `{{LEVEL}}` | "Senior" |
| Team(s) | `{{TEAM}}` | "Fyndoo Platform" |
| Review period | `{{REVIEW_PERIOD}}` | "2026" |
| Version | `{{VERSION}}` | "v1" or "v2" |
| Date | `{{DATE}}` | Today's date |
| Submitted date | `{{SUBMITTED_DATE}}` | Same as date for v1 |

### Step 2: Guided Goal Discovery — Multi-Mentor Interview

| Mentor | Interview Question | Focus |
|---|---|---|
| Naval | "What does your ideal life look like in 1 year? Not your job — your life." | Direction, wealth, freedom |
| Tony | "Where are you settling? Where have you accepted good enough?" | Standards, breakthroughs |

**Domain prompts** for specific areas:
- Career: "What's the next level? What skill or role would change everything?"
- Financial: "What milestone would give you more freedom? Freedom number?"
- Health: "How's your energy? One thing to change about health habits?"
- Mental: "What thought pattern drains you most?"
- Communication: "Who do you struggle to communicate with?"
- Calm: "What's creating the most noise? What would simplify everything?"
- Relationships: "Which relationship deserves more investment or repair?"

### Step 3: SMART-ify Each Goal

| Letter | Question | Variable |
|---|---|---|
| S | "What exactly will you do? Clearly enough for someone else to verify?" | `{{GOAL_N_SPECIFIC}}` |
| M | "How will you know? What number or observable change?" | `{{GOAL_N_MEASURABLE}}` |
| A | "Is this realistic given your time and resources?" | `{{GOAL_N_ACHIEVABLE}}` |
| R | "Why does this matter NOW? How does it connect to your bigger picture?" | `{{GOAL_N_RELEVANT}}` |
| T | "By when? Target date?" | `{{GOAL_N_TIMEBOUND}}` + `{{GOAL_N_DATE}}` |

**Challenge vague answers.** "Improve my skills" → "WHICH skill? To what level? How would your manager observe it?"

### Step 4: Define Competencies

| Field | Variable |
|---|---|
| Title | `{{COMP_N_TITLE}}` |
| Type | `{{COMP_N_TYPE}}` (Technical / Behavioral / Leadership / Domain) |
| Current state | `{{COMP_N_CURRENT}}` |
| Target state | `{{COMP_N_TARGET}}` |
| Measurement | `{{COMP_N_MEASURE}}` |

### Step 5: Define Actions

| Field | Variable |
|---|---|
| Action title | `{{ACTION_N_TITLE}}` |
| What exactly | `{{ACTION_N_WHAT}}` |
| Support needed | `{{ACTION_N_SUPPORT}}` |
| Success criteria | `{{ACTION_N_SUCCESS}}` |
| By when | `{{ACTION_N_BYWHEN}}` |

Each goal must have at least 1 action. Actions must be concrete.

### Step 6: Blockers & Support

| Field | Variable |
|---|---|
| Blocker | `{{BLOCKER_N}}` |
| Mitigation | `{{MITIGATION_N}}` |
| Support from coach | `{{SUPPORT_N}}` |

### Step 7: Render

1. Read `GOALS-TEMPLATE.HTML`
2. Apply theme (htp28 / akkuro / topicus)
3. Populate ALL template variables
4. Set version to v1, fill SMART letter boxes
5. Save as `goals-[period]-[name]-v1.html`

## Phase 2 — Goals Review (Coach Feedback)

1. **Ingest** feedback (PDF/docx/text)
2. **Analyze** against original goals — produce SMART compliance table in chat:
   - Per goal: S/M/A/R/T status (check/partial/fail), gaps, coach quotes, proposed changes
   - Per competency: current/target review, proposed changes
   - Actions: updates + new actions from coach suggestions
3. **Confirm** changes with user before proceeding

## Phase 3 — Goals Revision (v2+)

1. Apply confirmed changes to goal text, competencies, actions, blockers
2. Increment version, update date (keep submitted date)
3. Re-render with same theme
4. Save as `goals-[period]-[name]-v2.html`
5. Show brief diff summary in chat
