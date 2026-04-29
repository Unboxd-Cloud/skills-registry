# Cost Optimization, Upgrade, And On-Prem Migration Notes

Use this reference when the Canonical MicroCloud platform work includes cloud cost control, infrastructure upgrades, or migration from on-prem environments.

## Cloud Cost Optimization

Focus on durable cost levers rather than one-off cuts.

- Rightsize compute, storage, and network allocations.
- Reduce idle environments and orphaned resources.
- Prefer policy-driven shutdown schedules for non-production capacity.
- Track cost by environment, tenant, and platform service.
- Measure the cost of observability, backups, and cross-zone traffic.
- Treat model gateway routing and LLM usage as first-class cost surfaces.

## Infrastructure Upgradation

Treat upgrades as controlled platform changes, not package churn.

- Define current state, target state, and blocked upgrade paths.
- Separate control-plane upgrades from workload changes.
- Validate compatibility for storage, networking, identity, and automation.
- Keep rollback, hold points, and maintenance windows explicit.
- Run pre-upgrade and post-upgrade health checks.

## On-Prem Migration

Assume `op` means `on-prem` unless the user clarifies otherwise.

- Inventory workloads, dependencies, data stores, and operational constraints.
- Classify what can be rehosted, refactored, replaced, or retired.
- Migrate data and state with rollback-aware sequencing.
- Define cutover, coexistence, and decommission steps.
- Plan for bandwidth, latency, identity federation, and backup continuity.

## Output Expectations

When this reference is in play, produce:
- cost baseline and optimization levers
- upgrade sequence and validation plan
- migration phases, cutover plan, and rollback path
