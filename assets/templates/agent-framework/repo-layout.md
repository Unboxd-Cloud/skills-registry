# Microsoft Agent Framework Repo Layout

```text
agent-platform/
├── src/
│   ├── agents/
│   ├── workflows/
│   ├── tools/
│   ├── adapters/
│   ├── policies/
│   └── hosting/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── workflow/
├── infra/
│   ├── terraform/
│   └── ansible/
├── docs/
│   ├── architecture/
│   ├── runbooks/
│   └── decisions/
└── .github/workflows/
```

## Conventions

- Keep agents narrow and task-specific.
- Keep workflows deterministic and reviewable.
- Keep tool adapters thin wrappers around platform automation.
- Keep infrastructure code separate from agent runtime code.
