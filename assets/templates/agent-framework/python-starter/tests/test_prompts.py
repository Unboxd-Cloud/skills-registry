import sys
import types

from app.config import Settings
from app.prompts import load_system_prompt


class FakePrompt:
    def format(self, **kwargs):
        return f"env={kwargs['microcloud_environment']};approval={kwargs['approval_mode']}"


def test_load_system_prompt_uses_registry_alias(monkeypatch):
    mlflow_module = types.SimpleNamespace(
        load_prompt=lambda uri: FakePrompt(),
    )
    monkeypatch.setitem(sys.modules, "mlflow", mlflow_module)

    settings = Settings(
        litellm_base_url="http://localhost:4000",
        litellm_api_key="sk-test",
        litellm_model="ops-router",
    )

    prompt = load_system_prompt(settings)

    assert prompt == "env=lab;approval=manual"
