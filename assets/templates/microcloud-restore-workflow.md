# Canonical MicroCloud Restore Workflow

## Objective

Restore Canonical MicroCloud platform state or workload data from a known-good backup with explicit validation and containment steps.

## Preconditions

- Restore source is verified.
- Recovery objective and impact window are approved.
- Roll-forward and rollback expectations are documented.

## Inputs

- Environment name:
- Backup artifact id:
- Restore scope:
- Approval reference:

## Commands

```bash
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags restore
microcloud status
```

## Post-Restore Validation

```bash
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags verify-restore
microcloud status
```

## Evidence To Capture

- Restore approval
- Artifact id used
- Validation output
- Remaining issues or manual cleanup tasks

## Failure Handling

- Freeze further changes until environment state is understood.
- Capture diagnostics before retrying.
- Escalate if restored services remain degraded.
