import sys
import types

import pytest

from app.agent import build_agent
from app.config import Settings
from app.tools import MicroCloudTools


class FakeAIFunction:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class FakeAgent:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    async def run(self, prompt, **kwargs):
        return {"prompt": prompt, "kwargs": kwargs}


class FakeOpenAIResponsesClient:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def as_agent(self, **kwargs):
        return FakeAgent(**kwargs)


@pytest.mark.asyncio
async def test_build_agent_assembles_litellm_backed_runtime(monkeypatch):
    monkeypatch.setitem(sys.modules, "agent_framework", types.SimpleNamespace(AIFunction=FakeAIFunction))
    monkeypatch.setitem(sys.modules, "agent_framework.openai", types.SimpleNamespace(OpenAIResponsesClient=FakeOpenAIResponsesClient))

    settings = Settings(
        litellm_base_url="http://localhost:4000",
        litellm_api_key="sk-test",
        litellm_model="ops-router",
    )

    built = await build_agent(settings, MicroCloudTools())

    assert built.settings.litellm_model == "ops-router"
    assert built.agent.kwargs["name"] == "MicroCloudOperationsAgent"
    assert len(built.agent.kwargs["tools"]) == 3
