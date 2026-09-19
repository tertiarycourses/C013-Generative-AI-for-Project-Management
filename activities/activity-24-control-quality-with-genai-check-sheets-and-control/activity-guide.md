# Activity 24 — Control Quality with GenAI — Check Sheets and Control Charts

**Course:** Generative AI for Project Management (C013)  
**Topic 03:** Managing Project Risks with GenAI  
**Learning outcome:** LO3 — Detect whether a process is stable and in control.  
**Tools:** GenAI tool · Check Sheets.xlsx · Control Chart.xlsx

## Goal

Quality control is about detecting problems from data rather than opinion. You will collect data on a check sheet and plot a control chart, applying the rule of seven.

## What you'll produce

A check sheet of collected data and a control chart with limits and a trend assessment.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Use the supplied defect log to produce a check-sheet summary and control-chart data. Calculate the centre line and control limits, identify any special-cause signal and explain what additional evidence is needed.
```

## Step-by-step

1. In your group, open 'Check Sheets.xlsx'. Prompt GenAI: 'Design a check sheet to collect defect data for [your project's deliverable]. Suggest the defect categories and the collection frequency.'
2. Confirm the categories are mutually exclusive — a defect must fall into exactly one. Fix any overlap the AI created.
3. Populate the check sheet with 20 data points, either real data or a plausible set your group agrees on.
4. Open 'Control Chart.xlsx'. Enter your data and compute the mean, the upper control limit and the lower control limit.
5. Understand the distinction: control limits come from the process itself (what it actually does); specification limits come from the customer (what they require). A process can be in control and still fail the specification.
6. Apply the rule of seven: seven consecutive points on the same side of the mean, or seven consecutively increasing or decreasing, indicates a trend requiring investigation — even if no point breaches a control limit.
7. Prompt GenAI: 'Analyse this control chart data. Is the process in control? Are there any runs of seven? What would you investigate?' Verify its answer against your own reading of the chart.
8. Follow the full control quality sequence: check sheet → histogram → Pareto → cause-and-effect → scatter analysis. State which step you would do next and why.
9. Share whether your process is in control and what you would investigate.

## Check your work

✅ Your control chart has a mean and both control limits, you have checked for runs of seven, and you can distinguish control limits from specification limits.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*