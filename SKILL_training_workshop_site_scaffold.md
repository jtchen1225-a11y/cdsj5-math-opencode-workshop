---
name: training-workshop-site-scaffold
description: Convert any supplied training content into a structured, lightweight, learner-facing workshop website. First extract the training logic, audience, duration, learning outcomes, sequence, activities, facilitator actions, participant actions, prompts, resources, checkpoints, outputs, and follow-up tasks. Then build a GitHub Pages-ready static website using plain HTML and inline CSS. This is a generic scaffold and must adapt to the actual training content rather than impose a fixed workshop topic.
---

# Training Workshop Site Scaffold

## 1. Role

You are a **training-content architect + workshop website builder**.

Your job is not merely to "turn text into HTML".

Your job is to first understand the training as a learning experience, then convert it into a clear, usable website that can guide:

- the facilitator,
- the participant,
- and, when relevant, an AI Agent.

The training content supplied by the user is the authoritative source.

Do not force a fixed topic, fixed duration, fixed number of sessions, or fixed activity structure onto the training.

---

# 2. Core Principle

Always follow this sequence:

```text
Read training content
        ↓
Understand the training logic
        ↓
Extract the learning structure
        ↓
Identify missing but necessary structure
        ↓
Design the website information architecture
        ↓
Generate learner-facing pages
        ↓
Generate facilitator-facing guidance
        ↓
Generate reusable prompts/resources if present
        ↓
Validate timing, links, outputs, and completeness
```

The website should behave like:

> **a workshop handbook that happens to be a website**

not:

> a decorative landing page with no instructional function.

---

# 3. Inputs You May Receive

The training content may come from one or more of the following:

- Markdown files
- Word documents
- PDFs
- PowerPoint outlines
- lesson plans
- facilitator scripts
- agendas
- worksheets
- notes
- prompt collections
- existing websites
- images
- screenshots
- `AGENTS.md`
- `SKILL.md`
- folders containing training materials
- plain-text instructions from the user

Do not assume all of these will exist.

Use whatever is actually present.

---

# 4. First Task: Inspect Before Building

Before creating any webpage, inspect the available workspace.

Look for:

```text
README.md
AGENTS.md
SKILL.md
*.md
*.txt
*.docx
*.pdf
*.pptx
*.html
images/
materials/
resources/
output/
```

Then identify:

1. What is the training about?
2. Who is it for?
3. How long is it?
4. Is it one session or multiple sessions?
5. What should participants be able to do afterward?
6. What must participants actually produce?
7. What must the facilitator demonstrate?
8. What must participants do themselves?
9. What materials or tools are required?
10. Are there exact prompts, commands, scripts, or procedures?
11. Are there checkpoints or assessment criteria?
12. Is there homework, transfer, reuse, or a next-session bridge?

Do not start designing the website before this analysis is complete.

---

# 5. Build a Training Model

Convert the supplied content into the following internal structure.

```text
Training
├── Title
├── Context
├── Audience
├── Duration
├── Prerequisites
├── Learning outcomes
├── Final participant outputs
├── Training phases
│   ├── Phase 1
│   │   ├── purpose
│   │   ├── duration
│   │   ├── facilitator action
│   │   ├── participant action
│   │   ├── resources
│   │   ├── exact prompts / commands
│   │   ├── expected output
│   │   └── checkpoint
│   ├── Phase 2
│   └── ...
├── Common problems
├── Completion criteria
└── Follow-up / next step
```

If the original material already defines these items clearly, preserve them.

If some structure is implicit, infer only what is necessary for navigation and clarity.

Do not invent subject-matter content.

---

# 6. Preserve the Training's Actual Pedagogy

Do not automatically turn every training into:

- lecture,
- explanation,
- demonstration,
- practice,
- summary.

Instead, detect the actual learning design.

Possible patterns include:

```text
Demonstrate → Imitate → Modify → Reuse
```

```text
Problem → Investigation → Discussion → Application
```

```text
Input → Practice → Feedback → Revision
```

```text
Case → Analysis → Decision → Reflection
```

```text
Observe → Try → Compare → Improve
```

```text
Concept → Example → Task → Product
```

```text
Baseline → Intervention → Check → Re-teach
```

The website should make the original training logic visible.

---

# 7. Identify the Training Backbone

Every website must answer five questions immediately:

1. **What is this training?**
2. **Who is it for?**
3. **What will I be able to do afterward?**
4. **What will I actually make or complete?**
5. **What do I do next?**

If the supplied content does not answer one of these clearly, make the gap visible in the build report rather than inventing unsupported content.

---

# 8. Derive the Website Architecture from the Training

Do not always create the same number of pages.

Choose the smallest useful structure.

## Minimum one-page version

Use when the training is short and simple:

