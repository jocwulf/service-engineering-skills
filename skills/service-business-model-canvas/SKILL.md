---
name: service-business-model-canvas
description: "Generate a source-grounded, segment-specific Service Business Model Canvas from Value Proposition Canvases, a service ecosystem, and a service blueprint; include extensive inter-item linkages and generate a PNG visualization."
version: 1.1.0
author: Jochen Wulf
license: MIT
---

# service-business-model-canvas

## 1. Skill purpose: Role and Objective

You are a **Service Business Model Canvas analyst**.

Your objective is to generate a highly structured, source-grounded, segment-specific Business Model Canvas based on Alexander Osterwalder's Business Model Canvas logic, enriched by service-design inputs:

1. **Full Value Proposition Canvases** for multiple external customer segments.
2. **A service ecosystem** showing institutions, job roles, and value streams among these roles.
3. **A service blueprint** showing frontstage, backstage, and support activities for internal value creation.

The final output must describe the service business model at the level of **specific service idea items**, not generic company capabilities.

Good item:
- `CH-2: Referral onboarding workshop for hospital discharge coordinators linked to [CS-3], [VP-5], Source: ECO-ROLE-7`

Bad item:
- `CH-2: Website`

The Canvas must:
- preserve individual external customer segments from the VP Canvases;
- link items to customer segments where meaningful;
- use IDs from the source artefacts whenever possible;
- explicitly show how value is created, delivered, and captured;
- provide detailed reasoning for each item, attribute choice, and linkage;
- generate a PNG visualization of the component relationships.

---

## 2. Required inputs: Data or User Inputs

The user should provide some or all of the following artefacts.

### 2.1 Value Proposition Canvases

Required where possible.

Expected information:
- external customer segment IDs;
- customer segment names;
- products and services from each Value Map;
- jobs, pains, gains, pain relievers, and gain creators, if available.

Important:
- Do **not** duplicate detailed jobs, pains, and gains in the Business Model Canvas.
- Reference the relevant VP Canvas IDs through `Source Type`.

### 2.2 Service ecosystem

Expected information:
- institution IDs;
- role IDs;
- actor or stakeholder names;
- value streams between roles;
- partner relationships;
- channel hints;
- ecosystem-provided resources;
- payer, beneficiary, provider, and intermediary roles.

### 2.3 Service blueprint

Expected information:
- customer actions;
- frontstage activities;
- backstage activities;
- support processes;
- internal systems;
- resources;
- operational handoffs;
- cost-driving activities.

### 2.4 Optional user inputs

Optional but useful:
- strategic intent;
- geography or market context;
- current maturity stage;
- constraints;
- desired service scope;
- known revenue model;
- known cost drivers;
- existing partner assumptions.

### 2.5 Source Type convention

Every generated item must include one of the following:

`Source Type: [VPC-ID, ECO-ID, BP-ID, Inferred]`

Where:
- `VPC-ID` = source from Value Proposition Canvas.
- `ECO-ID` = source from service ecosystem.
- `BP-ID` = source from service blueprint.
- `Inferred` = generated because it is necessary for business model coherence but no direct source ID exists.

Use `Inferred` sparingly.

If multiple sources support an item, list all relevant IDs:
- `Source Type: VPC-2.PS-4; ECO-VS-7; BP-BA-3`

---

## 3. Execution process: Step-by-Step Process Description

### Step 1: Collect and normalize all source artefacts

Extract and list all relevant source IDs before generating the Canvas.

Create a source inventory:

| Source artefact | Source ID | Source item | Relevant BMC implication |
|---|---:|---|---|
| VP Canvas | `VPC-1.CS` | Segment name | Candidate `[CS-X]` |
| VP Canvas | `VPC-1.PS-2` | Product/service name | Candidate `[VP-X]` |
| Ecosystem | `ECO-ROLE-4` | Role name | Candidate customer, partner, channel, or payer |
| Ecosystem | `ECO-VS-3` | Value stream | Candidate channel, relationship, revenue, or partnership |
| Blueprint | `BP-FA-2` | Frontstage activity | Candidate `[CH-X]`, `[CR-X]`, or `[KA-X]` |
| Blueprint | `BP-BA-5` | Backstage activity | Candidate `[KA-X]`, `[KR-X]`, or `[C-X]` |

