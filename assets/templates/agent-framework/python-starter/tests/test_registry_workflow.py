from app.registry_workflow import SkillCapabilityWorkflow
from app.skill_registry import SkillRegistry


class FakeRegistry(SkillRegistry):
    def __init__(self):
        pass

    def search(self, query: str):
        return []

    def detect_capability_gap(self, requested_capability: str, discovered_skills):
        return type('Gap', (), {'reason': 'missing skill'})()


def test_registry_workflow_reports_gap():
    workflow = SkillCapabilityWorkflow(FakeRegistry())
    result = workflow.run('mlflow prompt optimization')

    assert result['gap_detected'] is True
    assert result['recommended_next_step'] == 'create-or-import-skill'
