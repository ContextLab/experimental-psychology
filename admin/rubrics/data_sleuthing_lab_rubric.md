# Data Sleuthing Lab Rubric (10 points total)

## Criterion 1: Overview and dataset description (1 point)

**Description:** Open with an overview paragraph that summarizes the dataset (source, observations, features, sample size), the questions you explored, and a high-level preview of findings. Briefly describe the dataset's structure, including feature types and any quirks (missing data, unusual distributions, suspicious values) noticed *before* running analyses.

| Points | Rating | Description |
|-|-|-|
| 1 | Exceeds | Overview names specific features, observation counts, and a 1–2 sentence summary of *each* major finding (not just "we found some interesting patterns"). Dataset description identifies feature *types* (categorical, ordinal, continuous) correctly and notes at least one specific data quirk that shaped subsequent analyses — e.g., "27 of the 540 rows had missing values in the `score` column, which we excluded from analyses involving that variable." |
| 0.5 | Below | Overview is generic ("the dataset has 5 columns and we ran some tests") or dataset description doesn't engage with the actual data structure (e.g., doesn't classify feature types, ignores missingness or outliers). |
| 0 | No evidence | Either section is missing, or both are present but contain no substantive content. |

---

## Criterion 2: Per-question analyses — analytic approach (2 points)

**Description:** For each of the five questions in the dataset's documentation, describe the analytic approach you took. Explain *how* the analysis connects to the question — i.e., why the test or visualization you chose actually addresses what's being asked. State any assumptions you needed to make.

| Points | Rating | Description |
|-|-|-|
| 2 | Exceeds | All five questions are addressed with a clearly motivated approach. The connection between question and analysis is explicit — e.g., "Q3 asks whether group X scored higher than group Y on the survey, so we ran an independent-samples t-test comparing the two groups' mean scores." Assumptions are stated explicitly (e.g., "we treated the 1–7 ratings as continuous"; "we excluded rows with missing data"). When the chosen analysis is non-obvious, the writeup explains why it was preferred over alternatives. |
| 1.5 | Mastery | All five questions addressed, but for some questions the analytic approach is described without clearly tying it back to the question — i.e., reader has to infer why the test was chosen. Assumptions may be partially stated. |
| 1 | Near | Three or four questions addressed; or all five but the analytic descriptions read as recipes ("we ran a t-test") without justification. |
| 0.5 | Below | Only one or two questions addressed substantively. Approaches are not justified. No assumptions stated. |
| 0 | No evidence | Per-question analyses are missing or each is a single sentence. |

---

## Criterion 3: Statistical results (1.5 points)

**Description:** Report relevant statistical results for each (answerable) question: the test statistic, $p$-value, effect size, and a 95% confidence interval where appropriate. Numbers should be reported with reasonable precision and matched to the right tests.

| Points | Rating | Description |
|-|-|-|
| 1.5 | Exceeds | Statistical results include all four pieces (statistic, $p$, effect size, CI) wherever applicable. Effect sizes are correctly chosen for the test (Cohen's $d$ for t-tests, $\eta^2$ for ANOVA, $r$ or $r^2$ for correlations, Cramér's $V$ for chi-squared). CIs match the parameter being estimated (e.g., CI for the mean difference, not for the test statistic itself). |
| 1 | Mastery | Test statistic and $p$-value are reported correctly. Effect sizes and CIs are present for most tests but missing or incorrect for some. |
| 0.5 | Below | Only $p$-values are reported, with no effect sizes or CIs. Or numbers are reported but tests are mismatched to data type (e.g., chi-squared on continuous variables). |
| 0 | No evidence | No statistical results, or results are unintelligible / clearly fabricated. |

---

## Criterion 4: Figures (1.5 points)

**Description:** Include at least one figure per (answerable) question — five figures total if all questions are answerable. Each figure should have a caption describing what it shows. Figures should be clearly labeled (axes, units, legends) and should *support* the analytic claim being made — not just decorate.

| Points | Rating | Description |
|-|-|-|
| 1.5 | Exceeds | All required figures are included, properly labeled, and have informative captions. Each figure is referenced in the text and *visually demonstrates* the claim being made — e.g., a bar plot with error bars when discussing group means; a scatter plot with a fitted line when discussing correlations. Figure choices match the data type (no pie charts for continuous data, no bar plots when a histogram would be clearer). |
| 1 | Mastery | All required figures present with reasonable labeling and captions. May have minor issues — e.g., one figure missing units, or a chart type that isn't optimal for the data. |
| 0.5 | Below | Some figures missing, or figures present but unlabeled / uncaptioned / illegible. Screenshots of raw spreadsheet data don't count as figures. |
| 0 | No evidence | No figures, or figures so degraded they can't be interpreted. |

---

## Criterion 5: Possible vs. impossible judgments (1 point)

**Description:** Across your five questions, identify which you judged to be possible vs. impossible to answer with the dataset. Explain *why* you classified each one as you did. For impossible questions, describe what additional data, design, or analyses would be needed to answer them. Reflect on any judgment calls or ambiguous cases.

