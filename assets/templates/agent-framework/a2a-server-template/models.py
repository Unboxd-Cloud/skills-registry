from dataclasses import dataclass, field
from typing import Any


@dataclass
class SendTaskRequest:
    task_id: str
    did: str | None = None
    message: str
    context_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class TaskResponse:
    task_id: str
    did: str | None = None
    state: str
    message: str
    artifacts: list[dict[str, Any]] = field(default_factory=list)
