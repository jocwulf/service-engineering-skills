#!/usr/bin/env python3
"""Render the service ecosystem Mermaid diagram to an image via the mermaid.ink API.

Paste the MERMAID_CHART value produced by the service-ecosystem skill, then run:
    python service-ecosystem.py
    python service-ecosystem.py -o ecosystem.svg --format svg --theme dark
"""

import argparse
import base64
import json
import sys
import urllib.request
from pathlib import Path


MERMAID_CHART = ""


def render_via_api(mermaid_code: str, output_path: Path, theme: str) -> None:
    graph_config = {"code": mermaid_code, "options": {"theme": theme}}
    base64_string = base64.b64encode(json.dumps(graph_config).encode("utf-8")).decode("utf-8")

    fmt = output_path.suffix.lstrip(".")
    if fmt == "pdf":
        fmt = "png"
        output_path = output_path.with_suffix(".png")

    url = f"https://mermaid.ink/{fmt}/{base64_string}"
    print("Sending request to mermaid.ink API...")
    try:
        with urllib.request.urlopen(url) as response:
            output_path.write_bytes(response.read())
    except Exception as e:
        sys.exit(f"API rendering failed: {e}")


def main() -> None:
    if not MERMAID_CHART.strip():
        sys.exit("error: MERMAID_CHART is empty — paste the chart value into this file first")

    parser = argparse.ArgumentParser(
        description="Render the MERMAID_CHART variable to an image via mermaid.ink",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s -o ecosystem.svg --format svg --theme dark
""",
    )
    parser.add_argument("-o", "--output", help="Output file path (default: service_ecosystem.<format>)")
    parser.add_argument(
        "--format",
        default="png",
        choices=["png", "svg"],
        help="Output image format (default: png)",
    )
    parser.add_argument(
        "--theme",
        default="default",
        choices=["default", "dark", "forest", "neutral", "base"],
        help="Mermaid theme (default: default)",
    )
    args = parser.parse_args()

    output_path = Path(args.output) if args.output else Path(f"service_ecosystem.{args.format}")

    print(f"Rendering → {output_path}  (theme={args.theme}, format={args.format})")
    render_via_api(MERMAID_CHART, output_path, args.theme)
    print(f"Saved {output_path.stat().st_size:,} bytes to {output_path}")


if __name__ == "__main__":
    main()
