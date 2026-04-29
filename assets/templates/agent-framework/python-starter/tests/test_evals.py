import sys
import types

from app.config import Settings
from app.evals import evaluate_agent_output


def test_evaluate_agent_output_calls_mlflow_genai(monkeypatch):
    captured = {}

    def fake_evaluate(**kwargs):
        captured.update(kwargs)
        return {"status": "ok"}

    mlflow_module = types.SimpleNamespace(
        genai=types.SimpleNamespace(evaluate=fake_evaluate),
    )
    monkeypatch.setitem(sys.modules, "mlflow", mlflow_module)

    settings = Settings(
        litellm_base_url="http://localhost:4000",
        litellm_api_key="sk-test",
        litellm_model="ops-router",
    )
    dataset = [{"inputs": {"question": "hello"}, "expectations": {"answer": "world"}}]

    result = evaluate_agent_output(settings, dataset)

    assert result == {"status": "ok"}
    assert captured["data"] == dataset
    assert callable(captured["predict_fn"])
