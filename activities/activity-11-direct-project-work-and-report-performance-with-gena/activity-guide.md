# Activity 11 — Direct Project Work and Report Performance with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 02:** Project Execution and Delivery with GenAI  
**Learning outcome:** LO2 — Turn raw project data into work performance information and reports.  
**Tools:** GenAI tool · Project Manager Buddy GPT

## Goal

Executing a project generates a flood of raw data. You will use GenAI to turn that data into information, and information into a report a sponsor will actually read — while learning the distinction that PMBOK draws between the three.

## What you'll produce

A project status report generated from raw work performance data.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Here is raw work performance data from my project [paste]. Compare it with the plan, distinguish data from interpretation, and produce a one-page status report for an executive sponsor.
```

## Step-by-step

1. In your group, write out ten lines of raw work performance data for a project in progress — for example '14 defects open', 'actual cost to date $62,000', '3 change requests raised'.
2. Confirm the distinction before you prompt: Data is the raw observation; Information compares two or more data points to make it meaningful; a Report is the representation intended to raise action or awareness.
3. Prompt GenAI: 'Here is raw work performance data from my project [paste]. Convert it into work performance information by comparing against the plan, then produce a one-page status report for an executive sponsor.'
4. Check what it inferred. It will assume a baseline you never gave it — identify every comparison it invented and supply the real planned figure.
5. Prompt it to sharpen the report: 'Rewrite this so the first three lines tell the sponsor whether the project is on track, what the single biggest problem is, and what decision I need from them.'
6. Add a version control block — version number, date/time stamp and author — as required for project document control.
7. Use the Persona pattern to test it: 'Act as a sceptical project sponsor. What would you challenge in this report?' Address the challenges it raises.
8. Share your report and state which figure GenAI fabricated before you corrected it.

## Check your work

✅ Your report distinguishes data from information, every comparison uses a real baseline figure, and it opens with status, biggest problem and the decision required.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*