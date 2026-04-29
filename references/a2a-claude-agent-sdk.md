# A2A With Claude Agent SDK

Use this reference when Canonical MicroCloud platform work needs Microsoft Agent Framework agents to interoperate with a Claude Agent SDK-based agent system.

## Integration Model

Treat A2A as the interoperability boundary.

- Microsoft Agent Framework can expose or consume A2A agents.
- Claude Agent SDK provides the agent runtime, tools, permissions, sessions, and MCP extensibility on the Anthropic side.
- The cross-framework connection should happen through an A2A-compliant HTTP endpoint and agent card, not through framework-private assumptions.

This is an architectural inference from the current docs:
- Anthropic documents Claude Agent SDK runtime capabilities.
- Microsoft documents A2A support and a Python `A2AAgent` wrapper for remote A2A agents.

## Recommended Pattern

1. Build the Claude-side agent with Claude Agent SDK.
2. Expose that Claude-side agent through an A2A-compliant service boundary.
3. Consume it from Microsoft Agent Framework using A2A discovery and a remote A2A agent wrapper.
4. Keep tool permissions and destructive actions enforced on both sides.

## Why Use This Pattern

- Cross-framework interoperability
- Clear discovery via agent cards
- Support for long-running tasks and remote delegation
- Decoupling between Claude-side agent runtime and MicroCloud control-plane runtime

## Operational Rules

- Use A2A for cross-boundary delegation, not for every internal call.
- Keep the Claude-side agent narrow and role-specific.
- Record remote agent id, task id, and endpoint in traces.
- Apply approval gates before any environment-changing action returned by the remote agent.

## Output Expectations

When this reference is in play, produce:
- remote agent role and boundary
- A2A endpoint and agent card expectations
- task routing model
- approval and traceability model
