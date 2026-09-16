---
name: math-agent-workshop-2h-site
description: Build and maintain a lightweight GitHub Pages workshop website for a 2-hour OpenCode / AI Agent training for primary mathematics teachers. The workshop must lead beginners through one complete cycle: first preparation, differentiated version, synchronized revision, reuse, and recording a real classroom problem for the next session. Use plain HTML, inline CSS, images, and human-readable Agent instructions; do not introduce unnecessary web frameworks.
---

# Math Agent Workshop 2H Site

## 1. Purpose

Create or update a lightweight workshop website for a **2-hour OpenCode / AI Agent practical training for primary mathematics teachers**.

The target participants are:

- Primary-school mathematics teachers from the Chinese and English sections.
- Most participants have used generative AI before.
- Most participants are beginners in AI Agents and OpenCode.
- Participants should not be expected to understand programming.
- Every participant should leave with a usable result, not only conceptual knowledge.

The workshop is not a general introduction to AI.

Its core learning loop is:

> Real teaching material → Agent reads project rules → teacher confirms requirements → first preparation → differentiation → synchronized revision → reuse → bring a real classroom problem into the next workshop.

The website must help a teacher understand **what to do, when to do it, what to type, what should be produced, and how to reuse it later**.

---

## 2. Non-negotiable Workshop Outcomes

By the end of the 120-minute workshop, each teacher should have completed:

1. One real preparation task based on an actual mathematics PDF.
2. One differentiated version for learners with different needs.
3. One synchronized revision in which a change in teaching requirements is propagated through related outputs.
4. One reuse task showing that the same project can be used again without rebuilding everything.
5. One recorded real classroom problem to bring into the next workshop.

Do not redesign the workshop into a lecture-heavy format.

Do not spend most of the workshop explaining AI theory.

Do not make coding the learning objective.

The central experience must be:

> "I gave the Agent my real material, I controlled the requirements, I modified the result, and I can use the same workflow again."

---

## 3. Required Training Project Structure

When explaining or demonstrating the teacher project, use this conceptual structure:

```text
Math-Agent-Workshop/
├── AGENTS.md
├── materials/
│   ├── 把教材放在這裡.txt
│   └── P5-分數加減法-示範教材.pdf
├── requirements/
│   └── task-spec.md
├── output/
│   ├── 01-first-version/
│   ├── 02-differentiated/
│   ├── 03-revised/
│   └── 04-reused/
└── notes/
    └── next-workshop-problem.md
```

Interpret the folders as follows:

- `AGENTS.md`: stable project rules and teacher preferences.
- `materials/`: source teaching materials; never modify the originals.
- `requirements/task-spec.md`: requirements confirmed between teacher and Agent before generation.
- `output/01-first-version/`: first usable teaching output.
- `output/02-differentiated/`: differentiated version.
- `output/03-revised/`: synchronized revised version.
- `output/04-reused/`: a new output created by reusing the same workflow.
- `notes/next-workshop-problem.md`: a real classroom problem for the next training session.

If the existing workspace already uses equivalent folder names, preserve the existing structure instead of renaming it unnecessarily.

---

## 4. Website Technical Architecture

Build the site as a simple static documentation website.

### Required technology

Use:

- Plain HTML5.
- CSS written inside each HTML file using `<style>`.
- Local PNG/JPG/WebP images when provided.
- Relative links.
- GitHub Pages compatible paths.

Avoid:

- React.
- Vue.
- Next.js.
- Angular.
- Vite.
- Webpack.
- Node-based build pipelines.
- Databases.
- Server-side code.
- Login systems.
- Heavy JavaScript frameworks.

JavaScript should not be added unless a requested interaction cannot reasonably be achieved with HTML/CSS alone.

The website should remain understandable by a teacher who opens the repository and reads the files directly.

---

## 5. Visual System

Use a consistent dark workshop-documentation style.

Recommended design tokens:

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

Use a system font stack suitable for Traditional Chinese:

```css
font-family:
  "Noto Sans TC",
  "PingFang TC",
  "Microsoft JhengHei",
  Arial,
  sans-serif;
```

Layout rules:

- Main content width: maximum 960px.
- Long guide pages: 820–880px is acceptable.
- Desktop and mobile must both be readable.
- Use CSS Grid for cards.
- Use Flexbox for tool tags.
- Use horizontal overflow for wide tables.
- Use one main orange accent and one yellow highlight.
- Use generous vertical spacing.
- Do not create visual complexity merely for decoration.

