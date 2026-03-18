# Feature Specification: Course Material Overhaul — GitHub Pages, Marp Slides, and Automated Builds

**Feature Branch**: `001-course-site-overhaul`
**Created**: 2026-03-18
**Status**: Draft
**Input**: User description: "Comprehensive overhaul of PSYC 11 course materials: GitHub Pages site, Marp slide conversion, automated assignment builds"

## Clarifications

### Session 2026-03-18

- Q: How should slide decks be grouped into week folders? → A: Organize by calendar week (week1–week9), matching the Spring 2026 academic schedule dates. Course dates MUST be updated to the Spring 2026 academic calendar. Regular meetings are MWF 10:10–11:15 AM; X-hours are Th 12:15–1:05 PM. Instructor absences on April 1–3, April 22, and May 29 require using X-hours to make up missed content/activities on those dates.
- Q: What should happen to original Keynote (.key) and PDF (.pdf) slide files after migration? → A: Remove from repository after migration is verified complete. Keep local/external backups only.

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Student Navigates Course Site (Priority: P1)

A student visits the PSYC 11 GitHub Pages site and sees a well-organized
course outline as the main page. They can navigate to any lecture's slides
(rendered as HTML), view or download any assignment as HTML or PDF, and
access the syllabus — all from the same site without needing to clone the
repo or open raw GitHub file links.

**Why this priority**: The entire overhaul exists to improve student
access to materials. If the site doesn't work for students, nothing
else matters.

**Independent Test**: Visit the deployed GitHub Pages URL. Verify the
main page loads with a navigable course outline, all slide links open
rendered presentations, all assignment links open HTML pages with PDF
download options, and the syllabus is accessible.

**Acceptance Scenarios**:

1. **Given** the GitHub Pages site is deployed, **When** a student visits
   the site root, **Then** they see a navigable course outline with links
   to all lectures, assignments, and the syllabus.
2. **Given** the site is loaded, **When** a student clicks a lecture link,
   **Then** the Marp-rendered HTML presentation opens in the browser.
3. **Given** the site is loaded, **When** a student clicks an assignment
   link, **Then** the assignment renders as a styled HTML page with a PDF
   download link.
4. **Given** the site is loaded, **When** a student clicks the syllabus
   link, **Then** the syllabus renders as a styled HTML page with a PDF
   download link.

---

### User Story 2 — Instructor Updates a Slide Deck (Priority: P2)

The instructor edits a markdown file for a lecture presentation, commits
and pushes to the main branch. GitHub Actions automatically compiles the
markdown into an HTML presentation (and optionally PDF) using the
cdl-slides/Marp toolchain with Dartmouth theming. The updated
presentation is live on the course site without any manual build steps.

**Why this priority**: Slides are the most frequently updated content.
Removing the Keynote dependency and automating builds is the highest-value
maintainability improvement.

**Independent Test**: Edit a slide markdown file, push to main, verify
the GitHub Action runs successfully and the updated HTML presentation
appears on the site.

**Acceptance Scenarios**:

1. **Given** a slide markdown file is edited and pushed, **When** the
   GitHub Action completes, **Then** the compiled HTML presentation
   reflects the changes on the live site.
2. **Given** a new slide deck markdown file is added to the appropriate
   week folder, **When** the action runs, **Then** it is compiled and
   linked from the course outline.
3. **Given** a slide deck references images in `slides/figs/`, **When**
   compiled, **Then** images render correctly in the HTML output.

---

### User Story 3 — Instructor Updates an Assignment (Priority: P3)

The instructor edits a markdown file for an assignment or lab, commits
and pushes. GitHub Actions automatically compiles it to both HTML and
PDF. Both versions are accessible from the assignments page on the
course site.

**Why this priority**: Assignments change less frequently than slides,
but automated dual-format output (HTML + PDF) is a key maintainability
and consistency improvement over the current manual pandoc workflow.

**Independent Test**: Edit an assignment markdown file, push to main,
verify both HTML and PDF outputs are generated and accessible from the
assignments page.

**Acceptance Scenarios**:

1. **Given** an assignment markdown file is edited and pushed, **When**
   the GitHub Action completes, **Then** both HTML and PDF versions are
   updated and accessible on the site.
2. **Given** a new lab markdown file is added, **When** the action runs,
   **Then** it appears on the assignments page in both formats.
3. **Given** all existing assignments are converted to the new format,
   **When** the site is built, **Then** every assignment listed in the
   course outline has working HTML and PDF links.

---

### User Story 4 — Community Visitor Browses the Open Course (Priority: P4)

A visitor (non-enrolled student, other instructor, or community member)
finds the PSYC 11 site and can browse all public course materials
including the outline, slides, assignments, and syllabus. The site
clearly communicates the course identity and attribution.

**Why this priority**: The course is open-source and designed for
community use. A polished public-facing site increases impact, but this
is secondary to core student and instructor functionality.

**Independent Test**: Open the site URL without any authentication.
Navigate all major sections and verify content is accessible and the
site presents a cohesive, branded experience.

**Acceptance Scenarios**:

1. **Given** a visitor navigates to the site, **When** the page loads,
   **Then** they see the course title, instructor, institution branding,
   and DOI badge.
2. **Given** a visitor browses the site, **When** they click any content
   link, **Then** the content loads without requiring authentication or
   repository access.

---

### Edge Cases

- What happens when a slide markdown file has a syntax error? The build
  MUST fail visibly (not silently produce broken output) and report the
  error in the GitHub Actions log.
- What happens when an image referenced in slides is missing from
  `slides/figs/`? The build MUST report the missing reference.
- What happens when the Keynote-to-markdown migration loses content?
  Each converted slide deck MUST be manually reviewed against the
  original PDF for completeness before the migration is considered done.
