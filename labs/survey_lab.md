---
title: "Psychology of Everyday Life Survey Lab"
author: Jeremy R. Manning
mainfont: Palatino
geometry: margin=1in
colorlinks: true
linkcolor: green
fontsize: 12pt
header-includes:
  - '`\usepackage{emoji}`{=latex}'
---

# \emoji{brain} Overview

How do we ask questions *scientifically*?  In everyday life, we make all sorts of casual observations about people-- "early risers are more productive," "people who exercise are happier," "too much screen time makes you stressed."  But are these observations actually *true*?  How would we even know?

The difference between casual intuition and scientific inquiry is *precision*.  Science requires us to (a) formalize our intuitions into specific, testable predictions, (b) collect data systematically, (c) apply appropriate statistical tests, and (d) interpret the results honestly-- even when they surprise us.

In this lab, you'll explore these ideas by designing and carrying out a mini-study of your classmates' everyday habits and attitudes.  You'll discover that turning a vague question like "does sleep affect stress?" into a rigorous scientific hypothesis is harder than it sounds-- and that the answers are often more nuanced than our intuitions suggest.

# \emoji{brain} Learning objectives

This laboratory exercise is intended to help you:

  - Practice formulating questions in a scientific way
  - Practice refining a high-level question into a specific, testable hypothesis
  - Understand the difference between scientific and non-scientific ways of asking questions
  - Practice collecting data systematically using a survey instrument
  - Practice selecting and applying appropriate statistical tests
  - Practice interpreting results and drawing conclusions
  - Practice collaborating with GenAI to refine an analysis plan and implement it

# \emoji{brain} Procedure

## \emoji{test-tube} Step 1: Take the class survey

Fill out our class's [Psychology of Everyday Life survey](https://forms.gle/WzY6GNiJHyQKNJcs5) with honest responses about your daily habits and attitudes.  The survey asks about things like:

  - How many hours of sleep you typically get
  - Your general stress level
  - How much time you spend on screens (outside of schoolwork)
  - How often you exercise
  - How much caffeine you consume
  - How happy you generally feel
  - How many hours per week you study
  - How socially active you are

