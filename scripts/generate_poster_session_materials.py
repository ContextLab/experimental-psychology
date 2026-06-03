#!/usr/bin/env python3
"""Generate poster-session materials for PSYC 11.

Produces two PDFs in admin/:
  1. group labels for posters.pdf  -- a large (50" x 36") sheet with a grid of
     "Group N" signs, one per group, meant to be printed and cut apart.
  2. poster_voting_form.pdf        -- a letter-size sign with a QR code and URL
     pointing to the poster-voting Google Form.

Both use Berkeley Mono Bold to match prior years' materials.

Usage:
    python scripts/generate_poster_session_materials.py [--groups N] [--url URL]
"""

import argparse
import os
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_pdf import PdfPages

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_PATH = os.path.expanduser("~/Library/Fonts/berkeley-mono.ttf")
DEFAULT_URL = "https://forms.gle/Nok8akR8K8sLLXR9A"
DEFAULT_BG = os.path.join(REPO_ROOT, "admin", "voting_form_background_image.png")


def _font(size):
    return FontProperties(fname=FONT_PATH, size=size)


def _fit_fontsize(fig, text, max_w_pt, max_h_pt, start=400, floor=10):
    """Largest font size (pt) such that `text` fits in the given box."""
    renderer = fig.canvas.get_renderer()
    size = start
    while size > floor:
        t = fig.text(0.5, 0.5, text, fontproperties=_font(size), ha="center", va="center")
        bb = t.get_window_extent(renderer=renderer)  # pixels at fig dpi
        t.remove()
        w_pt = bb.width / fig.dpi * 72
        h_pt = bb.height / fig.dpi * 72
        if w_pt <= max_w_pt and h_pt <= max_h_pt:
            return size
        size -= 2
    return floor


def make_group_labels(n_groups, out_path, ncols=4):
    """A 50" x 36" landscape sheet with a grid of 'Group N' signs."""
    W_IN, H_IN = 50.0, 36.0
    nrows = -(-n_groups // ncols)  # ceil

    fig = plt.figure(figsize=(W_IN, H_IN), dpi=72)
    fig.canvas.draw()  # init renderer

    # A square box surrounds each label; size it to fit within the grid cell.
    cell_w_in = W_IN / ncols
    cell_h_in = H_IN / nrows
    side_in = 0.88 * min(cell_w_in, cell_h_in)  # square, with a gap around it
    side_pt = side_in * 72

    # widest label determines a single shared font size that fits the square
    widest = max((f"Group {i}" for i in range(1, n_groups + 1)), key=len)
    fs = _fit_fontsize(fig, widest, max_w_pt=0.82 * side_pt,
                       max_h_pt=0.45 * side_pt)

    # square dimensions expressed in figure-fraction coords (page W != H)
    w_frac = side_in / W_IN
    h_frac = side_in / H_IN

    for i in range(1, n_groups + 1):
        idx = i - 1
        col = idx % ncols
        row = idx // ncols
        x = (col + 0.5) / ncols
        # matplotlib y is bottom-up; fill top-to-bottom
        y = 1 - (row + 0.5) / nrows
        rect = mpatches.Rectangle(
            (x - w_frac / 2, y - h_frac / 2), w_frac, h_frac,
            transform=fig.transFigure, fill=False, edgecolor="black",
            linewidth=3)
        fig.add_artist(rect)
        fig.text(x, y, f"Group {i}", fontproperties=_font(fs),
                 ha="center", va="center", color="black")

    with PdfPages(out_path) as pdf:
        pdf.savefig(fig)
    plt.close(fig)
    print(f"Wrote {out_path} ({n_groups} groups, {ncols}x{nrows} grid, "
          f"font {fs}pt, {side_in:.1f}\" squares)")


def make_voting_form(url, qr_path, out_path, bg_path=DEFAULT_BG):
    """Letter-size voting sign: title, instructions, QR code, URL."""
    W_IN, H_IN = 8.5, 11.0
    fig = plt.figure(figsize=(W_IN, H_IN), dpi=72)
    fig.canvas.draw()

    # Faint full-page background watermark. Center-crop the source image to the
    # page aspect ratio, then stretch it edge-to-edge (no distortion) at 5% alpha.
    if bg_path and os.path.exists(bg_path):
        bg = mpimg.imread(bg_path)
        ih, iw = bg.shape[:2]
        page_aspect = W_IN / H_IN
        img_aspect = iw / ih
        if img_aspect > page_aspect:  # too wide -> crop width
            new_w = int(round(ih * page_aspect))
            x0 = (iw - new_w) // 2
            bg = bg[:, x0:x0 + new_w]
        else:  # too tall -> crop height
            new_h = int(round(iw / page_aspect))
            y0 = (ih - new_h) // 2
            bg = bg[y0:y0 + new_h, :]
        bg_ax = fig.add_axes([0, 0, 1, 1], zorder=-1)
        bg_ax.imshow(bg, aspect="auto", extent=[0, 1, 0, 1], alpha=0.05)
        bg_ax.axis("off")

    # Title (two lines, large bold) centered near top
    fig.text(0.5, 0.86, "Welcome to the PSYC 11", fontproperties=_font(34),
             ha="center", va="center", color="black")
    fig.text(0.5, 0.80, "poster session!", fontproperties=_font(34),
             ha="center", va="center", color="black")

    # Instructions (smaller)
    fig.text(0.5, 0.68, "Please vote on your favorite poster",
             fontproperties=_font(17), ha="center", va="center", color="black")
    fig.text(0.5, 0.645, "by visiting the web form below:",
             fontproperties=_font(17), ha="center", va="center", color="black")

    # QR code centered
    qr = mpimg.imread(qr_path)
    ax = fig.add_axes([0.5 - 0.21, 0.30, 0.42, 0.32])  # [left, bottom, w, h]
    ax.imshow(qr, interpolation="nearest")
    ax.axis("off")

    # URL below QR
    fig.text(0.5, 0.24, url, fontproperties=_font(15),
             ha="center", va="center", color="black")

    with PdfPages(out_path) as pdf:
        pdf.savefig(fig)
    plt.close(fig)
    print(f"Wrote {out_path} (url: {url})")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--groups", type=int, default=14)
    p.add_argument("--url", default=DEFAULT_URL)
    p.add_argument("--qr", default=None, help="path to a pre-generated QR png")
    args = p.parse_args()

    admin = os.path.join(REPO_ROOT, "admin")
    make_group_labels(args.groups, os.path.join(admin, "group labels for posters.pdf"))

    qr_path = args.qr
    tmp = None
    if qr_path is None:
        import qrcode
        tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,
                           box_size=10, border=2)
        qr.add_data(args.url)
        qr.make(fit=True)
        qr.make_image(fill_color="black", back_color="white").save(tmp.name)
        qr_path = tmp.name

    make_voting_form(args.url, qr_path, os.path.join(admin, "poster_voting_form.pdf"))
    if tmp:
        os.unlink(tmp.name)


if __name__ == "__main__":
    main()
