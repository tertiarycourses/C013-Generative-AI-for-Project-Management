# Activity 13 — Root Cause Analysis with GenAI — Fishbone, Five Whys and Pareto

**Course:** Generative AI for Project Management (C013)  
**Topic 02:** Project Execution and Delivery with GenAI  
**Learning outcome:** LO2 — Diagnose the root cause of a delivery problem, not just its symptoms.  
**Tools:** GenAI tool · Fishbone Diagram Template.pptx · Pareto Principle Template.xlsx

## Goal

When delivery goes wrong, the visible problem is rarely the real one. You will run three complementary root-cause techniques on the same problem with GenAI's help and compare what each reveals.

## What you'll produce

A fishbone diagram, a five-whys chain and a Pareto analysis of the same delivery problem.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Analyse the issue records provided and identify the most likely root causes of recurring project deadline misses. Produce a fishbone structure, a five-whys chain and a Pareto-ready category table without inventing evidence.
```

## Step-by-step

1. In your group, choose one real delivery problem — recurring missed deadlines, rework, defects escaping to production.
2. Open 'Fishbone Diagram Template.pptx'. Prompt GenAI: 'What are the possible root causes of recurring project deadline misses in IT infrastructure upgrades?' — substituting your problem.
3. Sort the suggested causes into the fishbone categories (People, Process, Technology, Environment, Materials, Measurement). Reclassify anything the AI put in the wrong bone.
4. Add the causes GenAI could not know — the ones specific to your organisation's politics, tooling or history. These are usually the real ones.
5. Now run Five Whys on the single most likely cause. Prompt: 'Apply the Five Whys method to [problem] to uncover the root cause and identify potential solutions.'
6. Critique the chain. GenAI tends to produce a plausible but shallow chain that stops at 'insufficient planning'. Push each 'why' until you reach something you could actually change.
7. Open 'Pareto Principle Template.xlsx'. Prompt GenAI to generate a frequency count of defect or delay categories, enter them, and identify the vital few causing roughly 80% of the impact.
8. Compare the three techniques: which surfaced the actionable cause? Share your conclusion with the class.

## Check your work

✅ You have all three artifacts for one problem, you added at least two organisation-specific causes the AI missed, and your five-whys chain ends at something you can change.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*