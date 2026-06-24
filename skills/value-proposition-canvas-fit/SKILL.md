---
name: value-proposition-canvas-fit
description: "Create one Value Proposition Canvas per customer segment by selecting the highest-value features from a coherent feature bundle and mapping them through complete causal chains (PS → PR/GC → P/G → CJ)."
license: MIT
metadata:
  author: jocwulf
  version: 3.1.0
---

# value-proposition-canvas-fit — Multi-Segment Value Proposition Canvas Designer

> Transform a coherent feature bundle into a focused value proposition by selecting the highest-value features and creating one complete Value Proposition Canvas per customer segment with end-to-end flows.

# 1. Skill Purpose

You are a Value Proposition Design expert.

Given:

- customer segment profiles containing Jobs, Pains, and Gains
- monetary valuations of pains and gains
- a coherent bundle of envisioned service features

you must:

1. Select the subset of features with the highest customer value potential.
2. Construct one Value Proposition Canvas per customer segment.
3. Explicitly map causal relationships from Products & Services through Pain Relievers and Gain Creators to customer needs.
4. Assess fit quality at segment level and across segments.

The objective is not maximum feature coverage.

The objective is to identify the smallest coherent set of features capable of delivering the strongest customer value.

# 2. Required Inputs

Request any missing inputs before proceeding.

## Required Input A – Segment_Profiles

Customer segment profiles containing:

- Customer Jobs
- Customer Pains
- Customer Gains
- Pain Values
- Gain Values

Accept:

- output from the jobs-pains-gains skill
- output from pain/gain valuation analysis
- manually provided segment descriptions

Pain and gain valuations should be expressed in monetary terms whenever available.

---

## Required Input B – Feature_Set

A coherent bundle of envisioned features.

Accept:

- output from smart-service-ideation
- manually described features

The Feature_Set may contain significantly more features than will ultimately appear in the Value Proposition Canvas.

# 3. Execution Process

## Step 1 – Input Consolidation

List:

- all customer segments
- all candidate features

Ask the user whether any segments or candidate features should be excluded.

Do not proceed without approval.

---

## Step 2 – Feature Portfolio Selection

### Purpose

The Feature_Set represents a coherent opportunity space.

However, an effective value proposition should focus on the features that create the greatest customer value.

Before building any canvas, identify the most valuable subset of features.

### Step 2a – Candidate Feature Inventory

Assign temporary IDs:

| ID | Candidate Feature |
|------|------|
| FPS1 | ... |
| FPS2 | ... |

(FPS = Feature Portfolio Selection)

List all features from the input bundle.

---

### Step 2b – Feature Assessment

Evaluate every candidate feature against:

#### Economic Impact

Estimate the total customer value potentially influenced by the feature.

Calculate:

```text
Economic Impact =
Σ Pain Values Addressed
+
Σ Gain Values Created
```

Use the monetary valuations contained in the customer profiles.

---

#### Segment Reach

How many relevant customer segments benefit from the feature?

Report:

```text
1 Segment
2 Segments
3 Segments
...
```

---

#### Dependency Leverage

Does the feature enable or strengthen other valuable features?

Assess:

- High: Majority of other features depend on it.
- Medium: Some others depend on it.
- Low: No enablement of other features.

---

### Step 2c – Feature Selection

Select between:

- minimum 6 features
- maximum 10 features

Default target:

- 8 features

Selection should maximize:

- addressed pain and gain value
- cross-segment value creation
- dependency leverage

while minimizing redundancy

---

### Step 2d – Feature Dependency Check

A feature with lower direct economic impact may be retained when it is required to enable higher-value features.

---

### Step 2e – Portfolio Assessment

Produce:

#### Selected Features

| ID | Feature | Key Pains Addressed | Key Gains Created | Economic Impact | Selection Rationale |
|------|------|------|------|------|------|
| PS1 | ... | P1, P3 | G2 | CHF ... | ... |

---

#### Excluded Features

| Feature | Reason Excluded |
|------|------|
| ... | ... |

---

#### Portfolio Quality Assessment

Assess:

- Focus
- Cross-Segment Relevance
- Customer Value Concentration
- Dependency Coherence

Provide:

**Portfolio Rating:** Strong / Moderate / Weak

with a one-sentence explanation.

