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
  - Practice communicating findings to others

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

## \emoji{test-tube} Step 4: Analyze the data

Now you can look at the data!  Make a copy of the [class dataset](https://docs.google.com/spreadsheets/d/1MvZoEIU5OdAOVtUTw8QoYQdoz1HcOhInSqeZcE0wQgg/edit?usp=sharing) and carry out the statistical tests you planned in Step 3.  You can use [Google Colaboratory](https://colab.research.google.com/), Google Sheets, SPSS, R, [VassarStats](http://vassarstats.net/), or any other tool you're comfortable with.

For each test, record:

  - The test statistic and p-value
  - The effect size (if applicable)
  - Whether the result supports or contradicts your hypothesis

## \emoji{test-tube} Step 5: Interpret and communicate

Work with your group to interpret your results:

  - Were the relationships you predicted actually present in the data?
  - Were any results surprising?  Why might reality differ from your intuitions?
  - What alternative explanations might account for your findings?
  - What *can't* you conclude from this data?  (Think about confounds, sample size, and the limitations of correlational data.)
  - If you could collect additional data, what would you want to measure and why?

Prepare a brief presentation (2--3 minutes) for the class summarizing your group's most interesting finding.

# \emoji{brain} Using GenAI in this lab

Generative AI is a powerful tool for expanding what you can accomplish in this lab.  Here are some specific ways to leverage AI:

  - **Explore multiple statistical approaches**: Ask AI to suggest 3--5 different ways to test your hypothesis, and have it explain the assumptions and tradeoffs of each.  You might discover that a test you hadn't considered is actually a better fit for your data.
  - **Find published studies with similar designs**: Ask AI to find real psychology studies that investigated similar questions (e.g., the relationship between sleep and stress in college students).  How do their methods and findings compare to yours?
  - **Generate visualizations**: Ask AI to help you create publication-quality figures that effectively communicate your findings.  Experiment with different chart types and see which tells the clearest story.
  - **Brainstorm confounding variables**: Ask AI to help you think of variables that might explain away (or strengthen) the relationships you found.  This is excellent practice for thinking like a scientist.

## \emoji{test-tube} GenAI Challenge: Real vs. Fake Data

After you've completed your analysis of the real class data, try this:

  1. **Generate a fake dataset**: Describe the survey to a GenAI tool and ask it to generate a realistic-looking dataset of the same size and format as the real class data.  Be specific about the variables and their ranges.
  2. **Run the same analyses**: Apply your statistical tests and visualizations to the fake data.
  3. **Compare**: Which patterns are similar between the real and fake datasets?  Which are different?  Can you tell which dataset is real and which is fake just by looking at the results?
  4. **Reflect**: What does this tell you about how well AI "understands" human psychology?  Where does it get things right?  Where does it fall short?  What assumptions did the AI make about relationships between variables, and were those assumptions accurate?

This exercise will sharpen your intuitions about what makes real human data different from plausible-sounding fabrications-- a critical skill in an era where AI-generated content is increasingly common.

Remember: AI is most useful *after* you've done the hard work of thinking through your hypotheses and planned your analyses.  Use it to go deeper, not to skip the thinking.

# \emoji{brain} Writing your lab report

Your lab report should include the following elements:

  1. **Hypotheses**: State your 3 hypotheses clearly.  For each, explain how you refined it from a casual question into a testable prediction.
  2. **Methods**: Describe the survey, sample (your class), and the statistical tests you chose.  Explain *why* you chose each test.
  3. **Results**: Report the results of your 3 tests, including test statistics, p-values, and effect sizes.  Include at least one figure.
  4. **Interpretation**: Discuss what your results mean.  Address surprises, limitations, confounds, and what you would do differently in a follow-up study.
  5. **GenAI reflection**: Write a brief paragraph describing how you used generative AI during this lab.  What did you ask it?  What did you learn from the interaction?  Was the AI's output always accurate or useful?

# \emoji{brain} Closing discussion points

Think about what you and your classmates have learned from this survey exercise.  Consider:

  - How did the process of *formalizing* your intuitions change them?  Did any of your casual questions turn out to be harder to test than you expected?
  - Were there questions you wanted to ask that the survey couldn't answer?  What would you need to collect to answer them?
  - How does our class sample compare to the general population?  What limits our ability to generalize?
  - Think about how the skills you practiced today-- formulating hypotheses, choosing appropriate tests, interpreting results with appropriate caution-- apply to the *Introduction* section of a scientific paper.  A good introduction doesn't just state a question; it explains why the question is interesting, what's already known, and how the current study will add to that knowledge.

Finally, consider the bigger picture: how do you turn high-level *qualitative* questions about people's minds and behaviors into *quantitative*, testable hypotheses?  Is there a general strategy, or is every question unique?  Can "anything" be studied scientifically, or are there limits to what we can ask?
