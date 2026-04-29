# Canonical MicroCloud Tool Adapter Specification

Use this reference when implementing Microsoft Agent Framework tools for Canonical MicroCloud operations.

## Adapter Design Rules

- Keep adapters thin and deterministic.
- Each adapter should wrap one execution boundary cleanly.
- Return structured results with stdout, stderr, exit code, summary, and approval requirements.
- Separate read-only actions from mutating actions.
- Require explicit approval for mutating or disruptive operations.
- Add timeouts, retries only where safe, and redacted logging.

## Common Result Shape

```json
{
  "tool": "string",
  "action": "string",
  "status": "ok|error|approval_required",
  "summary": "short human-readable outcome",
  "stdout": "captured output or normalized data",
  "stderr": "captured errors",
  "exit_code": 0,
  "requires_approval": false,
  "rollback_hint": "what to do if this change fails"
}
```

## `microcloud` Adapter

Purpose:
- Cluster bootstrap
- Node join sequencing
- Cluster status and readiness checks
- Storage and network configuration inspection

Read-only actions:
- `cluster_status`
- `node_status`
- `storage_status`
- `network_status`

Mutating actions:
- `bootstrap_cluster`
- `join_node`
- `reconfigure_cluster`

Rules:
- Never combine bootstrap and join in one tool action.
- Require preflight validation before `bootstrap_cluster` and `join_node`.
- Return explicit rollback or containment guidance for every mutating action.

## `lxc` Adapter

Purpose:
- Inspect or manage local virtualization resources backing the environment.
- Support diagnostics, image checks, and container or VM state inspection.

Read-only actions:
- `list_instances`
- `instance_info`
- `list_images`
- `exec_readonly`

Mutating actions:
- `launch_instance`
- `stop_instance`
- `delete_instance`
- `exec_mutation`

Rules:
- Distinguish read-only exec from mutation exec.
- Require approval for destructive instance operations.
- Normalize instance identity and target environment in every result.

## `ansible` Adapter

Purpose:
- Node preparation
- Cluster bootstrap orchestration
- Day-2 operational procedures
- Post-change verification

Read-only actions:
- `check_inventory`
- `dry_run_playbook`
- `gather_facts`

Mutating actions:
- `run_playbook`
- `run_tagged_playbook`

Rules:
- Prefer tagged playbook execution over free-form command invocation.
- Always support `--check` style validation before live execution when feasible.
- Return changed hosts, failed hosts, and next recovery step.

## `terraform` Adapter

Purpose:
- Environment-adjacent infrastructure provisioning
- DNS, load balancer, secret backend, or external service provisioning

Read-only actions:
- `fmt_check`
- `validate`
- `plan`
- `show_state_summary`

Mutating actions:
- `apply`
- `destroy`

Rules:
- Never call `apply` without a prior `plan` artifact.
- Require approval for `apply` and always for `destroy`.
- Persist plan metadata or a plan identifier for auditability.

## Approval Policy

Require explicit human approval for:
- Cluster bootstrap
- Node join or removal
- Storage reconfiguration
- Network reconfiguration
- Terraform apply or destroy
- Ansible playbooks that mutate production-like environments
- Any `lxc` destructive action

## Suggested Microsoft Agent Framework Tool Boundaries

- `get_microcloud_cluster_status()`
- `plan_microcloud_node_join(node_name)`
- `bootstrap_microcloud_cluster(preflight_profile)`
- `list_lxc_instances()`
- `run_ansible_check(playbook, inventory, tags=None)`
- `run_ansible_apply(playbook, inventory, tags=None)`
- `terraform_plan(environment)`
- `terraform_apply(environment, plan_id)`

## Observability Requirements

Each adapter invocation should emit:
- Correlation id
- Environment name
- Actor type: agent, workflow, CI, or human operator
- Tool name and action
- Start and finish timestamps
- Approval decision if applicable

## `ssh` Adapter

Purpose:
- Remote diagnostics
- Remote command execution for validated operational procedures
- Controlled host inspection during migration or incident response

Read-only actions:
- `run_readonly_command`
- `collect_remote_facts`
- `check_connectivity`

Mutating actions:
- `run_remote_change`
- `transfer_artifact`

