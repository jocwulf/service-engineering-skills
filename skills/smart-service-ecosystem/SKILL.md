---
name: service-ecosystem
description: "Derive a complete service ecosystem (roles, institutions, and value flows) from customer jobs-pains-gains outputs, positioning the customer institution at the center and mapping all direct and indirect contributors to value creation."
license: MIT
metadata:
  author: jocwulf
  version: 1.0.0
---

# service-ecosystem — Service Ecosystem Modeling Skill

> Design a structured service ecosystem from a service concept making all value exchanges explicit across institutions.

---

## 1. Skill Purpose

You are a service design and systems thinking expert. Your task is to construct a **service ecosystem model** that captures how value is co-created across multiple institutions based on value proposition canvases for multiple segments targeted.

Input is the output of the `value-proposition-canvas-fit` skill (multi-segment canvases with mapped features, pains, and gains).

Output is a **fully specified service ecosystem** including:
- Roles (nodes)
- Institutions (clusters of roles)
- Explicit value flows (links between roles)

---

## 2. Required Input

### Primary Input
- `Value_Proposition_Canvas_Output` (mandatory)
  - All segment canvases
  - Jobs, Pains, Gains
  - Products & Services (features)
  - Pain Relievers / Gain Creators

### Optional Input
- Domain description (if not clear from canvases)

---

## 3. Execution Process

### Step 1: Domain & Customer Core Identification

1. Identify the **primary customer institution**:
   - Represents the focal customer segment(s)
   - Must be modeled as an institution with at least one role (e.g., "User", "Buyer", "Operator")

2. Extract:
   - Core jobs
   - Most critical pains/gains
   - Core features addressing them

3. Define the **central value creation logic**:
   - What is the service fundamentally enabling?

---

### Step 2: Institution Identification

Identify all institutions that directly or indirectly contribute to value creation.

#### Categories to cover (mandatory if relevant):
- Customer institution (center)
- Service provider(s)
- Technology/platform providers
- Suppliers / upstream providers
- Complementors / partners
- Payment/financial actors
- Regulators / government
- Infrastructure providers
- Support / service operators (e.g., maintenance, support)
- Competitors
- Customer's customers (if B2B2C)
---

### Step 3: Role Definition

Within each institution, define **roles** as nodes.

Rules for roles:
- Each role must:
  - Provide at least one value flow
  - Receive at least one value flow
- Roles must represent job roles humans execute (good: "Field Technician", "Service Agent") and not technical components (bad: "Database", "API") or vague entities (bad: "System", "Platform").

---

### Step 4: Value Flow Modeling

Define **directed value flows** between roles.

#### Types of value flows (must classify each):
- Functional (e.g., service delivery, data exchange)
- Financial (e.g., payments, subscriptions)
- Social/Emotional (e.g., trust, reputation, satisfaction)
- Environmental (e.g., emissions reduction, resource use)

---

### Step 5: Ecosystem Structuring

#### Use a mermaid graph (structure see section 6 below) with institutions as subgraphs and roles as nodes.
- Subgraph = Institution
- Node = Role
- Edge = Value flow (labeled)

#### Positioning
- Customer institution must be:
  - Central
- Other institutions:
  - Positioned closer if they provide direct/high value
  - Positioned farther if indirect/supporting

---

### Step 6: Output Construction

- Adapt and run the python script below with mermaid code to produce the ecosystem graph.
- Produce markdown report `serice-ecosystem-output.md` with output format described in Section 4.

---

## 4. Output Format

### 4.1 Ecosystem Overview

- Domain: [Name]
- Central Value Logic: [1–2 sentences]

---

### 4.2 Institutions & Roles

For each institution:

#### Institution: [Name]
- Description: [Short description]

**Roles:**
| Role ID | Role Name | Description |
|--------|-----------|-------------|
| R1 | ... | ... |

---

### 4.3 Value Flows

