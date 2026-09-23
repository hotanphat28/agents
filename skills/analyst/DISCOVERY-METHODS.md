# Discovery Methods

Reference for **The Analysis Layer** steps 2, 3, and 6 in `SKILL.md` — templates and question banks pulled out of the main flow so the step list stays short. Load this when actually running one of those steps; the step names and order stay in `SKILL.md`.

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
