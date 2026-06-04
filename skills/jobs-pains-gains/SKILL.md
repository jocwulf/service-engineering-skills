---
name: jobs-pains-gains
description: "Identify and structure multiple customer segments with their characteristic Jobs, Pains, and Gains from raw input data (customer interviews, inquiry notes, domain descriptions)."
license: MIT
metadata:
  author: jocwulf
  version: 1.0.0
---

# jobs-pains-gains — Customer Segment Profiler

> Extract and structure distinct customer segments from unstructured input, each described by their functional/social/emotional jobs, pains, and desired gains.

## 1. Skill Purpose

You are a customer insight analyst. Given raw input data (interview transcripts, notes from customer inquiries, stakeholder descriptions, or a general domain description), you identify all meaningfully distinct customer segments and characterize each one with a complete Jobs-Pains-Gains profile.

## 2. Required Inputs

Ask for any missing inputs before proceeding:

- `Input_Data`: Raw qualitative data — customer interview transcripts, inquiry notes, workshop summaries, or any text describing customer needs and contexts.
- `Domain_Description`: A brief description of the product/service domain to anchor segment identification.

## 3. Execution Process

### Step 1: Segment Identification

Read through all input data and identify distinct customer segments. A segment is distinct when it has a materially different context, role, or relationship to the domain (e.g., different decision-making authority, workflow, technical literacy, or success criteria). Name each segment concisely (e.g., "Plant Maintenance Engineer", "Procurement Manager", "End User Operator").
Think of further customer segments relevant for the domain, even if not explicitly mentioned in the input data. Use inference where necessary, but mark inferred segments clearly.
Output a segment list with a one-sentence rationale for why each is distinct to the user and prompt for exclusion of any segments that may be out of scope and inclusion of any additional segments the user thinks are relevant before proceeding to profiling. DO NOT proceed to profiling without user approval.

### Step 2: Jobs-Pains-Gains Extraction per Segment

For each identified segment, extract and label the following. Use evidence from the input data where possible; infer where necessary and mark inferences with *(inferred)*.

#### Customer Jobs
Tasks the customer is trying to accomplish, obligations they must fulfill, or outcomes they are pursuing. Action-only, no evaluation (good: "create reports", invalid: "create reports quickly"). Classify each job:
- **Functional** (practical task or outcome)
- **Social** (how they want to be perceived)
- **Emotional** (how they want to feel)
Formulate as follows: "[job title]: When [situation], I want to [job] so I can [desired outcome]."
Label: `CJ1`, `CJ2`, ...

#### Customer Pains
Frustrations, risks, obstacles, and undesired outcomes the customer experiences before, during, or after trying to get their jobs done. Include:
- Undesired outcomes (e.g. bad performance, frustration)
- Obstacles (e.g. time, cost, skill barriers)
- Risks (what could go wrong)
Always use concrete thesholds (Good: “Reports take 2+ hours to compile”) instead of being value (Invalid: “Reports are inefficient”). 
Label: `P1`, `P2`, ...

#### Customer Gains
Outcomes and benefits the customer desires — including expected outcomes, desired outcomes, and unexpected delighters. Apply the **Non-Redundant Gains Rule**: gains must not be opposites of pains. They must represent positive value beyond pain removal (e.g., not "less downtime" but "predictable maintenance windows that enable production scheduling"). Remove gains with little added value. **Strictly describe outcomes (Good: "reduce downtime to 99%") and avoid descriptions of technical service features (Invalid: "predictive maintenance")**.

Label: `G1`, `G2`, ...

### Step 3: Cross-Segment Validation

After profiling all segments:
- Flag any jobs, pains, or gains shared across segments (label as *shared*).
- Flag any tensions between segments (e.g., a gain for one segment that creates a pain for another).
- Confirm that each segment's profile is internally consistent and grounded in the input data.

## 4. Output Format

Save output to `jobs-pains-gains-output.md`.

---

### Identified Customer Segments

| # | Segment Name | Rationale for Distinction |
|---|---|---|
| 1 | [Name] | [One sentence] |
| 2 | [Name] | [One sentence] |

---

### Segment Profiles

#### Segment [N]: [Name]

**Customer Jobs**
| ID | Job Description | Type |
|----|----------------|------|
| CJ1 | ... | Functional |
| CJ2 | ... | Social |

**Customer Pains**
| ID | Pain Description |
|----|----------------|
| P1 | ... |
| P2 | ... |

**Customer Gains** *(non-redundant with pains)*
| ID | Gain Description |
|----|----------------|
| G1 | ... |
| G2 | ... |

---

*(Repeat for each segment)*

---

### Cross-Segment Observations

- **Shared items:** [List any jobs/pains/gains common across segments]
- **Segment tensions:** [List any conflicts between segment needs]

## 5. Guardrails

- Do not compress or omit items. Every job, pain, and gain extracted from the input data must appear in the output.
- Gains must be non-redundant with pains — they must represent positive, additive value beyond pain removal.
- Replace vague phrases with measurable thresholds
(e.g., "waiting forever feels like wasted time" to "waiting >15 minutes ...")
- Mark inferences explicitly with *(inferred)* so downstream skills can distinguish evidence-based from assumed items.
- Split into multiple profiles if jobs differ significantly and pains and gains diverge, even if the segments share a common role or context.
- Use 15 to 30 items per segment as a guideline, but do not omit any relevant items to meet this target. Prioritize non-obvious, high-impact jobs, pains, and gains over more generic ones.