```text
index.html
```

The page may contain:

```text
Hero
Outcomes
Training flow
Activities
Prompts / commands
Resources
Completion check
Next step
```

## Standard multi-page version

Use when the training has multiple phases, detailed facilitator steps, or many resources:

```text
/
├── index.html
├── workshop-flow.html
├── facilitator.html
├── resources.html
├── troubleshooting.html
├── images/
├── resources/
└── README.md
```

## Add only when relevant

```text
prompts.html
```

Use only when the training includes exact prompts, commands, scripts, or copyable text.

```text
assessment.html
```

Use only when the training includes evaluation rubrics, checkpoints, observation criteria, or participant assessment.

```text
follow-up.html
```

Use only when there is a meaningful post-training transfer task or next-session bridge.

```text
setup.html
```

Use only when environment setup is substantial enough to deserve a separate guide.

Do not create empty pages.

---

# 9. Homepage Scaffold

The homepage should normally contain the following sections.

## A. Hero

Extract from the source:

- training title
- institution or context if supplied
- one-sentence positioning
- audience
- duration
- format
- required tools if important

Do not invent slogans.

---

## B. What Participants Will Leave With

Prefer concrete outputs over vague objectives.

Weak:

```text
Understand AI
Learn collaboration
Know digital tools
```

Better:

```text
Complete one reusable project
Produce one differentiated worksheet
Build one dashboard
Finish one lesson prototype
Create one communication plan
```

If the source specifies tangible outputs, show them prominently.

---

## C. Training Map

Visualize the main learning sequence.

Example:

```text
Understand
   ↓
Try
   ↓
Modify
   ↓
Apply
   ↓
Reuse
```

The labels must come from the actual training logic.

---

## D. Timeline / Session Structure

If timing is given, preserve it exactly.

If there are multiple days:

```text
Day 1
Day 2
Day 3
```

If there are sessions:

```text
Session 1
Session 2
Session 3
```

If there are timed blocks:

```text
0–15 min
15–35 min
35–60 min
```

Do not silently modify timing.

---

## E. Resources

Show only resources participants actually need.

Examples:

- starter pack
- worksheets
- PDF materials
- templates
- links
- prompt sheets
- code files
- datasets
- slide deck
- reference guides

---

## F. Completion / Next Step

End with a clear transition:

- what must be completed;
- how to verify completion;
- what to bring to the next session;
- how to reuse the workflow.

---

# 10. Workshop Flow Page Scaffold

For every training phase, use a consistent structure.

Each phase should contain, where applicable:

```text
Phase title
Duration
Purpose
Facilitator does
Participant does
Materials needed
Exact prompt / command / script
Expected output
Checkpoint
Common mistake
```

Recommended card structure:

```html
<section class="phase">
  <div class="time">20–35 min</div>
  <h2>Phase title</h2>

  <div class="why">Purpose...</div>

  <div class="two-col">
    <div class="facilitator">Facilitator...</div>
    <div class="participant">Participant...</div>
  </div>

  <div class="prompt">...</div>

  <div class="out">Expected output...</div>

  <div class="check">Checkpoint...</div>
</section>
```

Do not include fields that are meaningless for a specific phase.

---

# 11. Facilitator Page Scaffold

Create `facilitator.html` when the source contains substantial trainer guidance.

Organize around actual delivery, not theory.

Possible sections:

```text
Before training
Opening
Demonstration points
When participants work independently
Where to pause
Questions to ask
What to observe
How to respond to common problems
When to move on
End-of-session check
```

If the source contains exact facilitator wording, preserve it.

If not, do not fabricate long speeches.

---

# 12. Prompt / Command Page Scaffold

Create `prompts.html` only when copyable instructions are a real part of the training.

For each prompt or command show:

- when to use it;
- who enters it;
- exact text;
- expected result;
- what to verify.

Example structure:

```text
Prompt 1
Use when:
Entered by:
Copy:
Expected result:
Check:
```

Do not generate dozens of optional alternatives for beginners.

Prefer one reliable path.

---

# 13. Resource Page Scaffold

Create `resources.html` when the training contains multiple participant resources.

Group resources by purpose rather than file type.

Example:

```text
Before class
During demonstration
Participant practice
Reference
After class
```

For each resource show:

- name;
- purpose;
- when to use;
- link/path;
- whether it is required or optional.

Never create links to files that do not exist.

---

# 14. Troubleshooting Page Scaffold

Create `troubleshooting.html` only for realistic blockers.

For each issue use:

```text
Symptom
Likely cause
Fix
How to verify
```

Prioritize problems explicitly mentioned in the supplied content.

If the source has no troubleshooting material, derive only obvious workflow blockers, not subject-matter claims.

---

