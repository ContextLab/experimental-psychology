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
    "robot": "\U0001F916",
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


def convert_blockquotes(html):
    """Convert markdown blockquotes (> ...) to styled HTML blockquotes."""
    lines = html.split("\n")
    result = []
    in_blockquote = False
    bq_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("> "):
            content = stripped[2:]
            bq_lines.append(content)
            if not in_blockquote:
                in_blockquote = True
        elif stripped == ">" and in_blockquote:
            bq_lines.append("")
        else:
            if in_blockquote:
                bq_content = "\n".join(bq_lines)
                result.append(f'<blockquote class="reflection-callout">{bq_content}</blockquote>')
                bq_lines = []
                in_blockquote = False
            result.append(line)

    if in_blockquote:
        bq_content = "\n".join(bq_lines)
        result.append(f'<blockquote class="reflection-callout">{bq_content}</blockquote>')

    return "\n".join(result)


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
            or p.startswith("<blockquote")
            or p.startswith("</blockquote")
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


_MATH_PLACEHOLDER = "\x00MATH{0}\x00"


def extract_math(text):
    """Pull inline ($...$) and display ($$...$$) LaTeX math out of the text
    so that subsequent markdown/HTML transforms don't mangle them. Returns
    (text_with_placeholders, list_of_math_strings).

    \\$ is treated as a literal dollar sign and not as a math delimiter.
    """
    math_segments = []

    # Temporarily protect escaped dollars
    text = text.replace(r"\$", "\x01ESCDOLLAR\x01")

    # Display math: $$...$$
    def repl_display(m):
        math_segments.append(("display", m.group(1)))
        return _MATH_PLACEHOLDER.format(len(math_segments) - 1)

    text = re.sub(r"\$\$(.+?)\$\$", repl_display, text, flags=re.DOTALL)

    # Inline math: $...$ (no newline inside)
    def repl_inline(m):
        math_segments.append(("inline", m.group(1)))
        return _MATH_PLACEHOLDER.format(len(math_segments) - 1)

    text = re.sub(r"\$([^\$\n]+?)\$", repl_inline, text)

    return text, math_segments


def restore_math(html, math_segments):
    """Put extracted math back as KaTeX-renderable spans."""
    for i, (kind, content) in enumerate(math_segments):
        # Escape HTML special chars in math content (KaTeX will handle LaTeX itself)
        escaped = (
            content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        if kind == "display":
            replacement = f'<span class="math-display">\\[{escaped}\\]</span>'
        else:
            replacement = f'<span class="math-inline">\\({escaped}\\)</span>'
        html = html.replace(_MATH_PLACEHOLDER.format(i), replacement)
    # Restore escaped dollars as literal $
    html = html.replace("\x01ESCDOLLAR\x01", "$")
    return html


def parse_markdown_to_html(markdown_text):
    """Convert markdown text to HTML."""
    html = strip_latex_preamble(markdown_text)
    html = convert_latex_emoji(html)
    html = convert_latex_href(html)
    html = convert_latex_table(html)

    # Extract LaTeX math before any other transforms touch it
    html, math_segments = extract_math(html)

    html = convert_code_blocks(html)
    html = convert_headers(html)
    html = convert_inline_formatting(html)
    html = convert_inline_code(html)
    html = convert_tables(html)
    html = convert_blockquotes(html)
    html = convert_lists(html)
    html = convert_horizontal_rules(html)
    html = convert_links(html)
    html = wrap_paragraphs(html)

    # Restore math as KaTeX-renderable spans
    html = restore_math(html, math_segments)

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
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '\\\\[', right: '\\\\]', display: true}}, {{left: '\\\\(', right: '\\\\)', display: false}}], throwOnError: false}});"></script>
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
        .content {{ max-width: 900px; margin: 0 auto; padding: 2rem; color: var(--text-secondary); line-height: 1.8; }}
        .content blockquote.reflection-callout {{
            background: var(--surface-color);
            border-left: 4px solid var(--primary-color);
            padding: 1rem 1.25rem;
            margin: 1.5rem 0;
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            color: var(--text-secondary);
            line-height: 1.7;
        }}
        .content blockquote.reflection-callout strong {{
            color: var(--primary-color);
        }}
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


