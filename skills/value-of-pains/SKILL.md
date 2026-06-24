---
name: value-of-pains
description: "Quantify the baseline economic potential of customer pains and gains (frequency × impact = potential value). Produces the valuation baseline used as input for the value-of-solving-pains skill."
version: 1.1.0
author: jocwulf
license: MIT
---

# The Value of Pains

## 1. Skill Purpose

You are an expert in service innovation and value-based pricing. Your objective is to quantify the **baseline economic potential** associated with customer pains and gains before any solution is implemented. The resulting valuation establishes the economic value at stake and serves as input for downstream solution-value analysis following the approach described in [The Value of Solving Pains](https://arxiv.org/pdf/2412.03130).

---

## 2. Required Inputs

Request any missing inputs before proceeding:

- `Segment_Profiles`: Jobs-Pains-Gains profiles for all relevant customer segments.
  - Preferably use `jobs-pains-gains-output.md` from the `jobs-pains-gains` skill.
  - Alternatively, ask the user to provide customer segments, pains, and gains manually.

---

## 3. Execution Process

Follow the phases in sequence. Do not proceed until the requirements of the current phase are completed.

### PHASE 1: Scope & Segment Selection

1. List all customer segments and their identified pains (`P1`, `P2`, ...) and gains (`G1`, `G2`, ...) from `Segment_Profiles`.
2. Ask the user which segments, pains, and gains are in scope for valuation.
3. Do not continue until the user approves the scope.

---

### Valuation Procedure

For each selected item (Pain or Gain), collect:

#### 1. Frequency ($f_i$)

Annualized occurrence frequency or probability.

Examples:
- Weekly event = 52
- Monthly event = 12
- Quarterly event = 4
- 10% annual risk = 0.1
- Expected once every 5 years = 0.2

#### 2. Impact ($v_i$)

Financial value per occurrence.

Examples:
- Labor costs
- Downtime costs
- Rework expenses
- Warranty expenses
- Revenue uplift
- Cost avoidance
- Margin improvement

---

### Evidence Requirements

For every estimated parameter ($f_i$ and $v_i$):

1. Provide a brief explanation (1–2 sentences) describing the reasoning.
2. Support the estimate using one of the following:
   - User-provided evidence
   - Customer interview evidence
   - Internal company data provided
   - A real public source (title and URL)
3. If no evidence is available, clearly mark as **assumption**.

Never fabricate sources, URLs, statistics, or evidence.

---

### Dual-Perspective Valuation

Evaluate each item separately for Customer and Provider. A financial impact may apply to both parties, only the customer, or only the provider. Record a value of `0` when no meaningful impact exists for a party.

---

### PHASE 2: Pain Valuation

For each pain in scope:

1. Collect and justify:
   - $f_i$ = annualized frequency/risk
   - $v_i$ = financial impact per occurrence

2. Calculate:

$$VP_{pot,i} = f_i \times v_i$$

where $VP_{pot,i}$ = Potential Pain Value. Repeat until all selected pains have been quantified.

---

### PHASE 3: Gain Valuation

For each gain in scope:

1. Collect and justify:
   - $f_i$ = annualized opportunity frequency/probability
   - $v_i$ = financial value per occurrence

2. Calculate:

$$VG_{pot,i} = f_i \times v_i$$

where $VG_{pot,i}$ = Potential Gain Value. Repeat until all selected gains have been quantified.

---

### PHASE 3b: Double-Counting Review

Before generating final outputs, identify potential economic double-counting.

#### Check Type 1: Pain–Gain Duplication

Remove a gain if it largely describes the absence or reversal of an already-valued pain **and** both valuations use the same underlying cash flow. Flag a gain as `pain-gain-duplication` if there is partial overlap with pain cash flow.

Example: Pain = "Unplanned downtime" / Gain = "No unplanned downtime", both valued via lost production hours.

#### Check Type 2: Cross-Segment/Role Duplication

Flag items where the same economic consequence is counted multiple times across customer segments or roles as `cross-segment-duplication`.

Examples:
- The same downtime loss attributed independently to two segment profiles.
- Machine Operator and Plant Manager both assigned the exact same machine-downtime cost.

---

## 4. Output Format

After all phases have been completed, produce the following outputs.

### 1. Markdown Report

File: `value_of_pains_report.md`

Include:

#### Methodology

- Definitions of all variables
- Calculation formulas
- Assumptions and evidence rules

#### Summary Table

| Item # | Description | Type | Agent | Frequency ($f_i$) | Impact ($v_i$) | Annual Potential Value | Source(s) | Duplication Type | Duplication Item #s |
|--------|-------------|------|-------|-------------------|----------------|----------------------|-----------|-----------------|---------------------|
|        |             |      |       |                   |                |                      |           |                 |                     |

#### Detailed Breakdown

For every pain and gain:
- Description, Agent, Frequency explanation, Impact explanation, Supporting evidence, Calculation

#### Double-Counting Review

Document flagged items, resolution decisions, and adjustments made.

#### Aggregate Results

- Total Pain Value (Customer)
- Total Pain Value (Provider)
- Total Gain Value (Customer)
- Total Gain Value (Provider)

---

### 2. CSV Export

File: `value_of_pains.csv`

Columns:

```text
Item ID,
Type,
Description,
Agent,
Frequency (f_i),
Impact (v_i),
Potential Value (Annual)
Duplication Type 
Duplication Item #s 
```

---

### 3. Visualization

Create a bar chart using the Python Visualization Template from Section 6 (pains in red/coral, gains in green/teal, values labeled on bars). Save as `value_of_pains.png`. Run the script after generating the dataset.

---

## 5. Guardrails

- **Mathematical Correctness:** All values must be annualized. Validate units and time horizons. Guarantee $\text{Potential Value} = f_i \times v_i$ for every item.
- **Completeness:** Quantify all approved pains and gains. Evaluate Customer and Provider impacts separately; record `0` when a party has no relevant impact.
- **Groundedness:** Never use unsupported numbers. Every parameter must include rationale and evidence or source. Mark as "assumption" if no evidence is available. Do not fabricate data.
- **Non-Redundancy:** Eliminate economic double-counting across both duplication types (Pain–Gain and Cross-Segment/Role). Gains must represent additive value, not the financial reversal of an already-quantified pain.
- **Transparency:** Clearly distinguish evidence, assumptions, user-provided estimates, and calculated values. Maintain full traceability from source inputs to final valuation results.

---

## 6. Python Visualization Template

```python
!pip install matplotlib
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

item_ids = []
types = []
descriptions = []
agents = []
potential_values = []

with open("value_of_pains.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        item_ids.append(row["Item ID"])
        types.append(row["Type (Pain/Gain)"])
        descriptions.append(row["Description"])
        agents.append(row["Agent (Customer/Provider)"])
        potential_values.append(float(row["Potential Value (Annual)"]))

colors = [
    "#e07070" if t.strip().lower() == "pain" else "#5cb85c"
    for t in types
]
edge_colors = [
    "#a03030" if t.strip().lower() == "pain" else "#2d7a2d"
    for t in types
]

short_labels = [
    f"{item_ids[i]}\n({agents[i][:4]})"
    for i in range(len(item_ids))
]

fig, ax = plt.subplots(figsize=(max(10, len(item_ids) * 1.3), 7))

x = range(len(item_ids))
bar_width = 0.55

bars = ax.bar(
    list(x),
    potential_values,
    width=bar_width,
    color=colors,
    edgecolor=edge_colors,
    linewidth=1.2,
    zorder=3,
)

for bar, val in zip(bars, potential_values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + max(potential_values) * 0.015,
        f"{int(val):,} €",
        ha="center",
        va="bottom",
        fontsize=8.5,
        fontweight="bold",
        color="#333333",
    )

ax.set_xticks(list(x))
ax.set_xticklabels(short_labels, fontsize=9)
ax.set_ylabel("Annual Potential Value (€)", fontsize=11)
ax.set_title(
    "Value of Pains & Gains — Baseline Potential Values\n"
    "Frequency × Impact per Item",
    fontsize=12,
    fontweight="bold",
    pad=14,
)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{int(v):,} €"))
ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="#e07070", edgecolor="#a03030", label="Pain ($VP_{pot}$)"),
    Patch(facecolor="#5cb85c", edgecolor="#2d7a2d", label="Gain ($VG_{pot}$)"),
]
ax.legend(handles=legend_elements, fontsize=10, loc="upper right")

total_pain = sum(v for v, t in zip(potential_values, types) if t.strip().lower() == "pain")
total_gain = sum(v for v, t in zip(potential_values, types) if t.strip().lower() == "gain")
total = total_pain + total_gain

ax.annotate(
    f"Total Pain: {total_pain:,.0f} €\nTotal Gain: {total_gain:,.0f} €\nTotal: {total:,.0f} €",
    xy=(0.98, 0.97),
    xycoords="axes fraction",
    ha="right",
    va="top",
    fontsize=10,
    fontweight="bold",
    color="#1b365d",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5f5f5", edgecolor="#555555", linewidth=1.2),
)

plt.tight_layout()
plt.savefig("value_of_pains.png", dpi=150, bbox_inches="tight")
print(f"Chart saved. Total Pain Potential: {total_pain:,.0f} €  |  Total Gain Potential: {total_gain:,.0f} €  |  Total: {total:,.0f} €")
```
