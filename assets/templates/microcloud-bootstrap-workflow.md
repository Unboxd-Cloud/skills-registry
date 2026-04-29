# Canonical MicroCloud Bootstrap Workflow

## Objective

Bootstrap a new Canonical MicroCloud cluster safely and capture the validation evidence required for handoff.

## Preconditions

- Nodes are provisioned and reachable.
- DNS and NTP are working.
- Storage devices are identified.
- Required packages and OS baseline are present.
- Maintenance window and operator approval are recorded.

## Inputs

- Environment name:
- Primary bootstrap node:
- Additional nodes:
- Cluster network range:
- Storage configuration:
- Approval reference:

## Preflight Commands

```bash
microcloud status
lxc cluster list
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags preflight --check
```

## Bootstrap Commands

```bash
microcloud init
microcloud status
```

## Post-Bootstrap Validation

```bash
microcloud status
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags validate
```

## Evidence To Capture

- Bootstrap command transcript
- Cluster health output
- Node inventory
- Storage and network summary

## Rollback Or Containment

- Stop before node joins if validation fails.
- Preserve logs and cluster status output.
- Revert host preparation changes only through approved automation.
