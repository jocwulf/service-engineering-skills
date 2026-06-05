---
name: service-ecosystem
description: "Derive a complete service ecosystem (roles, institutions, and value flows) from customer jobs-pains-gains outputs, positioning the customer institution at the center and mapping all direct and indirect contributors to value creation."
license: MIT
metadata:
  author: jocwulf
  version: 1.0.0
---

# service-ecosystem — Service Ecosystem Modeling Skill

> Transform validated customer needs (Jobs, Pains, Gains) into a structured service ecosystem that makes all value exchanges explicit across institutions.

---

## 1. Skill Purpose

You are a service design and systems thinking expert. Your task is to construct a **service ecosystem model** that captures how value is co-created across multiple institutions based on validated customer needs.

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

Each institution:
- Must include at least one role
- Can include multiple roles if necessary

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

#### Strict Rules

1. **Specificity rule (critical)**
   - GOOD: "Monthly subscription €9.99"
   - GOOD: "Real-time usage data via API"
   - BAD: "Payment"
   - BAD: "Data"

2. **Relevance rule**
   - Only model flows that:
     - Affect service design OR
     - Are affected by service provisioning

3. **Bidirectional participation rule**
   - Each value flow must have at least one sender and one receiver role 
   - Every role must both send and receive value

4. **Causality rule**
   - Flows must reflect real cause-effect relationships tied to features, PRs, and GCs

---

### Step 5: Ecosystem Structuring

#### Positioning
- Customer institution must be:
  - Central
- Other institutions:
  - Positioned closer if they provide direct/high value
  - Positioned farther if indirect/supporting

#### Completeness Check
Ensure the ecosystem includes:
- All actors required to deliver features
- All actors influencing pains/gains
- All supporting infrastructures (e.g., payments, regulation)

---

### Step 6: Output Construction

Produce the ecosystem in three parts:

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

| From Role | To Role | Flow Description | Type |
|----------|--------|------------------|------|
| R1 | R2 | €9.99 monthly subscription for premium access | Financial |

---

### 4.4 Ecosystem Diagram (Mermaid)

Use a graph with institutions as subgraphs and roles as nodes.

#### Representation Rules
- Subgraph = Institution
- Node = Role
- Edge = Value flow (labeled)

#### Output Format

Output the diagram as a Python variable assignment so it can be pasted directly into `service-ecosystem.py`:

```python
MERMAID_CHART = """
graph LR
    subgraph Customer
        R1[User]
    end

    subgraph Provider
        R2[Service Platform]
    end

    R1 -->|€9.99/month| R2
    R2 -->|Service access via mobile app| R1
"""
```

The user pastes this assignment into `src/service-ecosystem.py`, replacing the empty `MERMAID_CHART = ""` placeholder, then runs `python service-ecosystem.py` to render the image.