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
    *   `Resource Type:` [Tangible, Intangible, Human]
    *   `Link to Activity:` [Fits, Flows, Shared]

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
    *   `Strategic Importance:` [Scale 0-5]
    *   `Degree of Integration:` [Scale 0-5]
    *   `Substitutability:` [Scale 0-5]

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


##  Python Visualization Template
When executing Step 4, use the following Python code. Dynamically replace the `nodes` and `edges` dictionaries with the actual IDs and abbreviated labels generated in Step 2.

```python
import networkx as nx
import matplotlib.pyplot as plt

# LLM INSTRUCTION: Dynamically populate these nodes based on the generated BMC.
# Colors: CS=pink, VP=lightgreen, CH/CR=lightblue, RS=lightyellow, KR=peach, KA=salmon, KP=magenta, C=purple
nodes = {
    "CS-1": {"label": "CS-1: Segment Name\n(Demographic)", "color": "#ffb3ba"},
    "VP-1": {"label": "VP-1: Proposition\n(Effort/Economy)", "color": "#baffc9"},
    "CH-1": {"label": "CH-1: Channel\n(Purchase/Partner)", "color": "#bae1ff"},
    "CR-1": {"label": "CR-1: Relationship\n(Retention/Trust)", "color": "#bae1ff"},
    "RS-1": {"label": "RS-1: Revenue\n(Selling/Fixed)", "color": "#ffffba"},
    "KR-1": {"label": "KR-1: Resource\n(Intangible)", "color": "#ffdfba"},
    "KA-1": {"label": "KA-1: Activity\n(Value Chain/Ops)", "color": "#f67280"},
    "KP-1": {"label": "KP-1: Partner\n(Resource Acq/Int: 4)", "color": "#f8b195"},
    "C-1":  {"label": "C-1: Cost\n(Direct/60%)", "color": "#d5aaee"}
}

# LLM INSTRUCTION: Dynamically map the edges based on the relationships in the Markdown tables.
edges = [
    ("VP-1", "CH-1"), ("CH-1", "CS-1"),
    ("VP-1", "CR-1"), ("CR-1", "CS-1"),
    ("VP-1", "RS-1"), ("CS-1", "RS-1"),
    ("KR-1", "VP-1"),
    ("KA-1", "KR-1"),
    ("KP-1", "KA-1"), ("KP-1", "KR-1"),
    ("KA-1", "C-1"), ("KR-1", "C-1"), ("KP-1", "C-1")
]

# Generate directed graph
G = nx.DiGraph()
for node_id, attrs in nodes.items():
    G.add_node(node_id, label=attrs["label"], color=attrs["color"])
G.add_edges_from(edges)

plt.figure(figsize=(16, 10))
# Multipartite or spring layout
pos = nx.spring_layout(G, k=1.2, seed=42)

colors = [G.nodes[n]['color'] for n in G.nodes]
labels = {n: G.nodes[n]['label'] for n in G.nodes}

# Draw nodes as styled bounding boxes
nx.draw_networkx_nodes(G, pos, node_color=colors, node_shape="o", node_size=100) # Invisible backing
for p, (node, position) in zip(G.nodes, pos.items()):
    plt.text(position[0], position[1], labels[node], size=9, ha="center", va="center", 
             fontweight="bold", bbox=dict(boxstyle="round4,pad=0.5", fc=G.nodes[node]['color'], ec="gray", alpha=0.9))

nx.draw_networkx_edges(G, pos, arrowstyle="-|>", arrowsize=20, edge_color="gray", width=2, connectionstyle="arc3,rad=0.1")

plt.title("Ontological Business Model Interdependencies", fontsize=18, fontweight="bold")
plt.axis("off")
plt.tight_layout()

# Save the plot
filename = "business_model_ontology.png"
plt.savefig(filename, dpi=300, bbox_inches="tight")
print(f"Visualization successfully saved to {filename}")
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
