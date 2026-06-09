---
name: service-business-model-canvas
description: "Generate a highly structured, segment-specific Business Model Canvas based on Alexander Osterwalder's Business Model Canvas, and generate a PNG visualization of the component relationships."
version: 1.0.0
author: Jochen Wulf
license: MIT
---

# business-model-canvas (Advanced Ontology & Visualization Edition)

## 9 blocks
This skill relies on the exhaustive subcomponents and exact attribute enumerations from the Osterwalder Business Model Canvas.

1. Target Customers [ID: CS-X]
*   **Subcomponent (Criterion):** Demographics, firmographics, and behavior.
*   **Attributes:** `Name`, `Description`.

2. Value Propositions [ID: VP-X] 
*   **Subcomponent (Offering):** The elementary part of the bundle.
*   **Attributes:**
    *   `Reasoning:` [Use, Risk reduction, Effort reduction]
    *   `Value Level:` [Me-too, Innovative Imitation, Excellence, Innovation]
    *   `Price Level:` [Free, Economy, Market, High-end]
    *   `Life Cycle Phase:` [Creation, Purchase, Use, Renewal, Transfer]

3. Distribution Channels [ID: CH-X] -> Links [VP-X] to [CS-X]
*   **Subcomponent (Link):** The specific marketing task/channel role.
*   **Attributes:**
    *   `Customer Buying Cycle:` [Awareness, Evaluation, Purchase, After sales]
    *   `Actor:` [Self, Partner]

4. Relationship Management [ID: CR-X] -> Targets [CS-X]
*   **Subcomponent (Mechanism):** Function accomplished between firm and customer.
*   **Attributes:**
    *   `Customer Equity:` [Acquisition, Retention, Add-on selling]
    *   `Function:` [Personalization, Trust, Brand]

5. Revenue Model [ID: RS-X] -> Monetizes [VP-X] for [CS-X]
*   **Subcomponent (Revenue Stream & Pricing):**
*   **Attributes:**
    *   `Stream Type:` [Selling, Lending, Licensing, Transaction Cut, Advertising]
    *   `Pricing Method:` [Fixed, Differential, Market]
    *   `Percentage:` [% of total revenue]

6. Capabilities (Key Resources) [ID: KR-X] -> Enables [VP-X]
*   **Subcomponent (Resource):** Inputs into the value-creation process.
*   **Attributes:**
    *   `Resource Type:` [Tangible, Intangible, Human, Financial]

7. Value Configuration (Key Activities) [ID: KA-X] -> Uses [KR-X]
*   **Subcomponent (Activity):** Repeatable pattern of action.
*   **Attributes:**
    *   `Activity Level:` [Primary, Support]
    *   `Configuration Type & Nature:` 
        *   *Value Chain:* [Inbound logistics, Operations, Outbound logistics, Marketing/Sales, Service]
        *   *Value Shop:* [Problem finding/acquisition, Problem solving, Choice, Execution, Control/Evaluation]
        *   *Value Network:* [Network promotion/contract mgmt, Service provisioning, Infrastructure operation]

8. Partnership Network [ID: KP-X] -> Supplies [KR-X] / Performs [KA-X]
*   **Subcomponent (Agreement):** Voluntarily initiated cooperative agreement.
*   **Attributes:**
    *   `Reasoning:` [Optimization/Economies of scale, Reduction of risk/uncertainty, Acquisition of resources]
    *   `Strategic Importance:` [Scale 0 = very low -5 = very high]


9. Cost Structure [ID: C-X] -> Driven by [KA-X], [KR-X], [KP-X]
*   **Subcomponent (Account):** Registry of pecuniary transactions.
*   **Attributes:**
    *   `Cost Type:` [Direct costs, Running costs]
    *   `Percentage:` [% of total costs]


## Canvas Generation Process
Step 1: Ingest VPC & Assign IDs
*   Map user input to `[CS-X]` and `[VP-X]`. 

Step 2: Generate Front-Stage & Back-Stage Matrices
*   Generate `[CH-X]`, `[CR-X]`, `[RS-X]` mapping to specific segments and propositions.
*   Generate `[KA-X]`, `[KR-X]`, `[KP-X]`, `[C-X]` selecting *only* from the strict ontological enumerations listed above.

