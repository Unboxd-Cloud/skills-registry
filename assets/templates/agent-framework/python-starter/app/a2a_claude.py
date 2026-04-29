"""A2A interop scaffold for delegating to a Claude Agent SDK-based remote agent.

This template assumes the Claude-side runtime is exposed through an A2A-compliant endpoint.
"""

from typing import Any


async def build_remote_claude_a2a_agent(a2a_base_url: str, name: str = "ClaudeSpecialist") -> Any:
    from agent_framework.a2a import A2AAgent

    return A2AAgent(name=name, url=a2a_base_url)
