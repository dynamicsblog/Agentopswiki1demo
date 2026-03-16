# Toolkit Components

[⬅ Overview](./overview) | [Setup Guide ➡](./setup)

## Core building blocks

A typical Business Central AI playground implementation includes:

- **Business Central extension layer (AL):** The user-facing and domain logic integration point.
- **Prompting/orchestration layer:** Structures inputs, grounding context, and tool invocation logic.
- **Model endpoint(s):** LLM provider(s) used for generation, classification, and reasoning.
- **Business tools/actions:** Controlled capabilities the agent can call to read/write domain data.
- **Safety and policy checks:** Prompt filtering, role boundaries, and output guardrails.
- **Telemetry and diagnostics:** Logging prompts, latency, token usage, and errors.

## Recommended architecture flow

1. User issues a request in Business Central.
2. Extension gathers contextual records and user intent.
3. Orchestrator composes a safe, bounded prompt.
4. Model returns structured output.
5. Extension validates response and executes allowed operations.
6. UI surfaces result + optional user confirmation.

## Design principles

- Keep prompts task-focused and deterministic where possible.
- Prefer structured model outputs for business actions.
- Enforce explicit permissions for all data mutations.
- Add observability from day one to support tuning.
