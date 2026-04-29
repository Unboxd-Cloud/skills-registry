# Delivery Checklists

## Architecture Checklist

- Problem statement is explicit
- Assumptions are listed
- Constraints are named
- Topology is described
- Data paths are clear
- Failure domains are identified
- Security boundaries are defined
- Operations ownership is assigned
- Upgrade path exists
- Rollback path exists

## Environment Checklist

- Node count and roles are defined
- Network ranges and ingress/egress rules are defined
- Storage layout and replication expectations are defined
- DNS, certificates, and time sync are accounted for
- Secrets source of truth is defined
- Monitoring and alerting endpoints are chosen
- Backup targets and restore tests are planned

## CI/CD Checklist

- Build, test, package, and deploy stages are explicit
- Artifact versioning is deterministic
- Promotion rules are defined
- Environment-specific config is separated from code
- Secrets are injected securely
- Deployment verification is automated
- Rollback is scriptable

## Application Checklist

- Service boundaries are documented
- API or event contracts are named
- Data ownership is clear
- Configuration keys are listed
- Health endpoints exist where relevant
- Test strategy covers happy path and failure path
- Operational dashboards or logs support diagnosis

## Readiness Review Checklist

- Capacity assumptions are documented
- Recovery objectives are stated
- Single points of failure are acknowledged or removed
- Upgrade order is safe
- On-call or ownership path is clear
- Known risks and deferred work are visible
