# Generative AI for Project Management — Learner Guide

**Course Code:** C013  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 28 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Project Initiation and Planning with GenAI  (Day 1 · 3 connected labs)](#topic-01--project-initiation-and-planning-with-genai--day-1--3-connected-labs)
  - [Use GenAI as a Project Co-Pilot](#use-genai-as-a-project-co-pilot)
  - [Initiate the Project and Develop the Charter](#initiate-the-project-and-develop-the-charter)
  - [Identify Stakeholders and Plan Engagement](#identify-stakeholders-and-plan-engagement)
  - [Plan Scope with Requirements, Deliverables and a WBS](#plan-scope-with-requirements-deliverables-and-a-wbs)
  - [Build a Credible Schedule and Cost Baseline](#build-a-credible-schedule-and-cost-baseline)
  - [Integrate Quality, Resources, Communications, Risk and Procurement Plans](#integrate-quality-resources-communications-risk-and-procurement-plans)
  - [Lab 1 — Build the AI Working Agreement and Project Charter](#lab-1--build-the-ai-working-agreement-and-project-charter)
  - [Lab 2 — Build the Stakeholder Engagement and Communications Plan](#lab-2--build-the-stakeholder-engagement-and-communications-plan)
  - [Lab 3 — Build the Integrated Project Management Plan](#lab-3--build-the-integrated-project-management-plan)
- [Topic 02 — Project Execution and Delivery with GenAI  (Day 2 morning · 3 connected labs)](#topic-02--project-execution-and-delivery-with-genai--day-2-morning--3-connected-labs)
  - [Direct and Manage Project Work](#direct-and-manage-project-work)
  - [Manage Project Knowledge and Decisions](#manage-project-knowledge-and-decisions)
  - [Acquire Resources and Manage the Team](#acquire-resources-and-manage-the-team)
  - [Manage Quality and Deliverable Acceptance](#manage-quality-and-deliverable-acceptance)
  - [Manage Communications and Stakeholder Engagement](#manage-communications-and-stakeholder-engagement)
  - [Build Evidence-Led Status and Forecast Reporting](#build-evidence-led-status-and-forecast-reporting)
  - [Lab 4 — Turn the Baseline into an Executable Delivery System](#lab-4--turn-the-baseline-into-an-executable-delivery-system)
  - [Lab 5 — Manage Team Knowledge, Quality and Stakeholder Delivery](#lab-5--manage-team-knowledge-quality-and-stakeholder-delivery)
  - [Lab 6 — Build the Evidence-Led Project Status Pack](#lab-6--build-the-evidence-led-project-status-pack)
- [Topic 03 — Manage Project Risks with GenAI  (Day 2 afternoon · 3 connected labs)](#topic-03--manage-project-risks-with-genai--day-2-afternoon--3-connected-labs)
  - [Implement Risk Responses and Manage Issues](#implement-risk-responses-and-manage-issues)
  - [Conduct and Control Procurements](#conduct-and-control-procurements)
  - [Monitor and Control Project Work](#monitor-and-control-project-work)
  - [Perform Integrated Change Control](#perform-integrated-change-control)
  - [Control Scope, Schedule, Costs, Quality and Resources](#control-scope-schedule-costs-quality-and-resources)
  - [Monitor Communications, Stakeholders and Risks](#monitor-communications-stakeholders-and-risks)
  - [Close the Project or Phase](#close-the-project-or-phase)
  - [Lab 7 — Build the Risk, Issue and Procurement Response Cockpit](#lab-7--build-the-risk-issue-and-procurement-response-cockpit)
  - [Lab 8 — Run Integrated Change Control and Baseline Impact Analysis](#lab-8--run-integrated-change-control-and-baseline-impact-analysis)
  - [Lab 9 — Close the Project and Capture Reusable Lessons](#lab-9--close-the-project-and-capture-reusable-lessons)
- [Wrap-Up — Operate the Integrated System](#wrap-up--operate-the-integrated-system)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This guide teaches a human-owned method for using generative AI across the project life cycle. It follows the approved C013 topic spine: initiation and planning, execution and delivery, then risk, control and closure. The project-management concepts come first; the connected BeaconWorks portal labs then apply them to one synthetic project.

Use the guide as a reference after class. Each concept section explains what the practice is, why it matters, how it works, a worked example and situations in which the technique should or should not be used. Source links point to authoritative project, AI-risk and prompting guidance. All generated project content remains a draft until a named human owner checks and approves it.


## Course Learning Outcomes

- LO1: Develop project parameters and an integrated project plan with GenAI according to business requirements.
- LO2: Resolve project delivery challenges by using GenAI to support people, knowledge, quality, communications, resources and budgets.
- LO3: Anticipate, monitor and respond to project risks and changes with GenAI while keeping decisions evidence-led and human-owned.
- LO4: Control project performance, obtain acceptance and close a project or phase with traceable records and reusable lessons.


## Before You Start — Preparation

**What you need**

- A Windows or macOS laptop with a modern browser and spreadsheet application.
- Access to one organisation-approved generative AI assistant such as ChatGPT, Claude or Copilot.
- A text editor and the supplied synthetic files in labs/assets/.
- A local folder named C013-BeaconWorks-Project for all lab outputs.

**Verify your setup**

Create the project folder, open the supplied scenario files and confirm that you can save Markdown and CSV files. If no AI assistant is available, work with the provided prompt templates and complete the human-review steps manually.

```bash
C013-BeaconWorks-Project/
  01-initiation/
  02-planning/
  03-delivery/
  04-control/
  05-closure/
```

**Conventions used in every lab**

- Replace placeholders such as <SOURCE> and <STATUS_DATE>; never paste placeholder brackets into a final record.
- Use only the synthetic evidence supplied with the labs or information you are authorised to process.
- Mark FACT, ASSUMPTION, OPTION and UNKNOWN explicitly in material AI outputs.
- Save both the AI draft and the human-approved version when a decision or baseline is affected.


## Topic 01 — Project Initiation and Planning with GenAI  (Day 1 · 3 connected labs)

AI working method · charter and stakeholders · integrated management plan · scope, schedule, cost, quality, resources, communications, risk and procurement

**Key concepts**

- Human-owned AI workflow — Use GenAI to propose, structure and challenge; a named project owner validates every decision.
- Project charter — Connect the business need, measurable objectives, boundaries, authority and success conditions.
- Stakeholder strategy — Separate influence, interest, impact and information needs before choosing an engagement approach.
- Integrated baseline — Link deliverables, work packages, dependencies, resources, costs and acceptance evidence.
- Management plans — Define how scope, schedule, cost, quality, communications, risks and suppliers will be managed.
- Planning uncertainty — Record assumptions, confidence, sources and review triggers instead of hiding uncertainty in polished prose.


### Use GenAI as a Project Co-Pilot

A generative AI assistant creates likely text, tables and alternatives from the instructions and context it receives. For project work it is best treated as a co-pilot: useful for organising supplied evidence, generating options and challenging a draft, but not an accountable decision-maker or a source of project truth.

Project records affect money, commitments, people and suppliers. Fluency can disguise a missing source, an invented dependency or an unrealistic estimate. A controlled workflow makes the human owner, evidence boundary and review gate visible before an output enters the project record.

**How it works**

- Use C-O-S-T-A-R: Context, Objective, Sources, Tasks, Acceptance criteria and Review.
- Delimit approved source material; require the assistant to label facts, assumptions, options and unknowns.
- Verify dates, quantities, commitments and names against primary project records before approval.
- Keep a prompt-and-output log for material decisions and remove restricted data before using an AI service.

**Worked example**

- The project manager supplies the approved project brief and asks for a charter draft, not a new business case.
- The response includes a source ledger and marks an unstated target date as UNKNOWN.
- The sponsor selects the objective and the project manager records the final wording and rationale.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task is to structure, summarise, compare, draft, critique or explore options from approved inputs. | The prompt would expose confidential, personal or security-sensitive information to an unapproved service. |
| A human owner can check the result against evidence and has authority to approve the final record. | The output would create a commitment, forecast or decision without evidence and named human approval. |

**Authoritative references**

- https://www.pmi.org/learning/thought-leadership/prompt-engineering
- https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices
- https://www.nist.gov/itl/ai-risk-management-framework
- https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems

---


### Initiate the Project and Develop the Charter

Initiation turns a business need into an authorised project. A practical charter names the purpose, measurable objectives, high-level deliverables, exclusions, constraints, major assumptions, milestone horizon, initial risks, sponsor and project manager authority. It is a decision record, not a detailed plan.

Teams that begin with solution activity before confirming the problem and authority often optimise the wrong work. GenAI can expose ambiguity and draft alternatives, but only the sponsor and accountable leaders can decide which outcome, tolerance and boundary the organisation accepts.

**How it works**

- Trace every objective to the business need and express it with a measure, target and time horizon.
- Separate in-scope deliverables from explicit exclusions and list assumptions that could change the plan.
- Name decision rights: sponsor, project manager, product owner and acceptance authority.
- Review the charter for contradictions, unsupported promises and missing success measures before approval.

**Worked example**

- Need: reduce customer-service response delays during seasonal peaks.
- Objective: release an approved self-service portal pilot by week 12 within SGD 120,000, with named acceptance checks.
- Exclusion: replacement of the existing case-management platform; this prevents silent expansion.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A new project or phase needs shared authority, boundaries and measurable success conditions. | Using a charter as a substitute for detailed requirements, estimates or a delivery plan. |
| Several stakeholders interpret the business need differently and require one approved reference point. | Allowing AI-generated objectives or dates to become commitments before sponsor review. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.pmi.org/-/media/pmi/documents/public/pdf/pmief/skills-for-life-english.pdf

---


### Identify Stakeholders and Plan Engagement

A stakeholder is a person, group or organisation that can affect, be affected by or perceive itself to be affected by the project. Stakeholder planning combines identification, influence and interest analysis, impact, current and desired engagement, information needs, decision rights and an owner for each engagement action.

A generic mailing list treats every stakeholder as if the same information and cadence were useful. Analysis helps the team focus attention where decisions, adoption, resistance or operational impact matter, while avoiding unnecessary personal data.

**How it works**

- Start with roles and legitimate project needs; collect only information necessary for engagement.
- Map influence and interest, then record current versus desired engagement and the evidence for both.
- Choose a strategy—manage closely, keep satisfied, keep informed or monitor—and assign an action owner.
- Review the map at phase gates and when power, impact or sentiment changes.

**Worked example**

- The service director has high influence and owns acceptance; the support agents have high impact and essential workflow knowledge.
- The plan gives the director a fortnightly decision brief and the agents weekly design reviews with visible action tracking.
- AI suggests message variants from role-based needs; the project manager checks tone and factual accuracy.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Planning approvals, requirements discovery, change adoption, communications and escalation routes. | Inferring sensitive traits, private motivations or sentiment without evidence. |
| A project affects multiple functions with different concerns or decision rights. | Treating a power-interest grid as permanent or as a substitute for direct conversation. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.pdpc.gov.sg/guidelines-and-consultation/2020/03/advisory-guidelines-on-key-concepts-in-the-personal-data-protection-act

---


### Plan Scope with Requirements, Deliverables and a WBS

Scope planning converts needs into agreed requirements, deliverables, acceptance criteria and a work breakdown structure. A WBS decomposes the total project scope into manageable work packages; its dictionary explains each package, owner, boundaries and completion evidence. Decomposition describes outcomes before activities.

A schedule or budget built from vague nouns is fragile. The WBS creates a common reference for scope, schedule, cost, risk and responsibility, while acceptance criteria make completion observable. GenAI can find gaps and propose decomposition, but the team must confirm that the WBS covers exactly the approved scope.

**How it works**

- Translate needs into requirements with source, priority, owner and verifiable acceptance criteria.
- Decompose deliverables until a work package can be estimated, assigned, monitored and accepted.
- Apply the 100-percent rule: children collectively represent the parent scope without unrelated work.
- Create a requirements traceability view from need to requirement, deliverable, verification and acceptance.

**Worked example**

- Deliverable 1.0 Portal Pilot decomposes into 1.1 Content, 1.2 Configuration, 1.3 Integration, 1.4 Testing and 1.5 Launch readiness.
- Work package 1.4 has an owner, test environment, entry criteria, exit evidence and explicit exclusions.
- AI critiques the hierarchy for overlap; the team resolves the final boundary.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Building estimates, assigning ownership, controlling changes or defining acceptance. | Creating a task list with no deliverable hierarchy or acceptance evidence. |
| Requirements need traceability across business, technical and operational work. | Accepting AI-created requirements that cannot be traced to an authorised stakeholder or source. |

**Authoritative references**

- https://ntrs.nasa.gov/citations/20200000300
- https://www.gao.gov/products/gao-20-195g

---


### Build a Credible Schedule and Cost Baseline

A credible schedule sequences the complete work, uses realistic durations, links dependencies, identifies resources and shows the critical path and margin. A cost baseline time-phases approved estimates so planned value can later be compared with earned value and actual cost. Both baselines depend on the same WBS.

A list of dates does not show whether the finish is achievable. Network logic reveals which delay matters, while documented estimate assumptions make uncertainty discussable. GenAI may help normalise data or explore scenarios, but it must not invent durations, rates or dependencies.

**How it works**

- Sequence work packages with predecessors and successors; minimise unexplained constraints and open ends.
- Estimate duration and cost from documented quantities, rates, analogous data or expert input; record confidence.
- Calculate the longest dependent path and identify activities with zero or low float.
- Time-phase costs, include authorised contingency where appropriate and obtain baseline approval.

**Worked example**

- Content approval precedes portal configuration; integration test follows both configuration and test-data readiness.
- The critical path runs through content approval, configuration, integration test and acceptance.
- A two-week content delay moves the finish unless the team changes logic, scope or capacity through an approved decision.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Testing whether a target date and budget are realistic and creating a performance reference. | Using fixed target dates as if they were estimates or hiding uncertainty in a single precise number. |
| Analysing the consequence of delay, resource limits or an approved change. | Optimising a schedule generated by AI when its logic and source data have not been checked. |

**Authoritative references**

- https://www.gao.gov/products/gao-16-89g
- https://www.gao.gov/products/gao-20-195g
- https://www.nasa.gov/ocfo/ppc-corner/ppc-guidance-documents/

---


### Integrate Quality, Resources, Communications, Risk and Procurement Plans

The project management plan is an integrated set of baselines and management approaches. Quality planning defines standards, metrics and verification; resource planning defines roles, capacity and responsibility; communications planning matches message to audience and decision; risk planning defines categories, thresholds and response ownership; procurement planning defines make-or-buy, evaluation, contract and supplier controls.

Separate plans can conflict: a compressed schedule may require unavailable specialists; a low-cost supplier may not meet a quality threshold; a reporting cadence may arrive after the decision it supports. Integration checks reveal these trade-offs before execution.

**How it works**

- For each deliverable, link an owner, required capability, quality metric, verification method and acceptance authority.
- Define communication purpose, audience, content, format, cadence, sender and escalation trigger.
- Score threats and opportunities consistently; assign preventive, contingent and fallback actions with owners.
- Document supplier evaluation criteria, lead times, interfaces and approval limits before requesting commitments.

**Worked example**

- The portal needs accessibility review before acceptance; the specialist is available only in week 9.
- The schedule reserves that window, procurement includes the review deliverable and the quality plan names the evidence.
- The risk plan records a trigger and contingency if the specialist becomes unavailable.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Consolidating component plans and checking whether delivery assumptions agree across functions. | Producing isolated documents that do not trace to deliverables, dates, costs and owners. |
| Preparing the project for execution, governance review or supplier engagement. | Asking AI to choose a supplier, staff member or response without approved criteria and human review. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.nist.gov/itl/ai-risk-management-framework
- https://standards.nasa.gov/standard/MSFC/MSFC-HDBK-3684

---


### Lab 1 — Build the AI Working Agreement and Project Charter

Learning outcome: LO1: develop evidence-led project parameters and an authorised charter draft with GenAI.

Goal: Create the control rules and initiation pack that will govern every later lab.

You will open the synthetic BeaconWorks Customer Self-Service Portal brief, define a human-owned GenAI working agreement and turn the approved facts into a project charter. The exercise separates facts, assumptions, options and unknowns so polished language never becomes an unreviewed commitment.

**What you'll build**

01-initiation/ai-working-agreement.md, project-charter.md and source-ledger.csv containing the approved project parameters, human review gates and traceable evidence.   (Tools: Text editor · approved AI assistant · beaconworks-project-brief.md · spreadsheet.)

**Prerequisites**

- Create a local folder named C013-BeaconWorks-Project with 01-initiation through 05-closure subfolders.
- Open labs/assets/beaconworks-project-brief.md and confirm that no real customer or employee data is used.
- Have a spreadsheet application available for the source ledger.

**Step-by-step**

1. In 01-initiation, create source-ledger.csv with columns Record_ID, Claim_or_Parameter, Value, Source_File, Source_Section, Classification, Human_Owner and Status. Add rows for the business need, budget ceiling, target week, sponsor, project manager, pilot deliverable and stated exclusions. Use FACT only when the source brief says it directly; otherwise use ASSUMPTION or UNKNOWN.

   ```bash
   Record_ID,Claim_or_Parameter,Value,Source_File,Source_Section,Classification,Human_Owner,Status
SRC-001,Business need,<VALUE>,beaconworks-project-brief.md,<SECTION>,FACT,Project Manager,Verified
   ```

2. Create ai-working-agreement.md with six headings: Approved uses, Restricted information, Prompt rule, Review gates, Decision authority and Record keeping. Under Prompt rule, write the C-O-S-T-A-R pattern. Under Review gates, require evidence, calculation, confidentiality, bias, authority and record-update checks.

   ```bash
   C-O-S-T-A-R
Context: project and audience
Objective: one observable task
Sources: delimited approved evidence
Tasks: ordered operations
Acceptance criteria: format and quality checks
Review: facts, figures, uncertainty, confidentiality and human authority
   ```

3. Paste only the project brief into the approved AI assistant and request a charter draft with Purpose, Measurable objectives, High-level deliverables, In scope, Out of scope, Milestones, Budget, Assumptions, Constraints, Initial risks, Stakeholders, Authority and Approval readiness. Require a second table that labels each material statement FACT, ASSUMPTION, OPTION or UNKNOWN and cites the brief section.

   ```bash
   Objective: Draft a project charter from <PROJECT BRIEF> only.
Do not invent dates, people, figures or requirements. Use UNKNOWN when absent.
Return: charter headings + Statement | Classification | Source section | Review needed.
Before finishing, list contradictions and missing approval information.
   ```

4. Save the response as project-charter-ai-draft.md. Review every objective and parameter against the brief and source ledger. Edit the human-approved version into project-charter.md. Each objective must contain a result, measure, target and time horizon. Move unsupported material to Assumptions or Open questions; never repair a gap by inventing evidence.

   ```bash
   Objective quality check: result + measure + target + time horizon
Parameter quality check: source row + classification + owner + status
Final labels: FACT | ASSUMPTION | OPTION | UNKNOWN
   ```

5. Add a Charter readiness checklist to project-charter.md. Mark each item READY or ACTION: business need, objectives, boundaries, deliverables, budget, milestone horizon, authority, initial risks and open questions. Record the project manager as document owner and the synthetic sponsor as approval owner. Do not mark the charter approved; mark it Ready for sponsor review.

   ```bash
   Readiness item | Status | Evidence or action | Owner | Due
Final document status: Ready for sponsor review
   ```


**Test it**

The working agreement must contain all six headings and the six-part C-O-S-T-A-R pattern. The charter must contain all 13 requested sections, at least three measurable objectives, an explicit out-of-scope statement, a named document owner and approval owner, plus the status Ready for sponsor review. The source ledger must contain at least seven rows; every material figure and date in the charter must trace to a verified FACT row or be labelled ASSUMPTION or UNKNOWN.

**Checkpoint and rejoin point**

Keep the three initiation files. Lab 2 uses the charter boundaries and source ledger. To rejoin, copy the approved course checkpoint from labs/assets/checkpoint-01-initiation.md and mark its assumptions Pending validation.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The assistant adds a launch date or benefit target not present in the brief. | Delete it from the approved charter, add it to Open questions and repeat the prompt with 'Use UNKNOWN when absent.' |
| The objective sounds positive but cannot be checked. | Add a measure, target and time horizon while preserving the business intent in the source. |
| A fact has no clear source section. | Classify it as ASSUMPTION or UNKNOWN until a direct source can be cited. |

**Challenge**

Ask the assistant to critique the final charter as sponsor, operations owner and delivery lead. Keep only questions that expose a real gap, cite the role that raised each one and do not let the critique alter the charter.

**Reflection**

Which charter sentence was most improved by separating fact from assumption, and what decision risk did that prevent?

> **Note:** The complete lab and its support-file references are in labs/lab-01-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


### Lab 2 — Build the Stakeholder Engagement and Communications Plan

Learning outcome: LO1: identify stakeholders and plan evidence-led engagement and communications.

Goal: Create a role-based stakeholder strategy with explicit decisions, messages, owners and review triggers.

You will combine the approved charter with the supplied stakeholder inputs. GenAI will help structure and challenge the plan, while you make the final influence, interest, impact and engagement decisions from evidence. The resulting communication matrix starts with the action or decision each audience needs.

**What you'll build**

02-planning/stakeholder-register.csv and stakeholder-communications-plan.md with eight stakeholder rows, current and desired engagement, owned actions, decision-focused communications and privacy safeguards.   (Tools: Spreadsheet · text editor · approved AI assistant · stakeholder-inputs.csv · Lab 1 charter.)

**Prerequisites**

- Completed project-charter.md and source-ledger.csv from Lab 1, or the stated rejoin checkpoint.
- Open labs/assets/stakeholder-inputs.csv and read the Data_boundary column before prompting.
- Use roles and supplied project evidence; do not add private opinions or sensitive traits.

**Step-by-step**

1. Copy stakeholder-inputs.csv to 02-planning/stakeholder-register.csv. Add columns Influence_1_5, Interest_1_5, Project_Impact_1_5, Current_Engagement, Desired_Engagement, Strategy, Action, Action_Owner, Review_Trigger and Evidence. Preserve Stakeholder_ID and use role names rather than personal details.

   ```bash
   Allowed engagement states: Unaware | Resistant | Neutral | Supportive | Leading
Allowed strategies: Manage closely | Keep satisfied | Keep informed | Monitor
   ```

2. Paste only the charter and permitted stakeholder rows into the assistant. Ask for proposed scores and engagement states with a short evidence citation. Require UNKNOWN when a rating cannot be supported. Enter the suggestions in temporary Proposed_* columns; do not copy them directly into final columns.

   ```bash
   For each Stakeholder_ID return Proposed influence, interest, impact, current state and desired state.
Cite only supplied evidence. Do not infer personality, demographic, political or sensitive traits.
Use UNKNOWN when evidence is absent and list one question to validate it.
   ```

3. Review each proposal. Enter final 1–5 scores and states, then choose a strategy and one observable engagement action. Add an action owner and review trigger. If your final value differs from the proposal, record the reason in Evidence. Check that high-impact affected users receive dialogue, not only broadcast.

   ```bash
   Human review gate: evidence present · impact considered · strategy proportional · owner named · trigger observable
   ```

4. Create stakeholder-communications-plan.md with a table containing Communication_ID, Audience_IDs, Purpose_or_Decision, Verified_Input, Message_Outline, Format, Channel, Cadence_or_Trigger, Sender, Feedback_Method, Record_Location and Escalation. Include a sponsor decision brief, delivery-team coordination, support-agent design review, supplier interface and launch-readiness update.

   ```bash
   Start with: What must this audience understand, decide or do?
Then specify: evidence → message → channel → feedback → record → escalation
   ```

5. Ask the assistant to produce a 120-word sponsor version and a 120-word support-agent version of the same scope-boundary update. Compare both with the charter. Save the two drafts under Audience transformation example, correct any unsupported detail and add a note explaining what changed and what stayed invariant.

   ```bash
   Use only <VERIFIED CHARTER EXTRACT>.
Draft A for sponsor: decision, tolerance, recommendation and ask.
Draft B for support agents: workflow impact, participation, timing and feedback route.
Keep facts, uncertainty and boundary identical in both.
   ```


**Test it**

The register must contain exactly eight supplied Stakeholder_ID rows and no added personal data. Every row must have final influence, interest and impact scores; current and desired states; a strategy; an owned action; a review trigger; and evidence or UNKNOWN. The communications plan must contain at least five records and all 12 columns. The two audience drafts must preserve identical project facts and include different purpose-appropriate asks.

**Checkpoint and rejoin point**

Keep both planning files. Lab 3 uses the acceptance owner, specialist availability, supplier interface and communication triggers. To rejoin, use stakeholder-inputs.csv and the final-value rules printed in this lab.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Every stakeholder is rated high influence and high interest. | Compare decision authority, ability to affect the work and need for detail; use the supplied anchors and evidence independently. |
| The plan contains generic actions such as 'communicate regularly'. | Name the purpose, artifact, owner, cadence or trigger and required feedback or decision. |
| The assistant infers attitude or motivation. | Delete the inference, use UNKNOWN and create a respectful validation question or engagement action. |

**Challenge**

Create a second communication route for the highest-impact stakeholder if the normal channel is unavailable. State when the alternate route activates and how the official decision record remains singular.

**Reflection**

Which stakeholder needed the largest shift from current to desired engagement, and what evidence-led action could create that shift?

> **Note:** The complete lab and its support-file references are in labs/lab-02-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


### Lab 3 — Build the Integrated Project Management Plan

Learning outcome: LO1: develop an integrated scope, schedule, cost, quality, resource, communication, risk and procurement plan.

Goal: Turn the authorised project parameters into one coherent baseline and management plan.

You will use the charter, stakeholder plan and supplied work-package inputs to create a WBS-aligned baseline. You will calculate the network and budget yourself, then use GenAI to critique integration gaps across quality, resources, communications, risks and procurement.

**What you'll build**

02-planning/wbs-and-baseline.csv, integrated-management-plan.md, initial-risk-register.csv and procurement-evaluation-plan.csv with a verified 28-working-day critical path and SGD 120,000 authorised budget.   (Tools: Spreadsheet · text editor · approved AI assistant · planning-inputs.csv · risk-issue-inputs.csv.)

**Prerequisites**

- Completed charter, source ledger, stakeholder register and communications plan from Labs 1–2.
- Open labs/assets/planning-inputs.csv and labs/assets/risk-issue-inputs.csv.
- Know that the approved budget ceiling is SGD 120,000, including SGD 15,000 contingency.

**Step-by-step**

1. (20 minutes) Copy planning-inputs.csv to 02-planning/wbs-and-baseline.csv. Verify that the ten work packages cover the Portal Pilot deliverable and that exclusions in the charter are absent. Add columns Earliest_Start, Earliest_Finish, Latest_Start, Latest_Finish, Total_Float, Critical, Acceptance_Evidence and Human_Reviewer. Do not change supplied durations, predecessors or costs during the first calculation.

   ```bash
   WBS check: complete approved scope · no excluded scope · one owner · one acceptance criterion per work package
Day-zero convention: a work package with no predecessor has ES = 0; EF = ES + Duration.
Forward pass: ES = maximum predecessor EF; EF = ES + Duration.
   ```

2. (25 minutes) Complete the forward pass, then calculate the backward pass from a project finish of day 28. For terminal work packages set LF = 28 and LS = LF minus Duration. For every predecessor, set LF to the minimum LS of its successors and LS = LF minus Duration. Calculate Total_Float = LS minus ES and mark Critical = YES only when Total_Float = 0. Sum Work_Budget_SGD, add the approved contingency and compare with the charter ceiling. Record the expected baseline summary in integrated-management-plan.md. If your result is not 28 working days and SGD 105,000 work budget plus SGD 15,000 contingency, find the dependency or arithmetic error before continuing.

   ```bash
   Expected work budget = SGD 105,000
Contingency = SGD 15,000
Authorised total = SGD 120,000
Expected critical path = WP-01 -> WP-03 -> WP-04 -> WP-07 -> WP-08 -> WP-10
Expected critical path duration = 28 working days
Backward pass: terminal LF = 28; predecessor LF = minimum successor LS; Total_Float = LS - ES
   ```

3. (20 minutes) Create integrated-management-plan.md with sections Scope, Schedule, Cost, Quality, Resources, Communications, Risk, Procurement, Change, Baseline governance and Source register. For each section state the objective, method, owner, evidence, threshold or trigger and controlled record. Link the specialist availability, supplier interface and acceptance owner from Lab 2.

   ```bash
   Component plan pattern:
Objective | Method | Owner | Evidence | Threshold/trigger | Controlled record
Integration check: every work package has scope + date + cost + resource + quality evidence
   ```

4. (15 minutes) Copy the five RISK rows from risk-issue-inputs.csv to initial-risk-register.csv. Add Probability_1_5, Impact_1_5, Exposure, Strategy, Preventive_Action, Trigger, Contingency, Owner and Residual_Exposure. Ask the assistant to critique cause–event–effect structure and missing response fields; make the final scores and owners yourself.

   ```bash
   Risk statement: Because <cause>, <uncertain event> may occur, leading to <effect on objective>.
Exposure = Probability × Impact
Do not convert a current issue into a future risk.
   ```

5. (10 minutes) Create procurement-evaluation-plan.csv for the accessibility review with criteria Capability 25, Method and evidence 25, Lead time 20, Data handling 15 and Cost 15. Write 1–5 scoring anchors before viewing any offer. Ask the assistant to inspect the four planning files for contradictions and return Issue, Evidence, Consequence and Repair. Resolve every high-consequence contradiction or record an owned open action.

   ```bash
   Criterion,Weight_Percent,Score_1_Anchor,Score_3_Anchor,Score_5_Anchor,Decision_Owner
Capability,25,<MINIMUM>,<ADEQUATE>,<STRONG>,Procurement Lead
Weights must total 100.
   ```


**Test it**

The baseline must contain ten contiguous work packages, total SGD 105,000 before contingency and show the zero-float path WP-01 -> WP-03 -> WP-04 -> WP-07 -> WP-08 -> WP-10 at 28 working days. Every row must have ES, EF, LS, LF and Total_Float calculated with the stated day-zero convention. The integrated plan must contain all 11 sections and link every work package to an owner, resource role, cost, quality or acceptance evidence and communication or control record. The risk register must contain five cause–event–effect rows with scored exposure, action, trigger, contingency and owner. Procurement criteria weights must total 100 and include written 1, 3 and 5 scoring anchors.

**Checkpoint and rejoin point**

Freeze the four files as Baseline v1.0 and add the status 'Ready for sponsor baseline review'. Labs 4–9 use these records. To rejoin, copy the supplied planning inputs and reproduce the expected 28-day and SGD 120,000 checks.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The schedule finishes earlier than 28 working days. | Check that each activity starts after the maximum finish of all predecessors, not the first predecessor listed. |
| The work budget does not equal SGD 105,000. | Sum each unique work-package row once and keep contingency outside the work-package total. |
| The AI critique recommends changing the baseline. | Treat the output as an issue list; make changes only after checking source evidence and recording the human decision. |

**Challenge**

Model a scenario in which content approval takes two extra days. Recalculate the finish, identify the affected critical path and propose two recovery options without changing the frozen Baseline v1.0.

**Reflection**

Which dependency created the strongest connection among scope, schedule, cost, resources, quality and risk?

> **Note:** The complete lab and its support-file references are in labs/lab-03-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


## Topic 02 — Project Execution and Delivery with GenAI  (Day 2 morning · 3 connected labs)

direct and manage work · knowledge and decisions · team and resources · quality · communications · stakeholder engagement · evidence-led status

**Key concepts**

- Work authorisation — Translate the plan into owned work packages with inputs, constraints and completion evidence.
- Team coordination — Make responsibility, capacity, hand-offs, impediments and escalation routes visible.
- Knowledge flow — Capture decisions, rationale, assumptions and lessons where the team can reuse them.
- Quality at source — Prevent defects with clear criteria and peer checks instead of relying on late inspection.
- Purposeful communication — Design each update around the decision or action the audience needs.
- Evidence-led reporting — Separate facts, forecasts, decisions, risks and asks; never let narrative outrun the data.


### Direct and Manage Project Work

Directing and managing work means authorising planned work packages, coordinating execution, producing deliverables, handling issues and implementing approved changes. The plan guides action, while actual results and work-performance data feed monitoring and decisions.

Execution fails when tasks are launched without clear outcomes, prerequisites or completion evidence. A work package brief creates a bounded commitment and lets AI assist with sequencing, checklists and communication without redefining the approved scope.

**How it works**

- Confirm the work package objective, owner, inputs, constraints, dependencies, due date and done criteria.
- Authorise only work that is ready; make blockers and required decisions visible.
- Update actual start, progress evidence, forecast finish, actual cost and issues at an agreed cadence.
- Route any proposed baseline change through the change-control process before implementation.

**Worked example**

- The configuration package starts only after content approval and environment access are confirmed.
- The owner records evidence links and a forecast, not an unsupported percent-complete guess.
- A new reporting feature is logged as a change request rather than inserted into active work.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Converting an approved plan into short, owned units of delivery and coordinating dependencies. | Starting work from an AI-generated list that has not been reconciled to the WBS and baseline. |
| Clarifying what can start, what is blocked and what evidence demonstrates completion. | Treating activity volume or polished status text as proof of deliverable progress. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://standards.nasa.gov/standard/MSFC/MSFC-HDBK-3684

---


### Manage Project Knowledge and Decisions

Project knowledge includes explicit records—plans, decisions, designs and lessons—and tacit experience held by people. Knowledge management makes both usable through structured capture, context, ownership, retrieval and conversation. A decision log records the decision, options, evidence, rationale, owner, date and review trigger.

Meeting summaries without decisions and owners create the illusion of documentation. GenAI can extract candidate actions and themes, but source notes and participant confirmation are needed because a plausible summary can omit a condition or assign the wrong owner.

**How it works**

- Capture source notes first; ask AI to separate decisions, actions, questions, assumptions and risks.
- Confirm candidate records with the decision owner and participants before publishing.
- Link each decision to affected requirements, work packages, risks and changes.
- Record lessons during delivery with context and evidence, not only at closure.

**Worked example**

- A design review chooses option B because it meets accessibility and lead-time constraints.
- The log retains rejected options, evidence, decision owner and a review trigger if the supplier date changes.
- The AI summary is corrected against the meeting notes before the action register is updated.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Synthesising meetings, comparing options, onboarding team members or preserving rationale. | Recording confidential discussion in an unapproved service or treating an AI summary as the official record. |
| A project contains hand-offs, repeated decisions or knowledge that could be lost when people change. | Capturing lessons as generic advice with no context, consequence or evidence. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices

---


### Acquire Resources and Manage the Team

Resource management matches required capability and capacity to scheduled work, then supports people to deliver together. A responsibility view clarifies who is accountable, responsible, consulted and informed; a capacity view compares demand with realistic availability; a team working agreement defines collaboration, escalation and decision norms.

A plan can look feasible while over-allocating the same specialist or ignoring operational duties. GenAI can highlight conflicts and draft coaching questions, but staffing, performance and conflict decisions require context, fairness and accountable human judgement.

**How it works**

- Map each work package to required capability, named owner, effort window and availability.
- Resolve over-allocation by changing sequence, scope, capacity or date through authorised decisions.
- Use short coordination cycles to surface impediments, hand-offs and support needs.
- Address conflict through facts, interests, options and agreed action; do not infer personality or intent.

**Worked example**

- The same accessibility specialist is needed by content and test work in week 9.
- The team sequences the reviews and protects the critical-path activity rather than assuming parallel capacity.
- The resource plan records the change and the stakeholder update explains the trade-off.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Planning or rebalancing capacity, clarifying responsibility and coordinating cross-functional work. | Using AI to rank people, infer sensitive characteristics or make employment decisions. |
| A delivery delay may be caused by demand, skill or dependency rather than individual effort. | Treating availability as 100 percent of working time or ignoring operational responsibilities. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.nist.gov/itl/ai-risk-management-framework

---


### Manage Quality and Deliverable Acceptance

Managing quality turns the quality plan into preventive practices, peer review, process checks, defect learning and improvement. Quality control checks deliverable results against criteria; scope validation obtains formal acceptance from the authorised stakeholder. These are related but distinct: a deliverable may meet an internal check yet still need customer acceptance.

Late inspection makes defects expensive and encourages subjective debate. Clear criteria and evidence let the team build quality into the work. GenAI can create checklists and classify defects from approved records, but the criteria and acceptance decision remain human-owned.

**How it works**

- Translate each requirement into measurable acceptance criteria and a verification method.
- Use prevention, peer review and sampling during work; record defects with cause and corrective action.
- Present the deliverable, evidence and known limitations to the authorised acceptance owner.
- Capture accepted, conditionally accepted and rejected outcomes with actions and dates.

**Worked example**

- The portal content must meet the agreed reading level, link integrity and accessibility checks.
- A peer review catches missing alternative text before the acceptance demonstration.
- The service director accepts the pilot after the evidence pack and two minor actions are recorded.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Defining done, preventing rework, preparing a review or obtaining deliverable acceptance. | Using an AI score as the sole evidence of quality or silently changing criteria after delivery. |
| A quality dispute needs objective criteria, evidence and a named decision owner. | Confusing completion of internal work with formal acceptance of the deliverable. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.nist.gov/itl/ai-risk-management-framework

---


### Manage Communications and Stakeholder Engagement

Communication management creates, distributes, stores and retrieves project information for a defined purpose. Stakeholder engagement uses that information plus dialogue, participation and relationship actions to support decisions and adoption. Effective communication is measured by understanding and action, not by the volume of messages sent.

The same status dump does not serve a sponsor, delivery team and affected user. GenAI is helpful for transforming one verified evidence set into audience-specific drafts, provided that facts, uncertainty, tone and calls to action are checked before release.

**How it works**

- Start with the audience decision or action; include only the evidence needed for it.
- Separate completed facts, current forecast, variance, risks, decisions and asks.
- Choose channel and cadence based on urgency, sensitivity, complexity and need for dialogue.
- Confirm understanding, record decisions and update the engagement plan from observed response.

**Worked example**

- The team receives a detailed blocker-and-owner view; the sponsor receives trend, tolerance, decision and recommendation.
- Both versions use the same approved weekly data and preserve the same red status.
- The project manager removes unsupported certainty from the AI draft before distribution.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Preparing status updates, decision briefs, change communications or adoption conversations. | Using AI to manufacture positive sentiment, conceal bad news or impersonate a stakeholder. |
| Several audiences need different levels of detail from the same verified source. | Sending generated text without checking names, figures, commitments and confidentiality. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://openai.com/academy/writing/

---


### Build Evidence-Led Status and Forecast Reporting

Evidence-led reporting reconciles approved baselines, a common status date and verified work, cost, quality, resource, risk, issue and decision records before drafting a message. Earned value uses planned value (PV), earned value (EV) and actual cost (AC) at the same cut-off: schedule variance SV = EV − PV, cost variance CV = EV − AC, SPI = EV ÷ PV and CPI = EV ÷ AC. Forecasts remain assumptions until their method, remaining-work estimate and owner are explicit.

A polished status narrative can hide inconsistent dates, double-counted progress or unsupported optimism. A reconciled evidence table makes calculations reproducible and separates completed fact, current variance, forecast, risk, decision and ask. GenAI may transform the verified table for different audiences, but it must not calculate from mixed cut-offs or replace the project manager’s judgement.

**How it works**

- Freeze one status date and reconcile baseline, completion evidence, actual cost, remaining duration, defects, capacity, risks, issues and decisions.
- Calculate PV, EV and AC from approved records; derive SV, CV, SPI and CPI and show units, formulas and rounding.
- Forecast EAC from an explicit assumption—for example BAC ÷ CPI when current cost efficiency is expected to continue—and record ETC and VAC.
- Draft team and sponsor views from the same evidence table; keep status, variance and uncertainty identical while changing detail, decision and ask.

**Worked example**

- At week 8, PV is SGD 72,000, EV is SGD 60,000, AC is SGD 66,000 and BAC is SGD 105,000.
- SV is −SGD 12,000, CV is −SGD 6,000, SPI is 0.83 and CPI is 0.91; if CPI continues, EAC is SGD 115,500.
- The status remains red in both audience versions; the sponsor brief adds the decision needed while the team view adds owners and next-cycle evidence.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Preparing a weekly status pack, variance analysis, estimate at completion, recovery recommendation or decision brief. | Calculating earned value from unapproved scope, mixed status dates or progress percentages that lack completion evidence. |
| Different audiences need a consistent view of progress, cost, forecast, risk and action from one verified cut-off. | Using AI narrative confidence to hide an adverse variance, omit uncertainty or make a forecast appear authorised. |

**Authoritative references**

- https://www.gao.gov/products/gao-20-195g
- https://www.gao.gov/products/gao-16-89g
- https://www.pmi.org/standards/process-groups

---


### Lab 4 — Turn the Baseline into an Executable Delivery System

Learning outcome: LO2: direct and manage project work with owned work packages, dependencies and completion evidence.

Goal: Create a ready-to-run delivery board and authorise one bounded work package.

You will transform the frozen Baseline v1.0 into a delivery board without changing its scope or dates. The exercise distinguishes planned, ready, active, blocked and done work, then creates a detailed brief for portal configuration with prerequisites, acceptance evidence and escalation rules.

**What you'll build**

03-delivery/delivery-board.csv, work-package-brief-WP-04.md and decision-log.csv that translate the baseline into controlled execution records.   (Tools: Spreadsheet · text editor · approved AI assistant · Lab 3 baseline · delivery-events.md.)

**Prerequisites**

- Frozen wbs-and-baseline.csv and integrated-management-plan.md from Lab 3.
- Open labs/assets/delivery-events.md and read Events E01–E03 only.
- Do not implement or approve a baseline change in this lab.

**Step-by-step**

1. Copy the ten work-package rows from wbs-and-baseline.csv into 03-delivery/delivery-board.csv. Add Status, Readiness_Evidence, Actual_Start, Actual_Finish, Forecast_Finish, Percent_Complete_Method, Progress_Evidence, Blocker, Next_Action, Action_Owner and Escalation_Date. Set Status to Planned until the predecessor, input, owner and environment checks are supported.

   ```bash
   Allowed status: Planned | Ready | Active | Blocked | Done
Readiness gate: predecessor complete · approved input available · owner confirmed · environment available
   ```

2. Use delivery event E01 to update WP-01 through WP-03. Mark only work supported by the event as Done, Active or Ready and link its evidence label. For active work, define progress by completed acceptance items or verified sub-deliverables; do not enter a subjective percentage.

   ```bash
   Progress evidence examples: approved requirements record · accepted content batch · reviewed design artifact
Rule: activity or effort alone is not deliverable progress.
   ```

3. Create work-package-brief-WP-04.md for Portal configuration with Objective, Scope boundary, Inputs, Predecessors, Owner, Contributors, Start gate, Planned duration, Cost budget, Quality checks, Acceptance evidence, Risks, Communication, Done criteria and Escalation. Ask the assistant for a draft using only the baseline and E01, then reconcile every field to those records.

   ```bash
   Draft a bounded WP-04 brief from <BASELINE ROW> and <EVENT E01> only.
Use UNKNOWN for missing data. Do not add features or change dates.
Finish with Source field | Used value | Evidence | Human check.
   ```

4. Create decision-log.csv with columns Decision_ID, Date, Question, Options, Evidence, Decision, Rationale, Decision_Owner, Affected_Records, Review_Trigger and Status. Record the E02 environment-access decision as Pending decision. Ask the assistant to produce three options, then remove any option that violates the charter or baseline and record the human-approved recommendation separately.

   ```bash
   Decision analysis: Option | Benefits | Drawbacks | Scope impact | Schedule impact | Cost impact | Risk | Evidence
Status remains Pending decision until the named owner confirms it.
   ```

5. Apply event E03 to the board. If the event is an unapproved feature request, add Blocker or Next_Action as Log change request and leave baseline fields unchanged. Run a trace check from each active row to WBS, owner, predecessor, cost, quality evidence and communication record.

   ```bash
   Trace check result per active row: WBS PASS/REPAIR · Owner PASS/REPAIR · Logic PASS/REPAIR · Cost PASS/REPAIR · Evidence PASS/REPAIR · Communication PASS/REPAIR
   ```


**Test it**

The board must contain the same ten work packages, baseline durations and costs as Baseline v1.0. Every Ready or Active row must have readiness evidence, owner, next action and objective progress evidence. The WP-04 brief must contain all 15 requested sections and no added scope. The decision log must contain E02 as Pending decision with at least two viable options, and E03 must be routed to a change request without editing the baseline.

**Checkpoint and rejoin point**

Keep all three delivery records. Lab 5 adds team, knowledge and quality controls; Lab 6 uses the board as the status source. To rejoin, copy Baseline v1.0 and apply only delivery events E01–E03.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Several rows appear ready even though a predecessor is incomplete. | Apply the readiness gate row by row and return unsupported work to Planned. |
| Percent complete is a confident number without evidence. | Replace it with completed acceptance items, verified quantities or a forecast based on remaining work. |
| The feature request appears inside WP-04. | Remove it, log a change request and preserve the original work-package boundary. |

**Challenge**

Create a filtered view showing only work that can start in the next five working days. Explain the exact readiness evidence for each selected row and why every excluded row is not yet ready.

**Reflection**

Which field most clearly separated an authorised work package from a plausible AI-generated task list?

> **Note:** The complete lab and its support-file references are in labs/lab-04-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


### Lab 5 — Manage Team Knowledge, Quality and Stakeholder Delivery

Learning outcome: LO2: resolve delivery challenges through explicit capacity, knowledge, quality and engagement controls.

Goal: Turn live delivery events into owned team actions, verified quality records and confirmed project knowledge.

You will process synthetic capacity, meeting and defect evidence without inferring people’s intent. GenAI will extract candidate decisions and actions, while you confirm them against the source and update the resource, decision, quality and stakeholder records.

**What you'll build**

03-delivery/resource-and-raci-plan.csv, quality-and-acceptance-log.csv, meeting-record-ai-draft.md, meeting-record.md, stakeholder-engagement-update.md and delivery-handoff-checklist.md with confirmed owners and evidence.   (Tools: Spreadsheet · text editor · approved AI assistant · delivery-events.md · Lab 2–4 records.)

**Prerequisites**

- Delivery board and decision log from Lab 4.
- Stakeholder register and communications plan from Lab 2.
- Open delivery-events.md and use Events E04–E07 only.
- Use the five preformatted Lab 5 starter files in labs/assets so the 45-minute exercise focuses on evidence and decisions.

**Step-by-step**

1. (8 minutes) Copy lab-05-resource-raci-starter.csv to 03-delivery/resource-and-raci-plan.csv. Keep one row per Resource_Role; list every related work package in Affected_Work_Packages. Complete Responsible, Accountable, Consulted, Informed, Capability_Needed, Planned_Effort_Days, Available_Effort_Days, Variance_Days, Conflict, Resolution_Option and Human_Decision. Enter the supplied capacity values from E04 and calculate Variance_Days as available minus planned. Mark negative values as conflicts.

   ```bash
   Variance_Days = Available_Effort_Days - Planned_Effort_Days
Conflict = YES when Variance_Days < 0
Resolution options: resequence · reduce approved scope via change · add authorised capacity · change date
   ```

2. (10 minutes) Copy lab-05-meeting-record-starter.md to 03-delivery/meeting-record-ai-draft.md. Paste meeting note E05 into the assistant and request candidate Decisions, Actions, Questions, Assumptions, Risks and Lessons with exact source quotations of no more than 12 words. Save the response in that draft file, compare each item with E05, then save the corrected human-reviewed version as 03-delivery/meeting-record.md with Confirmed or Pending confirmation status.

   ```bash
   Extract only what the note supports.
Return Type | Candidate record | Owner | Date | Evidence excerpt | Confirmation needed.
Do not infer agreement, sentiment or an owner not named in the note.
   ```

3. (10 minutes) Add confirmed decisions to decision-log.csv. Copy lab-05-quality-acceptance-starter.csv to 03-delivery/quality-and-acceptance-log.csv with Deliverable_ID, Requirement_ID, Criterion, Verification_Method, Result, Evidence, Defect_ID, Severity, Corrective_Action, Action_Owner, Due and Acceptance_Status. Enter E06 and E07 exactly; keep quality result separate from stakeholder acceptance.

   ```bash
   Quality result: Meets | Does not meet | Not checked
Acceptance status: Pending | Accepted | Accepted with actions | Not accepted
A completed internal check does not equal stakeholder acceptance.
   ```

4. (8 minutes) Copy lab-05-stakeholder-engagement-update-starter.md to 03-delivery/stakeholder-engagement-update.md. Compare the support agents’ current and desired state with the evidence in E05–E07. Record Observation, Evidence, Consequence, Updated action, Owner, Trigger and Feedback method. Do not label attitude; describe observable participation, questions, delays or decisions.

   ```bash
   Acceptable observation: 'Three workflow questions remain open after the review.'
Not acceptable: 'The team is resistant.' unless direct, appropriate evidence and context support it.
   ```

5. (9 minutes) Ask the assistant to critique the four outputs for contradictions in owner, date, status and evidence. Resolve each contradiction against the source event. Copy lab-05-delivery-handoff-checklist-starter.md to 03-delivery/delivery-handoff-checklist.md and complete its seven rows: capacity, decision, action, defect, acceptance, stakeholder update and controlled-record link.

   ```bash
   Contradiction table: Field | File A | File B | Source evidence | Human resolution | Updated files
Handoff result: seven items each marked READY or ACTION with owner and due date.
   ```


**Test it**

The resource plan must use one row per resource role and show these E04 results: Accessibility Specialist -2/YES, Integration Engineer 0/NO, Content Lead -2/YES and Support Lead +1/NO for Variance_Days/Conflict. The meeting record must classify at least one decision, action, question, assumption, risk and lesson, each with evidence and confirmation status. The quality log must keep verification result separate from acceptance status and include owners for all corrective actions. The engagement update must use observable evidence and the handoff checklist must be saved as 03-delivery/delivery-handoff-checklist.md and contain all seven required items.

**Checkpoint and rejoin point**

Keep the corrected delivery records. Lab 6 uses confirmed decisions, defects, capacity conflicts and actions in the weekly status pack. To rejoin, reprocess E04–E07 and mark uncertain extraction Pending confirmation.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| RACI has more than one accountable role for a work package. | Escalate the ambiguity and name one final accountable decision owner in Human_Decision. |
| The summary assigns an action to someone not named in the note. | Set Owner to UNASSIGNED and add a Pending confirmation action. |
| A deliverable is marked accepted after an internal check. | Change Acceptance_Status to Pending until the authorised stakeholder records acceptance. |

**Challenge**

Propose a resource resolution that protects the 28-day baseline, then state the cost, quality, coordination and risk assumptions that would need approval before it could be used.

**Reflection**

Which source check prevented the largest error in the meeting, resource or quality record?

> **Note:** The complete lab and its support-file references are in labs/lab-05-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


### Lab 6 — Build the Evidence-Led Project Status Pack

Learning outcome: LO2: communicate project delivery status and budget challenges from verified work-performance evidence.

Goal: Calculate project performance and produce audience-specific updates that preserve one version of the facts.

You will reconcile the baseline, delivery board and supplied week-8 update. You will calculate schedule and cost indicators in the spreadsheet before asking GenAI to draft narrative. The final pack distinguishes fact, forecast, risk, decision and ask for both sponsor and team audiences.

**What you'll build**

03-delivery/week-08-performance.csv and week-08-status-pack.md containing transparent calculations, source links, a sponsor decision brief and a delivery-team action view.   (Tools: Spreadsheet · text editor · approved AI assistant · weekly-update-inputs.md · Lab 3–5 records.)

**Prerequisites**

- Frozen Baseline v1.0, current delivery board, decision log, quality log and resource plan.
- Open labs/assets/weekly-update-inputs.md and use the stated week-8 cut-off only.
- Use the work budget BAC of SGD 105,000; keep contingency outside earned-value calculations.

**Step-by-step**

1. Create week-08-performance.csv with Metric, Formula, Input_A, Input_B, Result, Unit, Source and Human_Check. Enter PV 72000, EV 60000, AC 66000 and BAC 105000 from the supplied update. Calculate SV, CV, SPI, CPI, EAC using BAC/CPI, ETC using EAC-AC and VAC using BAC-EAC. Round ratios to two decimals and currency to the nearest dollar.

   ```bash
   SV = EV - PV
CV = EV - AC
SPI = EV / PV
CPI = EV / AC
EAC = BAC / CPI
ETC = EAC - AC
VAC = BAC - EAC
   ```

2. Reconcile supplied milestone, defect, capacity, risk, issue and decision information with the current project records. In week-08-status-pack.md create an Evidence table with Evidence_ID, Status_Date, Fact, Source, Owner and Confidence. Record contradictions as Open data issue rather than choosing the more favourable value.

   ```bash
   One status date: Week 8 Friday 17:00
Evidence classes: COMPLETED FACT | CURRENT CONDITION | FORECAST | RISK | ISSUE | DECISION | ASK
   ```

3. Before using AI, write the overall status from the agreed thresholds: Red if SPI or CPI is below 0.90, or an approved milestone is forecast to breach by more than three working days without an authorised recovery; Amber for an emerging tolerance threat; Green only when within tolerance. State the threshold and evidence used.

   ```bash
   Expected calculations: SPI 0.83 · CPI 0.91 · EAC SGD 115,500 · VAC -SGD 10,500
Expected schedule forecast: 32 working days versus 28-day baseline
   ```

4. Give the assistant only the verified Evidence table and performance rows. Request two drafts: a sponsor brief with Outcome, Trend, Tolerance, Cause, Consequence, Options, Recommendation and Decision needed; and a team view with completed work, blocked work, next actions, owners and dates. Require the same status, figures and forecast in both.

   ```bash
   Use only <VERIFIED STATUS DATA>.
Do not soften Red, change a figure or invent a cause.
Draft A: sponsor decision brief, 180 words maximum.
Draft B: team action view, table format.
Finish with Claim | Evidence_ID | Classification.
   ```

5. Review every generated claim against the evidence and save the corrected versions. Add a Decision request that names the owner, latest decision date, options, recommendation and consequence of no decision. Add a next-cycle data checklist for progress evidence, actual cost, remaining duration, defects, capacity, risks, issues, supplier status and stakeholder feedback.

   ```bash
   Decision request: owner · decision · due · options · recommendation · no-decision consequence
Next-cycle checklist: nine evidence categories each with source owner and cut-off time
   ```


**Test it**

The spreadsheet must show SV -SGD 12,000, CV -SGD 6,000, SPI 0.83, CPI 0.91, EAC SGD 115,500, ETC SGD 49,500 and VAC -SGD 10,500. The pack must show a 32-day forecast against the 28-day baseline, apply the stated status threshold consistently, contain source IDs for every material claim, preserve identical facts across sponsor and team views, and include a complete decision request plus nine-item next-cycle checklist.

**Checkpoint and rejoin point**

Freeze the verified week-8 calculations and evidence table. Lab 7 uses the status risks and supplier data; Lab 8 uses the forecast and decision structure. To rejoin, reproduce the expected calculations before drafting narrative.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| EAC is calculated from the authorised total including contingency. | Use the SGD 105,000 work budget BAC for earned value and show contingency separately. |
| The AI draft changes Red to Amber. | Restore Red from the agreed rule and tell the assistant that status is a fixed input, not a writing choice. |
| Two files report different actual cost. | Record an Open data issue, name the source owner and do not publish a resolved figure until reconciled. |

**Challenge**

Calculate an alternative EAC using AC + (BAC-EV) and explain which performance assumption differs from BAC/CPI. Do not replace the official forecast without an authorised decision.

**Reflection**

Which part of the status pack required the most human judgement after the calculations were fixed?

> **Note:** The complete lab and its support-file references are in labs/lab-06-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


## Topic 03 — Manage Project Risks with GenAI  (Day 2 afternoon · 3 connected labs)

risk and issue response · procurement · monitor and control work · integrated change · scope, schedule, cost, quality, resources, communications, stakeholders and closure

**Key concepts**

- Risk response — Turn priority uncertainty into preventive action, triggers, contingencies, owners and residual exposure.
- Integrated control — Compare actual and forecast performance with approved baselines and explain the cause and consequence.
- Change control — Evaluate a proposed change across value, scope, schedule, cost, quality, resources, risk and contracts before deciding.
- Forecast discipline — Use transparent formulas and assumptions; treat AI narrative as a draft around verified numbers.
- Acceptance and transition — Close only after deliverables, obligations, handover, records and open actions have named owners.
- Learning loop — Capture reusable lessons with context, evidence and a future action, then feed them into the next project.


### Implement Risk Responses and Manage Issues

A risk is an uncertain event or condition that may affect objectives; an issue is a condition that has occurred and needs action. Response planning selects a strategy, owner, preventive action, trigger, contingency and fallback. Implementation executes those actions and checks whether exposure has changed or secondary risks have appeared.

A colourful risk register does not reduce exposure. Actionable records connect priority uncertainty to funded, scheduled work and decision triggers. GenAI can challenge causes, consequences and response completeness, but probability, impact and ownership must be grounded in project evidence.

**How it works**

- Write cause–event–effect risk statements and distinguish them from current issues.
- Score probability and impact with defined anchors; prioritise by exposure and risk tolerance.
- Choose avoid, mitigate, transfer, accept or escalate for threats; exploit, enhance, share, accept or escalate for opportunities.
- Track preventive action, trigger, contingency, residual exposure and owner at each review.

**Worked example**

- Cause: supplier API access may be delayed; event: test access is unavailable by week 8; effect: integration testing and launch move.
- Mitigation secures a sandbox date; trigger is no confirmed access by Friday; contingency uses a stub for non-production testing.
- When access misses the trigger, the record becomes an issue and the contingency starts.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Preparing risk reviews, selecting response actions or converting a triggered risk into issue work. | Inventing probabilities from no data or asking AI to own a risk. |
| The team needs a consistent way to compare threats, opportunities and response urgency. | Listing vague concerns with no cause, effect, trigger, action, date or responsible owner. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.nist.gov/itl/ai-risk-management-framework

---


### Conduct and Control Procurements

Procurement management selects an appropriate sourcing approach, defines requirements and evaluation criteria, obtains authorised offers, manages contract interfaces and monitors supplier performance. Project controls must include supplier deliverables, dependencies, costs, risks, changes, acceptance and obligations.

The cheapest offer is not necessarily the best value, and an AI-generated comparison can hide missing criteria or inconsistent evidence. A weighted decision matrix makes approved criteria and evidence visible while preserving accountable commercial judgement.

**How it works**

- Confirm make-or-buy rationale, scope, acceptance, lead time, data handling, interfaces and decision authority.
- Define weighted criteria and scoring anchors before reviewing offers.
- Score only supplied evidence, record clarifications and apply required commercial and legal review.
- Monitor supplier milestones, quality, invoices, risks, changes and closure obligations against the agreement.

**Worked example**

- Three accessibility-review offers are compared on capability, approach, lead time, evidence and cost.
- AI extracts comparable fields, but missing evidence receives no invented score and procurement validates the source.
- The selected supplier's dates and acceptance evidence are integrated into the project baseline.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Planning a purchase, comparing offers or monitoring external deliverables and obligations. | Sharing confidential offers with an unapproved AI service or delegating the award decision to AI. |
| A supplier dependency affects the critical path, quality, risk or acceptance. | Changing supplier scope informally without authorised project and contract change records. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.nist.gov/itl/ai-risk-management-framework

---


### Monitor and Control Project Work

Monitoring and control compare actual and forecast results with the approved plan, analyse variance and trends, evaluate consequences and recommend action. Useful control integrates scope, schedule, cost, quality, resources, risks, communications and supplier information at a consistent status date.

Percent complete and traffic-light colours can obscure the basis of a forecast. Controls are credible when they use traceable source data, defined thresholds and transparent calculations. GenAI may explain verified results and find contradictions, but it should not calculate from ambiguous fields or rewrite a red condition as green.

**How it works**

- Set one status date and collect actual starts, finishes, remaining duration, costs, completion evidence and open actions.
- Compare against scope, schedule and cost baselines; identify cause, consequence, owner and corrective option.
- Use trend and forecast measures with stated assumptions; keep source data and narrative linked.
- Escalate forecast breaches and decisions according to tolerance and governance rules.

**Worked example**

- At week 8: planned value is SGD 72,000, earned value SGD 60,000 and actual cost SGD 66,000.
- Schedule performance index = 60/72 = 0.83; cost performance index = 60/66 = 0.91.
- The project is behind plan and over cost for the work achieved; the report explains the integration-test dependency and recovery options.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Preparing a status review, diagnosing variance or forecasting whether objectives remain achievable. | Using narrative confidence without source data, a status date or baseline reference. |
| Several control dimensions must be reconciled before a decision. | Applying earned-value formulas when scope, schedule and cost are not integrated enough to support them. |

**Authoritative references**

- https://www.gao.gov/products/gao-20-195g
- https://www.gao.gov/products/gao-16-89g
- https://www.nasa.gov/ocfo/ppc-corner/ppc-guidance-documents/

---


### Perform Integrated Change Control

Integrated change control records a proposed change, analyses its total impact, obtains a decision from the authorised body and updates affected baselines and records only after approval. It also communicates the decision and verifies implementation. Change control protects value and traceability; it is not a promise to reject change.

A small feature can alter design, testing, schedule, cost, support, supplier work and risk. GenAI is useful for building an impact checklist and comparing options, but its proposal must be reconciled with the WBS, schedule, estimates, contracts and stakeholder evidence.

**How it works**

- Log the request with reason, value, urgency, requester and affected requirement or deliverable.
- Analyse options across scope, schedule, cost, quality, resources, risk, procurement, operations and benefits.
- Recommend approve, reject, defer or request more information; record decision, authority and rationale.
- After approval, update every affected baseline, plan, log, communication and work authorisation.

**Worked example**

- A bilingual FAQ is requested in week 8. The analysis adds content, translation, accessibility checks and support training.
- Option A adds SGD 9,000 and eight working days; option B pilots ten priority articles within tolerance.
- The sponsor approves option B; scope, schedule, cost, risk and stakeholder records are updated together.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A requirement, deliverable, baseline, contract or control threshold may change. | Implementing the request before authorisation or updating only the schedule while leaving scope and cost unchanged. |
| The team needs a traceable decision and coordinated update across project records. | Treating an AI recommendation as approval or omitting rejected options and rationale. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://standards.nasa.gov/standard/MSFC/MSFC-HDBK-3684

---


### Control Scope, Schedule, Costs, Quality and Resources

Control maintains alignment between approved baselines and actual work. Scope control prevents unapproved expansion and preserves traceability; schedule control updates logic and forecasts; cost control tracks actuals and estimates; quality control evaluates results; resource control compares required and available capability. Corrective action is integrated because one dimension can shift another.

Local optimisation can worsen the whole project—for example, adding people may increase cost and coordination load without recovering a late dependency. A control decision should state evidence, options, trade-offs and the authorised path.

**How it works**

- Trace every current work item to approved scope and route additions through change control.
- Update remaining duration and dependency logic before forecasting dates; analyse critical and near-critical paths.
- Compare budget, actual cost, committed cost and estimate to complete using consistent cut-off dates.
- Review defects, capacity, supplier results and risks together before recommending action.

**Worked example**

- Integration testing is late because supplier access moved, not because test effort increased.
- The team protects acceptance criteria, resequences training preparation and uses the authorised stub contingency.
- The forecast, cost impact, residual risk and stakeholder message are updated from the same decision.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Correcting performance, reforecasting, protecting scope or deciding how to use limited capacity. | Changing a baseline to make current performance look acceptable. |
| A variance crosses tolerance or affects another baseline dimension. | Recommending action from one metric without analysing consequences for quality, risk, people and value. |

**Authoritative references**

- https://www.gao.gov/products/gao-16-89g
- https://www.gao.gov/products/gao-20-195g
- https://standards.nasa.gov/standard/MSFC/MSFC-HDBK-3684

---


### Monitor Communications, Stakeholders and Risks

Monitoring checks whether communication is reaching the right people in time, whether stakeholder engagement is moving toward the desired state and whether risk exposure and response effectiveness have changed. The team updates plans from evidence such as decisions delayed, questions repeated, actions missed, sentiment expressed directly and triggers observed.

A communication can be sent yet fail to produce understanding or action. Stakeholder and risk conditions also change as delivery progresses. GenAI can cluster feedback and surface contradictions from approved material, but it must not infer hidden motives or treat sentiment labels as facts.

**How it works**

- Compare planned and actual communication by audience, purpose, timing, reach and required action.
- Review current versus desired engagement using direct evidence and update owners and actions.
- Re-score risks after responses, identify emerging and secondary risks and close only when criteria are met.
- Escalate when information, engagement or exposure crosses the defined threshold.

**Worked example**

- Support agents repeat the same launch-readiness question, showing that the FAQ update did not create understanding.
- The project replaces a one-way email with a live walkthrough and captures unresolved questions.
- The adoption risk score and communication plan are updated after the session.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Checking the effectiveness of a status cycle, change communication, adoption activity or risk response. | Inferring private attitudes from sparse text or storing unnecessary personal commentary. |
| A stakeholder delay or misunderstanding threatens a milestone or acceptance. | Closing a risk because an action was completed without checking residual exposure. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.nist.gov/itl/ai-risk-management-framework
- https://www.pdpc.gov.sg/guidelines-and-consultation/2020/03/advisory-guidelines-on-key-concepts-in-the-personal-data-protection-act

---


### Close the Project or Phase

Closure confirms that approved work is complete or formally transferred, acceptance is recorded, contracts and obligations are settled, operations can support the outcome, records are archived, remaining actions have owners and lessons are reusable. Closure may also document an authorised early termination and its consequences.

A launch date is not the same as closure. Unaccepted deliverables, open supplier obligations, unsupported operations or undocumented decisions create hidden work and risk. GenAI can help compile a closeout pack from verified records, but each acceptance, financial and contractual fact needs an authoritative source.

**How it works**

- Reconcile charter objectives, requirements, deliverables, acceptance records and approved changes.
- Complete transition, support, data, access, supplier, financial and records-management actions.
- Assign every residual action, risk and benefit measure to an operational owner with a date.
- Capture lessons as context–action–result–recommendation and publish them where future teams can find them.

**Worked example**

- The pilot is accepted with two minor actions transferred to the service owner and dated.
- Supplier acceptance, final invoice, access removal, support runbook and benefits review are recorded.
- A lesson about early content approval includes evidence, consequence and a reusable planning action.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Completing a project or phase, transitioning ownership or documenting an authorised stop. | Declaring closure because the team stopped working or because an AI summary says all items are complete. |
| Preparing an evidence pack for sponsor confirmation and future project reuse. | Leaving open actions, risks, benefits or support obligations without named operational owners. |

**Authoritative references**

- https://www.pmi.org/standards/process-groups
- https://www.pmi.org/-/media/pmi/documents/public/pdf/pmief/skills-for-life-english.pdf

---


### Lab 7 — Build the Risk, Issue and Procurement Response Cockpit

Learning outcome: LO3: anticipate and implement risk, issue and supplier responses from verified evidence.

Goal: Convert priority uncertainty and supplier evidence into owned, triggered and measurable response actions.

You will refresh the initial risk register at the week-8 status date, distinguish triggered risks from current issues and compare three synthetic accessibility-review offers against criteria written in Lab 3. GenAI may structure evidence and challenge gaps, but final scores, owners and recommendation remain human-owned.

**What you'll build**

04-control/risk-issue-cockpit.csv, procurement-comparison.csv and response-brief.md with current exposure, triggered actions, weighted supplier evidence and integrated project impacts.   (Tools: Spreadsheet · text editor · approved AI assistant · risk-issue-inputs.csv · vendor-bids.csv.)

**Prerequisites**

- Initial risk register and procurement-evaluation-plan.csv from Lab 3.
- Verified week-8 evidence table and status pack from Lab 6.
- Open labs/assets/risk-issue-inputs.csv and labs/assets/vendor-bids.csv.

**Step-by-step**

1. Copy the initial risks into 04-control/risk-issue-cockpit.csv and add Status_Date, Current_Status, Trigger_Result, Response_Action_Status, Issue_ID, Issue_Action, Action_Owner, Due, Residual_Probability, Residual_Impact and Residual_Exposure. Apply the week-8 update rows from risk-issue-inputs.csv. A risk becomes an issue only when the stated condition has occurred.

   ```bash
   Risk lifecycle: Open → Triggered → Response active → Closed
Issue lifecycle: Open → Action active → Resolved → Closed
Residual_Exposure = Residual_Probability × Residual_Impact
   ```

2. Ask the assistant to critique each cause–event–effect statement, trigger and response using only the cockpit and status evidence. Request missing fields and contradictions, not replacement scores. Make the final current and residual scores yourself; for each triggered item record the preventive action outcome, contingency start, owner, due date and secondary risk.

   ```bash
   Return Risk_ID | Structural gap | Evidence | Consequence | Repair question.
Do not invent probability, impact, trigger evidence or owner.
Separate a future uncertain event from a condition that has already occurred.
   ```

3. Copy vendor-bids.csv to procurement-comparison.csv. Add the five approved criterion scores from the evidence using the 1, 3 and 5 anchors written in Lab 3. Calculate Weighted_Total as the sum of Score × Weight divided by 100. Record Missing_Evidence, Clarification, Commercial_Review and Human_Recommendation. Do not change criteria after seeing the offers.

   ```bash
   Weighted_Total = Σ(criterion score × criterion weight) / 100
Expected evidence-based totals: Vendor A 3.90 · Vendor B 4.10 · Vendor C 3.70
   ```

4. Create response-brief.md with sections Status date, Top exposure, Triggered responses, Current issues, Supplier comparison, Recommendation, Project impacts, Decisions and Monitoring. Recommend Vendor B for authorised commercial review because it has the highest evidence-based total; do not call it awarded. Link supplier lead time, cost and data handling to the schedule, budget, quality and risk records.

   ```bash
   Recommendation wording: 'Recommend Vendor B for authorised commercial review, subject to clarification and required approval.'
Impact dimensions: scope · schedule · cost · quality · resources · data · risk · communications
   ```

5. Run a cockpit completeness check. Every high exposure or current issue must have one owner, one next action, one due date and one review point. Every supplier score must cite a bid field. Add a monitoring calendar with daily issue follow-up until stabilised, weekly risk review and supplier milestone checks.

   ```bash
   Completeness: evidence · status · action · owner · due · residual exposure · review date
Supplier trace: criterion score → bid field → anchor → human reviewer
   ```


**Test it**

All five initial risks must appear in the cockpit, with week-8 status, trigger result, current or residual exposure, owned action and review point. Conditions that have occurred must have Issue_IDs and must not remain worded only as future uncertainty. Procurement weights must remain unchanged and totals must be Vendor A 3.90, Vendor B 4.10 and Vendor C 3.70. The response brief must recommend—not award—Vendor B, integrate eight impact dimensions and contain the stated monitoring cadence.

**Checkpoint and rejoin point**

Keep the cockpit, comparison and response brief. Lab 8 uses the current exposures, supplier recommendation and week-8 forecast in a change decision. To rejoin, reproduce the three weighted totals before making a recommendation.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| A triggered risk and its resulting issue are duplicated with different owners. | Link them with Issue_ID, retain the risk for residual exposure and name one coordinated response owner. |
| The assistant scores missing supplier evidence as average. | Use the prewritten anchor; record missing evidence and request clarification instead of inventing a score. |
| The highest-scoring offer is described as awarded. | Change the status to Recommended for commercial review until the authorised process records a decision. |

**Challenge**

Recalculate totals if lead-time weight rises from 20 to 30 and cost falls from 15 to 5. Explain why that scenario is sensitivity analysis, not permission to change the approved criteria after bids were opened.

**Reflection**

Which risk or supplier conclusion changed most after evidence, trigger and scoring anchors were made explicit?

> **Note:** The complete lab and its support-file references are in labs/lab-07-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


### Lab 8 — Run Integrated Change Control and Baseline Impact Analysis

Learning outcome: LO3: evaluate and decide a project change across all affected controls with GenAI support.

Goal: Process CR-004 from request through impact analysis, authorised decision and coordinated record update.

You will evaluate a request for bilingual pilot content at week 8. The exercise prevents a useful feature from bypassing scope, schedule, cost, quality, resource, risk, supplier, communication and operational review. You will model options, record the synthetic sponsor decision and publish a traceable Baseline v1.1.

**What you'll build**

04-control/change-log.csv, change-impact-analysis-CR-004.md, baseline-v1.1.csv and change-implementation-checklist.md with an approved, fully traced incremental change.   (Tools: Spreadsheet · text editor · approved AI assistant · change-request-CR-004.md · Labs 3, 6 and 7 records.)

**Prerequisites**

- Frozen Baseline v1.0 and verified week-8 status evidence.
- Risk-issue cockpit and procurement response brief from Lab 7.
- Open labs/assets/change-request-CR-004.md and separate Request evidence from Sponsor decision record.
- Use the four preformatted Lab 8 starter files in labs/assets; do not recreate their schemas.

**Step-by-step**

1. (6 minutes) Copy lab-08-change-log-starter.csv to 04-control/change-log.csv with Change_ID, Date_Logged, Requester, Reason, Requested_Outcome, Urgency, Affected_Requirement, Status, Decision_Owner, Decision_Date, Decision, Rationale and Implementation_Status. Enter CR-004 from the Request section only and set Status to Analysing.

   ```bash
   Status: Logged | Analysing | More information | Approved | Rejected | Deferred | Implemented | Verified
Do not copy the sponsor decision until impact analysis is complete.
   ```

2. (12 minutes) Copy lab-08-change-impact-analysis-starter.md to 04-control/change-impact-analysis-CR-004.md. Complete the current baseline and four options: reject, defer, full 30-article change and ten-priority-article pilot. Ask the assistant to propose an impact checklist, then complete it from project evidence across value, scope, schedule, cost, quality, resources, risk, supplier, communications, operations, benefits and alternatives.

   ```bash
   For each option return: value · scope delta · WBS delta · duration · cost · quality evidence · resource need · risk · supplier · communication · operational effect · assumptions · recommendation.
Use UNKNOWN when the project record is silent.
   ```

3. (10 minutes) Calculate the two implementation options. Confirm that full scope adds SGD 9,000 and eight working days. Confirm that the pilot adds SGD 3,500 and three working days. Compare each with the authorised budget, remaining contingency, week-8 forecast, available translation capacity and acceptance evidence. Recommend the pilot with explicit residual risk and benefit limits.

   ```bash
   Full option: +SGD 9,000 · +8 working days
Pilot option: +SGD 3,500 · +3 working days
Pilot revised work budget = SGD 108,500
Remaining contingency = SGD 11,500
Pilot revised baseline duration = 31 working days
   ```

4. (12 minutes) After finishing the analysis, read the Sponsor decision record in the supplied file. Enter the approved pilot decision, owner, date and rationale in the change log. Copy lab-08-baseline-v1.1-starter.csv to 04-control/baseline-v1.1.csv. The exact approved WBS delta is a new WP-09A row, 'Ten-priority-article bilingual pilot package', duration 3, predecessors WP-08 and WP-09, work budget SGD 3,500; WP-10 then depends on WP-09A. Update planned baseline fields only. Keep week8-performance.csv, delivery-board.csv and the week-8 status pack frozen as historical evidence; do not add actual or variance fields to Baseline v1.1.

   ```bash
   Baseline version note: v1.1 implements approved CR-004 only.
Revised work budget SGD 108,500 + remaining contingency SGD 11,500 = authorised total SGD 120,000.
Revised duration 31 working days; prior status evidence remains unchanged.
   ```

5. (10 minutes) Copy lab-08-change-implementation-checklist-starter.md to 04-control/change-implementation-checklist.md. Complete the preformatted updates for charter or requirement trace, WBS, schedule, cost, quality and acceptance, resources, risk, supplier, communications, stakeholder engagement, work authorisation and status reporting. Give each update an owner, due, evidence and verification. Set the change to Implemented only after all required rows are complete, then Verified only after the acceptance check.

   ```bash
   Update row: Controlled record | Exact change | Owner | Due | Evidence | Status | Verifier
Lifecycle: Approved → baseline updated → work authorised → deliverable verified → change Verified
   ```


**Test it**

CR-004 must have a complete request record, four analysed options and at least 12 impact dimensions. The analysis must show full scope at +SGD 9,000/+8 days and the approved pilot at +SGD 3,500/+3 days. Baseline v1.1 must show SGD 108,500 work budget, SGD 11,500 remaining contingency, unchanged SGD 120,000 authorised total and 31 working days. The implementation checklist must contain all 12 controlled-record updates with owner, evidence and verifier. Baseline v1.1 must add WP-09A and make WP-10 depend on it, while week8-performance.csv, delivery-board.csv and the week-8 status pack remain frozen and unchanged.

**Checkpoint and rejoin point**

Keep the approved change log, Baseline v1.1, analysis and implementation evidence. Lab 9 reconciles these with final acceptance and closure. To rejoin, apply only the Sponsor decision record after reproducing both option calculations.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The revised budget becomes SGD 123,500. | The approved pilot draws from contingency: increase work budget by SGD 3,500 and reduce remaining contingency by the same amount. |
| The status history becomes Green after rebaselining. | Restore week-8 actuals and forecast; the new baseline reflects approved scope, not erased historical variance. |
| Only the schedule and cost files are updated. | Use the 12-row implementation checklist and keep the change open until every affected controlled record is addressed. |

**Challenge**

Model a defer-to-next-phase option with no current baseline change. State which benefits, risks, stakeholder expectations and transition records would still require action now.

**Reflection**

Which impact dimension made the requested change larger than its apparently simple content description?

> **Note:** The complete lab and its support-file references are in labs/lab-08-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


### Lab 9 — Close the Project and Capture Reusable Lessons

Learning outcome: LO4: validate scope, obtain acceptance, transition ownership and close with traceable records.

Goal: Produce a complete closeout pack that reconciles objectives, deliverables, obligations and future ownership.

You will use the final synthetic evidence to determine whether the BeaconWorks pilot is ready to close. GenAI will help compile and challenge the pack, while you trace each statement to final records, transfer remaining actions and benefits, and record the synthetic sponsor’s closure decision.

**What you'll build**

05-closure/closeout-checklist.csv, project-closeout-report.md, transition-and-benefits-plan.md and lessons-register.csv with formal acceptance, residual ownership and reusable context.   (Tools: Spreadsheet · text editor · approved AI assistant · closure-inputs.md · complete Labs 1–8 portfolio.)

**Prerequisites**

- Approved Baseline v1.1, change implementation evidence and all project logs from Labs 1–8.
- Open labs/assets/closure-inputs.md and use the final cut-off stated there.
- Create an archive copy of the final lab outputs before preparing the closeout summary.
- Use the four preformatted Lab 9 starter files in labs/assets; do not recreate their schemas.

**Step-by-step**

1. (12 minutes) Copy lab-09-closeout-checklist-starter.csv to 05-closure/closeout-checklist.csv with Category, Item_ID, Requirement_or_Obligation, Final_Status, Evidence, Acceptance_or_Transfer_Owner, Date, Residual_Action, Residual_Owner, Due and Closure_Blocker. Include charter objectives, original deliverables, CR-004 pilot scope, quality evidence, supplier obligations, invoices, access, records, training, support, risks, issues, benefits and communications.

   ```bash
   Final status: Complete | Accepted | Transferred | Open action | Not applicable
Closure blocker: YES only when completion, acceptance, legal, financial, operational or safety conditions prevent closure.
   ```

2. (12 minutes) Reconcile the preformatted checklist against the charter, requirements trace, Baseline v1.1, quality log, change log, risk-issue cockpit and procurement records. Ask the assistant for candidate gaps with File, Record_ID, Expected, Found and Consequence. Verify each gap yourself and update the checklist; never mark an item complete from the summary alone.

   ```bash
   Closeout reconciliation: objective → deliverable → requirement → verification → acceptance → owner
Commercial reconciliation: agreement → deliverable → acceptance → invoice → obligation closed or transferred
   ```

3. (10 minutes) Copy lab-09-transition-benefits-starter.md to 05-closure/transition-and-benefits-plan.md with Operational owner, Support boundary, Runbook and training, Access and data actions, Supplier follow-up, Open actions, Residual risks, Benefit measure, Baseline, Target, Measurement date, Data owner and Review forum. Transfer each non-blocking residual item to one named owner and obtain a stated due date.

   ```bash
   Residual item | Context | Current exposure | Action | Owner | Due | Review forum | Escalation
Benefit record | Baseline | Target | Measure date | Data source | Owner | Decision after review
   ```

4. (8 minutes) Copy lab-09-lessons-register-starter.csv to 05-closure/lessons-register.csv with Lesson_ID, Context, Expected, Observed, Evidence, Cause, Action_Taken, Result, Recommendation, Future_Owner and Reuse_Trigger. Use C-A-R-R: Context, Action, Result, Recommendation. Extract candidate lessons from the project records, then keep at least six that have evidence and a future action.

   ```bash
   C-A-R-R lesson: Context → Action → Result → Recommendation
Reject generic entries such as 'communicate more' unless context, evidence and reusable action are stated.
   ```

5. (8 minutes) Copy lab-09-closeout-report-starter.md to 05-closure/project-closeout-report.md. Complete its preformatted sections: Executive outcome, Objectives, Scope and changes, Schedule, Cost, Quality and acceptance, Stakeholders, Risks and issues, Procurement, Transition, Benefits, Lessons, Records location and Closure decision. Use the assistant to draft from the verified checklist only. Compare every figure and status with its source, then enter the Sponsor closure record from closure-inputs.md.

   ```bash
   Draft only from <VERIFIED CLOSEOUT CHECKLIST>.
Separate final fact, residual action and future benefit.
Finish with Claim | Evidence ID | Owner | Human verification.
Closure decision must name decision owner, date, accepted outcome and transferred actions.
   ```


**Test it**

The checklist must cover all 14 named categories, trace each completion or acceptance to evidence and show no unresolved Closure_Blocker. Every residual action, risk and benefit must have one owner and date in the transition plan. The lessons register must contain at least six evidence-backed C-A-R-R records with reuse triggers. The closeout report must contain all 14 named report sections plus the completed Claim verification table, reconcile final schedule and cost with the supplied evidence, record the sponsor closure decision and point to the final records location.

**Checkpoint and rejoin point**

This is the final checkpoint. The complete portfolio runs from AI working agreement and charter through Baseline v1.1, delivery and control evidence, acceptance, transition, benefits and reusable lessons.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| A residual action has no owner because the project team is disbanding. | Do not close that row; transfer it to an operational owner with due date and review forum. |
| The closeout summary says all objectives were achieved but one benefit is measured later. | Separate delivered capability from future benefit and keep the benefit review in the transition plan. |
| A lesson is a vague slogan. | Add project context, evidence, action, observed result and a specific recommendation with reuse trigger. |

**Challenge**

Prepare a one-page early-termination variant. Identify what acceptance, financial, supplier, records, people and risk actions would still be required even if the project stopped before delivering the pilot.

**Reflection**

Which closure record most clearly demonstrates that project completion and long-term benefit ownership are different?

> **Note:** The complete lab and its support-file references are in labs/lab-09-*.md. Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

---


## Wrap-Up — Operate the Integrated System

The nine labs produce one connected project evidence set. The value is not a collection of prompts; it is the traceability from business need to authorised plan, delivery evidence, control decision and closure.

**The Four Control Questions**

At every project review, ask the same four questions and point to evidence.

- What was approved, and where is that baseline or decision recorded?
- What has actually happened as of one status date?
- What is now forecast, and which assumptions or risks drive it?
- Who must decide or act next, by when, and what record will change?

**A Safe GenAI Handoff**

Before reusing a project prompt or artifact in the workplace, adapt it to organisational controls.

- Confirm approved tools, data classes, retention, access and review requirements.
- Replace synthetic scenario values only with authorised source records.
- Test prompts on representative examples and preserve a manual fallback.
- Assign an owner for accuracy, decisions, monitoring and continuous improvement.

---


## Next Steps

- Select one low-risk project artifact—such as a source-led meeting summary—and apply the C-O-S-T-A-R prompt pattern.
- Define the evidence, human review and record-update steps before using GenAI on a live project.
- Track one quality measure such as unsupported claims found, editing time or action-owner corrections.
- After three uses, review failures and update the prompt, checklist and organisational guidance.


## Glossary

- **Acceptance criteria** — Observable conditions a deliverable must satisfy for the authorised stakeholder to accept it.
- **Actual cost (AC)** — Cost incurred for the work performed as of the status date.
- **Assumption** — A factor treated as true for planning that requires validation or a response if it changes.
- **Baseline** — The approved version of scope, schedule or cost used for comparison and control.
- **Change request** — A documented proposal to modify a deliverable, baseline, plan or controlled record.
- **Cost performance index (CPI)** — Earned value divided by actual cost; a ratio below 1.0 indicates more cost was spent than value earned.
- **Critical path** — The longest dependent path through the schedule that determines the earliest finish under current logic.
- **Earned value (EV)** — Budgeted value of work actually completed as of the status date.
- **GenAI** — Generative artificial intelligence that creates content from instructions and context.
- **Issue** — A condition that has occurred and requires action or decision.
- **Planned value (PV)** — Budgeted value of work planned to be complete as of the status date.
- **Prompt** — The instruction, context, sources, constraints and desired output given to an AI assistant.
- **RACI** — A responsibility view identifying Responsible, Accountable, Consulted and Informed roles.
- **Risk** — An uncertain event or condition that may positively or negatively affect project objectives.
- **Schedule performance index (SPI)** — Earned value divided by planned value; a ratio below 1.0 indicates less work completed than planned.
- **Source ledger** — A table linking material facts and generated claims to authoritative project evidence.
- **Stakeholder** — A person, group or organisation that can affect, be affected by or perceive an effect from the project.
- **Status date** — The common cut-off date for actuals, progress, variance and forecast information.
- **Work breakdown structure (WBS)** — A deliverable-oriented decomposition of the complete project scope.
- **Work package** — A manageable WBS component that can be estimated, assigned, monitored and accepted.
