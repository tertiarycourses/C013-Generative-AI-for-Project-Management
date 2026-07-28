# C013---Generative-AI-for-Project-Management

Aligned commercial courseware for **Generative AI for Project Management (C013)**.

## Package

- Trainer slide deck (`.pptx`) and learner slides (`.pdf`)
- Learner Guide (`.docx`, `.pdf` and Markdown mirror)
- Lesson Plan (`.docx` and `.pdf`)
- Nine connected hands-on labs with synthetic project evidence

The package is generated from one source:
`.agents/skills/non-wsq-courseware-build/build/course_data.py` and
`data_domain1.py` through `data_domain3.py`.

## Build

From Git Bash on Windows:

```bash
COURSE_REPO="$PWD" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

## Quality check

```bash
python ".agents/skills/non-wsq-courseware-qa/scan_prohibited.py" .
```

The learner-facing package contains project-management knowledge, worked examples
and connected practice. Generated AI content remains subject to evidence checks and
named human approval.
