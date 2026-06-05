# Service Engineering Skills

A library of [Claude Code](https://claude.ai/code) skills for end-to-end smart service design — from raw customer research to financial validation.

## Overview

These skills implement a structured methodology for designing and evaluating smart (data-driven) services. Each skill is invoked as a slash command inside Claude Code. Skills form a DAG: each step accepts the outputs of its predecessors as direct inputs.

```
Customer Data
      │
      ▼
① /jobs-pains-gains
      │
      ▼
② /value-of-pains                     ← ①

③ /smart-service-ideation             ← ① ②

④ /value-proposition-canvas-fit       ← ① ③
      │
      ├──────────────────────────────────► ⑥ /service-ecosystem
      │
      ▼
⑤ /value-of-solving-pains             ← ② ④

⑦ /service-business-case              ← ④ ⑤
```

`/human-agent-interaction` is orthogonal — it configures the collaboration mode and can be applied at any point.

## Skills

| # | Skill | Slash Command | Inputs | Description |
|---|---|---|---|---|
| ① | [jobs-pains-gains](skills/jobs-pains-gains/) | `/jobs-pains-gains` | Customer data | Identify customer segments and characterize each with Jobs, Pains, and Gains from raw qualitative input |
| ② | [value-of-pains](skills/value-of-pains/) | `/value-of-pains` | ① | Quantify the baseline economic potential of each pain and gain (frequency × impact) |
| ③ | [smart-service-ideation](skills/smart-service-ideation/) | `/smart-service-ideation` | ① ② | Generate 100+ smart service ideas via Data Escalation, Cross-Pollination, and Business Model Patterns; consolidate into technical bundles |
| ④ | [value-proposition-canvas-fit](skills/value-proposition-canvas-fit/) | `/value-proposition-canvas-fit` | ① ③ | Map envisioned features to pains and gains per segment; produce a Mermaid VPC diagram per segment |
| ⑤ | [value-of-solving-pains](skills/value-of-solving-pains/) | `/value-of-solving-pains` | ② ④ | Apply alleviation factors to the pain/gain baseline to calculate effective value per service bundle; produce value-based pricing |
| ⑥ | [smart-service-ecosystem](skills/smart-service-ecosystem/) | `/service-ecosystem` | ④ | Derive a complete ecosystem of roles, institutions, and value flows from VPC outputs |
| ⑦ | [service-business-case](skills/service-business-case/) | `/service-business-case` | ④ ⑤ | Build a full financial business case: Simplified FCFF, NPV, IRR, and Payback Period with sensitivity analysis |
| — | [human-ai-interaction](skills/human-ai-interaction/) | `/human-agent-interaction` | *(orthogonal)* | Configure a structured human-in-the-loop collaboration protocol (interaction modes, checkpoints, approval gates) |

## Usage

Install Claude Code, then invoke any skill from within a project:

```
/jobs-pains-gains
```

Each skill asks for required inputs before executing. When a skill depends on a predecessor, paste or reference the predecessor's output when prompted — the skills are designed to accept each other's output format directly.

## Methodology

The pipeline implements the value-based service design approach described in [The Value of Solving Pains](https://arxiv.org/pdf/2412.03130). Core ideas:

- **Jobs-to-be-done** framing for customer segmentation
- **Frequency × impact** quantification of pains and gains
- **Alleviation factors (ω)** to translate potential value into realized value per service
- **Value-based pricing** derived from customer value, not cost-plus
- **FCFF-based financial modelling** for go/no-go investment decisions

## License

MIT
