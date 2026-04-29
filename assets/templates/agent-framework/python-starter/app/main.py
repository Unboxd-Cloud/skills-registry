import asyncio

from app.agent import build_agent
from app.config import Settings
from app.evals import evaluate_agent_output
from app.observability import configure_mlflow
from app.registry_workflow import SkillCapabilityWorkflow
from app.skill_registry import SkillRegistry
from app.tools import MicroCloudTools
from app.workflow import build_workflow


async def _run_agent(agent, prompt: str):
    import mlflow

    traced = mlflow.trace(
        agent.run,
        name="microcloud-agent-run",
        span_type="agent",
        attributes={"operation": "agent_run"},
    )
    return await traced(prompt)


async def _run_workflow(workflow, prompt: str):
    import mlflow

    traced = mlflow.trace(
        workflow.run,
        name="microcloud-workflow-run",
        span_type="workflow",
        attributes={"operation": "workflow_run"},
    )
    return await traced(prompt)


async def main() -> None:
    settings = Settings.from_env()
    configure_mlflow(settings)

    tools = MicroCloudTools()
    agent = await build_agent(settings, tools)
    workflow = await build_workflow(settings, tools)

    agent_result = await _run_agent(agent, "Summarize current Canonical MicroCloud readiness.")
    workflow_result = await _run_workflow(workflow, "Prepare a safe node-join plan for node-02.")

    print(agent_result)
    print(workflow_result)

    registry = SkillRegistry(
        active_path=settings.skill_registry_active_path,
        quarantine_path=settings.skill_registry_quarantine_path,
        authoring_path=settings.skill_registry_authoring_path,
    )
    capability_workflow = SkillCapabilityWorkflow(registry)
    capability_result = capability_workflow.run("mlflow prompt optimization")
    print(capability_result)

    sample_dataset = [
        {"inputs": {"question": "Is the cluster healthy?"}, "expectations": {"answer": "healthy"}},
    ]
    evaluate_agent_output(settings, sample_dataset)


if __name__ == "__main__":
    asyncio.run(main())
