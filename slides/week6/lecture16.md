---
marp: true
theme: cdl-theme
math: katex
transition: fade 0.25s
author: Contextual Dynamics Lab
---

# Quick-start guide to experimental design

### PSYC 11: Laboratory in Psychological Science

Jeremy R. Manning
Dartmouth College
Spring 2026

---

# What is the purpose of running an experiment?

<div class="note-box" data-title="Goals of experimentation">

- Understand or explore how something works
- Distinguish between several potential alternatives
- Get more information (data!)

</div>

---

<!-- _class: scale-90 -->

# What kind of study are you running?

<div class="definition-box" data-title="Different study types make different kinds of claims">

- **Controlled experiment:** you manipulate something; lets you make causal claims about that thing
- **Observational/correlational:** you measure naturally-occurring variation; correlations only, not causation
- **Descriptive:** you characterize what something looks like (frequencies, patterns, distributions); no comparison required
- **Qualitative:** interviews, open-ended responses, content analysis; rich detail, smaller samples
- **Mixed methods:** combinations of the above

</div>

<div class="warning-box" data-title="The trap to avoid">

The kind of study you run determines the *kind of conclusions you can draw*. Picking the wrong framing &mdash; or pretending you have a controlled experiment when you actually have a correlational one &mdash; will make your discussion section much harder to write honestly.

</div>

---

<!-- _class: scale-80 -->

# Two big design philosophies

<div class="important-box" data-title="Control vs. realism">

- **Classic (maximize control):** simplify the phenomenon, manipulate specific factors, measure the differences. *Strong* causal claims, but only about your simplified setup.
- **Naturalistic (maximize realism):** create a rich, realistic scenario, measure many things, mine the data for patterns. *Generalizable* findings, but harder to attribute to any one cause.

</div>

<div class="tip-box" data-title="The hidden cost of each">

- **Highly-controlled** studies often answer questions that nobody outside the lab cares about
- **Highly-naturalistic** studies often produce findings nobody can explain
- A good design is *deliberate* about where on the spectrum it lives, and **says so explicitly** when interpreting results

</div>

---

<!-- _class: scale-80 -->

# Confirmatory vs. exploratory: track which is which

<div class="definition-box" data-title="Two kinds of analyses, two kinds of claims">

- **Confirmatory (hypothesis-testing):** the question and the analysis were decided **before** you saw the data
- **Exploratory:** the question or analysis came **after** you looked at the data

</div>

<div class="warning-box" data-title="Both are valuable &mdash; but they support different conclusions">

- A *confirmatory* finding can be reported as evidence for or against a specific hypothesis
- An *exploratory* finding is a *suggestion* for a future study to test, not a conclusion in itself
- The difference matters because **anything will look interesting if you go fishing for it**. Reporting a fishing-trip finding as if it were a tested prediction is one of the most common mistakes in published science

</div>

<div class="tip-box" data-title="Practical move">

Write down your hypotheses and planned analyses *before* you collect data. When you discover something cool in the data later, you can still report it &mdash; just label it exploratory.

</div>

---

<!-- _class: scale-80 -->

# Common design pitfalls

<div class="warning-box" data-title="What goes wrong in real student projects">

- **Confounds:** something other than your manipulation differs between conditions (e.g., one condition was always run in the morning, the other always at night)
- **Demand characteristics:** participants guess what you expect and shift their behavior accordingly
- **Missing baseline:** without a comparison, you can't tell whether your "effect" is anything at all
- **Too many variables at once:** one clear comparison beats five murky ones
- **Outcome is unmeasurable:** "creativity," "happiness," "engagement" can be hard to operationalize; pick something concrete you can actually score
- **The "ceiling" or "floor" trap:** if everyone scores 100% (or 0%), you can't see your effect even if it's real

</div>

---

# Discussion: what's your design?

<div class="example-box" data-title="In your project groups, identify...">

- What **kind** of study is this? (Controlled? Observational? Descriptive? Qualitative? Mixed?)
- What is the **specific question** you're trying to answer?
- What does **success** look like? What does **failure** look like? (Both should be possible with your design!)
- What's the **single biggest threat** to your interpretation? (Confound, missing baseline, ceiling, etc.)
- Be ready to share with the class

</div>

---

<!-- _class: scale-80 -->

# Implementation: what tools should you use?

<div class="note-box" data-title="A spectrum">

- **Low-tech:** notebooks, voice recordings, Google Forms
- **Mid-tech:** Qualtrics surveys, slideshow paradigms
- **High-tech:** PsychoPy, jsPsych, custom web pages, Colab notebooks

</div>

<div class="tip-box" data-title="GenAI as your implementation partner">

You can ask Claude, ChatGPT, Gemini, etc. to build your experiment for you! A particularly nice pattern:

- Ask for a **single-file HTML page** that runs the entire experiment in the browser
- Have it save data after each run (e.g., download as a `.csv`, or POST to a Google Form/Apps Script endpoint)
- No server, no install, no setup &mdash; just open the file in a browser

</div>

<div class="warning-box" data-title="Verify it actually works">

GenAI-built experiments often look correct but mis-record data, skip conditions, or misorder trials. Pilot test with yourself first &mdash; *and* check the saved data file before recruiting any participants.

</div>

---

<!-- _class: scale-75 -->

# Working with human participants

<div class="important-box" data-title="Two requirements before you collect any data">

1. **Watch the human-subjects training video** (more info on Friday)
2. **Get my explicit written approval** of your study before you collect data &mdash; I'm acting as the IRB for this course

</div>

<div class="note-box" data-title="What I'll be looking for">

- A **clear description** of what participants will do
- A **consent statement** participants will see before starting
- An assessment of any **risks** (usually minimal for our projects, but say so)
- How **data are stored**, and whether anything is identifying
- A **debrief statement** participants will see after finishing
- Any potentially harmful **stimuli** or **procedures**

</div>

<div class="warning-box" data-title="Please ask me and/or the TAs to review your materials!">

- Ask for feedback on your experiment before you run it on participants
- Ethics approval looks for potential harms to participants. It does *not* provide feedback on whether your experiment is well-designed or will actually answer your question. You need to ask for that separately!

</div>

---

# Practical advice

<div class="tip-box" data-title="Keep these in mind">

- **Simplicity:** the art of maximizing the amount of work *not* done
- **Pilot test early.** Run your study on yourself, then a friend, before recruiting strangers
- **Plan your analysis before collecting data.** If you can't say what you'd do with the data, the design isn't done yet
- **Work together and ask for help**
- **You have 3&ndash;4 weeks** &mdash; scope accordingly

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

- **Today**: Work on designing your experiment. Literature Review Lab writeup *and* Weekly Snippet 1 are due by 11:59PM!
- **Friday**: Implement your experiment

</div>
