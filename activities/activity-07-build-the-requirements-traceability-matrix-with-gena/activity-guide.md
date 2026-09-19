# Activity 7 — Build the Requirements Traceability Matrix with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 01:** Project Initiation and Planning with GenAI  
**Learning outcome:** LO1 — Trace every requirement from source through to test and deliverable.  
**Tools:** GenAI tool · Requirements Traceability Matrix.xlsx

## Goal

An RTM proves that what you built is what was asked for. GenAI can populate one quickly, but it will happily invent requirement sources — which is exactly the failure mode an RTM exists to prevent.

## What you'll produce

A complete Requirements Traceability Matrix with verified sources.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Generate 5 to 10 sample requirements for a smart-city parking app. Include Requirement ID, Description, Source, Acceptance Criterion and Test Case ID. Flag any requirement that is not testable.
```

## Step-by-step

1. In your group, open 'Requirements Traceability Matrix.xlsx' from the template pack.
2. Prompt GenAI: 'Generate 5-10 sample requirements for a smart city parking app. Include: Requirement ID, Description, Source, and Test Case ID.' — or use your own project.
3. Try the worked example too: 'Generate a Requirements Traceability Matrix for an e-health app for appointment booking. Include requirement ID, description, stakeholder source, and test case.' Compare the structure of the two outputs.
4. Paste the output into the template. Now audit the Source column — for each row, ask 'which real stakeholder or document did this come from?'
5. Delete or re-source every requirement whose source the AI invented. This is the single most important step in this activity.
6. Link each requirement forward to the scope statement, an acceptance criterion and a test case ID so the trace is complete end to end.
7. Prompt GenAI to check your work: 'Review this RTM. Which requirements have no test case, and which test cases do not trace back to a requirement?'
8. Fix the gaps it finds and share your matrix with the class.

## Check your work

✅ Every row traces from a real, named source through to an acceptance criterion and a test case, with no orphan requirements or orphan tests.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*