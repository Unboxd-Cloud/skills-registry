import sys
import types

import pytest

from app.config import Settings
from app.tools import MicroCloudTools
from app.workflow import build_workflow


class FakeParticipant:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class FakeOpenAIResponsesClient:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def as_agent(self, **kwargs):
        return FakeParticipant(**kwargs)


class FakeWorkflow:
    async def run(self, prompt):
        return {"prompt": prompt}


class FakeSequentialBuilder:
    def __init__(self, participants):
        self.participants = participants

    def build(self):
        return FakeWorkflow()


@pytest.mark.asyncio
async def test_build_workflow_returns_litellm_backed_sequential_workflow(monkeypatch):
    monkeypatch.setitem(sys.modules, "agent_framework.openai", types.SimpleNamespace(OpenAIResponsesClient=FakeOpenAIResponsesClient))
    monkeypatch.setitem(sys.modules, "agent_framework.orchestrations", types.SimpleNamespace(SequentialBuilder=FakeSequentialBuilder))

    settings = Settings(
        litellm_base_url="http://localhost:4000",
        litellm_api_key="sk-test",
        litellm_model="ops-router",
    )

    workflow = await build_workflow(settings, MicroCloudTools())
    result = await workflow.run("plan node join")

    assert result["prompt"] == "plan node join"
