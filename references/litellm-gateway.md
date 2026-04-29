# LiteLLM Model Gateway Notes

Use this reference when the Canonical MicroCloud platform needs one agent runtime to reach multiple LLM providers through a single gateway.

As of April 28, 2026:
- LiteLLM supports a proxy server that exposes OpenAI-compatible endpoints including `/chat/completions` and `/responses`.
- Microsoft Agent Framework Python OpenAI clients support a `base_url`, which makes LiteLLM a clean gateway in front of multiple providers.

## Recommended Architecture

- Microsoft Agent Framework remains the agent runtime.
- LiteLLM Proxy is the model gateway.
- Provider-specific credentials stay behind the gateway.
- Agent code targets model aliases exposed by LiteLLM rather than raw provider endpoints.

## Why Use It

- Single OpenAI-compatible endpoint for multiple providers
- Centralized authentication, routing, rate limiting, and spend tracking
- Model aliasing and fallback without changing application code
- Cleaner separation between runtime logic and provider choice

## Integration Pattern

In the Python starter:
- Use `agent_framework.openai.OpenAIResponsesClient` or `OpenAIChatCompletionClient`
- Set `base_url` to the LiteLLM proxy URL
- Set `api_key` to the LiteLLM virtual key or gateway key
- Set `model_id` to a LiteLLM model alias such as `gpt-5`, `claude-sonnet`, or `ops-router`

## Operational Rules

- Prefer model aliases over provider-native model names in application code.
- Keep routing, fallback, and budget policy in LiteLLM config.
- Treat gateway outages as platform dependencies and instrument them.
- Do not embed upstream provider keys in agent app code.

## Output Expectations

When this reference is in play, produce:
- LiteLLM gateway placement in the topology
- Model alias strategy
- Routing and fallback policy
- Secret flow and gateway auth model
- Observability path for gateway and agent runtime
