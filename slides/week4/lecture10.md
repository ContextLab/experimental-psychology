---
marp: true
theme: cdl-theme
math: katex
transition: fade 0.25s
author: Contextual Dynamics Lab
---

# Exploring and understanding data

### PSYC 11: Laboratory in Psychological Science

Jeremy R. Manning
Dartmouth College
Spring 2026

---

# Truth and data

<div class="definition-box" data-title="Can data reveal truth?">

- The "universe" produces data
- Math doesn't lie&mdash; but **analyses** involve choices
- Different analyses can lead to different conclusions
- The same dataset can tell very different stories

</div>

---

# What patterns should you look for?

<div class="tip-box" data-title="First steps with any dataset">

- **Shape:** How many observations? How many features? Any missing data?
- **Distributions:** Are values clustered? Spread out? Skewed?
- **Relationships:** Do any features move together? In opposite directions?
- **Outliers:** Are there values that seem "wrong" or surprising?

</div>

---

<!-- _class: scale-90 -->

# The power of visualization

<div class="note-box" data-title="Why plot your data?">

- Tables of numbers hide patterns; plots reveal them
- Always look at your data **before** running statistics
- Anscombe's quartet (below): four datasets with **identical** means, variances, correlations, and regression lines &mdash; but completely different stories

</div>

<div style="text-align: center;">

<img src="../figs/data_exploration/anscombes_quartet.svg" width="900">

</div>

---

<!-- _class: scale-90 -->

# Discussion: what does this graph tell you?

<div class="note-box" data-title="The dataset">

A psychology professor surveyed 60 of her PSYC 6 students about their study habits and recorded their midterm exam scores. She fit a regression line to the data:

</div>

<div style="display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 1.5rem; align-items: center !important;">

<div>

<img src="../figs/data_exploration/study_hours_scores.svg" style="width: 100%;">

</div>

<div class="example-box" data-title="Think about it...">

- What **story** does this plot tell?
- What is it **not** telling you? What would you want to know before believing the "more studying &rarr; higher scores" story?
- What follow-up plot or analysis would you want to see next?

</div>

</div>

---

<!-- _class: scale-90 -->

# Discussion: how about this one?

<div class="note-box" data-title="A real correlation! (r = 0.80, p < 0.01)">

The number of xkcd comics published about literature is strongly positively correlated with the robbery rate in Vermont (2007&ndash;2022).

</div>

<div style="display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 1.5rem; align-items: center !important;">

<div>

<img src="../figs/data_exploration/spurious_correlation.svg" style="width: 100%;">

</div>

<div class="example-box" data-title="Think about it...">

- What **story** does this plot tell?
- What is it **not** telling you? What would you want to know before believing the "more xkcd literature comics &rarr; more robberies" in Vermont story?
- What follow-up plot or analysis would you want to see next?

</div>

</div>

---

<!-- _class: scale-90 -->

# Discussion: how about this one?

<div class="note-box" data-title="A real correlation! (r = 0.80, p < 0.01)">

The number of xkcd comics published about literature is strongly positively correlated with the robbery rate in Vermont (2007&ndash;2022).

</div>

<div style="display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 1.5rem; align-items: center !important;">

<div>

<img src="../figs/data_exploration/spurious_correlation.svg" style="width: 100%;">

</div>

<div class="example-box" data-title="AI generated explanation">

*"As xkcd published more literature comics, book enthusiasts flocked to Vermont. Caught up in literary intrigue, they sparked a wave of daring heists &mdash; leaving authorities to wonder why Shakespeare and Hemingway inspired the crime spike."*

</div>

</div>

---

# Analytic flexibility

<div class="warning-box" data-title="Multiple paths, multiple conclusions">

- There are typically many ways to analyze data
- Different choices (which subset, which test, which visualization) can lead to different conclusions
- This is why **transparency** about your analysis choices matters

</div>

---

# What's in your toolkit?

<div class="tip-box" data-title="From simple to sophisticated">

- Observation, intuition, and logic
- Simple summaries (mean, standard deviation, sorting)
- Traditional statistical tests (t-tests, correlations, ANOVAs)
- Fancier methods and simulations

</div>

---

# Getting help

<div class="note-box" data-title="Resources">

- Teaching staff (instructor + TAs)
- Other students
- Slack (`#stats-stuff`, `#data-sleuthing-lab`)
- Google, Stack Exchange, Wikipedia, ChatGPT/Claude/[chat.dartmouth](https://chat.dartmouth.edu)

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

- **Friday**: Part 3 of the lab (more analysis, discussion)

</div>
