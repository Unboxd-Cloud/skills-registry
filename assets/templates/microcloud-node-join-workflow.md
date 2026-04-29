# Canonical MicroCloud Node Join Workflow

## Objective

Join a new node to an existing Canonical MicroCloud cluster with explicit preflight, approval, and post-change verification.

## Preconditions

- Cluster is healthy before the change.
- New node passed OS, network, and storage preparation.
- Node identity and placement are approved.

## Inputs

- Environment name:
- Existing cluster endpoint:
- Joining node name:
- Expected role:
- Approval reference:

## Preflight Commands

```bash
microcloud status
lxc list
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags preflight-node --limit <node> --check
```

## Join Commands

```bash
microcloud add <node>
microcloud status
```

## Post-Join Validation

```bash
microcloud status
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags validate-node --limit <node>
```

## Evidence To Capture

- Join approval
- Cluster health before and after
- Node status after join
- Alerts generated during the window

## Rollback Or Containment

- If the join fails, isolate the node from further automation.
- Do not retry blindly; rerun preflight first.
- Escalate if cluster health regresses after the join.
