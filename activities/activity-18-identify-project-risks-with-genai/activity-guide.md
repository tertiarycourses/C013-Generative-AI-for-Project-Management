# Activity 18 — Identify Project Risks with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 03:** Managing Project Risks with GenAI  
**Learning outcome:** LO3 — Anticipate potential risks to project delivery (A3).  
**Tools:** GenAI tool · Project Manager Buddy GPT · Risk Register template

## Goal

GenAI is genuinely excellent at risk identification — it will suggest risks your team would never think of. It is correspondingly poor at knowing which of them matter to you. You will use both facts.

## What you'll produce

A populated risk register with risks sourced from GenAI and from your team.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
Act as an expert project manager in the [industry] working on a [project type]. Use the supplied project facts to draft a risk register covering cause, event, effect, category, owner and evidence. Separate facts from assumptions.
```

## Step-by-step

1. In your group, spend five minutes brainstorming risks to your project WITHOUT any AI. Write them down — this is your baseline and you will compare against it.
2. Now prompt GenAI with the Risk Matrix Template pattern: 'Imagine you are an expert project manager in the [Industry], focusing on [Project type] projects. Develop a comprehensive risk matrix. For each risk include Risk name, Description, Level of impact (high/medium/low) and Likelihood (high/medium/low). Cover budget, schedule, technology, regulatory, resource, scope creep, stakeholder, data security, quality and external dependency categories. Output as a table.'
3. Compare against your manual list. Count how many risks the AI found that your team missed — typically it will be more than half.
4. Now find the opposite: which risks did YOUR team identify that the AI missed? These are almost always the organisation-specific ones, and they are usually the ones that actually materialise.
5. Use the Risk Breakdown Structure as a checklist to find further gaps — work down from high-level categories (External, Organisational, Technical, Project Management) to specific risks.
6. For each risk, confirm it is written as a proper risk statement: cause → risk event → effect. 'The vendor may be late' is not enough; 'Because the vendor has one integration engineer, their resource may be unavailable in December, delaying UAT by two weeks' is.
7. Distinguish risks from issues as you go: risks are future and may be positive or negative and go in the risk register; issues are present, always negative, and go in the issue log.
8. Assign an owner to every risk and share your register with the class.

## Check your work

✅ Your register has risks from both sources, every entry is written as cause → event → effect with an owner, and you can name one risk your team found that the AI missed.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*