---

## Step 3 – Per-Segment Canvas Mapping

Perform all remaining steps independently for each segment.

### Step 3a – Customer Profile

#### Customer Jobs

Labels:

- CJ1
- CJ2
- ...

| ID | Description | Type |
|------|------|------|
| CJ1 | ... | Functional |

---

#### Customer Pains

Labels:

- P1
- P2
- ...

| ID | Description | Estimated Annual Value |
|------|------|------|
| P1 | ... | CHF ... |

---

#### Customer Gains

Labels:

- G1
- G2
- ...

| ID | Description | Estimated Annual Value |
|------|------|------|
| G1 | ... | CHF ... |

---

### Step 3b – Value Map

Only utilize features selected during Step 2.

#### Products & Services

Labels:

- PS1
- PS2
- ...

| ID | Feature Name | Description |
|------|------|------|
| PS1 | ... | ... |

---

#### Pain Relievers

Labels:

- PR1
- PR2
- ...

| ID | How It Relieves | Addresses |
|------|------|------|
| PR1 | ... | P1 |

---

#### Gain Creators

Labels:

- GC1
- GC2
- ...

| ID | How It Creates Gain | Addresses |
|------|------|------|
| GC1 | ... | G1 |

---

### Causal Validity Rule

Every Pain Reliever and Gain Creator must specify:

1. Customer Outcome (reduces pain or enables gain)
2. Intermediate Effect with measurable Thresholds
3. Causal Mechanism

Reject:

- circular explanations
- restatements
- unsupported claims

---

## Step 4 – Fit Assessment

Assess each segment independently.

### Coverage

Report:

- X of Y pains addressed
- X of Y gains addressed

---

### Economic Coverage

Calculate and report:

- Total Pain Value Addressed
- Total Pain Value Unaddressed
- Total Gain Value Enabled
- Total Gain Value Not Enabled

Express both absolute values and percentages.

Example:

```text
Pain Value Addressed:
CHF 1.2M of CHF 1.5M (80%)

Gain Value Enabled:
CHF 900k of CHF 1.1M (82%)
```

---

## Step 5 – End-to-End Connection Rules

All value proposition canvas connections must follow one of the following paths.

### Pain Path

```text
PS → PR → P → CJ
```

### Gain Path

```text
PS → GC → G → CJ
```

### Shortcut Rule

Forbidden:

```text
PS → CJ
PS → P
PS → G
PR → CJ
GC → CJ
```

Every relationship must pass through:

- a PR or GC
- a Pain or Gain

before reaching a Customer Job.

# 4. Python Visualization

For each segment canvas, generate a PNG using the Python renderer defined in **§ 7. Python Renderer**:

1. Copy the full renderer code from § 7.
2. Fill in the `canvas` data structure with this segment's data.
3. Write it to `vpcanvas_render.py` and run: `python vpcanvas_render.py vpcanvas_[segment_slug].png`
4. Embed the result in the output file as: `![Canvas: Segment Name](vpcanvas_[segment_slug].png)`

# 5. Output Format

Save all canvases to `value-proposition-canvases-output.md`. Each segment gets its own titled section. Generate `vpcanvas_[segment_slug].png` for each segment using the Python renderer in § 7. Include all content from 3.3 to 3.5.

# 6. Guardrails

## Portfolio Selection Guardrails

- Select 6–10 features before canvas construction.
- Use only selected features in subsequent mapping.
- Prioritize economic value over feature quantity.
- Base feature selection on quantified pain and gain values.
- Justify all excluded features.
- Retain enabling features when dependency relationships require them.

## Mapping Guardrails

- Create one canvas per segment.
- Do not merge segments.
- Every connection must follow:
  PS → PR/GC → P/G → CJ.
- Every PR and GC must satisfy the Causal Validity Rule.
- Maintain conceptual separation between Products & Services, Pain Relievers, and Gain Creators: P&S MUST be noun-based (Good: “Analytics dashboard”) and MUST NOT describe effects or outcomes (Invalid: “Time-saving dashboard”). Pains and gains: Reduces/enables [pain/gain] leading to [intermediate measureable effect] by [causal mechanism].
- Do not include a selected feature in a segment unless a meaningful causal connection exists.

# 7. Python Renderer

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