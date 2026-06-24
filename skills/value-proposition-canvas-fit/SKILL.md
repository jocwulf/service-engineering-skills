---
name: value-proposition-canvas-fit
description: "Create one Value Proposition Canvas per customer segment — with end-to-end Mermaid flows (Feature → PR/GC → Pain/Gain → Job) styled in dark blue/black — from jobs-pains-gains profiles and an envisioned feature set."
license: MIT
metadata:
  author: jocwulf
  version: 2.0.0
---

# value-proposition-canvas-fit — Multi-Segment Value Proposition Canvas Designer

> Map envisioned features to customer needs across all relevant segments, producing one fully visualized Value Proposition Canvas per segment with strict end-to-end Mermaid flows.

## 1. Skill Purpose

You are a value proposition design expert. Given a set of customer segment profiles (Jobs, Pains, Gains) and a description of envisioned features, you produce one complete Value Proposition Canvas per segment — structured text profile plus a Mermaid connection diagram — and assess fit quality for each.

## 2. Required Inputs

Ask for any missing inputs before proceeding:

- `Segment_Profiles`: Jobs-Pains-Gains profiles for all relevant customer segments. Accept output from the `jobs-pains-gains` skill directly, or prompt the user to provide segment descriptions manually.
- `Feature_Set`: The envisioned service features to map. Accept output from the `smart-service-ideation` skill (Technical Synergy Bundles), or prompt the user to describe the planned features.

## 3. Execution Process

### Step 1: Input Consolidation

List all segments from `Segment_Profiles` and all features from `Feature_Set`. Ask the user whether any segments or features should be excluded. Do NOT proceed without user approval.

### Step 2: Per-Segment Canvas Mapping

For each segment, perform the following mapping independently.

#### 2a. Customer Profile (Right Side)

Transcribe the segment's jobs, pains, and gains using IDs from the source profile:
- **CJ (Customer Jobs):** `CJ1`, `CJ2`, ...
- **P (Customer Pains):** `P1`, `P2`, ...
- **G (Customer Gains):** `G1`, `G2`, ... — verify gains satisfy the **Non-Redundant Gains Rule** (gains must not be simple opposites of pains).

#### 2b. Value Map (Left Side)

For each feature in `Feature_Set`, assess relevance to this segment and assign:
- **PS (Products & Services):** Features MUST be noun-based (Good: “Analytics dashboard”) and MUST NOT describe effects or outcomes (Invalid: “Time-saving dashboard”). Labels: `PS1`, `PS2`, ...
- **PR (Pain Relievers):** Structure: “[name]: Reduces/eliminates [pain] by [causal mechanism].” At least one PR per PS→Pain connection. Labels: `PR1`, `PR2`, ...
- **GC (Gain Creators):** Structure: “[name]: Enables/increases [gain] by [causal mechanism].” At least one GC per PS→Gain connection. Labels: `GC1`, `GC2`, ...

Not every feature needs to appear in every segment canvas — only include features with a meaningful connection.

#### 2c. Fit Assessment

After mapping, score the fit for this segment:
- **Coverage:** What percentage of the segment's pains and gains are addressed?
- **Gaps:** List any pains or gains with no corresponding PR or GC.
- **Fit Rating:** Strong / Moderate / Weak, with a one-sentence justification.

### Step 3: End-to-End Connection Rules

All connections in the `canvas` data structure **must** follow one of two complete paths:

- **Pain path:** `PS (from_ps) → PR → P (relieves) → CJ (linked_job)`
- **Gain path:** `PS (from_ps) → GC → G (creates) → CJ (linked_job)`

**Shortcut Rule:** Every Pain Reliever must carry both `from_ps` and `relieves`. Every Gain Creator must carry both `from_ps` and `creates`. Every Pain and Gain must carry `linked_job`. No direct PS → CJ connections are permitted.

## 4. Python Visualization

For each segment canvas, generate a PNG using the Python renderer defined in **§ 7. Python Renderer**:

1. Copy the full renderer code from § 7.
2. Fill in the `canvas` data structure with this segment's data.
3. Write it to `vpcanvas_render.py` and run: `python vpcanvas_render.py vpcanvas_[segment_slug].png`
4. Embed the result in the output file as: `![Canvas: Segment Name](vpcanvas_[segment_slug].png)`

## 5. Output Format

Save all canvases to `value-proposition-canvases-output.md`. Each segment gets its own titled section. Generate `vpcanvas_[segment_slug].png` for each segment using the Python renderer in § 7.

---

### Canvas: [Segment Name]

**Fit Rating:** [Strong / Moderate / Weak] — [one-sentence justification]
**Coverage:** [X of Y pains addressed], [X of Y gains addressed]
**Gaps:** [List uncovered pains/gains, or "None"]

---

#### Customer Profile

**Customer Jobs**
| ID | Description | Type |
|----|-------------|------|
| CJ1 | ... | Functional |

**Customer Pains**
| ID | Description |
|----|-------------|
| P1 | ... |

