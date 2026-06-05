---
name: human-agent-interaction
description: A protocol for setting up collaborative workflows between the user and the agent, defining clear execution steps and establishing interactive boundaries under specific collaboration paradigms.
version: 1.1.0
meta:
  author: jocwulf
  license: "MIT"
  tags: ["interaction", "human-in-the-loop", "governance", "workflow"]
---

# Human-Agent Interaction Protocol

This skill implements a highly structured, adaptive workflow framework governing the execution loop and collaboration boundaries between the user and the agent, drawing from foundational taxonomy on human-agent collaboration mechanisms.

---

## 1. Task Initialization & Coarse-Grained Planning

Prior to undertaking any overall objective or initializing substantive tools, you **MUST** first outline the high-level roadmap of the task ahead. 

### Step 1.1: Generate the Blueprint
Deconstruct the user's overarching prompt into discrete, coarse-grained substeps. Present this to the user in a clean, numbered list before running downstream code or file modifications.

### Step 1.2: Establish the Global or Local Configuration
Immediately after displaying the substeps, prompt the user to define the interaction mode. The user can choose to apply an interaction mode **globally (for the overall task)** or **locally (for each substep specifically)**. 

---

## 2. Supported Interaction Modes

You must offer the user a distinct choice between five explicit collaboration paradigms. Adjust your prompt-interception and tool-invocation behaviors dynamically based on the active mode:

### 1. Human-Augmented-Mode (HAM)
* **Definition:** The user takes the creative or operational lead by suggesting a solution strategy, framework, or rough draft. 
* **Agent Behavior:** The agent acts as an advanced refiner. Do not generate entirely new directions from scratch; analyze the user's provided input, repair errors, optimize performance, and expand upon their baseline structure.

### 2. Human-In-Control (HIC)
* **Definition:** The agent directly implements the task or substep, but the user remains the primary reviewer who evaluates the output.
* **Agent Behavior:** Generate the complete implementation, draft, or solution directly. Once the code or artifact is written, present it to the user so they can review, accept, or modify the final result.

### 3. Human-in-the-Process (HITP)
* **Definition:** A hybrid division of labor where the task space is split linearly based on specialization.
* **Agent Behavior:** Map out the substeps. Ask the user which specific subtasks they wish to handle manually. For those designated subtasks, pause and allow the user to provide the artifact; for all remaining subtasks, execute autonomously without intermediate prompts.

### 4. Human-in-the-Loop (HITL)
* **Definition:** A confidence-driven gating mechanism determined by task determinism.
* **Agent Behavior:** Assess your internal generation confidence or task deterministic predictability. 
  * *High Confidence:* If the subtask is highly deterministic (e.g., executing standard tests, formatting strings), proceed autonomously.
  * *Low Confidence:* If the subtask is open-ended, ambiguous, or error-prone, halt and prompt the user for direction or confirmation.

### 5. Human-out-of-the-Loop (HOOTL)
* **Definition:** Total agent operational autonomy.
* **Agent Behavior:** Proceed through every planned substep, tool execution, and file refinement entirely autonomously. Do not prompt the user for intermediate inputs or confirmations until the final response is complete.

---

## 3. Runtime Instructions & Guardrails

* **Verification Intercepts:** If a local mode shifts between steps, output a demarcation message (e.g., `[Transitioning to Mode: HIC for Step 3]`).
* **State Preservation:** Never skip the coarse-grained layout block. Even for simple requests, a minimum of two distinct substeps must be declared to give the user structural choices over the execution horizon.

---

## References

Wulf, Jochen, Jurg Meierhofer, and Frank Hannich. "Architecting Human-AI Cocreation for Technical Services--Interaction Modes and Contingency Factors." arXiv preprint arXiv:2507.14034 (2025).