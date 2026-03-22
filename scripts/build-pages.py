#!/usr/bin/env python3
"""
Build course pages from markdown sources.

Converts markdown files to styled HTML pages for PSYC 11:
Laboratory in Psychological Science.
"""

import re
import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

# Emoji mapping for LaTeX \emoji{name} commands
EMOJI_MAP = {
    "birthday-cake": "\U0001F382",
    "cupcake": "\U0001F9C1",
    "party-popper": "\U0001F389",
    "tada": "\U0001F389",
    "memo": "\U0001F4DD",
    "pencil": "\u270F\uFE0F",
    "microscope": "\U0001F52C",
    "magnifying-glass-tilted-left": "\U0001F50D",
    "magnifying-glass-tilted-right": "\U0001F50E",
    "bar-chart": "\U0001F4CA",
    "chart-increasing": "\U0001F4C8",
    "chart-decreasing": "\U0001F4C9",
    "brain": "\U0001F9E0",
    "light-bulb": "\U0001F4A1",
    "books": "\U0001F4DA",
    "open-book": "\U0001F4D6",
    "clipboard": "\U0001F4CB",
    "check-mark-button": "\u2705",
    "cross-mark": "\u274C",
    "warning": "\u26A0\uFE0F",
    "star": "\u2B50",
    "rocket": "\U0001F680",
    "hammer-and-wrench": "\U0001F6E0\uFE0F",
    "gear": "\u2699\uFE0F",
    "thinking-face": "\U0001F914",
    "writing-hand": "\u270D\uFE0F",
    "raised-hand": "\u270B",
    "handshake": "\U0001F91D",
    "people": "\U0001F465",
    "person-raising-hand": "\U0001F64B",
    "calendar": "\U0001F4C5",
    "clock": "\U0001F552",
    "trophy": "\U0001F3C6",
    "target": "\U0001F3AF",
    "puzzle-piece": "\U0001F9E9",
    "test-tube": "\U0001F9EA",
    "petri-dish": "\U0001F9EB",
    "dna": "\U0001F9EC",
    "graduation-cap": "\U0001F393",
    "school": "\U0001F3EB",
    "laptop": "\U0001F4BB",
    "globe": "\U0001F30D",
    "speech-balloon": "\U0001F4AC",
    "thought-balloon": "\U0001F4AD",
    "envelope": "\u2709\uFE0F",
    "link": "\U0001F517",
    "pushpin": "\U0001F4CC",
    "round-pushpin": "\U0001F4CD",
    "scissors": "\u2702\uFE0F",
    "file-folder": "\U0001F4C1",
    "open-file-folder": "\U0001F4C2",
    "page-facing-up": "\U0001F4C4",
    "newspaper": "\U0001F4F0",
    "artist-palette": "\U0001F3A8",
    "camera": "\U0001F4F7",
    "movie-camera": "\U0001F3A5",
    "desktop-computer": "\U0001F5A5\uFE0F",
    "printer": "\U0001F5A8\uFE0F",
    "mouse": "\U0001F5B1\uFE0F",
    "speaking-head": "\U0001F5E3\uFE0F",
    "teacher": "\U0001F9D1\u200D\U0001F3EB",
    "paintbrush": "\U0001F58C\uFE0F",
    "detective": "\U0001F575\uFE0F",
    "stopwatch": "\u23F1\uFE0F",
    "luggage": "\U0001F9F3",
    "framed-picture": "\U0001F5BC\uFE0F",
    "scroll": "\U0001F4DC",
}


def convert_latex_emoji(text):
    """Convert LaTeX \\emoji{name} to Unicode emoji."""
    def replace_emoji(match):
        name = match.group(1)
        return EMOJI_MAP.get(name, f"[{name}]")
    text = re.sub(r"\\emoji\{([^}]+)\}", replace_emoji, text)
    return text


def strip_latex_preamble(text):
    """Remove YAML frontmatter and LaTeX preamble from markdown files."""
    if text.startswith("---"):
        end_match = re.search(r"\n---\s*\n", text[3:])
        if end_match:
            text = text[3 + end_match.end():]

    if "\\begin{" not in text:
        return text
    match = re.search(r"^## ", text, re.MULTILINE)
    return text[match.start():] if match else text


def convert_latex_href(text):
    """Convert LaTeX \\href{url}{text} to markdown [text](url)."""
    pattern = r"\\href\{([^}]+)\}\{([^}]+)\}"
    return re.sub(pattern, r"[\2](\1)", text)