---

## 6. Required Reusable UI Components

The site should use a small, consistent component system.

At minimum include:

### `.card`
For outputs, steps, or workshop activities.

### `.warn`
For lecturer reminders, common mistakes, or attention points.

### `.out`
For "你會帶走 / You will leave with" outputs.

### `.tools`
For tags such as OpenCode, AGENTS.md, PDF, AI Agent, GitHub, Reuse.

### `.timeline`
For the 120-minute training sequence.

### `.prompt`
For exact lecturer or teacher text to enter into OpenCode.

### `.check`
For completion criteria.

### `.tw`
Wrapper around tables to allow horizontal scrolling on mobile.

Do not create dozens of unique components when the same visual pattern can be reused.

---

## 7. Required Website File Structure

Prefer this structure:

```text
/
├── index.html
├── workshop-flow.html
├── prompts.html
├── troubleshooting.html
├── images/
├── resources/
├── skills/
│   └── math-agent-workshop-2h-site/
│       └── SKILL.md
└── README.md
```

### `index.html`
Acts as the learner-facing overview.

### `workshop-flow.html`
Contains the full 120-minute practical flow.

### `prompts.html`
Contains the exact text the lecturer and teachers enter into OpenCode.

### `troubleshooting.html`
Contains only high-frequency beginner problems that can realistically happen during the workshop.

### `images/`
Contains workshop diagrams and screenshots.

### `resources/`
Contains downloadable or referenced learning materials when available.

### `skills/`
Contains Agent-readable instructions.

Do not create empty pages only to make the website appear larger.

---

## 8. Homepage Information Architecture

The homepage should be organized in this order.

### Section A — Hero

Show:

- School / workshop context when supplied.
- Workshop title.
- One-sentence positioning.
- Duration: 2 hours.
- Target: primary mathematics teachers.
- Beginner friendly.
- A clear statement that participants will complete a reusable Agent workflow.

Suggested positioning:

> 從一份真實數學教材開始，用 OpenCode 完成一次備課、一次分層、一次同步修訂和一次重用。

Do not exaggerate claims about AI replacing teachers.

### Section B — What You Will Leave With

Use four primary cards:

1. **第一次備課**
   - Agent reads real teaching material.
   - Teacher confirms requirements.
   - Produces a usable first version.

2. **分層**
   - Convert the same task into differentiated versions.
   - Preserve common learning goals.
   - Adjust support, complexity, or challenge.

3. **同步修訂**
   - Teacher changes a real requirement.
   - Agent updates related outputs consistently.
   - Teacher verifies that the changes were actually propagated.

4. **再次重用**
   - Reuse the same project rules and workflow on a new but related task.
   - Demonstrate that the project has become reusable rather than disposable.

Add a fifth small callout:

> 下一場培訓入口：帶一個真實課堂問題回來。

---

## 9. Fixed 120-Minute Workshop Flow

The workshop should be represented as a visible timeline.

The first half should establish the first usable result.

The second half should create depth through differentiation, synchronized revision, and reuse.

### 0–10 min — 看見終點

Lecturer actions:

- Show the four final outputs before teaching any commands.
- Explain the complete learning loop.
- Make it clear that the goal is not "learn all OpenCode functions".

Participant actions:

- Open the workshop project.
- Identify where materials, requirements, output, and AGENTS.md are located.

Output:

- Participant knows the end goal and project map.

### 10–20 min — 啟動專案

Lecturer actions:

- Demonstrate opening the prepared `Math-Agent-Workshop` folder.
- Confirm OpenCode can see the project.
- Explain that the Agent should work inside the project rather than in an unrelated temporary chat.

Participant actions:

- Open the same project.
- Confirm the PDF is inside `materials/`.

Completion check:

- OpenCode is running.
- Project folder is correct.
- Material is visible.

### 20–30 min — 讀懂 AGENTS.md

Lecturer actions:

- Explain `AGENTS.md` as the project's long-term rules.
- Distinguish stable rules from one-time task requirements.
- Avoid a long syntax lecture.

Participant actions:

- Ask the Agent to summarize the project rules.
- Check whether the summary matches the intended teaching context.

Suggested lecturer input:

