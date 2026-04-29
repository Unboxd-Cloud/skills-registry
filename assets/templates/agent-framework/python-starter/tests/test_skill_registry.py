from pathlib import Path

from app.skill_registry import SkillRegistry


def test_registry_detects_capability_gap(tmp_path: Path):
    active = tmp_path / 'active'
    quarantine = tmp_path / 'quarantine'
    authoring = tmp_path / 'authoring'
    active.mkdir()
    quarantine.mkdir()
    authoring.mkdir()

    registry = SkillRegistry(str(active), str(quarantine), str(authoring))
    results = registry.search('prompt optimization')
    gap = registry.detect_capability_gap('prompt optimization', results)

    assert results == []
    assert gap is not None
    assert 'prompt optimization' in gap.reason