def convert_latex_table(text):
    """Remove inline LaTeX table blocks."""
    text = re.sub(r"\\newpage\s*", "", text)
    text = re.sub(r"\\pagebreak\s*", "", text)
    text = re.sub(r"\\needspace\{[^}]*\}\s*", "", text)

    if "\\begin{tabular}" not in text:
        text = re.sub(r"\\setlength\{[^}]+\}\{[^}]+\}", "", text)
        text = re.sub(r"\\vspace\{[^}]+\}", "", text)
        text = re.sub(r"\\begin\{center\}", "", text)
        text = re.sub(r"\\end\{center\}", "", text)
        text = re.sub(r"\\textbf\{([^}]+)\}", r"**\1**", text)
        return text

    text = re.sub(r"\\setlength\{[^}]+\}\{[^}]+\}", "", text)
    text = re.sub(r"\\vspace\{[^}]+\}", "", text)
    text = re.sub(r"\\begin\{center\}", "", text)
    text = re.sub(r"\\end\{center\}", "", text)
    text = re.sub(r"\\begin\{tabular\}\{[^}]+\}", "", text)
    text = re.sub(r"\\end\{tabular\}", "", text)
    text = re.sub(r"\\hline", "", text)
    text = re.sub(r"\\textbf\{([^}]+)\}", r"**\1**", text)
    text = re.sub(r"\\\\", "", text)
    text = re.sub(r"&", " | ", text)
    return text


def slugify(text):
    """Convert text to URL-friendly slug for anchor IDs."""
    slug = text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = slug.strip("-")
    return slug


def convert_headers(html):
    """Convert markdown headers to HTML with anchor IDs."""
    def replace_header(match, tag):
        text = match.group(1)
        slug = slugify(text)
        return f'<{tag} id="{slug}">{text}</{tag}>'

    html = re.sub(
        r"^#### (.+)$", lambda m: replace_header(m, "h4"), html, flags=re.MULTILINE
    )
    html = re.sub(
        r"^### (.+)$", lambda m: replace_header(m, "h3"), html, flags=re.MULTILINE
    )
    html = re.sub(
        r"^## (.+)$", lambda m: replace_header(m, "h2"), html, flags=re.MULTILINE
    )
    html = re.sub(
        r"^# (.+)$", lambda m: replace_header(m, "h1"), html, flags=re.MULTILINE
    )
    return html


def convert_inline_formatting(html):
    """Convert bold and italic markdown to HTML."""
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)
    html = re.sub(r"(?<![\\a-zA-Z0-9])_([^_]+)_(?![a-zA-Z0-9])", r"<em>\1</em>", html)
    return html


