# Lab 2 — Build the Stakeholder Engagement and Communications Plan

**Course:** Generative AI for Project Management  
**Course Code:** C013  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Project Initiation and Planning with GenAI  
**Maps to:** LO1: identify stakeholders and plan evidence-led engagement and communications  
**Duration:** 80 minutes  
**Tools:** Spreadsheet · text editor · approved AI assistant · stakeholder-inputs.csv · Lab 1 charter

---

## Goal

Create a role-based stakeholder strategy with explicit decisions, messages, owners and review triggers.

## What You Will Do

You will combine the approved charter with the supplied stakeholder inputs. GenAI will help structure and challenge the plan, while you make the final influence, interest, impact and engagement decisions from evidence. The resulting communication matrix starts with the action or decision each audience needs.

## What You Will Build

02-planning/stakeholder-register.csv and stakeholder-communications-plan.md with eight stakeholder rows, current and desired engagement, owned actions, decision-focused communications and privacy safeguards.

## Prerequisites

- Completed project-charter.md and source-ledger.csv from Lab 1, or the stated rejoin checkpoint.
- Open labs/assets/stakeholder-inputs.csv and read the Data_boundary column before prompting.
- Use roles and supplied project evidence; do not add private opinions or sensitive traits.

> **Data note.** Use only the supplied synthetic BeaconWorks scenario or data you are authorised to process. Do not paste secrets, personal data or confidential commercial material into an unapproved AI service. A named human owner verifies every figure, commitment and decision.

## Steps

### 1. Copy stakeholder-inputs.csv to 02-planning/stakeholder-register.csv. Add columns Influence_1_5, Interest_1_5, Project_Impact_1_5, Current_Engagement, Desired_Engagement, Strategy, Action, Action_Owner, Review_Trigger and Evidence. Preserve Stakeholder_ID and use role names rather than personal details.

```text
Allowed engagement states: Unaware | Resistant | Neutral | Supportive | Leading
Allowed strategies: Manage closely | Keep satisfied | Keep informed | Monitor
```

### 2. Paste only the charter and permitted stakeholder rows into the assistant. Ask for proposed scores and engagement states with a short evidence citation. Require UNKNOWN when a rating cannot be supported. Enter the suggestions in temporary Proposed_* columns; do not copy them directly into final columns.

```text
For each Stakeholder_ID return Proposed influence, interest, impact, current state and desired state.
Cite only supplied evidence. Do not infer personality, demographic, political or sensitive traits.
Use UNKNOWN when evidence is absent and list one question to validate it.
```

### 3. Review each proposal. Enter final 1–5 scores and states, then choose a strategy and one observable engagement action. Add an action owner and review trigger. If your final value differs from the proposal, record the reason in Evidence. Check that high-impact affected users receive dialogue, not only broadcast.

```text
Human review gate: evidence present · impact considered · strategy proportional · owner named · trigger observable
```

### 4. Create stakeholder-communications-plan.md with a table containing Communication_ID, Audience_IDs, Purpose_or_Decision, Verified_Input, Message_Outline, Format, Channel, Cadence_or_Trigger, Sender, Feedback_Method, Record_Location and Escalation. Include a sponsor decision brief, delivery-team coordination, support-agent design review, supplier interface and launch-readiness update.

```text
Start with: What must this audience understand, decide or do?
Then specify: evidence → message → channel → feedback → record → escalation
```

### 5. Ask the assistant to produce a 120-word sponsor version and a 120-word support-agent version of the same scope-boundary update. Compare both with the charter. Save the two drafts under Audience transformation example, correct any unsupported detail and add a note explaining what changed and what stayed invariant.

```text
Use only <VERIFIED CHARTER EXTRACT>.
Draft A for sponsor: decision, tolerance, recommendation and ask.
Draft B for support agents: workflow impact, participation, timing and feedback route.
Keep facts, uncertainty and boundary identical in both.
```

## Test It

The register must contain exactly eight supplied Stakeholder_ID rows and no added personal data. Every row must have final influence, interest and impact scores; current and desired states; a strategy; an owned action; a review trigger; and evidence or UNKNOWN. The communications plan must contain at least five records and all 12 columns. The two audience drafts must preserve identical project facts and include different purpose-appropriate asks.

## Checkpoint and Rejoin Point

Keep both planning files. Lab 3 uses the acceptance owner, specialist availability, supplier interface and communication triggers. To rejoin, use stakeholder-inputs.csv and the final-value rules printed in this lab.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Every stakeholder is rated high influence and high interest. | Compare decision authority, ability to affect the work and need for detail; use the supplied anchors and evidence independently. |
| The plan contains generic actions such as 'communicate regularly'. | Name the purpose, artifact, owner, cadence or trigger and required feedback or decision. |
| The assistant infers attitude or motivation. | Delete the inference, use UNKNOWN and create a respectful validation question or engagement action. |

## Challenge

Create a second communication route for the highest-impact stakeholder if the normal channel is unavailable. State when the alternate route activates and how the official decision record remains singular.

## Reflection

Which stakeholder needed the largest shift from current to desired engagement, and what evidence-led action could create that shift?

---

[← Lab 1](lab-01-build-the-ai-working-agreement-and-project-charter.md) · [Lab 3 →](lab-03-build-the-integrated-project-management-plan.md)
