---
marp: true
theme: cdl-theme
math: katex
transition: fade 0.25s
author: Contextual Dynamics Lab
---

# Vibe coding tips and tricks
### PSYC 11: Laboratory in Psychological Science

Jeremy R. Manning
Dartmouth College
Spring 2026

---

# Today's agenda

<div class="definition-box" data-title="What is vibe coding?">

Vibe coding means using AI coding agents to rapidly prototype and implement software by describing what you want in natural language, then iterating on the output.

</div>

<div class="note-box" data-title="Topics we'll cover">

1. **Free AI coding tools for students:** GitHub Copilot, Google Gemini, [claude.dartmouth.edu](https://claude.dartmouth.edu)
2. **Setting up your environment:** VS Code, Claude Code, spec-kit
3. **The spec-kit workflow:** from design docs to implementation
4. **Live demo:** build something together! (*If there's time!*)

</div>

<div class="tip-box" data-title="Follow along!">

Install the tools (and *try using them*) as we go&mdash; and ask questions as they arise!

</div>

---
<!-- _class: scale-80 -->

# Free coding models

- **GitHub Copilot** (free for students): great at code completion, chat assistance
- **Google Gemini** (free for students): long context, reasoning-heavy tasks
- **Dartmouth GenAI** ([chat.dartmouth.edu](https://chat.dartmouth.edu)): free access to many models
- **Dartmouth Claude** ([claude.dartmouth.edu](https://claude.dartmouth.edu)): powerful coding model, free for Dartmouth students, faculty, and staff
- **Ollama** and **LM Studio**: run LLMs locally
- **Hugging Face**: open models, useful for integrating into projects

---
<!-- _class: scale-80 -->

# My favorite paid options

- **Anthropic Claude**: fantastic coding model (what I use most!)
- **OpenAI ChatGPT**: powerful, different feel; sometimes when one struggles the other helps

<div class="note-box" data-title="Student discounts">

Check for student discounts and free tiers; most AI providers offer generous free usage for students with a `.edu` email address.

</div>

---
<!-- _class: scale-80 -->

# Setting up your environment: two(ish) options

Two main options:

1. **Integrated Development Environment (IDE):** full-featured environment with syntax highlighting, debugging, Git integration, extensions (e.g., VS Code, PyCharm)
2. **Terminal-based coding agent:** lightweight, fast, scriptable (e.g., Claude Code, ChatGPT Codex CLI, OpenCode)

<div class="note-box" data-title="Some other options to try out">

- Claude, OpenAI, and OpenCode all have native desktop apps that combine terminal-based coding agents with IDE-like features (file browsing, syntax highlighting, etc.)
- Some IDEs are explicitly designed for AI coding (e.g., [Antigravity](https://antigravity.google/), [Cursor](https://cursor.com/))
- Google Colab now builds in AI coding assistance directly into notebooks (similar to VS Code's Copilot extension); no installation required!

</div>

---
<!-- _class: scale-60 -->

# Setting up VS Code

![width:1000px](../figs/vibe_coding/vs_code_cc.png)

---

# Setting up VS Code (details)

- Download and install from [code.visualstudio.com](https://code.visualstudio.com)
- Install essential extensions:
  - GitHub Copilot
  - Jupyter
  - Python
  - Claude Code
- Activate Copilot with your GitHub account (click the Accounts icon in bottom left)

---

# Setting up Claude Code (in Terminal)

<div class="note-box" data-title="Install command">

```bash
npm install -g @anthropic-ai/claude-code
```

</div>

![width:700px](../figs/vibe_coding/terminal_launch_cc.png)

---
<!-- _class: scale-60 -->

# Launch Claude Code

![width:900px](../figs/vibe_coding/cc_terminal.png)

---

# Claude Code configuration

- Use `/model` to switch between models (Claude Sonnet, Opus, Haiku)
- Connect with your Anthropic account, or use GitHub Copilot models
- Claude Code runs in your terminal inside your project directory
- It can read files, write code, run commands, and browse the web

---

# Spec-kit: a framework for AI-assisted software development

<div class="definition-box" data-title="What is spec-kit?">

A "spec" is a detailed, unambiguous description of what a software project should do. Spec-kit is a workflow for using AI to go from specification to implementation in a structured way.

</div>

<div class="example-box" data-title="Install it!">

```bash
# Install the spec-kit CLI tool globally
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Set up spec-kit in your project (from within your project folder in Terminal)
specify init --here --ai claude
```

</div>

---
<!-- _class: scale-80 -->

# Orienting Claude Code to your project

<div class="note-box" data-title="Start here!">

Clone (download) your repo and `cd` into it.

</div>

- Launch Claude Code (run `claude` inside the project folder)
- Run `/init` to tell Claude to explore your project folder
- It maintains a `CLAUDE.md` file to help future sessions understand the project

---
<!-- _class: scale-80 -->

# The four-step vibe coding workflow

```flow
[Describe:green] --> [Design:blue] --> [Plan:bonfire] --> [Implement:purple]
```

<div class="example-box" data-title="1. Detailed description">

Specify inputs/outputs, edge cases, and examples

</div>

<div class="note-box" data-title="2. Technical design doc">

Have AI draft the architecture, iterate on it, produce skeleton code

</div>

<div class="warning-box" data-title="3. Implementation plan">

Break into small tasks with verification steps; mind context limits

</div>

<div class="definition-box" data-title="4. Implement and verify">

Let AI write code, test each piece, stress test the final product

</div>

---

# The spec-kit workflow

<div class="definition-box" data-title="What is spec-kit?">

Instead of writing a technical design doc and implementation plan from scratch, you write a specification first. The spec becomes the executable source of truth.

</div>

<div class="example-box" data-title="The 6 steps">

1. **Constitution** — establish inviolable project principles
2. **Specify** — describe what you want built
3. **Clarify** — resolve ambiguities interactively
4. **Plan** — generate an architecture and design doc
5. **Tasks** — break the plan into ordered, actionable tasks
6. **Implement** — execute tasks with verification at each step

</div>

---
<!-- _class: scale-80 -->

# Writing a good spec

<div class="warning-box" data-title="The golden rule">

Focus on **WHAT** and **WHY**, not **HOW**.

</div>

<div class="example-box" data-title="Example prompt: build a game that tests my reaction time">

Spec out a game that tests the user's reaction time. It should display a stimulus (e.g., a circle) at random intervals, and the user should click as quickly as possible when they see it. The game should record the reaction time for each trial and display the average reaction time at the end of the session. It should run in a web browser and be visually engaging. Support desktop and mobile devices, and all major platforms and browsers. Store results locally without sending data to any servers. Include instructions and feedback for the user. Make it fun!

</div>

---
<!-- _class: scale-80 -->

# Writing a good spec

<div class="warning-box" data-title="The golden rule">

Focus on **WHAT** and **WHY**, not **HOW**.

</div>

<div class="example-box" data-title="Notice: what are we building?">

**Spec out a game that tests the user's reaction time.** It should display a stimulus (e.g., a circle) at random intervals, and the user should click as quickly as possible when they see it. The game should record the reaction time for each trial and display the average reaction time at the end of the session. It should run in a web browser and be visually engaging. Support desktop and mobile devices, and all major platforms and browsers. Store results locally without sending data to any servers. Include instructions and feedback for the user. Make it fun!

</div>

---
<!-- _class: scale-80 -->

# Writing a good spec

<div class="warning-box" data-title="The golden rule">

Focus on **WHAT** and **WHY**, not **HOW**.

</div>

<div class="example-box" data-title="Notice: how should it work?">

Spec out a game that tests the user's reaction time. **It should display a stimulus (e.g., a circle) at random intervals, and the user should click as quickly as possible when they see it. The game should record the reaction time for each trial and display the average reaction time at the end of the session.** It should run in a web browser and be visually engaging. Support desktop and mobile devices, and all major platforms and browsers. Store results locally without sending data to any servers. **Include instructions and feedback for the user.** Make it fun!

</div>

---
<!-- _class: scale-80 -->

# Writing a good spec

<div class="warning-box" data-title="The golden rule">

Focus on **WHAT** and **WHY**, not **HOW**.

</div>

<div class="example-box" data-title="Notice: what are the design constraints?">

Spec out a game that tests the user's reaction time. It should display a stimulus (e.g., a circle) at random intervals, and the user should click as quickly as possible when they see it. The game should record the reaction time for each trial and display the average reaction time at the end of the session. **It should run in a web browser and be visually engaging. Support desktop and mobile devices, and all major platforms and browsers. Store results locally without sending data to any servers.** Include instructions and feedback for the user. **Make it fun!**

</div>

---

# Example: Gamified cognitive testing battery

<div class="note-box" data-title="What we're building">

A single HTML file that runs participants through a battery of quick gamified cognitive tests (Stroop, free recall, go/no-go, N-back, digit span, flanker, visual search, mental rotation) and displays a bar chart of performance with a class leaderboard.

</div>

<div class="tip-box" data-title="Real research!">

You could use something like this in part 2 of this course!

</div>

---

# The spec-kit workflow for our demo

```flow
[Constitution] --> [Specify] --> [Clarify] --> [Plan] --> [Tasks] --> [Implement:purple]
```

<div class="note-box" data-title="Documents at each step">

Each step produces a document that becomes the source of truth.

</div>

<div class="important-box" data-title="Why this matters">

The spec-kit workflow keeps everything grounded in a clear, unambiguous specification.

</div>

---
<!-- _class: scale-80 -->

# Constitution

<div class="example-box" data-title="Prompt: /speckit.constitution">

Create a constitution for this project with these principles:
- Single HTML file (nothing to install or download, runs in any browser)
- Results are stored locally (no data sent to servers)
- User delight: smooth animations, clean design, fun feedback
- Privacy and security: no personally identifiable information collected
- Leaderboard uses three-letter user-chosen codes
- Must work on mobile and desktop browsers
- Accessible design (WCAG 2.1 AA)

</div>

<div class="note-box" data-title="Output">

A `constitution.md` file with inviolable rules.

</div>

---
<!-- _class: scale-70 -->

# Specify

<div class="example-box" data-title="Prompt: /speckit.specify">

Build a gamified cognitive testing battery. Single HTML file.

User Journey:
1. Student enters their anonymous class code
2. Sees a menu of 8 cognitive tasks (Stroop, free recall, 
   go/no-go, N-back, digit span, flanker, visual search, 
   mental rotation)
3. Completes each task with animated instructions and feedback
4. After all tasks, sees a bar chart of their scores
5. Can view a class leaderboard comparing anonymous scores

</div>

<div class="note-box" data-title="Output">

A `spec.md` with user stories, acceptance criteria.

</div>

---
<!-- _class: scale-80 -->

# Clarify

<div class="example-box" data-title="Prompt: /speckit.clarify">

The agent might ask...

1. How long should each task take?
2. What scoring metric for each task?
3. How to handle incomplete sessions?
4. Should tasks be randomized?
5. What happens if localStorage is full?

</div>

<div class="note-box" data-title="Output">

An updated `spec.md` with notes about what was clarified or changed.

</div>

---
<!-- _class: scale-78 -->

# Plan and tasks

<div class="example-box" data-title="Prompt: /speckit.plan">

Run this to generate a plan for implementing the project and define success criteria for each project milestone.

</div>

<div class="example-box" data-title="Prompt: /speckit.tasks">

Run this to break the implementation plan into discrete, ordered tasks with clear acceptance criteria for each task.

</div>

<div class="tip-box" data-title="Optional: /speckit.analyze">

For complex projects, run this to identify any inconsistencies, gaps, or potential issues in the specification or plan before you start implementing.

</div>

---
<!-- _class: scale-78 -->

# Implement

<div class="example-box" data-title="Prompt: /speckit.implement">

Running this command will launch an interactive coding session where the agent will execute the implementation plan task by task, generating code, running tests, and verifying outputs at each step.

</div>

<div class="note-box" data-title="Output">

Whatever each task specifies: functions, classes, tests, documentation, etc. A task is "done" when all its acceptance criteria are met.

</div>

<div class="tip-box" data-title="Babysitting">

Claude will prompt you (often very frequently) to ask for permission to run code, execute commands, or change files. Read them carefully the first time you see them, and then once you get used to how it works you can usually just skim and click "yes" to keep things moving.

</div>

---
<!-- _class: scale-90 -->

# Guiding principles

<div class="definition-box" data-title="Simplicity">

"Simplicity is the art of maximizing the amount of work not done."

</div>

<div class="note-box" data-title="Five principles for effective vibe coding">

1. **Start small** — get a working prototype before adding features
2. **Be specific** — vague prompts produce vague code
3. **Verify everything** — never trust AI output without checking it
4. **Iterate rapidly** — small changes, frequent testing
5. **Document as you go** — your future self (and your AI) will thank you

</div>

---

# Questions? Want to chat more?

<div class="emoji-figure">
  <div class="emoji-col">
    <span class="emoji emoji-xl emoji-bg emoji-bg-navy">&#x1F4E7;</span>
    <span class="label"><a href="mailto:jeremy@dartmouth.edu">Email</a> me</span>
  </div>
  <div class="emoji-col">
    <span class="emoji emoji-xl emoji-bg emoji-bg-purple">&#x1F4AC;</span>
    <span class="label">Join our <a href="https://psyc11.slack.com">Slack</a></span>
  </div>
  <div class="emoji-col">
    <span class="emoji emoji-xl emoji-bg emoji-bg-green">&#x1F481;</span>
    <span class="label">Come to <a href="https://context-lab.com/scheduler">office hours</a></span>
  </div>
</div>

<div class="note-box" data-title="Up next this week...">

**Friday**: data wrangling and how far can you get with stats?

</div>
