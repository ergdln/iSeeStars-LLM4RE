# I See Stars: Requirements Elicitation for iStar Modeling

## 🔭 Overview

**I See Stars** is a project that explores how **Large Language Models (LLMs)** can support **requirements engineering**, helping to transform natural language requirements into structured models using the **i* (iStar)** notation.

The project proposes an **Interactive Prompting Approach**, where the LLM asks clarification questions before generating the final model, aiming to reduce ambiguity and improve completeness.

---

## 🎯 Objectives

* Use LLMs to support the transformation of informal software requirements into formal **i*** models.
* Evaluate whether interactive prompting (with clarification questions) produces better results compared to a single direct prompt.
* Experiment with structured LLM outputs (e.g., JSON or DSL) to make the resulting models machine-readable and easier to analyze or visualize.

---

## 📌 Scope

The project includes:

* Natural language requirement scenarios.
* Prompts designed for:

  * A **baseline approach** (direct generation).
  * An **interactive multi-step approach** (questions first, model second).
* Analysis of how these different prompting strategies influence:

  * Model completeness
  * Clarity
  * Faithfulness to i* notation

No implementation is required; the project focuses on methodology, experimentation, and results.

---

## 🧠 Methodology

### Baseline (Zero-Shot)

The LLM receives a scenario and is asked to directly generate an i* model.

### Proposed Interactive Approach

1. The LLM first acts as a requirements engineer and generates 5–8 clarification questions about:

   * Actors
   * Goals
   * Softgoals
   * Tasks
   * Dependencies

2. The user (or group) provides answers to these questions.

3. The LLM generates the final i* model using both the original scenario and the additional information.

### Knowledge Support in Prompts

The prompts include:

* A brief explanation of the i* notation.
* Context about the scenario domain.
* Constraints on the structure of the output.

This helps the LLM stay consistent and avoid hallucinations.

---

## 🧪 Experiment Design

### Scenarios

The project uses 3–5 requirement examples (e.g., taxi app, library system, medical booking system) with intentional ambiguity to stimulate clarification.

### Models Compared

1. **Zero-Shot Model**
   Direct output from a single prompt.

2. **Interactive Model**
   Output after questions and answers have been exchanged.

### Evaluation

A small group of reviewers compares the models against a manually created reference, assessing:

* **Completeness**

  * Does the model capture expected actors and goals?

* **Conformance to i***

  * Are elements properly represented according to the notation?

* **Question Quality**

  * Were the questions useful for reducing ambiguity?

---

## 📁 Expected Deliverables

* Requirement scenarios in natural language.
* The prompts used for both approaches.
* The resulting structured outputs from the LLM.
* A written report analyzing:

  * The effectiveness of interactive elicitation.
  * Differences in completeness and correctness between approaches.

---

## 📚 License & Use

This project is intended for academic and research purposes, especially for studies involving LLMs in requirements engineering.

---
