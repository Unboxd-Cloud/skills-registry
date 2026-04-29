# ANP And ACP Notes

Use this reference when the Canonical MicroCloud platform needs additional agent interoperability patterns beyond A2A.

## ACP Status

As of April 28, 2026:
- ACP is an agent interoperability protocol introduced by IBM BeeAI.
- ACP has merged into A2A under the Linux Foundation umbrella.
- Treat ACP mainly as a legacy or coexistence protocol for systems that already expose ACP endpoints.

Recommended position:
- Prefer A2A for new cross-agent interoperability work.
- Add ACP only when a required external agent or platform already depends on ACP.

## ANP Position

ANP is a separate agent networking protocol oriented around decentralized identity, discovery, and agent-to-agent networking.

Recommended position:
- Use ANP only when the system genuinely needs decentralized agent identity, marketplace-style discovery, or open network participation.
- Do not introduce ANP for ordinary internal platform orchestration.

## Architectural Guidance

- `A2A`: primary protocol for remote agent interoperability
- `ACP`: compatibility layer for BeeAI or existing ACP-based agents
- `ANP`: optional decentralized networking layer for open agent ecosystems

## Output Expectations

When this reference is in play, produce:
- protocol selection rationale
- compatibility boundary
- discovery and identity model
- approval and risk implications


## Identity Boundary

Do not treat ACP, A2A, or ANP identifiers as the platform's primary identity model. Bind them to the DID-based Agent ID protocol or another future identity protocol through a mapping layer.