```text
請先閱讀本專案的 AGENTS.md。

不要開始產出教材。

請先用簡短條列告訴我：
1. 你理解這個專案的用途是甚麼；
2. 你必須遵守哪些規則；
3. 你之後產出的檔案應該放在哪裡；
4. 有哪些地方需要先向老師確認。
```

### 30–42 min — 讀取真實教材

Lecturer actions:

- Demonstrate pointing the Agent to the PDF in `materials/`.
- Make the Agent analyze before generating.

Participant actions:

- Ask the Agent to inspect the real mathematics material.
- Verify topic, learning objectives, prerequisites, likely difficulties, and important representations.

Suggested input:

```text
請閱讀 materials/ 內的示範教材。

目前只做教材分析，不要直接生成學習單。

請整理：
1. 本課核心數學概念；
2. 學生需要具備的前置知識；
3. 可能出現的常見錯誤或迷思；
4. 教材中值得保留的題型或表徵；
5. 如果要設計一份課堂學習單，你還需要向我確認甚麼。
```

### 42–50 min — 教師確認需求

The Agent should not silently invent the full task.

Lecturer demonstrates a short requirement interview.

Participant decides:

- Grade.
- Lesson stage.
- Estimated time.
- Core objective.
- Number of items.
- Difficulty.
- Whether answers are needed.
- Language requirements where relevant.
- Output format.

The Agent writes confirmed requirements into:

```text
requirements/task-spec.md
```

Suggested input:

```text
根據你剛才讀到的教材，請用不超過 6 個問題向我確認這次學習單的必要規格。

一次只問最重要的問題，不要問可以從教材直接得到答案的事情。

我回答後，請把最後確認的規格寫入：
requirements/task-spec.md

寫完後先停下來讓我確認，不要立即生成成品。
```

### 50–60 min — 完成第一次備課成果

Only after the teacher confirms `task-spec.md`, generate the first usable result.

Suggested input:

```text
我已確認 requirements/task-spec.md。

現在請依照：
- AGENTS.md
- materials/ 內的教材
- requirements/task-spec.md

完成第一版可直接使用的課堂學習材料。

要求：
1. 不要加入教材沒有依據的知識點；
2. 題目次序要有學習坡度；
3. 保留教師可再修改的空間；
4. 如需要答案，另外整理教師版；
5. 所有檔案寫入 output/01-first-version/。

完成後請列出：
- 你建立了哪些檔案；
- 每個檔案的用途；
- 哪三個地方最值得老師人工檢查。
```

Halfway checkpoint:

> By minute 60, the participant must already possess one usable first version.

### 60–75 min — 做一次分層

Do not restart from zero.

Use the existing first version and task specification.

The differentiation should preserve the same core learning goal while changing scaffolding or challenge.

Suggested input:

```text
不要重新設計一份完全不同的學習單。

請以 output/01-first-version/ 的版本為基礎，做一次真正的分層。

共同要求：
- 核心學習目標相同；
- 核心概念相同；
- 不因分層而降低數學的正確性。

請建立：
A. 支援版：增加提示、步驟、表徵或例題支架；
B. 基準版：保留目前主要難度；
C. 挑戰版：增加需要解釋、比較、推理或遷移的任務。

把分層版本寫入：
output/02-differentiated/

完成後請用一個表格說明三個版本到底「改了甚麼」，不要只說難度不同。
```

Completion check:

- Three versions are meaningfully different.
- Core objective remains aligned.
- Differentiation is visible in task design, not merely in labels.

### 75–95 min — 做一次同步修訂

The lecturer introduces a realistic change.

Examples:

- Lesson time reduced.
- Teacher wants fewer questions.
- A specific misconception must be added.
- The class needs more visual support.
- A challenge question should require reasoning rather than more calculation.

The Agent must update all affected files rather than only one visible paragraph.

Suggested input:

```text
現在模擬真實備課中的臨時修改。

新的要求是：
【在這裡輸入講師指定或老師自己的修改要求】

請先告訴我：
1. 這個改動會影響哪些既有檔案；
2. 每個檔案需要改甚麼；
3. 哪些內容不應被改動。

等我確認後，再同步更新相關內容。

更新後：
- 新版本放入 output/03-revised/；
- 不要覆蓋 output/01-first-version/ 或 output/02-differentiated/；
- 最後提供一份 change-summary.md，列出改動前後差異。
```

