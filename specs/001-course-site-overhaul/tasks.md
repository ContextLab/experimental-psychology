# Tasks: Course Material Overhaul — GitHub Pages, Marp Slides, Automated Builds

**Input**: Design documents from `/specs/001-course-site-overhaul/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md

**Tests**: Not explicitly requested. Manual verification tasks included
where visual comparison or link checking is required.

**Organization**: Tasks grouped by user story (P1–P4) with shared
infrastructure in Setup and Foundational phases.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: US1=Student Navigation, US2=Slide Updates, US3=Assignment Updates, US4=Public Site

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize project structure, toolchain, and build pipeline scaffolding

- [x] T001 Install cdl-slides via pip (replaced manual toolchain copy — added requirements.txt with cdl-slides>=1.2.0)
- [x] T002 [P] Create slides/figs/ directory for shared images and SVGs
- [x] T003 [P] Create week-based slide directories: slides/week1/ through slides/week10/
- [x] T004 [P] Create scripts/ directory and copy build-pages.py from llm-course to scripts/build-pages.py
- [x] T005 [P] Create .gitignore entries for _site/, *.key backup artifacts, and node_modules/
- [x] T006 [P] .nojekyll created dynamically by deploy workflow (no placeholder needed)
- [x] T007 Write compile_all_slides.sh in slides/ — uses cdl-slides compile command

**Checkpoint**: Toolchain installed, directory structure in place, batch compile script ready

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: GitHub Actions workflows and build-pages.py adaptation — MUST complete before any user story content is meaningful on the live site

**CRITICAL**: No user story work produces a visible site until these are done

- [x] T008 Adapt scripts/build-pages.py for PSYC 11: updated branding, nav, emoji conversion, assignment/lab scanning
- [x] T009 Adapt scripts/build-pages.py to also generate syllabus/index.html from admin/syllabus.md
- [x] T010 [P] Create .github/workflows/build-pages.yml — Python 3.11, build-pages.py, auto-commit
- [x] T011 [P] Create .github/workflows/deploy-site.yml — cdl-slides, compile slides, assemble _site/, deploy
- [x] T012 [P] Add pandoc PDF generation step to build-pages.yml for assignments
- [x] T013 [P] Add pandoc PDF generation step to build-pages.yml for syllabus
- [ ] T014 Verify GitHub Actions workflows run successfully on a test push (create a trivial change, push, confirm both workflows complete without error)

**Checkpoint**: Push any markdown change → site auto-builds and deploys. All downstream work is just adding content.

---

## Phase 3: User Story 1 — Student Navigates Course Site (Priority: P1) MVP

**Goal**: Students visit the GitHub Pages site and find a navigable course outline linking to all lectures, assignments, and the syllabus.

**Independent Test**: Visit deployed site URL → main page shows course outline → all section links work → slides open as HTML presentations → assignments render as HTML with PDF download → syllabus is accessible.

### Implementation for User Story 1

- [ ] T015 [US1] Create index.html at repository root — main course landing page with Dartmouth/CDL branding, course title ("Laboratory in Psychological Science — PSYC 11"), instructor name, DOI badge, Spring 2026 info (MWF 10:10–11:15 AM, X-hour Th 12:15–1:05 PM, Moore B03, breakout rooms 302/303/150), TAs (Yifan Fang, Yuqi Zhang, Eunhye Choe), office hours link (https://context-lab.com/scheduler). Match llm-course visual style (dark mode, Dartmouth colors, navigation bar).
- [ ] T016 [US1] Build navigable course outline section in index.html — week-by-week schedule for Spring 2026 with dates, topics, and links to slide HTML files. Mark instructor absence dates and X-hour makeup sessions. Include links to assignments page and syllabus.
- [ ] T017 [P] [US1] Convert admin/syllabus/PSYC_11_EXPERIMENTAL_PSYCHOLOGY.PDF content into admin/syllabus.md (markdown with YAML frontmatter matching llm-course format)
- [ ] T018 [P] [US1] Convert assignments/birthday_lab.md — strip LaTeX frontmatter, replace \emoji{} with HTML emoji, ensure clean markdown for build-pages.py processing
- [ ] T019 [P] [US1] Convert assignments/pitch_session_lab.md — same LaTeX→markdown cleanup
- [ ] T020 [P] [US1] Convert assignments/picture_lab.md — same LaTeX→markdown cleanup
- [ ] T021 [P] [US1] Convert assignments/data_sleuthing_lab.md — same LaTeX→markdown cleanup
- [ ] T022 [P] [US1] Convert assignments/literature_lab.md — same LaTeX→markdown cleanup
- [ ] T023 [P] [US1] Convert assignments/final_paper.md — same LaTeX→markdown cleanup
- [ ] T024 [P] [US1] Convert assignments/make_a_poster.md — same LaTeX→markdown cleanup
- [ ] T025 [P] [US1] Convert assignments/weekly_snippet.md — same LaTeX→markdown cleanup
- [ ] T026 [P] [US1] Convert assignments/brainstorm.md — same LaTeX→markdown cleanup (if it has LaTeX frontmatter)
- [ ] T027 [US1] Verify all assignment HTML and PDF links work on deployed site — check assignments/index.html lists every assignment with working HTML and PDF download links
- [ ] T028 [US1] Verify syllabus renders correctly as HTML at syllabus/index.html with PDF download link
- [ ] T029 [US1] Verify course outline in index.html has zero broken links (all slide placeholders, assignment links, syllabus link)

**Checkpoint**: Site is live with full course outline, all assignments in HTML+PDF, and syllabus. Slide links may point to placeholder/empty pages until US2 is complete.

---

## Phase 4: User Story 2 — Instructor Updates Slides (Priority: P2)

**Goal**: All 18 Keynote slide decks converted to Marp markdown. Editing a markdown file and pushing auto-compiles and deploys updated HTML presentations.

**Independent Test**: Edit a slide markdown file → push → GitHub Action compiles → updated HTML appears on site → visual comparison matches original PDF.

### Implementation for User Story 2

#### Week 1 (Mar 30)

- [ ] T030 [P] [US2] Open slides/intro_and_overview.key in Keynote, export all images to slides/figs/ with descriptive names (e.g., intro_overview_fig1.png)
- [ ] T031 [P] [US2] Open slides/statistical_building_blocks.key in Keynote, export all images to slides/figs/
- [ ] T032 [US2] Create slides/week1/lecture1.md (intro_and_overview) — Marp frontmatter with cdl-theme, transcribe content from PDF, reference images from ../figs/
- [ ] T033 [US2] Create slides/week1/lecture2.md (statistical_building_blocks) — same process

#### Week 2 (Apr 6–10)

- [ ] T034 [P] [US2] Export images from slides/data_wrangling.key to slides/figs/
- [ ] T035 [P] [US2] Export images from slides/motivating_people_about_your_science.key to slides/figs/
- [ ] T036 [US2] Create slides/week2/lecture3.md (data_wrangling)
- [ ] T037 [US2] Create slides/week2/lecture4.md (motivating_people_about_your_science)

#### Week 3 (Apr 13–17)

- [ ] T038 [P] [US2] Export images from slides/limits_of_data.key to slides/figs/
- [ ] T039 [P] [US2] Export images from slides/effective_explaining.key to slides/figs/
- [ ] T040 [P] [US2] Export images from slides/evaluating_methods.key to slides/figs/
- [ ] T041 [US2] Create slides/week3/lecture5.md (limits_of_data)
- [ ] T042 [US2] Create slides/week3/lecture6.md (effective_explaining)
- [ ] T043 [US2] Create slides/week3/lecture7.md (evaluating_methods)

#### Week 4 (Apr 20–24)

- [ ] T044 [P] [US2] Export images from slides/data_creation.key to slides/figs/
- [ ] T045 [P] [US2] Export images from slides/data_exploration.key to slides/figs/
- [ ] T046 [P] [US2] Export images from slides/data_exploration_hacks.key to slides/figs/
- [ ] T047 [US2] Create slides/week4/lecture8.md (data_creation)
- [ ] T048 [US2] Create slides/week4/lecture9.md (data_exploration)
- [ ] T049 [US2] Create slides/week4/lecture10.md (data_exploration_hacks)

#### Week 5 (Apr 27 – May 1)

- [ ] T050 [P] [US2] Export images from slides/literature_reviews.key to slides/figs/
- [ ] T051 [P] [US2] Export images from slides/synthesizing_across_studies.key to slides/figs/
- [ ] T052 [P] [US2] Export images from slides/logistics_week_5.key to slides/figs/
- [ ] T053 [US2] Create slides/week5/lecture11.md (literature_reviews)
- [ ] T054 [US2] Create slides/week5/lecture12.md (synthesizing_across_studies)
- [ ] T055 [US2] Create slides/week5/lecture13.md (logistics_week_5)

#### Week 6 (May 4–8)

- [ ] T056 [P] [US2] Export images from slides/final_project_initiation.key to slides/figs/
- [ ] T057 [P] [US2] Export images from slides/experimental_design_quickstart.key to slides/figs/
- [ ] T058 [P] [US2] Export images from slides/project_management.key to slides/figs/
- [ ] T059 [US2] Create slides/week6/lecture14.md (final_project_initiation)
- [ ] T060 [US2] Create slides/week6/lecture15.md (experimental_design_quickstart)
- [ ] T061 [US2] Create slides/week6/lecture16.md (project_management)

#### Week 8 (May 18–22)

- [ ] T062 [P] [US2] Export images from slides/poster_presentations.key to slides/figs/
- [ ] T063 [US2] Create slides/week8/lecture17.md (poster_presentations)

#### Week 9 (May 25–29)

- [ ] T064 [P] [US2] Export images from slides/effective_writing.key to slides/figs/
- [ ] T065 [US2] Create slides/week9/lecture18.md (effective_writing)

#### CPHS Presentation (externally authored)

- [ ] T066 [US2] Link CPHS presentation (.pptx and .pdf) from course outline — no Marp conversion, link directly to existing files in slides/

#### Verification

- [ ] T067 [US2] Compile all slide decks locally using slides/compile_all_slides.sh — verify all 18 compile without errors
- [ ] T068 [US2] Visually compare each compiled HTML presentation against its original PDF export — flag any content loss or rendering issues
- [ ] T069 [US2] Recreate any diagrams that did not export cleanly from Keynote as SVG files in slides/figs/ using cdl-theme colors
- [ ] T070 [US2] Push all slide markdown files and verify GitHub Actions compiles and deploys them to the live site
- [ ] T071 [US2] Update course outline links in index.html to point to compiled slide HTML files for all 18 lectures

**Checkpoint**: All 18 slide decks live as Marp HTML presentations on the site. Instructor can edit any slide markdown and push to auto-deploy.

---

## Phase 5: User Story 3 — Instructor Updates Assignments (Priority: P3)

**Goal**: Editing an assignment markdown file and pushing auto-generates both HTML and PDF. Both formats accessible from the assignments page.

**Independent Test**: Edit an assignment markdown → push → both HTML and PDF update on site → assignments page links work for both formats.

### Implementation for User Story 3

- [ ] T072 [US3] Verify all 9 assignment markdown files compile to HTML via build-pages.py without errors (should work from Phase 2, but verify after Phase 3 LaTeX cleanup)
- [ ] T073 [US3] Verify all 9 assignment markdown files compile to PDF via pandoc in GitHub Actions without errors
- [ ] T074 [US3] Verify assignments/index.html page lists all assignments with correct point values, due dates, status, and working links to both HTML and PDF
- [ ] T075 [US3] Test the full edit→push→deploy cycle: make a trivial edit to one assignment markdown file, push, verify both HTML and PDF update on the live site

**Checkpoint**: Full assignment pipeline working end-to-end. Instructor edits markdown, pushes, both formats auto-deploy.

---

## Phase 6: User Story 4 — Community Visitor Browses Site (Priority: P4)

**Goal**: Public-facing site is polished with branding, DOI badge, attribution, and all content accessible without authentication.

**Independent Test**: Open site in incognito browser → all content loads → branding is consistent → no login prompts.

### Implementation for User Story 4

- [ ] T076 [US4] Add Dartmouth/CDL visual branding to index.html — colors (#00693e green, #267aba river blue, #ffa00f bonfire orange), typography (Cormorant Garamond, Fira Code), logo if available
- [ ] T077 [P] [US4] Add DOI badge (Zenodo) to index.html matching existing README badge
- [ ] T078 [P] [US4] Add course attribution footer to index.html — instructor name, department, Creative Commons license note, link to GitHub repo
- [ ] T079 [P] [US4] Copy necessary font files to fonts/ directory (if using custom web fonts; otherwise rely on Google Fonts CDN references in CSS)
- [ ] T080 [US4] Verify GitHub Pages is configured to serve from the correct source (Settings → Pages → GitHub Actions artifact deployment)
- [ ] T081 [US4] Navigate all site sections in incognito mode — verify no authentication required, all content renders, consistent styling throughout

**Checkpoint**: Polished, branded, public-facing course site fully functional.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Cleanup, final verification, and file removal

- [ ] T082 [P] Update README.md to reference the GitHub Pages site URL instead of inline content (keep as a pointer to the live site)
- [ ] T083 [P] Remove old compile.sh scripts from labs/ and assignments/ (replaced by GitHub Actions pipeline)
- [ ] T084 [P] Remove generated .pdf files from labs/ and assignments/ (now generated by CI)
- [ ] T085 Back up all original .key and .pdf slide files externally (local backup or cloud storage — confirm with instructor before proceeding)
- [ ] T086 Remove all .key and .pdf files from slides/ directory in a single cleanup commit (per FR-015, after migration verified in T068)
- [ ] T087 Run full link validation across the deployed site — verify zero broken links (SC-003)
- [ ] T088 Verify site build completes within 5 minutes on GitHub Actions (SC-004)
- [ ] T089 Final visual consistency check — compare site appearance against llm-course for Dartmouth theme consistency (SC-005)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **US1 (Phase 3)**: Depends on Foundational — creates the site structure and converts assignments
- **US2 (Phase 4)**: Depends on Foundational — can run in PARALLEL with US1 (slides are independent content)
- **US3 (Phase 5)**: Depends on US1 completion (assignment conversion) and Foundational
- **US4 (Phase 6)**: Depends on US1 (site exists) — can overlap with US2
- **Polish (Phase 7)**: Depends on US1, US2, US3, and US4 all complete

### Parallel Opportunities

- **Phase 1**: T002, T003, T004, T005, T006 all parallel (independent directories/files)
- **Phase 2**: T010, T011, T012, T013 all parallel (independent workflow files)
- **Phase 3 (US1)**: T017–T026 all parallel (independent assignment conversions)
- **Phase 4 (US2)**: All image export tasks within a week are parallel; across weeks, export tasks are parallel. Markdown creation within a week is sequential (after its export tasks).
- **Phase 7**: T082, T083, T084 all parallel

### User Story Independence

- **US1** and **US2** are fully independent — can be developed in parallel by different contributors
- **US3** depends on US1 (assignments must be converted first)
- **US4** depends on US1 (site must exist), light dependency on US2 (links to slides)

---

## Implementation Strategy

### MVP First (US1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (GitHub Actions pipelines)
3. Complete Phase 3: US1 (site + assignments + syllabus)
4. **STOP and VALIDATE**: Site is live with course outline and all assignments
5. Deploy/demo — students can access assignments immediately

### Incremental Delivery

1. Setup + Foundational → pipeline working
2. US1 → site live with assignments (MVP!)
3. US2 → slides migrated → full course content online
4. US3 → verify end-to-end assignment pipeline
5. US4 → polish branding and public presentation
6. Polish → cleanup old files, final validation

### Parallel Team Strategy

With two contributors:
- **Contributor A**: US1 (site + assignments)
- **Contributor B**: US2 (slide conversion — this is the bulk of the work)
- After both complete: US3 verification, US4 polish, cleanup

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Slide conversion (US2) is the largest phase by far (18 decks × ~30 min each)
- Image export tasks (T030–T064 even numbers) require Keynote.app — must be done on macOS
- The LaTeX→markdown cleanup for assignments (T018–T026) is repetitive but each file is independent
- Commit after each week's worth of slide conversions for incremental progress
- Stop at any checkpoint to validate independently
