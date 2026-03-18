<!--
Sync Impact Report
==================
Version change: N/A (template) → 1.0.0
Bump rationale: MAJOR — initial constitution creation from template

Modified principles: N/A (all new)

Added sections:
  - Principle I: Excellent Student Experience
  - Principle II: Maintainability
  - Principle III: Security and Privacy
  - Principle IV: Generative AI Mindfulness
  - Section: Course Structure and Research Pipeline
  - Section: Content Verification and Quality Assurance
  - Governance

Removed sections:
  - All template placeholders replaced

Templates requiring updates:
  - .specify/templates/plan-template.md — ✅ no updates needed
    (Constitution Check section is dynamically filled; principles are
    referenced at plan time)
  - .specify/templates/spec-template.md — ✅ no updates needed
    (generic spec structure accommodates course-specific requirements)
  - .specify/templates/tasks-template.md — ✅ no updates needed
    (task phases are project-agnostic)

Follow-up TODOs: None
-->

# Laboratory in Psychological Science (PSYC 11) Constitution

## Core Principles

### I. Excellent Student Experience

Every element of this course MUST deliver a delightful, mind-expanding,
and highly engaging learning experience. This principle is the
non-negotiable foundation; all other principles serve it.

- **100% Accuracy**: All course materials (slides, labs, assignments,
  rubrics, links, example code, datasets) MUST be verified for
  correctness before release. Verification means at minimum one of:
  web search confirmation, direct testing/execution of code or
  instructions, or independent cross-reference against authoritative
  sources.
- **100% Consistency**: Terminology, formatting, grading criteria, and
  expectations MUST be uniform across all content areas. A concept
  introduced in slides MUST use identical language in the corresponding
  lab and assignment. Rubric criteria MUST map unambiguously to
  assignment instructions.
- **Clear Expectations**: Students MUST always know what is expected of
  them. Every assignment MUST state its learning objectives, deliverables,
  evaluation criteria, and due date. Grading rubrics MUST be published
  alongside or within each assignment.
- **Comprehensive and Fair Evaluation**: Assessments MUST measure what
  they claim to measure. Rubrics MUST be applied consistently across all
  students. Evaluation criteria MUST be specific enough that two
  independent graders would reach substantially similar scores.
- **Challenging and Engaging Content**: Materials MUST push students
  beyond their comfort zone while remaining achievable. Labs and
  assignments MUST connect to real-world research practices. Content
  SHOULD provoke curiosity and reward deep engagement over surface-level
  completion.

### II. Maintainability

All course materials MUST be easy to maintain, update, and extend across
offerings without requiring a complete rewrite.

- **Modular Structure**: Each lab, assignment, slide deck, and dataset
  MUST be self-contained enough to be updated independently without
  cascading changes across other materials.
- **Single Source of Truth**: Key information (due dates, point values,
  policies, links) MUST be defined in exactly one canonical location.
  All other references MUST derive from or link to that source.
- **Reproducible Artifacts**: Any computational component (code examples,
  data analysis scripts, Jupyter notebooks) MUST include sufficient
  dependency and environment information to be reproduced on a clean
  machine.
- **Version-Controlled Content**: All materials MUST live in this Git
  repository. Changes MUST be committed with descriptive messages that
  explain *why* a change was made, not just what changed.
- **Term-Agnostic Defaults**: Materials SHOULD use relative references
  (e.g., "Week 3") rather than absolute dates where possible, with
  term-specific dates injected via a single configuration point (e.g.,
  the README assignments table or syllabus).

### III. Security and Privacy

No private, sensitive, or credential information may ever be committed
to this repository.

- **No Secrets in Version Control**: API keys, passwords, tokens, and
  other credentials MUST NEVER be committed to the repository, even
  temporarily. Any file containing secrets MUST be listed in `.gitignore`
  before creation. If a secret is accidentally committed, it MUST be
  rotated immediately — removing it from history alone is insufficient.
- **No Student Private Data**: Student grades, personal identifiers
  (beyond what students themselves make public), email addresses, and
  accommodation details MUST NEVER appear in this repository. Grading
  and student records MUST remain in Canvas or other institutionally
  approved systems.
- **No Instructor Private Data**: Instructor credentials, personal
  notes containing student information, and draft evaluations MUST NOT
  be committed.
- **Sensitive File Review**: Every commit MUST be reviewed (manually or
  via pre-commit hook) for accidental inclusion of files matching
  patterns: `*.env`, `*credentials*`, `*secret*`, `*grades*`, `*roster*`.

### IV. Generative AI Mindfulness

This course is offered in an era where generative AI tools can
effectively complete many traditional assignments. All materials,
expectations, and evaluations MUST account for this reality while
ensuring that students genuinely learn the expected content.

- **GenAI as Amplifier, Not Replacement**: Students MUST use generative
  AI as a tool to expand their reach and scope — e.g., accelerating
  literature searches, exploring analytical approaches, refining writing.
  GenAI MUST NOT replace the student's own critical thinking, deep
  engagement with course material, or learning.