**Customer Gains**
| ID | Description |
|----|-------------|
| G1 | ... |

---

#### Value Map

**Products & Services**
| ID | Feature Name | Description |
|----|-------------|-------------|
| PS1 | ... | ... |

**Pain Relievers**
| ID | How It Relieves | Addresses |
|----|----------------|-----------|
| PR1 | ... | P1 |

**Gain Creators**
| ID | How It Creates Gain | Addresses |
|----|--------------------|-----------| 
| GC1 | ... | G1 |

---

#### Canvas Visualization

![Canvas: [Segment Name]](vpcanvas_[segment_slug].png)

---

*(Repeat for each segment)*

---

### Cross-Segment Fit Summary

| Segment | Fit Rating | Pains Covered | Gains Covered | Key Gap |
|---------|-----------|--------------|--------------|---------|
| [Name] | Strong | 4/5 | 3/4 | G4 unaddressed |

## 6. Guardrails

- Produce one complete canvas per segment — do not merge segments.
- Every connection in the canvas data structure must follow the full path: PS → PR/GC → P/G → CJ. No shortcuts.
- Gains must satisfy the Non-Redundant Gains Rule: they must not be simple opposites of pains.
- Do not include features in a segment canvas unless there is a meaningful, explainable connection.
- Do not compress, omit, or use placeholders — all tables and diagrams must be fully populated.

## 7. Python Renderer

Copy this code, fill in the `canvas` data structure, write it to `vpcanvas_render.py`, and run it.

