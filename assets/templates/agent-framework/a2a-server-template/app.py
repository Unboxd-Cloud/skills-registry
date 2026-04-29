"""Minimal HTTP skeleton for an A2A-facing remote agent service.

Replace the placeholder transport with the exact A2A binding and Claude Agent SDK
execution path you standardize on.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from uuid import uuid4

from models import SendTaskRequest
from tasks import TaskStore


TASKS = TaskStore()
AGENT_CARD_PATH = "/.well-known/agent-card.json"
TASK_SUBMIT_PATH = "/a2a/tasks/send"
TASK_GET_PREFIX = "/a2a/tasks/"


class A2AHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == AGENT_CARD_PATH:
            with open("agent_card.json", "r", encoding="utf-8") as f:
                self._send_json(200, json.load(f))
            return

        if self.path.startswith(TASK_GET_PREFIX):
            task_id = self.path.removeprefix(TASK_GET_PREFIX)
            task = TASKS.get_task(task_id)
            if task is None:
                self._send_json(404, {"error": "task_not_found"})
                return
            self._send_json(200, task.__dict__)
            return

        self._send_json(404, {"error": "not_found"})

    def do_POST(self):
        if self.path != TASK_SUBMIT_PATH:
            self._send_json(404, {"error": "not_found"})
            return

        length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(length) or b"{}")
        request = SendTaskRequest(
            task_id=payload.get("task_id", str(uuid4())),
            message=payload["message"],
            context_id=payload.get("context_id"),
            metadata=payload.get("metadata", {}),
            did=payload.get("did"),
        )
        task = TASKS.create_task(request.task_id, request.message, request.did)

        # Replace this placeholder completion path with real Claude Agent SDK execution.
        completed = TASKS.complete_task(request.task_id, f"Handled by remote Claude-side agent: {request.message}")
        self._send_json(202, completed.__dict__)


def main():
    server = HTTPServer(("127.0.0.1", 8080), A2AHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
