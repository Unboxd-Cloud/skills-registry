"""MLflow Prompt Registry helpers."""

from app.config import Settings


def load_system_prompt(settings: Settings) -> str:
    import mlflow

    prompt = mlflow.load_prompt(f"prompts:/{settings.mlflow_prompt_name}@{settings.mlflow_prompt_alias}")
    return prompt.format(
        microcloud_environment=settings.microcloud_environment,
        approval_mode=settings.microcloud_approval_mode,
    )