- **Learning Is the Non-Negotiable**: The primary goal of every
  assignment is that students *learn* the underlying concepts and skills.
  If an assignment can be completed by AI alone without the student
  learning anything, that assignment MUST be redesigned. Assignments
  SHOULD be structured so that AI assistance is most useful *after* the
  student has engaged deeply with the material.
- **Transparent Expectations**: Every assignment MUST clearly state how
  generative AI may (and may not) be used for that specific task. These
  expectations MUST be concrete and specific, not vague (e.g., "You may
  use AI to help debug your analysis code, but you must write your
  interpretation of results in your own words and be prepared to explain
  your reasoning").
- **Critical Evaluation of AI Output**: Students MUST develop the skill
  of critically evaluating AI-generated content. Course materials SHOULD
  include opportunities to identify errors, biases, or shallow reasoning
  in AI outputs as part of the learning process.
- **Assessment Design for the AI Era**: Evaluations MUST assess
  understanding, not just output. This means prioritizing:
  - Process documentation (showing reasoning, not just conclusions)
  - Live explanation and defense of work (e.g., poster sessions, Q&A)
  - Iterative work products that demonstrate evolving understanding
  - Novel application and synthesis that requires genuine comprehension
  - Group collaboration dynamics that AI cannot replicate

## Course Structure and Research Pipeline

This course equips students to execute every element of a real
psychology study. All materials and assignments MUST map to this
pipeline:

### Research Pipeline Stages

1. **Study/Experiment Design** — formulating testable questions
2. **Study Implementation** — building the apparatus/instruments
3. **Data Collection** — gathering observations systematically
4. **Data Analysis** — extracting meaning from data
5. **Interpretation** — understanding what results mean
6. **Writeup/Presentation** — communicating findings to others

### First Half: Weekly Labs (Research Paper Sections)

Each lab corresponds to a section of a research paper and MUST build
the specific skills needed for that section:

1. **Introduction Lab** — How do we ask questions effectively?
2. **Methods Lab** — How can we describe our approach to other
   scientists?
3. **Results Lab** — How can we analyze and interpret our findings?
4. **Discussion Lab** — How does the work fit into the broader
   literature?

Each lab MUST:
- Connect explicitly to its corresponding research paper section
- Include hands-on exercises (not just reading/lecture)
- Build cumulatively toward the group project in the second half
- State which pipeline stages it addresses

### Second Half: Group Research Project

Student groups execute a full-scale study encompassing all six pipeline
stages. This culminates in:

- **Poster Session** — public presentation to the Dartmouth community
- **Final Research Paper** — a complete scientific article

Group project materials MUST:
- Scaffold the transition from structured labs to independent research
- Provide checkpoints that catch problems early (e.g., weekly snippets)
- Include clear rubrics for both the poster and final paper
- Ensure equitable contribution tracking (group contributions statement)

## Content Verification and Quality Assurance

To uphold Principle I (Excellent Student Experience), all content
changes MUST pass the following verification gates before release:

- **Link Validation**: Every URL in the repository MUST resolve to a
  live, correct destination. Links MUST be checked before each term
  offering.
- **Code and Instruction Testing**: Any step-by-step instructions,
  code snippets, or computational notebooks MUST be executed
  successfully on a clean environment before release.
- **Cross-Reference Consistency**: When a concept, date, point value,
  or policy is mentioned in multiple locations, all instances MUST
  agree. A search for the relevant term across the repository MUST
  return consistent results.
- **Rubric-Assignment Alignment**: Every graded deliverable MUST have
  a rubric. Every rubric criterion MUST correspond to a clearly stated
  requirement in the assignment instructions.
- **GenAI Audit**: Before each offering, assignments MUST be evaluated
  for vulnerability to AI-only completion. Any assignment that can be
  fully completed by AI without student learning MUST be redesigned per
  Principle IV.

## Governance

This constitution is the highest-authority document for the development
and maintenance of PSYC 11 course materials in this repository. All
contributions, reviews, and material updates MUST comply with these
principles.

- **Amendment Process**: Amendments require (1) a written proposal
  describing the change and its rationale, (2) review of impact on
  existing materials, and (3) an updated Sync Impact Report at the top
  of this file. Version MUST be incremented per semantic versioning:
  MAJOR for principle removals/redefinitions, MINOR for new principles
  or material expansions, PATCH for clarifications and typo fixes.
- **Compliance Review**: At the start of each new term offering, all
  materials MUST be reviewed against this constitution. Non-compliant
  materials MUST be updated before being assigned to students.
- **Conflict Resolution**: If a material change satisfies one principle
  but violates another, Principle I (Excellent Student Experience) takes
  precedence, followed by Principle IV (Generative AI Mindfulness),
  then Principle III (Security and Privacy), then Principle II
  (Maintainability).
- **Guidance File**: For runtime development guidance (day-to-day
  contribution patterns, Git workflow, etc.), consult the repository
  `CLAUDE.md` and `README.md`.

**Version**: 1.0.0 | **Ratified**: 2026-03-18 | **Last Amended**: 2026-03-18
