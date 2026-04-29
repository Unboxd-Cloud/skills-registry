# Canonical MicroCloud Upgrade Plan

## Scope

- Environment:
- Current version or state:
- Target version or state:
- In-scope components:

## Preconditions

- Backup completed:
- Rollback path defined:
- Maintenance window approved:
- Compatibility review completed:

## Sequence

1. Pre-upgrade validation
2. Control-plane upgrade
3. Node or cluster component upgrade
4. Post-upgrade verification
5. Workload validation

## Validation Commands

```bash
microcloud status
ansible-playbook -i inventories/<env>/hosts.yml site.yml --tags validate
```

## Risks

- Compatibility risk:
- Recovery risk:
- Operational risk:

## Rollback

- Trigger:
- Steps:
- Evidence to capture:
