---
marp: true
theme: cdl-theme
math: katex
transition: fade 0.25s
author: Contextual Dynamics Lab
---

# Creating data

### PSYC 11: Laboratory in Psychological Science

Jeremy R. Manning
Dartmouth College
Spring 2026

---

# What makes a good dataset?

<div class="definition-box" data-title="Key properties">

- Tells us about something we care about
- Has enough observations to draw conclusions
- Includes the right features to test hypotheses
- Is organized so others can work with it

</div>

---

# What would you want to measure?

<div class="example-box" data-title="Think-pair-share">

- Pick a topic you find interesting (e.g., sleep, social media, climate, sports)
- What **features** would you measure? How many observations would you need?
- What questions could you answer with that data? What questions would be **impossible** to answer?
- Be ready to share your top idea with the class

</div>

---

# Where do data come from?

<div class="tip-box" data-title="Three approaches">

- **Find existing data:** Kaggle, Google Dataset Search, FiveThirtyEight, Awesome Public Datasets
- **Generate synthetic data:** random number generators, data spoofing libraries (Faker, Mimesis)
- **Collect new data:** surveys, sensors, observations

</div>

---

# What can go wrong?

<div class="warning-box" data-title="Common pitfalls">

- Too few observations or too few features
- Missing data or inconsistent formatting
- Data that **looks** like it answers your question but actually doesn't
- Confusing correlation with causation

</div>

---

# Answerable vs. unanswerable

<div class="example-box" data-title="Think-pair-share">

- Given a dataset of 1,000 college students with: GPA, major, sleep hours, and screen time...
- Which questions **can** you answer? Which **can't** you answer?
- What additional features would unlock new questions?

</div>

---

<!-- _class: scale-90 -->

# Data sleuthing lab overview

<div class="important-box" data-title="Your two roles">

- You'll play two roles: **data creator** and **data sleuth**
- **Monday:** find or generate a dataset + write 5 questions about it
  - At least 1 question must be **possible** to answer with the dataset
  - At least 1 question must be **impossible** to answer
  - At least 5 features per observation, at least 500 observations
- **Thursday:** hand off datasets (A&rarr;B, B&rarr;C, C&rarr;D, D&rarr;A) and explore
- **Friday:** wrap up analysis and discussion

</div>

---

<!-- _class: scale-90 -->

# What makes a good "impossible" question?

<div class="warning-box" data-title="Bad: too obvious">

- Asking about something completely unrelated to the dataset
- Asking about a feature that isn't in the dataset (e.g., "what's their favorite color?" when no color column exists)
- These are too easy to spot &mdash; the sleuth will know immediately

</div>

<div class="tip-box" data-title="Better: subtle and interesting">

- Ask about **values or patterns** that *seem* answerable but actually require data you don't have
  - "Does X cause Y?" when you only have correlational data
  - "Did this trend hold *before* the data collection started?"
  - "What would happen if we doubled this variable?" (no experimental manipulation)
- The sleuth should have to **analyze** the data &mdash; not just glance at the columns &mdash; to figure out whether it's possible

</div>

---

# Let's get started!

<div class="tip-box" data-title="Today's goal">

- Form your groups and start brainstorming your dataset
- Think about what will make it **interesting** for the other group to explore
- Organize everything into a clean spreadsheet

</div>

<div style="text-align: center;">

<a href="https://context-lab.com/experimental-psychology/assignments/data_sleuthing_lab/">Lab instructions</a> (also linked via QR code below)

<img src="../figs/data_creation/data_sleuthing_lab_qr.png" width="300">

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

<div class="note-box" data-title="Up next...">

- **Wednesday**: No class (I'm away!)
- **Thursday X-hour**: Part 2 of the lab (data sleuthing)
- **Friday**: Part 3 of the lab (analysis and discussion)

</div>
