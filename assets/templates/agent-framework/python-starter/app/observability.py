"""MLflow-based agent observability setup."""

from app.config import Settings


def configure_mlflow(settings: Settings) -> None:
    import mlflow

    if settings.mlflow_tracking_uri:
        mlflow.set_tracking_uri(settings.mlflow_tracking_uri)

    mlflow.set_experiment(settings.mlflow_experiment_name)
    mlflow.openai.autolog(log_traces=True)
