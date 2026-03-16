#!/usr/bin/env python3
"""Convert an SVG icon to multiple PNG sizes.

Usage:
    python svg_to_png.py icon.svg --sizes 16,24,32,48,64,128,256,512 --output-dir ./sizes/

Tries cairosvg first (best quality), falls back to Pillow.
"""

import argparse
import os
import sys

DEFAULT_SIZES = [16, 24, 32, 48, 64, 128, 256, 512]


def convert_with_cairosvg(svg_path, output_dir, sizes, base_name):
    """High-quality SVG to PNG using cairosvg."""
    import cairosvg

    for size in sizes:
        output_path = os.path.join(output_dir, f"{base_name}_{size}x{size}.png")
        cairosvg.svg2png(
            url=svg_path,
            write_to=output_path,
            output_width=size,
            output_height=size,
        )
        print(f"  Created {output_path}")

    # Also create the largest size as the main icon
    largest = max(sizes)
    main_path = os.path.join(output_dir, f"{base_name}_{largest}.png")
    if not os.path.exists(main_path):
        cairosvg.svg2png(
            url=svg_path,
            write_to=main_path,
            output_width=largest,
            output_height=largest,
        )


def convert_with_pillow(svg_path, output_dir, sizes, base_name):
    """Fallback: render SVG at largest size, then resize down with Pillow."""
    from PIL import Image
    import subprocess
    import tempfile

    largest = max(sizes)

    # Try using rsvg-convert if available
    tmp_png = os.path.join(tempfile.gettempdir(), f"{base_name}_tmp.png")
    try:
        subprocess.run(
            ["rsvg-convert", "-w", str(largest), "-h", str(largest), svg_path, "-o", tmp_png],
            check=True, capture_output=True,
        )
        img = Image.open(tmp_png)
    except (FileNotFoundError, subprocess.CalledProcessError):
        # Last resort: try opening SVG directly with Pillow (limited support)
        try:
            img = Image.open(svg_path)
            img = img.resize((largest, largest), Image.LANCZOS)
        except Exception:
            print(f"  Warning: Could not render SVG. Install cairosvg for best results:")
            print(f"    pip install cairosvg --break-system-packages")
            return False

    for size in sizes:
        resized = img.resize((size, size), Image.LANCZOS)
        output_path = os.path.join(output_dir, f"{base_name}_{size}x{size}.png")
        resized.save(output_path, "PNG")
        print(f"  Created {output_path}")

    # Clean up temp file
    if os.path.exists(tmp_png):
        os.remove(tmp_png)

    return True


def create_ico(png_dir, base_name, output_dir):
    """Create a favicon.ico from existing PNGs."""
    from PIL import Image

    ico_sizes = [(16, 16), (32, 32), (48, 48)]
    images = []
    for w, h in ico_sizes:
        png_path = os.path.join(png_dir, f"{base_name}_{w}x{h}.png")
        if os.path.exists(png_path):
            images.append(Image.open(png_path))

    if images:
        ico_path = os.path.join(output_dir, "favicon.ico")
        images[0].save(ico_path, format="ICO", sizes=ico_sizes, append_images=images[1:])
        print(f"  Created {ico_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert SVG to multiple PNG sizes")
    parser.add_argument("svg", help="Path to the SVG file")
    parser.add_argument("--sizes", default=",".join(map(str, DEFAULT_SIZES)),
                        help="Comma-separated list of sizes (default: 16,24,32,48,64,128,256,512)")
    parser.add_argument("--output-dir", default="./sizes/", help="Output directory")
    parser.add_argument("--ico", action="store_true", help="Also generate favicon.ico")
    parser.add_argument("--name", default=None, help="Base name for output files (default: SVG filename)")
    args = parser.parse_args()

    sizes = [int(s.strip()) for s in args.sizes.split(",")]
    os.makedirs(args.output_dir, exist_ok=True)
    base_name = args.name or os.path.splitext(os.path.basename(args.svg))[0]

    print(f"Converting {args.svg} to PNG at sizes: {sizes}")

    try:
        import cairosvg
        print("Using cairosvg (high quality)")
        convert_with_cairosvg(args.svg, args.output_dir, sizes, base_name)
    except ImportError:
        print("cairosvg not found, trying Pillow fallback")
        convert_with_pillow(args.svg, args.output_dir, sizes, base_name)

    if args.ico:
        try:
            create_ico(args.output_dir, base_name, args.output_dir)
        except Exception as e:
            print(f"  Warning: Could not create favicon.ico: {e}")

    print("Done!")


if __name__ == "__main__":
    main()
