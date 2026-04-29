import sys
import types

from app.config import Settings
from app.observability import configure_mlflow


class FakeOpenAIFlavor:
    def __init__(self):
        self.calls = []

    def autolog(self, **kwargs):
        self.calls.append(kwargs)


def test_configure_mlflow_sets_tracking_and_autolog(monkeypatch):
    openai_flavor = FakeOpenAIFlavor()
    mlflow_module = types.SimpleNamespace(
        set_tracking_uri=lambda uri: setattr(mlflow_module, "tracking_uri", uri),
        set_experiment=lambda name: setattr(mlflow_module, "experiment_name", name),
        openai=openai_flavor,
    )
    monkeypatch.setitem(sys.modules, "mlflow", mlflow_module)

    settings = Settings(
        litellm_base_url="http://localhost:4000",
        litellm_api_key="sk-test",
        litellm_model="ops-router",
        mlflow_tracking_uri="http://localhost:5000",
    )

    configure_mlflow(settings)

    assert mlflow_module.tracking_uri == "http://localhost:5000"
    assert mlflow_module.experiment_name == "canonical-microcloud-agentops"
    assert openai_flavor.calls == [{"log_traces": True}]
