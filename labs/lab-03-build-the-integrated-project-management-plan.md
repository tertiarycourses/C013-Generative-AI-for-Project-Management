# Lab 3 — Build the Integrated Project Management Plan

**Course:** Generative AI for Project Management  
**Course Code:** C013  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Project Initiation and Planning with GenAI  
**Maps to:** LO1: develop an integrated scope, schedule, cost, quality, resource, communication, risk and procurement plan  
**Duration:** 90 minutes  
**Tools:** Spreadsheet · text editor · approved AI assistant · planning-inputs.csv · risk-issue-inputs.csv

---

## Goal

Turn the authorised project parameters into one coherent baseline and management plan.

## What You Will Do

You will use the charter, stakeholder plan and supplied work-package inputs to create a WBS-aligned baseline. You will calculate the network and budget yourself, then use GenAI to critique integration gaps across quality, resources, communications, risks and procurement.

## What You Will Build

02-planning/wbs-and-baseline.csv, integrated-management-plan.md, initial-risk-register.csv and procurement-evaluation-plan.csv with a verified 28-working-day critical path and SGD 120,000 authorised budget.

## Prerequisites

- Completed charter, source ledger, stakeholder register and communications plan from Labs 1–2.
- Open labs/assets/planning-inputs.csv and labs/assets/risk-issue-inputs.csv.
- Know that the approved budget ceiling is SGD 120,000, including SGD 15,000 contingency.

> **Data note.** Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

## Steps

### 1. (20 minutes) Copy planning-inputs.csv to 02-planning/wbs-and-baseline.csv. Verify that the ten work packages cover the Portal Pilot deliverable and that exclusions in the charter are absent. Add columns Earliest_Start, Earliest_Finish, Latest_Start, Latest_Finish, Total_Float, Critical, Acceptance_Evidence and Human_Reviewer. Do not change supplied durations, predecessors or costs during the first calculation.

```text
WBS check: complete approved scope · no excluded scope · one owner · one acceptance criterion per work package
Day-zero convention: a work package with no predecessor has ES = 0; EF = ES + Duration.
Forward pass: ES = maximum predecessor EF; EF = ES + Duration.
```

### 2. (25 minutes) Complete the forward pass, then calculate the backward pass from a project finish of day 28. For terminal work packages set LF = 28 and LS = LF minus Duration. For every predecessor, set LF to the minimum LS of its successors and LS = LF minus Duration. Calculate Total_Float = LS minus ES and mark Critical = YES only when Total_Float = 0. Sum Work_Budget_SGD, add the approved contingency and compare with the charter ceiling. Record the expected baseline summary in integrated-management-plan.md. If your result is not 28 working days and SGD 105,000 work budget plus SGD 15,000 contingency, find the dependency or arithmetic error before continuing.

```text
Expected work budget = SGD 105,000
Contingency = SGD 15,000
Authorised total = SGD 120,000
Expected critical path = WP-01 -> WP-03 -> WP-04 -> WP-07 -> WP-08 -> WP-10
Expected critical path duration = 28 working days
Backward pass: terminal LF = 28; predecessor LF = minimum successor LS; Total_Float = LS - ES
```

### 3. (20 minutes) Create integrated-management-plan.md with sections Scope, Schedule, Cost, Quality, Resources, Communications, Risk, Procurement, Change, Baseline governance and Source register. For each section state the objective, method, owner, evidence, threshold or trigger and controlled record. Link the specialist availability, supplier interface and acceptance owner from Lab 2.

```text
Component plan pattern:
Objective | Method | Owner | Evidence | Threshold/trigger | Controlled record
Integration check: every work package has scope + date + cost + resource + quality evidence
```

### 4. (15 minutes) Copy the five RISK rows from risk-issue-inputs.csv to initial-risk-register.csv. Add Probability_1_5, Impact_1_5, Exposure, Strategy, Preventive_Action, Trigger, Contingency, Owner and Residual_Exposure. Ask the assistant to critique cause–event–effect structure and missing response fields; make the final scores and owners yourself.

```text
Risk statement: Because <cause>, <uncertain event> may occur, leading to <effect on objective>.
Exposure = Probability × Impact
Do not convert a current issue into a future risk.
```

### 5. (10 minutes) Create procurement-evaluation-plan.csv for the accessibility review with criteria Capability 25, Method and evidence 25, Lead time 20, Data handling 15 and Cost 15. Write 1–5 scoring anchors before viewing any offer. Ask the assistant to inspect the four planning files for contradictions and return Issue, Evidence, Consequence and Repair. Resolve every high-consequence contradiction or record an owned open action.

```text
Criterion,Weight_Percent,Score_1_Anchor,Score_3_Anchor,Score_5_Anchor,Decision_Owner
Capability,25,<MINIMUM>,<ADEQUATE>,<STRONG>,Procurement Lead
Weights must total 100.
```

## Test It

The baseline must contain ten contiguous work packages, total SGD 105,000 before contingency and show the zero-float path WP-01 -> WP-03 -> WP-04 -> WP-07 -> WP-08 -> WP-10 at 28 working days. Every row must have ES, EF, LS, LF and Total_Float calculated with the stated day-zero convention. The integrated plan must contain all 11 sections and link every work package to an owner, resource role, cost, quality or acceptance evidence and communication or control record. The risk register must contain five cause–event–effect rows with scored exposure, action, trigger, contingency and owner. Procurement criteria weights must total 100 and include written 1, 3 and 5 scoring anchors.

## Checkpoint and Rejoin Point

Freeze the four files as Baseline v1.0 and add the status 'Ready for sponsor baseline review'. Labs 4–9 use these records. To rejoin, copy the supplied planning inputs and reproduce the expected 28-day and SGD 120,000 checks.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The schedule finishes earlier than 28 working days. | Check that each activity starts after the maximum finish of all predecessors, not the first predecessor listed. |
| The work budget does not equal SGD 105,000. | Sum each unique work-package row once and keep contingency outside the work-package total. |
| The AI critique recommends changing the baseline. | Treat the output as an issue list; make changes only after checking source evidence and recording the human decision. |

## Challenge

Model a scenario in which content approval takes two extra days. Recalculate the finish, identify the affected critical path and propose two recovery options without changing the frozen Baseline v1.0.

## Reflection

Which dependency created the strongest connection among scope, schedule, cost, resources, quality and risk?

---

[← Lab 2](lab-02-build-the-stakeholder-engagement-and-communications-plan.md) · [Lab 4 →](lab-04-turn-the-baseline-into-an-executable-delivery-system.md)
