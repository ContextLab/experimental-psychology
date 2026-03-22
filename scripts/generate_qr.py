#!/usr/bin/env python3
"""Generate QR code PNG images for use in Marp slides.

Usage:
    python scripts/generate_qr.py <url> <output_path>

Example:
    python scripts/generate_qr.py "https://colab.research.google.com/github/ContextLab/experimental-psychology/blob/main/notebooks/demo.ipynb" slides/figs/demo_qr.png
"""

import sys
import qrcode


def generate_qr(url: str, output_path: str, box_size: int = 10, border: int = 2) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    print(f"QR code saved to {output_path} (encodes: {url})")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    generate_qr(sys.argv[1], sys.argv[2])
