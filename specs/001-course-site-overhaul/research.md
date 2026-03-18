# Research: Course Material Overhaul

**Date**: 2026-03-18
**Feature**: 001-course-site-overhaul

## Decision 1: Site Build Pipeline

**Decision**: Two-stage GitHub Actions pipeline matching llm-course.

- **Stage 1** (`build-pages.yml`): Python script converts assignment/syllabus
  markdown → HTML, auto-commits generated files back to repo.
- **Stage 2** (`deploy-demos.yml`): Copies all assets (slides, assignments,
  syllabus, figures, fonts) into `_site/`, creates `.nojekyll`, deploys to
  GitHub Pages via `actions/deploy-pages@v4`.

**Rationale**: Proven pattern already working in llm-course. Python build
script uses only stdlib (no pip dependencies). Generated HTML committed to
repo enables local viewing without build tools.

**Alternatives considered**:
- Jekyll: Rejected — llm-course explicitly bypasses Jekyll with `.nojekyll`.
  Custom Python script gives more control over LaTeX-to-HTML conversion.
- Hugo/Docusaurus: Rejected — adds dependency complexity with no benefit
  over the proven custom script.

## Decision 2: Slide Compilation Toolchain

**Decision**: Marp CLI + process_markdown.py preprocessor + cdl-theme.css,
copied from llm-course `slides/template_deck/`.

**Key dependencies**:
- `@marp-team/marp-cli` (npm, global install)
- `python3` (for process_markdown.py preprocessor)
- `pygments` (optional Python package, graceful fallback)

**Compile pipeline** (per deck):
1. `compile.sh` parses args (input file, format, theme dir)
2. `python3 process_markdown.py` preprocesses: auto-splits long code
   blocks/tables, converts flow diagrams to inline SVG, analyzes density
3. `marp-cli` renders to HTML/PDF using `cdl-theme.css`
4. JavaScript injection: chart-defaults.js, chart-animations.js

**Rationale**: Exact same toolchain as llm-course ensures visual consistency
and reuses battle-tested code. Marp markdown format is simple and maintainable.

**Alternatives considered**:
- reveal.js: More flexible but requires more HTML markup in slides. Marp's
  markdown-first approach better matches maintainability principle.
- Pandoc Beamer: Current PSYC 11 uses pandoc for assignments but not slides.
  Beamer output is PDF-only, no HTML presentations.

## Decision 3: Assignment Build Pipeline

**Decision**: Adapt llm-course `build-pages.py` to convert assignment
markdown to HTML. Add pandoc PDF generation in the GitHub Actions workflow
for dual-format output.

**Key functions from build-pages.py** (Python stdlib only):
- `strip_latex_preamble()` — removes YAML frontmatter
- `convert_latex_href()` — `\href{url}{text}` → `[text](url)`
- `convert_latex_table()` — LaTeX tabular → markdown table
- `build_individual_assignments()` — generates per-assignment HTML pages
- `build_assignment_hub()` — generates assignments index page

**Rationale**: Existing assignment markdown files use LaTeX frontmatter and
commands (`\emoji{}`, `\usepackage`). The build-pages.py script already
handles stripping these for HTML. Adding pandoc in CI provides PDF output
matching the current workflow.

**Alternatives considered**:
- Marp for assignments: Assignments are documents, not presentations. Marp's
  slide-oriented format is a poor fit.
- Pure pandoc (current approach): Produces good PDFs but no HTML. Adding
  the Python HTML converter gives both formats.

## Decision 4: Spring 2026 Schedule

**Decision**: Week-based folder organization (week1–week10) aligned to
Spring 2026 Dartmouth academic calendar.

**Term dates**:
- First day: March 30, 2026 (Monday)
- Last day: June 3, 2026 (Wednesday)
- Memorial Day (no classes): May 25
- Finals: June 5–9

**Regular meetings**: MWF 10:10–11:15 AM
**X-hours**: Th 12:15–1:05 PM

**Instructor absences**: April 1 (W), April 2 (Th), April 3 (F),
April 22 (W), May 29 (F)

**Available class meetings**: 22 of 27 MWF slots (minus 3 absences,
1 holiday, 1 absence)
**Available X-hours**: 8 of 10 Thursday slots (minus 1 absence,
1 pre-exam break)

**X-hour makeup sessions needed for**:
- April 1 (W) content → use April 2 X-hour is also absent → defer to
  next available. Since April 1–3 are all absent, Week 1 has only
  March 30 (Mon). Content from April 1 and 3 must be rescheduled to
  X-hours in weeks 2+ or absorbed into remaining Week 1/2 meetings.
- April 22 (W) content → use April 23 (Th) X-hour
- May 29 (F) content → use May 28 (Th) X-hour

## Decision 5: Directory Structure

**Decision**: Flat content-type directories at root (matching llm-course
pattern), with week-based subfolders for slides.

```text
experimental-psychology/
├── .github/workflows/
│   ├── build-pages.yml         # Python: md→HTML for syllabus/assignments
│   └── deploy-site.yml         # Copy to _site/, deploy to GitHub Pages
├── scripts/
│   └── build-pages.py          # Markdown→HTML converter (stdlib only)
├── admin/
│   └── syllabus.md             # Course syllabus source
├── assignments/                # Labs and assignments (markdown source)
│   ├── birthday_lab.md
│   ├── pitch_session_lab.md
│   ├── picture_lab.md
│   ├── data_sleuthing_lab.md
│   ├── literature_lab.md
│   ├── final_paper.md
│   ├── make_a_poster.md
│   └── weekly_snippet.md
├── labs/                       # Keep separate from assignments if needed
├── slides/
│   ├── template_deck/          # Marp toolchain (copied from llm-course)
│   │   ├── compile.sh
│   │   ├── process_markdown.py
│   │   ├── chart-defaults.js
│   │   ├── chart-animations.js
│   │   └── themes/
│   │       └── cdl-theme.css
│   ├── figs/                   # Shared images and SVGs
│   ├── week1/                  # March 30
│   ├── week2/                  # April 6–10
│   │   └── *.md → *.html
│   ├── ...
│   └── week10/                 # June 1–3
├── figures/                    # Site-wide images (logo, DOI badge, etc.)
├── fonts/                      # Web fonts
├── readings/                   # Existing PDFs (Belmont Report, etc.)
├── index.html                  # Main course landing page
└── .gitignore
```

## Decision 6: Original File Disposition

**Decision**: Remove original .key and .pdf slide files from repository
after migration is verified. Maintain local/external backups before
removal.

**Rationale**: Binary files bloat the repo. PDFs serve as verification
reference during migration but are replaced by Marp HTML+PDF output.
Keynote files are the source being replaced by markdown.

**Process**: Backup → verify all 18 decks migrated → single cleanup
commit removing .key/.pdf files.
