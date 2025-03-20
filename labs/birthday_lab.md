---
title: PSYC 11 Birthday Matching Lab
author: Jeremy R. Manning
mainfont: Palatino
geometry: margin=1in
colorlinks: true
linkcolor: green
fontsize: 12pt
header-includes:
  - '`\usepackage{emoji}`{=latex}'
---

# \emoji{birthday-cake} Overview

We're all familiar with asking questions in everyday conversation-- but how can
we ask questions in a *scientific* way when we are carrying out research?  While
there is no single "universal" approach to asking questions in a scientific way,
this lab is intended to help get you thinking about how to design questions in
ways that can be (a) formalized, (b) quantified, and (c) explicitly tested.

# \emoji{birthday-cake} Learning objectives

This laboratory exercise is intended to help you:

  - Practice formulating questions in a scientific way
  - Practice formulating a hypothesis about the "answer" to your question
  - Practice formally testing a hypothesis using the following approaches:
    - Data wrangling
    - Applying statistical tests
    - Interpreting results
    - Presenting or describing results

# \emoji{birthday-cake} Procedure

## \emoji{cupcake} Step 1: data collection

Please fill out our class's [birthday survey](https://forms.gle/rXVBtfNXLKewrZtL6) with your birth month and day.  Once all students have submitted their responses, a spreadsheet containing the collected data will be available [here](https://docs.google.com/spreadsheets/d/1VkNjgUe0bf-RObDgtnnvVJb_xhHa-39nLz53k9Nk_HE/edit?usp=sharing).  Important note: *do not "peek" at the data before you have completed Steps 2 and 3, below*!

## \emoji{cupcake} Step 2: formulate your questions as testable hypotheses

In this lab, we will be exploring 3 questions:

  1. How many students in our class share the same birthday (month and day)?
  2. How many students in our class share the same birth *month* (i.e., excluding the day)?
  3. How many students in our class share the same birth *day* (i.e., excluding the month)?

**Before** looking at the data, take some time to discuss with your group what you think the answers to each question might be.  To get you started, you might consider:

  - What are the chances that any two randomly chosen students from the class share a birthday?
  - How can you extrapolate from the probability of two students matching to
  predict how many students in the class share their birthdays?
  - Make sure your framing of the question is unambiguous.  For example, are you going to try to explain the *maximum* number of students with the same birthday?  Or are you trying to explain the number of students who share a birthday with *at least* one other student in the class?  Or something else?
  - How might the way you formalize your question affect your answer?

## \emoji{cupcake} Step 3: define your statistical test(s)

Drawing on your prior knowledge of statistics (also feel free to Google and/or
consult with your lab leader!), try to write out one or more formal tests of
your hypothesized "answers" to the questions in Step 2.  For example:

  - Will you be using a $t$-test?  An ANOVA?  A $\chi^2$-test?  A correlation?  Something else?
  - How many tests will you need to carry out?  If you run multiple tests, will all of the tests be set up the same way?  Do you need to account for multiple comparisons if you're running multiple tests?  (And if so, how would you do that?)
  - Consider the possible *outcomes* of your test(s).  What would it look like if your hypotheses are correct versus incorrect?

## \emoji{cupcake} Step 4: implement your statistical test(s)

Assuming you've completed Steps 1--3, you're finally cleared to take a look at
the data!  Within Google Sheets, make a copy of the [dataset](https://docs.google.com/spreadsheets/d/1VkNjgUe0bf-RObDgtnnvVJb_xhHa-39nLz53k9Nk_HE/edit?usp=sharing).  Use [built-in formulas](https://support.google.com/docs/table/25273?hl=en), [Google Colaboratory](https://colab.research.google.com/), SPSS, R, [VassarStats](http://vassarstats.net/), or any other tool you're familiar with, to carry out each of the tests you described in Step 3.  Record the results.

## \emoji{cupcake} Step 5: draw conclusions and communicate your findings

Work with your group to interpret the results of the tests you ran.  For example:

  - Was the observed number of people with matching birthdays greater than or less than what you had expected?
  - Were the differences statistically reliable?
  - What do you think might explain your findings?
    - Did you confirm or refute your hypothesis?
    - Given what you have learned, could you generate a new (testable!) hypothesis (if appropriate)?
  - How might you formally study and/or test your new hypothesis (if appropriate)?

Plan with your group how to briefly communicate your approach and findings to the class.

# \emoji{birthday-cake} Closing discussion points

Consider what you and your classmates have learned from the birthday data we've collected in this lab.  Think about how the conclusions about "matching" between students might compare if we had instead collected data about one or more of the the following:

  - Street numbers (digits only) of a childhood residence
  - "Randomly" (privately) chosen numbers between 1 and 100
  - Favorite colors
  - Favorite foods
  - Last digit of childhood phone number or zip code

Finally, think about how the questions we've considered in this lab might compare to higher-level questions about psychology.  For example:

  - Are people better at remembering other people's names or their faces?
  - What makes some movies scary (or funny, sad, exciting, engaging, etc.)?
  - How many things can people think about simultaneously?
  - How effectively can two people communicate if they don't share any common languages?
  - Do all people have the same basic set of feelings and emotions?
  - Can people learn to get better at learning?

In other words: how might you turn high-level *qualitative* questions about abstract aspects of the human mind (or the human experience) into *quantitative*
questions that we can turn into formal, testable, hypotheses?  Are there general
strategies we can use, or is every question unique?  Can "anything" be quantified or turned into a testable question, or are there limits to what we can ask scientifically?