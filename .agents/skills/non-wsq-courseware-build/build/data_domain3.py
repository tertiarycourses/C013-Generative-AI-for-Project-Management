"""Topic 3 connected labs: risk, control, change and closure."""

DOMAIN3 = [
    dict(
        num=7,
        topic=3,
        title="Build the Risk, Issue and Procurement Response Cockpit",
        duration=50,
        objective="LO3: anticipate and implement risk, issue and supplier responses from verified evidence",
        goal="Convert priority uncertainty and supplier evidence into owned, triggered and measurable response actions.",
        workflow=["Refresh exposure", "Trigger responses", "Score offers", "Integrate actions"],
        desc=(
            "You will refresh the initial risk register at the week-8 status date, distinguish triggered risks from "
            "current issues and compare three synthetic accessibility-review offers against criteria written in Lab 3. "
            "GenAI may structure evidence and challenge gaps, but final scores, owners and recommendation remain human-owned."
        ),
        build=(
            "04-control/risk-issue-cockpit.csv, procurement-comparison.csv and response-brief.md with current exposure, "
            "triggered actions, weighted supplier evidence and integrated project impacts."
        ),
        services="Spreadsheet · text editor · approved AI assistant · risk-issue-inputs.csv · vendor-bids.csv",
        prerequisites=[
            "Initial risk register and procurement-evaluation-plan.csv from Lab 3.",
            "Verified week-8 evidence table and status pack from Lab 6.",
            "Open labs/assets/risk-issue-inputs.csv and labs/assets/vendor-bids.csv.",
        ],
        steps=[
            (
                "Copy the initial risks into 04-control/risk-issue-cockpit.csv and add Status_Date, Current_Status, "
                "Trigger_Result, Response_Action_Status, Issue_ID, Issue_Action, Action_Owner, Due, Residual_Probability, "
                "Residual_Impact and Residual_Exposure. Apply the week-8 update rows from risk-issue-inputs.csv. A risk "
                "becomes an issue only when the stated condition has occurred.",
                "Risk lifecycle: Open → Triggered → Response active → Closed\n"
                "Issue lifecycle: Open → Action active → Resolved → Closed\n"
                "Residual_Exposure = Residual_Probability × Residual_Impact",
            ),
            (
                "Ask the assistant to critique each cause–event–effect statement, trigger and response using only the "
                "cockpit and status evidence. Request missing fields and contradictions, not replacement scores. Make the "
                "final current and residual scores yourself; for each triggered item record the preventive action outcome, "
                "contingency start, owner, due date and secondary risk.",
                "Return Risk_ID | Structural gap | Evidence | Consequence | Repair question.\n"
                "Do not invent probability, impact, trigger evidence or owner.\n"
                "Separate a future uncertain event from a condition that has already occurred.",
            ),
            (
                "Copy vendor-bids.csv to procurement-comparison.csv. Add the five approved criterion scores from the "
                "evidence using the 1, 3 and 5 anchors written in Lab 3. Calculate Weighted_Total as the sum of Score × "
                "Weight divided by 100. Record Missing_Evidence, Clarification, Commercial_Review and Human_Recommendation. "
                "Do not change criteria after seeing the offers.",
                "Weighted_Total = Σ(criterion score × criterion weight) / 100\n"
                "Expected evidence-based totals: Vendor A 3.90 · Vendor B 4.10 · Vendor C 3.70",
            ),
            (
                "Create response-brief.md with sections Status date, Top exposure, Triggered responses, Current issues, "
                "Supplier comparison, Recommendation, Project impacts, Decisions and Monitoring. Recommend Vendor B for "
                "authorised commercial review because it has the highest evidence-based total; do not call it awarded. "
                "Link supplier lead time, cost and data handling to the schedule, budget, quality and risk records.",
                "Recommendation wording: 'Recommend Vendor B for authorised commercial review, subject to clarification "
                "and required approval.'\n"
                "Impact dimensions: scope · schedule · cost · quality · resources · data · risk · communications",
            ),
            (
                "Run a cockpit completeness check. Every high exposure or current issue must have one owner, one next action, "
                "one due date and one review point. Every supplier score must cite a bid field. Add a monitoring calendar "
                "with daily issue follow-up until stabilised, weekly risk review and supplier milestone checks.",
                "Completeness: evidence · status · action · owner · due · residual exposure · review date\n"
                "Supplier trace: criterion score → bid field → anchor → human reviewer",
            ),
        ],
        test=(
            "All five initial risks must appear in the cockpit, with week-8 status, trigger result, current or residual "
            "exposure, owned action and review point. Conditions that have occurred must have Issue_IDs and must not remain "
            "worded only as future uncertainty. Procurement weights must remain unchanged and totals must be Vendor A 3.90, "
            "Vendor B 4.10 and Vendor C 3.70. The response brief must recommend—not award—Vendor B, integrate eight impact "
            "dimensions and contain the stated monitoring cadence."
        ),
        checkpoint=(
            "Keep the cockpit, comparison and response brief. Lab 8 uses the current exposures, supplier recommendation "
            "and week-8 forecast in a change decision. To rejoin, reproduce the three weighted totals before making a recommendation."
        ),
        troubleshooting=[
            (
                "A triggered risk and its resulting issue are duplicated with different owners.",
                "Link them with Issue_ID, retain the risk for residual exposure and name one coordinated response owner.",
            ),
            (
                "The assistant scores missing supplier evidence as average.",
                "Use the prewritten anchor; record missing evidence and request clarification instead of inventing a score.",
            ),
            (
                "The highest-scoring offer is described as awarded.",
                "Change the status to Recommended for commercial review until the authorised process records a decision.",
            ),
        ],
        challenge=(
            "Recalculate totals if lead-time weight rises from 20 to 30 and cost falls from 15 to 5. Explain why that "
            "scenario is sensitivity analysis, not permission to change the approved criteria after bids were opened."
        ),
        reflection=(
            "Which risk or supplier conclusion changed most after evidence, trigger and scoring anchors were made explicit?"
        ),
    ),
    dict(
        num=8,
        topic=3,
        title="Run Integrated Change Control and Baseline Impact Analysis",
        duration=50,
        objective="LO3: evaluate and decide a project change across all affected controls with GenAI support",
        goal="Process CR-004 from request through impact analysis, authorised decision and coordinated record update.",
        workflow=["Log the request", "Analyse options", "Record the decision", "Update controlled records"],
        desc=(
            "You will evaluate a request for bilingual pilot content at week 8. The exercise prevents a useful feature "
            "from bypassing scope, schedule, cost, quality, resource, risk, supplier, communication and operational review. "
            "You will model options, record the synthetic sponsor decision and publish a traceable Baseline v1.1."
        ),
        build=(
            "04-control/change-log.csv, change-impact-analysis-CR-004.md, baseline-v1.1.csv and "
            "change-implementation-checklist.md with an approved, fully traced incremental change."
        ),
        services="Spreadsheet · text editor · approved AI assistant · change-request-CR-004.md · Labs 3, 6 and 7 records",
        prerequisites=[
            "Frozen Baseline v1.0 and verified week-8 status evidence.",
            "Risk-issue cockpit and procurement response brief from Lab 7.",
            "Open labs/assets/change-request-CR-004.md and separate Request evidence from Sponsor decision record.",
            "Use the four preformatted Lab 8 starter files in labs/assets; do not recreate their schemas.",
        ],
        steps=[
            (
                "(6 minutes) Copy lab-08-change-log-starter.csv to 04-control/change-log.csv with Change_ID, Date_Logged, "
                "Requester, Reason, Requested_Outcome, Urgency, "
                "Affected_Requirement, Status, Decision_Owner, Decision_Date, Decision, Rationale and Implementation_Status. "
                "Enter CR-004 from the Request section only and set Status to Analysing.",
                "Status: Logged | Analysing | More information | Approved | Rejected | Deferred | Implemented | Verified\n"
                "Do not copy the sponsor decision until impact analysis is complete.",
            ),
            (
                "(12 minutes) Copy lab-08-change-impact-analysis-starter.md to "
                "04-control/change-impact-analysis-CR-004.md. Complete the current baseline and four options: reject, defer, full "
                "30-article change and ten-priority-article pilot. Ask the assistant to propose an impact checklist, then "
                "complete it from project evidence across value, scope, schedule, cost, quality, resources, risk, supplier, "
                "communications, operations, benefits and alternatives.",
                "For each option return: value · scope delta · WBS delta · duration · cost · quality evidence · resource "
                "need · risk · supplier · communication · operational effect · assumptions · recommendation.\n"
                "Use UNKNOWN when the project record is silent.",
            ),
            (
                "(10 minutes) Calculate the two implementation options. Confirm that full scope adds SGD 9,000 and eight working days. "
                "Confirm that the pilot adds SGD 3,500 and three working days. Compare each with the authorised budget, "
                "remaining contingency, week-8 forecast, available translation capacity and acceptance evidence. Recommend "
                "the pilot with explicit residual risk and benefit limits.",
                "Full option: +SGD 9,000 · +8 working days\n"
                "Pilot option: +SGD 3,500 · +3 working days\n"
                "Pilot revised work budget = SGD 108,500\n"
                "Remaining contingency = SGD 11,500\n"
                "Pilot revised baseline duration = 31 working days",
            ),
            (
                "(12 minutes) After finishing the analysis, read the Sponsor decision record in the supplied file. Enter the approved "
                "pilot decision, owner, date and rationale in the change log. Copy lab-08-baseline-v1.1-starter.csv to "
                "04-control/baseline-v1.1.csv. The exact approved WBS delta is a new WP-09A row, 'Ten-priority-article "
                "bilingual pilot package', duration 3, predecessors WP-08 and WP-09, work budget SGD 3,500; WP-10 then "
                "depends on WP-09A. Update planned baseline fields only. Keep week8-performance.csv, delivery-board.csv and "
                "the week-8 status pack frozen as historical evidence; do not add actual or variance fields to Baseline v1.1.",
                "Baseline version note: v1.1 implements approved CR-004 only.\n"
                "Revised work budget SGD 108,500 + remaining contingency SGD 11,500 = authorised total SGD 120,000.\n"
                "Revised duration 31 working days; prior status evidence remains unchanged.",
            ),
            (
                "(10 minutes) Copy lab-08-change-implementation-checklist-starter.md to "
                "04-control/change-implementation-checklist.md. Complete the preformatted updates for charter or requirement trace, WBS, schedule, "
                "cost, quality and acceptance, resources, risk, supplier, communications, stakeholder engagement, work "
                "authorisation and status reporting. Give each update an owner, due, evidence and verification. Set the "
                "change to Implemented only after all required rows are complete, then Verified only after the acceptance check.",
                "Update row: Controlled record | Exact change | Owner | Due | Evidence | Status | Verifier\n"
                "Lifecycle: Approved → baseline updated → work authorised → deliverable verified → change Verified",
            ),
        ],
        test=(
            "CR-004 must have a complete request record, four analysed options and at least 12 impact dimensions. The "
            "analysis must show full scope at +SGD 9,000/+8 days and the approved pilot at +SGD 3,500/+3 days. Baseline "
            "v1.1 must show SGD 108,500 work budget, SGD 11,500 remaining contingency, unchanged SGD 120,000 authorised "
            "total and 31 working days. The implementation checklist must contain all 12 controlled-record updates with "
            "owner, evidence and verifier. Baseline v1.1 must add WP-09A and make WP-10 depend on it, while "
            "week8-performance.csv, delivery-board.csv and the week-8 status pack remain frozen and unchanged."
        ),
        checkpoint=(
            "Keep the approved change log, Baseline v1.1, analysis and implementation evidence. Lab 9 reconciles these "
            "with final acceptance and closure. To rejoin, apply only the Sponsor decision record after reproducing both option calculations."
        ),
        troubleshooting=[
            (
                "The revised budget becomes SGD 123,500.",
                "The approved pilot draws from contingency: increase work budget by SGD 3,500 and reduce remaining contingency by the same amount.",
            ),
            (
                "The status history becomes Green after rebaselining.",
                "Restore week-8 actuals and forecast; the new baseline reflects approved scope, not erased historical variance.",
            ),
            (
                "Only the schedule and cost files are updated.",
                "Use the 12-row implementation checklist and keep the change open until every affected controlled record is addressed.",
            ),
        ],
        challenge=(
            "Model a defer-to-next-phase option with no current baseline change. State which benefits, risks, stakeholder "
            "expectations and transition records would still require action now."
        ),
        reflection=(
            "Which impact dimension made the requested change larger than its apparently simple content description?"
        ),
    ),
    dict(
        num=9,
        topic=3,
        title="Close the Project and Capture Reusable Lessons",
        duration=50,
        objective="LO4: validate scope, obtain acceptance, transition ownership and close with traceable records",
        goal="Produce a complete closeout pack that reconciles objectives, deliverables, obligations and future ownership.",
        workflow=["Reconcile completion", "Confirm acceptance", "Transition ownership", "Publish lessons"],
        desc=(
            "You will use the final synthetic evidence to determine whether the BeaconWorks pilot is ready to close. "
            "GenAI will help compile and challenge the pack, while you trace each statement to final records, transfer "
            "remaining actions and benefits, and record the synthetic sponsor’s closure decision."
        ),
        build=(
            "05-closure/closeout-checklist.csv, project-closeout-report.md, transition-and-benefits-plan.md and "
            "lessons-register.csv with formal acceptance, residual ownership and reusable context."
        ),
        services="Spreadsheet · text editor · approved AI assistant · closure-inputs.md · complete Labs 1–8 portfolio",
        prerequisites=[
            "Approved Baseline v1.1, change implementation evidence and all project logs from Labs 1–8.",
            "Open labs/assets/closure-inputs.md and use the final cut-off stated there.",
            "Create an archive copy of the final lab outputs before preparing the closeout summary.",
            "Use the four preformatted Lab 9 starter files in labs/assets; do not recreate their schemas.",
        ],
        steps=[
            (
                "(12 minutes) Copy lab-09-closeout-checklist-starter.csv to 05-closure/closeout-checklist.csv with Category, "
                "Item_ID, Requirement_or_Obligation, Final_Status, Evidence, "
                "Acceptance_or_Transfer_Owner, Date, Residual_Action, Residual_Owner, Due and Closure_Blocker. Include charter "
                "objectives, original deliverables, CR-004 pilot scope, quality evidence, supplier obligations, invoices, "
                "access, records, training, support, risks, issues, benefits and communications.",
                "Final status: Complete | Accepted | Transferred | Open action | Not applicable\n"
                "Closure blocker: YES only when completion, acceptance, legal, financial, operational or safety conditions prevent closure.",
            ),
            (
                "(12 minutes) Reconcile the preformatted checklist against the charter, requirements trace, Baseline v1.1, quality log, change "
                "log, risk-issue cockpit and procurement records. Ask the assistant for candidate gaps with File, Record_ID, "
                "Expected, Found and Consequence. Verify each gap yourself and update the checklist; never mark an item "
                "complete from the summary alone.",
                "Closeout reconciliation: objective → deliverable → requirement → verification → acceptance → owner\n"
                "Commercial reconciliation: agreement → deliverable → acceptance → invoice → obligation closed or transferred",
            ),
            (
                "(10 minutes) Copy lab-09-transition-benefits-starter.md to "
                "05-closure/transition-and-benefits-plan.md with Operational owner, Support boundary, Runbook and training, "
                "Access and data actions, Supplier follow-up, Open actions, Residual risks, Benefit measure, Baseline, Target, "
                "Measurement date, Data owner and Review forum. Transfer each non-blocking residual item to one named owner "
                "and obtain a stated due date.",
                "Residual item | Context | Current exposure | Action | Owner | Due | Review forum | Escalation\n"
                "Benefit record | Baseline | Target | Measure date | Data source | Owner | Decision after review",
            ),
            (
                "(8 minutes) Copy lab-09-lessons-register-starter.csv to 05-closure/lessons-register.csv with Lesson_ID, "
                "Context, Expected, Observed, Evidence, Cause, Action_Taken, "
                "Result, Recommendation, Future_Owner and Reuse_Trigger. Use C-A-R-R: Context, Action, Result, Recommendation. "
                "Extract candidate lessons from the project records, then keep at least six that have evidence and a future action.",
                "C-A-R-R lesson: Context → Action → Result → Recommendation\n"
                "Reject generic entries such as 'communicate more' unless context, evidence and reusable action are stated.",
            ),
            (
                "(8 minutes) Copy lab-09-closeout-report-starter.md to 05-closure/project-closeout-report.md. Complete its "
                "preformatted sections: Executive outcome, Objectives, Scope and changes, Schedule, Cost, "
                "Quality and acceptance, Stakeholders, Risks and issues, Procurement, Transition, Benefits, Lessons, Records "
                "location and Closure decision. Use the assistant to draft from the verified checklist only. Compare every "
                "figure and status with its source, then enter the Sponsor closure record from closure-inputs.md.",
                "Draft only from <VERIFIED CLOSEOUT CHECKLIST>.\n"
                "Separate final fact, residual action and future benefit.\n"
                "Finish with Claim | Evidence ID | Owner | Human verification.\n"
                "Closure decision must name decision owner, date, accepted outcome and transferred actions.",
            ),
        ],
        test=(
            "The checklist must cover all 14 named categories, trace each completion or acceptance to evidence and show "
            "no unresolved Closure_Blocker. Every residual action, risk and benefit must have one owner and date in the "
            "transition plan. The lessons register must contain at least six evidence-backed C-A-R-R records with reuse "
            "triggers. The closeout report must contain all 14 named report sections plus the completed Claim verification "
            "table, reconcile final schedule and cost with the supplied evidence, record the sponsor closure decision and "
            "point to the final records location."
        ),
        checkpoint=(
            "This is the final checkpoint. The complete portfolio runs from AI working agreement and charter through "
            "Baseline v1.1, delivery and control evidence, acceptance, transition, benefits and reusable lessons."
        ),
        troubleshooting=[
            (
                "A residual action has no owner because the project team is disbanding.",
                "Do not close that row; transfer it to an operational owner with due date and review forum.",
            ),
            (
                "The closeout summary says all objectives were achieved but one benefit is measured later.",
                "Separate delivered capability from future benefit and keep the benefit review in the transition plan.",
            ),
            (
                "A lesson is a vague slogan.",
                "Add project context, evidence, action, observed result and a specific recommendation with reuse trigger.",
            ),
        ],
        challenge=(
            "Prepare a one-page early-termination variant. Identify what acceptance, financial, supplier, records, people "
            "and risk actions would still be required even if the project stopped before delivering the pilot."
        ),
        reflection=(
            "Which closure record most clearly demonstrates that project completion and long-term benefit ownership are different?"
        ),
    ),
]