| From Role | To Role | Flow Description | Type | Explanation of Relevance for Service | 
|----------|--------|------------------|------|------------------|
| R1 | R2 | €9.99 monthly subscription for premium access | Financial | Financial transaction primary incentive for service provision 

---

## 5. Guardrails

1. **Value flow specificity**: value flows must be specific to the service concept and its features, not generic or vague.
   - GOOD: "Monthly subscription €9.99"
   - BAD: "Payment"
   - GOOD: "Real-time usage data via API"
   - BAD: "Data"

2. **Actor relevance and completeneness**: Model all actors but only actors that directly or indirectly affect or affected by service design or provisioning.

3. **Bidirectional participation rule**:
   - Each value flow must have at least one sender and one receiver role.
   - Every role must both send and receive value.

4. **Institution design**: Each institution must represent a legal entity and include at least one role.

## 6. Python mermaid rendering script

```python
#!/usr/bin/env python3
"""Render the service ecosystem Mermaid diagram to a high-resolution PNG.

Rendered locally via mmdc (mermaid-js CLI) at 3× scale.

Paste the MERMAID_CHART value, then run:
    python service-ecosystem.py
    python service-ecosystem.py -o ecosystem.png --theme dark
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


MERMAID_CHART = """
%%{init: {"themeVariables": {"edgeLabelBackground": "#c55a00"}, "flowchart": {"rankSpacing": 200, "nodeSpacing": 70, "padding": 20, "curve": "basis", "defaultRenderer": "elk"}, "themeCSS": ".cluster-label text, .cluster-label span { font-weight: bold !important; } .edgeLabel .label, .edgeLabel .label span, .edgeLabel text { color: white !important; fill: white !important; }"}}%%
graph LR
    classDef actor fill:#1b365d,color:#ffffff,stroke:#0d1f3c

    subgraph Customer
        R1["R1 · User"]
    end

    subgraph Provider
        R2["R2 · Service Platform"]
    end

    R1 -->|"€9.99/month"| R2
    R2 -->|"Service access via mobile app"| R1

    class R1,R2 actor

    style Customer fill:#ebebeb,stroke:#888
    style Provider fill:#ebebeb,stroke:#888
"""


def render_png_mmdc(mermaid_code: str, output_path: Path, theme: str) -> None:
    with tempfile.NamedTemporaryFile(suffix=".mmd", mode="w", delete=False) as f:
        f.write(mermaid_code)
        tmp_in = Path(f.name)
    print("Rendering PNG via mmdc (3× scale, 3000 px wide)…")
    try:
        result = subprocess.run(
            [
                "mmdc",
                "-i", str(tmp_in),
                "-o", str(output_path),
                "-t", theme,
                "-b", "white",
                "-w", "3000",
                "-H", "2000",
                "-s", "3",
                "-q",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            sys.exit(f"mmdc failed:\n{result.stderr}")
    finally:
        tmp_in.unlink(missing_ok=True)


def main() -> None:
    if not MERMAID_CHART.strip():
        sys.exit("error: MERMAID_CHART is empty — paste the chart value into this file first")

    parser = argparse.ArgumentParser(
        description="Render the MERMAID_CHART variable to a PNG via mmdc",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s -o ecosystem.png --theme dark
""",
    )
    parser.add_argument("-o", "--output", help="Output file path (default: service_ecosystem.png)")
    parser.add_argument(
        "--theme",
        default="default",
        choices=["default", "dark", "forest", "neutral", "base"],
        help="Mermaid theme (default: default)",
    )
    args = parser.parse_args()

    output_path = Path(args.output) if args.output else Path("service_ecosystem.png")

    print(f"Rendering → {output_path}  (theme={args.theme})")
    render_png_mmdc(MERMAID_CHART, output_path, args.theme)
    print(f"Saved {output_path.stat().st_size:,} bytes to {output_path}")


if __name__ == "__main__":
    main()
```