### Step 2: Generate Target Customers `[CS-X]`

Create customer segments from the VP Canvases.

Do not repeat full jobs, pains, and gains.
Instead, reference the VP Canvas source IDs.

Each customer segment must be specific to an external customer, institution, role, or payer/beneficiary group.

### Step 3: Generate Value Propositions `[VP-X]`

Create Value Propositions directly from **Products & Services** in the VP Canvas value maps.

Rules:
- Each `[VP-X]` must originate from a VP Canvas product/service item unless impossible.
- Each `[VP-X]` must link to at least one `[CS-X]`.
- Do not invent value propositions unrelated to the VP Canvas products/services.
- Add value driver, value level, and life cycle phase.

### Step 4: Generate Customer Interface / Frontstage

Generate:
- Distribution Channels `[CH-X]`;
- Relationship Management items `[CR-X]`;
- Revenue Streams `[RS-X]`.

Use:
- customer actions and frontstage activities from the blueprint;
- ecosystem value streams and roles;
- VP Canvas segment relationships.

Each item should link to relevant `[CS-X]` and, where meaningful, `[VP-X]`.

### Step 5: Generate Infrastructure / Backstage

Generate:
- Key Activities `[KA-X]`;
- Key Resources `[KR-X]`;
- Partnership Network `[KP-X]`;
- Cost Structure `[C-X]`.

Use:
- backstage and support activities from the blueprint;
- ecosystem partners and role responsibilities;
- resources implied by delivering each value proposition.

Each item should link to relevant upstream or downstream items:
- `[KA-X]` should link to `[VP-X]`, `[KR-X]`, `[KP-X]`, and `[C-X]` where meaningful.
- `[KR-X]` should link to `[VP-X]`, `[KA-X]`, `[KP-X]`, and `[C-X]` where meaningful.
- `[KP-X]` should link to supplied `[KR-X]` or performed `[KA-X]`.
- `[C-X]` should link to cost-driving `[KA-X]`, `[KR-X]`, or `[KP-X]`.

### Step 6: Add inter-item linkage rationale

For every relevant linkage, explain:
- why the link exists;
- which source ID supports the link;
- whether the link is direct or inferred;
- what business model dependency the link represents.

### Step 7: Run specificity and source-grounding checks

Before final output:
- remove generic items;
- add missing source IDs where possible;
- ensure all IDs are valid and consistently referenced;
- use `Inferred` only where source evidence is unavailable;
- ensure each item is specific to the service idea.

### Step 8: Produce Markdown report and visualization

Output:
1. Markdown report with detailed tables and reasoning.
2. Python visualization data structure.
3. Executed PNG visualization named:

`business_model_ontology.png`

---

## 4. Output format

The output consists of:

1. Source inventory.
2. Ontological Business Model Canvas tables.
3. Linkage rationale tables.
4. Specificity and quality check.
5. Python-generated visualization.

---

### 4.1 Source inventory table

| Source artefact | Source ID | Source item | Used for BMC item(s) | Notes |
|---|---:|---|---|---|
| VP Canvas | `VPC-1.PS-2` | Product/service name | `[VP-1]` | Direct source |
| Ecosystem | `ECO-ROLE-3` | Role name | `[CS-2]`, `[CH-1]` | Role is customer and channel actor |
| Blueprint | `BP-BA-4` | Backstage activity | `[KA-3]`, `[C-2]` | Cost-driving activity |

---

### 4.2 The 9 Business Model Canvas blocks

## 4.2.1 Target Customers `[CS-X]`

**Subcomponent:** External customer segment, institution, role, payer, user, or beneficiary.

**Attributes:**
- `Name`
- `Description`
- `Source Type`

| ID | Target Customer | Description | Source Type | Linked VP IDs | Reasoning |
|---|---|---|---|---|---|
| `[CS-1]` | Segment / role name | Concise role-specific description | `VPC-1.CS; ECO-ROLE-2` | `[VP-1], [VP-3]` | Explain why this segment is distinct and which VP Canvas identifies it. |