def parse_outline_frontmatter(text):
    """Parse YAML frontmatter from outline.md using regex (stdlib only).

    Returns a dict with: title, code, term, instructor, teaching_assistants,
    rooms, links, resources, assignments, start_date, end_date.
    """
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not fm_match:
        return {}
    fm = fm_match.group(1)
    data = {}

    # Simple scalar fields
    for key in ("title", "code", "term", "institution", "start_date", "end_date"):
        m = re.search(rf"^{key}:\s*(.+)$", fm, re.MULTILINE)
        if m:
            data[key] = m.group(1).strip().strip('"').strip("'")

    # Instructor
    m_instr = re.search(r"^instructor:\s*\n((?:\s+.+\n)*)", fm, re.MULTILINE)
    if m_instr:
        instr_block = m_instr.group(1)
        name_m = re.search(r"name:\s*(.+)", instr_block)
        oh_m = re.search(r"office_hours_url:\s*(.+)", instr_block)
        data["instructor"] = {
            "name": name_m.group(1).strip() if name_m else "",
            "office_hours_url": oh_m.group(1).strip() if oh_m else "",
        }

    # Teaching assistants (list of objects with name+email, or plain names)
    m_ta = re.search(r"^teaching_assistants:\s*\n((?:\s+[-\s].+\n)*)", fm, re.MULTILINE)
    if m_ta:
        ta_block = m_ta.group(1)
        ta_list = []
        current_ta = {}
        for line in ta_block.strip().split("\n"):
            line = line.strip()
            if line.startswith("- name:"):
                if current_ta:
                    ta_list.append(current_ta)
                current_ta = {"name": line.split(":", 1)[1].strip()}
            elif line.startswith("email:"):
                current_ta["email"] = line.split(":", 1)[1].strip()
            elif line.startswith("- ") and "name:" not in line:
                # Simple format: just a name
                ta_list.append({"name": line[2:].strip()})
        if current_ta:
            ta_list.append(current_ta)
        data["teaching_assistants"] = ta_list

    # Rooms
    m_rooms = re.search(r"^rooms:\s*\n((?:\s+.+\n)*)", fm, re.MULTILINE)
    if m_rooms:
        rooms_block = m_rooms.group(1)
        main_m = re.search(r"main:\s*(.+)", rooms_block)
        breakout_m = re.search(r"breakout:\s*(.+)", rooms_block)
        data["rooms"] = {
            "main": main_m.group(1).strip() if main_m else "",
            "breakout": breakout_m.group(1).strip() if breakout_m else "",
        }

    # Links
    m_links = re.search(r"^links:\s*\n((?:\s+.+\n)*)", fm, re.MULTILINE)
    if m_links:
        links_block = m_links.group(1)
        data["links"] = {}
        for lm in re.finditer(r"(\w+):\s*(.+)", links_block):
            data["links"][lm.group(1).strip()] = lm.group(2).strip()

    # Resources (list of sections with items)
    m_res = re.search(r"^resources:\s*\n((?:\s+.+\n)*)", fm, re.MULTILINE)
    if m_res:
        res_block = m_res.group(1)
        data["resources"] = []
        # Split on section markers
        sections = re.split(r"  - section:", res_block)
        for sec in sections:
            if not sec.strip():
                continue
            lines = sec.strip().split("\n")
            section_name = lines[0].strip().strip('"').strip("'")
            icon_m = re.search(r"icon:\s*(.+)", sec)
            icon = icon_m.group(1).strip() if icon_m else ""
            items = []
            item_blocks = re.split(r"      - label:", sec)
            for ib in item_blocks[1:]:
                label_val = ib.strip().split("\n")[0].strip().strip('"').strip("'")
                url_m = re.search(r"url:\s*(.+)", ib)
                icon_i_m = re.search(r"icon:\s*(.+)", ib)
                ext_m = re.search(r"external:\s*(.+)", ib)
                items.append({
                    "label": label_val,
                    "url": url_m.group(1).strip() if url_m else "",
                    "icon": icon_i_m.group(1).strip() if icon_i_m else "",
                    "external": ext_m.group(1).strip().lower() == "true" if ext_m else False,
                })
            data["resources"].append({
                "section": section_name,
                "icon": icon,
                "items": items,
            })

    # Assignments (list of dicts)
    m_asgn = re.search(r"^assignments:\s*\n((?:\s+.+\n)*)", fm, re.MULTILINE)
    if m_asgn:
        asgn_block = m_asgn.group(1)
        data["assignments"] = []
        entries = re.split(r"  - name:", asgn_block)
        for entry in entries:
            if not entry.strip():
                continue
            name_val = entry.strip().split("\n")[0].strip().strip('"').strip("'")
            url_m = re.search(r"url:\s*(.+)", entry)
            pts_m = re.search(r"points:\s*(.+)", entry)
            due_m = re.search(r"due:\s*(.+)", entry)
            data["assignments"].append({
                "name": name_val,
                "url": url_m.group(1).strip() if url_m else "",
                "points": int(pts_m.group(1).strip()) if pts_m else 0,
                "due": due_m.group(1).strip().strip('"').strip("'") if due_m else "",
            })

    return data


def parse_outline_weeks(text):
    """Parse the body of outline.md into week structures.

    Returns list of dicts: {number, title, date_range, sessions: [{day, date, title, slides, assignment, xhour, absent, holiday}]}
    """
    # Get body after frontmatter
    fm_match = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    body = text[fm_match.end():] if fm_match else text

    # Split into week blocks by --- separator
    week_blocks = re.split(r"\n---\s*\n", body)
    weeks = []

    for block in week_blocks:
        block = block.strip()
        if not block:
            continue

        # Parse week header: # Week N: Title
        week_m = re.match(r"^#\s+Week\s+(\d+):\s*(.+)$", block, re.MULTILINE)
        if not week_m:
            continue

        week_num = int(week_m.group(1))
        week_title = week_m.group(2).strip()

        # Parse date range: ## Date Range
        date_m = re.search(r"^##\s+(.+)$", block, re.MULTILINE)
        date_range = date_m.group(1).strip() if date_m else ""

        # Parse sessions: ### Day Date: Title
        sessions = []
        session_blocks = re.split(r"(?=^### )", block, flags=re.MULTILINE)
        for sb in session_blocks:
            sess_m = re.match(r"^###\s+(\w+)\s+(\w+\s+\d+):\s*(.+)$", sb, re.MULTILINE)
            if not sess_m:
                continue
            day = sess_m.group(1)
            date = sess_m.group(2)
            title = sess_m.group(3).strip()

            slides = ""
            assignment = ""
            xhour = False
            absent = False
            holiday = False

            pdf = ""

            slides_m = re.search(r"^-\s+slides:\s*(.+)$", sb, re.MULTILINE)
            if slides_m:
                slides = slides_m.group(1).strip()

            pdf_m = re.search(r"^-\s+pdf:\s*(.+)$", sb, re.MULTILINE)
            if pdf_m:
                pdf = pdf_m.group(1).strip()

            asgn_m = re.search(r"^-\s+assignment:\s*(.+)$", sb, re.MULTILINE)
            if asgn_m:
                assignment = asgn_m.group(1).strip()

            if re.search(r"^-\s+xhour:\s*true", sb, re.MULTILINE):
                xhour = True
            if re.search(r"^-\s+absent:\s*true", sb, re.MULTILINE):
                absent = True
            if re.search(r"^-\s+holiday:\s*true", sb, re.MULTILINE):
                holiday = True

            sessions.append({
                "day": day,
                "date": date,
                "title": title,
                "slides": slides,
                "pdf": pdf,
                "assignment": assignment,
                "xhour": xhour,
                "absent": absent,
                "holiday": holiday,
            })

        weeks.append({
            "number": week_num,
            "title": week_title,
            "date_range": date_range,
            "sessions": sessions,
        })

    return weeks