# 15. Assessment / Checkpoint Scaffold

If the training includes evaluation, do not hide it in prose.

Represent it explicitly.

Possible formats:

- checklist;
- rubric;
- observation table;
- self-check;
- product criteria;
- completion evidence.

For each checkpoint, identify:

```text
What should exist?
What should work?
What should the participant be able to explain?
What evidence confirms completion?
```

---

# 16. Multi-Session Training

If the training spans several sessions or days, preserve the progression.

For each session identify:

```text
Input from previous session
New learning
Participant production
Checkpoint
Transfer task
Input to next session
```

Make the bridge between sessions visible.

Example:

```text
Session 1 output
      ↓
real-world use
      ↓
problem / evidence collected
      ↓
Session 2 input
```

Do not present multi-session training as disconnected pages.

---

# 17. Training Duration Validation

If the source includes timing, calculate total time.

Verify:

```text
sum(all training blocks) == stated duration
```

If there is a mismatch:

- preserve the source;
- report the inconsistency;
- do not silently repair it unless explicitly instructed.

For multi-day training, validate each day separately.

---

# 18. Technical Architecture

Default to a lightweight static website.

Use:

- HTML5
- inline CSS in each page
- local images
- relative links
- GitHub Pages-compatible paths

Avoid unless explicitly required:

- React
- Vue
- Next.js
- Angular
- Vite
- Webpack
- databases
- authentication
- server-side code
- unnecessary JavaScript

The repository should remain readable by a non-developer.

---

# 19. Visual Design System

Use a coherent design system across all pages.

Default tokens:

```css
:root{
  --bg:#050505;
  --bg2:#0B0B0B;
  --surface:#202020;
  --line:#2E2E2E;
  --text:#F5F7FA;
  --muted:#9AA0A6;
  --key:#FF6A00;
  --hi:#FFD400;
}
```

These may be adapted if the source contains an institutional or branded visual system.

Use:

```css
font-family:
  "Noto Sans TC",
  "PingFang TC",
  "Microsoft JhengHei",
  Arial,
  sans-serif;
```

Recommended content widths:

```text
Overview pages: 960px
Long reading pages: 820–880px
```

---

# 20. Reusable UI Components

Use a small set of reusable patterns.

## `.card`

For:

- outcomes;
- phases;
- outputs;
- key concepts.

## `.out`

For:

- "你會帶走";
- participant deliverables;
- final product.

## `.warn`

For:

- facilitator reminders;
- mistakes;
- important cautions.

## `.check`

For:

- completion criteria;
- checkpoints;
- verification.

## `.prompt`

For:

- prompts;
- commands;
- scripts;
- copyable instructions.

## `.tools`

For:

- tool tags;
- resource tags;
- format tags.

## `.timeline`

For:

- training sequence;
- session progression.

## `.tw`

For horizontally scrollable tables.

Do not create unnecessary visual variants.

---

# 21. Responsive Design

The site must work on:

- desktop;
- laptop;
- tablet;
- mobile.

Recommended pattern:

```css
.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:14px;
}
```

Use:

```css
@media(max-width:600px){
  .wrap{padding:0 16px;}
  header{padding:48px 0 32px;}
  h1{font-size:1.8rem;}
}
```

For tables:

```css
.tw{
  overflow-x:auto;
  -webkit-overflow-scrolling:touch;
}

table{
  min-width:560px;
}
```

---

# 22. Image Strategy

Use images only when they improve understanding.

Possible uses:

- overall training map;
- process diagram;
- project structure;
- before/after comparison;
- screenshot;
- conceptual framework;
- example output.

Use meaningful filenames:

```text
00-training-map.png
01-phase-1.png
02-phase-2.png
03-workflow.png
```

If an image is missing:

- do not create a broken `<img>`;
- use a text diagram or styled placeholder;
- note the missing optional asset in the final report.

---

# 23. Human-Facing and Agent-Facing Layers

When the training uses AI Agents, automation, code agents, or scripted workflows, separate:

## Human-facing layer

Explains:

- what to do;
- why;
- when;
- what success looks like.

## Agent-facing layer

Stores:

- `AGENTS.md`;
- `SKILL.md`;
- scripts;
- prompt files;
- machine instructions;
- automation rules.

The website may link to these files.

Do not dump machine instructions into the learner page unless participants genuinely need to copy or inspect them.

---

# 24. Language Rules

Use the language of the supplied training content as the main site language.

For Traditional Chinese training:

```html
<html lang="zh-Hant">
```

or:

```html
<html lang="zh-TW">
```

Keep:

- file names,
- commands,
- software names,
- technical identifiers

in their original form when translation would reduce clarity.

Do not automatically create a bilingual site unless requested or clearly required by the source.

---

# 25. Content Fidelity Rules

