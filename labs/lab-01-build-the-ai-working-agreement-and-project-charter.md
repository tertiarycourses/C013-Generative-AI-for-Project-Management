# Lab 1 — Build the AI Working Agreement and Project Charter

**Course:** Generative AI for Project Management  
**Course Code:** C013  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Project Initiation and Planning with GenAI  
**Maps to:** LO1: develop evidence-led project parameters and an authorised charter draft with GenAI  
**Duration:** 70 minutes  
**Tools:** Text editor · approved AI assistant · beaconworks-project-brief.md · spreadsheet

---

## Goal

Create the control rules and initiation pack that will govern every later lab.

## What You Will Do

You will open the synthetic BeaconWorks Customer Self-Service Portal brief, define a human-owned GenAI working agreement and turn the approved facts into a project charter. The exercise separates facts, assumptions, options and unknowns so polished language never becomes an unreviewed commitment.

## What You Will Build

01-initiation/ai-working-agreement.md, project-charter.md and source-ledger.csv containing the approved project parameters, human review gates and traceable evidence.

## Prerequisites

- Create a local folder named C013-BeaconWorks-Project with 01-initiation through 05-closure subfolders.
- Open labs/assets/beaconworks-project-brief.md and confirm that no real customer or employee data is used.
- Have a spreadsheet application available for the source ledger.

> **Data note.** Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

## Steps

### 1. In 01-initiation, create source-ledger.csv with columns Record_ID, Claim_or_Parameter, Value, Source_File, Source_Section, Classification, Human_Owner and Status. Add rows for the business need, budget ceiling, target week, sponsor, project manager, pilot deliverable and stated exclusions. Use FACT only when the source brief says it directly; otherwise use ASSUMPTION or UNKNOWN.

```text
Record_ID,Claim_or_Parameter,Value,Source_File,Source_Section,Classification,Human_Owner,Status
SRC-001,Business need,<VALUE>,beaconworks-project-brief.md,<SECTION>,FACT,Project Manager,Verified
```

### 2. Create ai-working-agreement.md with six headings: Approved uses, Restricted information, Prompt rule, Review gates, Decision authority and Record keeping. Under Prompt rule, write the C-O-S-T-A-R pattern. Under Review gates, require evidence, calculation, confidentiality, bias, authority and record-update checks.

```text
C-O-S-T-A-R
Context: project and audience
Objective: one observable task
Sources: delimited approved evidence
Tasks: ordered operations
Acceptance criteria: format and quality checks
Review: facts, figures, uncertainty, confidentiality and human authority
```

### 3. Paste only the project brief into the approved AI assistant and request a charter draft with Purpose, Measurable objectives, High-level deliverables, In scope, Out of scope, Milestones, Budget, Assumptions, Constraints, Initial risks, Stakeholders, Authority and Approval readiness. Require a second table that labels each material statement FACT, ASSUMPTION, OPTION or UNKNOWN and cites the brief section.

```text
Objective: Draft a project charter from <PROJECT BRIEF> only.
Do not invent dates, people, figures or requirements. Use UNKNOWN when absent.
Return: charter headings + Statement | Classification | Source section | Review needed.
Before finishing, list contradictions and missing approval information.
```

### 4. Save the response as project-charter-ai-draft.md. Review every objective and parameter against the brief and source ledger. Edit the human-approved version into project-charter.md. Each objective must contain a result, measure, target and time horizon. Move unsupported material to Assumptions or Open questions; never repair a gap by inventing evidence.

```text
Objective quality check: result + measure + target + time horizon
Parameter quality check: source row + classification + owner + status
Final labels: FACT | ASSUMPTION | OPTION | UNKNOWN
```

### 5. Add a Charter readiness checklist to project-charter.md. Mark each item READY or ACTION: business need, objectives, boundaries, deliverables, budget, milestone horizon, authority, initial risks and open questions. Record the project manager as document owner and the synthetic sponsor as approval owner. Do not mark the charter approved; mark it Ready for sponsor review.

```text
Readiness item | Status | Evidence or action | Owner | Due
Final document status: Ready for sponsor review
```

## Test It

The working agreement must contain all six headings and the six-part C-O-S-T-A-R pattern. The charter must contain all 13 requested sections, at least three measurable objectives, an explicit out-of-scope statement, a named document owner and approval owner, plus the status Ready for sponsor review. The source ledger must contain at least seven rows; every material figure and date in the charter must trace to a verified FACT row or be labelled ASSUMPTION or UNKNOWN.

## Checkpoint and Rejoin Point

Keep the three initiation files. Lab 2 uses the charter boundaries and source ledger. To rejoin, copy the approved course checkpoint from labs/assets/checkpoint-01-initiation.md and mark its assumptions Pending validation.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The assistant adds a launch date or benefit target not present in the brief. | Delete it from the approved charter, add it to Open questions and repeat the prompt with 'Use UNKNOWN when absent.' |
| The objective sounds positive but cannot be checked. | Add a measure, target and time horizon while preserving the business intent in the source. |
| A fact has no clear source section. | Classify it as ASSUMPTION or UNKNOWN until a direct source can be cited. |

## Challenge

Ask the assistant to critique the final charter as sponsor, operations owner and delivery lead. Keep only questions that expose a real gap, cite the role that raised each one and do not let the critique alter the charter.

## Reflection

Which charter sentence was most improved by separating fact from assumption, and what decision risk did that prevent?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-build-the-stakeholder-engagement-and-communications-plan.md)
