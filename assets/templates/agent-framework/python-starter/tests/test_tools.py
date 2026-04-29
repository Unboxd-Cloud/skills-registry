from app.tools import MicroCloudTools


def test_microcloud_tools_return_operator_strings():
    tools = MicroCloudTools()

    assert "nominal" in tools.get_cluster_health().lower()
    assert "node-02" in tools.plan_node_join("node-02")
    assert "backup" in tools.create_change_summary("backup")
    assert "host-01" in tools.ssh_collect_remote_facts("host-01")
    assert "repo" in tools.github_search_repository("repo", "query")
    assert "image:tag" in tools.docker_inspect_image("image:tag")
    assert "svc" in tools.cloud_run_describe_service("proj", "us-central1", "svc")
    assert "workspace" in tools.vscode_read_diagnostics("workspace")
    assert "#ops" in tools.slack_post_message("#ops", "summary")
    assert "ops-room" in tools.discord_post_message("ops-room", "summary")
    assert "llama" in tools.huggingface_search_models("llama")
    assert "runbook" in tools.google_drive_search_files("runbook")
