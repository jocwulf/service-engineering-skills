---
name: value-of-solving-pains
description: "Calculate the effective economic value delivered per smart service bundle by applying alleviation and gain-achievement factors (ω_i) to the pain/gain baseline. Produces value-based pricing recommendations per service."
version: 2.0.0
author: jocwulf
license: MIT
---

# The Value of Solving Pains

## 1. Skill Purpose

You are an expert in service innovation and value-based pricing. Your goal is to calculate the **effective economic value created by each proposed service** by applying alleviation and gain-achievement factors to a quantified pain/gain baseline, following [The Value of Solving Pains](https://arxiv.org/pdf/2412.03130).

## 2. Required Inputs

Ask for any missing inputs before proceeding:

- `Pain_Gain_Baseline`: Quantified potential values ($VP_{pot,i}$, $VG_{pot,i}$) for all pains and gains, including frequency ($f_i$) and impact ($v_i$). Accept output from the `value-of-pains` skill directly, or ask the user to provide these values manually.
- `VPC_Fit`: Value Proposition Canvases mapping features to pains (via Pain Relievers, PR) and gains (via Gain Creators, GC). Accept output from the `value-proposition-canvas-fit` skill.
- A specifification of the products and services from the Value Proposition Canvases to be covered.

## 3. Execution Process

Strictly follow these sequential phases. **Do not move to the next phase until the user has confirmed the current one.**

### PHASE 1: Input Alignment & Cross-Bundle Redundancy Check

1. List all selected products and services from the specified Value Proposition Canvases.
2. For each product and servce, identify which pains and gains it addresses by cross-referencing the PR-to-Pain and GC-to-Gain connections in `VPC_Fit`.
3. **Flag shared items**: Identify every pain or gain that appears in more than one bundle and mark it with a warning. These shared items must not be double-counted.
5. Present the full product&service-to-pain/gain mapping, including flagged shared items, to the user. Ask for confirmation or corrections before proceeding.

### PHASE 2: Alleviation & Achievement Factors

For each product and service, and for **each pain or gain it addresses**, interview the user to determine:

- **$\omega_i$ (Alleviation / Achievement Factor)**: A value between 0.0 and 1.0 representing how effectively this specific service:
  - **Pains**: reduces or eliminates the pain (0 = no relief, 1 = fully eliminated).
  - **Gains**: enables or achieves the gain (0 = not enabled, 1 = fully achieved).

For **each $\omega_i$**, you must:
- Provide a brief **assumption explanation** (1-2 sentences describing the reasoning).
- If the user provides no reasoning, cite either a user interview statement from the provided data or at least one **internet source** (title + URL) substantiating the assumption. Use web search to find real, publicly accessible sources. Do not fabricate statements or URLs.

Calculate for each addressed item:
- **Effective Pain Value ($VC_{C,i}$)**: `$VC_{C,i} = \omega_i \times VP_{pot,i}$`
- **Effective Gain Value ($VG_{C,i}$)**: `$VG_{C,i} = \omega_i \times VG_{pot,i}$`

### PHASE 3: Economic Value per Bundle

For each product and service, calculate:

1. **Total Customer Effective Value ($V_C^{p&s}$)**: Sum of all Customer $VC_{C,i}$ and $VG_{C,i}$ for this product and service.
2. **Total Provider Effective Value**: Sum of all Provider $VC_{C,i}$ and $VG_{C,i}$ (if applicable).
3. Present a per-p&s summary table in the format shown in the Reference Example below.

### PHASE 3b: Pain or Gain Deduplication

For each pain or gain that appears in more than one product and service, determine a single **combined alleviation factor $\omega_i^{combined}$** (capped at 1.0) instead of summing the individual $\omega_i$ values. Use the appropriate rule based on how the mechanisms interact:

- **Overlapping mechanisms** (bundles address the same root cause in similar ways): `$\omega_i^{combined} = \max(\omega_{i,k})$` across all bundles $k$ that address item $i$.
- **Independent/complementary mechanisms** (bundles tackle different aspects of the same pain/gain): `$\omega_i^{combined} = 1 - \prod_k (1 - \omega_{i,k})$`, capped at 1.0.

For each flagged shared item, ask the user which rule applies and confirm the resulting $\omega_i^{combined}$. Then:
- Assign the shared item (with $\omega_i^{combined}$) to one bundle as its **primary owner**.
- Remove that item's effective value from all other products and services that listed it.
- The portfolio-level effective value for this item equals $\omega_i^{combined} \times VP_{pot,i}$ (counted exactly once).

Record each deduplication decision and the chosen rule in the report.

### PHASE 4: Cross-Product/Service Comparison & Outputs

1. Present all products and services side-by-side in the corss-product/service comparison table. Add a **Portfolio Total** row that sums deduplicated values — never sum a shared item's effective value more than once.
2. Save the following files:

   - **Markdown report** (`value_of_solving_pains_report.md`) containing:
     - Methodology section (formulas and parameter definitions).
     - Per-product/service summary tables with $f_i$, $v_i$, $\omega_i$, and effective values.
     - Detailed item-by-item breakdown with assumption explanations and source citations.
     - Cross-product/service comparison and total value summary.

   - **CSV file** (`value_of_solving_pains.csv`) with columns:
     `Product/Service, Item ID, Type (Pain/Gain), Description, Agent, Frequency (f_i), Impact (v_i), Alleviation (omega_i), Potential Value (Annual), Effective Value (Annual)`

   - **Bar chart** using a Python script (`value_of_solving_pains.py`) that reads the CSV and plots effective values grouped by bundle as a labeled bar chart, saving output as `value_of_solving_pains.png`. Run the script after writing it.

---

## 5. Output Formatting & Reference Example

**Scenario**: Two smart service bundles evaluated for a machine operator.

### Per-Bundle Summary Table

| Item # | Description | Agent | Freq. ($f_i$) | Impact ($v_i$) | Alleviation ($\omega_i$) | Effective Value (Annual) |
|---|---|---|---|---|---|---|
| **P1** | Missing info about current job | Customer | 25 | 50 EUR | 0.8 | 1'000 EUR |
| | *Same pain* | Provider | 25 | 25 EUR | 0.8 | 500 EUR |
| **P3** | Machine breakdowns | Customer | 6 | 600 EUR | 0.7 | 2'520 EUR |
| | *Same pain* | Provider | 6 | 1'000 EUR | 0.7 | 4'200 EUR |
| **G1** | Predictable maintenance windows | Customer | 12 | 200 EUR | 0.8 | 1'920 EUR |

### Cross-Bundle Comparison (Compare mode — bundles as alternatives)

| Bundle | Total Customer $V_C$ | Total Provider Savings | Target $V_P$ | Total Economic $V_{Economic}$ |
|---|---|---|---|---|
| Bundle 1: Predictive Asset Health | 7'780 EUR | 5'300 EUR | 3'890 EUR | 11'670 EUR |
| Bundle 2: Digital Service Portal | 4'200 EUR | 1'800 EUR | 2'100 EUR | 6'300 EUR |

### Cross-Bundle Comparison (Combined mode — shared items deduplicated)

| Bundle | Total Customer $V_C$ | Notes |
|---|---|---|
| Bundle 1: Predictive Asset Health | 7'780 EUR | Owns P3 (combined $\omega$ = 0.85) |
| Bundle 2: Digital Service Portal | 2'280 EUR | P3 removed (assigned to Bundle 1) |
| **Portfolio Total** | **10'060 EUR** | P3 counted once at $\omega^{combined}$ = 0.85 |

## 6. Guardrails

### 6.2 Mathematical Correctness
- Use the defined formulas only:
  - `VP_pot,i = f_i × v_i`
  - `VG_pot,i = f_i × v_i`
  - `VC_C,i = ω_i × VP_pot,i`
  - `VG_C,i = ω_i × VG_pot,i`
- Ensure every `ω_i` is numeric and within `[0,1]`.
- Annualize all values consistently before comparison or aggregation.
- Bundle totals must exactly equal the sum of their item-level effective values.
- Portfolio totals must reconcile exactly after deduplication.
- Keep full precision internally; round only for presentation.

### 6.3 Overlap Calculation Correctness
- Explicitly flag every pain or gain that appears in more than one bundle.
- Never double-count shared items at portfolio level.
- For each shared item, apply exactly one rule:
  - overlapping mechanisms: `ω_i^combined = max(ω_i,k)`
  - complementary mechanisms: `ω_i^combined = 1 - ∏_k (1 - ω_i,k)`
- Cap `ω_i^combined` at `1.0`.
- Assign one primary owner bundle to each shared item.
- Remove duplicate value from all non-owner bundles.
- Record the selected rule, combined factor, and ownership decision.

### 6.4 Strength of Reasoning
- Every `ω_i` must include a brief, specific rationale.
- The rationale must explain how the service mechanism affects the pain/gain and why the chosen level is plausible.
- Include key assumptions, constraints, or limiting conditions where relevant.
- Avoid vague or generic explanations.
- If confidence is limited, state the uncertainty explicitly.

### 6.5 Evidence Strength
- Support each `ω_i` with at least one credible and relevant source whenever possible.
- Acceptable evidence includes customer interviews, operational data, pilots, internal documentation, or externally verifiable publications.
- Never fabricate evidence, quotes, titles, or URLs.
- If no evidence is available, label the factor explicitly as an assumption.
- Do not present weak or indirect evidence as strong validation.

## 7. Python Template Script for Bar Chart Generation

```python
!pip install matplotlib
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

pain_ids = []
pain_labels = []
effective_values = []
potential_values = []

with open("value_of_solving_pains.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pain_ids.append(row["Pain ID"])
        pain_labels.append(row["Pain Description"])
        effective_values.append(float(row["Effective Value (Annual)"]))
        potential_values.append(float(row["Potential Value (Annual)"]))

short_labels = [
    "P1\nSync Rework",
    "P2\nPitch Rejection",
    "P3\nCollab Friction",
    "P4\nAnalysis Paralysis",
    "P5\nProductivity",
    "P6\nBlindspots",
    "P7\nNo Ext. View",
    "P8\nCapacity",
]

fig, ax = plt.subplots(figsize=(13, 7))

x = range(len(pain_ids))
bar_width = 0.38

bars_pot = ax.bar(
    [i - bar_width / 2 for i in x],
    potential_values,
    width=bar_width,
    color="#c8d8e8",
    edgecolor="#4a7aab",
    linewidth=1.2,
    label="Potential Value ($VC_{pot}$)",
    zorder=3,
)
bars_eff = ax.bar(
    [i + bar_width / 2 for i in x],
    effective_values,
    width=bar_width,
    color="#1b365d",
    edgecolor="#0d1f38",
    linewidth=1.2,
    label="Effective Value ($VC_{C}$)",
    zorder=3,
)

for bar, val in zip(bars_eff, effective_values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 250,
        f"{int(val):,} €",
        ha="center",
        va="bottom",
        fontsize=8.5,
        fontweight="bold",
        color="#1b365d",
    )

ax.set_xticks(list(x))
ax.set_xticklabels(short_labels, fontsize=9)
ax.set_ylabel("Annual Value (€)", fontsize=11)
ax.set_title(
    "Value of Solving Pains — Skills Collection for Service Engineering\n"
    "Customer Segment: Corporate Product Managers & Cross-Functional Innovation Teams",
    fontsize=12,
    fontweight="bold",
    pad=14,
)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{int(v):,} €"))
ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(fontsize=10, loc="upper left")

total_vc = sum(effective_values)
ax.annotate(
    f"Total $V_C$ = {total_vc:,.0f} €",
    xy=(0.98, 0.97),
    xycoords="axes fraction",
    ha="right",
    va="top",
    fontsize=11,
    fontweight="bold",
    color="#1b365d",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#e8f0f8", edgecolor="#1b365d", linewidth=1.2),
)

plt.tight_layout()
plt.savefig("value_of_solving_pains.png", dpi=150, bbox_inches="tight")
print(f"Chart saved. Total Customer Value (V_C): {total_vc:,.0f} €")
```
