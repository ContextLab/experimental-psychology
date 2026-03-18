# Quickstart: Contributing to PSYC 11 Course Materials

## Prerequisites

- Git
- Node.js 20+ (for Marp CLI)
- Python 3.11+
- pandoc with lualatex (for PDF generation)

## Setup

```bash
git clone https://github.com/ContextLab/experimental-psychology.git
cd experimental-psychology

# Install Marp CLI globally
npm install -g @marp-team/marp-cli
```

## Adding or Editing a Slide Deck

1. Navigate to the appropriate week folder:
   ```bash
   cd slides/week3/
   ```

2. Create or edit a lecture markdown file:
   ```bash
   # New file uses this frontmatter:
   cat > lecture7.md << 'EOF'
   ---
   marp: true
   theme: cdl-theme
   math: katex
   transition: fade 0.25s
   author: Contextual Dynamics Lab
   ---

   # Lecture 7: Your Title Here

   ### PSYC 11: Laboratory in Psychological Science

   Jeremy R. Manning
   Dartmouth College
   Spring 2026

   ---

   # Slide content here

   EOF
   ```

3. Compile locally:
   ```bash
   ../template_deck/compile.sh lecture7.md
   # Produces lecture7.html and lecture7.pdf
   ```

4. Preview by opening `lecture7.html` in a browser.

5. Commit and push — GitHub Actions will rebuild the site.

## Adding or Editing an Assignment

1. Edit the markdown file in `assignments/`:
   ```bash
   vim assignments/my_new_lab.md
   ```

2. Use this frontmatter format:
   ```yaml
   ---
   title: "PSYC 11: My New Lab"
   author: Jeremy R. Manning
   ---
   ```

3. Commit and push — GitHub Actions generates both HTML and PDF.

## Editing the Syllabus

1. Edit `admin/syllabus.md`
2. Commit and push — both HTML and PDF are regenerated.

## Adding Images to Slides

1. Save images to `slides/figs/` with descriptive names
2. Reference in markdown: `![Description](../figs/my_image.png)`
3. For diagrams, prefer SVG format using cdl-theme colors

## Building the Full Site Locally

```bash
# Compile all slides
./slides/compile_all_slides.sh

# Build assignment/syllabus HTML
python3 scripts/build-pages.py

# Preview: open index.html in browser
```

## Key Conventions

- Slide files: `lectureN.md` (sequential numbering)
- Figures: `slides/figs/` (shared across all decks)
- Theme: always `cdl-theme` in Marp frontmatter
- Assignments use standard markdown (no LaTeX commands)
- All dates and term-specific info managed via index.html and syllabus