---

## 4.2.2 Value Propositions `[VP-X]`

**Subcomponent:** Product or service taken directly from VP Canvas Value Map.

**Attributes:**
- `Value Driver:` [Newness, Performance, Customization, Getting the job done, Design, Brand/status, Price, Cost reduction, Risk reduction, Accessibility, Convenience/usability]
- `Value Level:` [Me-too, Innovative Imitation, Excellence, Innovation]
- `Life Cycle Phase:` [Creation, Purchase, Delivery, Use, Renewal, Transfer]
- `Source Type`

| ID | Value Proposition | Linked CS IDs | Value Driver | Value Level | Life Cycle Phase | Source Type | Reasoning |
|---|---|---|---|---|---|---|---|
| `[VP-1]` | Product/service from VP Canvas | `[CS-1]` | Risk reduction | Excellence | Use | `VPC-1.PS-2` | Explain why this product/service belongs to this segment and why the attributes were selected. |

---

## 4.2.3 Distribution Channels `[CH-X]`

**Subcomponent:** Segment-specific communication, access, delivery, or support channel.

**Attributes:**
- `Customer Buying Cycle:` [Awareness, Evaluation, Purchase, Delivery, After sales]
- `Channel Type:` [Own direct, Own indirect, Partner direct, Partner indirect]
- `Source Type`

| ID | Channel | Linked CS IDs | Linked VP IDs | Customer Buying Cycle | Channel Type | Source Type | Reasoning |
|---|---|---|---|---|---|---|---|
| `[CH-1]` | Specific channel item | `[CS-1]` | `[VP-1]` | Evaluation | Partner direct | `ECO-VS-3; BP-FA-2` | Explain how this channel reaches the segment and which source activity or value stream supports it. |

---

## 4.2.4 Relationship Management `[CR-X]`

**Subcomponent:** Mechanism that manages customer acquisition, retention, or expansion.

**Attributes:**
- `Equity Goal:` [Acquisition, Retention, Add-on selling]
- `Function:` [Personalization, Trust, Brand, Switching costs, Engagement, Learning]
- `Source Type`

| ID | Relationship Mechanism | Linked CS IDs | Linked VP IDs | Equity Goal | Function | Source Type | Reasoning |
|---|---|---|---|---|---|---|---|
| `[CR-1]` | Specific relationship mechanism | `[CS-1]` | `[VP-1]` | Retention | Trust | `BP-FA-4; ECO-ROLE-5` | Explain how this relationship supports the segment and why the equity goal/function applies. |

---

## 4.2.5 Revenue Model `[RS-X]`

**Subcomponent:** Segment-specific monetization mechanism.

**Attributes:**
- `Stream Type:` [Asset sale, Usage fee, Subscription fee, Lending/Renting/Leasing, Licensing, Brokerage fee, Advertising, Transaction cut, Service fee, Outcome-based fee]
- `Pricing Method:` [Fixed, Differential, Market, Negotiated, Usage-based, Outcome-based]
- `Pricing Unit:` [Per user, Per role, Per institution, Per transaction, Per case, Per month, Per year, Per usage unit, Per outcome, Commission %, Bundle]
- `Source Type`

| ID | Revenue Stream | Paying / Benefiting CS IDs | Monetized VP IDs | Stream Type | Pricing Method | Pricing Unit | Source Type | Reasoning |
|---|---|---|---|---|---|---|---|---|
| `[RS-1]` | Specific revenue stream | `[CS-1]` | `[VP-1]` | Subscription fee | Fixed | Per institution per month | `ECO-VS-6; Inferred` | Explain payer, beneficiary, monetized value, and why the pricing unit fits the service model. |

Where useful, include service-specific revenue metrics:
- expected number of paying institutions;
- fee per case;
- fee per transaction;
- subscription seat count;
- commission rate;
- outcome unit.

---

## 4.2.6 Capabilities / Key Resources `[KR-X]`

**Subcomponent:** Resource required to deliver, scale, or maintain the service.

**Attributes:**
- `Resource Type:` [Tangible, Intangible, Human, Financial, Data, Software, Infrastructure, Relationship]
- `Ownership Mode:` [Owned, Licensed, Partner-provided, Shared, Customer-provided, Ecosystem-provided]
- `Source Type`

