from app.config import Settings


def test_settings_from_env(monkeypatch):
    monkeypatch.setenv("LITELLM_BASE_URL", "http://localhost:4000")
    monkeypatch.setenv("LITELLM_API_KEY", "sk-test")
    monkeypatch.setenv("LITELLM_MODEL", "ops-router")
    monkeypatch.setenv("MLFLOW_TRACKING_URI", "http://localhost:5000")

    settings = Settings.from_env()

    assert settings.litellm_base_url == "http://localhost:4000"
    assert settings.litellm_api_key == "sk-test"
    assert settings.litellm_model == "ops-router"
    assert settings.mlflow_tracking_uri == "http://localhost:5000"
    assert settings.mlflow_experiment_name == "canonical-microcloud-agentops"
    assert settings.mlflow_prompt_name == "canonical-microcloud-system"
    assert settings.mlflow_prompt_alias == "production"
