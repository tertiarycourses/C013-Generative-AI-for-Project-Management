"""Topic 2 connected labs: execution and delivery."""

DOMAIN2 = [
    dict(
        num=4,
        topic=2,
        title="Turn the Baseline into an Executable Delivery System",
        duration=50,
        objective="LO2: direct and manage project work with owned work packages, dependencies and completion evidence",
        goal="Create a ready-to-run delivery board and authorise one bounded work package.",
        workflow=["Confirm readiness", "Authorise work", "Track evidence", "Log decisions"],
        desc=(
            "You will transform the frozen Baseline v1.0 into a delivery board without changing its scope or dates. "
            "The exercise distinguishes planned, ready, active, blocked and done work, then creates a detailed brief "
            "for portal configuration with prerequisites, acceptance evidence and escalation rules."
        ),
        build=(
            "03-delivery/delivery-board.csv, work-package-brief-WP-04.md and decision-log.csv that translate the "
            "baseline into controlled execution records."
        ),
        services="Spreadsheet · text editor · approved AI assistant · Lab 3 baseline · delivery-events.md",
        prerequisites=[
            "Frozen wbs-and-baseline.csv and integrated-management-plan.md from Lab 3.",
            "Open labs/assets/delivery-events.md and read Events E01–E03 only.",
            "Do not implement or approve a baseline change in this lab.",
        ],
        steps=[
            (
                "Copy the ten work-package rows from wbs-and-baseline.csv into 03-delivery/delivery-board.csv. Add "
                "Status, Readiness_Evidence, Actual_Start, Actual_Finish, Forecast_Finish, Percent_Complete_Method, "
                "Progress_Evidence, Blocker, Next_Action, Action_Owner and Escalation_Date. Set Status to Planned until "
                "the predecessor, input, owner and environment checks are supported.",
                "Allowed status: Planned | Ready | Active | Blocked | Done\n"
                "Readiness gate: predecessor complete · approved input available · owner confirmed · environment available",
            ),
            (
                "Use delivery event E01 to update WP-01 through WP-03. Mark only work supported by the event as Done, "
                "Active or Ready and link its evidence label. For active work, define progress by completed acceptance "
                "items or verified sub-deliverables; do not enter a subjective percentage.",
                "Progress evidence examples: approved requirements record · accepted content batch · reviewed design artifact\n"
                "Rule: activity or effort alone is not deliverable progress.",
            ),
            (
                "Create work-package-brief-WP-04.md for Portal configuration with Objective, Scope boundary, Inputs, "
                "Predecessors, Owner, Contributors, Start gate, Planned duration, Cost budget, Quality checks, Acceptance "
                "evidence, Risks, Communication, Done criteria and Escalation. Ask the assistant for a draft using only "
                "the baseline and E01, then reconcile every field to those records.",
                "Draft a bounded WP-04 brief from <BASELINE ROW> and <EVENT E01> only.\n"
                "Use UNKNOWN for missing data. Do not add features or change dates.\n"
                "Finish with Source field | Used value | Evidence | Human check.",
            ),
            (
                "Create decision-log.csv with columns Decision_ID, Date, Question, Options, Evidence, Decision, Rationale, "
                "Decision_Owner, Affected_Records, Review_Trigger and Status. Record the E02 environment-access decision "
                "as Pending decision. Ask the assistant to produce three options, then remove any option that violates the "
                "charter or baseline and record the human-approved recommendation separately.",
                "Decision analysis: Option | Benefits | Drawbacks | Scope impact | Schedule impact | Cost impact | Risk | Evidence\n"
                "Status remains Pending decision until the named owner confirms it.",
            ),
            (
                "Apply event E03 to the board. If the event is an unapproved feature request, add Blocker or Next_Action "
                "as Log change request and leave baseline fields unchanged. Run a trace check from each active row to WBS, "
                "owner, predecessor, cost, quality evidence and communication record.",
                "Trace check result per active row: WBS PASS/REPAIR · Owner PASS/REPAIR · Logic PASS/REPAIR · "
                "Cost PASS/REPAIR · Evidence PASS/REPAIR · Communication PASS/REPAIR",
            ),
        ],
        test=(
            "The board must contain the same ten work packages, baseline durations and costs as Baseline v1.0. Every "
            "Ready or Active row must have readiness evidence, owner, next action and objective progress evidence. The "
            "WP-04 brief must contain all 15 requested sections and no added scope. The decision log must contain E02 as "
            "Pending decision with at least two viable options, and E03 must be routed to a change request without editing "
            "the baseline."
        ),
        checkpoint=(
            "Keep all three delivery records. Lab 5 adds team, knowledge and quality controls; Lab 6 uses the board as "
            "the status source. To rejoin, copy Baseline v1.0 and apply only delivery events E01–E03."
        ),
        troubleshooting=[
            (
                "Several rows appear ready even though a predecessor is incomplete.",
                "Apply the readiness gate row by row and return unsupported work to Planned.",
            ),
            (
                "Percent complete is a confident number without evidence.",
                "Replace it with completed acceptance items, verified quantities or a forecast based on remaining work.",
            ),
            (
                "The feature request appears inside WP-04.",
                "Remove it, log a change request and preserve the original work-package boundary.",
            ),
        ],
        challenge=(
            "Create a filtered view showing only work that can start in the next five working days. Explain the exact "
            "readiness evidence for each selected row and why every excluded row is not yet ready."
        ),
        reflection=(
            "Which field most clearly separated an authorised work package from a plausible AI-generated task list?"
        ),
    ),
    dict(
        num=5,
        topic=2,
        title="Manage Team Knowledge, Quality and Stakeholder Delivery",
        duration=45,
        objective="LO2: resolve delivery challenges through explicit capacity, knowledge, quality and engagement controls",
        goal="Turn live delivery events into owned team actions, verified quality records and confirmed project knowledge.",
        workflow=["Reconcile capacity", "Extract knowledge", "Control quality", "Update engagement"],
        desc=(
            "You will process synthetic capacity, meeting and defect evidence without inferring people’s intent. GenAI "
            "will extract candidate decisions and actions, while you confirm them against the source and update the "
            "resource, decision, quality and stakeholder records."
        ),
        build=(
            "03-delivery/resource-and-raci-plan.csv, quality-and-acceptance-log.csv, meeting-record-ai-draft.md, "
            "meeting-record.md, stakeholder-engagement-update.md and delivery-handoff-checklist.md with confirmed owners and evidence."
        ),
        services="Spreadsheet · text editor · approved AI assistant · delivery-events.md · Lab 2–4 records",
        prerequisites=[
            "Delivery board and decision log from Lab 4.",
            "Stakeholder register and communications plan from Lab 2.",
            "Open delivery-events.md and use Events E04–E07 only.",
            "Use the five preformatted Lab 5 starter files in labs/assets so the 45-minute exercise focuses on evidence and decisions.",
        ],
        steps=[
            (
                "(8 minutes) Copy lab-05-resource-raci-starter.csv to 03-delivery/resource-and-raci-plan.csv. Keep one row "
                "per Resource_Role; list every related work package in Affected_Work_Packages. Complete Responsible, Accountable, "
                "Consulted, Informed, "
                "Capability_Needed, Planned_Effort_Days, Available_Effort_Days, Variance_Days, Conflict, Resolution_Option "
                "and Human_Decision. Enter the supplied capacity values from E04 and calculate Variance_Days as available "
                "minus planned. Mark negative values as conflicts.",
                "Variance_Days = Available_Effort_Days - Planned_Effort_Days\n"
                "Conflict = YES when Variance_Days < 0\n"
                "Resolution options: resequence · reduce approved scope via change · add authorised capacity · change date",
            ),
            (
                "(10 minutes) Copy lab-05-meeting-record-starter.md to 03-delivery/meeting-record-ai-draft.md. Paste meeting "
                "note E05 into the assistant and request candidate Decisions, Actions, Questions, Assumptions, Risks and "
                "Lessons with exact source quotations of no more than 12 words. Save the response in that draft file, compare "
                "each item with E05, then save the corrected human-reviewed version as 03-delivery/meeting-record.md with "
                "Confirmed or Pending confirmation status.",
                "Extract only what the note supports.\n"
                "Return Type | Candidate record | Owner | Date | Evidence excerpt | Confirmation needed.\n"
                "Do not infer agreement, sentiment or an owner not named in the note.",
            ),
            (
                "(10 minutes) Add confirmed decisions to decision-log.csv. Copy lab-05-quality-acceptance-starter.csv to "
                "03-delivery/quality-and-acceptance-log.csv with Deliverable_ID, "
                "Requirement_ID, Criterion, Verification_Method, Result, Evidence, Defect_ID, Severity, Corrective_Action, "
                "Action_Owner, Due and Acceptance_Status. Enter E06 and E07 exactly; keep quality result separate from "
                "stakeholder acceptance.",
                "Quality result: Meets | Does not meet | Not checked\n"
                "Acceptance status: Pending | Accepted | Accepted with actions | Not accepted\n"
                "A completed internal check does not equal stakeholder acceptance.",
            ),
            (
                "(8 minutes) Copy lab-05-stakeholder-engagement-update-starter.md to "
                "03-delivery/stakeholder-engagement-update.md. Compare the support agents’ current and desired state with the "
                "evidence in E05–E07. Record Observation, Evidence, Consequence, Updated action, Owner, Trigger and Feedback "
                "method. Do not label attitude; describe observable participation, questions, delays or decisions.",
                "Acceptable observation: 'Three workflow questions remain open after the review.'\n"
                "Not acceptable: 'The team is resistant.' unless direct, appropriate evidence and context support it.",
            ),
            (
                "(9 minutes) Ask the assistant to critique the four outputs for contradictions in owner, date, status and evidence. "
                "Resolve each contradiction against the source event. Copy lab-05-delivery-handoff-checklist-starter.md to "
                "03-delivery/delivery-handoff-checklist.md and complete its seven rows: "
                "capacity, decision, action, defect, acceptance, stakeholder update and controlled-record link.",
                "Contradiction table: Field | File A | File B | Source evidence | Human resolution | Updated files\n"
                "Handoff result: seven items each marked READY or ACTION with owner and due date.",
            ),
        ],
        test=(
            "The resource plan must use one row per resource role and show these E04 results: Accessibility Specialist -2/YES, "
            "Integration Engineer 0/NO, Content Lead -2/YES and Support Lead +1/NO for Variance_Days/Conflict. The meeting record "
            "must classify at least one decision, action, question, assumption, risk and lesson, each with evidence and "
            "confirmation status. The quality log must keep verification result separate from acceptance status and include "
            "owners for all corrective actions. The engagement update must use observable evidence and the handoff checklist "
            "must be saved as 03-delivery/delivery-handoff-checklist.md and contain all seven required items."
        ),
        checkpoint=(
            "Keep the corrected delivery records. Lab 6 uses confirmed decisions, defects, capacity conflicts and actions "
            "in the weekly status pack. To rejoin, reprocess E04–E07 and mark uncertain extraction Pending confirmation."
        ),
        troubleshooting=[
            (
                "RACI has more than one accountable role for a work package.",
                "Escalate the ambiguity and name one final accountable decision owner in Human_Decision.",
            ),
            (
                "The summary assigns an action to someone not named in the note.",
                "Set Owner to UNASSIGNED and add a Pending confirmation action.",
            ),
            (
                "A deliverable is marked accepted after an internal check.",
                "Change Acceptance_Status to Pending until the authorised stakeholder records acceptance.",
            ),
        ],
        challenge=(
            "Propose a resource resolution that protects the 28-day baseline, then state the cost, quality, coordination "
            "and risk assumptions that would need approval before it could be used."
        ),
        reflection=(
            "Which source check prevented the largest error in the meeting, resource or quality record?"
        ),
    ),
    dict(
        num=6,
        topic=2,
        title="Build the Evidence-Led Project Status Pack",
        duration=60,
        objective="LO2: communicate project delivery status and budget challenges from verified work-performance evidence",
        goal="Calculate project performance and produce audience-specific updates that preserve one version of the facts.",
        workflow=["Set status date", "Calculate variance", "Forecast outcome", "Tailor the message"],
        desc=(
            "You will reconcile the baseline, delivery board and supplied week-8 update. You will calculate schedule and "
            "cost indicators in the spreadsheet before asking GenAI to draft narrative. The final pack distinguishes fact, "
            "forecast, risk, decision and ask for both sponsor and team audiences."
        ),
        build=(
            "03-delivery/week-08-performance.csv and week-08-status-pack.md containing transparent calculations, "
            "source links, a sponsor decision brief and a delivery-team action view."
        ),
        services="Spreadsheet · text editor · approved AI assistant · weekly-update-inputs.md · Lab 3–5 records",
        prerequisites=[
            "Frozen Baseline v1.0, current delivery board, decision log, quality log and resource plan.",
            "Open labs/assets/weekly-update-inputs.md and use the stated week-8 cut-off only.",
            "Use the work budget BAC of SGD 105,000; keep contingency outside earned-value calculations.",
        ],
        steps=[
            (
                "Create week-08-performance.csv with Metric, Formula, Input_A, Input_B, Result, Unit, Source and Human_Check. "
                "Enter PV 72000, EV 60000, AC 66000 and BAC 105000 from the supplied update. Calculate SV, CV, SPI, CPI, "
                "EAC using BAC/CPI, ETC using EAC-AC and VAC using BAC-EAC. Round ratios to two decimals and currency to "
                "the nearest dollar.",
                "SV = EV - PV\nCV = EV - AC\nSPI = EV / PV\nCPI = EV / AC\n"
                "EAC = BAC / CPI\nETC = EAC - AC\nVAC = BAC - EAC",
            ),
            (
                "Reconcile supplied milestone, defect, capacity, risk, issue and decision information with the current "
                "project records. In week-08-status-pack.md create an Evidence table with Evidence_ID, Status_Date, Fact, "
                "Source, Owner and Confidence. Record contradictions as Open data issue rather than choosing the more "
                "favourable value.",
                "One status date: Week 8 Friday 17:00\n"
                "Evidence classes: COMPLETED FACT | CURRENT CONDITION | FORECAST | RISK | ISSUE | DECISION | ASK",
            ),
            (
                "Before using AI, write the overall status from the agreed thresholds: Red if SPI or CPI is below 0.90, "
                "or an approved milestone is forecast to breach by more than three working days without an authorised "
                "recovery; Amber for an emerging tolerance threat; Green only when within tolerance. State the threshold "
                "and evidence used.",
                "Expected calculations: SPI 0.83 · CPI 0.91 · EAC SGD 115,500 · VAC -SGD 10,500\n"
                "Expected schedule forecast: 32 working days versus 28-day baseline",
            ),
            (
                "Give the assistant only the verified Evidence table and performance rows. Request two drafts: a sponsor "
                "brief with Outcome, Trend, Tolerance, Cause, Consequence, Options, Recommendation and Decision needed; "
                "and a team view with completed work, blocked work, next actions, owners and dates. Require the same status, "
                "figures and forecast in both.",
                "Use only <VERIFIED STATUS DATA>.\n"
                "Do not soften Red, change a figure or invent a cause.\n"
                "Draft A: sponsor decision brief, 180 words maximum.\n"
                "Draft B: team action view, table format.\n"
                "Finish with Claim | Evidence_ID | Classification.",
            ),
            (
                "Review every generated claim against the evidence and save the corrected versions. Add a Decision request "
                "that names the owner, latest decision date, options, recommendation and consequence of no decision. Add a "
                "next-cycle data checklist for progress evidence, actual cost, remaining duration, defects, capacity, risks, "
                "issues, supplier status and stakeholder feedback.",
                "Decision request: owner · decision · due · options · recommendation · no-decision consequence\n"
                "Next-cycle checklist: nine evidence categories each with source owner and cut-off time",
            ),
        ],
        test=(
            "The spreadsheet must show SV -SGD 12,000, CV -SGD 6,000, SPI 0.83, CPI 0.91, EAC SGD 115,500, ETC "
            "SGD 49,500 and VAC -SGD 10,500. The pack must show a 32-day forecast against the 28-day baseline, apply the "
            "stated status threshold consistently, contain source IDs for every material claim, preserve identical facts "
            "across sponsor and team views, and include a complete decision request plus nine-item next-cycle checklist."
        ),
        checkpoint=(
            "Freeze the verified week-8 calculations and evidence table. Lab 7 uses the status risks and supplier data; "
            "Lab 8 uses the forecast and decision structure. To rejoin, reproduce the expected calculations before drafting narrative."
        ),
        troubleshooting=[
            (
                "EAC is calculated from the authorised total including contingency.",
                "Use the SGD 105,000 work budget BAC for earned value and show contingency separately.",
            ),
            (
                "The AI draft changes Red to Amber.",
                "Restore Red from the agreed rule and tell the assistant that status is a fixed input, not a writing choice.",
            ),
            (
                "Two files report different actual cost.",
                "Record an Open data issue, name the source owner and do not publish a resolved figure until reconciled.",
            ),
        ],
        challenge=(
            "Calculate an alternative EAC using AC + (BAC-EV) and explain which performance assumption differs from BAC/CPI. "
            "Do not replace the official forecast without an authorised decision."
        ),
        reflection=(
            "Which part of the status pack required the most human judgement after the calculations were fixed?"
        ),
    ),
]