- What happens when a markdown assignment uses LaTeX-specific commands
  (e.g., `\emoji{}`)? The build pipeline MUST handle or gracefully
  convert these to HTML-compatible equivalents.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The repository MUST be configured as a GitHub Pages site
  matching the style and theming of the ContextLab/llm-course site.
- **FR-002**: The site's main page MUST be a navigable course outline
  with links to all lectures, assignments, and the syllabus.
- **FR-003**: The site MUST display current course information: Spring
  2026 offering, regular meetings MWF 10:10–11:15 AM, X-hour Th
  12:15–1:05 PM, classroom Moore B03, breakout rooms Moore 302/303/150,
  TAs (Yifan Fang, Yuqi Zhang, Eunhye Choe), and instructor office
  hours link (https://context-lab.com/scheduler).
- **FR-004**: All slide decks MUST be converted from Keynote (.key)
  format to Marp-compatible markdown files using the cdl-slides theme
  (cdl-theme.css with Dartmouth branding).
- **FR-005**: Slide images from Keynote files MUST be extracted and
  saved to a shared `slides/figs/` directory accessible by all
  presentations.
- **FR-006**: Diagrams that need regeneration MUST be recreated as SVG
  files using cdl-slides theming and saved to `slides/figs/`.
- **FR-007**: A GitHub Actions workflow MUST automatically compile slide
  markdown files to HTML (and optionally PDF) on push to main.
- **FR-008**: All assignment and lab markdown files MUST be automatically
  compiled to both HTML and PDF via GitHub Actions on push to main.
- **FR-009**: The site MUST include a dedicated assignments page linking
  to HTML and PDF versions of every assignment and lab.
- **FR-010**: The syllabus MUST be rendered as HTML on the site with a
  PDF download option.
- **FR-011**: The build system MUST use the same cdl-slides compile
  toolchain (Marp CLI + process_markdown.py preprocessor + cdl-theme.css)
  used by the llm-course repository.
- **FR-012**: The site MUST include appropriate Dartmouth/CDL branding,
  course title, instructor attribution, and the existing DOI badge.
- **FR-013**: Existing content accuracy MUST be preserved — no content
  may be lost or altered during migration (verified by manual comparison
  of each converted deck against its original PDF).
- **FR-014**: The course schedule MUST be updated to the Spring 2026
  academic calendar. Instructor absences on April 1–3, April 22, and
  May 29 MUST be accounted for by scheduling X-hour makeup sessions
  (Th 12:15–1:05 PM) for any missed content or activities.
- **FR-015**: Original Keynote (.key) and PDF (.pdf) slide files MUST
  be removed from the repository after migration is verified complete.
  Local/external backups MUST be maintained before removal.

### Key Entities

- **Slide Deck**: A Marp-compatible markdown file representing one
  lecture. Has a topic, date association, and references to shared
  figures. Compiled to HTML and optionally PDF.
- **Assignment/Lab**: A markdown file describing a student deliverable.
  Has a title, point value, status, and due date. Compiled to both HTML
  and PDF.
- **Course Outline**: The site's main page. An ordered list of course
  meetings with links to slides, assignments, and resources.
- **Syllabus**: The formal course description, policies, and schedule.
  Rendered as HTML with PDF download.
- **Shared Figures**: Images and SVGs in `slides/figs/` referenced
  across multiple presentations.

### Assumptions

- The cdl-slides toolchain (Marp CLI, process_markdown.py, cdl-theme.css,
  compile.sh) will be copied into this repository's `slides/` directory
  following the same structure as llm-course, not installed as an
  external dependency.
- Keynote files contain exportable images that can be extracted manually
  (by opening in Keynote and exporting media) since there is no
  automated .key extraction in the pipeline.
- The existing pandoc-based compile scripts for assignments will be
  replaced by the new GitHub Actions pipeline, but the markdown source
  files will be preserved and adapted.
- Assignment markdown files will need their LaTeX-specific frontmatter
  (lualatex, `\emoji{}` commands) converted to HTML-compatible
  alternatives.
- The site deployment follows the same pattern as llm-course: a
  `.nojekyll` file, a custom Python build script, and the
  `actions/deploy-pages` GitHub Action.
- The CPHS presentation (currently .pptx) will remain as-is since it is
  externally authored content — it will be linked from the site but not
  converted to Marp format.
- Week-based folder organization for slides (week1–week9, matching
  llm-course convention) will replace the current flat `slides/`
  directory. Grouping follows the Spring 2026 calendar week boundaries.
- Course-specific details (term dates, room assignments, TA names) will
  be defined in a single configuration point so they can be updated for
  future offerings without editing multiple files.
- Original .key and .pdf slide files will be backed up externally before
  being removed from the repository in a dedicated cleanup commit after
  all migration verification is complete.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of existing slide content is available as
  Marp-rendered HTML presentations on the GitHub Pages site, with no
  content loss versus the original PDF exports (verified by manual
  side-by-side review).
- **SC-002**: 100% of existing assignments and labs are available on the
  site as both HTML pages and downloadable PDFs.
- **SC-003**: The course outline page links to every lecture, assignment,
  and the syllabus, with zero broken links.
- **SC-004**: A push to the main branch that modifies any slide or
  assignment markdown file triggers an automated build that updates the
  site within 5 minutes.
- **SC-005**: The site's visual presentation (colors, typography,
  branding) is consistent with the ContextLab/llm-course site's
  Dartmouth-themed appearance.
- **SC-006**: A new instructor or contributor can add a new slide deck
  or assignment by creating a single markdown file and pushing — no
  manual build steps required.
- **SC-007**: All 18 existing slide decks (excluding the externally
  authored CPHS presentation) are converted to Marp markdown with
  extracted images in `slides/figs/`.
