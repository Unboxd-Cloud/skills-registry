# Canonical MicroCloud Backup Workflow

## Objective

Run and verify a backup workflow for Canonical MicroCloud platform state and dependent workload data.

## Backup Scope

- Platform configuration:
- Workload metadata:
- Persistent data stores:
- Secret or certificate material:

## Preconditions

- Backup target is reachable.
- Retention policy is confirmed.
- Restore procedure exists.

## Commands

```bash
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags backup
microcloud status
```

## Verification

```bash
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags verify-backup
```

## Evidence To Capture

- Backup job id or artifact id
- Target location
- Verification output
- Retention window

## Failure Handling

- Mark backup status as failed.
- Preserve error output.
- Do not mark the environment protected until verification passes.
