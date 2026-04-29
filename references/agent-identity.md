# Agent ID Protocol Integration

Use this reference when the system needs to integrate with the standalone Agent ID protocol repository rather than define identity inline in this skill.

## Position

Agent identity is defined outside this skill in a separate protocol repository.

Primary external source of truth:
- `https://github.com/didoneworld/agent-id-protocol`

Pinned release for current integration baseline:
- `https://github.com/didoneworld/agent-id-protocol/releases/tag/v0.1.1`

Local working copy:
- `/Users/apple/agent-id-protocol`

This skill should consume that protocol through integration fields and bindings.

## Integration Rule

- Use W3C DID as the identity foundation.
- Store DID and binding metadata in runtime, registry, and trace records.
- Keep A2A, ACP, and ANP as bindings, not identity sources.

## Local Reference Files

- `/Users/apple/agent-id-protocol/docs/agent-id-spec.md`
- `/Users/apple/agent-id-protocol/docs/compatibility.md`
- `/Users/apple/agent-id-protocol/schemas/agent-id-record.yaml`
- `/Users/apple/agent-id-protocol/examples/a2a-agent-card.json`
