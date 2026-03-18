# Laboratory in Psychological Science

Course materials for [PSYC 11: Laboratory in Psychological Science](https://contextlab.github.io/experimental-psychology/) at Dartmouth College.

[![DOI](https://zenodo.org/badge/459250616.svg)](https://zenodo.org/badge/latestdoi/459250616)

## Course Website

**All course materials are available at the course website:**

**[https://contextlab.github.io/experimental-psychology/](https://contextlab.github.io/experimental-psychology/)**

The site includes the complete course outline, lecture slides, assignments, syllabus, and resources.

## About

This course teaches students how to carry out psychological research by working through each element of a real study: experiment design, implementation, data collection, analysis, interpretation, and writeup/presentation.

- **First half**: Weekly labs covering each section of a research paper (Introduction, Methods, Results, Discussion)
- **Second half**: Group research projects culminating in a poster session and final paper

## Current Offering

- **Term**: Spring 2026
- **Schedule**: MWF 10:10-11:15 AM, X-hour Th 12:15-1:05 PM
- **Location**: Moore B03
- **Instructor**: [Dr. Jeremy R. Manning](https://context-lab.com)

## Contributing

If you notice inaccuracies or have suggestions, please [open an issue](https://github.com/ContextLab/experimental-psychology/issues) or submit a [pull request](https://github.com/ContextLab/experimental-psychology/pulls). If you are a course instructor, you may use these materials in your own courses (attribution appreciated).

## Development

The site is built automatically via GitHub Actions:

- **Slide decks**: Marp markdown compiled via [cdl-slides](https://github.com/ContextLab/cdl-slides)
- **Assignments/Syllabus**: Markdown converted to HTML+PDF via `scripts/build-pages.py` and pandoc
- **Deployment**: Static site assembled and deployed to GitHub Pages

To build locally:

```bash
pip install cdl-slides
python scripts/build-pages.py          # Build assignment/syllabus HTML
./slides/compile_all_slides.sh         # Compile all slide decks
```
