# ANP And ACP Interoperability Topology

## Recommended Protocol Order

1. A2A for primary remote agent interoperability
2. ACP only for compatibility with existing ACP-based agents
3. ANP only for decentralized or marketplace-style agent networking

## Topology

- Microsoft Agent Framework: local control-plane runtime
- A2A: primary remote delegation path
- ACP adapter: optional compatibility boundary for legacy BeeAI or ACP agents
- ANP gateway: optional decentralized discovery and network participation boundary

## Guardrails

- Avoid running multiple protocols in the same path unless the integration need is explicit.
- Keep approval and observability consistent across protocol boundaries.
- Record protocol type, remote endpoint, and task correlation ids.