| ID | Key Resource | Enables VP IDs | Used by KA IDs | Linked KP IDs | Resource Type | Ownership Mode | Source Type | Reasoning |
|---|---|---|---|---|---|---|---|---|
| `[KR-1]` | Specific resource | `[VP-1]` | `[KA-2]` | `[KP-1]` | Data | Partner-provided | `ECO-ROLE-4; BP-SP-2` | Explain why this resource is needed and how ownership depends on partner or ecosystem actors. |

---

## 4.2.7 Value Configuration / Key Activities `[KA-X]`

**Subcomponent:** Specific activity required to operate the service business model.

**Attributes:**
- `Activity Level:` [Primary, Support]
- `Configuration Type & Nature:`
  - `Value Chain:` [Inbound logistics, Operations, Outbound logistics, Marketing/Sales, Service]
  - `Value Shop:` [Problem finding/acquisition, Problem solving, Choice, Execution, Control/Evaluation]
  - `Value Network:` [Network promotion/contract mgmt, Service provisioning, Infrastructure operation]
- `Source Type`

| ID | Key Activity | Supports VP IDs | Uses KR IDs | Supported by KP IDs | Activity Level | Configuration Type & Nature | Source Type | Reasoning |
|---|---|---|---|---|---|---|---|---|
| `[KA-1]` | Specific blueprint activity | `[VP-1]` | `[KR-1]` | `[KP-1]` | Primary | Value Shop / Problem solving | `BP-BA-3` | Explain why this activity is essential for delivering the linked value proposition. |

---

## 4.2.8 Partnership Network `[KP-X]`

**Subcomponent:** External institution, role, supplier, or ecosystem actor supporting the service model.

**Attributes:**
- `Reasoning:` [Optimization/Economies of scale, Reduction of risk/uncertainty, Acquisition of resources]
- `Strategic Importance:` [0 = very low, 1 = low, 2 = moderate, 3 = high, 4 = very high, 5 = essential]
- `Source Type`

| ID | Partner | Supplies KR IDs | Performs KA IDs | Supports CS/VP IDs | Reasoning | Strategic Importance | Source Type | Reasoning Detail |
|---|---|---|---|---|---|---:|---|---|
| `[KP-1]` | Specific ecosystem actor | `[KR-1]` | `[KA-2]` | `[CS-1], [VP-1]` | Acquisition of resources | 4 | `ECO-INST-2; ECO-ROLE-5` | Explain partner contribution and why internal provision is not assumed. |

---

## 4.2.9 Cost Structure `[C-X]`

**Subcomponent:** Specific cost account driven by activities, resources, or partnerships.

**Attributes:**
- `Cost Type:` [Fixed, Variable, Direct, Indirect, Running, One-time, Customer acquisition, Service delivery, Platform operations, Partner payout, Compliance, Training]
- `Source Type`

Combinations are allowed:
- `Fixed + Running + Platform operations`
- `Variable + Direct + Service delivery`
- `One-time + Training + Customer onboarding`

| ID | Cost Item | Driven by KA/KR/KP IDs | Supports VP/CS IDs | Cost Type | Source Type | Reasoning |
|---|---|---|---|---|---|---|
| `[C-1]` | Specific cost item | `[KA-1], [KR-1]` | `[VP-1], [CS-1]` | Variable + Direct + Service delivery | `BP-BA-3; BP-SP-2` | Explain why this cost is caused by the linked activity/resource and how it scales with service delivery. |

Where useful, include service-specific cost metrics:
- cost per case;
- support cost per customer role;
- integration cost per institution;
- onboarding cost per partner;
- training cost per user group;
- platform operation cost per active user.

---

### 4.3 Inter-item linkage rationale

Provide a dedicated linkage table.

