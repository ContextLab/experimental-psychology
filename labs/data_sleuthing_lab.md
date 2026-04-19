---
title: Data Sleuthing Lab
author: Jeremy R. Manning
mainfont: Palatino
geometry: margin=1in
colorlinks: true
linkcolor: green
fontsize: 12pt
header-includes:
  - '`\usepackage{emoji}`{=latex}'
---

# \emoji{detective} Overview

What can (and *can't*!) data tell us? In this lab, your team will explore this
important issue by playing two roles: **data creator** and **data sleuth**. Your
job in the "creator" role will be to (as the name implies)  *create* a dataset
to be shared with another team.  Later, once you've passed off your team's
dataset and received a new one from another team, your team will transition
into a "sleuth" role, where you'll examine and analyze different aspects of the
dataset.

# \emoji{detective} Learning objectives

The goal of this lab is to learn about the "results" sections of scientific
articles.  In general, results sections report the *results* of the analyses
described in the paper's methods section.  A good results section will also help
its audience to understand the basic logic of the study, any critical design
decisions pertaining to the analyses, and how the different findings might be
interpreted.  To that end, you'll:

- Practice communicating clearly and directly
- Improve your understanding of what goes into creating a dataset
- Gain intuitions about what you can versus can't conclude from a given dataset
- Practice wrangling and analyzing data, creating figures, and running statistical tests
- Practice interpreting results
- Practice thinking about study design, resources, effort allocation, and time management

# \emoji{detective} Procedure

We'll divide the class into four teams: A, B, C, and D.  Each team will begin by
finding or creating a dataset, following some specific guidelines (outlined
below).  You'll also create some "documentation" for the dataset.  As part of
putting your dataset's documentation together, you'll come up with a set of
questions to be explored or answered about your dataset.

In the second phase of the lab, you'll pass your dataset onto another team and
receive a dataset from a different team (A will give their dataset to B; B to C,
and C to D; D to A).  Using the "sending" team's questions as a guide, the "receiving"
team will work with their designated teaching assistant to examine the dataset.

You'll conclude the lab by drafting a "results section" based on the dataset you
analyzed.

## \emoji{magnifying-glass-tilted-right} Part 1: Construct a dataset!

Your team's dataset can be made-up (fake) or real (e.g., downloaded from a
public repository, etc.).  However, whether you create a fake or real dataset,
it should be *interesting* (broadly construed), and it must follow several
formatting guidelines:

  1. Your dataset should contain a minimum of 500 observations and a maximum of 10,000 observations.
  2. Each observation should include at least 5 features and no more than 100 features.  For example, if you
  were constructing a dataset about fish swimming in an aquarium, each "feature"
  might be some aspect of a fish's position in the tank (e.g., $x$, $y$, and $z$
  coordinates, and perhaps the yaw, pitch, and roll of the fish relative to each
  axis).
  3. You should save your dataset as a Google Sheet (set sharing permissions to "anyone with a link can view"):
  
      - Top row: column labels (single word or abbreviation, lowercase, no non-letter characters)
      - Each subsequent row should have a single observation
      - Each column should correspond to a single data feature
      - Data values should either be integers (1, 2, 3, etc.), real numbers
      (3.14, 2.71, -45.6789, etc.), dates or times (12:50:00 04/18/2022, etc.),
      or character strings ("happy", "sad", "angry", "excited", etc.; note: strings don't need to be enclosed by quotation marks).
      - The formatting should be consistent throughout the dataset (to facilitate analysis)
      - The formatting should be consistent within each column-- e.g., all of the values in a column should have the same "type"
  4. Create documentation for your dataset (save as a Google Doc; set sharing permissions to "anyone with a link can view").  Include the following information:
  
     - Where did the data come from?  This can be made up, but it should be explained!  Interesting back stories are encouraged.  Help to motivate the team you're sending the dataset to.
     - How were the data collected? Briefly explain, in 1--2 paragraphs.
     - What do each of the features mean, in plain English?
     - What are the observations?  (E.g., timepoints?  People?  Trials?)
     - A list of 5 questions:
       
       - All questions must seem plausible
       - All questions must be answerable (or potentially answerable) with a relatively straightforward analysis (e.g., PSYC 10-style statistical test, a basic chart or figure, etc.).  In other words, you should keep the scope of the questions relatively narrow and specific.
       - At least 1 question should be possible to explore/answer using the dataset
       - At least 1 question should be *im*possible to explore/answer using the dataset
       - All other questions can either be possible or impossible to explore/answer using the dataset
       - Keep track of which questions can/can't be answered with the dataset, but keep those labels hidden (i.e., don't put it in your to-be-shared documentation)

