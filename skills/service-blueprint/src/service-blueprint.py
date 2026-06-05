---

### 2. `./src/service-blueprint.py`

```python
#!/usr/bin/env python3
import textwrap
import os

# ==============================================================================
# AGENT INSTRUCTION: Rewrite this file and replace the BLUEPRINT_DATA dictionary 
# below with your synthesized service blueprint data before executing the script.
# ==============================================================================
BLUEPRINT_DATA = {
  "title": "Service Blueprint: Example Segment - Example Product",
  "phases": ["Phase 1", "Phase 2", "Phase 3"],
  "rows": [
    {
      "name": "Physical / Digital Evidence",
      "cells": [
        [{"id": "e1", "content": "Example artifact"}], # Phase 1
        [{"content": ""}],                              # Blank spacer (Phase 2)
        [{"id": "e3", "content": "Another artifact"}]   # Phase 3
      ]
    },
    {
      "name": "Customer Actions",
      "cells": [
        [{"id": "c1", "content": "Example action 1"}],
        [                                               # Multiple actions in Phase 2
          {"id": "c2a", "content": "Example action 2A"},
          {"id": "c2b", "content": "Example action 2B"}
        ],
        [{"content": ""}]
      ]
    },
    {
      "name": "Frontstage Actions",
      "divider": "Line of Interaction",
      "cells": [
        [{"id": "f1", "content": "Visible staff action"}],
        [{"id": "f2", "content": "Staff assists with 2A"}],
        [{"content": ""}]
      ]
    },
    {
      "name": "Backstage Actions",
      "divider": "Line of Visibility",
      "cells": [
        [{"id": "b1", "content": "Invisible processing"}],
        [{"id": "b2", "content": "System validates 2B"}],
        [{"content": ""}]
      ]
    },
    {
      "name": "Support Processes",
      "divider": "Line of Internal Interaction",
      "cells": [
        [{"content": ""}],
        [{"id": "s2", "content": "System infrastructure"}],
        [{"content": ""}]
      ]
    }
  ],
  "connections": [
    {"from": "c1", "to": "f1"},
    {"from": "f1", "to": "b1"},
    {"from": "b1", "to": "c2a"},
    {"from": "c2a", "to": "f2"},
    {"from": "c2a", "to": "c2b"},
    {"from": "c2b", "to": "b2"},
    {"from": "b2", "to": "s2"},
    {"from": "s2", "to": "e3"}
  ]
}
# ==============================================================================

def wrap_text(text, width=32):
    """Wraps text into multiple lines for SVG rendering."""
    if not text:
        return []
    return textwrap.wrap(text, width=width)

def generate_svg_image(data, output_file):
    """
    Renders a 2D grid SVG image, calculates bounding boxes for all cell IDs, 
    and draws curved paths for connections. Supports multiple items per cell.
    """
    col_w = 260
    label_w = 200
    header_h = 70
    margin = 40
    line_h = 18
    
    # Padding settings
    cell_padding = 15  # Distance from grid line to the block of boxes
    box_padding = 10   # Internal padding inside the white action box
    item_spacing = 10  # Space between stacked boxes in the same cell

    phases = data.get("phases", [])
    num_cols = len(phases)
    rows = data.get("rows", [])
    connections = data.get("connections", [])
    
    cell_coords = {}
    
    # Pass 1: Calculate row heights based on multiple items and wrapped text
    row_heights = []
    for row in rows:
        max_cell_h = 0
        for cell in row.get("cells", []):
            items = cell
            
            cell_block_h = 0
            valid_items = 0
            
            for item in items:
                content = item.get("content", "").strip() if isinstance(item, dict) else str(item).strip()
                if content:
                    lines = wrap_text(content)
                    item_h = (box_padding * 2) + (len(lines) * line_h)
                    cell_block_h += item_h
                    valid_items += 1
                    
            if valid_items > 1:
                cell_block_h += item_spacing * (valid_items - 1)
                
            max_cell_h = max(max_cell_h, cell_block_h)
            
        calculated_height = (cell_padding * 2) + max_cell_h
        row_heights.append(max(calculated_height, 80)) # Minimum 80px row height

    width = label_w + (num_cols * col_w) + (2 * margin)
    height = header_h + sum(row_heights) + (2 * margin)
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '    <path d="M 0 0 L 10 5 L 0 10 z" fill="#805ad5" />',
        '  </marker>',
        '</defs>',
        '<style>',
        '  text { font-family: "Segoe UI", Arial, sans-serif; }',
        '  .title { font-size: 26px; font-weight: bold; fill: #1a202c; }',
        '  .header { font-size: 16px; font-weight: bold; fill: #2d3748; }',
        '  .label { font-size: 14px; font-weight: bold; fill: #4a5568; }',
        '  .content { font-size: 13px; fill: #2d3748; }',
        '  .divider-line { stroke: #e53e3e; stroke-width: 2; stroke-dasharray: 6,4; }',
        '  .divider-text { font-size: 12px; font-weight: bold; fill: #e53e3e; font-style: italic; }',
        '  .grid-line { stroke: #e2e8f0; stroke-width: 1; }',
        '  .cell-rect { fill: #ffffff; stroke: #cbd5e0; stroke-width: 1; rx: 6px; }',
        '  .connection { stroke: #805ad5; stroke-width: 2; fill: none; stroke-dasharray: 4,2; opacity: 0.8; }',
        '</style>',
        f'<rect width="{width}" height="{height}" fill="#f7fafc" />'
    ]
    
    title = data.get("title", "Service Blueprint")
    svg.append(f'<text x="{margin}" y="{margin + 20}" class="title">{title}</text>')
    
    offset_x = margin + label_w
    offset_y = margin + header_h
    
    # Draw Phase Headers
    for i, phase in enumerate(phases):
        x = offset_x + (i * col_w) + (col_w / 2)
        y = offset_y - 15
        svg.append(f'<text x="{x}" y="{y}" class="header" text-anchor="middle">{phase}</text>')
        
    # Pass 2: Calculate coordinates and draw background lines/labels and boxes
    current_y = offset_y
    cell_rects_and_text = [] # Save these to draw *after* the connection lines
    
    for r_idx, row in enumerate(rows):
        row_h = row_heights[r_idx]
        
        # Grid lines / Dividers
        if row.get("divider"):
            svg.append(f'<line x1="{margin}" y1="{current_y}" x2="{width-margin}" y2="{current_y}" class="divider-line"/>')
            svg.append(f'<text x="{width-margin}" y="{current_y-6}" class="divider-text" text-anchor="end">{row["divider"]}</text>')
        elif r_idx > 0:
            svg.append(f'<line x1="{margin}" y1="{current_y}" x2="{width-margin}" y2="{current_y}" class="grid-line"/>')
            
        svg.append(f'<text x="{margin}" y="{current_y + (row_h/2) + 5}" class="label">{row.get("name", "")}</text>')
            
        # Draw cells
        for c_idx, cell in enumerate(row.get("cells", [])):
            items = cell
            x = offset_x + (c_idx * col_w)
            
            # First, calculate total block height to vertically center it in the row
            valid_items_list = []
            cell_block_h = 0
            for item in items:
                content = item.get("content", "").strip() if isinstance(item, dict) else str(item).strip()
                if content:
                    lines = wrap_text(content)
                    item_h = (box_padding * 2) + (len(lines) * line_h)
                    valid_items_list.append((item, lines, item_h))
                    cell_block_h += item_h
                    
            if len(valid_items_list) > 1:
                cell_block_h += item_spacing * (len(valid_items_list) - 1)
                
            if valid_items_list:
                # Calculate starting Y to center the block of items vertically
                start_y = current_y + (row_h - cell_block_h) / 2
                current_item_y = start_y
                
                for item, lines, item_h in valid_items_list:
                    box_x = x + 10
                    box_w = col_w - 20
                    
                    if isinstance(item, dict) and item.get("id"):
                        cell_coords[item["id"]] = {
                            "cx": box_x + (box_w / 2),
                            "cy": current_item_y + (item_h / 2),
                            "top": current_item_y,
                            "bottom": current_item_y + item_h,
                            "left": box_x,
                            "right": box_x + box_w
                        }
                    
                    rect_svg = f'<rect x="{box_x}" y="{current_item_y}" width="{box_w}" height="{item_h}" class="cell-rect"/>'
                    cell_rects_and_text.append(rect_svg)
                    
                    for l_idx, line in enumerate(lines):
                        ly = current_item_y + box_padding + (l_idx * line_h) + 5
                        safe_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                        cell_rects_and_text.append(f'<text x="{box_x + box_padding}" y="{ly}" class="content">{safe_line}</text>')
                        
                    current_item_y += item_h + item_spacing
                
        current_y += row_h

    # Pass 3: Draw Connection Lines (Bezier Curves)
    for conn in connections:
        src = cell_coords.get(conn.get("from"))
        dst = cell_coords.get(conn.get("to"))
        
        if src and dst:
            is_vertical = abs(dst["cx"] - src["cx"]) < abs(dst["cy"] - src["cy"])
            
            if is_vertical:
                sx, ex = src["cx"], dst["cx"]
                if dst["cy"] > src["cy"]: # Flowing down
                    sy, ey = src["bottom"], dst["top"]
                else:                     # Flowing up
                    sy, ey = src["top"], dst["bottom"]
                    
                cp1x, cp1y = sx, sy + (ey - sy) * 0.4
                cp2x, cp2y = ex, ey - (ey - sy) * 0.4
            else:
                sy, ey = src["cy"], dst["cy"]
                if dst["cx"] > src["cx"]: # Flowing right
                    sx, ex = src["right"], dst["left"]
                else:                     # Flowing left
                    sx, ex = src["left"], dst["right"]
                    
                cp1x, cp1y = sx + (ex - sx) * 0.4, sy
                cp2x, cp2y = ex - (ex - sx) * 0.4, ey

            path_d = f"M {sx} {sy} C {cp1x} {cp1y}, {cp2x} {cp2y}, {ex} {ey}"
            svg.append(f'<path d="{path_d}" class="connection" marker-end="url(#arrow)" />')

    # Pass 4: Draw boxes and text so they sit above the connecting lines
    svg.extend(cell_rects_and_text)
        
    svg.append('</svg>')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(svg))

def main():
    output_path = "blueprint.svg"
    try:
        generate_svg_image(BLUEPRINT_DATA, output_path)
        print(f"✅ Service Blueprint image successfully generated at '{output_path}'.")
        print("Note: SVGs are vector images that can be viewed in any web browser or image viewer.")
        print("Agent Instruction: Now, please generate the detailed 'service-blueprint.md' report.")
    except Exception as e:
        print(f"❌ Unexpected error generating image: {e}")

if __name__ == "__main__":
    main()