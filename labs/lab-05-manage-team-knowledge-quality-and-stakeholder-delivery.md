# Lab 5 — Manage Team Knowledge, Quality and Stakeholder Delivery

**Course:** Generative AI for Project Management  
**Course Code:** C013  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** Project Execution and Delivery with GenAI  
**Maps to:** LO2: resolve delivery challenges through explicit capacity, knowledge, quality and engagement controls  
**Duration:** 45 minutes  
**Tools:** Spreadsheet · text editor · approved AI assistant · delivery-events.md · Lab 2–4 records

---

## Goal

Turn live delivery events into owned team actions, verified quality records and confirmed project knowledge.

## What You Will Do

You will process synthetic capacity, meeting and defect evidence without inferring people’s intent. GenAI will extract candidate decisions and actions, while you confirm them against the source and update the resource, decision, quality and stakeholder records.

## What You Will Build

03-delivery/resource-and-raci-plan.csv, quality-and-acceptance-log.csv, meeting-record-ai-draft.md, meeting-record.md, stakeholder-engagement-update.md and delivery-handoff-checklist.md with confirmed owners and evidence.

## Prerequisites

- Delivery board and decision log from Lab 4.
- Stakeholder register and communications plan from Lab 2.
- Open delivery-events.md and use Events E04–E07 only.
- Use the five preformatted Lab 5 starter files in labs/assets so the 45-minute exercise focuses on evidence and decisions.

> **Data note.** Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

## Steps

### 1. (8 minutes) Copy lab-05-resource-raci-starter.csv to 03-delivery/resource-and-raci-plan.csv. Keep one row per Resource_Role; list every related work package in Affected_Work_Packages. Complete Responsible, Accountable, Consulted, Informed, Capability_Needed, Planned_Effort_Days, Available_Effort_Days, Variance_Days, Conflict, Resolution_Option and Human_Decision. Enter the supplied capacity values from E04 and calculate Variance_Days as available minus planned. Mark negative values as conflicts.

```text
Variance_Days = Available_Effort_Days - Planned_Effort_Days
Conflict = YES when Variance_Days < 0
Resolution options: resequence · reduce approved scope via change · add authorised capacity · change date
```

### 2. (10 minutes) Copy lab-05-meeting-record-starter.md to 03-delivery/meeting-record-ai-draft.md. Paste meeting note E05 into the assistant and request candidate Decisions, Actions, Questions, Assumptions, Risks and Lessons with exact source quotations of no more than 12 words. Save the response in that draft file, compare each item with E05, then save the corrected human-reviewed version as 03-delivery/meeting-record.md with Confirmed or Pending confirmation status.

```text
Extract only what the note supports.
Return Type | Candidate record | Owner | Date | Evidence excerpt | Confirmation needed.
Do not infer agreement, sentiment or an owner not named in the note.
```

### 3. (10 minutes) Add confirmed decisions to decision-log.csv. Copy lab-05-quality-acceptance-starter.csv to 03-delivery/quality-and-acceptance-log.csv with Deliverable_ID, Requirement_ID, Criterion, Verification_Method, Result, Evidence, Defect_ID, Severity, Corrective_Action, Action_Owner, Due and Acceptance_Status. Enter E06 and E07 exactly; keep quality result separate from stakeholder acceptance.

```text
Quality result: Meets | Does not meet | Not checked
Acceptance status: Pending | Accepted | Accepted with actions | Not accepted
A completed internal check does not equal stakeholder acceptance.
```

### 4. (8 minutes) Copy lab-05-stakeholder-engagement-update-starter.md to 03-delivery/stakeholder-engagement-update.md. Compare the support agents’ current and desired state with the evidence in E05–E07. Record Observation, Evidence, Consequence, Updated action, Owner, Trigger and Feedback method. Do not label attitude; describe observable participation, questions, delays or decisions.

```text
Acceptable observation: 'Three workflow questions remain open after the review.'
Not acceptable: 'The team is resistant.' unless direct, appropriate evidence and context support it.
```

### 5. (9 minutes) Ask the assistant to critique the four outputs for contradictions in owner, date, status and evidence. Resolve each contradiction against the source event. Copy lab-05-delivery-handoff-checklist-starter.md to 03-delivery/delivery-handoff-checklist.md and complete its seven rows: capacity, decision, action, defect, acceptance, stakeholder update and controlled-record link.

```text
Contradiction table: Field | File A | File B | Source evidence | Human resolution | Updated files
Handoff result: seven items each marked READY or ACTION with owner and due date.
```

## Test It

The resource plan must use one row per resource role and show these E04 results: Accessibility Specialist -2/YES, Integration Engineer 0/NO, Content Lead -2/YES and Support Lead +1/NO for Variance_Days/Conflict. The meeting record must classify at least one decision, action, question, assumption, risk and lesson, each with evidence and confirmation status. The quality log must keep verification result separate from acceptance status and include owners for all corrective actions. The engagement update must use observable evidence and the handoff checklist must be saved as 03-delivery/delivery-handoff-checklist.md and contain all seven required items.

## Checkpoint and Rejoin Point

Keep the corrected delivery records. Lab 6 uses confirmed decisions, defects, capacity conflicts and actions in the weekly status pack. To rejoin, reprocess E04–E07 and mark uncertain extraction Pending confirmation.

## Troubleshooting

| If this happens | Fix |
|---|---|
| RACI has more than one accountable role for a work package. | Escalate the ambiguity and name one final accountable decision owner in Human_Decision. |
| The summary assigns an action to someone not named in the note. | Set Owner to UNASSIGNED and add a Pending confirmation action. |
| A deliverable is marked accepted after an internal check. | Change Acceptance_Status to Pending until the authorised stakeholder records acceptance. |

## Challenge

Propose a resource resolution that protects the 28-day baseline, then state the cost, quality, coordination and risk assumptions that would need approval before it could be used.

## Reflection

Which source check prevented the largest error in the meeting, resource or quality record?

---

[← Lab 4](lab-04-turn-the-baseline-into-an-executable-delivery-system.md) · [Lab 6 →](lab-06-build-the-evidence-led-project-status-pack.md)
