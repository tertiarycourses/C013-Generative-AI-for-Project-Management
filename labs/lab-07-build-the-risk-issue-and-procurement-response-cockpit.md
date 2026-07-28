# Lab 7 — Build the Risk, Issue and Procurement Response Cockpit

**Course:** Generative AI for Project Management  
**Course Code:** C013  
**Version:** v1.0 (28 July 2026)  
**Topic 3:** Manage Project Risks with GenAI  
**Maps to:** LO3: anticipate and implement risk, issue and supplier responses from verified evidence  
**Duration:** 50 minutes  
**Tools:** Spreadsheet · text editor · approved AI assistant · risk-issue-inputs.csv · vendor-bids.csv

---

## Goal

Convert priority uncertainty and supplier evidence into owned, triggered and measurable response actions.

## What You Will Do

You will refresh the initial risk register at the week-8 status date, distinguish triggered risks from current issues and compare three synthetic accessibility-review offers against criteria written in Lab 3. GenAI may structure evidence and challenge gaps, but final scores, owners and recommendation remain human-owned.

## What You Will Build

04-control/risk-issue-cockpit.csv, procurement-comparison.csv and response-brief.md with current exposure, triggered actions, weighted supplier evidence and integrated project impacts.

## Prerequisites

- Initial risk register and procurement-evaluation-plan.csv from Lab 3.
- Verified week-8 evidence table and status pack from Lab 6.
- Open labs/assets/risk-issue-inputs.csv and labs/assets/vendor-bids.csv.

> **Data note.** Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

## Steps

### 1. Copy the initial risks into 04-control/risk-issue-cockpit.csv and add Status_Date, Current_Status, Trigger_Result, Response_Action_Status, Issue_ID, Issue_Action, Action_Owner, Due, Residual_Probability, Residual_Impact and Residual_Exposure. Apply the week-8 update rows from risk-issue-inputs.csv. A risk becomes an issue only when the stated condition has occurred.

```text
Risk lifecycle: Open → Triggered → Response active → Closed
Issue lifecycle: Open → Action active → Resolved → Closed
Residual_Exposure = Residual_Probability × Residual_Impact
```

### 2. Ask the assistant to critique each cause–event–effect statement, trigger and response using only the cockpit and status evidence. Request missing fields and contradictions, not replacement scores. Make the final current and residual scores yourself; for each triggered item record the preventive action outcome, contingency start, owner, due date and secondary risk.

```text
Return Risk_ID | Structural gap | Evidence | Consequence | Repair question.
Do not invent probability, impact, trigger evidence or owner.
Separate a future uncertain event from a condition that has already occurred.
```

### 3. Copy vendor-bids.csv to procurement-comparison.csv. Add the five approved criterion scores from the evidence using the 1, 3 and 5 anchors written in Lab 3. Calculate Weighted_Total as the sum of Score × Weight divided by 100. Record Missing_Evidence, Clarification, Commercial_Review and Human_Recommendation. Do not change criteria after seeing the offers.

```text
Weighted_Total = Σ(criterion score × criterion weight) / 100
Expected evidence-based totals: Vendor A 3.90 · Vendor B 4.10 · Vendor C 3.70
```

### 4. Create response-brief.md with sections Status date, Top exposure, Triggered responses, Current issues, Supplier comparison, Recommendation, Project impacts, Decisions and Monitoring. Recommend Vendor B for authorised commercial review because it has the highest evidence-based total; do not call it awarded. Link supplier lead time, cost and data handling to the schedule, budget, quality and risk records.

```text
Recommendation wording: 'Recommend Vendor B for authorised commercial review, subject to clarification and required approval.'
Impact dimensions: scope · schedule · cost · quality · resources · data · risk · communications
```

### 5. Run a cockpit completeness check. Every high exposure or current issue must have one owner, one next action, one due date and one review point. Every supplier score must cite a bid field. Add a monitoring calendar with daily issue follow-up until stabilised, weekly risk review and supplier milestone checks.

```text
Completeness: evidence · status · action · owner · due · residual exposure · review date
Supplier trace: criterion score → bid field → anchor → human reviewer
```

## Test It

All five initial risks must appear in the cockpit, with week-8 status, trigger result, current or residual exposure, owned action and review point. Conditions that have occurred must have Issue_IDs and must not remain worded only as future uncertainty. Procurement weights must remain unchanged and totals must be Vendor A 3.90, Vendor B 4.10 and Vendor C 3.70. The response brief must recommend—not award—Vendor B, integrate eight impact dimensions and contain the stated monitoring cadence.

## Checkpoint and Rejoin Point

Keep the cockpit, comparison and response brief. Lab 8 uses the current exposures, supplier recommendation and week-8 forecast in a change decision. To rejoin, reproduce the three weighted totals before making a recommendation.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A triggered risk and its resulting issue are duplicated with different owners. | Link them with Issue_ID, retain the risk for residual exposure and name one coordinated response owner. |
| The assistant scores missing supplier evidence as average. | Use the prewritten anchor; record missing evidence and request clarification instead of inventing a score. |
| The highest-scoring offer is described as awarded. | Change the status to Recommended for commercial review until the authorised process records a decision. |

## Challenge

Recalculate totals if lead-time weight rises from 20 to 30 and cost falls from 15 to 5. Explain why that scenario is sensitivity analysis, not permission to change the approved criteria after bids were opened.

## Reflection

Which risk or supplier conclusion changed most after evidence, trigger and scoring anchors were made explicit?

---

[← Lab 6](lab-06-build-the-evidence-led-project-status-pack.md) · [Lab 8 →](lab-08-run-integrated-change-control-and-baseline-impact-analysis.md)
