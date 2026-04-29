"""Workflow composition using Microsoft Agent Framework with LiteLLM-backed model routing."""

from typing import Any

from app.config import Settings
from app.tools import MicroCloudTools


async def build_workflow(settings: Settings, tools: MicroCloudTools) -> Any:
    from agent_framework.openai import OpenAIResponsesClient
    from agent_framework.orchestrations import SequentialBuilder

    client = OpenAIResponsesClient(
        model_id=settings.litellm_model,
        api_key=settings.litellm_api_key,
        base_url=settings.litellm_base_url,
    )

    researcher = client.as_agent(
        name="MicroCloudResearcher",
        instructions="Gather current platform facts and summarize the operational context.",
    )
    operator = client.as_agent(
        name="MicroCloudOperator",
        instructions="Turn the gathered facts into a safe operator action plan.",
    )

    return SequentialBuilder(participants=[researcher, operator]).build()
