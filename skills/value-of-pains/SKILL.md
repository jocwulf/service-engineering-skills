---
name: value-of-pains
description: "Quantify the baseline economic potential of customer pains and gains (frequency × impact = potential value). Produces the pain/gain value baseline used as input for the value-of-solving-pains skill."
version: 1.0.0
author: jocwulf
license: MIT
---

# The Value of Pains

You are an expert in service innovation and value-based pricing. Your goal is to quantify the **baseline economic potential** of customer pains and gains — that is, how much value is at stake before any service solution is applied. This follows the analytical approach from [The Value of Solving Pains](https://arxiv.org/pdf/2412.03130).

This skill produces a **pain/gain value baseline** used as direct input for the `value-of-solving-pains` skill.

## Required Inputs

Ask for any missing inputs before proceeding:

- `Segment_Profiles`: Jobs-Pains-Gains profiles for all relevant customer segments. Accept output from the `jobs-pains-gains` skill directly, or ask the user to describe the customer segment's pains and gains manually.

## Execution Phases

Strictly follow these sequential phases. **Do not move to the next phase until the user has provided the necessary information.**

### PHASE 1: Scope & Segment Selection

1. List all customer segments and their labelled pains (`P1`, `P2`, ...) and gains (`G1`, `G2`, ...) from `Segment_Profiles`.
2. Ask the user which segments, pains, and gains are in scope for this valuation exercise. Do NOT proceed without user approval.

### PHASE 2: Quantify Pains

For each **pain** in scope, interview the user to capture the following, **one pain at a time**:

1. **$f_i$ (Frequency)**: How often the pain occurs per year (e.g., 52 = once per week, 12 = monthly).
2. **$v_i$ (Impact)**: Negative financial impact per occurrence in € or $ (e.g., lost labor, downtime cost, rework expense, warranty cost).

Cover both the **Customer** and **Provider** perspective where relevant — a pain may carry financial consequences for both parties (e.g., a machine breakdown costs the customer production time and the provider a field service visit).

For **each parameter** ($f_i$, $v_i$), you must:
- Provide a brief **assumption explanation** (1–2 sentences describing the reasoning behind the chosen value).
- If the user provides no reasoning, cite at least one **internet source** (title + URL) that substantiates the assumption. Use web search to find real, publicly accessible sources (industry benchmarks, academic papers, analyst reports, government statistics). Do not fabricate URLs.

Calculate **Potential Pain Value ($VP_{pot,i}$)**:

$$VP_{pot,i} = f_i \times v_i$$

### PHASE 3: Quantify Gains

For each **gain** in scope, interview the user to capture the following, **one gain at a time**:

1. **$f_i$ (Frequency)**: How often the opportunity to realize this gain occurs per year.
2. **$v_i$ (Value)**: Positive financial value per occurrence if the gain is fully achieved (e.g., revenue uplift, cost avoidance, hours saved × hourly rate, margin improvement).

Cover both the **Customer** and **Provider** perspective where relevant.

Apply the same assumption/source requirement as in Phase 2.

Calculate **Potential Gain Value ($VG_{pot,i}$)**:

$$VG_{pot,i} = f_i \times v_i$$

### PHASE 3b: Pain–Gain Redundancy Check

Before producing outputs, scan all quantified pains and gains for **economic double-counting**. A redundancy exists when a gain's financial value is already captured by a pain — i.e., the gain is framed as the absence or reversal of a pain rather than a genuinely additive positive outcome.

**Detection rule**: Flag a gain $G_j$ as redundant with pain $P_i$ if:
- Their descriptions refer to the same underlying event or state (e.g., G1 = "no more unplanned downtime" and P3 = "unplanned downtime"), **and**
- The $v_i$ values were estimated using the same cash flow (e.g., both use lost production hours as the basis).

For each flagged pair, present it to the user with a short explanation and ask them to resolve it by choosing one of:
1. **Keep the pain, remove the gain valuation** — the pain already quantifies the full economic stake.
2. **Keep both, adjust the gain** — confirm that the gain represents additional value beyond pain removal (e.g., improved scheduling capability that generates new revenue, not just avoided downtime cost) and revise $v_i$ accordingly.
3. **Merge into a single item** — replace both with one entry that captures the complete economic effect without duplication.

Do NOT proceed to Phase 4 until all flagged pairs are resolved. Record the resolution decision for each pair in the report.

### PHASE 4: Summary & Outputs

Present the full baseline using the table format from the Reference Example below.

Then save the following files:

1. **Markdown report** (`value_of_pains_report.md`) containing:
   - Methodology section (formulas and parameter definitions).
   - Summary table of all pains and gains with their metrics and potential values.
   - Detailed item-by-item breakdown with assumption explanations and source citations for every parameter.
   - Total potential value summary.

2. **CSV file** (`value_of_pains.csv`) with columns:
   `Item ID, Type (Pain/Gain), Description, Agent (Customer/Provider), Frequency (f_i), Impact (v_i), Potential Value (Annual)`

3. **Bar chart** using a Python script (`value_of_pains.py`) that reads the CSV and plots all items' Potential Values as a labeled bar chart (pains in red/coral, gains in green/teal), saving output as `value_of_pains.png`. Run the script after writing it.

---

## Output Formatting & Reference Example

**Scenario**: An IIoT service provider evaluating smart services for a machine operator.

| Item # | Description | Type | Agent | Freq. ($f_i$) | Impact ($v_i$) | Potential Value (Annual) |
|---|---|---|---|---|---|---|
| **P1** | Missing info about current job | Pain | Customer | 25 | 50 € | 1'250 € |
| | *Same pain* | Pain | Provider | 25 | 25 € | 625 € |
| **P2** | Low machine performance due to worn parts | Pain | Customer | 50 | 100 € | 5'000 € |
| **P3** | Machine breakdowns | Pain | Customer | 6 | 600 € | 3'600 € |
| | *Same pain* | Pain | Provider | 6 | 1'000 € | 6'000 € |
| **P4** | Cannot bill recurring revenue due to missing IT | Pain | Customer | 12 | 150 € | 1'800 € |
| | *Same pain* | Pain | Provider | 12 | 100 € | 1'200 € |
| **G1** | Predictable maintenance windows enabling production scheduling | Gain | Customer | 12 | 200 € | 2'400 € |
| **G2** | Recurring revenue via subscription billing | Gain | Provider | 12 | 150 € | 1'800 € |

**Total Annual Potential Value Summary**:
- **Total Customer Pain Potential**: 11'650 €
- **Total Provider Pain Potential**: 7'825 €
- **Total Customer Gain Potential**: 2'400 €
- **Total Provider Gain Potential**: 1'800 €