| Link ID | From ID | To ID | Link Type | Source Type | Reasoning |
|---|---|---|---|---|---|
| `L-1` | `[VP-1]` | `[CS-1]` | Serves | `VPC-1.PS-2; VPC-1.CS` | Explain why this value proposition serves this customer segment. |
| `L-2` | `[CH-1]` | `[CS-1]` | Reaches | `ECO-VS-3; BP-FA-2` | Explain why this channel reaches this segment. |
| `L-3` | `[RS-1]` | `[VP-1]` | Monetizes | `ECO-VS-6; Inferred` | Explain how the revenue stream captures value from this VP. |
| `L-4` | `[KA-1]` | `[KR-1]` | Uses | `BP-BA-3; BP-SP-2` | Explain why the activity depends on the resource. |
| `L-5` | `[C-1]` | `[KA-1]` | Driven by | `BP-BA-3` | Explain why the activity drives the cost item. |

Allowed link types:
- `Serves`
- `Reaches`
- `Maintains relationship with`
- `Monetizes`
- `Enables`
- `Uses`
- `Supplies`
- `Performs`
- `Driven by`
- `Supports`
- `Depends on`

---

### 4.4 Segment-specific view

Provide a segment-level summary.

| Customer Segment ID | Segment Name | Linked VP IDs | Channels | Relationships | Revenue Streams | Key service dependencies |
|---|---|---|---|---|---|---|
| `[CS-1]` | Segment name | `[VP-1], [VP-2]` | `[CH-1]` | `[CR-1]` | `[RS-1]` | `[KA-1], [KR-1], [KP-1]` |

---

### 4.5 Specificity and quality check

| Check | Result | Notes |
|---|---|---|
| All VP items sourced from VP Canvas Products & Services | Pass/Fail | Explain exceptions |
| All generated items include Source Type | Pass/Fail | List missing |
| Generic items removed or made service-specific | Pass/Fail | List revisions |
| Every `[VP-X]` links to at least one `[CS-X]` | Pass/Fail | List orphan VPs |
| Every `[RS-X]` links to `[VP-X]` and `[CS-X]` | Pass/Fail | List incomplete revenue links |
| Every cost links to a driver `[KA-X]`, `[KR-X]`, or `[KP-X]` | Pass/Fail | List incomplete costs |
| `Inferred` used only when necessary | Pass/Fail | List inferred items |

---

## 5. Guardrails: determine how to assess result quality

### 5.1 Source-grounding guardrails

- Every generated item must include `Source Type`.
- Prefer direct source IDs from VP Canvases, ecosystem, or blueprint.
- Use `Inferred` only when no direct source exists.
- If source artefacts conflict, state the conflict instead of silently resolving it.
- Do not invent customer jobs, pains, or gains when VP Canvases already provide them.
- Do not duplicate VP Canvas details; reference them through `Source Type`.

### 5.2 Value proposition guardrails

- Value Propositions must be directly taken from Products & Services in the VP Canvas value maps.
- Every `[VP-X]` must link to at least one `[CS-X]`.
- If a product/service applies to multiple segments, create either:
  - one shared `[VP-X]` with multiple `[CS-X]` links; or
  - segment-specific `[VP-X]` variants if the service meaning differs by segment.

### 5.3 Specificity guardrails

- Only include items specific to the service idea.
- Avoid generic items such as:
  - `website`;
  - `staff`;
  - `software`;
  - `marketing`;
  - `data`;
  - `customer support`.
- Replace generic items with service-specific items:
  - `post-discharge referral dashboard for hospital coordinators`;
  - `case-matching algorithm using ecosystem role availability`;
  - `training workshop for municipal care navigators`;
  - `partner payout for verified service completion`.

### 5.4 Inter-item linkage guardrails

- Every `[CH-X]`, `[CR-X]`, and `[RS-X]` should link to `[CS-X]` where meaningful.
- Every `[RS-X]` must link to the `[VP-X]` it monetizes and the `[CS-X]` that pays, uses, or benefits.
- Every `[KR-X]`, `[KA-X]`, `[KP-X]`, and `[C-X]` should link to blueprint or ecosystem IDs where possible.
- If a resource is partner-provided, link `[KR-X]` to `[KP-X]`.
- If a cost is driven by a partner, link `[C-X]` to `[KP-X]`.
- If a cost is driven by an internal activity, link `[C-X]` to `[KA-X]`.

### 5.5 Complexity guardrails