```python
#!/usr/bin/env python3
"""Value Proposition Canvas renderer — fill in `canvas` below, then run."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import textwrap

# ═══════════════════════════════════════════════════════════════════════════
#  CANVAS DATA — the executing agent fills in all items below before running
# ═══════════════════════════════════════════════════════════════════════════
canvas = {
    "segment": "Segment Name",

    # Left side — Value Map
    "products_services": [
        # noun-based feature names only
        {"id": "PS1", "label": "Feature Name"},
    ],
    "pain_relievers": [
        # from_ps + relieves define the PS → PR → P path
        {"id": "PR1", "label": "Reliever description", "from_ps": "PS1", "relieves": "P1"},
    ],
    "gain_creators": [
        # from_ps + creates define the PS → GC → G path
        {"id": "GC1", "label": "Creator description", "from_ps": "PS1", "creates": "G1"},
    ],

    # Right side — Customer Profile
    "pains": [
        # linked_job completes the P → CJ connection
        {"id": "P1", "label": "Pain description", "linked_job": "CJ1"},
    ],
    "gains": [
        # linked_job completes the G → CJ connection
        {"id": "G1", "label": "Gain description", "linked_job": "CJ1"},
    ],
    "jobs": [
        {"id": "CJ1", "label": "Job description"},
    ],
}
# ═══════════════════════════════════════════════════════════════════════════


NODE_FILL = "#1b365d"
NODE_TEXT = "#ffffff"
BORDER    = "#000000"
NODE_W    = 2.2
NODE_H    = 0.62
ROW_SPC   = 1.05   # vertical distance between node centers
SEC_GAP   = 1.1    # vertical gap between pain and gain sections
PAD       = 0.9    # outer padding
COL_X     = [1.5, 4.4, 7.3, 10.2]   # x-centers: PS | PR/GC | P/G | CJ


def _label(item):
    return textwrap.fill(f"{item['id']}: {item['label']}", width=22)


def _node(ax, x, y, text):
    ax.add_patch(FancyBboxPatch(
        (x - NODE_W / 2, y - NODE_H / 2), NODE_W, NODE_H,
        boxstyle="round,pad=0.06",
        facecolor=NODE_FILL, edgecolor=BORDER, linewidth=1.5, zorder=3,
    ))
    ax.text(x, y, text, ha="center", va="center",
            fontsize=7, color=NODE_TEXT, zorder=4, multialignment="center")


def _box(ax, x1, y1, x2, y2, label=None, lw=2):
    ax.add_patch(Rectangle(
        (x1, y1), x2 - x1, y2 - y1,
        facecolor="none", edgecolor=BORDER, linewidth=lw, zorder=1,
    ))
    if label:
        ax.text((x1 + x2) / 2, y2 + 0.1, label,
                ha="center", va="bottom", fontsize=8,
                fontweight="bold", color=BORDER, zorder=2)


def _arrow(ax, src, dst):
    """Arrow from right edge of src to left edge of dst."""
    ax.annotate(
        "", xy=(dst[0] - NODE_W / 2, dst[1]),
        xytext=(src[0] + NODE_W / 2, src[1]),
        arrowprops=dict(arrowstyle="-|>", color=BORDER, lw=1.1),
        annotation_clip=False, zorder=5,
    )


def render(canvas, output="vpcanvas.png"):
    ps, prs, gcs, pins, gins, jobs = (
        canvas["products_services"], canvas["pain_relievers"],
        canvas["gain_creators"],     canvas["pains"],
        canvas["gains"],             canvas["jobs"],
    )

    pain_rows = max(len(prs), len(pins), 1)
    gain_rows = max(len(gcs), len(gins), 1)

    # y increases upward; gain section at bottom, pain section above it
    gain_bottom_y = PAD
    gain_top_y    = gain_bottom_y + (gain_rows - 1) * ROW_SPC
    pain_bottom_y = gain_top_y + SEC_GAP
    pain_top_y    = pain_bottom_y + (pain_rows - 1) * ROW_SPC
    content_mid   = (gain_bottom_y + pain_top_y) / 2

    pos = {}
    for i, n in enumerate(prs):
        pos[n["id"]] = (COL_X[1], pain_top_y - i * ROW_SPC)
    for i, n in enumerate(gcs):
        pos[n["id"]] = (COL_X[1], gain_top_y - i * ROW_SPC)
    for i, n in enumerate(pins):
        pos[n["id"]] = (COL_X[2], pain_top_y - i * ROW_SPC)
    for i, n in enumerate(gins):
        pos[n["id"]] = (COL_X[2], gain_top_y - i * ROW_SPC)
    for i, n in enumerate(ps):
        y0 = content_mid + (len(ps) - 1) / 2 * ROW_SPC
        pos[n["id"]] = (COL_X[0], y0 - i * ROW_SPC)
    for i, n in enumerate(jobs):
        y0 = content_mid + (len(jobs) - 1) / 2 * ROW_SPC
        pos[n["id"]] = (COL_X[3], y0 - i * ROW_SPC)

    fig_h = pain_top_y + NODE_H / 2 + PAD + 1.4
    fig_w = max(COL_X) + NODE_W / 2 + PAD

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(0, fig_w)
    ax.set_ylim(0, fig_h)
    ax.axis("off")

    ax.text(fig_w / 2, fig_h - 0.45,
            f"Value Proposition Canvas — {canvas['segment']}",
            ha="center", va="top", fontsize=12, fontweight="bold")

    sp = 0.22

    def grp_box(nodes, col):
        ys = [pos[n["id"]][1] for n in nodes if n["id"] in pos]
        if not ys:
            return None
        return (col - NODE_W / 2 - sp, min(ys) - NODE_H / 2 - sp,
                col + NODE_W / 2 + sp, max(ys) + NODE_H / 2 + sp)

    boxes = {
        "Products & Services": grp_box(ps,   COL_X[0]),
        "Pain Relievers":      grp_box(prs,  COL_X[1]),
        "Gain Creators":       grp_box(gcs,  COL_X[1]),
        "Pains":               grp_box(pins, COL_X[2]),
        "Gains":               grp_box(gins, COL_X[2]),
        "Customer Jobs":       grp_box(jobs, COL_X[3]),
    }
    for lbl, b in boxes.items():
        if b:
            _box(ax, *b, label=lbl, lw=1)

    vm_keys = ("Products & Services", "Pain Relievers", "Gain Creators")
    cp_keys = ("Pains", "Gains", "Customer Jobs")
    outer_sp = sp + 0.18
    for keys, lbl in [(vm_keys, "Value Map"), (cp_keys, "Customer Profile")]:
        group = [boxes[k] for k in keys if boxes.get(k)]
        if group:
            _box(ax,
                 min(b[0] for b in group) - outer_sp,
                 min(b[1] for b in group) - outer_sp,
                 max(b[2] for b in group) + outer_sp,
                 max(b[3] for b in group) + outer_sp,
                 label=lbl, lw=2)

    for grp in (ps, prs, gcs, pins, gins, jobs):
        for n in grp:
            if n["id"] in pos:
                _node(ax, *pos[n["id"]], _label(n))

    for pr in prs:
        if pr.get("from_ps") in pos and pr["id"] in pos:
            _arrow(ax, pos[pr["from_ps"]], pos[pr["id"]])
        if pr["id"] in pos and pr.get("relieves") in pos:
            _arrow(ax, pos[pr["id"]], pos[pr["relieves"]])
    for gc in gcs:
        if gc.get("from_ps") in pos and gc["id"] in pos:
            _arrow(ax, pos[gc["from_ps"]], pos[gc["id"]])
        if gc["id"] in pos and gc.get("creates") in pos:
            _arrow(ax, pos[gc["id"]], pos[gc["creates"]])
    for p in pins:
        if p["id"] in pos and p.get("linked_job") in pos:
            _arrow(ax, pos[p["id"]], pos[p["linked_job"]])
    for g in gins:
        if g["id"] in pos and g.get("linked_job") in pos:
            _arrow(ax, pos[g["id"]], pos[g["linked_job"]])

    plt.savefig(output, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved → {output}")


if __name__ == "__main__":
    import sys
    slug = canvas["segment"].lower().replace(" ", "_")
    out  = sys.argv[1] if len(sys.argv) > 1 else f"vpcanvas_{slug}.png"
    render(canvas, out)
```