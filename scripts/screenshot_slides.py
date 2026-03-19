#!/usr/bin/env python3
"""Screenshot every slide from a compiled Marp HTML presentation.

Usage: python3 scripts/screenshot_slides.py slides/week1/lecture1.html
"""

import http.server
import os
import re
import socketserver
import subprocess
import sys
import threading
import time
from pathlib import Path


def find_free_port():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def start_server(directory, port):
    handler = http.server.SimpleHTTPRequestHandler
    os.chdir(directory)
    httpd = socketserver.TCPServer(("", port), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd


def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Installing playwright...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
    print("Ensuring Chromium browser is installed...")
    subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        check=True,
    )


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/screenshot_slides.py <path/to/slides.html>")
        sys.exit(1)

    html_path = Path(sys.argv[1]).resolve()
    if not html_path.exists():
        print(f"File not found: {html_path}")
        sys.exit(1)

    # Derive lecture name from the file path (e.g., "lecture1" from "slides/week1/lecture1.html")
    lecture_name = html_path.stem

    # Repo root is the directory containing the scripts/ folder
    repo_root = Path(__file__).resolve().parent.parent

    # Output directory
    out_dir = repo_root / "screenshots" / lecture_name
    out_dir.mkdir(parents=True, exist_ok=True)

    ensure_playwright()

    # Start local HTTP server from repo root
    port = find_free_port()
    rel_path = html_path.relative_to(repo_root)
    httpd = start_server(str(repo_root), port)
    url = f"http://localhost:{port}/{rel_path}"
    print(f"Serving at http://localhost:{port}, opening {url}")

    from playwright.sync_api import sync_playwright

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            page.goto(url, wait_until="networkidle")
            # Wait for bespoke to initialize
            time.sleep(1)

            # Get total slide count from the OSC "Page X of Y" element
            total_slides = page.evaluate("""
                () => {
                    const el = document.querySelector('[data-bespoke-marp-osc="page"]');
                    if (el) {
                        const m = el.textContent.match(/of\\s+(\\d+)/);
                        if (m) return parseInt(m[1]);
                    }
                    // Fallback: count section elements
                    return document.querySelectorAll('svg[data-marpit-svg] > foreignObject > section').length;
                }
            """)
            print(f"Detected {total_slides} slides")

            slides_info = []

            for i in range(1, total_slides + 1):
                # Wait for any transition to settle
                time.sleep(0.4)

                # Extract slide title (first h1 or h2 in the active slide)
                title = page.evaluate("""
                    () => {
                        const active = document.querySelector('.bespoke-marp-active');
                        if (!active) return '';
                        const h = active.querySelector('h1, h2, h3');
                        return h ? h.textContent.trim() : '';
                    }
                """)

                filename = f"slide{i:02d}.png"
                filepath = out_dir / filename
                page.screenshot(path=str(filepath))
                print(f"  Slide {i}/{total_slides}: {filename}" + (f" - {title}" if title else ""))

                slides_info.append({"number": i, "filename": filename, "title": title})

                # Navigate to next slide (except after last)
                if i < total_slides:
                    page.keyboard.press("ArrowRight")

            browser.close()

            # Generate report
            report_path = out_dir / "report.md"
            with open(report_path, "w") as f:
                f.write(f"# {lecture_name}\n\n")
                f.write(f"**Total slides:** {total_slides}\n\n")
                f.write("| Slide | Screenshot | Title |\n")
                f.write("|-|-|-|\n")
                for s in slides_info:
                    title = s["title"] or "(no title)"
                    f.write(f"| {s['number']} | {s['filename']} | {title} |\n")

            print(f"\nDone! Screenshots saved to: {out_dir}")
            print(f"Report: {report_path}")

    finally:
        httpd.shutdown()


if __name__ == "__main__":
    main()
