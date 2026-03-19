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

# The "intro to stats" view of stats

<div class="note-box" data-title="Choosing a test">

You have several options to choose from:
- Want to compare the means of distributions? Use t-tests or ANOVAs
- Want to compare trends? Use correlations or regressions
- Etc.

</div>

---

# Where do those tests come from?

<div class="note-box" data-title="Types of observations">

Consider what sorts of values your observations can take on:
- Real numbers?
- Counts?
- Probabilities?
- Sets of numbers that sum to 1?

</div>

---

# Where do those tests come from?

<div class="important-box" data-title="Key idea">

Then we can ask: under different (typically very simple) assumptions about where the numbers came from, how likely would it be to see something like our actual data?

</div>

---

# Where do those tests come from?

<div class="example-box" data-title="Example">

**Data:** [-1.2, 2.04, 0.087, -0.1, ...]

How unexpected would these numbers be if:
- We thought the numbers came from a Normal distribution with mean = 0, var = 1
- We thought the numbers came from a Normal distribution with mean = 100, var = 1

</div>

---

# Where do those tests come from?

<div class="note-box" data-title="Building tests from distributions">

- To create the different tests you learn about in introductory stats courses, people have solved out the probabilities of observing different (sets of) values under different assumptions
- The p-value we get out tells us how unlikely it was that the observed data came from some "null" distribution

</div>

---

# Making your own statistical tests

<div class="note-box" data-title="Distributions and parameters">

- Different distributions can produce different types of draws-- Real numbers, counts, etc.
- Each distribution is typically controlled by one or more parameters-- mean/variance, probabilities, etc.

</div>

---

<!-- _class: scale-78 -->

# Probability distributions

| **Distribution name** | **Parameter(s)** | **What you get out** | **Example draws** |
|-|-|-|-|
| **Gaussian (Normal)** | Mean, variance | Real numbers | -0.2, -10.923, 45.08, -6.4545 |
| **Bernoulli** | Probability that x = 1 | Results of "coin flips" | 0, 1, 1, 0, 1, 0, 0, 0 |
| **Binomial** | Number of observations, probability that each observation is 1 | The number of observations where x = 1 | 10, 5, 38, 0, 267 |
| **Multinomial** | Number of observations, probability that each *feature* in each observation is 1 | The per-feature counts showing how many times each feature was 1 | [3, 10, 2, 27], [46, 5, 4, 0] |
| **Uniform** | Start and end points (Real numbers) | A number between the start and end points | 0.2, 0.7532, 0.00000123 |
| **Von Mises** | Circular mean and concentration | Angles | 3.6, 186, 240, 359.98 |

---

# Making your own statistical tests

<div class="tip-box" data-title="Recipe for a statistical test">

1. Pick an appropriate distribution
2. Pick parameters that correspond to your "null hypothesis" (e.g., that the distribution has a mean of 0, that the values are equally likely, etc.)
3. Take a bunch of samples from your distribution
4. Compare the values of those samples to your actual data

</div>

---

# Example: is a coin fair?

<div class="example-box" data-title="Setting up the problem">

Suppose you observe some coin flips: [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, ...]

How could you figure out whether the coin is fair (e.g., explainable by 0 and 1 being equally likely)?

</div>

---

# Example: is a coin fair?

<div class="note-box" data-title="Step 1: Choose a distribution">

Suppose you observe some coin flips: [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, ...]

First, we need an appropriate distribution

</div>

---

# Example: is a coin fair?

<div class="example-box" data-title="Step 2: Set up the null hypothesis">

- Suppose you observe 12 coin flips: [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
- For a fair coin, p(1) = 0.5
- We know that the number of "events" is 12 (i.e., the number of flips)
- Now we can ask: what's the probability of observing 3 or fewer 1s if the coin is fair?

</div>

---

# Example: is a coin fair?

<div class="example-box" data-title="Step 3: Compute the p-value">

- Suppose you observe 12 coin flips: [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
- Parameters: N = 12, p(x = 1) = 0.5
- Now take a bunch of draws from the binomial distribution. Let's take 1,000,000 draws and ask: what proportion of those draws have a count less than or equal to 3?
- That's our p-value!

</div>

---

# Demo

<img src="../figs/statistical_building_blocks/binomial_demo_qr-14834.png" width="500">