Once you've created your team's dataset, documentation, and "possible vs. impossible" labels for each question, upload your materials using [this form](https://forms.gle/NV5TqtpZwKhz21sw8).

## \emoji{magnifying-glass-tilted-right} Part 2: Check out the data!

Each team will analyze data from their designated source team.  Answer each of
the five questions included in your received dataset's documentation using any
approach you deem appropriate.  Figures and stats are encouraged!

For each question, document the following:

  - State any assumptions you're making to answer the question
  - Explain how you'll approach answering question with the given analysis.  In other words, explain how what you're trying to discover relates to the analytic tools and approaches you're employing.
  - Explain what conclusions can or can't be drawn from the given analysis (according to how the analysis turned out).
  - If you think a particular question is impossible to answer, explain why-- and what you'd need (from the dataset, analytic tools, etc.) in order to be able to answer that question.  You should still carry out *some* sort of analysis for each question; the idea is to notice and document when the insights possible to attain from a particular analysis fall short of the question(s) you're trying to answer about the data.

Your team can share a common document and set of analyses, figures, stats, etc.

# \emoji{detective} Writing your lab report

Your writeup for this lab will mimic a "results section" of a scientific article,
about the dataset you analyzed with your team.  You should include the following elements:

  - For each question:
    - Create at least one figure
    - The figure should include a caption describing what the figure is showing
    - Also write (roughly) a paragraph of text describing the key analyses, results,
      relevant interpretations, etc.  For example, describe "answers" or "insights" into the question that you gained through your analyses, or describe how the question is impossible to answer given the data, etc.
  - Organize the questions and paragraphs so that they tell a "story" about the dataset.
  - Add transition sentences as needed.
  - Add an "overview" paragraph at the beginning to summarize the dataset, how it was analyzed, and what you found.
  - Include a brief paragraph reflecting on how you used generative AI during this lab.  What analytical suggestions did AI provide?  Were they useful?  Did AI help you see the data differently?

# \emoji{detective} Using GenAI in this lab

Generative AI can be a powerful analytical partner-- but only if you understand both its capabilities and its limits.  In this lab, you'll deliberately compare two ways of working with GenAI: a **hands-off** approach (where you let the AI decide everything) and a **hands-on** approach (where you specify exactly what you want).

## \emoji{magnifying-glass-tilted-right} Part A: The hands-off prompt

Take your dataset and ask your GenAI tool of choice (e.g., ChatGPT, Claude, Gemini) to **analyze it for you**, without providing further clarifications or specifications.  A prompt as simple as *"Here's a dataset.  Please analyze it and tell me what you find."* is fine.  Then reflect carefully on what happened:

  - **Which analyses did the AI choose?**  Did it run a t-test?  Compute correlations?  Make a histogram?  Do something more complex?
  - **Were the chosen analyses *appropriate* for the data?**  For example, did it use a t-test on continuous data when chi-squared would have been more appropriate?  Did it compute correlations between variables that don't make sense to correlate?
  - **Were the analyses implemented correctly?**  If the AI showed you code, does the code actually do what it claims?  If it just gave you results, can you reproduce them?
  - **Did the AI come to its own conclusions?**  Did it claim to find a "significant effect" or "important pattern"?
  - **Were those conclusions accurate or hallucinated?**  How can you tell?  Can you verify them against the actual data?

Document what you found.  Be specific: include the exact prompts you used, the AI's responses, and your verification steps.

## \emoji{magnifying-glass-tilted-right} Part B: The hands-on prompt

Now switch modes.  Pick *one specific analysis* you want to perform on your dataset (it can be one of the questions from your dataset's documentation, or something new you noticed in Part A).  Before opening any AI tool:

  1. **Outline the analysis step by step on paper or a whiteboard.**  What are the inputs?  What's the output?  What intermediate steps are needed?  What test or visualization will you use?  How will you interpret the result?
  2. **Construct a detailed prompt** for your GenAI tool.  Include: the structure of the dataset (column names, types), the specific question you're answering, the analysis steps you've outlined, and the format you want the output in.
  3. **Run the prompt** with your dataset attached.

Then reflect:

  - Did the AI follow your specification, or did it deviate?
  - Was the result more accurate, more useful, or easier to verify than what Part A produced?
  - What was easier?  What was harder?
  - Were there steps you specified that the AI got wrong?  Were there steps you *didn't* specify that the AI handled well anyway?

## \emoji{magnifying-glass-tilted-right} Reflection

In your writeup, compare the two approaches.  When is the hands-off approach acceptable?  When is it dangerous?  What does the hands-on approach require *you* to bring to the table?  What does this tell you about how (and when) to use GenAI as a scientific collaborator?

The ability to use AI as an analytical tool *while maintaining rigorous verification* is one of the most valuable skills you can develop as a scientist.  AI can do the computational heavy lifting, but *you* must be the one who knows whether the results make sense.

# \emoji{detective} Closing discussion points

The results section of a scientific paper is, in many ways, its core.  The "merit" of a paper
typically rests on how accurately and effectively it communicates the main findings of
the study.  For example:

  - Was the dataset appropriate for answering the proposed questions?
  - Were the analyses appropriate?
  - Were the interpretations and/or conclusions justified by the data (or analyses)?
  - Are the results visualized in an intuitive way?
  - Are the results communicated clearly?
  - Was the "logic" of the analytic approach clear and/or easy to follow?

Achieving these ideals is not simply a matter of listing sets of numbers or the
outcomes of a series statistical tests.  You need to help your intended audience
understand *why* the approaches you took helped you to understand the questions
you explored, how the questions fit together into a cohesive narrative, and so
on.  In other words, you need to make your "story" easy to read, easy to
believe, and easy to follow.
  