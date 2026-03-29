# Tasks: Schedule Reorder and Slide Restructure

**Input**: Design documents from `/specs/003-schedule-reorder/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md

**Tests**: Not explicitly requested. Verification tasks included (compile check, link validation).

**Organization**: Tasks grouped by user story (P1-P4). US1 (file moves) must complete before US2-US4.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: US1=Slide Reorganization, US2=Course Site Update, US3=Syllabus Update, US4=Content Refactoring

---

## Phase 1: Setup

**Purpose**: Prepare directories and verify current state before moving files

- [x] T001 Create new week directories that don't exist yet: slides/week7/, slides/week8/, slides/week10/ (week8 exists from old structure but verify; week7 and week10 are new empty directories)
- [x] T002 Verify all 18 existing slide files are present and compile successfully by running slides/compile_all_slides.sh
- [x] T003 Grep all slide markdown files for image paths to confirm they all use `../figs/` pattern (no absolute or other relative paths that would break on move)

**Checkpoint**: All prerequisites verified — safe to begin file moves.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Remove compiled artifacts that would conflict with moves

**CRITICAL**: Must complete before any file moves.

- [x] T004 Delete all compiled HTML and PDF files in slides/week*/ directories (lecture*.html, lecture*.pdf) — these will be regenerated after the reorganization. Use `find slides -name "lecture*.html" -o -name "lecture*.pdf" | xargs rm -f`

**Checkpoint**: Working directory clean of compiled artifacts — file moves can proceed.

---

## Phase 3: User Story 1 — Slide Files Reorganized (Priority: P1) MVP

**Goal**: All 18 existing slide files moved to correct new locations. 3 new slide decks created. Global sequential numbering lecture1-lecture20.

**Independent Test**: `ls slides/week*/lecture*.md` shows exactly 20 files in the correct week directories with correct numbers. All compile via cdl-slides.

### Move existing files (batch git mv)

The moves must be executed carefully to avoid filename collisions. Files that stay in the same week but change number, and files that move to a different week, must be handled to avoid overwriting.

**Strategy**: Move to a temporary name first if the target path already has a file, then rename. Execute in dependency order.

- [x] T005 [US1] Move slides that change week AND keep same or get new lecture number — execute these git mv commands in order. **NOTE**: The lecture3↔lecture4 swap within week2 is intentional — old lecture4 ("Motivating your science") becomes new lecture3, and old lecture3 ("Data wrangling") becomes new lecture4. After the swap, verify by checking the `# ` title line in each file.
  - `git mv slides/week2/lecture2.md slides/week1/lecture2.md` (week2→week1)
  - `git mv slides/week2/lecture4.md slides/week2/lecture3.md.tmp` (rename within week2, temp to avoid collision with lecture3)
  - `git mv slides/week2/lecture3.md slides/week2/lecture4.md.tmp` (rename within week2, temp)
  - `git mv slides/week2/lecture3.md.tmp slides/week2/lecture3.md` (finalize — should contain "Motivating your science")
  - `git mv slides/week2/lecture4.md.tmp slides/week2/lecture4.md` (finalize — should contain "Data wrangling")
  - `git mv slides/week3/lecture5.md slides/week2/lecture5.md` (week3→week2)
  - `git mv slides/week3/lecture7.md slides/week3/lecture8.md` (renumber within week3, safe — lecture8 doesn't exist in week3)
  - `git mv slides/week4/lecture8.md slides/week4/lecture9.md.tmp` (temp rename)
  - `git mv slides/week4/lecture9.md slides/week4/lecture10.md.tmp` (temp rename)
  - `git mv slides/week4/lecture10.md slides/week4/lecture11.md` (safe — lecture11 doesn't exist)
  - `git mv slides/week4/lecture9.md.tmp slides/week4/lecture9.md` (finalize from old lecture8)
  - `git mv slides/week4/lecture10.md.tmp slides/week4/lecture10.md` (finalize from old lecture9)

- [x] T006 [US1] Move slides from week5 — renumber within same week:
  - `git mv slides/week5/lecture11.md slides/week5/lecture12.md.tmp`
  - `git mv slides/week5/lecture12.md slides/week5/lecture13.md.tmp`
  - `git mv slides/week5/lecture13.md slides/week5/lecture14.md`
  - `git mv slides/week5/lecture12.md.tmp slides/week5/lecture12.md` (finalize from old lecture11)
  - `git mv slides/week5/lecture13.md.tmp slides/week5/lecture13.md` (finalize from old lecture12)

- [x] T007 [US1] Move slides from week6 — renumber within same week:
  - `git mv slides/week6/lecture14.md slides/week6/lecture15.md.tmp`
  - `git mv slides/week6/lecture15.md slides/week6/lecture16.md.tmp`
  - `git mv slides/week6/lecture16.md slides/week6/lecture17.md`
  - `git mv slides/week6/lecture15.md.tmp slides/week6/lecture15.md` (finalize from old lecture14)
  - `git mv slides/week6/lecture16.md.tmp slides/week6/lecture16.md` (finalize from old lecture15)

- [x] T008 [US1] Move slides from week8 and week9:
  - `git mv slides/week8/lecture17.md slides/week8/lecture18.md`
  - `git mv slides/week9/lecture18.md slides/week9/lecture20.md`

- [x] T009 [US1] Verify the 18 moved files are in their new locations and no orphans remain:
  - List `slides/week*/lecture*.md` — should show exactly 18 files: week1/(1,2), week2/(3,4,5), week3/(6,8), week4/(9,10,11), week5/(12,13,14), week6/(15,16,17), week8/(18), week9/(20). (New decks lecture7, lecture19 don't exist yet — they're created in T010/T012.)
  - Verify zero orphaned .md files from old numbering remain (e.g., no old lecture5 in week3, no old lecture11 in week5, etc.).
  - Grep all moved slide files for QR code image references (`qr` pattern) and verify each referenced PNG still exists in slides/figs/.
  - Spot-check the lecture3↔lecture4 swap in week2: `head -1 slides/week2/lecture3.md` should contain "Motivating" and `head -1 slides/week2/lecture4.md` should contain "wrangling".

### Create new slide decks

- [x] T010 [P] [US1] Create slides/week3/lecture7.md — Stats refresher (~8 slides). Content: descriptive stats review (mean, SD, distributions), hypothesis testing refresher (null vs alternative, p-values), when to use t-tests vs correlations vs chi-square, interpreting effect sizes. Frame as discussion questions ("What test would you use for X?"). Use cdl-theme Marp format with callout boxes.

- [x] T011 [P] [US1] Add vibe coding tutorial section to slides/week2/lecture4.md — this file contains the old lecture3 ("Data wrangling") content after the T005 swap. Append ~5 slides for the vibe coding tutorial. Adapt from llm-course slides/week3/lecture9.md (at /Users/jmanning/llm-course/slides/week3/lecture9.md): free AI tools for students (GitHub Copilot, Gemini, Dartmouth GenAI, Google Colab AI features), the describe→design→plan→implement workflow simplified for non-CS students, practical tips for using AI to write analysis code in Colab. Update deck title to reflect combined content.

- [x] T012 [P] [US1] Create slides/week8/lecture19.md — Poster creation workshop (~10 slides). Content: anatomy of a scientific poster (title, abstract, intro, methods, results, discussion, references), visual design principles (less text, more figures, visual hierarchy), common poster mistakes to avoid, example good vs bad posters. Include a hands-on activity: groups sketch their poster layout on paper (15 min). Use cdl-theme Marp format.

- [x] T013 [US1] Compile all slide decks via slides/compile_all_slides.sh and verify all 20 decks compile without errors

**Checkpoint**: All 20 slide files in correct locations, all compile. MVP complete.

---

## Phase 4: User Story 2 — Course Site Updated (Priority: P2)

**Goal**: index.html reflects the new 10-week schedule with correct session titles, dates, slide links, and descriptions for no-slide sessions.

**Independent Test**: Every slide link on the course site resolves. Week titles and session descriptions match the new schedule. No broken links.

- [x] T014 [US2] Rewrite the week sections in index.html to match the new schedule. For each of the 10 weeks, update: week title/subtitle, session list with correct dates (Spring 2026 calendar starting 3/30), slide links pointing to correct weekN/lectureM paths, descriptions for no-slide sessions (pitch presentations, data collection, office hours, group work). Mark holidays and instructor absences clearly.

- [x] T015 [US2] Update the week pill navigation in index.html to show all 10 weeks with correct anchor links

- [x] T016 [US2] Verify all slide links in index.html by checking that each referenced file exists: grep all `slides/week` hrefs and confirm each target file is present on disk

**Checkpoint**: Course site accurately reflects the new schedule with all links working.

---

## Phase 5: User Story 3 — Syllabus Updated (Priority: P3)

**Goal**: admin/syllabus.md reflects the new week-by-week schedule with correct dates, topics, and lab timing.

**Independent Test**: Syllabus schedule matches the new schedule. All dates correct for Spring 2026.

- [x] T017 [US3] Rewrite the schedule section of admin/syllabus.md with the new 10-week plan. Each week should list: M/W/Th(X-hour)/F sessions with dates, topics, lab start/end markers, and notes for no-class days (instructor away, Memorial Day). Update any references to old lecture numbers.

- [x] T018 [US3] Rebuild the syllabus HTML and PDF by running scripts/build-pages.py — verify syllabus/index.html and admin/syllabus.pdf are generated correctly

**Checkpoint**: Syllabus matches the new schedule exactly.

---

## Phase 6: User Story 4 — Slide Content Refactored (Priority: P4)

**Goal**: All existing slide decks trimmed to 5-10 slides (max 15), focused on intuitions, questions, discussions, and breakout group prompts.

**Independent Test**: No deck exceeds 15 slides. Each deck has at least one discussion question or breakout activity. All decks compile.

### Refactor each deck (all parallelizable — different files)

- [x] T019 [P] [US4] Refactor slides/week1/lecture1.md — trim intro to ~10 slides: course overview, key questions we'll explore, survey lab intro, data collection instructions. Remove lengthy content that duplicates what's in the lab handout.

- [x] T020 [P] [US4] Refactor slides/week1/lecture2.md — trim statistical building blocks to ~10 slides focused on intuitions: what is a distribution? what does a p-value really mean? discussion question: "give an example of a hypothesis you could test." Remove detailed formula derivations.

- [x] T021 [P] [US4] Refactor slides/week2/lecture3.md — trim motivating science to ~8 slides: why does science matter? what makes a question interesting? transition to pitch lab instructions. Add discussion prompt: "What mystery would you want to solve?"

- [x] T022 [P] [US4] Refactor slides/week2/lecture5.md — trim "how far with data/stats" to ~8 slides: what can stats tell us? what can't they tell us? discussion: "give an example where data is misleading."

- [x] T023 [P] [US4] Refactor slides/week3/lecture6.md — trim effective explaining to ~8 slides: why are methods important? what makes instructions clear? transition to drawing lab. Discussion: "describe how to make a peanut butter sandwich — what did you leave out?"

- [x] T024 [P] [US4] Refactor slides/week3/lecture8.md — trim analyzing drawing lab data to ~8 slides: how to evaluate instruction quality, discussion of group results, framing for lab report.

- [x] T025 [P] [US4] Refactor slides/week4/lecture9.md — trim creating data to ~8 slides: what makes a good dataset? discussion: "what would you want to measure about X?" Transition to data sleuthing lab.

- [x] T026 [P] [US4] Refactor slides/week4/lecture10.md — trim exploring data to ~8 slides: visualization intuitions, what patterns to look for, discussion: "what does this graph tell you?"

- [x] T027 [P] [US4] Refactor slides/week4/lecture11.md — trim quick start data guide to ~8 slides: practical tips for digging into unfamiliar data, common pitfalls.

- [x] T028 [P] [US4] Refactor slides/week5/lecture12.md — trim literature search to ~8 slides: how to find papers, evaluating sources, transition to lit review lab.

- [x] T029 [P] [US4] Refactor slides/week5/lecture13.md — trim synthesizing across studies to ~8 slides: how to compare findings, discussion: "do these two papers agree or disagree?"

- [x] T030 [P] [US4] Refactor slides/week5/lecture14.md — trim logistics to ~5 slides: announcements for weeks 6-10, transition to group work time.

- [x] T031 [P] [US4] Refactor slides/week6/lecture15.md — trim getting started to ~8 slides: how to pick a topic, forming groups, brainstorming. Discussion: breakout group brainstorm activity.

- [x] T032 [P] [US4] Refactor slides/week6/lecture16.md — trim study design to ~8 slides: experimental design basics, discussion: "what's your IV/DV?"

- [x] T033 [P] [US4] Refactor slides/week6/lecture17.md — trim project management to ~8 slides: tips and tricks for implementation, add human subjects training info (CPHS, done at home over weekend).

- [x] T034 [P] [US4] Refactor slides/week8/lecture18.md — trim poster presentations intro to ~8 slides: what makes a good poster? discussion: "show me a poster — what works and what doesn't?"

- [x] T035 [P] [US4] Refactor slides/week9/lecture20.md — trim scientific writing to ~8 slides: effective writing principles, discussion: "read this paragraph — how would you improve it?"

- [x] T036 [US4] Compile all 20 slide decks after refactoring and verify all compile without errors

**Checkpoint**: All decks are 5-15 slides, discussion-focused, and compile correctly.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final verification and cleanup

- [x] T037 [P] Remove any empty/orphaned week directories or files left from the old structure
- [x] T038 [P] Rebuild all assignment HTML and PDFs via scripts/build-pages.py — verify no broken references to old slide paths
- [x] T039 Run full link validation: verify every slide link in index.html resolves to an existing file
- [x] T040 Verify the deploy pipeline works by checking .github/workflows/deploy-site.yml references are compatible with the new file structure
- [x] T041 Final end-to-end review: open index.html locally, click through every week, verify all slide links work and session descriptions are correct

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Setup
- **US1 (Phase 3)**: Depends on Foundational — BLOCKS all other user stories
- **US2 (Phase 4)**: Depends on US1 (needs correct file paths)
- **US3 (Phase 5)**: Depends on US1 (needs correct lecture numbers). Can run in PARALLEL with US2.
- **US4 (Phase 6)**: Depends on US1 (files must be in final locations). Can run in PARALLEL with US2 and US3.
- **Polish (Phase 7)**: Depends on US1, US2, US3, US4 all complete

### Within US1 (File Moves)

- T005 → T006 → T007 → T008 must be SEQUENTIAL (avoid git mv conflicts)
- T009 (verify) depends on T005-T008
- T010, T011, T012 (new decks) are PARALLEL and independent of moves
- T013 (compile) depends on T005-T012 all complete

### Parallel Opportunities After US1

- **US2 + US3 + US4** can all run in parallel once US1 is done
- Within US4: all T019-T035 are fully parallel (different files)
- T036 depends on T019-T035

---

## Implementation Strategy

### MVP First (US1 Only)

1. Complete Phase 1: Setup (verify state)
2. Complete Phase 2: Clean compiled artifacts
3. Complete Phase 3: US1 (move all files + create new decks)
4. **STOP and VALIDATE**: 20 files in correct locations, all compile
5. Can deploy with old site content if urgent

### Incremental Delivery

1. Setup + Foundational → ready to move
2. US1 → files in place (MVP!)
3. US2 + US3 + US4 in parallel → site updated, syllabus updated, content refactored
4. Polish → final verification

---

## Notes

- [P] tasks = different files, no dependencies
- File moves (T005-T008) must be sequential to avoid git mv collisions
- The vibe coding tutorial (T011) is a MERGE into an existing deck, not a standalone file
- Week 7 and Week 10 have no slides — no directories needed unless we want empty placeholders
- Existing compiled HTML/PDF in slides/ must be deleted before moves (T004) to avoid confusion
