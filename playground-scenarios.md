# Playground Scenarios

[⬅ Setup Guide](./setup) | [References ➡](./references)

## Scenario 1: Document summarization

**Goal:** Summarize long business records into concise operational insights.

- Input: customer notes, case details, or transaction history.
- Output: highlights, risks, and suggested follow-up tasks.
- Guardrail: strip or mask sensitive fields where required.

## Scenario 2: Guided data entry

**Goal:** Assist users by generating draft values from natural language.

- Input: user request in plain language.
- Output: pre-filled fields and rationale.
- Guardrail: require user confirmation before commit.

## Scenario 3: Process assistant

**Goal:** Provide step-by-step operational guidance tied to BC entities.

- Input: current page context + user question.
- Output: recommended next actions and links to relevant records.
- Guardrail: role-aware filtering of suggested actions.

## Scenario readiness rubric

Use this rubric before promoting a scenario beyond playground:

- **Accuracy:** useful and factually correct in representative tests.
- **Safety:** no unauthorized data exposure or unsafe execution paths.
- **Reliability:** stable latency and graceful error handling.
- **Auditability:** traceable logs for decisions and actions.
