# Activity 15 — Optimise Resources and Budget with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 02:** Project Execution and Delivery with GenAI  
**Learning outcome:** LO2 — Resolve over-allocation and budget pressure by modelling options with GenAI (K3).  
**Tools:** GenAI tool · your schedule from Activity 9 · Gantt Chart Template.xlsx

## Goal

This is the heart of LO2. A resource is over-allocated and the budget is under pressure — you will use GenAI to generate genuine alternatives, evaluate the trade-offs, and defend the option you choose.

## What you'll produce

A resource optimisation decision with a documented trade-off analysis.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
I have an over-allocated resource on these activities [paste] and a 15% budget reduction. Compare resource levelling, resource smoothing, crashing and fast tracking, including cost, schedule, quality and risk trade-offs.
```

## Step-by-step

1. Take your schedule from Activity 9 and deliberately create a problem: assign one person to two activities running in the same period, and cut the budget by 15%.
2. Confirm the two techniques before prompting: resource LEVELLING adjusts the schedule to fix over-allocation and may move the critical path; resource SMOOTHING adjusts only within available float, so the critical path does not change.
3. Prompt with the Alternative Approaches pattern: 'I have an over-allocated resource on these activities [paste] and a 15% budget cut. Suggest at least three options — including resource levelling, resource smoothing, crashing and fast tracking. Compare pros, cons, cost impact and schedule impact in a table.'
4. Check each option against the definitions. GenAI frequently confuses levelling with smoothing and describes crashing without noting it only works on the critical path.
5. For any crashing option, verify it targets a critical path activity — crashing a non-critical activity buys you nothing. For fast tracking, identify the rework risk it creates.
6. Apply the Cognitive Verifier pattern: 'Break down which option gives the best schedule outcome for the least cost increase and the least added risk, then combine into a recommendation.'
7. Make your group's decision, adjust the Gantt chart accordingly, and write three sentences justifying it to a sponsor.
8. Present your recommendation and state one thing GenAI got wrong about levelling, smoothing, crashing or fast tracking.

## Check your work

✅ Your chosen option is correctly named, crashing (if used) targets the critical path, and you can justify the cost/schedule/risk trade-off in three sentences.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*