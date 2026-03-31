---
marp: true
theme: cdl-theme
math: katex
transition: fade 0.25s
author: Contextual Dynamics Lab
---

# Statistical building blocks

### PSYC 11: Laboratory in Psychological Science

Jeremy R. Manning
Dartmouth College
Spring 2026

---

![bg](../figs/statistical_building_blocks/pasted-image-14274.png)

---

# Today's goal

<div class="note-box" data-title="Connecting Stats to Your Survey Data">

You collected survey data on Monday -- sleep, stress, happiness, screen time, exercise, caffeine, study hours, social activity.

Today we'll build the statistical intuitions you need to **analyze** that data:
- What kinds of patterns can we look for?
- How do we know if a pattern is "real" or just noise?
- Which tools match which questions?

</div>

---

# What is a distribution?

<div class="definition-box" data-title="Core Intuition">

A distribution describes what values are likely (or unlikely) when we observe something.

</div>

<div class="example-box" data-title="Think About Your Survey Data">

- If you plotted everyone's sleep hours, what shape would you expect? A bell curve? Skewed?
- What about stress ratings (1--10)? Would they cluster in the middle or spread out?
- **Discussion**: sketch what you think the sleep distribution looks like. Compare with a neighbor.

</div>

---

# What is a p-value, really?

<div class="important-box" data-title="The Key Idea">

A p-value answers: *"If there were NO relationship between these variables, how surprised should I be by what I see in the data?"*

- Low p-value → the pattern would be very unlikely to occur by chance
- It does **not** tell you the probability that your hypothesis is true!
- It does **not** tell you how strong or important the effect is!

</div>

---

# Discussion: Your survey hypotheses

<div class="example-box" data-title="Think-Pair-Share">

- You formed hypotheses on Monday about relationships in the survey data
- For one of your hypotheses: what would the "null" hypothesis be?
- What would you expect to see in the data if there really is NO relationship?
- What result would surprise you enough to reject the null?

</div>

---

<!-- _class: scale-80 -->

# Which test for which question?

<div class="tip-box" data-title="Matching Your Question to a Test">

| Your question | Test | Example from our survey |
|-|-|-|
| Do two groups differ? | **t-test** | Do high-sleepers (≥7 hrs) have lower stress than low-sleepers? |
| Are two continuous variables related? | **Correlation** | Is screen time associated with happiness? |
| Are two categories associated? | **Chi-square** | Is exercise level (high/low) related to caffeine level (high/low)? |

</div>

<div class="warning-box" data-title="Watch Out">

Choosing the wrong test for your data type is one of the most common mistakes. When in doubt, ask!

</div>

---

# The recipe for any statistical test

<div class="note-box" data-title="Four Steps">

1. **State your hypothesis** clearly (and what the null alternative is)
2. **Pick the right test** based on your data type and question
3. **Run the test** and get a test statistic + p-value
4. **Interpret honestly** -- what can you conclude? What can't you?

</div>

---

# Beyond p-values: effect sizes

<div class="warning-box" data-title="Why p-values Aren't Enough">

- A *tiny* effect can be "significant" with enough data
- A *large* effect might not be "significant" with too little data
- Always ask: **how big** is the effect, not just "is it significant?"
- For correlations: r = 0.1 is small, r = 0.3 is medium, r = 0.5 is large

</div>

---

# Let's look at some analysis tools

<div class="tip-box" data-title="Survey Analysis Notebook">

This notebook has templates for all the tests we discussed -- t-tests, correlations, chi-square -- pre-loaded with column names from our class survey.

Open it in Google Colab and start exploring!

</div>

<div style="text-align: center;">

<img src="../figs/statistical_building_blocks/survey_analysis_qr.png" width="350">

Survey analysis notebook

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

- **Today**: start thinking about your hypotheses and analysis plan
- **Thursday and Friday**: no class this week (instructor away)
- **Next Monday**: Motivating your science + Pitch lab starts

</div>
