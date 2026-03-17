# Setup Guide

[⬅ Toolkit Components](./toolkit-components) | [Playground Scenarios ➡](./playground-scenarios)

## Prerequisites

- Access to a Business Central sandbox environment.
- AL development tooling (for extension development and deployment).
- Access to an approved AI model endpoint.
- Environment-specific secrets/configuration strategy.

## Quickstart checklist

1. Create or open a Business Central extension project.
2. Configure environment variables/secrets for your AI service.
3. Add a minimal playground page/action in Business Central.
4. Implement one narrow use case (e.g., summarize selected records).
5. Add logging for request/response metadata.
6. Validate with test prompts and role-based access scenarios.

## Hardening checklist

- Add prompt templates for consistency.
- Restrict and validate all agent actions.
- Add retry/error boundaries for endpoint failures.
- Track usage and performance metrics.
- Document known limits and escalation paths.
