# Glossary of Terms

This document provides a single source of truth for terminology used within the `product-analyze` skill, ensuring context accuracy and preventing hallucinations.

## Frameworks

* **Human-Centred Design (HCD)**: A design and management framework that develops solutions by involving the human perspective in all steps of the problem-solving process. Rooted in empathy, it ensures products are desirable, viable, and feasible. Closely related to Design Thinking.
* **Double Diamond**: A design process model with four phases — Discover (diverge to explore the problem), Define (converge to frame the right problem), Develop (diverge to explore solutions), Deliver (converge to ship the right solution). Prevents jumping to solutions before understanding the problem.
* **Desirability × Viability × Feasibility (DVF)**: The three-lens validation model from IDEO/Stanford d.school. A solution must pass all three: users want it (desirability), the business can sustain it (viability), and the team can build it (feasibility).
* **Wardley Map**: A business strategy framework that visualizes the evolution of components (from genesis to commodity) against user needs, helping determine what to build vs. buy.
* **JTBD (Jobs To Be Done)**: A framework for understanding customer behavior that focuses on the "job" a customer is hiring a product to do, rather than the customer's demographic profile.
* **OKRs (Objectives and Key Results)**: A goal-setting framework that defines qualitative, aspirational Objectives and pairs them with quantitative, measurable Key Results.
* **RICE / ICE**: Prioritization frameworks. RICE = Reach, Impact, Confidence, Effort. ICE = Impact, Confidence, Ease.

## Methods

* **Empathy Map**: A collaborative tool that captures what a user Says, Thinks, Does, and Feels to build shared understanding of user needs. Used at the start of any HCD process to ground decisions in real user behaviour.
* **"How Might We" (HMW)**: A framing technique that turns pain points into open-ended opportunity questions (e.g., "How might we reduce onboarding friction?"). Opens solution space without prescribing answers.
* **Assumption Mapping**: A prioritization technique where assumptions are plotted on a 2×2 matrix of criticality (how bad if wrong) vs. evidence (how confident). High-risk, low-evidence assumptions become research or spike priorities.
* **Lean Canvas**: A 1-page business plan template that helps deconstruct a business idea into its key assumptions (e.g., Problem, Solution, Key Metrics, Value Proposition).
* **Event Storming**: A workshop-based method to quickly find out what is happening in the domain of a software program, focusing on domain events (sticky notes) rather than data structures.
* **Impact Mapping**: A strategic planning technique that visually connects business goals (Why) to actors (Who), impacts (How), and deliverables (What).
* **Story Mapping**: A technique to visualize the product backlog in two dimensions: user journey (horizontal) and release slices/priority (vertical).
* **C4 Model**: An "abstraction-first" approach to software architecture diagramming consisting of Context, Container, Component, and Code diagrams.
* **Strangler Fig Pattern**: A software migration pattern where a legacy system is gradually replaced by a new system by intercepting traffic at the edge and routing it to the new system, feature by feature, until the old system can be safely decommissioned.
* **User Journey Map**: A visualization of the end-to-end experience a user has with a product, mapping their actions, thoughts, emotions, and touchpoints across each stage. Used to identify pain points and moments of truth.

## Documents & Artifacts

* **PRD (Product Requirements Document)**: A document containing all the requirements to a certain product, describing what the product should do and how it should behave.
* **BRD (Business Requirements Document)**: A document detailing the business solution for a project, including customer needs, purpose, and expectations. Focuses on the "Why" and "What" from a business perspective.
* **ADR (Architecture Decision Record)**: A document that captures an important architectural decision made along with its context and consequences.
* **IA (Information Architecture)**: The structural design of shared information environments; the art and science of organizing and labeling websites, intranets, online communities, and software to support usability and findability.
* **RFC (Request for Comments)**: A document authored by an engineer or team to propose a significant technical or process change, designed to gather feedback before implementation.

## Metrics & Strategy

* **North Star Metric**: The single key indicator that best captures the core value your product delivers to its customers.
* **GTM (Go-To-Market)**: The strategy a company uses to bring a new product or service to market, including pricing, positioning, and distribution.
* **AARRR (Pirate Metrics)**: A startup metrics model focusing on Acquisition, Activation, Retention, Referral, and Revenue.
* **MVP (Minimum Viable Product)**: A version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort.

## Agile & JIRA

* **AC (Acceptance Criteria)**: Conditions that a software product must satisfy to be accepted by a user, customer, or other stakeholder (often written in Given/When/Then format).
* **DoR (Definition of Ready)**: A checklist of criteria that a user story must meet before it is considered ready to be pulled into a sprint by the development team.
* **DoD (Definition of Done)**: A checklist of criteria (e.g., code reviewed, tested, deployed) that must be met before a work item is considered fully complete.
* **Spike**: A time-boxed investigation or research task aimed at answering a specific question, reducing risk, or prototyping a solution before full implementation.
* **JQL (Jira Query Language)**: The SQL-like language used to search for issues in Jira.
* **ADF (Atlassian Document Format)**: The JSON-based markdown-like format used by Jira Cloud to render rich text fields.
* **Fibonacci Estimation**: A relative sizing technique using the Fibonacci sequence (1, 2, 3, 5, 8, 13...) to estimate the effort of user stories.
* **T-Shirt Sizing**: A relative sizing technique using t-shirt sizes (XS, S, M, L, XL) to provide rough, high-level estimates for epics or features.

## Architecture & Engineering

* **NFRs (Non-Functional Requirements)**: Requirements that specify criteria that can be used to judge the operation of a system, rather than specific behaviors (e.g., performance, security, scalability).
* **SRP (Single Responsibility Principle)**: A software design principle stating that every module, class, or function should have responsibility over a single part of the functionality provided by the software.
* **OWASP (Open Worldwide Application Security Project)**: A nonprofit foundation that works to improve the security of software, famous for its "Top 10" list of critical security risks.
* **CI/CD (Continuous Integration / Continuous Deployment)**: The practice of automating the building, testing, and deployment of code changes to reduce manual effort and improve delivery speed.
* **IaC (Infrastructure as Code)**: The process of managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.
* **UAT (User Acceptance Testing)**: The final phase of software testing in which actual software users test the software to make sure it can handle required tasks in real-world scenarios.

## Domain-Driven Design (DDD)

* **Domain-Driven Design (DDD)**: An approach to software development that centers the development on programming a model that has a deep understanding of the processes and rules of a domain.
* **Ubiquitous Language**: A common, rigorous language built up by the team and domain experts to connect all the activities of the team with the software. It ensures developers and business stakeholders speak the exact same language.
* **Bounded Context**: A central pattern in DDD. It is the boundary within a domain where a particular domain model applies (e.g., "Sales" context vs "Shipping" context). Inside the boundary, all terms have a specific and unambiguous meaning.
* **Aggregate**: A cluster of domain objects that can be treated as a single unit for data changes. Every aggregate has a root and a boundary.
* **Entity**: An object that is not defined by its attributes, but rather by a thread of continuity and its identity (e.g., a User or an Order).
* **Value Object**: An object that contains attributes but has no conceptual identity (e.g., a Money object or a Color). They should be treated as immutable.
