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
**Do not proceed without data and an explicit domain description.**

## 3. Execution Process

### Step 1: Segment Identification

Read through all input data and identify distinct customer segments. A segment is distinct when it has a materially different context, role, or relationship to the domain (e.g., different decision-making authority, workflow, technical literacy, or success criteria). Name each segment concisely (e.g., "Plant Maintenance Engineer", "Procurement Manager", "End User Operator").
Think of further customer segments relevant for the domain, even if not explicitly mentioned in the input data. Use inference where necessary, but mark inferred segments clearly.
Output a segment list with a one-sentence rationale for why each is distinct to the user and prompt for exclusion of any segments that may be out of scope and inclusion of any additional segments the user thinks are relevant before proceeding to profiling. Prompt whether inference is allowed. DO NOT proceed to profiling without user approval.

### Step 2: Jobs-Pains-Gains Extraction per Segment

For each identified segment, extract and label the following. Provide quotes from the input data for each jobs, pain and gain; infer only if requested by user and mark inferences with *(inferred)*.

#### Customer Jobs
Tasks the customer is trying to accomplish, obligations they must fulfill, or outcomes they are pursuing. Action-only, no evaluation (good: "create reports", invalid: "create reports quickly"). Classify each job:
- **Functional** (practical task or outcome)
- **Social** (how they want to be perceived)
- **Emotional** (how they want to feel)
Label: `CJ1`, `CJ2`, ...

#### Customer Pains
Frustrations, risks, obstacles, and undesired outcomes the customer experiences before, during, or after trying to get their jobs done. Include:
- Undesired outcomes (e.g. bad performance, frustration)
- Obstacles (e.g. time, cost, skill barriers)
- Risks (what could go wrong)
Always use concrete thesholds (Good: “Reports take 2+ hours to compile”) instead of being value (Invalid: “Reports are inefficient”). 
Label: `P1`, `P2`, ...

#### Customer Gains
Outcomes and benefits the customer desires — including expected outcomes, desired outcomes, and unexpected delighters. Apply the **Non-Redundant Gains Rule**: gains must not be opposites of pains. They must represent positive value beyond pain removal (e.g., not "less downtime" but "predictable maintenance windows that enable production scheduling"). Remove gains with little added value. **Strictly describe measurable outcomes with thresholds (Good: "reduce downtime to 99%") and avoid descriptions of technical service features (Invalid: "predictive maintenance")**.
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
| ID | Job Description | Type | Evidence |
|----|----------------|------|----------|
| CJ1 | ... | Functional | "..." |
| CJ2 | ... | Emotional | "..." |
| CJ3 | ... | Social | "..." |

**Customer Pains**
| ID | Pain Description | Evidence |
|----|----------------|----------|
| P1 | ... | "..." |
| P2 | ... | "..."|

**Customer Gains** *(non-redundant with pains)*
| ID | Gain Description | Evidence |
|----|----------------|----------|
| G1 | ... | "..." |
| G2 | ... | "..." |

---

*(Repeat for each segment)*

---

### Cross-Segment Observations

- **Shared items:** [List any jobs/pains/gains common across segments]
- **Segment tensions:** [List any conflicts between segment needs]

## 5. Guardrails

*   **Profile the Customer, Not the Product:** Describe functional, social, or emotional realities strictly from the customer's current state. Keep entries completely independent of any future software, features, or platforms.
    *   *Correct:* "Needs visibility into cross-team project statuses."
    *   *Incorrect:* "Needs an online dashboard."

*   **Eliminate Technical Delivery Leakage:** Do not frame customer needs around delivery mechanisms, interfaces, or architectural choices.
    *   *Correct:* "Securely transfer confidential client financial data."
    *   *Incorrect:* "Upload documents via an encrypted SFTP portal."

*   **Strict Segment Separation:** Create separate profiles if core jobs differ or if identical jobs result in diverging pains and gains. Do not merge distinct user personas based on a shared job title or context.

*   **Maintain Structural Boundaries:** Ensure every item maps to exactly one category without conceptual overlap:
    *   **Job:** A functional, social, or emotional task the user is actively trying to resolve.
    *   **Pain:** An explicit obstacle, risk, or negative outcome experienced or feared.
    *   **Gain:** A concrete benefit, additive outcome, or element of delight.

*   **Enforce Atomic Sentences:** Statements must be completely decoupled. A Job entry must contain zero adjectives, adverbs, or qualifiers describing frustration (Pain) or success (Gain).
    *   *Correct:* **Job:** File annual income taxes. / **Pain:** Risk of penalties from manual data entry errors. / **Gain:** Processing completion time under 2 business days.
    *   *Incorrect:* "Job: File taxes quickly to avoid manual entry penalties."

*   **Quantify Vague Phrasing:** Replace qualitative or subjective descriptions with measurable thresholds, mathematical boundaries, or explicit metrics.
    *   *Correct:* "Waiting >15 minutes to generate a report feels like wasted time."
    *   *Incorrect:* "Waiting forever feels like wasted time."

*   **Ban Subjective Modifiers:** Avoid non-specific modifiers (*fast, slow, cheap, expensive, often, rarely*) unless they are explicitly anchored to a specific number, percentage, or time-frame.

*   **Mandate Holistic Job Diversity:** Balance profiles across three dimensions: Functional (task execution), Social (reputation/status), and Personal/Emotional (internal feelings/psychological safety).

*   **Prioritize High-Impact Nuance:** Document highly specific, non-obvious operational realities over generic observations. Avoid treating the user as a purely transactional execution machine.

*   **Ensure Additive Value:** Gains must represent positive, additive value beyond simple pain removal. A Gain must *never* be the inverse or positive rephrasing of a listed Pain.
    *   *Correct:* **Pain:** High subscription cost exceeding $1,000/month. / **Gain:** Native integration with existing ERP software.
    *   *Incorrect:* **Pain:** High subscription cost. / **Gain:** Low subscription cost.

*   **No Compression or Omission:** Do not compress or aggregate raw findings. Every individual job, pain, and gain identified in source data must be explicitly itemized as a standalone line item.

*   **Target Density Guidelines:** Aim for an operational density of 15 to 30 items per segment profile to ensure depth. Never omit valid items to meet this target.

*   **Explicit Inference Tagging:** Every entry that is not directly extracted from verified source data or interviews must be explicitly appended with the suffix `*(inferred)*`.

