# Activity 10 — Estimate Costs and Build the Budget with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 01:** Project Initiation and Planning with GenAI  
**Learning outcome:** LO1/LO2 — Produce a defensible cost baseline with appropriate reserves.  
**Tools:** GenAI tool · Cost Benefit Analysis.xlsx · your WBS from Activity 8

## Goal

You will apply the four estimating techniques to the same work, compare what each produces, and assemble a cost baseline with contingency and management reserves.

## What you'll produce

A cost baseline built bottom-up from your WBS, with reserves and a documented estimating basis.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Estimate the cost of each work package in this WBS using bottom-up estimating. Show assumed rates and quantities separately from totals, then add contingency and management reserves without double counting.
```

## Step-by-step

1. Using the WBS from Activity 8, prompt GenAI: 'Estimate the cost of each work package in this WBS using bottom-up estimating. Show your assumed rates and quantities separately from the totals.'
2. Ask for the same total three more ways: analogous ('estimate from a similar past project'), parametric ('use a rate per unit') and three-point ('give optimistic, most likely and pessimistic').
3. Compute the three-point estimate yourself using Ce = (Co + 4Cm + Cp) / 6 and compare all four figures. Explain to your group why they differ and which you would defend to a sponsor.
4. Challenge the assumed rates. Prompt: 'Which of these rates did you assume rather than know? Mark each with [ASSUMPTION].' Replace them with rates from your own organisation.
5. Roll the work package costs up to a project total — this is your cost baseline before reserves.
6. Add a contingency reserve for the identified risks you will quantify in Topic 3, and a management reserve for unforeseen in-scope work. Prompt GenAI to suggest a percentage and to justify it, then decide your own figure.
7. Confirm you can state the difference: contingency reserve is inside the cost baseline for known risks; management reserve sits outside it for unknown work.
8. Share your baseline and the reserve percentages you chose, with your justification.

## Check your work

✅ You have one cost baseline built bottom-up, four comparable estimates for the same work, no unmarked assumed rates, and a stated contingency and management reserve you can justify.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*