def build_outline_page():
    """Build the main index.html course outline page from outline.md."""
    source = REPO_ROOT / "outline.md"
    dest = REPO_ROOT / "index.html"

    if not source.exists():
        print(f"Warning: {source} not found, skipping outline page")
        return

    text = source.read_text()
    fm = parse_outline_frontmatter(text)
    weeks = parse_outline_weeks(text)

    # Build COURSE_WEEK_STARTS JS object from week date ranges
    week_starts_js = ""
    for w in weeks:
        # Parse start date from date range like "Mar 30 -- Apr 3"
        # or from session dates
        if w["sessions"]:
            first_date = w["sessions"][0]["date"]  # e.g. "Mar 30"
            # Determine year from course start_date
            start_year = fm.get("start_date", "2026-03-30")[:4]
            month_str, day_str = first_date.split()
            months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                       "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                       "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
            month_num = months.get(month_str, "01")
            iso_date = f"{start_year}-{month_num}-{day_str.zfill(2)}"
            week_starts_js += f"            {w['number']}: new Date('{iso_date}'),\n"

    # Compute COURSE_END from end_date
    course_end = fm.get("end_date", "2026-06-05")
    # Add one day to end_date for the COURSE_END sentinel
    # Simple: just use the end_date + 1 day
    end_parts = course_end.split("-")
    end_day = int(end_parts[2]) + 1
    course_end_js = f"{end_parts[0]}-{end_parts[1]}-{str(end_day).zfill(2)}"

    num_weeks = len(weeks)

    # Build week pills HTML
    week_pills_html = ""
    for w in weeks:
        week_pills_html += f'            <a href="#week{w["number"]}" class="week-pill">Week {w["number"]}</a>\n'

    # Build week sections HTML
    weeks_html = ""
    for w in weeks:
        # Format date range for subtitle: "Mar 30 -- Apr 3" -> "Mar 30&ndash;Apr 3"
        subtitle = w["date_range"].replace(" -- ", "&ndash;").replace("--", "&ndash;")

        # Build session cards
        cards_html = ""
        for sess in w["sessions"]:
            # Day span classes
            day_classes = ["lecture-day"]
            if sess["holiday"]:
                day_classes.append("holiday")
            elif sess["absent"]:
                day_classes.append("absent")
            if sess["xhour"]:
                day_classes.append("xhour")

            day_class_str = " ".join(day_classes)

            # Day label
            day_label = f'{sess["day"]} {sess["date"]}'
            if sess["xhour"]:
                day_label += " (X)"

            # Title classes
            title_classes = ["lecture-title"]
            if sess["holiday"]:
                title_classes.append("holiday")
            elif sess["absent"]:
                title_classes.append("absent")
            title_class_str = " ".join(title_classes)

            # Resource section
            resource_html = ""
            if sess["slides"] or sess["assignment"]:
                resource_html = '\n                    <div class="resource-section">'
                if sess["slides"]:
                    pdf_link = ""
                    if sess.get("pdf"):
                        pdf_link = (
                            f'\n                            <a href="{sess["pdf"]}" class="resource-link">'
                            '<span class="icon"><i class="fa-solid fa-file-pdf"></i></span> PDF</a>'
                        )
                    resource_html += (
                        '\n                        <div class="resource-group">'
                        '<div class="resource-label">Slides</div>'
                        '<div class="resource-links">'
                        f'\n                            <a href="{sess["slides"]}" class="resource-link primary">'
                        '<span class="icon"><i class="fa-solid fa-globe"></i></span> HTML</a>'
                        f'{pdf_link}'
                        '\n                        </div></div>'
                    )
                if sess["assignment"]:
                    # Parse "Name | url" format
                    if "|" in sess["assignment"]:
                        parts = sess["assignment"].split("|", 1)
                        asgn_name = parts[0].strip()
                        asgn_url = parts[1].strip()
                    else:
                        asgn_name = sess["assignment"]
                        asgn_url = "#"
                    resource_html += (
                        '\n                        <div class="resource-group">'
                        '<div class="resource-label">Assignment</div>'
                        '<div class="resource-links">'
                        f'\n                            <a href="{asgn_url}" class="resource-link">'
                        f'<span class="icon"><i class="fa-solid fa-flask"></i></span> {asgn_name}</a>'
                        '\n                        </div></div>'
                    )
                resource_html += "\n                    </div>"

            cards_html += f"""
                <div class="lecture-card">
                    <div class="lecture-header">
                        <span class="{day_class_str}">{day_label}</span>
                    </div>
                    <h3 class="{title_class_str}">{sess["title"]}</h3>{resource_html}
                </div>"""

        weeks_html += f"""
        <!-- Week {w["number"]} -->
        <section class="week-section" id="week{w["number"]}">
            <div class="week-header" onclick="toggleWeek(this)">
                <div class="week-header-content">
                    <span class="week-number">Week {w["number"]}</span>
                    <h2 class="week-title">{w["title"]}</h2>
                    <p class="week-subtitle">{subtitle}</p>
                </div>
                <span class="expand-icon"><i class="fa-solid fa-chevron-down"></i></span>
            </div>
            <div class="week-content">{cards_html}
            </div>
        </section>
"""

    # Build info cards
    instructor = fm.get("instructor", {})
    tas = fm.get("teaching_assistants", [])
    rooms = fm.get("rooms", {})
    links = fm.get("links", {})

    tas_html = ""
    for ta in tas:
        if isinstance(ta, dict):
            name = ta.get("name", "")
            email = ta.get("email", "")
            if email:
                tas_html += f'                <p><a href="mailto:{email}">{name}</a></p>\n'
            else:
                tas_html += f"                <p>{name}</p>\n"
        else:
            tas_html += f"                <p>{ta}</p>\n"

    # Build assignments table rows
    assignments = fm.get("assignments", [])
    asgn_rows = ""
    for a in assignments:
        asgn_rows += f"""                <tr>
                    <td><a href="{a["url"]}">{a["name"]}</a></td>
                    <td>{a["points"]} pts</td>
                    <td>{a["due"]}</td>
                </tr>
"""

    # Build resources section
    resources = fm.get("resources", [])
    resources_cards_html = ""
    for rsec in resources:
        items_html = ""
        for item in rsec["items"]:
            target = ' target="_blank"' if item.get("external") else ""
            items_html += f'                    <li><a href="{item["url"]}"{target}><i class="{item["icon"]}"></i> {item["label"]}</a></li>\n'
        resources_cards_html += f"""            <div class="resource-card">
                <h3><i class="{rsec["icon"]}"></i> {rsec["section"]}</h3>
                <ul>
{items_html}                </ul>
            </div>
"""

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{fm.get("title", "Laboratory in Psychological Science")} - {fm.get("code", "PSYC 11")}</title>
    <meta name="description" content="Course materials for {fm.get("code", "PSYC 11")}: {fm.get("title", "Laboratory in Psychological Science")} - {fm.get("institution", "Dartmouth College")}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '\\\\[', right: '\\\\]', display: true}}, {{left: '\\\\(', right: '\\\\)', display: false}}], throwOnError: false}});"></script>
    <link rel="stylesheet" href="./css/theme.css">

    <style>
        /* Navigation - matching demos page style */
        .course-nav {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: var(--spacing-md) var(--spacing-xl);
            background: var(--bg-color);
            border-bottom: 1px solid var(--border-color);
            z-index: var(--z-fixed);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }}

        .course-nav.scrolled {{
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}

        .course-nav .logo {{
            font-size: 1.5rem;
            font-weight: 700;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .course-nav .nav-links {{
            display: flex;
            gap: 2rem;
            align-items: center;
        }}

        .course-nav .nav-links a {{
            color: var(--text-secondary);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }}

        .course-nav .nav-links a:hover,
        .course-nav .nav-links a.active {{
            color: var(--primary-color);
        }}

        .course-nav .theme-toggle {{
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-full);
            width: 40px;
            height: 40px;
            font-size: 1.25rem;
            cursor: pointer;
            transition: all var(--transition-fast);
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .course-nav .theme-toggle:hover {{
            background: var(--surface-hover);
            border-color: var(--primary-color);
            transform: scale(1.05);
        }}

        /* Hero Section */
        .hero {{
            margin-top: 70px;
            padding: 3rem 2rem 2rem;
            text-align: center;
            background: linear-gradient(180deg, var(--surface-color) 0%, var(--bg-color) 100%);
        }}

        .hero h1 {{
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 800;
            margin-bottom: 1rem;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: fadeInUp 0.8s ease;
        }}

        .hero p {{
            font-size: clamp(1rem, 2vw, 1.25rem);
            color: var(--text-secondary);
            max-width: 700px;
            margin: 0 auto 1.5rem;
            animation: fadeInUp 0.8s ease 0.2s both;
        }}

        .course-meta {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
            animation: fadeInUp 0.8s ease 0.3s both;
        }}

        .meta-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.95rem;
        }}

        .meta-item .icon {{
            font-size: 1.2rem;
        }}

        /* DOI Badge */
        .doi-badge {{
            margin-top: 1.5rem;
            animation: fadeInUp 0.8s ease 0.4s both;
        }}

        /* Course Info Section */
        .course-info {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 1.5rem 2rem 0;
            animation: fadeInUp 0.8s ease 0.5s both;
        }}

        .course-info-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }}

        .info-card {{
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.25rem;
        }}

        .info-card h4 {{
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-muted);
            margin-bottom: 0.75rem;
        }}

        .info-card p, .info-card a {{
            font-size: 0.95rem;
            margin-bottom: 0.25rem;
        }}

        .info-card a {{
            color: var(--primary-color);
            text-decoration: none;
        }}

        .info-card a:hover {{
            text-decoration: underline;
        }}

        /* Quick Links Bar */
        .quick-links {{
            background: var(--surface-color);
            border-bottom: 1px solid var(--border-color);
            padding: 1rem 2rem;
            position: sticky;
            top: 60px;
            z-index: 100;
        }}

        .quick-links-container {{
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}

        .week-pill {{
            background: var(--bg-color);
            color: var(--text-secondary);
            padding: 0.5rem 1rem;
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 500;
            cursor: pointer;
            border: 1px solid var(--border-color);
            transition: all var(--transition-base);
            text-decoration: none;
        }}

        .week-pill:hover {{
            border-color: var(--primary-color);
            color: var(--primary-color);
        }}

        .week-pill.active {{
            background: var(--gradient-primary);
            color: white;
            border-color: transparent;
        }}

        /* Main Content */
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}

        /* Week Section */
        .week-section {{
            margin-bottom: 2rem;
            scroll-margin-top: 140px;
        }}

        .week-header {{
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1.5rem 2rem;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .week-header:hover {{
            border-color: var(--primary-color);
            background: var(--surface-hover);
        }}

        .week-header.expanded {{
            border-bottom-left-radius: 0;
            border-bottom-right-radius: 0;
            border-bottom-color: transparent;
        }}

        .week-header-content {{
            flex: 1;
        }}

        .week-number {{
            display: inline-block;
            background: var(--gradient-primary);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}

        .week-title {{
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }}

        .week-subtitle {{
            color: var(--text-secondary);
            font-size: 0.95rem;
        }}

        .expand-icon {{
            font-size: 1.5rem;
            color: var(--text-secondary);
            transition: transform 0.3s ease;
        }}

        .week-header.expanded .expand-icon {{
            transform: rotate(180deg);
        }}

        .week-content {{
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-top: none;
            border-bottom-left-radius: var(--radius-lg);
            border-bottom-right-radius: var(--radius-lg);
            padding: 0;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s ease, padding 0.3s ease;
        }}

        .week-content.expanded {{
            max-height: 5000px;
            padding: 1.5rem 2rem;
        }}

        /* Lecture Card */
        .lecture-card {{
            background: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }}

        .lecture-card:last-child {{
            margin-bottom: 0;
        }}

        .lecture-card:hover {{
            border-color: var(--primary-color);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        .lecture-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .lecture-day {{
            background: var(--surface-hover);
            color: var(--primary-color);
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-sm);
            font-size: 0.85rem;
            font-weight: 600;
        }}

        .lecture-day.xhour {{
            background: rgba(139, 92, 246, 0.2);
            color: #a78bfa;
        }}

        .lecture-day.absent {{
            background: rgba(251, 191, 36, 0.15);
            color: #fbbf24;
            font-style: italic;
        }}

        .lecture-day.holiday {{
            background: rgba(251, 191, 36, 0.15);
            color: #fbbf24;
            font-style: italic;
        }}

        .lecture-title {{
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.75rem;
        }}

        .lecture-title.absent {{
            color: var(--text-muted);
            font-style: italic;
        }}

        .lecture-title.holiday {{
            color: var(--text-muted);
            font-style: italic;
        }}

        /* Resource Links */
        .resource-section {{
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border-color);
        }}

        .resource-group {{
            margin-bottom: 0.75rem;
        }}

        .resource-label {{
            font-size: 0.8rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }}

        .resource-links {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .resource-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.4rem 0.75rem;
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-sm);
            color: var(--text-primary);
            text-decoration: none;
            font-size: 0.85rem;
            transition: all 0.2s ease;
        }}

        .resource-link:hover {{
            border-color: var(--primary-color);
            color: var(--primary-color);
            transform: translateY(-2px);
        }}

        .resource-link.primary {{
            background: var(--gradient-primary);
            color: white;
            border-color: transparent;
        }}

        .resource-link.primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
            color: white;
        }}

        .resource-link .icon {{
            font-size: 1rem;
        }}

        /* No Class Notice */
        .no-class-notice {{
            background: rgba(251, 191, 36, 0.1);
            border: 1px solid rgba(251, 191, 36, 0.3);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            text-align: center;
            color: #fbbf24;
            margin-bottom: 1rem;
        }}

        .no-class-notice h4 {{
            margin-bottom: 0.5rem;
            font-size: 1.1rem;
        }}

        .no-class-notice p {{
            opacity: 0.8;
            font-size: 0.9rem;
        }}

        /* Assignments Table */
        .assignments-section {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem 2rem;
        }}

        .assignments-section h2 {{
            font-size: 1.75rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .assignments-table {{
            width: 100%;
            border-collapse: collapse;
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            overflow: hidden;
        }}

        .assignments-table th {{
            background: var(--bg-color);
            color: var(--text-primary);
            padding: 1rem 1.5rem;
            text-align: left;
            font-weight: 600;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 2px solid var(--border-color);
        }}

        .assignments-table td {{
            padding: 0.85rem 1.5rem;
            border-bottom: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.95rem;
        }}

        .assignments-table tr:last-child td {{
            border-bottom: none;
        }}

        .assignments-table tr:hover td {{
            background: var(--surface-hover);
        }}

        .assignments-table a {{
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 500;
        }}

        .assignments-table a:hover {{
            text-decoration: underline;
        }}

        /* Resources Section */
        .resources-section {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem 3rem;
        }}

        .resources-section h2 {{
            font-size: 1.75rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .resources-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }}

        .resource-card {{
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            transition: all 0.3s ease;
        }}

        .resource-card:hover {{
            border-color: var(--primary-color);
        }}

        .resource-card h3 {{
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }}

        .resource-card ul {{
            list-style: none;
            padding: 0;
        }}

        .resource-card li {{
            margin-bottom: 0.5rem;
        }}

        .resource-card li a {{
            color: var(--primary-color);
            text-decoration: none;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .resource-card li a:hover {{
            text-decoration: underline;
        }}

        /* Footer */
        footer {{
            background: var(--surface-color);
            border-top: 1px solid var(--border-color);
            padding: 2rem;
            text-align: center;
        }}

        .footer-content {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        .footer-content p {{
            color: var(--text-secondary);
            margin: 0.5rem 0;
        }}

        .footer-content a {{
            color: var(--primary-color);
            text-decoration: none;
        }}

        .footer-content a:hover {{
            text-decoration: underline;
        }}

        /* Animations */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .course-nav .nav-links {{
                gap: 1rem;
            }}

            .course-meta {{
                flex-direction: column;
                gap: 0.75rem;
            }}

            .quick-links {{
                padding: 0.75rem 1rem;
            }}

            .week-pill {{
                padding: 0.4rem 0.8rem;
                font-size: 0.8rem;
            }}

            .week-header {{
                padding: 1rem 1.5rem;
            }}

            .week-title {{
                font-size: 1.25rem;
            }}

            .lecture-header {{
                flex-direction: column;
            }}

            .course-info-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}

            .assignments-table {{
                font-size: 0.85rem;
            }}

            .assignments-table th,
            .assignments-table td {{
                padding: 0.65rem 1rem;
            }}
        }}
    </style>
</head>
<body>
    <nav class="course-nav" id="navbar">
        <div class="logo">{fm.get("code", "PSYC 11")}</div>
        <div class="nav-links">
            <a href="./" class="active">Outline</a>
            <a href="./syllabus/">Syllabus</a>
            <a href="./assignments/">Assignments</a>
            <a href="https://github.com/ContextLab/experimental-psychology" target="_blank">GitHub</a>
            <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
                <span id="themeIcon"></span>
            </button>
        </div>
    </nav>

    <section class="hero">
        <h1>{fm.get("title", "Laboratory in Psychological Science")}</h1>
        <p>{fm.get("code", "PSYC 11")} &mdash; {fm.get("institution", "Dartmouth College")}</p>
        <div class="course-meta">
            <div class="meta-item">
                <span class="icon"><i class="fa-regular fa-calendar"></i></span>
                <span>MWF 10:10-11:15 AM</span>
            </div>
            <div class="meta-item">
                <span class="icon"><i class="fa-solid fa-book"></i></span>
                <span>X-Hour: Thu 12:15-1:05 PM</span>
            </div>
            <div class="meta-item">
                <span class="icon"><i class="fa-solid fa-graduation-cap"></i></span>
                <span>{fm.get("term", "Spring 2026")}</span>
            </div>
            <div class="meta-item">
                <span class="icon"><i class="fa-solid fa-location-dot"></i></span>
                <span>{rooms.get("main", "TBD")}</span>
            </div>
        </div>
        <div class="doi-badge">
            <a href="https://zenodo.org/badge/latestdoi/459250616" target="_blank"><img src="https://zenodo.org/badge/459250616.svg" alt="DOI"></a>
        </div>
    </section>

    <div class="course-info">
        <div class="course-info-grid">
            <div class="info-card">
                <h4>Instructor</h4>
                <p><strong>{instructor.get("name", "")}</strong></p>
                <p><a href="{instructor.get("office_hours_url", "#")}" target="_blank"><i class="fa-regular fa-calendar-check"></i> Office Hours</a></p>
            </div>
            <div class="info-card">
                <h4>Teaching Assistants</h4>
{tas_html}            </div>
            <div class="info-card">
                <h4>Rooms</h4>
                <p><strong>Main:</strong> {rooms.get("main", "TBD")}</p>
                <p><strong>Breakout:</strong> {rooms.get("breakout", "TBD")}</p>
            </div>
            <div class="info-card">
                <h4>Quick Links</h4>
                <p><a href="{links.get("syllabus", "./syllabus/")}"><i class="fa-solid fa-file-lines"></i> Syllabus</a></p>
                <p><a href="{links.get("assignments", "./assignments/")}"><i class="fa-solid fa-clipboard-list"></i> Assignments</a></p>
                <p><a href="{links.get("canvas", "#")}" target="_blank"><i class="fa-solid fa-chalkboard"></i> Canvas</a></p>
                <p><a href="{links.get("slack", "#")}" target="_blank"><i class="fa-brands fa-slack"></i> Slack</a></p>
                <p><a href="{links.get("github", "#")}" target="_blank"><i class="fa-brands fa-github"></i> GitHub</a></p>
            </div>
        </div>
    </div>

    <div class="quick-links">
        <div class="quick-links-container" id="quick-links-container">
{week_pills_html}        </div>
    </div>

    <main class="container" id="weeks-container">
{weeks_html}
    </main>

    <!-- Assignments -->
    <section class="assignments-section">
        <h2>Assignments</h2>
        <table class="assignments-table">
            <thead>
                <tr>
                    <th>Assignment</th>
                    <th>Points</th>
                    <th>Due Date</th>
                </tr>
            </thead>
            <tbody>
{asgn_rows}            </tbody>
        </table>
    </section>

    <!-- Resources -->
    <section class="resources-section">
        <h2>Resources</h2>
        <div class="resources-grid">
{resources_cards_html}        </div>
    </section>

    <footer>
        <div class="footer-content">
            <p>&copy; 2026 <a href="https://www.context-lab.com" target="_blank">Contextual Dynamics Lab</a></p>
            <p>{fm.get("code", "PSYC 11")}: {fm.get("title", "Laboratory in Psychological Science")}</p>
        </div>
    </footer>

    <script>
        // ============================================
        // COURSE WEEK DATES - {fm.get("term", "Spring 2026")}
        // ============================================
        var COURSE_WEEK_STARTS = {{
{week_starts_js}        }};
        var COURSE_END = new Date('{course_end_js}');

        function getCurrentWeek() {{
            var now = new Date();
            if (now < COURSE_WEEK_STARTS[1]) return 1;
            if (now >= COURSE_END) return {num_weeks};
            for (var week = {num_weeks}; week >= 1; week--) {{
                if (now >= COURSE_WEEK_STARTS[week]) return week;
            }}
            return 1;
        }}

        // ============================================
        // ACCORDION TOGGLE
        // ============================================
        function toggleWeek(header) {{
            var content = header.nextElementSibling;
            var isExpanded = header.classList.contains('expanded');
            if (isExpanded) {{
                header.classList.remove('expanded');
                content.classList.remove('expanded');
            }} else {{
                header.classList.add('expanded');
                content.classList.add('expanded');
            }}
        }}

        // ============================================
        // WEEK PILL NAVIGATION
        // ============================================
        function setupQuickLinks() {{
            document.querySelectorAll('.week-pill').forEach(function(pill) {{
                pill.addEventListener('click', function(e) {{
                    e.preventDefault();
                    var targetId = pill.getAttribute('href').substring(1);
                    var targetSection = document.getElementById(targetId);
                    if (targetSection) {{
                        var header = targetSection.querySelector('.week-header');
                        var content = targetSection.querySelector('.week-content');
                        if (header && !header.classList.contains('expanded')) {{
                            header.classList.add('expanded');
                            content.classList.add('expanded');
                        }}
                        targetSection.scrollIntoView({{ behavior: 'smooth' }});
                    }}
                }});
            }});
        }}

        // ============================================
        // SCROLL SPY - ACTIVE WEEK PILL
        // ============================================
        function updateActiveWeek() {{
            var weekPills = document.querySelectorAll('.week-pill');
            var weekSections = document.querySelectorAll('.week-section');
            var scrollPos = window.scrollY + 200;

            weekSections.forEach(function(section, index) {{
                var top = section.offsetTop;
                var bottom = top + section.offsetHeight;
                if (scrollPos >= top && scrollPos < bottom) {{
                    weekPills.forEach(function(pill) {{ pill.classList.remove('active'); }});
                    if (weekPills[index]) weekPills[index].classList.add('active');
                }}
            }});
        }}

        // ============================================
        // FADE-IN ANIMATIONS
        // ============================================
        function setupAnimations() {{
            var observerOptions = {{ threshold: 0.1 }};
            var observer = new IntersectionObserver(function(entries) {{
                entries.forEach(function(entry) {{
                    if (entry.isIntersecting) {{
                        entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
                        observer.unobserve(entry.target);
                    }}
                }});
            }}, observerOptions);

            document.querySelectorAll('.week-section').forEach(function(section) {{
                section.style.opacity = '0';
                observer.observe(section);
            }});
        }}

        // ============================================
        // THEME TOGGLE
        // ============================================
        var themeToggle = document.getElementById('themeToggle');
        var themeIcon = document.getElementById('themeIcon');
        var htmlEl = document.documentElement;

        var currentTheme = localStorage.getItem('theme') || 'dark';
        htmlEl.setAttribute('data-theme', currentTheme);
        themeIcon.textContent = currentTheme === 'dark' ? '\\uD83C\\uDF19' : '\\u2600\\uFE0F';

        themeToggle.addEventListener('click', function() {{
            var current = htmlEl.getAttribute('data-theme');
            var newTheme = current === 'dark' ? 'light' : 'dark';
            htmlEl.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            themeIcon.textContent = newTheme === 'dark' ? '\\uD83C\\uDF19' : '\\u2600\\uFE0F';
        }});

        // ============================================
        // NAVBAR SCROLL EFFECT
        // ============================================
        var navbar = document.getElementById('navbar');
        window.addEventListener('scroll', function() {{
            if (window.pageYOffset > 50) {{
                navbar.classList.add('scrolled');
            }} else {{
                navbar.classList.remove('scrolled');
            }}
            updateActiveWeek();
        }});

        // ============================================
        // AUTO-EXPAND CURRENT WEEK
        // ============================================
        function autoExpandCurrentWeek() {{
            var currentWeekNum = getCurrentWeek();
            var weekId = 'week' + currentWeekNum;
            var section = document.getElementById(weekId);
            if (section) {{
                var header = section.querySelector('.week-header');
                var content = section.querySelector('.week-content');
                if (header && content) {{
                    header.classList.add('expanded');
                    content.classList.add('expanded');
                }}
            }}
            // Highlight the corresponding pill
            var pills = document.querySelectorAll('.week-pill');
            if (pills[currentWeekNum - 1]) {{
                pills[currentWeekNum - 1].classList.add('active');
            }}
        }}

        // ============================================
        // INITIALIZE
        // ============================================
        setupQuickLinks();
        setupAnimations();
        autoExpandCurrentWeek();
    </script>
</body>
</html>'''

    dest.write_text(html)
    print(f"Built: {dest}")


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
    "survey_lab",         # Week 1: Psychology of Everyday Life Survey Lab
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
    """Prepare markdown for pandoc PDF generation.

    Converts \\emoji{name} to Unicode characters, strips variant selectors
    and ZWJ sequences (which break lualatex), and removes the LaTeX emoji
    package header-include.
    """
    text = md_file.read_text()
    text = convert_latex_emoji(text)
    # Strip Unicode variant selectors (U+FE0F) and ZWJ (U+200D) sequences
    # that lualatex cannot handle — the base emoji still renders via the
    # Apple Color Emoji fallback font
    text = text.replace("\uFE0F", "").replace("\u200D", "")
    text = re.sub(
        r"header-includes:\s*\n\s*-\s*'`\\usepackage\{emoji\}`\{=latex\}'\s*\n",
        "",
        text,
    )
    # Strip mainfont: from YAML frontmatter — the build script sets the font
    # via a preamble, and Palatino isn't installed on the Linux runner.
    # Letting it through would override our preamble and break PDF generation.
    text = re.sub(r"^mainfont:\s*.+\n", "", text, flags=re.MULTILINE)
    return text


def build_assignment_pdf(md_file, output_path):
    """Generate PDF from markdown using pandoc + lualatex.

    Uses lualatex with Unicode emoji characters (converted from LaTeX
    \\emoji{} commands) and Apple Color Emoji as a fallback font for
    emoji rendering on macOS.
    """
    try:
        import tempfile
        prepared_md = prepare_markdown_for_pdf(md_file)

        # Write LaTeX preamble that sets up emoji font fallback
        # Use Apple Color Emoji on macOS, Noto Color Emoji on Linux
        import platform
        if platform.system() == "Darwin":
            emoji_font = "Apple Color Emoji"
            main_font = "Palatino"
        else:
            emoji_font = "Noto Color Emoji"
            main_font = "TeX Gyre Pagella"  # Palatino-equivalent on Linux
        preamble = (
            f"\\directlua{{luaotfload.add_fallback(\"emojifallback\","
            f"{{\"{emoji_font}:mode=harf;\"}})"
            f"}}\n"
            f"\\setmainfont{{{main_font}}}[RawFeature={{fallback=emojifallback}}]\n"
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".tex", delete=False) as pf:
            pf.write(preamble)
            preamble_path = pf.name

        cmd = [
            "pandoc",
            "-f", "markdown",
            "-o", str(output_path),
            "--pdf-engine=lualatex",
            "-V", "geometry:margin=1in",
            "-V", "fontsize:12pt",
            "-V", "colorlinks:true",
            "-V", "linkcolor:green",
            "-H", preamble_path,
        ]

        result = subprocess.run(
            cmd, input=prepared_md, capture_output=True, text=True, timeout=120
        )
        os.unlink(preamble_path)
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


def build_individual_assignments(changed_files=None):
    """Build individual assignment/lab pages from markdown files.

    Args:
        changed_files: If provided, a set of file paths. Only generate PDFs
            for files in this set. HTML is always rebuilt (fast). If None,
            rebuild everything.
    """
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

            # Generate PDF only if file changed (or no filter specified)
            rel_path = str(md_file.relative_to(REPO_ROOT))
            if changed_files is not None and rel_path not in changed_files:
                print(f"Skip PDF (unchanged): {name}")
                continue

            pdf_dest = output_base / f"{name}.pdf"
            build_assignment_pdf(md_file, pdf_dest)


def main():
    """Main build function.

    Supports --changed flag to only generate PDFs for specified files.
    HTML pages are always rebuilt (fast). PDFs are only rebuilt for
    changed files (slow — lualatex takes ~10s per file).
    """
    import sys

    # Parse --changed flag: list of changed .md file paths
    changed_files = None
    if "--changed" in sys.argv:
        idx = sys.argv.index("--changed")
        if idx + 1 < len(sys.argv):
            changed_arg = sys.argv[idx + 1].strip()
            if changed_arg:
                changed_files = set(changed_arg.split())
                print(f"Incremental build: PDFs only for {len(changed_files)} changed file(s)")
            else:
                changed_files = set()
                print("No changed files specified — skipping PDF generation")

    print("Building PSYC 11 course pages...")
    print("=" * 50)

    (REPO_ROOT / "syllabus").mkdir(exist_ok=True)
    (REPO_ROOT / "assignments").mkdir(exist_ok=True)

    build_outline_page()
    build_syllabus()
    build_assignment_hub()
    build_individual_assignments(changed_files=changed_files)

    print("=" * 50)
    print("Done!")


if __name__ == "__main__":
    main()