def convert_code_blocks(text):
    """Convert fenced code blocks to HTML pre/code tags."""
    lines = text.split("\n")
    result = []
    in_code_block = False
    code_lines = []
    lang = ""

    for line in lines:
        if line.strip().startswith("```") and not in_code_block:
            in_code_block = True
            lang = line.strip()[3:].strip()
            code_lines = []
        elif line.strip() == "```" and in_code_block:
            in_code_block = False
            code_content = "\n".join(code_lines)
            code_content = (
                code_content.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            lang_class = f' class="language-{lang}"' if lang else ""
            result.append(f"<pre><code{lang_class}>{code_content}</code></pre>")
        elif in_code_block:
            code_lines.append(line)
        else:
            result.append(line)

    return "\n".join(result)


def convert_inline_code(text):
    """Convert backtick inline code to HTML code tags."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", text)


def convert_links(html):
    """Convert markdown links to HTML."""
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        is_external = (
            url.startswith("http://")
            or url.startswith("https://")
            or url.startswith("mailto:")
        )
        if is_external:
            return f'<a href="{url}" target="_blank">{text}</a>'
        else:
            return f'<a href="{url}">{text}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, html)


def convert_tables(html):
    """Convert markdown tables to HTML tables."""
    lines = html.split("\n")
    result = []
    in_table = False
    table_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(stripped)
        else:
            if in_table:
                result.append(convert_table_block(table_lines))
                in_table = False
                table_lines = []
            result.append(line)

    if in_table and table_lines:
        result.append(convert_table_block(table_lines))

    return "\n".join(result)


def convert_table_block(lines):
    """Convert a block of markdown table lines to HTML."""
    if len(lines) < 2:
        return "\n".join(lines)

    html = ["<table>"]
    for i, line in enumerate(lines):
        if re.match(r"^\|[-:\s|]+\|$", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if i == 0:
            html.append("<thead><tr>")
            for cell in cells:
                html.append(f"<th>{cell}</th>")
            html.append("</tr></thead>")
            html.append("<tbody>")
        else:
            html.append("<tr>")
            for cell in cells:
                html.append(f"<td>{cell}</td>")
            html.append("</tr>")

    html.append("</tbody>")
    html.append("</table>")
    return "\n".join(html)


def convert_lists(html):
    """Convert markdown lists to HTML with proper nesting support."""
    lines = html.split("\n")
    result = []
    stack = []

    def get_indent(line):
        return len(line) - len(line.lstrip())

    def parse_list_item(line):
        stripped = line.lstrip()
        indent = get_indent(line)

        ordered_match = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        if ordered_match:
            return indent, "ol", ordered_match.group(2)

        unordered_match = re.match(r"^[-*]\s+(.+)$", stripped)
        if unordered_match:
            return indent, "ul", unordered_match.group(1)

        return -1, "", ""

    def close_to_indent(target_indent):
        while stack and stack[-1][0] >= target_indent:
            _, list_type, has_open_li = stack.pop()
            if has_open_li:
                result.append("</li>")
            result.append(f"</{list_type}>")

    def peek_next_list_item(start_idx):
        for j in range(start_idx, len(lines)):
            if lines[j].strip():
                return parse_list_item(lines[j])
        return -1, "", ""

    i = 0
    while i < len(lines):
        line = lines[i]
        indent, list_type, content = parse_list_item(line)

        if list_type:
            next_indent, next_type, _ = peek_next_list_item(i + 1)
            has_nested = next_type and next_indent > indent

            while stack and stack[-1][0] >= indent:
                if stack[-1][0] == indent and stack[-1][1] == list_type:
                    if stack[-1][2]:
                        result.append("</li>")
                        stack[-1] = (stack[-1][0], stack[-1][1], False)
                    break
                _, old_type, old_has_li = stack.pop()
                if old_has_li:
                    result.append("</li>")
                result.append(f"</{old_type}>")

            if not stack or stack[-1][0] < indent:
                result.append(f"<{list_type}>")
                stack.append((indent, list_type, False))

            if has_nested:
                result.append(f"<li>{content}")
                stack[-1] = (stack[-1][0], stack[-1][1], True)
            else:
                result.append(f"<li>{content}</li>")

            i += 1
        else:
            if line.strip():
                close_to_indent(0)
            result.append(line)
            i += 1

    close_to_indent(0)
    return "\n".join(result)


def convert_horizontal_rules(html):
    """Convert markdown horizontal rules to HTML."""
    return re.sub(r"^---+$", "<hr>", html, flags=re.MULTILINE)


def wrap_paragraphs(html):
    """Wrap plain text blocks in paragraph tags."""
    paragraphs = re.split(r"\n\n+", html)
    formatted = []

    for p in paragraphs:
        p = p.strip()
        if not p:
            continue

        starts_with_tag = (
            p.startswith("<h")
            or p.startswith("</h")
            or p.startswith("<ul")
            or p.startswith("</ul")
            or p.startswith("<ol")
            or p.startswith("</ol")
            or p.startswith("<li")
            or p.startswith("</li")
            or p.startswith("<table")
            or p.startswith("</table")
            or p.startswith("<thead")
            or p.startswith("</thead")
            or p.startswith("<tbody")
            or p.startswith("</tbody")
            or p.startswith("<tr")
            or p.startswith("</tr")
            or p.startswith("<hr")
            or p.startswith("<div")
            or p.startswith("</div")
            or p.startswith("<p")
            or p.startswith("</p")
            or p.startswith("<input")
            or p.startswith("<pre")
        )

        contains_block_html = (
            "<ul>" in p
            or "</ul>" in p
            or "<ol>" in p
            or "</ol>" in p
            or "<li>" in p
            or "</li>" in p
            or "<table>" in p
            or "</table>" in p
        )

        if starts_with_tag or contains_block_html:
            formatted.append(p)
        else:
            formatted.append(f"<p>{p}</p>")

    return "\n".join(formatted)


def parse_markdown_to_html(markdown_text):
    """Convert markdown text to HTML."""
    html = strip_latex_preamble(markdown_text)
    html = convert_latex_emoji(html)
    html = convert_latex_href(html)
    html = convert_latex_table(html)

    html = convert_code_blocks(html)
    html = convert_headers(html)
    html = convert_inline_formatting(html)
    html = convert_inline_code(html)
    html = convert_tables(html)
    html = convert_lists(html)
    html = convert_horizontal_rules(html)
    html = convert_links(html)
    html = wrap_paragraphs(html)

    return html


# Theme toggle uses only hardcoded emoji characters (moon/sun), not user input
THEME_SCRIPT = """
    <script>
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        const htmlEl = document.documentElement;
        const currentTheme = localStorage.getItem('theme') || 'dark';
        htmlEl.setAttribute('data-theme', currentTheme);
        themeIcon.textContent = currentTheme === 'dark' ? '\\u{1F319}' : '\\u{2600}';
        themeToggle.addEventListener('click', () => {
            const current = htmlEl.getAttribute('data-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';
            htmlEl.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            themeIcon.textContent = newTheme === 'dark' ? '\\u{1F319}' : '\\u{2600}';
        });
    </script>
"""


def get_page_template(title, nav_active, content, depth=1):
    """Generate full HTML page matching the index.html theme."""
    prefix = "../" * depth

    nav_items = [
        ("Outline", f"{prefix}", nav_active == "outline"),
        ("Syllabus", f"{prefix}syllabus/", nav_active == "syllabus"),
        ("Assignments", f"{prefix}assignments/", nav_active == "assignments"),
        ("GitHub", "https://github.com/ContextLab/experimental-psychology", False),
    ]

    nav_html = ""
    for name, href, active in nav_items:
        target = ' target="_blank"' if "github.com" in href else ""
        active_class = ' class="active"' if active else ""
        nav_html += f'<a href="{href}"{active_class}{target}>{name}</a>\n            '

    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - PSYC 11</title>
    <meta name="description" content="{title} for PSYC 11: Laboratory in Psychological Science">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="{prefix}css/theme.css">
    <style>
        /* Nav — matches index.html .course-nav */
        .course-nav {{
            position: fixed; top: 0; left: 0; right: 0;
            display: flex; justify-content: space-between; align-items: center;
            padding: var(--spacing-md) var(--spacing-xl);
            background: var(--bg-color);
            border-bottom: 1px solid var(--border-color);
            z-index: var(--z-fixed);
            backdrop-filter: blur(10px);
        }}
        .course-nav .logo {{
            font-size: 1.5rem; font-weight: 700;
            background: var(--gradient-primary);
            -webkit-background-clip: text; background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .course-nav .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
        .course-nav .nav-links a {{
            color: var(--text-secondary); text-decoration: none;
            font-weight: 500; transition: color 0.3s ease;
        }}
        .course-nav .nav-links a:hover,
        .course-nav .nav-links a.active {{ color: var(--primary-color); }}
        .course-nav .theme-toggle {{
            background: var(--surface-color); border: 1px solid var(--border-color);
            border-radius: var(--radius-full); width: 40px; height: 40px;
            font-size: 1.25rem; cursor: pointer;
            display: flex; align-items: center; justify-content: center;
            transition: all var(--transition-fast);
        }}
        .course-nav .theme-toggle:hover {{
            background: var(--surface-hover); border-color: var(--primary-color);
            transform: scale(1.05);
        }}
        /* Page header */
        .page-header {{
            margin-top: 70px; padding: 3rem 2rem 2rem; text-align: center;
            background: linear-gradient(180deg, var(--surface-color) 0%, var(--bg-color) 100%);
        }}
        .page-header h1 {{
            font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; margin-bottom: 1rem;
            background: var(--gradient-primary);
            -webkit-background-clip: text; background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        /* Content area */
        .content {{ max-width: 900px; margin: 0 auto; padding: 2rem; }}
        .content h1 {{ font-size: 2rem; font-weight: 800; color: var(--text-primary); margin: 2rem 0 1rem; }}
        .content h2 {{
            font-size: 1.75rem; font-weight: 700; color: var(--text-primary);
            margin: 2rem 0 1rem; padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--border-color);
        }}
        .content h3 {{ font-size: 1.25rem; font-weight: 600; color: var(--text-primary); margin: 1.5rem 0 0.75rem; }}
        .content h4 {{ font-size: 1.1rem; font-weight: 600; color: var(--text-primary); margin: 1.25rem 0 0.5rem; }}
        .content p {{ color: var(--text-secondary); line-height: 1.8; margin-bottom: 1rem; }}
        .content ul, .content ol {{ color: var(--text-secondary); padding-left: 1.5rem; margin-bottom: 1rem; }}
        .content li {{ margin-bottom: 0.5rem; line-height: 1.6; }}
        .content a {{ color: var(--primary-color); text-decoration: none; }}
        .content a:hover {{ text-decoration: underline; }}
        .content strong {{ color: var(--text-primary); }}
        .content hr {{ border: none; border-top: 1px solid var(--border-color); margin: 2rem 0; }}
        .content table {{
            width: 100%; border-collapse: collapse; margin: 1.5rem 0;
            background: var(--surface-color); border: 1px solid var(--border-color);
            border-radius: var(--radius-lg); overflow: hidden;
        }}
        .content th {{
            background: var(--bg-color); color: var(--text-primary);
            padding: 1rem 1.5rem; text-align: left; font-weight: 600;
            font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px;
            border-bottom: 2px solid var(--border-color);
        }}
        .content td {{
            padding: 0.85rem 1.5rem; border-bottom: 1px solid var(--border-color);
            color: var(--text-secondary); font-size: 0.95rem;
        }}
        .content tr:last-child td {{ border-bottom: none; }}
        .content tr:hover td {{ background: var(--surface-hover); }}
        .content code {{
            background: var(--surface-color); padding: 0.2em 0.4em; border-radius: 4px;
            font-family: 'Fira Code', monospace; font-size: 0.9em; color: var(--primary-color);
        }}
        .content pre {{
            background: var(--surface-color); padding: 1rem; border-radius: var(--radius-md);
            overflow-x: auto; margin: 1rem 0; border: 1px solid var(--border-color);
        }}
        .content pre code {{
            background: none; padding: 0; color: var(--text-secondary);
            font-size: 0.875rem; line-height: 1.6;
        }}
        /* Footer — matches index.html */
        footer {{
            background: var(--surface-color); border-top: 1px solid var(--border-color);
            padding: 2rem; text-align: center;
        }}
        .footer-content {{ max-width: 1400px; margin: 0 auto; }}
        .footer-content p {{ color: var(--text-secondary); margin: 0.5rem 0; }}
        .footer-content a {{ color: var(--primary-color); text-decoration: none; }}
        .footer-content a:hover {{ text-decoration: underline; }}
        @media (max-width: 768px) {{
            .course-nav .nav-links {{ gap: 1rem; font-size: 0.9rem; }}
        }}
    </style>
</head>
<body>
    <nav class="course-nav">
        <div class="logo">PSYC 11</div>
        <div class="nav-links">
            {nav_html}<button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
                <span id="themeIcon"></span>
            </button>
        </div>
    </nav>

    <header class="page-header">
        <h1>{title}</h1>
    </header>

    <main class="content">
        {content}
    </main>

    <footer>
        <div class="footer-content">
            <p>&copy; 2026 <a href="https://www.context-lab.com" target="_blank">Contextual Dynamics Lab</a></p>
            <p>PSYC 11: Laboratory in Psychological Science</p>
        </div>
    </footer>

    {THEME_SCRIPT}
</body>
</html>'''


def build_syllabus():
    """Build the syllabus page from markdown."""
    source = REPO_ROOT / "admin" / "syllabus.md"
    dest = REPO_ROOT / "syllabus" / "index.html"

    if not source.exists():
        print(f"Warning: {source} not found, skipping syllabus")
        return

    markdown = source.read_text()
    content = parse_markdown_to_html(markdown)
    html = get_page_template("Course Syllabus", "syllabus", content, depth=1)

    dest.parent.mkdir(exist_ok=True)
    dest.write_text(html)
    print(f"Built: {dest}")



# Assignment ordering by course schedule (labs first in order, then assignments)
ASSIGNMENT_ORDER = [
    "birthday_lab",       # Week 1: Psychology of Everyday Life Survey Lab
    "pitch_session_lab",  # Week 2: Pitch Session Lab
    "picture_lab",        # Week 3: Picture Lab
    "data_sleuthing_lab", # Week 4: Data Sleuthing Lab
    "literature_lab",     # Week 5: Literature Review Lab
    "brainstorm",         # Week 6: Brainstorm
    "weekly_snippet",     # Ongoing: Weekly Snippets
    "make_a_poster",      # Week 9-10: Poster Presentation
    "final_paper",        # Week 9-10: Final Paper
]


def get_assignment_sort_key(name):
    """Return sort key for assignment ordering by course schedule."""
    try:
        return ASSIGNMENT_ORDER.index(name)
    except ValueError:
        return len(ASSIGNMENT_ORDER)


def prepare_markdown_for_pdf(md_file):
    """Prepare markdown for pandoc PDF generation by converting LaTeX emojis
    to Unicode and stripping the emoji package header-include."""
    text = md_file.read_text()
    # Convert \emoji{name} to Unicode
    text = convert_latex_emoji(text)
    # Remove the header-includes that loads the LaTeX emoji package
    text = re.sub(
        r"header-includes:\s*\n\s*-\s*'`\\usepackage\{emoji\}`\{=latex\}'\s*\n",
        "",
        text,
    )
    return text


def build_assignment_pdf(md_file, output_path):
    """Generate PDF from markdown using pandoc."""
    try:
        # Prepare markdown with Unicode emojis instead of LaTeX \emoji{}
        prepared_md = prepare_markdown_for_pdf(md_file)

        cmd = [
            "pandoc",
            "-f", "markdown",
            "-o", str(output_path),
            "--pdf-engine=xelatex",
            "-V", "geometry:margin=1in",
            "-V", "mainfont:Palatino",
            "-V", "fontsize:12pt",
            "-V", "colorlinks:true",
            "-V", "linkcolor:green",
        ]
        result = subprocess.run(
            cmd, input=prepared_md, capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            print(f"PDF:   {output_path}")
            return True
        else:
            print(f"PDF failed for {md_file.name}: {result.stderr[:200]}")
            return False
    except FileNotFoundError:
        print(f"Warning: pandoc not found, skipping PDF for {md_file.name}")
        return False
    except subprocess.TimeoutExpired:
        print(f"Warning: PDF generation timed out for {md_file.name}")
        return False


def build_assignment_hub():
    """Build the main assignments hub page listing all assignments and labs."""
    dest = REPO_ROOT / "assignments" / "index.html"

    assignments = []
    for md_dir in ["assignments", "labs"]:
        source_dir = REPO_ROOT / md_dir
        if not source_dir.exists():
            continue
        for md_file in sorted(source_dir.glob("*.md")):
            if md_file.name in ("README.md", "index.md"):
                continue
            text = md_file.read_text()
            title_match = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip().strip('"').strip("'")
            else:
                h1_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
                title = h1_match.group(1) if h1_match else md_file.stem.replace("_", " ").title()

            name = md_file.stem
            assignments.append((title, name, md_dir))

    # Sort by course schedule order
    assignments.sort(key=lambda x: get_assignment_sort_key(x[1]))

    hub_md = "# Assignments and Labs\n\n"
    hub_md += "All assignments for PSYC 11: Laboratory in Psychological Science.\n\n"
    hub_md += "| Assignment | HTML | PDF |\n"
    hub_md += "|---|---|---|\n"
    for title, name, source_dir in assignments:
        hub_md += f"| {title} | [View](./{name}/) | [PDF](./{name}.pdf) |\n"

    content = parse_markdown_to_html(hub_md)
    html = get_page_template("Assignments", "assignments", content, depth=1)

    dest.parent.mkdir(exist_ok=True)
    dest.write_text(html)
    print(f"Built: {dest}")


def build_individual_assignments():
    """Build individual assignment/lab pages from markdown files."""
    for md_dir in ["assignments", "labs"]:
        source_dir = REPO_ROOT / md_dir
        if not source_dir.exists():
            continue

        output_base = REPO_ROOT / "assignments"

        for md_file in sorted(source_dir.glob("*.md")):
            if md_file.name in ("README.md", "index.md"):
                continue

            name = md_file.stem
            dest_dir = output_base / name
            dest = dest_dir / "index.html"

            markdown = md_file.read_text()

            title_match = re.search(r"^title:\s*(.+)$", markdown, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip().strip('"').strip("'")
            else:
                h1_match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
                title = h1_match.group(1) if h1_match else name.replace("_", " ").title()

            content = parse_markdown_to_html(markdown)
            html = get_page_template(title, "assignments", content, depth=2)

            dest_dir.mkdir(exist_ok=True)
            dest.write_text(html)
            print(f"Built: {dest}")

            # Generate PDF
            pdf_dest = output_base / f"{name}.pdf"
            build_assignment_pdf(md_file, pdf_dest)


def main():
    """Main build function."""
    print("Building PSYC 11 course pages...")
    print("=" * 50)

    (REPO_ROOT / "syllabus").mkdir(exist_ok=True)
    (REPO_ROOT / "assignments").mkdir(exist_ok=True)

    build_syllabus()
    build_assignment_hub()
    build_individual_assignments()

    print("=" * 50)
    print("Done!")


if __name__ == "__main__":
    main()
