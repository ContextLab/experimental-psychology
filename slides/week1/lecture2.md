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

<img src="../figs/statistical_building_blocks/pasted-image-14274.png" style="max-height: 450px; width: auto;">

---

# What is a distribution?

<div class="note-box" data-title="Core Intuition">

- A distribution describes what values are likely (or unlikely) when we observe something
- Different distributions produce different types of data: real numbers, counts, coin flips, etc.
- Each distribution has **parameters** that control its shape (e.g., mean, variance, probability)

</div>

---

# What is a p-value, really?

<div class="important-box" data-title="Key Idea">

- A p-value answers: "If nothing interesting were happening, how surprised should I be by this data?"
- Low p-value = the data would be very unlikely under the "boring" (null) explanation
- It does **not** tell you the probability that your hypothesis is true!

</div>

---

# Discussion: Hypotheses

<div class="example-box" data-title="Your Turn">

- Give an example of a hypothesis you could test with data from this class
- What would your "null" hypothesis be? What outcome would make you reject it?
- Share with a neighbor and compare

</div>

---

# The recipe for any statistical test

<div class="tip-box" data-title="How Tests Work">

1. Pick a distribution that matches your data type
2. Choose "null" parameters (e.g., mean = 0, coin is fair)
3. Simulate many draws from that null distribution
4. Compare your actual data to those simulations -- how unusual is it?

</div>

---

# Example: Is a coin fair?

<div class="example-box" data-title="Worked Example">

- You flip a coin 12 times and get 3 heads
- Null hypothesis: p(heads) = 0.5
- Simulate 1,000,000 sets of 12 flips with a fair coin
- What fraction give 3 or fewer heads? That fraction is your p-value!

</div>

---

<!-- _class: scale-78 -->

# Common distributions (reference)

| **Distribution** | **Parameter(s)** | **What you get out** |
|-|-|-|
| **Gaussian (Normal)** | Mean, variance | Real numbers |
| **Bernoulli** | Probability that x = 1 | Coin flips (0 or 1) |
| **Binomial** | N observations, probability | Count of successes |
| **Uniform** | Start and end points | Number in that range |

---

# Demo

<img src="../figs/statistical_building_blocks/binomial_demo_qr-14834.png" width="500">
