"""Single source of truth for the C013 courseware package."""

TITLE = "Generative AI for Project Management"
SHORT_TITLE = "Generative AI for Project Management"
COURSE_CODE = "C013"
VERSION = "v1.0"
VERSION_DATE = "28 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Tertiary Infotech Academy Trainer"
COURSE_URL = "https://www.tertiarycourses.com.sg/effective-project-management-with-generative-ai-genai.html"
DAYS = 2
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am–6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Develop project parameters and an integrated project plan with GenAI according to business requirements.",
    "LO2: Resolve project delivery challenges by using GenAI to support people, knowledge, quality, communications, resources and budgets.",
    "LO3: Anticipate, monitor and respond to project risks and changes with GenAI while keeping decisions evidence-led and human-owned.",
    "LO4: Control project performance, obtain acceptance and close a project or phase with traceable records and reusable lessons.",
]

LO_TITLES = [
    "Initiate & Plan",
    "Execute & Deliver",
    "Respond & Change",
    "Control & Close",
]

TOPICS = [
    dict(
        num=1,
        code="01",
        title="Project Initiation and Planning with GenAI",
        subtitle=(
            "AI working method · charter and stakeholders · integrated management plan · "
            "scope, schedule, cost, quality, resources, communications, risk and procurement"
        ),
        weighting="Day 1 · 3 connected labs",
        concepts=[
            ("Human-owned AI workflow", "Use GenAI to propose, structure and challenge; a named project owner validates every decision."),
            ("Project charter", "Connect the business need, measurable objectives, boundaries, authority and success conditions."),
            ("Stakeholder strategy", "Separate influence, interest, impact and information needs before choosing an engagement approach."),
            ("Integrated baseline", "Link deliverables, work packages, dependencies, resources, costs and acceptance evidence."),
            ("Management plans", "Define how scope, schedule, cost, quality, communications, risks and suppliers will be managed."),
            ("Planning uncertainty", "Record assumptions, confidence, sources and review triggers instead of hiding uncertainty in polished prose."),
        ],
        sections=[
            dict(
                title="Use GenAI as a Project Co-Pilot",
                definition=(
                    "A generative AI assistant creates likely text, tables and alternatives from the instructions and context it receives. "
                    "For project work it is best treated as a co-pilot: useful for organising supplied evidence, generating options and "
                    "challenging a draft, but not an accountable decision-maker or a source of project truth."
                ),
                why=(
                    "Project records affect money, commitments, people and suppliers. Fluency can disguise a missing source, an invented "
                    "dependency or an unrealistic estimate. A controlled workflow makes the human owner, evidence boundary and review gate "
                    "visible before an output enters the project record."
                ),
                how=[
                    "Use C-O-S-T-A-R: Context, Objective, Sources, Tasks, Acceptance criteria and Review.",
                    "Delimit approved source material; require the assistant to label facts, assumptions, options and unknowns.",
                    "Verify dates, quantities, commitments and names against primary project records before approval.",
                    "Keep a prompt-and-output log for material decisions and remove restricted data before using an AI service.",
                ],
                example=[
                    "The project manager supplies the approved project brief and asks for a charter draft, not a new business case.",
                    "The response includes a source ledger and marks an unstated target date as UNKNOWN.",
                    "The sponsor selects the objective and the project manager records the final wording and rationale.",
                ],
                use_when=[
                    "The task is to structure, summarise, compare, draft, critique or explore options from approved inputs.",
                    "A human owner can check the result against evidence and has authority to approve the final record.",
                ],
                avoid_when=[
                    "The prompt would expose confidential, personal or security-sensitive information to an unapproved service.",
                    "The output would create a commitment, forecast or decision without evidence and named human approval.",
                ],
                sources=[
                    "https://www.pmi.org/learning/thought-leadership/prompt-engineering",
                    "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems",
                ],
            ),
            dict(
                title="Initiate the Project and Develop the Charter",
                definition=(
                    "Initiation turns a business need into an authorised project. A practical charter names the purpose, measurable objectives, "
                    "high-level deliverables, exclusions, constraints, major assumptions, milestone horizon, initial risks, sponsor and project "
                    "manager authority. It is a decision record, not a detailed plan."
                ),
                why=(
                    "Teams that begin with solution activity before confirming the problem and authority often optimise the wrong work. GenAI can "
                    "expose ambiguity and draft alternatives, but only the sponsor and accountable leaders can decide which outcome, tolerance and "
                    "boundary the organisation accepts."
                ),
                how=[
                    "Trace every objective to the business need and express it with a measure, target and time horizon.",
                    "Separate in-scope deliverables from explicit exclusions and list assumptions that could change the plan.",
                    "Name decision rights: sponsor, project manager, product owner and acceptance authority.",
                    "Review the charter for contradictions, unsupported promises and missing success measures before approval.",
                ],
                example=[
                    "Need: reduce customer-service response delays during seasonal peaks.",
                    "Objective: release an approved self-service portal pilot by week 12 within SGD 120,000, with named acceptance checks.",
                    "Exclusion: replacement of the existing case-management platform; this prevents silent expansion.",
                ],
                use_when=[
                    "A new project or phase needs shared authority, boundaries and measurable success conditions.",
                    "Several stakeholders interpret the business need differently and require one approved reference point.",
                ],
                avoid_when=[
                    "Using a charter as a substitute for detailed requirements, estimates or a delivery plan.",
                    "Allowing AI-generated objectives or dates to become commitments before sponsor review.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.pmi.org/-/media/pmi/documents/public/pdf/pmief/skills-for-life-english.pdf",
                ],
            ),
            dict(
                title="Identify Stakeholders and Plan Engagement",
                definition=(
                    "A stakeholder is a person, group or organisation that can affect, be affected by or perceive itself to be affected by the "
                    "project. Stakeholder planning combines identification, influence and interest analysis, impact, current and desired engagement, "
                    "information needs, decision rights and an owner for each engagement action."
                ),
                why=(
                    "A generic mailing list treats every stakeholder as if the same information and cadence were useful. Analysis helps the team "
                    "focus attention where decisions, adoption, resistance or operational impact matter, while avoiding unnecessary personal data."
                ),
                how=[
                    "Start with roles and legitimate project needs; collect only information necessary for engagement.",
                    "Map influence and interest, then record current versus desired engagement and the evidence for both.",
                    "Choose a strategy—manage closely, keep satisfied, keep informed or monitor—and assign an action owner.",
                    "Review the map at phase gates and when power, impact or sentiment changes.",
                ],
                example=[
                    "The service director has high influence and owns acceptance; the support agents have high impact and essential workflow knowledge.",
                    "The plan gives the director a fortnightly decision brief and the agents weekly design reviews with visible action tracking.",
                    "AI suggests message variants from role-based needs; the project manager checks tone and factual accuracy.",
                ],
                use_when=[
                    "Planning approvals, requirements discovery, change adoption, communications and escalation routes.",
                    "A project affects multiple functions with different concerns or decision rights.",
                ],
                avoid_when=[
                    "Inferring sensitive traits, private motivations or sentiment without evidence.",
                    "Treating a power-interest grid as permanent or as a substitute for direct conversation.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2020/03/advisory-guidelines-on-key-concepts-in-the-personal-data-protection-act",
                ],
            ),
            dict(
                title="Plan Scope with Requirements, Deliverables and a WBS",
                definition=(
                    "Scope planning converts needs into agreed requirements, deliverables, acceptance criteria and a work breakdown structure. "
                    "A WBS decomposes the total project scope into manageable work packages; its dictionary explains each package, owner, boundaries "
                    "and completion evidence. Decomposition describes outcomes before activities."
                ),
                why=(
                    "A schedule or budget built from vague nouns is fragile. The WBS creates a common reference for scope, schedule, cost, risk and "
                    "responsibility, while acceptance criteria make completion observable. GenAI can find gaps and propose decomposition, but the team "
                    "must confirm that the WBS covers exactly the approved scope."
                ),
                how=[
                    "Translate needs into requirements with source, priority, owner and verifiable acceptance criteria.",
                    "Decompose deliverables until a work package can be estimated, assigned, monitored and accepted.",
                    "Apply the 100-percent rule: children collectively represent the parent scope without unrelated work.",
                    "Create a requirements traceability view from need to requirement, deliverable, verification and acceptance.",
                ],
                example=[
                    "Deliverable 1.0 Portal Pilot decomposes into 1.1 Content, 1.2 Configuration, 1.3 Integration, 1.4 Testing and 1.5 Launch readiness.",
                    "Work package 1.4 has an owner, test environment, entry criteria, exit evidence and explicit exclusions.",
                    "AI critiques the hierarchy for overlap; the team resolves the final boundary.",
                ],
                use_when=[
                    "Building estimates, assigning ownership, controlling changes or defining acceptance.",
                    "Requirements need traceability across business, technical and operational work.",
                ],
                avoid_when=[
                    "Creating a task list with no deliverable hierarchy or acceptance evidence.",
                    "Accepting AI-created requirements that cannot be traced to an authorised stakeholder or source.",
                ],
                sources=[
                    "https://ntrs.nasa.gov/citations/20200000300",
                    "https://www.gao.gov/products/gao-20-195g",
                ],
            ),
            dict(
                title="Build a Credible Schedule and Cost Baseline",
                definition=(
                    "A credible schedule sequences the complete work, uses realistic durations, links dependencies, identifies resources and shows "
                    "the critical path and margin. A cost baseline time-phases approved estimates so planned value can later be compared with earned "
                    "value and actual cost. Both baselines depend on the same WBS."
                ),
                why=(
                    "A list of dates does not show whether the finish is achievable. Network logic reveals which delay matters, while documented "
                    "estimate assumptions make uncertainty discussable. GenAI may help normalise data or explore scenarios, but it must not invent "
                    "durations, rates or dependencies."
                ),
                how=[
                    "Sequence work packages with predecessors and successors; minimise unexplained constraints and open ends.",
                    "Estimate duration and cost from documented quantities, rates, analogous data or expert input; record confidence.",
                    "Calculate the longest dependent path and identify activities with zero or low float.",
                    "Time-phase costs, include authorised contingency where appropriate and obtain baseline approval.",
                ],
                example=[
                    "Content approval precedes portal configuration; integration test follows both configuration and test-data readiness.",
                    "The critical path runs through content approval, configuration, integration test and acceptance.",
                    "A two-week content delay moves the finish unless the team changes logic, scope or capacity through an approved decision.",
                ],
                use_when=[
                    "Testing whether a target date and budget are realistic and creating a performance reference.",
                    "Analysing the consequence of delay, resource limits or an approved change.",
                ],
                avoid_when=[
                    "Using fixed target dates as if they were estimates or hiding uncertainty in a single precise number.",
                    "Optimising a schedule generated by AI when its logic and source data have not been checked.",
                ],
                sources=[
                    "https://www.gao.gov/products/gao-16-89g",
                    "https://www.gao.gov/products/gao-20-195g",
                    "https://www.nasa.gov/ocfo/ppc-corner/ppc-guidance-documents/",
                ],
            ),
            dict(
                title="Integrate Quality, Resources, Communications, Risk and Procurement Plans",
                definition=(
                    "The project management plan is an integrated set of baselines and management approaches. Quality planning defines standards, "
                    "metrics and verification; resource planning defines roles, capacity and responsibility; communications planning matches message "
                    "to audience and decision; risk planning defines categories, thresholds and response ownership; procurement planning defines make-or-buy, "
                    "evaluation, contract and supplier controls."
                ),
                why=(
                    "Separate plans can conflict: a compressed schedule may require unavailable specialists; a low-cost supplier may not meet a quality "
                    "threshold; a reporting cadence may arrive after the decision it supports. Integration checks reveal these trade-offs before execution."
                ),
                how=[
                    "For each deliverable, link an owner, required capability, quality metric, verification method and acceptance authority.",
                    "Define communication purpose, audience, content, format, cadence, sender and escalation trigger.",
                    "Score threats and opportunities consistently; assign preventive, contingent and fallback actions with owners.",
                    "Document supplier evaluation criteria, lead times, interfaces and approval limits before requesting commitments.",
                ],
                example=[
                    "The portal needs accessibility review before acceptance; the specialist is available only in week 9.",
                    "The schedule reserves that window, procurement includes the review deliverable and the quality plan names the evidence.",
                    "The risk plan records a trigger and contingency if the specialist becomes unavailable.",
                ],
                use_when=[
                    "Consolidating component plans and checking whether delivery assumptions agree across functions.",
                    "Preparing the project for execution, governance review or supplier engagement.",
                ],
                avoid_when=[
                    "Producing isolated documents that do not trace to deliverables, dates, costs and owners.",
                    "Asking AI to choose a supplier, staff member or response without approved criteria and human review.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                    "https://standards.nasa.gov/standard/MSFC/MSFC-HDBK-3684",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Project Execution and Delivery with GenAI",
        subtitle=(
            "direct and manage work · knowledge and decisions · team and resources · "
            "quality · communications · stakeholder engagement · evidence-led status"
        ),
        weighting="Day 2 morning · 3 connected labs",
        concepts=[
            ("Work authorisation", "Translate the plan into owned work packages with inputs, constraints and completion evidence."),
            ("Team coordination", "Make responsibility, capacity, hand-offs, impediments and escalation routes visible."),
            ("Knowledge flow", "Capture decisions, rationale, assumptions and lessons where the team can reuse them."),
            ("Quality at source", "Prevent defects with clear criteria and peer checks instead of relying on late inspection."),
            ("Purposeful communication", "Design each update around the decision or action the audience needs."),
            ("Evidence-led reporting", "Separate facts, forecasts, decisions, risks and asks; never let narrative outrun the data."),
        ],
        sections=[
            dict(
                title="Direct and Manage Project Work",
                definition=(
                    "Directing and managing work means authorising planned work packages, coordinating execution, producing deliverables, handling issues "
                    "and implementing approved changes. The plan guides action, while actual results and work-performance data feed monitoring and decisions."
                ),
                why=(
                    "Execution fails when tasks are launched without clear outcomes, prerequisites or completion evidence. A work package brief creates a "
                    "bounded commitment and lets AI assist with sequencing, checklists and communication without redefining the approved scope."
                ),
                how=[
                    "Confirm the work package objective, owner, inputs, constraints, dependencies, due date and done criteria.",
                    "Authorise only work that is ready; make blockers and required decisions visible.",
                    "Update actual start, progress evidence, forecast finish, actual cost and issues at an agreed cadence.",
                    "Route any proposed baseline change through the change-control process before implementation.",
                ],
                example=[
                    "The configuration package starts only after content approval and environment access are confirmed.",
                    "The owner records evidence links and a forecast, not an unsupported percent-complete guess.",
                    "A new reporting feature is logged as a change request rather than inserted into active work.",
                ],
                use_when=[
                    "Converting an approved plan into short, owned units of delivery and coordinating dependencies.",
                    "Clarifying what can start, what is blocked and what evidence demonstrates completion.",
                ],
                avoid_when=[
                    "Starting work from an AI-generated list that has not been reconciled to the WBS and baseline.",
                    "Treating activity volume or polished status text as proof of deliverable progress.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://standards.nasa.gov/standard/MSFC/MSFC-HDBK-3684",
                ],
            ),
            dict(
                title="Manage Project Knowledge and Decisions",
                definition=(
                    "Project knowledge includes explicit records—plans, decisions, designs and lessons—and tacit experience held by people. Knowledge "
                    "management makes both usable through structured capture, context, ownership, retrieval and conversation. A decision log records the "
                    "decision, options, evidence, rationale, owner, date and review trigger."
                ),
                why=(
                    "Meeting summaries without decisions and owners create the illusion of documentation. GenAI can extract candidate actions and themes, "
                    "but source notes and participant confirmation are needed because a plausible summary can omit a condition or assign the wrong owner."
                ),
                how=[
                    "Capture source notes first; ask AI to separate decisions, actions, questions, assumptions and risks.",
                    "Confirm candidate records with the decision owner and participants before publishing.",
                    "Link each decision to affected requirements, work packages, risks and changes.",
                    "Record lessons during delivery with context and evidence, not only at closure.",
                ],
                example=[
                    "A design review chooses option B because it meets accessibility and lead-time constraints.",
                    "The log retains rejected options, evidence, decision owner and a review trigger if the supplier date changes.",
                    "The AI summary is corrected against the meeting notes before the action register is updated.",
                ],
                use_when=[
                    "Synthesising meetings, comparing options, onboarding team members or preserving rationale.",
                    "A project contains hand-offs, repeated decisions or knowledge that could be lost when people change.",
                ],
                avoid_when=[
                    "Recording confidential discussion in an unapproved service or treating an AI summary as the official record.",
                    "Capturing lessons as generic advice with no context, consequence or evidence.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices",
                ],
            ),
            dict(
                title="Acquire Resources and Manage the Team",
                definition=(
                    "Resource management matches required capability and capacity to scheduled work, then supports people to deliver together. A responsibility "
                    "view clarifies who is accountable, responsible, consulted and informed; a capacity view compares demand with realistic availability; a team "
                    "working agreement defines collaboration, escalation and decision norms."
                ),
                why=(
                    "A plan can look feasible while over-allocating the same specialist or ignoring operational duties. GenAI can highlight conflicts and draft "
                    "coaching questions, but staffing, performance and conflict decisions require context, fairness and accountable human judgement."
                ),
                how=[
                    "Map each work package to required capability, named owner, effort window and availability.",
                    "Resolve over-allocation by changing sequence, scope, capacity or date through authorised decisions.",
                    "Use short coordination cycles to surface impediments, hand-offs and support needs.",
                    "Address conflict through facts, interests, options and agreed action; do not infer personality or intent.",
                ],
                example=[
                    "The same accessibility specialist is needed by content and test work in week 9.",
                    "The team sequences the reviews and protects the critical-path activity rather than assuming parallel capacity.",
                    "The resource plan records the change and the stakeholder update explains the trade-off.",
                ],
                use_when=[
                    "Planning or rebalancing capacity, clarifying responsibility and coordinating cross-functional work.",
                    "A delivery delay may be caused by demand, skill or dependency rather than individual effort.",
                ],
                avoid_when=[
                    "Using AI to rank people, infer sensitive characteristics or make employment decisions.",
                    "Treating availability as 100 percent of working time or ignoring operational responsibilities.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                ],
            ),
            dict(
                title="Manage Quality and Deliverable Acceptance",
                definition=(
                    "Managing quality turns the quality plan into preventive practices, peer review, process checks, defect learning and improvement. Quality "
                    "control checks deliverable results against criteria; scope validation obtains formal acceptance from the authorised stakeholder. These are "
                    "related but distinct: a deliverable may meet an internal check yet still need customer acceptance."
                ),
                why=(
                    "Late inspection makes defects expensive and encourages subjective debate. Clear criteria and evidence let the team build quality into the "
                    "work. GenAI can create checklists and classify defects from approved records, but the criteria and acceptance decision remain human-owned."
                ),
                how=[
                    "Translate each requirement into measurable acceptance criteria and a verification method.",
                    "Use prevention, peer review and sampling during work; record defects with cause and corrective action.",
                    "Present the deliverable, evidence and known limitations to the authorised acceptance owner.",
                    "Capture accepted, conditionally accepted and rejected outcomes with actions and dates.",
                ],
                example=[
                    "The portal content must meet the agreed reading level, link integrity and accessibility checks.",
                    "A peer review catches missing alternative text before the acceptance demonstration.",
                    "The service director accepts the pilot after the evidence pack and two minor actions are recorded.",
                ],
                use_when=[
                    "Defining done, preventing rework, preparing a review or obtaining deliverable acceptance.",
                    "A quality dispute needs objective criteria, evidence and a named decision owner.",
                ],
                avoid_when=[
                    "Using an AI score as the sole evidence of quality or silently changing criteria after delivery.",
                    "Confusing completion of internal work with formal acceptance of the deliverable.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                ],
            ),
            dict(
                title="Manage Communications and Stakeholder Engagement",
                definition=(
                    "Communication management creates, distributes, stores and retrieves project information for a defined purpose. Stakeholder engagement "
                    "uses that information plus dialogue, participation and relationship actions to support decisions and adoption. Effective communication is "
                    "measured by understanding and action, not by the volume of messages sent."
                ),
                why=(
                    "The same status dump does not serve a sponsor, delivery team and affected user. GenAI is helpful for transforming one verified evidence "
                    "set into audience-specific drafts, provided that facts, uncertainty, tone and calls to action are checked before release."
                ),
                how=[
                    "Start with the audience decision or action; include only the evidence needed for it.",
                    "Separate completed facts, current forecast, variance, risks, decisions and asks.",
                    "Choose channel and cadence based on urgency, sensitivity, complexity and need for dialogue.",
                    "Confirm understanding, record decisions and update the engagement plan from observed response.",
                ],
                example=[
                    "The team receives a detailed blocker-and-owner view; the sponsor receives trend, tolerance, decision and recommendation.",
                    "Both versions use the same approved weekly data and preserve the same red status.",
                    "The project manager removes unsupported certainty from the AI draft before distribution.",
                ],
                use_when=[
                    "Preparing status updates, decision briefs, change communications or adoption conversations.",
                    "Several audiences need different levels of detail from the same verified source.",
                ],
                avoid_when=[
                    "Using AI to manufacture positive sentiment, conceal bad news or impersonate a stakeholder.",
                    "Sending generated text without checking names, figures, commitments and confidentiality.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://openai.com/academy/writing/",
                ],
            ),
            dict(
                title="Build Evidence-Led Status and Forecast Reporting",
                definition=(
                    "Evidence-led reporting reconciles approved baselines, a common status date and verified work, cost, quality, resource, risk, issue and "
                    "decision records before drafting a message. Earned value uses planned value (PV), earned value (EV) and actual cost (AC) at the same "
                    "cut-off: schedule variance SV = EV − PV, cost variance CV = EV − AC, SPI = EV ÷ PV and CPI = EV ÷ AC. Forecasts remain assumptions "
                    "until their method, remaining-work estimate and owner are explicit."
                ),
                why=(
                    "A polished status narrative can hide inconsistent dates, double-counted progress or unsupported optimism. A reconciled evidence table "
                    "makes calculations reproducible and separates completed fact, current variance, forecast, risk, decision and ask. GenAI may transform "
                    "the verified table for different audiences, but it must not calculate from mixed cut-offs or replace the project manager’s judgement."
                ),
                how=[
                    "Freeze one status date and reconcile baseline, completion evidence, actual cost, remaining duration, defects, capacity, risks, issues and decisions.",
                    "Calculate PV, EV and AC from approved records; derive SV, CV, SPI and CPI and show units, formulas and rounding.",
                    "Forecast EAC from an explicit assumption—for example BAC ÷ CPI when current cost efficiency is expected to continue—and record ETC and VAC.",
                    "Draft team and sponsor views from the same evidence table; keep status, variance and uncertainty identical while changing detail, decision and ask.",
                ],
                example=[
                    "At week 8, PV is SGD 72,000, EV is SGD 60,000, AC is SGD 66,000 and BAC is SGD 105,000.",
                    "SV is −SGD 12,000, CV is −SGD 6,000, SPI is 0.83 and CPI is 0.91; if CPI continues, EAC is SGD 115,500.",
                    "The status remains red in both audience versions; the sponsor brief adds the decision needed while the team view adds owners and next-cycle evidence.",
                ],
                use_when=[
                    "Preparing a weekly status pack, variance analysis, estimate at completion, recovery recommendation or decision brief.",
                    "Different audiences need a consistent view of progress, cost, forecast, risk and action from one verified cut-off.",
                ],
                avoid_when=[
                    "Calculating earned value from unapproved scope, mixed status dates or progress percentages that lack completion evidence.",
                    "Using AI narrative confidence to hide an adverse variance, omit uncertainty or make a forecast appear authorised.",
                ],
                sources=[
                    "https://www.gao.gov/products/gao-20-195g",
                    "https://www.gao.gov/products/gao-16-89g",
                    "https://www.pmi.org/standards/process-groups",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Manage Project Risks with GenAI",
        subtitle=(
            "risk and issue response · procurement · monitor and control work · integrated change · "
            "scope, schedule, cost, quality, resources, communications, stakeholders and closure"
        ),
        weighting="Day 2 afternoon · 3 connected labs",
        concepts=[
            ("Risk response", "Turn priority uncertainty into preventive action, triggers, contingencies, owners and residual exposure."),
            ("Integrated control", "Compare actual and forecast performance with approved baselines and explain the cause and consequence."),
            ("Change control", "Evaluate a proposed change across value, scope, schedule, cost, quality, resources, risk and contracts before deciding."),
            ("Forecast discipline", "Use transparent formulas and assumptions; treat AI narrative as a draft around verified numbers."),
            ("Acceptance and transition", "Close only after deliverables, obligations, handover, records and open actions have named owners."),
            ("Learning loop", "Capture reusable lessons with context, evidence and a future action, then feed them into the next project."),
        ],
        sections=[
            dict(
                title="Implement Risk Responses and Manage Issues",
                definition=(
                    "A risk is an uncertain event or condition that may affect objectives; an issue is a condition that has occurred and needs action. Response "
                    "planning selects a strategy, owner, preventive action, trigger, contingency and fallback. Implementation executes those actions and checks "
                    "whether exposure has changed or secondary risks have appeared."
                ),
                why=(
                    "A colourful risk register does not reduce exposure. Actionable records connect priority uncertainty to funded, scheduled work and decision "
                    "triggers. GenAI can challenge causes, consequences and response completeness, but probability, impact and ownership must be grounded in "
                    "project evidence."
                ),
                how=[
                    "Write cause–event–effect risk statements and distinguish them from current issues.",
                    "Score probability and impact with defined anchors; prioritise by exposure and risk tolerance.",
                    "Choose avoid, mitigate, transfer, accept or escalate for threats; exploit, enhance, share, accept or escalate for opportunities.",
                    "Track preventive action, trigger, contingency, residual exposure and owner at each review.",
                ],
                example=[
                    "Cause: supplier API access may be delayed; event: test access is unavailable by week 8; effect: integration testing and launch move.",
                    "Mitigation secures a sandbox date; trigger is no confirmed access by Friday; contingency uses a stub for non-production testing.",
                    "When access misses the trigger, the record becomes an issue and the contingency starts.",
                ],
                use_when=[
                    "Preparing risk reviews, selecting response actions or converting a triggered risk into issue work.",
                    "The team needs a consistent way to compare threats, opportunities and response urgency.",
                ],
                avoid_when=[
                    "Inventing probabilities from no data or asking AI to own a risk.",
                    "Listing vague concerns with no cause, effect, trigger, action, date or responsible owner.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                ],
            ),
            dict(
                title="Conduct and Control Procurements",
                definition=(
                    "Procurement management selects an appropriate sourcing approach, defines requirements and evaluation criteria, obtains authorised offers, "
                    "manages contract interfaces and monitors supplier performance. Project controls must include supplier deliverables, dependencies, costs, "
                    "risks, changes, acceptance and obligations."
                ),
                why=(
                    "The cheapest offer is not necessarily the best value, and an AI-generated comparison can hide missing criteria or inconsistent evidence. "
                    "A weighted decision matrix makes approved criteria and evidence visible while preserving accountable commercial judgement."
                ),
                how=[
                    "Confirm make-or-buy rationale, scope, acceptance, lead time, data handling, interfaces and decision authority.",
                    "Define weighted criteria and scoring anchors before reviewing offers.",
                    "Score only supplied evidence, record clarifications and apply required commercial and legal review.",
                    "Monitor supplier milestones, quality, invoices, risks, changes and closure obligations against the agreement.",
                ],
                example=[
                    "Three accessibility-review offers are compared on capability, approach, lead time, evidence and cost.",
                    "AI extracts comparable fields, but missing evidence receives no invented score and procurement validates the source.",
                    "The selected supplier's dates and acceptance evidence are integrated into the project baseline.",
                ],
                use_when=[
                    "Planning a purchase, comparing offers or monitoring external deliverables and obligations.",
                    "A supplier dependency affects the critical path, quality, risk or acceptance.",
                ],
                avoid_when=[
                    "Sharing confidential offers with an unapproved AI service or delegating the award decision to AI.",
                    "Changing supplier scope informally without authorised project and contract change records.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                ],
            ),
            dict(
                title="Monitor and Control Project Work",
                definition=(
                    "Monitoring and control compare actual and forecast results with the approved plan, analyse variance and trends, evaluate consequences and "
                    "recommend action. Useful control integrates scope, schedule, cost, quality, resources, risks, communications and supplier information at "
                    "a consistent status date."
                ),
                why=(
                    "Percent complete and traffic-light colours can obscure the basis of a forecast. Controls are credible when they use traceable source data, "
                    "defined thresholds and transparent calculations. GenAI may explain verified results and find contradictions, but it should not calculate "
                    "from ambiguous fields or rewrite a red condition as green."
                ),
                how=[
                    "Set one status date and collect actual starts, finishes, remaining duration, costs, completion evidence and open actions.",
                    "Compare against scope, schedule and cost baselines; identify cause, consequence, owner and corrective option.",
                    "Use trend and forecast measures with stated assumptions; keep source data and narrative linked.",
                    "Escalate forecast breaches and decisions according to tolerance and governance rules.",
                ],
                example=[
                    "At week 8: planned value is SGD 72,000, earned value SGD 60,000 and actual cost SGD 66,000.",
                    "Schedule performance index = 60/72 = 0.83; cost performance index = 60/66 = 0.91.",
                    "The project is behind plan and over cost for the work achieved; the report explains the integration-test dependency and recovery options.",
                ],
                use_when=[
                    "Preparing a status review, diagnosing variance or forecasting whether objectives remain achievable.",
                    "Several control dimensions must be reconciled before a decision.",
                ],
                avoid_when=[
                    "Using narrative confidence without source data, a status date or baseline reference.",
                    "Applying earned-value formulas when scope, schedule and cost are not integrated enough to support them.",
                ],
                sources=[
                    "https://www.gao.gov/products/gao-20-195g",
                    "https://www.gao.gov/products/gao-16-89g",
                    "https://www.nasa.gov/ocfo/ppc-corner/ppc-guidance-documents/",
                ],
            ),
            dict(
                title="Perform Integrated Change Control",
                definition=(
                    "Integrated change control records a proposed change, analyses its total impact, obtains a decision from the authorised body and updates "
                    "affected baselines and records only after approval. It also communicates the decision and verifies implementation. Change control protects "
                    "value and traceability; it is not a promise to reject change."
                ),
                why=(
                    "A small feature can alter design, testing, schedule, cost, support, supplier work and risk. GenAI is useful for building an impact checklist "
                    "and comparing options, but its proposal must be reconciled with the WBS, schedule, estimates, contracts and stakeholder evidence."
                ),
                how=[
                    "Log the request with reason, value, urgency, requester and affected requirement or deliverable.",
                    "Analyse options across scope, schedule, cost, quality, resources, risk, procurement, operations and benefits.",
                    "Recommend approve, reject, defer or request more information; record decision, authority and rationale.",
                    "After approval, update every affected baseline, plan, log, communication and work authorisation.",
                ],
                example=[
                    "A bilingual FAQ is requested in week 8. The analysis adds content, translation, accessibility checks and support training.",
                    "Option A adds SGD 9,000 and eight working days; option B pilots ten priority articles within tolerance.",
                    "The sponsor approves option B; scope, schedule, cost, risk and stakeholder records are updated together.",
                ],
                use_when=[
                    "A requirement, deliverable, baseline, contract or control threshold may change.",
                    "The team needs a traceable decision and coordinated update across project records.",
                ],
                avoid_when=[
                    "Implementing the request before authorisation or updating only the schedule while leaving scope and cost unchanged.",
                    "Treating an AI recommendation as approval or omitting rejected options and rationale.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://standards.nasa.gov/standard/MSFC/MSFC-HDBK-3684",
                ],
            ),
            dict(
                title="Control Scope, Schedule, Costs, Quality and Resources",
                definition=(
                    "Control maintains alignment between approved baselines and actual work. Scope control prevents unapproved expansion and preserves traceability; "
                    "schedule control updates logic and forecasts; cost control tracks actuals and estimates; quality control evaluates results; resource control "
                    "compares required and available capability. Corrective action is integrated because one dimension can shift another."
                ),
                why=(
                    "Local optimisation can worsen the whole project—for example, adding people may increase cost and coordination load without recovering a late "
                    "dependency. A control decision should state evidence, options, trade-offs and the authorised path."
                ),
                how=[
                    "Trace every current work item to approved scope and route additions through change control.",
                    "Update remaining duration and dependency logic before forecasting dates; analyse critical and near-critical paths.",
                    "Compare budget, actual cost, committed cost and estimate to complete using consistent cut-off dates.",
                    "Review defects, capacity, supplier results and risks together before recommending action.",
                ],
                example=[
                    "Integration testing is late because supplier access moved, not because test effort increased.",
                    "The team protects acceptance criteria, resequences training preparation and uses the authorised stub contingency.",
                    "The forecast, cost impact, residual risk and stakeholder message are updated from the same decision.",
                ],
                use_when=[
                    "Correcting performance, reforecasting, protecting scope or deciding how to use limited capacity.",
                    "A variance crosses tolerance or affects another baseline dimension.",
                ],
                avoid_when=[
                    "Changing a baseline to make current performance look acceptable.",
                    "Recommending action from one metric without analysing consequences for quality, risk, people and value.",
                ],
                sources=[
                    "https://www.gao.gov/products/gao-16-89g",
                    "https://www.gao.gov/products/gao-20-195g",
                    "https://standards.nasa.gov/standard/MSFC/MSFC-HDBK-3684",
                ],
            ),
            dict(
                title="Monitor Communications, Stakeholders and Risks",
                definition=(
                    "Monitoring checks whether communication is reaching the right people in time, whether stakeholder engagement is moving toward the desired "
                    "state and whether risk exposure and response effectiveness have changed. The team updates plans from evidence such as decisions delayed, "
                    "questions repeated, actions missed, sentiment expressed directly and triggers observed."
                ),
                why=(
                    "A communication can be sent yet fail to produce understanding or action. Stakeholder and risk conditions also change as delivery progresses. "
                    "GenAI can cluster feedback and surface contradictions from approved material, but it must not infer hidden motives or treat sentiment labels "
                    "as facts."
                ),
                how=[
                    "Compare planned and actual communication by audience, purpose, timing, reach and required action.",
                    "Review current versus desired engagement using direct evidence and update owners and actions.",
                    "Re-score risks after responses, identify emerging and secondary risks and close only when criteria are met.",
                    "Escalate when information, engagement or exposure crosses the defined threshold.",
                ],
                example=[
                    "Support agents repeat the same launch-readiness question, showing that the FAQ update did not create understanding.",
                    "The project replaces a one-way email with a live walkthrough and captures unresolved questions.",
                    "The adoption risk score and communication plan are updated after the session.",
                ],
                use_when=[
                    "Checking the effectiveness of a status cycle, change communication, adoption activity or risk response.",
                    "A stakeholder delay or misunderstanding threatens a milestone or acceptance.",
                ],
                avoid_when=[
                    "Inferring private attitudes from sparse text or storing unnecessary personal commentary.",
                    "Closing a risk because an action was completed without checking residual exposure.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2020/03/advisory-guidelines-on-key-concepts-in-the-personal-data-protection-act",
                ],
            ),
            dict(
                title="Close the Project or Phase",
                definition=(
                    "Closure confirms that approved work is complete or formally transferred, acceptance is recorded, contracts and obligations are settled, "
                    "operations can support the outcome, records are archived, remaining actions have owners and lessons are reusable. Closure may also document "
                    "an authorised early termination and its consequences."
                ),
                why=(
                    "A launch date is not the same as closure. Unaccepted deliverables, open supplier obligations, unsupported operations or undocumented decisions "
                    "create hidden work and risk. GenAI can help compile a closeout pack from verified records, but each acceptance, financial and contractual fact "
                    "needs an authoritative source."
                ),
                how=[
                    "Reconcile charter objectives, requirements, deliverables, acceptance records and approved changes.",
                    "Complete transition, support, data, access, supplier, financial and records-management actions.",
                    "Assign every residual action, risk and benefit measure to an operational owner with a date.",
                    "Capture lessons as context–action–result–recommendation and publish them where future teams can find them.",
                ],
                example=[
                    "The pilot is accepted with two minor actions transferred to the service owner and dated.",
                    "Supplier acceptance, final invoice, access removal, support runbook and benefits review are recorded.",
                    "A lesson about early content approval includes evidence, consequence and a reusable planning action.",
                ],
                use_when=[
                    "Completing a project or phase, transitioning ownership or documenting an authorised stop.",
                    "Preparing an evidence pack for sponsor confirmation and future project reuse.",
                ],
                avoid_when=[
                    "Declaring closure because the team stopped working or because an AI summary says all items are complete.",
                    "Leaving open actions, risks, benefits or support obligations without named operational owners.",
                ],
                sources=[
                    "https://www.pmi.org/standards/process-groups",
                    "https://www.pmi.org/-/media/pmi/documents/public/pdf/pmief/skills-for-life-english.pdf",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Initiate and Plan — establish evidence, authority and an integrated baseline",
    2: "Execute, Control and Close — deliver with traceable decisions and responsive controls",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:30", "9:50", 20, "admin", "Welcome, course orientation, scenario and responsible AI working agreement"),
                ("9:50", "10:35", 45, "topic", "Topic 1 — GenAI co-pilot method, initiation and charter concepts"),
                ("10:35", "10:50", 15, "break", "Tea break"),
                ("10:50", "12:00", 70, "lab", "Hands-on: " + lab_titles([1])),
                ("12:00", "13:00", 60, "topic", "Topic 1 — stakeholder, scope and engagement planning concepts"),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "15:20", 80, "lab", "Hands-on: " + lab_titles([2])),
                ("15:20", "15:35", 15, "break", "Tea break"),
                ("15:35", "16:35", 60, "topic", "Topic 1 — schedule, cost, quality, resources, risk and procurement planning"),
                ("16:35", "18:05", 90, "lab", "Hands-on: " + lab_titles([3])),
                ("18:05", "18:30", 25, "recap", "Day 1 LO1 recap, evidence review and Q&A"),
            ],
        ),
        2: (
            DAY_THEMES[2],
            [
                ("9:30", "10:10", 40, "topic", "Topic 2 — direct work, knowledge, resources and team concepts"),
                ("10:10", "11:00", 50, "lab", "Hands-on: " + lab_titles([4])),
                ("11:00", "11:15", 15, "break", "Tea break"),
                ("11:15", "12:00", 45, "lab", "Hands-on: " + lab_titles([5])),
                ("12:00", "13:00", 60, "lab", "Hands-on: " + lab_titles([6])),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "14:45", 45, "topic", "Topic 3 — risk, issue, procurement and integrated control concepts"),
                ("14:45", "15:35", 50, "lab", "Hands-on: " + lab_titles([7])),
                ("15:35", "15:50", 15, "break", "Tea break"),
                ("15:50", "16:30", 40, "topic", "Topic 3 — change, forecast, acceptance and closure concepts"),
                ("16:30", "17:20", 50, "lab", "Hands-on: " + lab_titles([8])),
                ("17:20", "18:10", 50, "lab", "Hands-on: " + lab_titles([9])),
                ("18:10", "18:30", 20, "recap", "LO2–LO4 recap, integrated portfolio check and next steps"),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="The Human-Owned GenAI Project System",
    concepts=[
        ("Ground", "Use approved project evidence and make the source boundary explicit."),
        ("Generate", "Ask for options, structures, critiques and transformations—not hidden authority."),
        ("Check", "Verify facts, calculations, commitments, confidentiality and uncertainty."),
        ("Decide", "Name the human owner, rationale, approval and update to the project record."),
    ],
    framework_title="One Integrated Project Loop",
    framework=[
        ("Initiate", "Authorise purpose, boundaries, stakeholders and decision rights."),
        ("Plan", "Integrate scope, schedule, cost, quality, resources, communications, risk and procurement."),
        ("Execute", "Authorise work, manage people and knowledge, produce and verify deliverables."),
        ("Control", "Compare evidence with baselines, respond to risk and decide changes."),
        ("Close", "Accept, transition, archive and convert experience into reusable lessons."),
    ],
    statement=dict(
        headline="AI accelerates project thinking; people own project truth.",
        body="Every generated output is a draft until its evidence, assumptions, calculations and authority are checked.",
        kicker="COURSE OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Initiation Pack", ["AI working agreement", "charter, assumptions and source ledger"]),
        ("Integrated Plan", ["stakeholder and communications plan", "scope, schedule, cost, quality, resource, risk and procurement baseline"]),
        ("Delivery System", ["work package and decision records", "quality, team and status evidence"]),
        ("Control & Closure", ["risk and change decisions", "acceptance, transition and lessons pack"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Open the verified synthetic project checkpoint from the prior lab.",
        "Run a bounded prompt against supplied evidence and preserve unknowns.",
        "Apply project-management logic, formulas and decision criteria.",
        "Perform a named human review and record the final decision.",
        "Test the artifact against observable checks and save the next checkpoint.",
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This guide teaches a human-owned method for using generative AI across the project life cycle. "
    "It follows the approved C013 topic spine: initiation and planning, execution and delivery, then "
    "risk, control and closure. The project-management concepts come first; the connected BeaconWorks "
    "portal labs then apply them to one synthetic project."
)
LG_INTRO2 = (
    "Use the guide as a reference after class. Each concept section explains what the practice is, why it "
    "matters, how it works, a worked example and situations in which the technique should or should not be "
    "used. Source links point to authoritative project, AI-risk and prompting guidance. All generated project "
    "content remains a draft until a named human owner checks and approves it."
)

LG_SETUP = dict(
    needs=[
        "A Windows or macOS laptop with a modern browser and spreadsheet application.",
        "Access to one organisation-approved generative AI assistant such as ChatGPT, Claude or Copilot.",
        "A text editor and the supplied synthetic files in labs/assets/.",
        "A local folder named C013-BeaconWorks-Project for all lab outputs.",
    ],
    verify_text=(
        "Create the project folder, open the supplied scenario files and confirm that you can save Markdown and CSV files. "
        "If no AI assistant is available, work with the provided prompt templates and complete the human-review steps manually."
    ),
    verify_code=(
        "C013-BeaconWorks-Project/\n"
        "  01-initiation/\n"
        "  02-planning/\n"
        "  03-delivery/\n"
        "  04-control/\n"
        "  05-closure/"
    ),
    conventions=[
        "Replace placeholders such as <SOURCE> and <STATUS_DATE>; never paste placeholder brackets into a final record.",
        "Use only the synthetic evidence supplied with the labs or information you are authorised to process.",
        "Mark FACT, ASSUMPTION, OPTION and UNKNOWN explicitly in material AI outputs.",
        "Save both the AI draft and the human-approved version when a decision or baseline is affected.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. "
    "Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. "
    "A named human owner verifies every figure, commitment and decision."
)

LG_WRAPUP = dict(
    title="Wrap-Up — Operate the Integrated System",
    intro=(
        "The nine labs produce one connected project evidence set. The value is not a collection of prompts; "
        "it is the traceability from business need to authorised plan, delivery evidence, control decision and closure."
    ),
    sections=[
        dict(
            title="The Four Control Questions",
            text="At every project review, ask the same four questions and point to evidence.",
            bullets=[
                "What was approved, and where is that baseline or decision recorded?",
                "What has actually happened as of one status date?",
                "What is now forecast, and which assumptions or risks drive it?",
                "Who must decide or act next, by when, and what record will change?",
            ],
        ),
        dict(
            title="A Safe GenAI Handoff",
            text="Before reusing a project prompt or artifact in the workplace, adapt it to organisational controls.",
            bullets=[
                "Confirm approved tools, data classes, retention, access and review requirements.",
                "Replace synthetic scenario values only with authorised source records.",
                "Test prompts on representative examples and preserve a manual fallback.",
                "Assign an owner for accuracy, decisions, monitoring and continuous improvement.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Select one low-risk project artifact—such as a source-led meeting summary—and apply the C-O-S-T-A-R prompt pattern.",
    "Define the evidence, human review and record-update steps before using GenAI on a live project.",
    "Track one quality measure such as unsupported claims found, editing time or action-owner corrections.",
    "After three uses, review failures and update the prompt, checklist and organisational guidance.",
]

LG_GLOSSARY = [
    ("Acceptance criteria", "Observable conditions a deliverable must satisfy for the authorised stakeholder to accept it."),
    ("Actual cost (AC)", "Cost incurred for the work performed as of the status date."),
    ("Assumption", "A factor treated as true for planning that requires validation or a response if it changes."),
    ("Baseline", "The approved version of scope, schedule or cost used for comparison and control."),
    ("Change request", "A documented proposal to modify a deliverable, baseline, plan or controlled record."),
    ("Cost performance index (CPI)", "Earned value divided by actual cost; a ratio below 1.0 indicates more cost was spent than value earned."),
    ("Critical path", "The longest dependent path through the schedule that determines the earliest finish under current logic."),
    ("Earned value (EV)", "Budgeted value of work actually completed as of the status date."),
    ("GenAI", "Generative artificial intelligence that creates content from instructions and context."),
    ("Issue", "A condition that has occurred and requires action or decision."),
    ("Planned value (PV)", "Budgeted value of work planned to be complete as of the status date."),
    ("Prompt", "The instruction, context, sources, constraints and desired output given to an AI assistant."),
    ("RACI", "A responsibility view identifying Responsible, Accountable, Consulted and Informed roles."),
    ("Risk", "An uncertain event or condition that may positively or negatively affect project objectives."),
    ("Schedule performance index (SPI)", "Earned value divided by planned value; a ratio below 1.0 indicates less work completed than planned."),
    ("Source ledger", "A table linking material facts and generated claims to authoritative project evidence."),
    ("Stakeholder", "A person, group or organisation that can affect, be affected by or perceive an effect from the project."),
    ("Status date", "The common cut-off date for actuals, progress, variance and forecast information."),
    ("Work breakdown structure (WBS)", "A deliverable-oriented decomposition of the complete project scope."),
    ("Work package", "A manageable WBS component that can be estimated, assigned, monitored and accepted."),
]

TRAINER_TEAM = [
    (
        "Assigned Tertiary Infotech Academy Trainer",
        "Project-management and generative-AI facilitator who guides evidence-led planning, "
        "delivery, control and hands-on application to the synthetic BeaconWorks scenario.",
    ),
]

VERSION_HISTORY = [
    (
        "1.0",
        VERSION_DATE,
        "Initial aligned release of the slide deck, Learner Guide, Lesson Plan and nine connected labs.",
        TRAINER,
    ),
]
