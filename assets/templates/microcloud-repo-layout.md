# Canonical MicroCloud Repo Layout

```text
platform/
├── docs/
│   ├── architecture/
│   ├── operations/
│   └── decisions/
├── terraform/
│   ├── modules/
│   ├── environments/
│   │   ├── lab/
│   │   ├── staging/
│   │   └── production/
│   └── versions.tf
├── ansible/
│   ├── inventories/
│   ├── group_vars/
│   ├── host_vars/
│   ├── roles/
│   └── site.yml
├── scripts/
├── .github/workflows/
└── services/
```

## Conventions

- Keep infrastructure definitions versioned with environment separation.
- Keep cluster bootstrap and day-2 operations in Ansible.
- Keep architectural decisions in short ADRs under `docs/decisions/`.
- Keep service manifests close to the services they deploy unless the repo is platform-only.
