"""Topic 1 connected labs: initiation and planning."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Build the AI Working Agreement and Project Charter",
        duration=70,
        objective="LO1: develop evidence-led project parameters and an authorised charter draft with GenAI",
        goal="Create the control rules and initiation pack that will govern every later lab.",
        workflow=["Inspect evidence", "Define AI controls", "Draft the charter", "Trace and approve"],
        desc=(
            "You will open the synthetic BeaconWorks Customer Self-Service Portal brief, define a human-owned GenAI "
            "working agreement and turn the approved facts into a project charter. The exercise separates facts, "
            "assumptions, options and unknowns so polished language never becomes an unreviewed commitment."
        ),
        build=(
            "01-initiation/ai-working-agreement.md, project-charter.md and source-ledger.csv containing the approved "
            "project parameters, human review gates and traceable evidence."
        ),
        services="Text editor · approved AI assistant · beaconworks-project-brief.md · spreadsheet",
        prerequisites=[
            "Create a local folder named C013-BeaconWorks-Project with 01-initiation through 05-closure subfolders.",
            "Open labs/assets/beaconworks-project-brief.md and confirm that no real customer or employee data is used.",
            "Have a spreadsheet application available for the source ledger.",
        ],
        steps=[
            (
                "In 01-initiation, create source-ledger.csv with columns Record_ID, Claim_or_Parameter, Value, "
                "Source_File, Source_Section, Classification, Human_Owner and Status. Add rows for the business need, "
                "budget ceiling, target week, sponsor, project manager, pilot deliverable and stated exclusions. "
                "Use FACT only when the source brief says it directly; otherwise use ASSUMPTION or UNKNOWN.",
                "Record_ID,Claim_or_Parameter,Value,Source_File,Source_Section,Classification,Human_Owner,Status\n"
                "SRC-001,Business need,<VALUE>,beaconworks-project-brief.md,<SECTION>,FACT,Project Manager,Verified",
            ),
            (
                "Create ai-working-agreement.md with six headings: Approved uses, Restricted information, Prompt rule, "
                "Review gates, Decision authority and Record keeping. Under Prompt rule, write the C-O-S-T-A-R pattern. "
                "Under Review gates, require evidence, calculation, confidentiality, bias, authority and record-update checks.",
                "C-O-S-T-A-R\n"
                "Context: project and audience\nObjective: one observable task\nSources: delimited approved evidence\n"
                "Tasks: ordered operations\nAcceptance criteria: format and quality checks\n"
                "Review: facts, figures, uncertainty, confidentiality and human authority",
            ),
            (
                "Paste only the project brief into the approved AI assistant and request a charter draft with Purpose, "
                "Measurable objectives, High-level deliverables, In scope, Out of scope, Milestones, Budget, Assumptions, "
                "Constraints, Initial risks, Stakeholders, Authority and Approval readiness. Require a second table that "
                "labels each material statement FACT, ASSUMPTION, OPTION or UNKNOWN and cites the brief section.",
                "Objective: Draft a project charter from <PROJECT BRIEF> only.\n"
                "Do not invent dates, people, figures or requirements. Use UNKNOWN when absent.\n"
                "Return: charter headings + Statement | Classification | Source section | Review needed.\n"
                "Before finishing, list contradictions and missing approval information.",
            ),
            (
                "Save the response as project-charter-ai-draft.md. Review every objective and parameter against the "
                "brief and source ledger. Edit the human-approved version into project-charter.md. Each objective must "
                "contain a result, measure, target and time horizon. Move unsupported material to Assumptions or Open "
                "questions; never repair a gap by inventing evidence.",
                "Objective quality check: result + measure + target + time horizon\n"
                "Parameter quality check: source row + classification + owner + status\n"
                "Final labels: FACT | ASSUMPTION | OPTION | UNKNOWN",
            ),
            (
                "Add a Charter readiness checklist to project-charter.md. Mark each item READY or ACTION: business "
                "need, objectives, boundaries, deliverables, budget, milestone horizon, authority, initial risks and "
                "open questions. Record the project manager as document owner and the synthetic sponsor as approval "
                "owner. Do not mark the charter approved; mark it Ready for sponsor review.",
                "Readiness item | Status | Evidence or action | Owner | Due\n"
                "Final document status: Ready for sponsor review",
            ),
        ],
        test=(
            "The working agreement must contain all six headings and the six-part C-O-S-T-A-R pattern. The charter must "
            "contain all 13 requested sections, at least three measurable objectives, an explicit out-of-scope statement, "
            "a named document owner and approval owner, plus the status Ready for sponsor review. The source ledger must "
            "contain at least seven rows; every material figure and date in the charter must trace to a verified FACT row "
            "or be labelled ASSUMPTION or UNKNOWN."
        ),
        checkpoint=(
            "Keep the three initiation files. Lab 2 uses the charter boundaries and source ledger. To rejoin, copy the "
            "approved course checkpoint from labs/assets/checkpoint-01-initiation.md and mark its assumptions Pending validation."
        ),
        troubleshooting=[
            (
                "The assistant adds a launch date or benefit target not present in the brief.",
                "Delete it from the approved charter, add it to Open questions and repeat the prompt with 'Use UNKNOWN when absent.'",
            ),
            (
                "The objective sounds positive but cannot be checked.",
                "Add a measure, target and time horizon while preserving the business intent in the source.",
            ),
            (
                "A fact has no clear source section.",
                "Classify it as ASSUMPTION or UNKNOWN until a direct source can be cited.",
            ),
        ],
        challenge=(
            "Ask the assistant to critique the final charter as sponsor, operations owner and delivery lead. Keep only "
            "questions that expose a real gap, cite the role that raised each one and do not let the critique alter the charter."
        ),
        reflection=(
            "Which charter sentence was most improved by separating fact from assumption, and what decision risk did that prevent?"
        ),
    ),
    dict(
        num=2,
        topic=1,
        title="Build the Stakeholder Engagement and Communications Plan",
        duration=80,
        objective="LO1: identify stakeholders and plan evidence-led engagement and communications",
        goal="Create a role-based stakeholder strategy with explicit decisions, messages, owners and review triggers.",
        workflow=["Identify roles", "Analyse evidence", "Plan engagement", "Design communications"],
        desc=(
            "You will combine the approved charter with the supplied stakeholder inputs. GenAI will help structure and "
            "challenge the plan, while you make the final influence, interest, impact and engagement decisions from "
            "evidence. The resulting communication matrix starts with the action or decision each audience needs."
        ),
        build=(
            "02-planning/stakeholder-register.csv and stakeholder-communications-plan.md with eight stakeholder rows, "
            "current and desired engagement, owned actions, decision-focused communications and privacy safeguards."
        ),
        services="Spreadsheet · text editor · approved AI assistant · stakeholder-inputs.csv · Lab 1 charter",
        prerequisites=[
            "Completed project-charter.md and source-ledger.csv from Lab 1, or the stated rejoin checkpoint.",
            "Open labs/assets/stakeholder-inputs.csv and read the Data_boundary column before prompting.",
            "Use roles and supplied project evidence; do not add private opinions or sensitive traits.",
        ],
        steps=[
            (
                "Copy stakeholder-inputs.csv to 02-planning/stakeholder-register.csv. Add columns Influence_1_5, "
                "Interest_1_5, Project_Impact_1_5, Current_Engagement, Desired_Engagement, Strategy, Action, Action_Owner, "
                "Review_Trigger and Evidence. Preserve Stakeholder_ID and use role names rather than personal details.",
                "Allowed engagement states: Unaware | Resistant | Neutral | Supportive | Leading\n"
                "Allowed strategies: Manage closely | Keep satisfied | Keep informed | Monitor",
            ),
            (
                "Paste only the charter and permitted stakeholder rows into the assistant. Ask for proposed scores and "
                "engagement states with a short evidence citation. Require UNKNOWN when a rating cannot be supported. "
                "Enter the suggestions in temporary Proposed_* columns; do not copy them directly into final columns.",
                "For each Stakeholder_ID return Proposed influence, interest, impact, current state and desired state.\n"
                "Cite only supplied evidence. Do not infer personality, demographic, political or sensitive traits.\n"
                "Use UNKNOWN when evidence is absent and list one question to validate it.",
            ),
            (
                "Review each proposal. Enter final 1–5 scores and states, then choose a strategy and one observable "
                "engagement action. Add an action owner and review trigger. If your final value differs from the proposal, "
                "record the reason in Evidence. Check that high-impact affected users receive dialogue, not only broadcast.",
                "Human review gate: evidence present · impact considered · strategy proportional · owner named · trigger observable",
            ),
            (
                "Create stakeholder-communications-plan.md with a table containing Communication_ID, Audience_IDs, "
                "Purpose_or_Decision, Verified_Input, Message_Outline, Format, Channel, Cadence_or_Trigger, Sender, "
                "Feedback_Method, Record_Location and Escalation. Include a sponsor decision brief, delivery-team "
                "coordination, support-agent design review, supplier interface and launch-readiness update.",
                "Start with: What must this audience understand, decide or do?\n"
                "Then specify: evidence → message → channel → feedback → record → escalation",
            ),
            (
                "Ask the assistant to produce a 120-word sponsor version and a 120-word support-agent version of the same "
                "scope-boundary update. Compare both with the charter. Save the two drafts under Audience transformation "
                "example, correct any unsupported detail and add a note explaining what changed and what stayed invariant.",
                "Use only <VERIFIED CHARTER EXTRACT>.\n"
                "Draft A for sponsor: decision, tolerance, recommendation and ask.\n"
                "Draft B for support agents: workflow impact, participation, timing and feedback route.\n"
                "Keep facts, uncertainty and boundary identical in both.",
            ),
        ],
        test=(
            "The register must contain exactly eight supplied Stakeholder_ID rows and no added personal data. Every row "
            "must have final influence, interest and impact scores; current and desired states; a strategy; an owned action; "
            "a review trigger; and evidence or UNKNOWN. The communications plan must contain at least five records and all "
            "12 columns. The two audience drafts must preserve identical project facts and include different purpose-appropriate asks."
        ),
        checkpoint=(
            "Keep both planning files. Lab 3 uses the acceptance owner, specialist availability, supplier interface and "
            "communication triggers. To rejoin, use stakeholder-inputs.csv and the final-value rules printed in this lab."
        ),
        troubleshooting=[
            (
                "Every stakeholder is rated high influence and high interest.",
                "Compare decision authority, ability to affect the work and need for detail; use the supplied anchors and evidence independently.",
            ),
            (
                "The plan contains generic actions such as 'communicate regularly'.",
                "Name the purpose, artifact, owner, cadence or trigger and required feedback or decision.",
            ),
            (
                "The assistant infers attitude or motivation.",
                "Delete the inference, use UNKNOWN and create a respectful validation question or engagement action.",
            ),
        ],
        challenge=(
            "Create a second communication route for the highest-impact stakeholder if the normal channel is unavailable. "
            "State when the alternate route activates and how the official decision record remains singular."
        ),
        reflection=(
            "Which stakeholder needed the largest shift from current to desired engagement, and what evidence-led action could create that shift?"
        ),
    ),
    dict(
        num=3,
        topic=1,
        title="Build the Integrated Project Management Plan",
        duration=90,
        objective="LO1: develop an integrated scope, schedule, cost, quality, resource, communication, risk and procurement plan",
        goal="Turn the authorised project parameters into one coherent baseline and management plan.",
        workflow=["Decompose scope", "Sequence and estimate", "Integrate controls", "Verify the baseline"],
        desc=(
            "You will use the charter, stakeholder plan and supplied work-package inputs to create a WBS-aligned baseline. "
            "You will calculate the network and budget yourself, then use GenAI to critique integration gaps across quality, "
            "resources, communications, risks and procurement."
        ),
        build=(
            "02-planning/wbs-and-baseline.csv, integrated-management-plan.md, initial-risk-register.csv and "
            "procurement-evaluation-plan.csv with a verified 28-working-day critical path and SGD 120,000 authorised budget."
        ),
        services="Spreadsheet · text editor · approved AI assistant · planning-inputs.csv · risk-issue-inputs.csv",
        prerequisites=[
            "Completed charter, source ledger, stakeholder register and communications plan from Labs 1–2.",
            "Open labs/assets/planning-inputs.csv and labs/assets/risk-issue-inputs.csv.",
            "Know that the approved budget ceiling is SGD 120,000, including SGD 15,000 contingency.",
        ],
        steps=[
            (
                "(20 minutes) Copy planning-inputs.csv to 02-planning/wbs-and-baseline.csv. Verify that the ten work packages cover "
                "the Portal Pilot deliverable and that exclusions in the charter are absent. Add columns Earliest_Start, "
                "Earliest_Finish, Latest_Start, Latest_Finish, Total_Float, Critical, Acceptance_Evidence and Human_Reviewer. Do not change supplied "
                "durations, predecessors or costs during the first calculation.",
                "WBS check: complete approved scope · no excluded scope · one owner · one acceptance criterion per work package\n"
                "Day-zero convention: a work package with no predecessor has ES = 0; EF = ES + Duration.\n"
                "Forward pass: ES = maximum predecessor EF; EF = ES + Duration.",
            ),
            (
                "(25 minutes) Complete the forward pass, then calculate the backward pass from a project finish of day 28. "
                "For terminal work packages set LF = 28 and LS = LF minus Duration. For every predecessor, set LF to the "
                "minimum LS of its successors and LS = LF minus Duration. Calculate Total_Float = LS minus ES and mark "
                "Critical = YES only when Total_Float = 0. Sum Work_Budget_SGD, add the approved contingency "
                "and compare with the charter ceiling. Record the expected baseline summary in integrated-management-plan.md. "
                "If your result is not 28 working days and SGD 105,000 work budget plus SGD 15,000 contingency, find the "
                "dependency or arithmetic error before continuing.",
                "Expected work budget = SGD 105,000\nContingency = SGD 15,000\nAuthorised total = SGD 120,000\n"
                "Expected critical path = WP-01 -> WP-03 -> WP-04 -> WP-07 -> WP-08 -> WP-10\n"
                "Expected critical path duration = 28 working days\n"
                "Backward pass: terminal LF = 28; predecessor LF = minimum successor LS; Total_Float = LS - ES",
            ),
            (
                "(20 minutes) Create integrated-management-plan.md with sections Scope, Schedule, Cost, Quality, Resources, "
                "Communications, Risk, Procurement, Change, Baseline governance and Source register. For each section "
                "state the objective, method, owner, evidence, threshold or trigger and controlled record. Link the "
                "specialist availability, supplier interface and acceptance owner from Lab 2.",
                "Component plan pattern:\nObjective | Method | Owner | Evidence | Threshold/trigger | Controlled record\n"
                "Integration check: every work package has scope + date + cost + resource + quality evidence",
            ),
            (
                "(15 minutes) Copy the five RISK rows from risk-issue-inputs.csv to initial-risk-register.csv. Add Probability_1_5, "
                "Impact_1_5, Exposure, Strategy, Preventive_Action, Trigger, Contingency, Owner and Residual_Exposure. "
                "Ask the assistant to critique cause–event–effect structure and missing response fields; make the final "
                "scores and owners yourself.",
                "Risk statement: Because <cause>, <uncertain event> may occur, leading to <effect on objective>.\n"
                "Exposure = Probability × Impact\n"
                "Do not convert a current issue into a future risk.",
            ),
            (
                "(10 minutes) Create procurement-evaluation-plan.csv for the accessibility review with criteria Capability 25, "
                "Method and evidence 25, Lead time 20, Data handling 15 and Cost 15. Write 1–5 scoring anchors before "
                "viewing any offer. Ask the assistant to inspect the four planning files for contradictions and return "
                "Issue, Evidence, Consequence and Repair. Resolve every high-consequence contradiction or record an owned open action.",
                "Criterion,Weight_Percent,Score_1_Anchor,Score_3_Anchor,Score_5_Anchor,Decision_Owner\n"
                "Capability,25,<MINIMUM>,<ADEQUATE>,<STRONG>,Procurement Lead\n"
                "Weights must total 100.",
            ),
        ],
        test=(
            "The baseline must contain ten contiguous work packages, total SGD 105,000 before contingency and show the "
            "zero-float path WP-01 -> WP-03 -> WP-04 -> WP-07 -> WP-08 -> WP-10 at 28 working days. Every row must have "
            "ES, EF, LS, LF and Total_Float calculated with the stated day-zero convention. The integrated plan must contain "
            "all 11 sections and link every work package "
            "to an owner, resource role, cost, quality or acceptance evidence and communication or control record. The risk "
            "register must contain five cause–event–effect rows with scored exposure, action, trigger, contingency and owner. "
            "Procurement criteria weights must total 100 and include written 1, 3 and 5 scoring anchors."
        ),
        checkpoint=(
            "Freeze the four files as Baseline v1.0 and add the status 'Ready for sponsor baseline review'. Labs 4–9 use "
            "these records. To rejoin, copy the supplied planning inputs and reproduce the expected 28-day and SGD 120,000 checks."
        ),
        troubleshooting=[
            (
                "The schedule finishes earlier than 28 working days.",
                "Check that each activity starts after the maximum finish of all predecessors, not the first predecessor listed.",
            ),
            (
                "The work budget does not equal SGD 105,000.",
                "Sum each unique work-package row once and keep contingency outside the work-package total.",
            ),
            (
                "The AI critique recommends changing the baseline.",
                "Treat the output as an issue list; make changes only after checking source evidence and recording the human decision.",
            ),
        ],
        challenge=(
            "Model a scenario in which content approval takes two extra days. Recalculate the finish, identify the "
            "affected critical path and propose two recovery options without changing the frozen Baseline v1.0."
        ),
        reflection=(
            "Which dependency created the strongest connection among scope, schedule, cost, resources, quality and risk?"
        ),
    ),
]
