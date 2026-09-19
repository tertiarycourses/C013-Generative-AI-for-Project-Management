# Activity 21 — Plan Risk Responses with GenAI

**Course:** Generative AI for Project Management (C013)  
**Topic 03:** Managing Project Risks with GenAI  
**Learning outcome:** LO3 — Devise risk mitigation measures to ensure project success (A4).  
**Tools:** GenAI tool · your risk register from Activities 18-19

## Goal

A risk register with no responses is a list of things you will be surprised by. You will plan a response for every priority risk and check for the second-order effects that responses create.

## What you'll produce

A response plan for every priority risk, with owners, triggers and fallback plans.

## Activity files

- [Activity guide PDF](./activity-guide.pdf)
- [Prompt sheet](./prompts.pdf)
- [Detailed instruction manual](./instruction-manual.pdf)
- [Mock data workbook](./mock-data.xlsx)

## Core prompt

```text
For each priority risk [paste], recommend one primary response strategy from avoid, transfer, mitigate, accept, escalate, exploit, share or enhance. Give the action, owner, trigger, fallback and response cost.
```

## Step-by-step

1. Confirm the eight response strategies. For threats: Avoid, Transfer, Mitigate, Accept. For opportunities: Exploit, Share, Enhance, Accept. Escalate applies to both when the risk is outside your authority.
2. Prompt GenAI: 'For each of these priority risks [paste], recommend a response strategy from avoid, transfer, mitigate, accept, escalate, exploit, share or enhance. Give the specific action, an owner role, the trigger condition, and the estimated cost of the response.'
3. Audit the strategy names. GenAI routinely labels a mitigation as an avoidance — avoiding a risk means eliminating the cause entirely, usually by changing the plan, not by reducing the likelihood.
4. Check the cost logic: a response costing more than the risk exposure it removes is a bad response. Prompt: 'For each response, compare its cost against the risk exposure (probability x impact). Flag any response that costs more than the exposure.'
5. Identify SECONDARY risks — new risks created by your responses. Prompt: 'What new risks does each of these responses introduce?' Transferring risk to a vendor, for instance, creates vendor dependency risk.
6. Identify RESIDUAL risk — what remains after the response is implemented. Every accepted residual risk needs a contingency plan and a contingency reserve.
7. Write a fallback plan for your top three risks: what you do if the primary response fails.
8. Define the trigger condition for each response — the observable signal that tells you to act. A response with no trigger is never implemented in time.
9. Update your register and share your top three responses with their triggers and fallbacks.

## Check your work

✅ Every priority risk has a correctly-named strategy, an owner, an observable trigger, an identified secondary and residual risk, and your top three have fallback plans.

---

**Remember:** GenAI gives you a fast first draft. Check every figure, source and assumption before the output leaves your hands — you remain accountable for it.

*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.*