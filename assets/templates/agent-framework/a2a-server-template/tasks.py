from models import TaskResponse


class TaskStore:
    def __init__(self):
        self._tasks: dict[str, TaskResponse] = {}

    def create_task(self, task_id: str, message: str, did: str | None = None) -> TaskResponse:
        task = TaskResponse(task_id=task_id, did=did, state="submitted", message=message)
        self._tasks[task_id] = task
        return task

    def complete_task(self, task_id: str, result: str) -> TaskResponse:
        task = self._tasks[task_id]
        task.state = "completed"
        task.artifacts.append({"type": "text", "text": result})
        return task

    def get_task(self, task_id: str) -> TaskResponse | None:
        return self._tasks.get(task_id)