The survey should take about 10 minutes.  Once everyone has submitted their responses, the collected data will be available [here](https://docs.google.com/spreadsheets/d/1MvZoEIU5OdAOVtUTw8QoYQdoz1HcOhInSqeZcE0wQgg/edit?usp=sharing).

**Important**: Do NOT look at the data before completing Steps 2 and 3!

## \emoji{test-tube} Step 2: Brainstorm and refine your questions

Before looking at the data, work with your group to brainstorm questions about the relationships between the survey variables.  Start with high-level, casual questions-- the kinds of things you might say in everyday conversation:

  - "Do people who sleep more feel less stressed?"
  - "Are people who exercise also happier?"
  - "Does screen time affect how well people sleep?"

Now, practice *refining* these into more precise, scientific questions.  For each casual question, consider:

  - **What exactly are you measuring?**  For example, "sleep" could mean hours of sleep, sleep quality, consistency of sleep schedule, etc.  Our survey measures hours per night-- so your question needs to be about *that specific measure*.
  - **What kind of relationship are you predicting?**  A positive correlation?  A negative correlation?  A difference between groups?  Be specific.
  - **How strong do you expect the relationship to be?**  Will it be obvious, or subtle?
  - **What might *confound* the relationship?**  For example, if exercisers are also happier, is that because exercise causes happiness, or because some third factor (e.g., having more free time) enables both?

With your group, choose 3 questions to investigate.  Write each one as a formal, testable hypothesis.  For example:

  - *Casual*: "Sleep helps with stress"
  - *Scientific*: "Students who report sleeping 7 or more hours per night will report significantly lower stress levels (on a 1--10 scale) than students who report sleeping fewer than 7 hours, as measured by an independent-samples t-test."

## \emoji{test-tube} Step 3: Plan your statistical tests

For each of your 3 hypotheses, decide (before looking at the data!) which statistical test is most appropriate.  Consider:

  - Are you comparing two groups (t-test)?  More than two groups (ANOVA)?
  - Are you looking for a relationship between two continuous variables (correlation)?
  - Is one or both of your variables categorical (chi-square test)?
  - If you're running multiple tests, do you need to correct for multiple comparisons?
  - What would your results look like if your hypothesis is correct?  What about if it's wrong?

Write down your planned tests for each hypothesis.

## \emoji{test-tube} Step 4: Analyze the data with GenAI

Now you can look at the data!  Make a copy of the [class dataset](https://docs.google.com/spreadsheets/d/1MvZoEIU5OdAOVtUTw8QoYQdoz1HcOhInSqeZcE0wQgg/edit?usp=sharing) and carry out the analyses described in the "Using GenAI" section below.

# \emoji{brain} Using GenAI in this lab

Generative AI is a core tool for this lab.  You'll use it to refine your analysis plan, implement your statistical tests, and sanity-check your results.  The goal is to learn how to *collaborate* with AI effectively-- treating it as a capable but imperfect research partner.

## \emoji{test-tube} Getting set up

Dartmouth students have free access to several powerful AI tools:

  - [**Dartmouth Chat**](https://chat.dartmouth.edu) — free for all Dartmouth community members. Includes GPT, Claude, Gemini, and Llama models. Log in with your Dartmouth credentials. This is the easiest starting point.
  - [**Claude for Education**](https://claude.dartmouth.edu) — free Claude Pro access for Dartmouth students via the Anthropic partnership. Log in with your Dartmouth credentials for the first time.
  - [**Google Gemini**](https://gemini.google/students/) — check if the student offer is still available, or access Gemini models through Dartmouth Chat.

Pick whichever tool you're most comfortable with (or try more than one!).

## \emoji{test-tube} The AI-assisted analysis workflow

Follow these steps with your group:

### 1. Come up with a plan

Start by drafting an analysis plan *on your own* (with your group).  Based on your 3 hypotheses from Step 3, sketch out:

  - Which statistical tests you'll use for each hypothesis
  - What figures or visualizations would help communicate your findings
  - What you expect the results to look like if your hypotheses are correct (and if they're wrong)

### 2. Refine, stress-test, and deepen with AI

Share your analysis plan with a GenAI tool and ask it to help you improve it.  Here's the critical thing to watch out for:

**GenAI tends to be highly sycophantic**-- it will very likely agree with whatever plan you suggest, even if your plan is logically flawed or uses the wrong test.  To get genuinely useful feedback, try prompting strategies like:

  - *"Play devil's advocate: what's wrong with this analysis plan?"*
  - *"What are 3 ways this plan could lead to misleading conclusions?"*
  - *"Assume I've made at least one mistake in my plan. Find it."*
  - *"If you were reviewing this plan as a skeptical peer reviewer, what would you flag?"*

Use the AI's pushback to strengthen your plan.  Did it catch something you missed?  Did it suggest a better test or an additional control?

### 3. Outline a robust analysis plan

Based on your AI-refined thinking, write out a final analysis plan.  Collaborate with the AI on this-- ask it to help you organize the plan clearly:

  - For each hypothesis: the exact test, the variables, what you'll report
  - Which figures you'll create and what they should show
  - Any additional exploratory analyses that might be interesting

### 4. Implement the plan

Use [Google Colaboratory](https://colab.research.google.com/) to implement your analysis.  You can ask your GenAI tool to help write the code-- describe what you need clearly (e.g., "I have a CSV with columns sleep_hours, stress_level, happiness... I want to run a t-test comparing stress between high and low sleepers and make a box plot").  The [companion analysis notebook](https://colab.research.google.com/github/ContextLab/experimental-psychology/blob/main/notebooks/survey_analysis.ipynb) provides templates to get started.

### 5. Sanity check

This is the most important step.  For every result and figure the AI helps you produce, ask yourself:

  - **Do the results make sense?**  If the AI says the correlation between sleep and stress is r = 0.99, that's probably a bug.
  - **Does the code do what you think it should?**  Even if you don't know Python, you can ask the AI: *"Explain this code line by line.  What is it actually doing?"*
  - **Is there evidence of hallucination?**  Did the AI reference functions that don't exist, or produce numbers that don't match the data?
  - **Try changing something small** (e.g., flip which group is "high" vs. "low") and see if the results change in the direction you'd expect.

### 6. Refine presentation

Work with the AI to polish your figures and results:

  - Ask it to suggest better chart types, color schemes, or labels
  - Have it help you write clear figure captions
  - Ask for alternative ways to visualize the same finding-- which tells the story most effectively?

# \emoji{brain} Closing discussion points

Think about what you and your classmates have learned from this survey exercise.  Consider:

  - How did the process of *formalizing* your intuitions change them?  Did any of your casual questions turn out to be harder to test than you expected?
  - Were there questions you wanted to ask that the survey couldn't answer?  What would you need to collect to answer them?
  - How does our class sample compare to the general population?  What limits our ability to generalize?
  - How useful was the AI as a collaborator?  Where did it help most?  Where did it fall short or lead you astray?
  - Think about how the skills you practiced today-- formulating hypotheses, choosing appropriate tests, interpreting results with appropriate caution-- apply to the *Introduction* section of a scientific paper.  A good introduction doesn't just state a question; it explains why the question is interesting, what's already known, and how the current study will add to that knowledge.

Finally, consider the bigger picture: how do you turn high-level *qualitative* questions about people's minds and behaviors into *quantitative*, testable hypotheses?  Is there a general strategy, or is every question unique?  Can "anything" be studied scientifically, or are there limits to what we can ask?
