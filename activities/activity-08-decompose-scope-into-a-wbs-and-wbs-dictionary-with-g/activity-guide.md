# Activity 8 — Decompose Scope into a WBS and WBS Dictionary with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 01:** Project Initiation and Planning with GenAI  
**Learning outcome:** LO1 — Decompose project scope into work packages with a supporting dictionary.  
**Tools:** GenAI tool · WBS Template.pptx · WBS Dictionary.xlsx

## Goal

The WBS is the backbone of the plan — everything downstream, schedule and cost, is built from it. GenAI decomposes work quickly; your job is to check the decomposition is complete and mutually exclusive.

## What you'll produce

A three-level WBS and a WBS Dictionary for your work packages.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Create a three-level work breakdown structure for implementing an internal knowledge portal for a consulting firm. Make every lowest-level item a deliverable-based work package.
```

## Step-by-step

1. In your group, prompt GenAI: 'Create a WBS for implementing an internal knowledge portal for a consulting firm.' — or use your own project scenario.
2. Organise the output into levels 1, 2 and 3 in 'WBS Template.pptx'. Level 3 items should be work packages — small enough to assign to one person or team.
3. Apply the 100% rule: the children of any node must add up to all of that node's work, with no overlap. Ask GenAI: 'Does this WBS satisfy the 100% rule? Identify any missing or overlapping work.'
4. Check for the work GenAI habitually forgets: project management effort itself, testing, training, documentation, handover and warranty support. Add what is missing.
5. Open 'WBS Dictionary.xlsx'. Prompt GenAI: 'For each work package, produce a WBS dictionary entry with WBS code, description of work, responsible role, resources required, cost estimate, quality requirements and acceptance criteria.'
6. Review each entry — particularly the acceptance criteria, which must be testable. Rewrite any that are vague ('works well' is not an acceptance criterion).
7. Confirm the flow is intact: Scope Statement → WBS → Work Packages → Activity List, ready for scheduling. Share with the class.

## Check your work

✅ Your WBS decomposes to assignable work packages, satisfies the 100% rule, includes PM/testing/training effort, and every dictionary entry has testable acceptance criteria.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*