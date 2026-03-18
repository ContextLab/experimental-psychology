# Data Model: Course Material Overhaul

**Date**: 2026-03-18
**Feature**: 001-course-site-overhaul

## Entities

### Slide Deck

A single lecture presentation in Marp markdown format.

| Attribute | Description |
|-|-|
| filename | `lectureN.md` where N is the sequential lecture number |
| week_folder | `slides/weekN/` directory containing this deck |
| title | Lecture title (in Marp frontmatter and H1) |
| topic | Brief topic description |
| date | Scheduled class meeting date (Spring 2026) |
| theme | Always `cdl-theme` (set in YAML frontmatter) |
| figures | References to images in `slides/figs/` |
| compiled_html | Generated `lectureN.html` in same directory |
| compiled_pdf | Generated `lectureN.pdf` in same directory (optional) |

**Lifecycle**: Draft → Compiled → Verified (against original PDF) → Live

### Assignment/Lab

A student deliverable described in markdown.

| Attribute | Description |
|-|-|
| filename | `snake_case_name.md` in `assignments/` |
| title | Assignment title (in YAML frontmatter) |
| point_value | Integer points (0–40) |
| due_date | ISO date string |
| status | active, expired, or inactive |
| type | lab or assignment |
| compiled_html | Generated HTML in `assignments/name/index.html` |
| compiled_pdf | Generated PDF in `assignments/name.pdf` |

**Lifecycle**: Inactive → Active (when assigned) → Expired (past due date)

### Course Outline

The main site page listing all course meetings.

| Attribute | Description |
|-|-|
| file | `index.html` at repository root |
| weeks | Ordered list of Week entities |
| syllabus_link | Link to `syllabus/index.html` |
| assignments_link | Link to `assignments/index.html` |
| course_info | Term, meeting times, room, TAs, office hours |

### Week

A grouping of class meetings within the course outline.

| Attribute | Description |
|-|-|
| number | 1–10 |
| date_range | Start and end dates for the week |
| meetings | List of Meeting entities (MWF + optional X-hour) |
| folder | `slides/weekN/` |

### Meeting

A single class session.

| Attribute | Description |
|-|-|
| date | ISO date |
| day | M, W, F, or Th (X-hour) |
| topic | Lecture topic or activity description |
| slide_link | Link to compiled HTML presentation (if applicable) |
| is_absent | Boolean — instructor absent on this date |
| is_xhour_makeup | Boolean — X-hour used as makeup session |

### Syllabus

The formal course document.

| Attribute | Description |
|-|-|
| source | `admin/syllabus.md` |
| compiled_html | `syllabus/index.html` |
| compiled_pdf | `admin/syllabus.pdf` |

### Shared Figure

An image or SVG used across slide decks.

| Attribute | Description |
|-|-|
| filename | Descriptive name in `slides/figs/` |
| format | PNG, JPG, or SVG |
| source | Extracted from Keynote, or regenerated as SVG |
| used_by | List of slide decks referencing this figure |

## Relationships

- **Course Outline** contains 10 **Weeks**
- **Week** contains 1–4 **Meetings** (MWF + optional X-hour)
- **Meeting** links to 0–1 **Slide Decks**
- **Slide Deck** references 0–N **Shared Figures**
- **Course Outline** links to **Syllabus** and assignments index
- **Assignment/Lab** entities are listed on the assignments index page
