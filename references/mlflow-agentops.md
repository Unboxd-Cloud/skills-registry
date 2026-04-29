# MLflow AgentOps Notes

Use this reference when the Canonical MicroCloud platform needs agent observability, trace capture, and operational debugging for agent and workflow runs.

As of April 28, 2026:
- MLflow Tracing is positioned as LLM and agent observability with OpenTelemetry compatibility.
- MLflow supports manual tracing via `@mlflow.trace` for sync and async functions.
- MLflow also supports OpenAI autologging via `mlflow.openai.autolog()`.
- LiteLLM documents MLflow as an observability callback option on the LiteLLM side.

## Recommended Split

- Microsoft Agent Framework: agent runtime and orchestration
- LiteLLM: model gateway and multi-provider routing
- MLflow: trace storage, request visibility, and agent operations analysis

## What To Trace

- Agent request entry and final response
- Workflow execution steps and latency
- Tool invocation boundaries
- Approval-required operations
- Gateway-facing model calls
- Error paths and retries

## Integration Pattern

In the Python starter:
- Configure `mlflow.set_tracking_uri()` when a tracking server is used.
- Set an experiment name for the service.
- Enable `mlflow.openai.autolog()` because the agent uses the OpenAI-compatible client surface.
- Add `@mlflow.trace` around key async functions that define agent and workflow boundaries.

## Operational Rules

- Keep trace attributes low-cardinality where possible.
- Record environment, model alias, and operation type on spans.
- Do not put secrets or raw credentials in traces.
- Use traces as the system of record for debugging agent behavior, not ad hoc print logs.

## Output Expectations

When this reference is in play, produce:
- Tracking server placement
- Experiment naming strategy
- Span boundaries for agent, workflow, and tool steps
- Trace attributes to keep
- Data redaction guidance
