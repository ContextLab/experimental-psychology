# Implementation Plan: Course Material Overhaul

**Branch**: `001-course-site-overhaul` | **Date**: 2026-03-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-course-site-overhaul/spec.md`

## Summary

Overhaul PSYC 11 course materials into a GitHub Pages site matching the
ContextLab/llm-course pattern. Convert 18 Keynote slide decks to Marp
markdown using the cdl-slides toolchain. Automate assignment and syllabus
HTML+PDF generation via GitHub Actions. Reorganize slides into week-based
folders aligned to the Spring 2026 Dartmouth academic calendar. Remove
original binary files after verified migration.

## Technical Context

**Language/Version**: Python 3.11 (build scripts, stdlib only), Bash (compile scripts)
**Primary Dependencies**: @marp-team/marp-cli (npm, slide compilation), pandoc (PDF generation)
**Storage**: N/A — static site, all content in Git
**Testing**: Manual link validation, visual comparison of migrated slides vs original PDFs
**Target Platform**: GitHub Pages (static HTML), modern browsers
**Project Type**: Static course website with automated build pipeline
**Performance Goals**: Site build completes in <5 minutes via GitHub Actions
**Constraints**: No external Python packages for build-pages.py (stdlib only); Marp CLI is the only npm dependency for slides
**Scale/Scope**: 18 slide decks, 8 assignments/labs, 1 syllabus, ~30 pages of site content

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status |
|-|-|-|
| I. Excellent Student Experience | All migrated content verified for accuracy against originals; all links functional; clear site navigation | PASS — SC-001 through SC-003 enforce this |
| II. Maintainability | Single-source markdown for all content; automated builds; week-based organization; term-agnostic defaults where possible | PASS — FR-001 through FR-011 enforce this |
| III. Security and Privacy | No secrets, grades, or PII in repo; .gitignore reviewed | PASS — no credentials involved in static site build |
| IV. GenAI Mindfulness | Not directly applicable to infrastructure overhaul (content unchanged) | PASS — content migration preserves existing material; genAI policy updates are a separate future feature |

**Post-Phase 1 re-check**: No violations. Infrastructure-only change does not affect course content or assessment design.

## Project Structure

### Documentation (this feature)

```text
specs/001-course-site-overhaul/
├── plan.md              # This file
├── research.md          # Phase 0: build pipeline research
├── data-model.md        # Phase 1: content entity model
├── quickstart.md        # Phase 1: contributor quickstart guide
└── tasks.md             # Phase 2: task breakdown (/speckit.tasks)
```

### Source Code (repository root)

```text
experimental-psychology/
├── .github/workflows/
│   ├── build-pages.yml          # Stage 1: markdown → HTML (Python)
│   └── deploy-site.yml          # Stage 2: assemble _site/, deploy
├── scripts/
│   └── build-pages.py           # Markdown→HTML converter (stdlib only)
├── admin/
│   ├── syllabus.md              # Syllabus source (markdown)
│   └── syllabus/                # (fonts, if needed)
├── assignments/
│   ├── birthday_lab.md
│   ├── pitch_session_lab.md
│   ├── picture_lab.md
│   ├── data_sleuthing_lab.md
│   ├── literature_lab.md
│   ├── brainstorm.md
│   ├── final_paper.md
│   ├── make_a_poster.md
│   └── weekly_snippet.md
├── slides/
│   ├── template_deck/           # Marp toolchain (from llm-course)
│   │   ├── compile.sh
│   │   ├── process_markdown.py
│   │   ├── chart-defaults.js
│   │   ├── chart-animations.js
│   │   └── themes/
│   │       └── cdl-theme.css
│   ├── compile_all_slides.sh    # Batch Marp compilation script
│   ├── figs/                    # Shared images and SVGs
│   ├── week1/                   # Mar 30
│   │   └── *.md → *.html
│   ├── week2/                   # Apr 6–10
│   ├── week3/                   # Apr 13–17
│   ├── week4/                   # Apr 20–24
│   ├── week5/                   # Apr 27 – May 1
│   ├── week6/                   # May 4–8
│   ├── week7/                   # May 11–15
│   ├── week8/                   # May 18–22
│   ├── week9/                   # May 25–29
│   └── week10/                  # Jun 1–3
├── readings/                    # Existing PDFs (Belmont Report, etc.)
├── figures/                     # Site-wide images
├── fonts/                       # Web fonts (if needed)
├── index.html                   # Main course landing page
└── .gitignore
```

**Structure Decision**: Content-type directories at root with week-based
slide subfolders, matching the llm-course convention. Existing `labs/`
content merged into `assignments/` since the build pipeline treats them
identically. The `readings/` directory is preserved as-is (static PDFs,
no conversion needed).

## Spring 2026 Schedule Mapping

Slides are organized by week. Each week folder contains the Marp markdown
files for that week's lectures. Instructor absences require X-hour makeups.

| Week | Dates (MWF) | X-hour (Th) | Notes |
|-|-|-|-|
| 1 | Mar 30 | Apr 2 ~~absent~~ | Apr 1 (W), Apr 2 (Th), Apr 3 (F) all absent — only Mon class |
| 2 | Apr 6, 8, 10 | Apr 9 | Full week; X-hour available for Week 1 makeup |
| 3 | Apr 13, 15, 17 | Apr 16 | Full week |
| 4 | Apr 20, ~~22~~, 24 | Apr 23 | Apr 22 absent — use Apr 23 X-hour for makeup |
| 5 | Apr 27, 29, May 1 | Apr 30 | Full week |
| 6 | May 4, 6, 8 | May 7 | Full week |
| 7 | May 11, 13, 15 | May 14 | Full week |
| 8 | May 18, 20, 22 | May 21 | Full week |
| 9 | ~~May 25~~, 27, ~~29~~ | May 28 | Memorial Day + absence — use May 28 X-hour for makeup |
| 10 | Jun 1, 3 | — | Last week; no X-hour (pre-exam break Jun 4) |

**Available meetings**: 22 MWF + 8 X-hours = 30 total slots
**Makeup X-hours needed**: 3 (for 5 missed MWF sessions; Week 1 loses 2
classes with no same-week X-hour — use Week 2 X-hour for one, absorb/
compress the other)

## Complexity Tracking

> No constitution violations to justify. All decisions align with principles.

## Phase 0: Research (Complete)

See [research.md](research.md) for full details. Key decisions:

1. **Build pipeline**: Two-stage GitHub Actions (build-pages.yml → deploy-site.yml)
2. **Slide toolchain**: Marp CLI + process_markdown.py + cdl-theme.css
3. **Assignment pipeline**: build-pages.py (HTML) + pandoc (PDF) in CI
4. **Directory structure**: Content-type roots with week-based slide folders
5. **File disposition**: Remove .key/.pdf after verified migration

## Phase 1: Design

### Content Model

See [data-model.md](data-model.md) for entity details.

### Key Design Decisions

**Main page (index.html)**: Custom HTML matching llm-course design.
Navigable course outline organized by week. Each week section contains:
- Date and topic
- Link to slide HTML presentation
- Link to any associated assignment/lab
- Status indicator (upcoming/current/past)

**Assignment page**: Generated by build-pages.py as `assignments/index.html`.
Lists all assignments with links to HTML and PDF versions, point values,
due dates, and status.

**Slide compilation**: Each week folder contains a `compile.sh` symlink
to `template_deck/compile.sh`. The batch script `compile_all_slides.sh`
iterates over `week*/lecture*.md` and compiles each to HTML+PDF.

**Syllabus**: Source in `admin/syllabus.md`. Build-pages.py generates
`syllabus/index.html`. Pandoc generates `admin/syllabus.pdf` in CI.

### Migration Strategy

The 18 existing slide decks map to weeks as follows (exact mapping to be
refined during implementation based on content review):

| Current file | Target |
|-|-|
| intro_and_overview | week1/lecture1.md |
| statistical_building_blocks | week1/lecture2.md |
| data_wrangling | week2/lecture3.md |
| motivating_people_about_your_science | week2/lecture4.md |
| limits_of_data | week3/lecture5.md |
| effective_explaining | week3/lecture6.md |
| evaluating_methods | week3/lecture7.md |
| data_creation | week4/lecture8.md |
| data_exploration | week4/lecture9.md |
| data_exploration_hacks | week4/lecture10.md |
| literature_reviews | week5/lecture11.md |
| synthesizing_across_studies | week5/lecture12.md |
| logistics_week_5 | week5/lecture13.md |
| final_project_initiation | week6/lecture14.md |
| experimental_design_quickstart | week6/lecture15.md |
| project_management | week6/lecture16.md |
| poster_presentations | week8/lecture17.md |
| effective_writing | week9/lecture18.md |

**Migration process per deck**:
1. Open .key file in Keynote, export all images to `slides/figs/`
2. Create Marp markdown file with cdl-theme frontmatter
3. Transcribe slide content from PDF reference into markdown
4. Replace image references with paths to `slides/figs/`
5. Recreate diagrams as SVG using cdl-theme colors where needed
6. Compile with `compile.sh` and visually compare HTML to original PDF
7. Mark as verified when instructor confirms no content loss

### Agent Context

Updated via `update-agent-context.sh claude` after plan completion.
