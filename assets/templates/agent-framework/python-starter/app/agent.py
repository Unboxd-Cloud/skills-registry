"""Microsoft Agent Framework agent wiring for Canonical MicroCloud operations via LiteLLM."""

from typing import Any

from app.config import Settings
from app.prompts import load_system_prompt
from app.tools import MicroCloudTools


class MicroCloudOperationsAgent:
    def __init__(self, settings: Settings, agent: Any):
        self.settings = settings
        self.agent = agent

    async def run(self, prompt: str, **kwargs: Any) -> Any:
        return await self.agent.run(prompt, **kwargs)


async def build_agent(settings: Settings, tools: MicroCloudTools) -> MicroCloudOperationsAgent:
    from agent_framework import AIFunction
    from agent_framework.openai import OpenAIResponsesClient

    client = OpenAIResponsesClient(
        model_id=settings.litellm_model,
        api_key=settings.litellm_api_key,
        base_url=settings.litellm_base_url,
    )

    ai_tools = [
        AIFunction(
            name="get_microcloud_cluster_health",
            description="Get a Canonical MicroCloud cluster health summary.",
            func=tools.get_cluster_health,
        ),
        AIFunction(
            name="plan_microcloud_node_join",
            description="Plan a safe Canonical MicroCloud node join.",
            approval_mode="always_require",
            func=tools.plan_node_join,
        ),
        AIFunction(
            name="create_microcloud_change_summary",
            description="Create an operator-facing change summary.",
            func=tools.create_change_summary,
        ),
        AIFunction(
            name="ssh_collect_remote_facts",
            description="Collect read-only remote facts over SSH.",
            func=tools.ssh_collect_remote_facts,
        ),
        AIFunction(
            name="github_search_repository",
            description="Search a GitHub repository for relevant code or configuration.",
            func=tools.github_search_repository,
        ),
        AIFunction(
            name="docker_inspect_image",
            description="Inspect a Docker image for migration or runtime validation.",
            func=tools.docker_inspect_image,
        ),
        AIFunction(
            name="cloud_run_describe_service",
            description="Describe a Google Cloud Run service during migration or coexistence operations.",
            func=tools.cloud_run_describe_service,
        ),
        AIFunction(
            name="vscode_read_diagnostics",
            description="Read VS Code workspace diagnostics for developer triage.",
            func=tools.vscode_read_diagnostics,
        ),
        AIFunction(
            name="slack_post_message",
            description="Prepare or send a Slack operational update.",
            func=tools.slack_post_message,
        ),
        AIFunction(
            name="discord_post_message",
            description="Prepare or send a Discord operational update.",
            func=tools.discord_post_message,
        ),
        AIFunction(
            name="huggingface_search_models",
            description="Search Hugging Face models for AI workload or evaluation use cases.",
            func=tools.huggingface_search_models,
        ),
        AIFunction(
            name="google_drive_search_files",
            description="Search Google Drive files for migration or operational artifacts.",
            func=tools.google_drive_search_files,
        ),
    ]

    agent = client.as_agent(
        name="MicroCloudOperationsAgent",
        instructions=load_system_prompt(settings),
        tools=ai_tools,
    )
    return MicroCloudOperationsAgent(settings=settings, agent=agent)
