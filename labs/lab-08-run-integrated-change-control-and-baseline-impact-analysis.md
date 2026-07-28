# Lab 8 — Run Integrated Change Control and Baseline Impact Analysis

**Course:** Generative AI for Project Management  
**Course Code:** C013  
**Version:** v1.0 (28 July 2026)  
**Topic 3:** Manage Project Risks with GenAI  
**Maps to:** LO3: evaluate and decide a project change across all affected controls with GenAI support  
**Duration:** 50 minutes  
**Tools:** Spreadsheet · text editor · approved AI assistant · change-request-CR-004.md · Labs 3, 6 and 7 records

---

## Goal

Process CR-004 from request through impact analysis, authorised decision and coordinated record update.

## What You Will Do

You will evaluate a request for bilingual pilot content at week 8. The exercise prevents a useful feature from bypassing scope, schedule, cost, quality, resource, risk, supplier, communication and operational review. You will model options, record the synthetic sponsor decision and publish a traceable Baseline v1.1.

## What You Will Build

04-control/change-log.csv, change-impact-analysis-CR-004.md, baseline-v1.1.csv and change-implementation-checklist.md with an approved, fully traced incremental change.

## Prerequisites

- Frozen Baseline v1.0 and verified week-8 status evidence.
- Risk-issue cockpit and procurement response brief from Lab 7.
- Open labs/assets/change-request-CR-004.md and separate Request evidence from Sponsor decision record.
- Use the four preformatted Lab 8 starter files in labs/assets; do not recreate their schemas.

> **Data note.** Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

## Steps

### 1. (6 minutes) Copy lab-08-change-log-starter.csv to 04-control/change-log.csv with Change_ID, Date_Logged, Requester, Reason, Requested_Outcome, Urgency, Affected_Requirement, Status, Decision_Owner, Decision_Date, Decision, Rationale and Implementation_Status. Enter CR-004 from the Request section only and set Status to Analysing.

```text
Status: Logged | Analysing | More information | Approved | Rejected | Deferred | Implemented | Verified
Do not copy the sponsor decision until impact analysis is complete.
```

### 2. (12 minutes) Copy lab-08-change-impact-analysis-starter.md to 04-control/change-impact-analysis-CR-004.md. Complete the current baseline and four options: reject, defer, full 30-article change and ten-priority-article pilot. Ask the assistant to propose an impact checklist, then complete it from project evidence across value, scope, schedule, cost, quality, resources, risk, supplier, communications, operations, benefits and alternatives.

```text
For each option return: value · scope delta · WBS delta · duration · cost · quality evidence · resource need · risk · supplier · communication · operational effect · assumptions · recommendation.
Use UNKNOWN when the project record is silent.
```

### 3. (10 minutes) Calculate the two implementation options. Confirm that full scope adds SGD 9,000 and eight working days. Confirm that the pilot adds SGD 3,500 and three working days. Compare each with the authorised budget, remaining contingency, week-8 forecast, available translation capacity and acceptance evidence. Recommend the pilot with explicit residual risk and benefit limits.

```text
Full option: +SGD 9,000 · +8 working days
Pilot option: +SGD 3,500 · +3 working days
Pilot revised work budget = SGD 108,500
Remaining contingency = SGD 11,500
Pilot revised baseline duration = 31 working days
```

### 4. (12 minutes) After finishing the analysis, read the Sponsor decision record in the supplied file. Enter the approved pilot decision, owner, date and rationale in the change log. Copy lab-08-baseline-v1.1-starter.csv to 04-control/baseline-v1.1.csv. The exact approved WBS delta is a new WP-09A row, 'Ten-priority-article bilingual pilot package', duration 3, predecessors WP-08 and WP-09, work budget SGD 3,500; WP-10 then depends on WP-09A. Update planned baseline fields only. Keep week8-performance.csv, delivery-board.csv and the week-8 status pack frozen as historical evidence; do not add actual or variance fields to Baseline v1.1.

```text
Baseline version note: v1.1 implements approved CR-004 only.
Revised work budget SGD 108,500 + remaining contingency SGD 11,500 = authorised total SGD 120,000.
Revised duration 31 working days; prior status evidence remains unchanged.
```

### 5. (10 minutes) Copy lab-08-change-implementation-checklist-starter.md to 04-control/change-implementation-checklist.md. Complete the preformatted updates for charter or requirement trace, WBS, schedule, cost, quality and acceptance, resources, risk, supplier, communications, stakeholder engagement, work authorisation and status reporting. Give each update an owner, due, evidence and verification. Set the change to Implemented only after all required rows are complete, then Verified only after the acceptance check.

```text
Update row: Controlled record | Exact change | Owner | Due | Evidence | Status | Verifier
Lifecycle: Approved → baseline updated → work authorised → deliverable verified → change Verified
```

## Test It

CR-004 must have a complete request record, four analysed options and at least 12 impact dimensions. The analysis must show full scope at +SGD 9,000/+8 days and the approved pilot at +SGD 3,500/+3 days. Baseline v1.1 must show SGD 108,500 work budget, SGD 11,500 remaining contingency, unchanged SGD 120,000 authorised total and 31 working days. The implementation checklist must contain all 12 controlled-record updates with owner, evidence and verifier. Baseline v1.1 must add WP-09A and make WP-10 depend on it, while week8-performance.csv, delivery-board.csv and the week-8 status pack remain frozen and unchanged.

## Checkpoint and Rejoin Point

Keep the approved change log, Baseline v1.1, analysis and implementation evidence. Lab 9 reconciles these with final acceptance and closure. To rejoin, apply only the Sponsor decision record after reproducing both option calculations.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The revised budget becomes SGD 123,500. | The approved pilot draws from contingency: increase work budget by SGD 3,500 and reduce remaining contingency by the same amount. |
| The status history becomes Green after rebaselining. | Restore week-8 actuals and forecast; the new baseline reflects approved scope, not erased historical variance. |
| Only the schedule and cost files are updated. | Use the 12-row implementation checklist and keep the change open until every affected controlled record is addressed. |

## Challenge

Model a defer-to-next-phase option with no current baseline change. State which benefits, risks, stakeholder expectations and transition records would still require action now.

## Reflection

Which impact dimension made the requested change larger than its apparently simple content description?

---

[← Lab 7](lab-07-build-the-risk-issue-and-procurement-response-cockpit.md) · [Lab 9 →](lab-09-close-the-project-and-capture-reusable-lessons.md)
