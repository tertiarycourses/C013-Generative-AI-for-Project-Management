# Activity 23 — Earned Value Analysis with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 03:** Managing Project Risks with GenAI  
**Learning outcome:** LO3 — Measure project performance objectively and forecast the outcome.  
**Tools:** GenAI tool · calculator

## Goal

Earned value is the one technique that tells you objectively whether you are ahead or behind, over or under. You will compute it by hand first, then test whether GenAI gets it right.

## What you'll produce

A complete earned value analysis with variances, indices and a forecast.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Using the supplied baseline, completion and actual-cost data, calculate PV, EV, AC, CV, SV, CPI, SPI, EAC and ETC. Show the formula and substitution for every result, then interpret the project status.
```

## Step-by-step

1. Work this classic scenario by hand, individually. Task: develop and install ten printer drivers. Budget: $100,000 ($10K per driver). Time: 10 weeks (1 driver per week). At week 5: 4 drivers are complete and $47,500 has been spent.
2. Compute the three base values. PV = the budget for work SCHEDULED by now. EV = the budget for work ACTUALLY DONE. AC = what has actually been spent.
3. Confirm your answers: PV = $50,000 (5 drivers scheduled x $10K). EV = $40,000 (4 drivers done x $10K). AC = $47,500.
4. Compute the variances. Cost Variance CV = EV - AC = $40,000 - $47,500 = -$7,500 (negative is bad — over budget). Schedule Variance SV = EV - PV = $40,000 - $50,000 = -$10,000 (negative is bad — behind schedule).
5. Compute the indices. CPI = EV / AC = 40,000 / 47,500 = 0.84. SPI = EV / PV = 40,000 / 50,000 = 0.80. Both below 1 — over budget and behind schedule.
6. Forecast the outcome. EAC = BAC / CPI = 100,000 / 0.84 = approximately $119,000. ETC = EAC - AC. State what you would tell the sponsor.
7. NOW test GenAI. Give it the same scenario and ask for PV, EV, AC, CV, SV, CPI, SPI and EAC. Compare every figure against yours.
8. Where it differs, identify the error. GenAI commonly confuses EV with AC, or computes EAC without using CPI. This is precisely why you must be able to do this by hand.
9. Discuss as a group: the assessment is open book, but the arithmetic is yours. What is the minimum you must be able to compute without help?

## Check your work

✅ You can compute PV, EV, AC, CV, SV, CPI, SPI and EAC unaided for a fresh scenario, and you found at least one error in the AI's version.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*