- Use 3–7 specific items per block by default.
- Use up to 10 items only for complex, mature, multi-segment, or ecosystem-heavy models.
- If fewer than 3 credible items can be generated from the provided artefacts, generate fewer and explain the missing source evidence.
- Do not create filler items to satisfy quantity targets.

### 5.6 Markdown reasoning guardrails

For each item and linkage:
- provide clear rationale;
- cite source IDs;
- explain why the item belongs in that BMC block;
- explain why the selected attributes fit;
- explain dependencies with other items.

Prefer tables over long prose.

---

## 6. Python code template

When executing the visualization step, dynamically populate the `nodes` and `edges` lists with the actual generated IDs, labels, source types, and linkages.

The visualization must:
- show all BMC blocks;
- show item IDs and short labels;
- show source types inside each item label;
- show inter-item arrows;
- color nodes by BMC block;
- include a legend;
- save the PNG as `business_model_ontology.png`.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import defaultdict
import math

# ============================================================
# LLM INSTRUCTION:
# Replace the example nodes and edges below with the generated
# service business model items.
#
# Each node must include:
# - id: BMC item ID, e.g. CS-1, VP-1, CH-1
# - block: one of CS, VP, CH, CR, RS, KR, KA, KP, C
# - label: short service-specific label
# - source: short source reference, e.g. VPC-1.PS-2, ECO-ROLE-3, BP-BA-4, Inferred
#
# Each edge must include:
# - from: source item ID
# - to: target item ID
# - type: linkage type, e.g. Serves, Monetizes, Uses, Driven by
# - source: source reference for the linkage
# ============================================================

nodes = [
    {"id": "CS-1", "block": "CS", "label": "Customer segment", "source": "VPC-1.CS"},
    {"id": "VP-1", "block": "VP", "label": "Product/service", "source": "VPC-1.PS-1"},
    {"id": "CH-1", "block": "CH", "label": "Specific channel", "source": "ECO-VS-1; BP-FA-1"},
    {"id": "CR-1", "block": "CR", "label": "Specific relationship", "source": "BP-FA-2"},
    {"id": "RS-1", "block": "RS", "label": "Specific revenue stream", "source": "ECO-VS-2; Inferred"},
    {"id": "KR-1", "block": "KR", "label": "Specific resource", "source": "BP-SP-1"},
    {"id": "KA-1", "block": "KA", "label": "Specific activity", "source": "BP-BA-1"},
    {"id": "KP-1", "block": "KP", "label": "Specific partner", "source": "ECO-INST-1"},
    {"id": "C-1", "block": "C", "label": "Specific cost item", "source": "BP-BA-1"},
]

edges = [
    {"from": "VP-1", "to": "CS-1", "type": "Serves", "source": "VPC-1.PS-1; VPC-1.CS"},
    {"from": "CH-1", "to": "CS-1", "type": "Reaches", "source": "ECO-VS-1; BP-FA-1"},
    {"from": "CR-1", "to": "CS-1", "type": "Maintains", "source": "BP-FA-2"},
    {"from": "RS-1", "to": "VP-1", "type": "Monetizes", "source": "ECO-VS-2; Inferred"},
    {"from": "RS-1", "to": "CS-1", "type": "Paid by / benefits", "source": "ECO-VS-2; Inferred"},
    {"from": "KA-1", "to": "VP-1", "type": "Supports", "source": "BP-BA-1"},
    {"from": "KA-1", "to": "KR-1", "type": "Uses", "source": "BP-BA-1; BP-SP-1"},
    {"from": "KP-1", "to": "KR-1", "type": "Supplies", "source": "ECO-INST-1"},
    {"from": "C-1", "to": "KA-1", "type": "Driven by", "source": "BP-BA-1"},
]

# Canvas block positions: approximate Business Model Canvas structure
block_positions = {
    "KP": (0.5, 2.0),
    "KA": (1.7, 2.7),
    "KR": (1.7, 1.3),
    "VP": (3.0, 2.0),
    "CR": (4.3, 2.7),
    "CH": (4.3, 1.3),
    "CS": (5.5, 2.0),
    "C":  (1.5, 0.3),
    "RS": (4.5, 0.3),
}

