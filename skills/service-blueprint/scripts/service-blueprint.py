#!/usr/bin/env python3
import textwrap, math
from PIL import Image, ImageDraw, ImageFont

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
        [{"id": "e1", "content": "Example artifact"}],
        [{"content": ""}],
        [{"id": "e3", "content": "Another artifact"}]
      ]
    },
    {
      "name": "Customer Actions",
      "cells": [
        [{"id": "c1", "content": "Example action 1"}],
        [
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
    {"from": "c1",  "to": "f1"},
    {"from": "f1",  "to": "b1"},
    {"from": "b1",  "to": "c2a"},
    {"from": "c2a", "to": "f2"},
    {"from": "c2a", "to": "c2b"},
    {"from": "c2b", "to": "b2"},
    {"from": "b2",  "to": "s2"},
    {"from": "s2",  "to": "e3"}
  ]
}
# ==============================================================================

# ── palette ────────────────────────────────────────────────────────────────────
BG      = (247, 250, 252, 255)
DARK    = ( 26,  32,  44, 255)
MED     = ( 45,  55,  72, 255)
GRAY    = ( 74,  85, 104, 255)
LGRAY   = (226, 232, 240, 255)
WHITE   = (255, 255, 255, 255)
BORDER  = (203, 213, 224, 255)
RED     = (229,  62,  62, 255)
PURPLE  = (  0,   0,   0, 200)
PURP_S  = (  0,   0,   0, 255)
DIV_LINE= ( 74,  85, 104, 255)


def wrap_text(text, width=32):
    return textwrap.wrap(text, width=width) if text else []


def load_font(size):
    for path in [
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()


def bezier_pt(t, p0, p1, p2, p3):
    u = 1 - t
    return (
        u**3*p0[0] + 3*u**2*t*p1[0] + 3*u*t**2*p2[0] + t**3*p3[0],
        u**3*p0[1] + 3*u**2*t*p1[1] + 3*u*t**2*p2[1] + t**3*p3[1],
    )


def draw_bezier(draw, p0, p1, p2, p3, color, lw):
    pts = [bezier_pt(i / 60, p0, p1, p2, p3) for i in range(61)]
    draw.line(pts, fill=color, width=lw)


def draw_arrow(draw, tip, prev, color, size):
    dx, dy = tip[0] - prev[0], tip[1] - prev[1]
    dist = math.hypot(dx, dy)
    if dist < 0.1:
        return
    ux, uy = dx / dist, dy / dist
    base = (tip[0] - ux * size, tip[1] - uy * size)
    draw.polygon([
        (int(tip[0]),               int(tip[1])),
        (int(base[0] - uy*size*0.45), int(base[1] + ux*size*0.45)),
        (int(base[0] + uy*size*0.45), int(base[1] - ux*size*0.45)),
    ], fill=color)


def rrect(draw, x1, y1, x2, y2, r, fill, outline, lw):
    try:
        draw.rounded_rectangle([(x1, y1), (x2, y2)], radius=r,
                                fill=fill, outline=outline, width=lw)
    except AttributeError:
        draw.rectangle([(x1, y1), (x2, y2)], fill=fill, outline=outline, width=lw)


def generate_png(data, output_file, scale=2):
    col_w    = 260; label_w  = 200; header_h = 70;  margin   = 40
    line_h   = 18;  cell_pad = 15;  box_pad  = 10;  item_gap = 10

    phases = data.get("phases", [])
    rows   = data.get("rows",   [])
    conns  = data.get("connections", [])
    nc     = len(phases)

    # Pass 1 – row heights
    rh_list = []
    for row in rows:
        max_h = 0
        for cell in row.get("cells", []):
            bh = n = 0
            for item in cell:
                c = (item.get("content", "") if isinstance(item, dict) else str(item)).strip()
                if c:
                    bh += box_pad * 2 + len(wrap_text(c)) * line_h
                    n  += 1
            if n > 1:
                bh += item_gap * (n - 1)
            max_h = max(max_h, bh)
        rh_list.append(max(cell_pad * 2 + max_h, 80))

    W = label_w + nc * col_w + 2 * margin
    H = header_h + sum(rh_list) + 2 * margin
    S = scale

    img  = Image.new("RGBA", (W * S, H * S), BG)
    draw = ImageDraw.Draw(img)

    ft = load_font(26 * S); fh = load_font(16 * S)
    fl = load_font(14 * S); fc = load_font(13 * S); fd = load_font(12 * S)

    # Title
    draw.text((margin * S, (margin + 4) * S),
              data.get("title", "Service Blueprint"), font=ft, fill=DARK)

    ox, oy = margin + label_w, margin + header_h

    # Phase headers (horizontally centered)
    for i, ph in enumerate(phases):
        bb = draw.textbbox((0, 0), ph, font=fh)
        tw = bb[2] - bb[0]
        x  = (ox + i * col_w + col_w // 2) * S - tw // 2
        draw.text((x, (oy - 22) * S), ph, font=fh, fill=MED)

    cur_y  = oy
    coords = {}
    later  = []   # drawn after connections: ("rect", x1,y1,x2,y2) | ("text", x,y,s,f,col)

    for r_idx, row in enumerate(rows):
        rh = rh_list[r_idx]

        # Grid / divider line
        if row.get("divider"):
            draw.line([(margin * S, cur_y * S), ((W - margin) * S, cur_y * S)],
                      fill=DIV_LINE, width=2 * S)
            txt = row["divider"]
            bb  = draw.textbbox((0, 0), txt, font=fd)
            tw  = bb[2] - bb[0]
            later.append(("text", (W - margin) * S - tw - 4 * S, (cur_y - 14) * S,
                          txt, fd, DIV_LINE))
        elif r_idx > 0:
            draw.line([(margin * S, cur_y * S), ((W - margin) * S, cur_y * S)],
                      fill=LGRAY, width=S)

        # Row label (vertically centered)
        lbl = row.get("name", "")
        bb  = draw.textbbox((0, 0), lbl, font=fl)
        lh  = bb[3] - bb[1]
        draw.text((margin * S, (cur_y + rh // 2) * S - lh // 2),
                  lbl, font=fl, fill=GRAY)

        # Cells
        for ci, cell in enumerate(row.get("cells", [])):
            bx0 = ox + ci * col_w
            vitems, block_h = [], 0
            for item in cell:
                c = (item.get("content", "") if isinstance(item, dict) else str(item)).strip()
                if c:
                    lns = wrap_text(c)
                    ih  = box_pad * 2 + len(lns) * line_h
                    vitems.append((item, lns, ih))
                    block_h += ih
            if len(vitems) > 1:
                block_h += item_gap * (len(vitems) - 1)
            if vitems:
                iy = cur_y + (rh - block_h) // 2
                for item, lns, ih in vitems:
                    bx, bw = bx0 + 10, col_w - 20
                    if isinstance(item, dict) and item.get("id"):
                        coords[item["id"]] = dict(
                            cx=bx + bw / 2,  cy=iy + ih / 2,
                            top=iy,          bottom=iy + ih,
                            left=bx,         right=bx + bw,
                        )
                    later.append(("rect", bx * S, iy * S, (bx + bw) * S, (iy + ih) * S))
                    for li, line in enumerate(lns):
                        ly = (iy + box_pad + li * line_h + 2) * S
                        later.append(("text", (bx + box_pad) * S, ly, line, fc, MED))
                    iy += ih + item_gap

        cur_y += rh

    # Pass 3 – connection curves (drawn before boxes)
    for conn in conns:
        src = coords.get(conn.get("from"))
        dst = coords.get(conn.get("to"))
        if not (src and dst):
            continue
        vert = abs(dst["cx"] - src["cx"]) < abs(dst["cy"] - src["cy"])
        if vert:
            sx, ex = src["cx"], dst["cx"]
            if dst["cy"] > src["cy"]: sy, ey = src["bottom"], dst["top"]
            else:                     sy, ey = src["top"],    dst["bottom"]
            cp1 = (sx, sy + (ey - sy) * 0.4)
            cp2 = (ex, ey - (ey - sy) * 0.4)
        else:
            sy, ey = src["cy"], dst["cy"]
            if dst["cx"] > src["cx"]: sx, ex = src["right"], dst["left"]
            else:                     sx, ex = src["left"],  dst["right"]
            cp1 = (sx + (ex - sx) * 0.4, sy)
            cp2 = (ex - (ex - sx) * 0.4, ey)

        p0 = (sx*S, sy*S); p1 = (cp1[0]*S, cp1[1]*S)
        p2 = (cp2[0]*S, cp2[1]*S); p3 = (ex*S, ey*S)
        draw_bezier(draw, p0, p1, p2, p3, PURPLE, 2 * S)
        near = bezier_pt(0.94, p0, p1, p2, p3)
        draw_arrow(draw, p3, near, PURP_S, 10 * S)

    # Pass 4 – boxes and text on top of connection lines
    for d in later:
        if d[0] == "rect":
            rrect(draw, d[1], d[2], d[3], d[4], 6 * S, WHITE, BORDER, S)
        else:
            draw.text((d[1], d[2]), d[3], font=d[4], fill=d[5])

    # Downsample for smooth anti-aliasing
    img.convert("RGB").resize((W, H), Image.LANCZOS).save(output_file, "PNG")


def main():
    output_path = "blueprint.png"
    try:
        generate_png(BLUEPRINT_DATA, output_path)
        print(f"✅ Service Blueprint image successfully generated at '{output_path}'.")
        print("Note: PNG images can be viewed in any image viewer or web browser.")
        print("Agent Instruction: Now, please generate the detailed 'service-blueprint.md' report.")
    except Exception as e:
        import traceback; traceback.print_exc()
        print(f"❌ Unexpected error generating image: {e}")


if __name__ == "__main__":
    main()
