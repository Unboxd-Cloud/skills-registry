# MLflow Prompt Registry And Evaluation Notes

Use this reference when the Canonical MicroCloud platform should manage prompts and evaluations inside MLflow rather than adding a separate prompt-ops product.

As of April 28, 2026:
- MLflow Prompt Registry supports prompt versioning, aliases, reuse, and lineage.
- MLflow GenAI evaluation supports datasets, LLM judges, custom scorers, human feedback, and production monitoring.

## Recommended Split

- MLflow Prompt Registry: prompt source of truth
- MLflow Tracing: runtime observability and feedback capture
- MLflow GenAI evaluation: regression testing and quality monitoring
- LiteLLM: model routing and fallback
- Microsoft Agent Framework: agent runtime and workflow orchestration

## Prompt Management Pattern

- Store prompts in MLflow Prompt Registry.
- Reference prompts by stable alias such as `production`, `candidate`, or `staging`.
- Fetch prompt content at runtime or deployment time.
- Keep agent code responsible for prompt variables and tool boundaries, not prompt text storage.

## Evaluation Pattern

- Build evaluation datasets from curated test cases and traced production examples.
- Run `mlflow.genai.evaluate()` against agent outputs.
- Use LLM judges and custom scorers only where they materially improve confidence.
- Treat evaluation results as release gates for prompt or runtime changes.

## Operational Rules

- Prefer prompt aliases over hard-coded version numbers in app code.
- Record prompt name, alias, and resolved version in traces or run metadata.
- Keep evaluation datasets versioned and reviewable.
- Use human feedback to augment LLM-based scores, not replace them.

## Output Expectations

When this reference is in play, produce:
- Prompt registry naming and alias strategy
- Runtime prompt fetch path
- Evaluation dataset shape
- Release gate proposal for prompt and model changes