Rules:
- Prefer read-only collection before remote mutation.
- Require approval for any mutating remote action.
- Record host, user, command class, and correlation id.

## `github` Adapter

Purpose:
- Repository inspection
- Issue, PR, and workflow coordination
- Controlled change publication

Read-only actions:
- `search_repository`
- `read_issue`
- `read_pull_request`
- `list_workflows`

Mutating actions:
- `create_branch`
- `open_pull_request`
- `comment_on_issue`
- `dispatch_workflow`

Rules:
- Keep repository writes explicit and reviewable.
- Prefer PR creation over direct default-branch mutation.
- Record repo, branch, PR id, and workflow run id when relevant.

## `docker` Adapter

Purpose:
- Build, inspect, run, and validate containerized components
- Package operational utilities and migration tooling

Read-only actions:
- `list_images`
- `list_containers`
- `inspect_image`
- `inspect_container`
- `show_logs`

Mutating actions:
- `build_image`
- `run_container`
- `stop_container`
- `remove_container`
- `push_image`

Rules:
- Prefer deterministic builds with tagged images.
- Require approval for pushes to shared registries.
- Record image tag, container id, and registry target.

## `google_cloud_run` Adapter

Purpose:
- Inspect or manage Cloud Run services during migration from GCP or coexistence operations.
- Validate service configuration and rollout state.

Read-only actions:
- `list_services`
- `describe_service`
- `list_revisions`
- `read_logs`

Mutating actions:
- `deploy_service`
- `update_service`
- `shift_traffic`
- `delete_service`

Rules:
- Treat traffic shifts as approval-gated production changes.
- Record project, region, service, revision, and traffic split.
- Use this adapter mainly for migration discovery, coexistence, and controlled cutover work.

## `vs_code` Adapter

Purpose:
- Workspace-aware editor automation
- File, search, and diagnostics coordination inside the developer environment
- Controlled developer assistance flows

Read-only actions:
- `search_workspace`
- `read_diagnostics`
- `list_open_files`

Mutating actions:
- `open_file`
- `apply_workspace_edit`
- `trigger_task`

Rules:
- Keep edits reviewable and scoped.
- Prefer repository-local changes over editor-only state changes.
- Record workspace path, file targets, and task identifiers.

## `slack` Adapter

Purpose:
- Read operational context from Slack
- Draft or send updates, approvals, and incident coordination messages

Read-only actions:
- `read_channel_context`
- `read_thread`
- `search_messages`

Mutating actions:
- `post_message`
- `reply_in_thread`
- `create_canvas`

Rules:
- Treat message sends as externally visible changes.
- Keep incident and approval messages concise and auditable.
- Record channel, thread, and message identifiers.

## `discord` Adapter

Purpose:
- Read or send collaboration updates in Discord communities or internal guilds
- Coordinate operational status where Discord is part of the workflow

Read-only actions:
- `read_channel_context`
- `read_thread`
- `search_messages`

Mutating actions:
- `post_message`
- `reply_in_thread`

Rules:
- Treat Discord sends as externally visible changes.
- Avoid posting sensitive infrastructure details without approval.
- Record guild, channel, thread, and message identifiers.

## `huggingface` Adapter

Purpose:
- Inspect models, datasets, Spaces, and inference-related assets
- Coordinate model packaging or evaluation inputs for AI workloads

Read-only actions:
- `search_models`
- `search_datasets`
- `read_model_card`
- `read_dataset_card`

Mutating actions:
- `create_repo`
- `upload_artifact`
- `trigger_job`

Rules:
- Keep model and dataset provenance explicit.
- Record repository id, model id, dataset id, and job identifiers.
- Require approval for artifact publication to shared or public destinations.

## `google_drive` Adapter

Purpose:
- Read or store migration artifacts, runbooks, reports, and shared operational documents
- Coordinate document exchange where Drive is the system of record

Read-only actions:
- `search_files`
- `read_document_metadata`
- `export_document`

Mutating actions:
- `upload_file`
- `create_folder`
- `share_document`
- `update_document`

Rules:
- Keep sharing boundaries explicit.
- Record drive id, folder id, document id, and export target.
- Require approval before sharing outside the expected tenant or group.
