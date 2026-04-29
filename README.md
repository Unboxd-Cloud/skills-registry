# Canonical MicroCloud Skill Registry

This repository publishes the `canonical-microcloud-platform` Codex skill.

## Purpose

The skill is designed for work across Canonical MicroCloud architecture, DevOps, system design, platform delivery, migration, and agent-runtime integration.

It helps Codex act as a:
- solution architect
- DevOps engineer
- system designer
- developer

## What Is Included

- `SKILL.md`: skill metadata and execution guidance
- `references/`: focused reference documents for runtime, identity, interoperability, observability, migration, and operations
- `assets/templates/`: reusable templates for migration plans, runbooks, cost optimization, upgrade planning, A2A, Agent Framework, and self-improving skill registry operations
- `agents/openai.yaml`: UI metadata for skill discovery

## Major Integration Areas

- Canonical MicroCloud platform design and operations
- Microsoft Agent Framework runtime patterns
- LiteLLM model gateway integration
- MLflow observability, prompt management, and evaluation
- Agent interoperability with A2A, ACP, and ANP guidance
- DID-based Agent ID protocol integration
- Migration planning from AWS, OpenStack, GCP, Azure, and on-prem environments

## Repository Layout

```text
.
├── SKILL.md
├── agents/
├── references/
└── assets/templates/
```

## Related Protocol Repository

The DID-based Agent ID protocol used by this skill is published separately:
- https://github.com/didoneworld/agent-id-protocol

## Source Of Truth

This repository is the GitHub-published copy of the local skill used under `~/.codex/skills/canonical-microcloud-platform`.