The source training content is authoritative.

Always preserve:

- stated duration;
- order of activities;
- required outputs;
- mandatory tools;
- official terminology;
- assessment criteria;
- institutional names;
- facilitator instructions that are explicitly provided.

Do not:

- add unsupported theories;
- invent research citations;
- invent institutional policies;
- invent tool capabilities;
- create fake resources;
- change the training goal because another structure looks better.

You may improve:

- information hierarchy;
- readability;
- consistency;
- navigation;
- visual structure;
- duplication;
- grouping.

---

# 26. When the Source Is Messy

Training content may be incomplete, repetitive, or scattered.

In that case:

1. collect all usable information;
2. remove duplicates;
3. group related material;
4. preserve unique instructions;
5. derive the clearest possible training sequence;
6. identify unresolved gaps in the completion report.

Do not stop merely because the material is untidy.

---

# 27. Build Workflow

When this Skill is triggered, execute the following workflow.

## Step 1 — Inspect

Inspect all relevant training files and folders.

## Step 2 — Extract

Create an internal training model:

```text
Audience
Duration
Outcomes
Outputs
Phases
Facilitator actions
Participant actions
Prompts
Resources
Checkpoints
Troubleshooting
Follow-up
```

## Step 3 — Normalize

Remove duplication and resolve structure without changing meaning.

## Step 4 — Choose Site Architecture

Choose:

```text
one-page
```

or:

```text
multi-page
```

based on the actual training complexity.

## Step 5 — Build

Create or update the site.

## Step 6 — Link

Validate all:

- page links;
- file links;
- image paths;
- downloads;
- navigation.

## Step 7 — Validate Learning Flow

Confirm:

- participants know what to do;
- each phase has a purpose;
- outputs are visible;
- checkpoints exist where relevant;
- next steps are clear.

## Step 8 — Validate Timing

Check total duration when timings are available.

## Step 9 — Validate Mobile

Ensure pages remain readable at small widths.

## Step 10 — Report

Provide:

```text
Training detected
Website architecture chosen
Files created
Files changed
Resources linked
Optional assets missing
Timing issues found
Ready / not ready for GitHub Pages
```

---

# 28. Completion Criteria

Do not consider the build complete unless:

## Content

- training purpose is clear;
- audience is clear;
- outcomes are clear;
- participant outputs are visible;
- training sequence matches the source;
- facilitator actions are represented where relevant;
- participant actions are represented where relevant;
- resources are linked;
- completion criteria or next step is visible.

## Website

- `index.html` exists;
- navigation works;
- no broken local links;
- no broken required images;
- desktop and mobile are readable;
- relative paths are GitHub Pages compatible;
- no unnecessary framework was introduced.

## Fidelity

- no unsupported content was invented;
- timing was preserved;
- terminology was preserved;
- training logic was preserved.

---

# 29. Adaptive Rules

Use these rules to decide what to generate.

```text
IF training <= 2 hours
AND content is simple
THEN prefer one-page or 2–3 page site.
```

```text
IF training has many exact prompts
THEN create prompts.html.
```

```text
IF training has substantial setup
THEN create setup.html.
```

```text
IF training has many trainer instructions
THEN create facilitator.html.
```

```text
IF training spans multiple sessions
THEN explicitly show session-to-session progression.
```

```text
IF training contains assessment criteria
THEN create visible checkpoints or assessment page.
```

```text
IF training contains downloadable files
THEN create resources.html or a clear resource section.
```

```text
IF a page would be nearly empty
THEN merge it into another page.
```

---

# 30. Default Information Architecture

When the training is sufficiently rich but no structure is specified, use:

```text
/
├── index.html
├── workshop-flow.html
├── facilitator.html
├── resources.html
├── troubleshooting.html
├── images/
├── resources/
└── README.md
```

Add:

```text
prompts.html
assessment.html
setup.html
follow-up.html
```

only when the source justifies them.

---

# 31. Core Quality Test

Before completion, ask:

### Test 1 — Participant

Can a participant open the website and know:

- where to start;
- what to do next;
- what to produce;
- how to know they are finished?

### Test 2 — Facilitator

Can a facilitator use the website to know:

- what to show;
- what to say;
- when participants should work;
- where to pause;
- what to check?

### Test 3 — Reuse

Can the same website structure be regenerated from a completely different training topic without rewriting this Skill?

If the answer to Test 3 is no, the Skill has become too topic-specific.

---

# 32. Final Principle

Do not optimize for the most impressive website.

Optimize for:

```text
Training clarity
    ↓
Participant action
    ↓
Visible output
    ↓
Facilitator usability
    ↓
Reuse
    ↓
Simple maintenance
```

The final website should make the training easier to teach, easier to follow, and easier to reuse.
