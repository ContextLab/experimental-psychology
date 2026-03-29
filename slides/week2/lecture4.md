---
marp: true
theme: cdl-theme
math: katex
transition: fade 0.25s
author: Contextual Dynamics Lab
---

# Data wrangling + Vibe coding tutorial

### PSYC 11: Laboratory in Psychological Science

Jeremy R. Manning
Dartmouth College
Spring 2026

---

# Posing your questions

<div class="note-box" data-title="Survey data questions">

- How do students' sleep habits relate to their reported stress levels?
- Are there patterns in screen time, happiness, or daily routines across the class?
- Which everyday habits show the most variation among students?

</div>

---

# Posing your questions

<div class="note-box" data-title="Levels of sophistication">

- Non-scientific framing: guess
- Simple framing: just count and report!
- More sophisticated: try to **explain** what you observed (stats!)

</div>

---

# Statistical tests

<div class="important-box" data-title="Why wrangle?">

To actually carry out whatever tests or analyses you decide on, you need to **wrangle** your data

</div>

---

# Data wrangling

<div class="definition-box" data-title="Data wrangling">

Data wrangling means organizing or transforming your data into a format that is more convenient for you to work with

</div>

---

# What do we have?

<img src="../figs/data_wrangling/Screen Shot 2022-03-31 at 6.40.46 PM-14409.png" width="700">

---

# Discuss (with your group)

<div class="tip-box" data-title="Discussion questions">

- Are there any **challenges** to analyzing the data in its current form?
- What data format do you **want**?
- How can you "wrangle" the dataset into a more convenient format? (Try it!)

</div>

---

# Example analysis of the survey data

<img src="../figs/data_wrangling/survey_analysis_qr.png" width="500">

---

# Vibe coding: using AI to analyze data

<div class="definition-box" data-title="What is vibe coding?">

Vibe coding means using AI tools to help you write code by describing what you want in natural language. You don't need to be a programmer — you just need to clearly describe your analysis goals.

</div>

---
<!-- _class: scale-80 -->

# Free AI tools for data analysis

<div class="note-box" data-title="Tools you can use right now">

- [**Google Colab AI**](https://colab.research.google.com): built-in AI coding assistance — just click the "Generate" button in any code cell
- [**GitHub Copilot**](https://github.com/education/students): free for students — great for code completion
- [**Dartmouth GenAI**](https://chat.dartmouth.edu): free access to Claude, ChatGPT, and other models
- [**ChatGPT**](https://chat.openai.com) / [**Claude**](https://claude.ai): paste your data questions and get analysis code back

</div>

<div class="tip-box" data-title="Pro tip">

Google Colab is the easiest starting point — no installation needed, and the AI features are built right in.

</div>

---

# The key to effective vibe coding

<div class="important-box" data-title="Describe → Check → Iterate">

1. **Describe clearly**: tell the AI exactly what data you have and what you want to learn
2. **Check the output**: never trust AI-generated code blindly — run it, inspect the results, verify it makes sense
3. **Iterate**: if the result isn't right, describe what's wrong and ask for a fix

</div>

<div class="warning-box" data-title="The #1 mistake">

Accepting AI output without checking it. AI can produce code that runs but gives wrong answers. Always sanity-check your results!

</div>

---
<!-- _class: scale-80 -->

# Example: analyzing survey data with AI

<div class="example-box" data-title="What to say to the AI">

"I have a CSV file with columns: sleep_hours, stress_level, happiness, screen_time, exercise_frequency, caffeine_intake, study_hours, social_activity. All are numeric. I want to: (1) create a correlation heatmap of all variables, (2) run a t-test comparing stress levels between high-sleep (>=7 hrs) and low-sleep (<7 hrs) groups, (3) make a scatter plot of screen_time vs happiness with a regression line."

</div>

<div class="tip-box" data-title="What makes this prompt effective?">

It specifies the data format, column names, data types, and exactly what analyses to perform. The more specific you are, the better the code you'll get.

</div>

---

# Discussion: when should you trust AI-generated code?

<div class="note-box" data-title="Breakout group activity (10 min)">

Discuss with your group:
- How would you verify that a correlation heatmap is correct?
- If an AI gives you a p-value, what sanity checks would you run?
- When is it OK to use AI-generated code without fully understanding every line?
- When is it NOT OK?

</div>

---

<!-- _class: scale-70 -->

# Next week: "pitch session" lab

<div class="note-box" data-title="Coming up">

- Goal: learn about how to motivate an idea or question
- Each group will come up with an idea to pitch to the class (Monday)
- You'll present your pitches and evaluate each other (Wednesday)
- Then we'll discuss which strategies were effective

</div>

<img src="../figs/data_wrangling/pitch_lab-14568.png" width="150">
