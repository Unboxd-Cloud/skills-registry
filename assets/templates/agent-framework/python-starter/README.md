# Microsoft Agent Framework Python Starter

This starter is a code-first baseline for a Canonical MicroCloud agent runtime using Microsoft Agent Framework with a LiteLLM model gateway and MLflow for observability, prompt management, and evaluation.

## What It Includes

- `app/config.py`: environment-driven LiteLLM and MLflow settings
- `app/prompts.py`: MLflow Prompt Registry loader
- `app/tools.py`: deterministic platform tool boundaries
- `app/agent.py`: Agent Framework agent construction using `OpenAIResponsesClient` against LiteLLM
- `app/workflow.py`: workflow construction using `SequentialBuilder`
- `app/a2a_claude.py`: A2A scaffold for a Claude Agent SDK-based remote specialist agent
- `../a2a-server-template/`: minimal Claude-side A2A endpoint skeleton with agent card and task lifecycle stubs
- `app/openai_client.py`: direct OpenAI SDK helper using the Responses API
- `app/agent_id_protocol.py`: pinned Agent ID protocol baseline for runtime integrations
- `app/protocols.py`: helper for choosing A2A, ACP, or ANP by use case
- `app/observability.py`: MLflow setup for tracing and OpenAI autologging
- `app/skill_registry.py`: local skill registry helpers
- `app/registry_workflow.py`: capability-gap detection workflow
- `app/evals.py`: MLflow GenAI evaluation scaffold
- `app/main.py`: local entrypoint with traced agent and workflow runs
- `tests/`: starter tests for config, runtime assembly, prompt loading, and observability setup
- `../litellm-config.yaml`: sample LiteLLM proxy configuration with aliases and fallbacks

## Expected Environment Variables

- `LITELLM_BASE_URL`
- `LITELLM_API_KEY`
- `LITELLM_MODEL`
- `MLFLOW_TRACKING_URI`
- `MLFLOW_EXPERIMENT_NAME`
- `MLFLOW_PROMPT_NAME`
- `MLFLOW_PROMPT_ALIAS`
- `MICROCLOUD_ENVIRONMENT`
- `MICROCLOUD_APPROVAL_MODE`
- `SKILL_REGISTRY_ACTIVE_PATH`
- `SKILL_REGISTRY_QUARANTINE_PATH`
- `SKILL_REGISTRY_AUTHORING_PATH`
- `OPENAI_API_KEY`
- `OPENAI_MODEL`

## Prompt Strategy

- Store the system prompt in MLflow Prompt Registry.
- Reference it via `MLFLOW_PROMPT_NAME` and `MLFLOW_PROMPT_ALIAS`.
- Keep prompt text out of application code.

## Evaluation Strategy

- Build evaluation datasets from curated cases and traced production examples.
- Use `mlflow.genai.evaluate()` as the default evaluation surface.
- Treat prompt and model changes as changes that should run through evaluation.
- Use the registry workflow to detect capability gaps before creating or importing new skills.

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python -m app.main
```

## Test

```bash
pytest
```
