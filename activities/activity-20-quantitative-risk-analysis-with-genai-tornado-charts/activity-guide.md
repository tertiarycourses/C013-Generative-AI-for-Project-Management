# Activity 20 — Quantitative Risk Analysis with GenAI — Tornado Charts and Decision Trees

**Course:** Generative AI for Project Management (C013)  
**Topic 03:** Managing Project Risks with GenAI  
**Learning outcome:** LO3 — Quantify risk exposure to support a financial decision.  
**Tools:** GenAI tool · Tornado Chart - Sensitivity Analysis.xlsx · Decision Tree Analysis.xlsx

## Goal

When a decision carries real money, qualitative scoring is not enough. You will run a sensitivity analysis and a decision tree, using GenAI for the setup and doing the arithmetic yourself.

## What you'll produce

A tornado chart identifying your most sensitive risk variables and a decision tree with expected monetary values.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Use the supplied high, base and low values to rank the ten variables by their effect on project cost or schedule. Produce tornado-chart data and one decision tree with expected monetary values, showing every calculation.
```

## Step-by-step

1. In your group, open 'Tornado Chart - Sensitivity Analysis.xlsx'.
2. Prompt GenAI: 'List 10 risk variables that could affect the cost or schedule of a digital transformation project. Estimate high and low values for each.'
3. Enter each variable with its high/low range and plot the bars, longest at the top. The variables at the top of the tornado are where your management attention belongs.
4. Sanity-check the ranges. GenAI produces symmetric ranges by default; real project risks are usually asymmetric — things go wrong further than they go right. Widen the downside where your experience says so.
5. Open 'Decision Tree Analysis.xlsx'. Define a real either/or decision from your project — build vs buy, or two vendors.
6. Prompt GenAI: 'Structure this decision as a decision tree. For each branch give the cost, the possible outcomes with their probabilities, and the payoff of each outcome.'
7. Calculate the Expected Monetary Value for each branch yourself: EMV = sum of (probability x payoff) for each outcome, minus the branch cost. Do NOT accept the AI's arithmetic — verify every multiplication.
8. Compare your computed EMV with GenAI's. Where they differ, find the error. This is the single most important habit when using AI for quantitative work.
9. State your recommended decision and the EMV that supports it. Share with the class.

## Check your work

✅ Your tornado chart is ordered by sensitivity with justified asymmetric ranges, and you have hand-verified the EMV of every decision tree branch.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*