# Ansible Starter Notes

Use Ansible here for node preparation, cluster bootstrap orchestration, and day-2 operations.

Suggested ownership:
- Base package and OS preparation
- NTP, DNS, and certificate prerequisites
- MicroCloud bootstrap and node join sequencing
- Post-install validation and operational tasks

Suggested files:
- `inventories/<env>/hosts.yml`
- `group_vars/all.yml`
- `roles/common/`
- `roles/microcloud_bootstrap/`
- `roles/microcloud_join/`
- `roles/observability/`
- `site.yml`

Rules:
- Make sequencing explicit.
- Tag destructive or disruptive tasks.
- Add idempotent validations after each major step.