The learning point is:

> AI Agent 的價值不只是「重新生成」，而是能在專案脈絡中管理修改。

### 95–110 min — 再次重用

The teacher now proves that the workflow is reusable.

Use either:

- another section of the same unit;
- another similar lesson;
- another short teaching task.

Do not rebuild `AGENTS.md`.

Suggested input:

```text
現在我要測試這個專案是否真的可以重用。

請保留：
- AGENTS.md 的長期規則；
- 已建立的工作方式；
- 檔案管理原則。

這次的新任務是：
【老師輸入一個新的、但相關的備課任務】

請先判斷：
1. 哪些既有規則可以直接重用；
2. 哪些 task-specific requirements 需要重新確認；
3. 哪些舊內容不應直接照搬。

完成必要確認後，將新成果寫入：
output/04-reused/
```

Completion check:

- The teacher did not recreate the project.
- The Agent reused stable rules.
- New task-specific requirements were still confirmed.

### 110–117 min — 驗收

Participants inspect rather than merely admire the output.

Use this checklist:

- Mathematics is correct.
- Learning objective is aligned.
- Instructions are understandable by pupils.
- Difficulty progression is reasonable.
- Differentiated versions are truly different.
- Revision was propagated consistently.
- No original material was overwritten.
- New task demonstrates reuse.
- File locations are understandable.

The site must visibly communicate:

> AI 產出 ≠ 完成。教師驗收才是完成。

### 117–120 min — 帶一個真實問題離場

Each teacher records one real classroom problem.

Write it into:

```text
notes/next-workshop-problem.md
```

Suggested input:

```text
請建立 notes/next-workshop-problem.md。

請用簡潔格式記錄：

# 下一場我要解決的真實課堂問題

- 年級：
- 課題：
- 現在最花時間的工作：
- 學生最常出現的問題：
- 我希望 AI Agent 幫我做到甚麼：
- 有甚麼事情我仍然必須由老師親自判斷：

不要替我虛構內容；缺少的地方留給我填寫。
```

This file becomes the entry point to the next workshop.

---

## 10. Prompt Page Requirements

`prompts.html` must contain the exact prompts used during the workshop.

Organize them by phase:

1. Read AGENTS.md.
2. Analyze material.
3. Confirm requirements.
4. Generate first version.
5. Differentiate.
6. Synchronize revision.
7. Reuse.
8. Record next classroom problem.

Each prompt block should include:

- When to use it.
- What the Agent should do.
- What it should not do.
- Expected file output.
- A copyable code block.

Do not fill the prompt page with dozens of alternative prompts.

The goal is to give beginners one reliable path.

---

## 11. Human Documentation + Agent Instructions

The site should maintain two layers of information.

### Human-facing layer

Explain:

- what the teacher is doing;
- why this step matters;
- what success looks like;
- what file should appear next.

### Agent-facing layer

Store operational instructions in `SKILL.md`, `AGENTS.md`, or other clearly named Markdown files.

The website may link to raw Agent instruction files when useful.

Do not mix long machine instructions directly into learner-facing prose unless the learner must copy them.

---

## 12. Image Strategy

Images are supporting material, not the core implementation.

If suitable images already exist:

- place them under `images/`;
- use meaningful filenames;
- add descriptive `alt` text;
- reference them with relative paths.

Useful diagrams may include:

```text
00-workshop-map.png
01-project-structure.png
02-first-preparation.png
03-differentiation.png
04-sync-revision.png
05-reuse-loop.png
06-next-workshop.png
```

If images do not yet exist:

- do not create broken `<img>` links;
- use a styled placeholder card or text diagram;
- keep the page functional without images.

---

## 13. Responsive Design

At minimum support:

- desktop browser;
- laptop;
- tablet;
- mobile phone.

Use patterns such as:

```css
.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:14px;
}
```

and:

```css
@media(max-width:600px){
  .wrap{padding:0 16px;}
  header{padding:48px 0 32px;}
  h1{font-size:1.8rem;}
}
```

For wide tables:

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

## 14. Accessibility and Clarity

Always:

- include `<meta name="viewport">`;
- use semantic heading levels;
- add `alt` text to images;
- maintain readable contrast;
- avoid tiny text;
- avoid huge walls of prose;
- provide visible focus states for links and buttons where practical;
- use `lang="zh-Hant"` or `lang="zh-TW"` consistently.