Step 3: Output Markdown Tables
*   Print the structural analysis in clean markdown.
*   Add detailed explanations of the reasoning behind each mapping and attribute selection.

Step 4: Execute Visualization Script
*   Dynamically populate the provided Python template with the generated nodes and edges.
*   Use your Python code execution tool to run the script and generate `business_model_ontology.png`.
*   Present the image to the user.


## Guidelines
*   **Item Specificity:** Only include items specific to a business model idea (good: "Customer Channel: Instagram Launch Campaign") and leave out items that are generic (bad: "Customer Channel: Homepage")
*   **Complexity:** Use at least 5 actionable and specific iteams per block, but do not exceed 10 items per block to maintain clarity.
*   **Strict ID Mapping:** Ensure every component explicitly connects to its relevant counterparts using the ID scheme (e.g., if a new partnership is formed, explicitly state which `[KA-X]` or `[KR-X]` it supports).
*   **Actionable Cost/Revenue:** Do not just say "Software Costs"; say "Direct Cost: AWS Server architecture supporting `[VP-2]`"
*   **Reasoning Transparency:** For each mapping, attribute selection and valuation, provide a clear rationale and core assumptions.

##  Python Visualization Template
When executing Step 4, use the following Python code. Dynamically replace the `nodes` and `edges` dictionaries with the actual IDs and abbreviated labels generated in Step 2.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# LLM INSTRUCTION: Populate these 9 blocks with actual IDs, short labels, linked IDs, and colors.
# Layout follows the standard Business Model Canvas grid (4 columns × 3 rows + bottom strip).
# linked_ids: list the IDs this block connects to — they appear as small text inside the cell.
# Colors: CS=pink, VP=lightgreen, CH/CR=lightblue, RS=lightyellow, KR=peach, KA=salmon, KP=magenta, C=purple

blocks = [
    # (col, row, colspan, rowspan, section_title, id_label, short_label, linked_ids, color)
    (0, 1, 1, 1, "Key Partners",        "KP-1", "Partner Name\n(Resource Acq)",    ["KA-1","KR-1","C-1"],   "#f8b195"),
    (1, 0, 1, 1, "Key Activities",      "KA-1", "Activity Name\n(Value Chain/Ops)", ["KP-1","KR-1","VP-1","C-1"], "#f67280"),
    (1, 2, 1, 1, "Key Resources",       "KR-1", "Resource Name\n(Intangible)",      ["KP-1","KA-1","VP-1","C-1"], "#ffdfba"),
    (2, 1, 1, 1, "Value Propositions",  "VP-1", "Proposition\n(Effort/Economy)",    ["CS-1","CH-1","CR-1","RS-1","KR-1"], "#baffc9"),
    (3, 0, 1, 1, "Customer Relations",  "CR-1", "Relationship\n(Retention/Trust)",  ["CS-1","VP-1"],         "#bae1ff"),
    (3, 2, 1, 1, "Channels",            "CH-1", "Channel\n(Purchase/Partner)",      ["CS-1","VP-1"],         "#bae1ff"),
    (4, 1, 1, 1, "Customer Segments",   "CS-1", "Segment Name\n(Demographic)",      ["VP-1","CH-1","CR-1","RS-1"], "#ffb3ba"),
    (0, 3, 2, 1, "Cost Structure",      "C-1",  "Cost Name\n(Direct/60%)",          ["KP-1","KA-1","KR-1"],  "#d5aaee"),
    (3, 3, 2, 1, "Revenue Streams",     "RS-1", "Revenue Name\n(Selling/Fixed)",    ["CS-1","VP-1"],         "#ffffba"),
]

# Grid geometry
COL_W  = 1.0   # width of one column unit
ROW_H  = 0.8   # height of one row unit
COLS   = 5
ROWS   = 4
FIG_W  = COLS * COL_W * 3.2
FIG_H  = ROWS * ROW_H * 3.2

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, COLS * COL_W)
ax.set_ylim(0, ROWS * ROW_H)
ax.axis("off")

