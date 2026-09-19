# Activity 9 — Build the Schedule and Find the Critical Path with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 01:** Project Initiation and Planning with GenAI  
**Learning outcome:** LO1 — Sequence activities, estimate durations and identify the critical path.  
**Tools:** GenAI tool · Gantt Chart Template.xlsx · Schedule Network Diagram.xlsx

## Goal

You will turn your work packages into a sequenced, estimated schedule, draw the network diagram, and compute the critical path — then check whether GenAI's arithmetic can be trusted.

## What you'll produce

A Gantt chart, a schedule network diagram and a calculated critical path.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Using the task data provided, propose a project schedule for building a CRM system. Preserve the stated dependencies, identify the critical path and show your forward-pass and backward-pass calculations.
```

## Step-by-step

1. In your group, prompt GenAI: 'Generate a list of tasks with estimated durations for building a CRM system over 8 weeks.' Open 'Gantt Chart Template.xlsx'.
2. Enter the tasks and durations, then add dependencies. Classify each dependency as Mandatory, Discretionary, External or Internal — GenAI will not do this correctly for your context.
3. Apply three-point estimating to your five most uncertain tasks. Prompt: 'For each task give an optimistic, most likely and pessimistic duration.' Compute the PERT estimate yourself: (O + 4M + P) / 6.
4. Compare the PERT figure with GenAI's single-point estimate. Note how much optimism was hidden in the original number.
5. Open 'Schedule Network Diagram.xlsx'. Prompt: 'List 10 project tasks with durations and dependencies for developing an internal helpdesk ticketing system.'
6. Enter activities, durations and dependencies, then perform the forward and backward pass to find each activity's float.
7. Determine the critical path — the sequence with zero float — and calculate the total project duration.
8. Now verify GenAI: ask it to compute the critical path for the same network, and compare with your manual answer. Where they differ, work out which is right and why.
9. Share your critical path and total duration with the class.

## Check your work

✅ You can state the critical path, the total duration and the float on at least one non-critical activity, and you have checked GenAI's computed path against your own.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*