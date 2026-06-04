#!/usr/bin/env python3
"""Convert a Mermaid chart to an image using the local Mermaid CLI (mmdc).

Requires Node.js and @mermaid-js/mermaid-cli:
    npm install -g @mermaid-js/mermaid-cli
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def find_mmdc() -> str:
    """Return the mmdc executable path, or exit with an install hint."""
    cmd = shutil.which("mmdc") or shutil.which("mmdc.cmd")
    if cmd:
        return cmd
    sys.exit(
        "error: mmdc not found. Install the Mermaid CLI with:\n"
        "    npm install -g @mermaid-js/mermaid-cli"
    )


def extract_mermaid(content: str, index: int = 0) -> str:
    blocks = re.findall(r"```mermaid\n(.*?)```", content, re.DOTALL)
    if not blocks:
        raise ValueError("No mermaid code block found in input")
    if index >= len(blocks):
        raise ValueError(f"Block index {index} out of range — found {len(blocks)} block(s)")
    return blocks[index].strip()


def extract_segments(content: str) -> list[tuple[str, str]]:
    """Return [(segment_name, mermaid_code), ...] for each '### Canvas: Name' section."""
    section_re = re.compile(r"^### Canvas:\s*(.+)$", re.MULTILINE)
    mermaid_re = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)

    segments = []
    section_matches = list(section_re.finditer(content))
    for i, match in enumerate(section_matches):
        name = match.group(1).strip()
        start = match.end()
        end = section_matches[i + 1].start() if i + 1 < len(section_matches) else len(content)
        mermaid_match = mermaid_re.search(content[start:end])
        if mermaid_match:
            segments.append((name, mermaid_match.group(1).strip()))
    return segments


def slugify(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_").lower()


def render(mmdc: str, mermaid_code: str, output_path: Path, theme: str) -> None:
    with tempfile.NamedTemporaryFile(suffix=".mmd", mode="w", delete=False) as tmp:
        tmp.write(mermaid_code)
        tmp_path = Path(tmp.name)

    try:
        result = subprocess.run(
            [mmdc, "-i", str(tmp_path), "-o", str(output_path), "-t", theme, "-b", "transparent"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            sys.exit(f"mmdc failed:\n{result.stderr.strip()}")
    finally:
        tmp_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a Mermaid chart to an image using the local mmdc CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s value_proposition_canvas.md
  %(prog)s diagram.mmd -o out.png
  %(prog)s value_proposition_canvas.md --format svg --theme dark
  %(prog)s value-proposition-canvases-output.md --all-segments
  %(prog)s value-proposition-canvases-output.md --all-segments --output-dir ./images
  cat diagram.mmd | %(prog)s -
""",
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="Input file (.md or .mmd), or '-' to read from stdin (default: stdin)",
    )
    parser.add_argument("-o", "--output", help="Output file path (default: <input stem>.<format>)")
    parser.add_argument(
        "--format",
        default="png",
        choices=["png", "svg", "pdf"],
        help="Output image format (default: png)",
    )
    parser.add_argument(
        "--theme",
        default="default",
        choices=["default", "dark", "forest", "neutral", "base"],
        help="Mermaid theme (default: default)",
    )
    parser.add_argument(
        "--block",
        type=int,
        default=0,
        metavar="N",
        help="Which mermaid block to render when input has multiple (0-indexed, default: 0)",
    )
    parser.add_argument(
        "--all-segments",
        action="store_true",
        help=(
            "Render every '### Canvas: [Name]' section as vpcanvas_<name>.<format>. "
            "Output directory defaults to the input file's directory."
        ),
    )
    parser.add_argument(
        "--output-dir",
        help="Directory for --all-segments output files (default: input file directory)",
    )
    args = parser.parse_args()

    mmdc = find_mmdc()

    # Read source
    if args.input == "-":
        content = sys.stdin.read()
        input_path = None
    else:
        input_path = Path(args.input)
        if not input_path.exists():
            sys.exit(f"error: '{input_path}' not found")
        content = input_path.read_text(encoding="utf-8")

    # Multi-segment mode: render every ### Canvas: section
    if args.all_segments:
        segments = extract_segments(content)
        if not segments:
            sys.exit("error: no '### Canvas: [Name]' sections with mermaid blocks found")
        out_dir = (
            Path(args.output_dir)
            if args.output_dir
            else (input_path.parent if input_path else Path("."))
        )
        out_dir.mkdir(parents=True, exist_ok=True)
        for name, mermaid_code in segments:
            out_path = out_dir / f"vpcanvas_{slugify(name)}.{args.format}"
            print(f"Rendering '{name}' → {out_path}  (theme={args.theme})")
            render(mmdc, mermaid_code, out_path, args.theme)
            print(f"  Saved {out_path.stat().st_size:,} bytes")
        return

    # Extract mermaid code
    is_pure_mmd = input_path is not None and input_path.suffix == ".mmd"
    try:
        mermaid_code = content.strip() if is_pure_mmd else extract_mermaid(content, args.block)
    except ValueError as exc:
        sys.exit(f"error: {exc}")

    # Resolve output path
    if args.output:
        output_path = Path(args.output)
    elif input_path:
        output_path = input_path.with_suffix(f".{args.format}")
    else:
        output_path = Path(f"output.{args.format}")

    print(f"Rendering → {output_path}  (theme={args.theme}, format={args.format})")
    render(mmdc, mermaid_code, output_path, args.theme)
    print(f"Saved {output_path.stat().st_size:,} bytes to {output_path}")


if __name__ == "__main__":
    main()
