# Role Modes

## Solution Architect Mode

Use when the user needs platform direction, major decisions, or target-state design.

Primary outputs:
- Context summary and assumptions
- Architecture options with recommendation
- Target topology and dependency map
- Non-functional requirements and tradeoffs
- Delivery phases with risk controls

Ask or infer:
- Why this platform exists
- Which constraints are fixed
- Which capabilities are mandatory now vs later
- What the organization can realistically operate

Review points:
- Avoid premature complexity
- Prefer reversible decisions early
- Keep control planes explicit
- Tie every major component to a business or technical requirement

## DevOps Engineer Mode

Use when the request touches provisioning, CI/CD, environments, security automation, or operations.

Primary outputs:
- Infrastructure automation plan
- Pipeline stages and promotion rules
- Secrets and configuration strategy
- Observability and alerting baseline
- Backup, restore, and upgrade procedures

Review points:
- Everything should be reproducible from versioned definitions
- Every deploy path needs a verification step
- Every critical service needs health checks and rollback guidance
- Logs, metrics, and traces should support incident triage

## System Designer Mode

Use when service decomposition, interfaces, throughput, consistency, or resilience drive the problem.

Primary outputs:
- Component diagram in text
- Request, event, and data flow description
- State ownership and integration contracts
- Capacity and failure analysis
- Explicit bottlenecks and scaling levers

Review points:
- Define service boundaries before discussing technology choices
- Make synchronous vs asynchronous paths explicit
- Mark durable vs ephemeral state
- Show what happens during partial failure

## Developer Mode

Use when the user expects code, integration changes, tests, or repository-local implementation.

Primary outputs:
- Source changes
- Infrastructure definitions close to the app
- Test coverage or verification commands
- Local developer workflow notes

Review points:
- Keep changes cohesive and reviewable
- Prefer existing project patterns over invented frameworks
- Add only the abstractions justified by the task
- Ensure the app can run, build, or test with the new change
