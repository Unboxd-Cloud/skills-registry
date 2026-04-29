# OpenAI SDK Notes

Use this reference when the Canonical MicroCloud platform needs direct OpenAI SDK integration in addition to, or instead of, a LiteLLM-routed OpenAI-compatible endpoint.

## Current Direction

OpenAI documents the `Responses` API as the primary API surface for new work.

## Recommended Role In This Skill

- Keep Microsoft Agent Framework as the runtime.
- Keep LiteLLM as the default multi-model gateway where multi-provider routing is required.
- Use the OpenAI SDK directly when the runtime should talk to OpenAI-native endpoints or when a narrow direct client path is simpler than gateway routing.

## Design Rules

- Prefer the `Responses` API for new direct OpenAI integrations.
- Keep direct OpenAI use behind a clear adapter or client module.
- Do not mix direct provider calls and gateway calls in the same code path without a clear routing reason.
- Record model id, request purpose, and trace correlation id.

## Output Expectations

When this reference is in play, produce:
- direct-vs-gateway decision
- SDK client placement
- model selection strategy
- observability and approval implications