| Points | Rating | Description |
|-|-|-|
| 1 | Exceeds | Each of the five questions is explicitly classified (possible / impossible / partial). For impossible questions, the writeup names the *specific* gap — e.g., "this asks about causation but we only have correlational data," or "this asks what would happen *before* the data collection window started, which we have no observations of." For partial cases, the writeup is honest about what *can* be inferred and what can't. The student also engages with whether their classification matches the creating team's intent (or notes that they don't know yet). |
| 0.5 | Mastery | All five questions classified with reasons. Reasoning may be less precise — e.g., "this question is too vague to answer" without specifying *what* would make it answerable. |
| 0.25 | Below | Only some questions classified, OR classifications are stated without explanation. |
| 0 | No evidence | No discussion of possibility/impossibility, or all five classified with no reasoning. |

---

## Criterion 6: Storytelling and structure (1.5 points)

**Description:** Organize the report so that the question-paragraphs tell a coherent story about the dataset. Use transition sentences between sections. The order of questions doesn't have to match the original documentation — pick an order that makes the narrative flow.

| Points | Rating | Description |
|-|-|-|
| 1.5 | Exceeds | Sections are clearly organized with transitions that meaningfully connect findings — e.g., "Having established that group means differ overall, we next asked whether this difference is driven by..." The chosen order makes narrative sense (e.g., descriptive findings before inferential ones; broader before narrower). The report reads as a *story* about the dataset, not a list of disconnected analyses. The opening overview and final reflection bookend the narrative coherently. |
| 1 | Mastery | Most sections flow logically with reasonable transitions. The order makes sense but transitions may be perfunctory ("Next, we examined...") rather than substantive. The story is mostly there but feels assembled rather than woven. |
| 0.5 | Below | Sections are present but feel disconnected. No transition sentences, or transitions are mechanical ("Next question."). Order may follow the documentation rigidly without considering what makes narrative sense. |
| 0 | No evidence | Report is a fragmented list with no organizational logic. |

---

## Criterion 7: GenAI exploration writeup (1.25 points)

**Description:** Document your two-part GenAI exercise. Part A (hands-off): include the prompt, a summary of the AI's output, and your verification. Identify at least one analysis the AI got right and one it got wrong, with evidence. Part B (hands-on): include your analytic plan, the constructed prompt, and a summary of the output. Compare Part A and Part B. Conclude with a reflection on when each approach is appropriate.

| Points | Rating | Description |
|-|-|-|
| 1.25 | Exceeds | Both parts are documented with the actual prompts used (not paraphrased). Part A includes a *verified* example of an AI mistake — e.g., "the AI claimed groups differed significantly with $p = 0.001$, but when we re-ran the test by hand we got $p = 0.18$; the AI used the wrong column." Part B's plan is concrete and step-by-step (not just "I asked for an ANOVA"). The comparison between A and B is substantive — e.g., "Part B caught an issue Part A had silently glossed over." The reflection identifies a *specific* condition under which hands-off is acceptable (e.g., "for quick exploration when the stakes are low and you'll verify before publishing") and a specific danger ("when the AI's confident tone hides errors that look correct on the surface"). |
| 0.75 | Mastery | Both parts documented with prompts and outputs. Verification is present but may be informal. The comparison between A and B is reasonable but doesn't go deep. Reflection is present but generic. |
| 0.25 | Below | Only one part attempted, OR both parts attempted but without specifics — no actual prompts, no verification, no comparison. Reads as if the student went through the motions without engaging. |
| 0 | No evidence | GenAI section is missing or a single paragraph with no documentation of what was actually done. |

---

## Criterion 8: Reflection on the experience (0.25 points)

**Description:** A brief reflection on the lab as a whole. What was the hardest part of being a "data sleuth"? What do you wish your dataset's creators had done differently? What will you keep in mind the next time you encounter a dataset you didn't create?

| Points | Rating | Description |
|-|-|-|
| 0.25 | Complete | Reflection names specific challenges (not just "the data was confusing") and articulates at least one concrete takeaway for future work — e.g., "I'll always check the distribution of every variable before running any test; the dataset we received looked normal until we plotted it and saw a huge outlier that explained our 'significant' result." |
| 0 | Missing | Reflection is generic, missing, or just a sentence saying the lab was hard/interesting. |

---

## Grading notes for TAs

- **AI-proofing**: The strongest AI-proof elements are the per-question analyses (Criterion 2), possible/impossible judgments (Criterion 5), and the GenAI exploration writeup (Criterion 7). Pay special attention to whether the writeup references *specific* features, *specific* values, and *specific* AI prompts/outputs that only someone who worked with the dataset would know.
- **Statistical correctness**: For Criterion 3, check that effect sizes match the test type. Cohen's $d$ for a chi-squared test is wrong; $\eta^2$ for a correlation is wrong. CIs should match the parameter being estimated.
- **Possible vs. impossible**: For Criterion 5, the *quality* of the reasoning matters more than whether the student's classification matches the creating team's intent. A student who correctly identifies that a "possible" question is actually only answerable under strong assumptions should be rewarded for the insight.
- **GenAI verification**: For Criterion 7, look for *evidence* that the student actually verified AI output (not just claimed to). The strongest reports will include a specific case where the AI's answer didn't match a hand-computed or independently verified result.
- **Specificity over length**: A concise report that names specific tests, specific results, and specific AI failures is worth more than a long report that speaks in generalities. The "could this have been written by someone who never opened the dataset?" test applies here too.
