# Discovery Methods

Reference for **The Analysis Layer** steps 2, 3, 4, and 6 in `SKILL.md` — templates and question banks pulled out of the main flow so the step list stays short. Load this when actually running one of those steps; the step names and order stay in `SKILL.md`.

## Step 2 — User & Problem Discovery (Human-Centred Design)

### Empathy Mapping (10 min exercise)
Fill out this template for each primary persona:
| Quadrant | Prompt |
|---|---|
| **Says** | Direct quotes or paraphrases from user interviews, support tickets, feedback |
| **Thinks** | What occupies their mind? What worries them? What are their unspoken goals? |
| **Does** | Observable actions, workarounds, current steps they take |
| **Feels** | Emotional state — frustrated, anxious, confident, overwhelmed? |
| **Pain points** | Top 3 frustrations with the current experience |
| **Gains** | What would delight them? What does "success" look like for them? |

If no real user data exists yet, explicitly mark the empathy map as **assumption-based** and recommend validation methods (user interviews, survey, observation session).

### "How Might We" Framing
Convert each pain point into a "How Might We" (HMW) question to open solution space:
* Pain point: "Users abandon the form at step 3" → HMW: "How might we reduce friction in the application process so users complete it in one sitting?"
* Generate 3-5 HMW questions per persona. These become the design brief for ideation.

### User Journey Mapping
Map the end-to-end experience (not just the system flow):
1. **Stages**: Awareness → Consideration → Onboarding → Usage → Support → Renewal/Exit
2. **For each stage**: what the user does, thinks, feels, and what touchpoints they interact with
3. **Identify moments of truth**: where the experience breaks or delights
4. **Mark pain points and opportunities** directly on the journey

## Step 3 — Business Discovery (Value & Strategy)

### Problem Framing (Hypothesis Template)
Write down the core hypothesis before diving into solutions:
> "We believe that **[target persona]** has a problem with **[pain point]** when trying to **[job-to-be-done]**. If we build **[proposed solution]**, we expect **[measurable outcome]** which we will validate by **[metric/signal]**."

### Business Context Checklist
* **Lifecycle:** Greenfield (new) or Brownfield (enhancement)?
* **Problem & User:** Core problem and primary persona? (Pull from empathy map above)
* **JTBD:** What job is the user hiring this product/feature to do?
* **Success Criteria:** What OKR or North Star Metric does this serve? How will you measure success in 30/60/90 days?
* **Stakeholder Map:** Who has decision power, who is impacted, who needs to be informed?
* **Cost of Inaction:** What happens if we do nothing? (Quantify where possible: lost revenue, churn rate, support cost)

### OKR Drafting Template (If Missing)
If the user does not have a clearly defined OKR for this initiative, the Product Owner persona MUST help them draft one:
* **Objective**: A qualitative, inspirational statement of what you want to achieve (e.g., "Provide a frictionless onboarding experience").
* **Key Results (3-5 max)**: Quantitative metrics that measure if the objective was met. Must follow the format: "Increase/Decrease [metric] from X to Y." (e.g., "Decrease onboarding drop-off rate from 40% to 15%").

### WSJF (Weighted Shortest Job First) — *On-Demand Reference*
Use this framework **only when explicitly requested** to rank competing Epics or Initiatives quantitatively. 
* **Cost of Delay (CoD)** = User/Business Value + Time Criticality + Risk Reduction/Opportunity Enablement (using Fibonacci scale: 1, 2, 3, 5, 8, 13, 20).
* **Job Size** = Estimated effort/complexity (using Fibonacci scale).
* **WSJF Score** = Cost of Delay / Job Size. Highest score wins.

## Step 4 — Functional & Logic Analysis (Mapping)

### User Story Mapping
Translate the User Journey into actionable execution slices:
1. **The Backbone (Activities)**: High-level chronological steps the user takes to achieve a goal (from left to right).
2. **The Body (Tasks/Stories)**: Specific actions or features required to complete each activity (placed vertically below the backbone, prioritized top to bottom).
3. **Slicing (Releases & MoSCoW)**: Draw horizontal lines across the map to group tasks into meaningful releases. Apply the **MoSCoW framework** to label these slices:
   * **Must Have** (Slice 1 / MVP): Non-negotiable for the release.
   * **Should Have** (Slice 2): Important but not strictly necessary for launch.
   * **Could Have** (Slice 3): Nice to have if time permits.
   * **Won't Have** (Excluded): Explicitly out of scope for now.

## Step 6 — Validation Gate question bank

### Desirability Check (BA leads)
* "Do real users actually want this?" — point to evidence (user quotes, data, empathy maps). If no evidence exists, flag it as assumption-based and recommend a validation step (prototype test, survey, or concierge MVP).
* "Does the user journey improve meaningfully? Where exactly?"
* "Are we solving the most painful problem, or just the most obvious one?"

### Viability Check (PO leads)
* "Why do this at all? What happens if we don't?"
* "Is there a cheaper or simpler alternative that delivers 80% of the value?"
* "Does the ROI justify the investment in the next 6-12 months?"

### Feasibility Check (SA leads)
* "Can we build this with our current stack and team capacity?"
* "Do we really need a new service, or can existing infrastructure handle it?"
* "What's the simplest architecture that solves the validated problem?"

### Inversion Check (all personas)
Invert the question before validating: *"What would guarantee this fails catastrophically?"* Each persona lists the top failure modes for their lens (e.g. no adoption, wrong ROI assumption, infra can't scale). These become the seed of the Risks / Impacts section in the Outcome Layer, not an afterthought brainstorm.
