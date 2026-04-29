# A2A Topology With Claude Agent SDK

## Components

- Canonical MicroCloud control-plane agent runtime: Microsoft Agent Framework
- Remote specialist agent runtime: Claude Agent SDK
- Interop boundary: A2A endpoint and agent card
- Shared observability: MLflow traces and registry metadata

## Request Flow

1. A Microsoft Agent Framework agent identifies a task that should be delegated.
2. The runtime resolves the remote A2A agent card.
3. The task is submitted to the remote Claude-side agent over A2A.
4. The remote agent executes within its own permission and tool boundaries.
5. The result returns through A2A.
6. The local runtime applies approval and validation before acting on the result.

## Typical Claude-Side Roles

- migration analyst
- repo refactoring specialist
- document or prompt optimizer
- research or summarization specialist

## Guardrails

- Do not let remote output mutate infrastructure without local approval.
- Keep A2A task payloads scoped and auditable.
- Preserve trace ids and task ids across the delegation boundary.
