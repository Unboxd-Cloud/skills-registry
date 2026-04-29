from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    litellm_base_url: str
    litellm_api_key: str
    litellm_model: str
    microcloud_environment: str = "lab"
    microcloud_approval_mode: str = "manual"
    mlflow_tracking_uri: str | None = None
    mlflow_experiment_name: str = "canonical-microcloud-agentops"
    mlflow_prompt_name: str = "canonical-microcloud-system"
    mlflow_prompt_alias: str = "production"
    skill_registry_active_path: str = "~/.codex/skills"
    skill_registry_quarantine_path: str = "~/.codex/skills-quarantine"
    skill_registry_authoring_path: str = "~/.codex/skills-authoring"
    openai_api_key: str | None = None
    openai_model: str = "gpt-5-mini"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            litellm_base_url=os.environ["LITELLM_BASE_URL"],
            litellm_api_key=os.environ["LITELLM_API_KEY"],
            litellm_model=os.environ["LITELLM_MODEL"],
            microcloud_environment=os.getenv("MICROCLOUD_ENVIRONMENT", "lab"),
            microcloud_approval_mode=os.getenv("MICROCLOUD_APPROVAL_MODE", "manual"),
            mlflow_tracking_uri=os.getenv("MLFLOW_TRACKING_URI"),
            mlflow_experiment_name=os.getenv("MLFLOW_EXPERIMENT_NAME", "canonical-microcloud-agentops"),
            mlflow_prompt_name=os.getenv("MLFLOW_PROMPT_NAME", "canonical-microcloud-system"),
            mlflow_prompt_alias=os.getenv("MLFLOW_PROMPT_ALIAS", "production"),
            skill_registry_active_path=os.getenv("SKILL_REGISTRY_ACTIVE_PATH", "~/.codex/skills"),
            skill_registry_quarantine_path=os.getenv("SKILL_REGISTRY_QUARANTINE_PATH", "~/.codex/skills-quarantine"),
            skill_registry_authoring_path=os.getenv("SKILL_REGISTRY_AUTHORING_PATH", "~/.codex/skills-authoring"),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
        )
