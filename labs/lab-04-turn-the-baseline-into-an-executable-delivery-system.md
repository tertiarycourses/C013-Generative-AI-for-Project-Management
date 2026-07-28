# Lab 4 — Turn the Baseline into an Executable Delivery System

**Course:** Generative AI for Project Management  
**Course Code:** C013  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** Project Execution and Delivery with GenAI  
**Maps to:** LO2: direct and manage project work with owned work packages, dependencies and completion evidence  
**Duration:** 50 minutes  
**Tools:** Spreadsheet · text editor · approved AI assistant · Lab 3 baseline · delivery-events.md

---

## Goal

Create a ready-to-run delivery board and authorise one bounded work package.

## What You Will Do

You will transform the frozen Baseline v1.0 into a delivery board without changing its scope or dates. The exercise distinguishes planned, ready, active, blocked and done work, then creates a detailed brief for portal configuration with prerequisites, acceptance evidence and escalation rules.

## What You Will Build

03-delivery/delivery-board.csv, work-package-brief-WP-04.md and decision-log.csv that translate the baseline into controlled execution records.

## Prerequisites

- Frozen wbs-and-baseline.csv and integrated-management-plan.md from Lab 3.
- Open labs/assets/delivery-events.md and read Events E01–E03 only.
- Do not implement or approve a baseline change in this lab.

> **Data note.** Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

## Steps

### 1. Copy the ten work-package rows from wbs-and-baseline.csv into 03-delivery/delivery-board.csv. Add Status, Readiness_Evidence, Actual_Start, Actual_Finish, Forecast_Finish, Percent_Complete_Method, Progress_Evidence, Blocker, Next_Action, Action_Owner and Escalation_Date. Set Status to Planned until the predecessor, input, owner and environment checks are supported.

```text
Allowed status: Planned | Ready | Active | Blocked | Done
Readiness gate: predecessor complete · approved input available · owner confirmed · environment available
```

### 2. Use delivery event E01 to update WP-01 through WP-03. Mark only work supported by the event as Done, Active or Ready and link its evidence label. For active work, define progress by completed acceptance items or verified sub-deliverables; do not enter a subjective percentage.

```text
Progress evidence examples: approved requirements record · accepted content batch · reviewed design artifact
Rule: activity or effort alone is not deliverable progress.
```

### 3. Create work-package-brief-WP-04.md for Portal configuration with Objective, Scope boundary, Inputs, Predecessors, Owner, Contributors, Start gate, Planned duration, Cost budget, Quality checks, Acceptance evidence, Risks, Communication, Done criteria and Escalation. Ask the assistant for a draft using only the baseline and E01, then reconcile every field to those records.

```text
Draft a bounded WP-04 brief from <BASELINE ROW> and <EVENT E01> only.
Use UNKNOWN for missing data. Do not add features or change dates.
Finish with Source field | Used value | Evidence | Human check.
```

### 4. Create decision-log.csv with columns Decision_ID, Date, Question, Options, Evidence, Decision, Rationale, Decision_Owner, Affected_Records, Review_Trigger and Status. Record the E02 environment-access decision as Pending decision. Ask the assistant to produce three options, then remove any option that violates the charter or baseline and record the human-approved recommendation separately.

```text
Decision analysis: Option | Benefits | Drawbacks | Scope impact | Schedule impact | Cost impact | Risk | Evidence
Status remains Pending decision until the named owner confirms it.
```

### 5. Apply event E03 to the board. If the event is an unapproved feature request, add Blocker or Next_Action as Log change request and leave baseline fields unchanged. Run a trace check from each active row to WBS, owner, predecessor, cost, quality evidence and communication record.

```text
Trace check result per active row: WBS PASS/REPAIR · Owner PASS/REPAIR · Logic PASS/REPAIR · Cost PASS/REPAIR · Evidence PASS/REPAIR · Communication PASS/REPAIR
```

## Test It

The board must contain the same ten work packages, baseline durations and costs as Baseline v1.0. Every Ready or Active row must have readiness evidence, owner, next action and objective progress evidence. The WP-04 brief must contain all 15 requested sections and no added scope. The decision log must contain E02 as Pending decision with at least two viable options, and E03 must be routed to a change request without editing the baseline.

## Checkpoint and Rejoin Point

Keep all three delivery records. Lab 5 adds team, knowledge and quality controls; Lab 6 uses the board as the status source. To rejoin, copy Baseline v1.0 and apply only delivery events E01–E03.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Several rows appear ready even though a predecessor is incomplete. | Apply the readiness gate row by row and return unsupported work to Planned. |
| Percent complete is a confident number without evidence. | Replace it with completed acceptance items, verified quantities or a forecast based on remaining work. |
| The feature request appears inside WP-04. | Remove it, log a change request and preserve the original work-package boundary. |

## Challenge

Create a filtered view showing only work that can start in the next five working days. Explain the exact readiness evidence for each selected row and why every excluded row is not yet ready.

## Reflection

Which field most clearly separated an authorised work package from a plausible AI-generated task list?

---

[← Lab 3](lab-03-build-the-integrated-project-management-plan.md) · [Lab 5 →](lab-05-manage-team-knowledge-quality-and-stakeholder-delivery.md)