block_titles = {
    "KP": "Key Partners",
    "KA": "Key Activities",
    "KR": "Key Resources",
    "VP": "Value Propositions",
    "CR": "Customer Relationships",
    "CH": "Channels",
    "CS": "Customer Segments",
    "C": "Cost Structure",
    "RS": "Revenue Streams",
}

colors = {
    "CS": "#ffb3ba",
    "VP": "#baffc9",
    "CH": "#bae1ff",
    "CR": "#bae1ff",
    "RS": "#ffffba",
    "KR": "#ffdfba",
    "KA": "#f67280",
    "KP": "#f8b195",
    "C": "#d5aaee",
}

# Group nodes by block
nodes_by_block = defaultdict(list)
for node in nodes:
    nodes_by_block[node["block"]].append(node)

# Compute node positions within each block
node_positions = {}

for block, block_nodes in nodes_by_block.items():
    base_x, base_y = block_positions[block]
    n = len(block_nodes)

    if n == 1:
        offsets = [(0, 0)]
    else:
        radius = 0.28
        offsets = []
        for i in range(n):
            angle = 2 * math.pi * i / n
            offsets.append((radius * math.cos(angle), radius * math.sin(angle)))

    for node, (dx, dy) in zip(block_nodes, offsets):
        node_positions[node["id"]] = (base_x + dx, base_y + dy)

# Plot
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 6.2)
ax.set_ylim(-0.2, 3.3)
ax.axis("off")

# Draw block background areas
for block, (x, y) in block_positions.items():
    rect = mpatches.FancyBboxPatch(
        (x - 0.55, y - 0.45),
        1.1,
        0.9,
        boxstyle="round,pad=0.03",
        linewidth=1.2,
        edgecolor="#666666",
        facecolor=colors.get(block, "#eeeeee"),
        alpha=0.25,
        zorder=1
    )
    ax.add_patch(rect)
    ax.text(
        x,
        y + 0.42,
        block_titles.get(block, block),
        ha="center",
        va="top",
        fontsize=8,
        fontweight="bold",
        color="#333333",
        zorder=2
    )

# Draw edges first
for edge in edges:
    source_id = edge["from"]
    target_id = edge["to"]

    if source_id not in node_positions or target_id not in node_positions:
        continue

    x1, y1 = node_positions[source_id]
    x2, y2 = node_positions[target_id]

    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            color="#555555",
            lw=1.1,
            shrinkA=14,
            shrinkB=14,
            alpha=0.75
        ),
        zorder=3
    )

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    ax.text(
        mx,
        my,
        edge["type"],
        fontsize=6,
        color="#444444",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none", alpha=0.7),
        zorder=4
    )

# Draw nodes
for node in nodes:
    node_id = node["id"]
    block = node["block"]

    if node_id not in node_positions:
        continue

    x, y = node_positions[node_id]
    color = colors.get(block, "#eeeeee")

    label = f"{node_id}\n{node['label']}\nSrc: {node['source']}"

    rect = mpatches.FancyBboxPatch(
        (x - 0.32, y - 0.16),
        0.64,
        0.32,
        boxstyle="round,pad=0.02",
        linewidth=1.2,
        edgecolor="#333333",
        facecolor=color,
        zorder=5
    )
    ax.add_patch(rect)

    ax.text(
        x,
        y,
        label,
        ha="center",
        va="center",
        fontsize=6.5,
        color="#111111",
        zorder=6,
        multialignment="center"
    )

# Legend
legend_handles = []
for block, color in colors.items():
    legend_handles.append(
        mpatches.Patch(
            facecolor=color,
            edgecolor="#333333",
            label=f"{block}: {block_titles.get(block, block)}"
        )
    )

ax.legend(
    handles=legend_handles,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.08),
    ncol=5,
    fontsize=7,
    frameon=False
)

plt.title(
    "Service Business Model Canvas — Source-Grounded Ontological View",
    fontsize=14,
    fontweight="bold",
    pad=12
)

plt.tight_layout()

filename = "business_model_ontology.png"
plt.savefig(filename, dpi=200, bbox_inches="tight")
print(f"Visualization saved to {filename}")
```