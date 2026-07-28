# Lab 6 — Build the Evidence-Led Project Status Pack

**Course:** Generative AI for Project Management  
**Course Code:** C013  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** Project Execution and Delivery with GenAI  
**Maps to:** LO2: communicate project delivery status and budget challenges from verified work-performance evidence  
**Duration:** 60 minutes  
**Tools:** Spreadsheet · text editor · approved AI assistant · weekly-update-inputs.md · Lab 3–5 records

---

## Goal

Calculate project performance and produce audience-specific updates that preserve one version of the facts.

## What You Will Do

You will reconcile the baseline, delivery board and supplied week-8 update. You will calculate schedule and cost indicators in the spreadsheet before asking GenAI to draft narrative. The final pack distinguishes fact, forecast, risk, decision and ask for both sponsor and team audiences.

## What You Will Build

03-delivery/week-08-performance.csv and week-08-status-pack.md containing transparent calculations, source links, a sponsor decision brief and a delivery-team action view.

## Prerequisites

- Frozen Baseline v1.0, current delivery board, decision log, quality log and resource plan.
- Open labs/assets/weekly-update-inputs.md and use the stated week-8 cut-off only.
- Use the work budget BAC of SGD 105,000; keep contingency outside earned-value calculations.

> **Data note.** Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

## Steps

### 1. Create week-08-performance.csv with Metric, Formula, Input_A, Input_B, Result, Unit, Source and Human_Check. Enter PV 72000, EV 60000, AC 66000 and BAC 105000 from the supplied update. Calculate SV, CV, SPI, CPI, EAC using BAC/CPI, ETC using EAC-AC and VAC using BAC-EAC. Round ratios to two decimals and currency to the nearest dollar.

```text
SV = EV - PV
CV = EV - AC
SPI = EV / PV
CPI = EV / AC
EAC = BAC / CPI
ETC = EAC - AC
VAC = BAC - EAC
```

### 2. Reconcile supplied milestone, defect, capacity, risk, issue and decision information with the current project records. In week-08-status-pack.md create an Evidence table with Evidence_ID, Status_Date, Fact, Source, Owner and Confidence. Record contradictions as Open data issue rather than choosing the more favourable value.

```text
One status date: Week 8 Friday 17:00
Evidence classes: COMPLETED FACT | CURRENT CONDITION | FORECAST | RISK | ISSUE | DECISION | ASK
```

### 3. Before using AI, write the overall status from the agreed thresholds: Red if SPI or CPI is below 0.90, or an approved milestone is forecast to breach by more than three working days without an authorised recovery; Amber for an emerging tolerance threat; Green only when within tolerance. State the threshold and evidence used.

```text
Expected calculations: SPI 0.83 · CPI 0.91 · EAC SGD 115,500 · VAC -SGD 10,500
Expected schedule forecast: 32 working days versus 28-day baseline
```

### 4. Give the assistant only the verified Evidence table and performance rows. Request two drafts: a sponsor brief with Outcome, Trend, Tolerance, Cause, Consequence, Options, Recommendation and Decision needed; and a team view with completed work, blocked work, next actions, owners and dates. Require the same status, figures and forecast in both.

```text
Use only <VERIFIED STATUS DATA>.
Do not soften Red, change a figure or invent a cause.
Draft A: sponsor decision brief, 180 words maximum.
Draft B: team action view, table format.
Finish with Claim | Evidence_ID | Classification.
```

### 5. Review every generated claim against the evidence and save the corrected versions. Add a Decision request that names the owner, latest decision date, options, recommendation and consequence of no decision. Add a next-cycle data checklist for progress evidence, actual cost, remaining duration, defects, capacity, risks, issues, supplier status and stakeholder feedback.

```text
Decision request: owner · decision · due · options · recommendation · no-decision consequence
Next-cycle checklist: nine evidence categories each with source owner and cut-off time
```

## Test It

The spreadsheet must show SV -SGD 12,000, CV -SGD 6,000, SPI 0.83, CPI 0.91, EAC SGD 115,500, ETC SGD 49,500 and VAC -SGD 10,500. The pack must show a 32-day forecast against the 28-day baseline, apply the stated status threshold consistently, contain source IDs for every material claim, preserve identical facts across sponsor and team views, and include a complete decision request plus nine-item next-cycle checklist.

## Checkpoint and Rejoin Point

Freeze the verified week-8 calculations and evidence table. Lab 7 uses the status risks and supplier data; Lab 8 uses the forecast and decision structure. To rejoin, reproduce the expected calculations before drafting narrative.

## Troubleshooting

| If this happens | Fix |
|---|---|
| EAC is calculated from the authorised total including contingency. | Use the SGD 105,000 work budget BAC for earned value and show contingency separately. |
| The AI draft changes Red to Amber. | Restore Red from the agreed rule and tell the assistant that status is a fixed input, not a writing choice. |
| Two files report different actual cost. | Record an Open data issue, name the source owner and do not publish a resolved figure until reconciled. |

## Challenge

Calculate an alternative EAC using AC + (BAC-EV) and explain which performance assumption differs from BAC/CPI. Do not replace the official forecast without an authorised decision.

## Reflection

Which part of the status pack required the most human judgement after the calculations were fixed?

---

[← Lab 5](lab-05-manage-team-knowledge-quality-and-stakeholder-delivery.md) · [Lab 7 →](lab-07-build-the-risk-issue-and-procurement-response-cockpit.md)