for (col, row, cspan, rspan, section, id_label, short_label, linked_ids, color) in blocks:
    x = col * COL_W
    # row=0 is top; flip y so row 0 appears at top
    y = (ROWS - row - rspan) * ROW_H
    w = cspan * COL_W
    h = rspan * ROW_H

    rect = mpatches.FancyBboxPatch(
        (x + 0.01, y + 0.01), w - 0.02, h - 0.02,
        boxstyle="round,pad=0.02",
        linewidth=1.5, edgecolor="#555555",
        facecolor=color, zorder=2
    )
    ax.add_patch(rect)

    cx = x + w / 2
    cy = y + h / 2

    # Section header (small, top of cell)
    ax.text(cx, y + h - 0.05, section,
            ha="center", va="top", fontsize=7, color="#444444",
            fontstyle="italic", zorder=3)

    # Main ID + label (centre)
    ax.text(cx, cy + 0.04, f"{id_label}\n{short_label}",
            ha="center", va="center", fontsize=9,
            fontweight="bold", color="#111111", zorder=3,
            multialignment="center")

    # Linked IDs (small, bottom of cell)
    if linked_ids:
        link_text = "→ " + "  ".join(linked_ids)
        ax.text(cx, y + 0.05, link_text,
                ha="center", va="bottom", fontsize=6.5,
                color="#555555", zorder=3)

# Vertical divider between left half (cost) and right half (revenue) in bottom row
mid_x = COLS / 2 * COL_W
bottom_y = 0
top_y = ROW_H
ax.plot([mid_x, mid_x], [bottom_y, top_y], color="#888888", linewidth=1, zorder=4)

plt.title("Business Model Canvas — Ontological View", fontsize=14, fontweight="bold", pad=10)
plt.tight_layout()

filename = "business_model_ontology.png"
plt.savefig(filename, dpi=200, bbox_inches="tight")
print(f"Visualization saved to {filename}")
```

## Ontological Business Model Canvas

### 1. The Value Match
| ID | Target Customer (Criterion) | Maps To | Value Proposition (Offering Attributes) |
|---|---|---|---|
| `[CS-1]` | Name (Demographic/Behavioral) | <-> | `[VP-1]` Name (**Reasoning:** Use/Risk/Effort. **Value:** Me-too/Excellence etc. **Price:** Economy/High-end etc. **Life Cycle:** Phase) |

### 2. The Customer Interface (Front-Stage)
| ID | Component | Maps To | Deep Ontological Attributes |
|---|---|---|---|
| `[CH-1]` | Channel | `[CS-1]`, `[VP-1]` | **Cycle:** [Awareness/Evaluation/Purchase/After-sales] <br> **Actor:** [Self/Partner] |
| `[CR-1]` | Relationship | `[CS-1]` | **Equity:** [Acquisition/Retention/Add-on] <br> **Function:** [Personalization/Trust/Brand] |

### 3. Infrastructure Management (Back-Stage)
| ID | Component | Supports | Deep Ontological Attributes |
|---|---|---|---|
| `[KA-1]` | Activity | `[VP-1]`, `[KR-1]` | **Level:** [Primary/Support] <br> **Config/Nature:** [e.g., Value Shop / Problem Solving] |
| `[KR-1]` | Resource | `[KA-1]` | **Type:** [Tangible/Intangible/Human] <br> **Link:** [Fits/Flows/Shared] |
| `[KP-1]` | Partnership | `[KR-1]`, `[KA-1]`| **Reasoning:** [Optimization/Risk/Resource Acq.] <br> **Integration:** [0-5] <br> **Substitutability:** [0-5] |

### 4. Financial Aspects (Revenue Streams & Cost Structure)
| ID | Account | Driven By | Deep Ontological Attributes |
|---|---|---|---|
| `[RS-1]` | Revenue Stream | `[VP-1]`, `[CS-1]` | **Stream Type:** [Selling/Lending/Licensing/Transaction Cut/Advertising] <br> **Pricing Method:** [Fixed/Differential/Market] <br> **Percentage:** [% of total revenue] |
| `[C-1]` | Cost Name | `[KA-1]`, `[KR-1]` | **Cost Type:** [Direct/Running] <br> **Percentage:** [%] |
