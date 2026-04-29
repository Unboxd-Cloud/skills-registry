# Microsoft Agent Framework Notes

As of April 28, 2026, Microsoft Agent Framework is in public preview.

Treat it as the runtime for this skill's agent layer.

## Decision Rules

- Use an **agent** when the task is open-ended, conversational, or requires tool use guided by model reasoning.
- Use a **workflow** when the process has explicit steps, control flow, approvals, or long-running orchestration.
- Use a **plain function or service** when the logic is deterministic and does not benefit from model-driven planning.

## Relevant Capabilities

- Agents for tool use and conversations.
- Workflows for sequential, concurrent, branching, and multi-agent orchestration.
- Sessions for state management.
- MCP client support for tool integration.
- Middleware for interception, policy, and telemetry hooks.
- Durable hosting through Azure Functions for long-running and resumable execution.

## Canonical MicroCloud Mapping

Use Microsoft Agent Framework as the control and orchestration runtime, not as a replacement for platform automation.

Recommended split:
- Agent Framework agent: request interpretation, planning, tool invocation, incident triage assistance, or platform operator interaction.
- Agent Framework workflow: environment provisioning flow, change approval flow, remediation pipeline, or multi-step operational runbook execution.
- Ansible/Terraform/MicroCloud CLI: actual infrastructure mutation and validation steps.
- CI/CD: build, test, package, deploy, and policy enforcement.

## Hosting Guidance

Prefer these hosting options in this order unless constraints say otherwise.

1. Azure Functions durable hosting for event-driven, resumable, or long-lived orchestrations.
2. A standard service host when the agent is synchronous and fits existing platform hosting patterns.
3. A managed service only if the user explicitly prefers that operating model.

## Design Constraints

- Keep agent count low.
- Make tool boundaries explicit.
- Keep sensitive actions behind approval or deterministic workflow steps.
- Persist state only where operationally necessary.
- Ensure every environment-changing action has verification and rollback.

## Output Expectations

When this reference is in play, produce:
- The agent and workflow boundary
- Hosting choice and why
- Tool interface list
- State model
- Approval gates
- Failure and retry behavior
- Observability and audit path
