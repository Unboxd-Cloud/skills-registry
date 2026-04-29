"""Direct OpenAI SDK helper.

Use this only when a direct OpenAI client path is preferred over the LiteLLM gateway.
"""

from app.config import Settings


async def run_openai_response(settings: Settings, prompt: str) -> str:
    from openai import AsyncOpenAI

    client = AsyncOpenAI(api_key=settings.openai_api_key)
    response = await client.responses.create(
        model=settings.openai_model,
        input=prompt,
    )
    return response.output_text