The main learner-facing language should be Traditional Chinese unless the existing project specifies otherwise.

Because both Chinese- and English-section mathematics teachers may use the material, keep technical labels and file names clear in English where this improves consistency.

Do not automatically translate the entire website into English unless requested.

---

## 15. Beginner-Friendly Rules

When writing learner instructions:

- Give one action at a time.
- Use exact file paths.
- Show exact OpenCode input when needed.
- Explain unfamiliar terms only when they first appear.
- Avoid unexplained command-line jargon.
- Avoid asking teachers to edit code manually unless the workshop explicitly requires it.
- Do not introduce Git concepts unless they are needed for the current action.
- Keep troubleshooting focused on likely workshop blockers.

---

## 16. Troubleshooting Page

Only include high-frequency issues such as:

- OpenCode opened the wrong folder.
- PDF is not inside `materials/`.
- Agent starts generating before confirming requirements.
- Agent cannot find `AGENTS.md`.
- Files are written outside `output/`.
- Teacher accidentally asks the Agent to overwrite the original.
- Output is too generic because requirements are vague.
- Differentiation only changes labels, not scaffolding or reasoning demand.
- Synchronized revision updates only one file.
- Reuse becomes copy-paste instead of using the project rules.

For each problem provide:

1. symptom;
2. likely cause;
3. one corrective action;
4. one verification step.

Do not turn the troubleshooting page into a general OpenCode manual.

---

## 17. Content Tone

The site should feel:

- practical;
- calm;
- teacher-centered;
- operational;
- non-technical where possible.

Avoid:

- exaggerated AI marketing;
- claims that AI replaces professional judgement;
- long theoretical definitions before practice;
- language that makes beginners feel technically inadequate.

Emphasize:

> Agent 負責加速流程；教師負責目標、判斷、驗收與課堂決策。

---

## 18. Build Workflow for Antigravity

When this Skill is triggered, work in this order.

### Step 1 — Inspect

Inspect the workspace for:

- existing HTML files;
- existing `AGENTS.md`;
- workshop materials;
- images;
- current folder names;
- README;
- any previous workshop site.

Do not overwrite or rename working files without a reason.

### Step 2 — Map Existing Content

Create an internal mapping of:

- supplied training content;
- required website section;
- required downloadable resource;
- any missing asset.

Do not invent missing institutional details.

### Step 3 — Build or Update

Create the smallest set of files needed to satisfy the site architecture.

Reuse the same visual system across pages.

### Step 4 — Validate Paths

Check:

- relative links;
- images;
- subpage links;
- file names;
- GitHub Pages compatibility.

### Step 5 — Validate Content

Check that the website includes all four practical cycles:

- first preparation;
- differentiation;
- synchronized revision;
- reuse.

Also check that the next-workshop classroom problem is explicitly captured.

### Step 6 — Validate 120 Minutes

The total timeline must equal exactly 120 minutes.

Do not silently change the timing.

### Step 7 — Report

At completion, provide a concise report containing:

- files created;
- files changed;
- pages available;
- missing optional assets;
- how to preview locally;
- whether the site is ready for GitHub Pages.

---

## 19. Completion Criteria

Do not consider the task complete unless all applicable conditions are true.

### Website

- `index.html` exists.
- Main navigation works.
- Site is readable on desktop and mobile.
- No unnecessary framework was introduced.
- All local links use correct relative paths.
- Missing images do not create broken elements.

### Workshop Content

- 120-minute flow is complete.
- First usable output exists conceptually by minute 60.
- Differentiation is explicitly taught.
- Synchronized revision is explicitly taught.
- Reuse is explicitly taught.
- Teacher validation is explicitly taught.
- Next-workshop classroom problem is explicitly captured.

### Agent Workflow

- `AGENTS.md` is treated as stable project rules.
- Task-specific requirements are written separately.
- Original materials are preserved.
- Outputs are versioned by stage rather than overwritten.
- Reuse keeps stable rules while reconfirming task-specific requirements.

---

## 20. Core Principle

When choices conflict, prioritize this sequence:

> Teacher learning clarity → usable workshop result → reusability → simple maintenance → visual polish.

The final site should behave like a **workshop handbook that happens to be a website**, not like a software product trying to demonstrate technical complexity.
