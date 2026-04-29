"""MLflow GenAI evaluation scaffold."""

from typing import Any

from app.config import Settings


def evaluate_agent_output(settings: Settings, evaluation_dataset: list[dict[str, Any]]) -> Any:
    import mlflow

    def predict_fn(inputs: dict[str, Any]) -> dict[str, Any]:
        return {
            "response": f"Stub prediction for {inputs['question']} in {settings.microcloud_environment}",
        }

    return mlflow.genai.evaluate(
        data=evaluation_dataset,
        predict_fn=predict_fn,
    )
